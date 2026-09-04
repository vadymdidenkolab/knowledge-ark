#!/usr/bin/env python3
"""Offline-only inventory, fixity verification and local search.

The tool never downloads content and never upgrades a file's safety, legal or
content-review status. It follows no symlinks and uses only Python's standard
library so that the seed kit remains portable.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import html
from html.parser import HTMLParser
import mimetypes
from pathlib import Path
import re
import sqlite3
import sys
import tempfile
from typing import Iterable


TEXT_SUFFIXES = {
    ".md",
    ".markdown",
    ".txt",
    ".csv",
    ".tsv",
    ".html",
    ".htm",
    ".json",
    ".xml",
    ".yaml",
    ".yml",
    ".rst",
    ".ini",
    ".toml",
    ".py",
    ".js",
    ".css",
    ".svg",
}

LOCK_FIELDS = [
    "relative_path",
    "byte_size",
    "mtime_ns_observed",
    "sha256",
    "media_type",
    "index_mode",
]


class VisibleHTML(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.parts: list[str] = []
        self.suppressed = 0

    def handle_starttag(self, tag: str, attrs) -> None:  # noqa: ANN001
        if tag.lower() in {"script", "style", "noscript", "svg"}:
            self.suppressed += 1

    def handle_endtag(self, tag: str) -> None:
        if tag.lower() in {"script", "style", "noscript", "svg"} and self.suppressed:
            self.suppressed -= 1

    def handle_data(self, data: str) -> None:
        if not self.suppressed:
            cleaned = " ".join(data.split())
            if cleaned:
                self.parts.append(cleaned)

    def text(self) -> str:
        return "\n".join(self.parts)


def safe_root(value: str) -> Path:
    root = Path(value).expanduser().resolve()
    if not root.is_dir():
        raise ValueError(f"library root is not a directory: {root}")
    return root


def iter_files(root: Path, excluded: Iterable[Path] = ()) -> Iterable[Path]:
    excluded_resolved = {path.resolve() for path in excluded if path.exists()}
    for path in sorted(root.rglob("*"), key=lambda item: item.as_posix()):
        if path.is_symlink():
            continue
        if not path.is_file():
            continue
        try:
            resolved = path.resolve()
        except OSError:
            continue
        if resolved in excluded_resolved:
            continue
        try:
            resolved.relative_to(root)
        except ValueError:
            continue
        yield path


def sha256_file(path: Path, block_size: int = 1024 * 1024) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        while True:
            block = handle.read(block_size)
            if not block:
                break
            digest.update(block)
    return digest.hexdigest()


def index_mode(path: Path) -> str:
    return "FULL_TEXT" if path.suffix.lower() in TEXT_SUFFIXES else "METADATA_ONLY"


def lock_row(root: Path, path: Path) -> dict[str, str]:
    stat = path.stat()
    media_type = mimetypes.guess_type(path.name)[0] or "application/octet-stream"
    return {
        "relative_path": path.relative_to(root).as_posix(),
        "byte_size": str(stat.st_size),
        "mtime_ns_observed": str(stat.st_mtime_ns),
        "sha256": sha256_file(path),
        "media_type": media_type,
        "index_mode": index_mode(path),
    }


def atomic_csv(path: Path, rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile(
        "w", encoding="utf-8", newline="", dir=path.parent, delete=False
    ) as handle:
        temp_path = Path(handle.name)
        writer = csv.DictWriter(handle, fieldnames=LOCK_FIELDS, quoting=csv.QUOTE_ALL)
        writer.writeheader()
        writer.writerows(rows)
    temp_path.replace(path)


def command_inventory(args: argparse.Namespace) -> int:
    root = safe_root(args.root)
    output = Path(args.output).expanduser().resolve()
    rows = [lock_row(root, path) for path in iter_files(root, [output])]
    atomic_csv(output, rows)
    total_bytes = sum(int(row["byte_size"]) for row in rows)
    print(f"inventory_ok files={len(rows)} bytes={total_bytes} output={output}")
    return 0


def read_lock(path: Path) -> dict[str, dict[str, str]]:
    with path.open("r", encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        if list(reader.fieldnames or []) != LOCK_FIELDS:
            raise ValueError(f"unexpected lock schema in {path}")
        rows = list(reader)
    by_path: dict[str, dict[str, str]] = {}
    for row in rows:
        relative = row["relative_path"]
        if relative in by_path:
            raise ValueError(f"duplicate relative_path in lock: {relative}")
        by_path[relative] = row
    return by_path


def command_verify(args: argparse.Namespace) -> int:
    root = safe_root(args.root)
    lock_path = Path(args.lock).expanduser().resolve()
    expected = read_lock(lock_path)
    actual_paths = {
        path.relative_to(root).as_posix(): path
        for path in iter_files(root, [lock_path])
    }
    missing = sorted(set(expected) - set(actual_paths))
    extra = sorted(set(actual_paths) - set(expected))
    size_mismatch: list[str] = []
    hash_mismatch: list[str] = []
    verified = 0
    for relative in sorted(set(expected) & set(actual_paths)):
        path = actual_paths[relative]
        if str(path.stat().st_size) != expected[relative]["byte_size"]:
            size_mismatch.append(relative)
            continue
        if sha256_file(path) != expected[relative]["sha256"]:
            hash_mismatch.append(relative)
            continue
        verified += 1

    for label, values in [
        ("MISSING", missing),
        ("EXTRA", extra),
        ("SIZE_MISMATCH", size_mismatch),
        ("HASH_MISMATCH", hash_mismatch),
    ]:
        for value in values:
            print(f"{label}\t{value}")

    extra_failure = bool(extra) and not args.allow_extra
    failed = bool(missing or size_mismatch or hash_mismatch or extra_failure)
    print(
        "verify_summary "
        f"verified={verified} missing={len(missing)} extra={len(extra)} "
        f"size_mismatch={len(size_mismatch)} hash_mismatch={len(hash_mismatch)} "
        f"result={'FAIL' if failed else 'PASS'}"
    )
    return 1 if failed else 0


def decode_text(path: Path, max_bytes: int) -> tuple[str, str]:
    if path.suffix.lower() not in TEXT_SUFFIXES:
        return "", "METADATA_ONLY"
    size = path.stat().st_size
    if size > max_bytes:
        return "", "SKIPPED_TOO_LARGE"
    raw = path.read_bytes()
    text = raw.decode("utf-8", errors="replace")
    if path.suffix.lower() in {".html", ".htm"}:
        parser = VisibleHTML()
        parser.feed(text)
        text = parser.text()
    elif path.suffix.lower() == ".svg":
        parser = VisibleHTML()
        parser.feed(text)
        text = parser.text()
    text = html.unescape(text).replace("\x00", " ")
    return text, "FULL_TEXT"


def create_index_schema(connection: sqlite3.Connection) -> None:
    connection.execute("PRAGMA journal_mode=DELETE")
    connection.execute("PRAGMA synchronous=FULL")
    connection.execute(
        """
        CREATE TABLE documents (
            document_id INTEGER PRIMARY KEY,
            relative_path TEXT NOT NULL UNIQUE,
            byte_size INTEGER NOT NULL,
            sha256 TEXT NOT NULL,
            media_type TEXT NOT NULL,
            index_mode TEXT NOT NULL,
            title TEXT NOT NULL,
            body TEXT NOT NULL
        )
        """
    )
    connection.execute(
        """
        CREATE VIRTUAL TABLE documents_fts USING fts5(
            relative_path,
            title,
            body,
            content='documents',
            content_rowid='document_id',
            tokenize='unicode61 remove_diacritics 2'
        )
        """
    )
    connection.executescript(
        """
        CREATE TRIGGER documents_ai AFTER INSERT ON documents BEGIN
          INSERT INTO documents_fts(rowid, relative_path, title, body)
          VALUES (new.document_id, new.relative_path, new.title, new.body);
        END;
        CREATE TRIGGER documents_ad AFTER DELETE ON documents BEGIN
          INSERT INTO documents_fts(documents_fts, rowid, relative_path, title, body)
          VALUES ('delete', old.document_id, old.relative_path, old.title, old.body);
        END;
        CREATE TRIGGER documents_au AFTER UPDATE ON documents BEGIN
          INSERT INTO documents_fts(documents_fts, rowid, relative_path, title, body)
          VALUES ('delete', old.document_id, old.relative_path, old.title, old.body);
          INSERT INTO documents_fts(rowid, relative_path, title, body)
          VALUES (new.document_id, new.relative_path, new.title, new.body);
        END;
        """
    )


def command_index(args: argparse.Namespace) -> int:
    root = safe_root(args.root)
    database = Path(args.database).expanduser().resolve()
    database.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile(dir=database.parent, delete=False) as handle:
        temp_path = Path(handle.name)
    temp_path.unlink()
    connection = sqlite3.connect(temp_path)
    try:
        create_index_schema(connection)
        file_count = 0
        full_text_count = 0
        for path in iter_files(root, [database, temp_path]):
            relative = path.relative_to(root).as_posix()
            body, mode = decode_text(path, args.max_text_bytes)
            stat = path.stat()
            media_type = mimetypes.guess_type(path.name)[0] or "application/octet-stream"
            title = path.stem.replace("_", " ").replace("-", " ")
            connection.execute(
                """
                INSERT INTO documents
                (relative_path, byte_size, sha256, media_type, index_mode, title, body)
                VALUES (?, ?, ?, ?, ?, ?, ?)
                """,
                (relative, stat.st_size, sha256_file(path), media_type, mode, title, body),
            )
            file_count += 1
            full_text_count += mode == "FULL_TEXT"
        connection.commit()
        result = connection.execute("PRAGMA integrity_check").fetchone()
        if not result or result[0] != "ok":
            raise RuntimeError(f"SQLite integrity_check failed: {result}")
    finally:
        connection.close()
    temp_path.replace(database)
    print(
        f"index_ok files={file_count} full_text={full_text_count} "
        f"metadata_only={file_count - full_text_count} database={database}"
    )
    return 0


def safe_fts_query(value: str) -> str:
    tokens = re.findall(r"[^\W_]+", value, flags=re.UNICODE)
    if not tokens:
        raise ValueError("search query contains no searchable words")
    return " AND ".join('"' + token.replace('"', '""') + '"' for token in tokens)


def command_search(args: argparse.Namespace) -> int:
    database = Path(args.database).expanduser().resolve()
    if not database.is_file():
        raise ValueError(f"database does not exist: {database}")
    query = safe_fts_query(args.query)
    uri = f"file:{database.as_posix()}?mode=ro"
    connection = sqlite3.connect(uri, uri=True)
    try:
        rows = connection.execute(
            """
            SELECT d.relative_path,
                   bm25(documents_fts) AS score,
                   snippet(documents_fts, 2, '[', ']', ' … ', 18) AS excerpt
            FROM documents_fts
            JOIN documents AS d ON d.document_id = documents_fts.rowid
            WHERE documents_fts MATCH ?
            ORDER BY score
            LIMIT ?
            """,
            (query, args.limit),
        ).fetchall()
    finally:
        connection.close()
    for relative_path, score, excerpt in rows:
        cleaned = " ".join((excerpt or "").split())
        print(f"{relative_path}\t{score:.6f}\t{cleaned}")
    print(f"search_summary results={len(rows)} query={args.query!r}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Offline inventory, fixity verification and local full-text search"
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    inventory = subparsers.add_parser(
        "inventory",
        help="create a sorted SHA-256 snapshot CSV with observed file metadata",
    )
    inventory.add_argument("root", help="library root")
    inventory.add_argument("--output", required=True, help="output CSV path")
    inventory.set_defaults(func=command_inventory)

    verify = subparsers.add_parser("verify", help="verify a root against an inventory lock")
    verify.add_argument("root", help="library root")
    verify.add_argument("lock", help="lock CSV created by inventory")
    verify.add_argument("--allow-extra", action="store_true", help="do not fail on unlisted extra files")
    verify.set_defaults(func=command_verify)

    index = subparsers.add_parser("index", help="build an offline SQLite FTS5 index")
    index.add_argument("root", help="library root")
    index.add_argument("database", help="output SQLite database")
    index.add_argument(
        "--max-text-bytes",
        type=int,
        default=16 * 1024 * 1024,
        help="maximum size of one text file to index (default: 16 MiB)",
    )
    index.set_defaults(func=command_index)

    search = subparsers.add_parser("search", help="search an existing offline index")
    search.add_argument("database", help="SQLite database created by index")
    search.add_argument("query", help="words to search; all words must match")
    search.add_argument("--limit", type=int, default=20)
    search.set_defaults(func=command_search)
    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    try:
        return int(args.func(args))
    except (OSError, ValueError, sqlite3.Error, RuntimeError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
