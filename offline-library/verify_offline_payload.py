#!/usr/bin/env python3
"""Fail-closed verifier for the offline-library payload register.

The always-available checks use only the Python standard library.  If pdfinfo
or hdiutil is installed, the verifier also repeats the external format checks.
"""

from __future__ import annotations

import csv
import hashlib
import os
import re
import shutil
import subprocess
import sys
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parent
REGISTER = ROOT / "offline-payload-register.csv"
PAYLOAD_ROOTS = (
    "released",
    "candidate",
    "quarantine",
    "superseded",
    "private-licensed",
    "readers",
)
REQUIRED_DIRS = PAYLOAD_ROOTS + ("metadata",)
EXPECTED_COLUMNS = (
    "payload_id",
    "relative_path",
    "title",
    "publisher",
    "edition_date",
    "language",
    "audience",
    "canonical_url",
    "acquisition_url",
    "media_type",
    "page_count",
    "byte_size",
    "sha256",
    "upstream_digest_algorithm",
    "upstream_digest",
    "upstream_digest_url",
    "rights_statement",
    "rights_url",
    "rights_review_state",
    "redistribution_scope",
    "safety_class",
    "release_status",
    "operational_use",
    "format_check",
    "open_test_state",
    "retrieved_at_utc",
    "notes",
)
RELEASED_RIGHTS = {
    "CLEARED_OPEN_LICENSE",
    "CLEARED_PUBLIC_USE",
    "CLEARED_US_GOVERNMENT_WORK",
}
ALLOWED_STATUSES = {
    "RELEASED_REFERENCE",
    "RELEASED_TRAINING_ONLY",
    "PRIVATE_PERSONAL_COPY_REFERENCE",
    "CANDIDATE_REFERENCE_NOT_OPERATIONAL",
    "READER_VERIFIED_NOT_LAUNCHED",
}
SHA256_RE = re.compile(r"[0-9a-f]{64}")
HEX_RE = re.compile(r"[0-9a-f]+")


def digest_file(path: Path, algorithm: str) -> str:
    digest = hashlib.new(algorithm)
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def is_inside(path: Path, parent: Path) -> bool:
    try:
        path.relative_to(parent)
    except ValueError:
        return False
    return True


def payload_files() -> set[str]:
    files: set[str] = set()
    for name in PAYLOAD_ROOTS:
        base = ROOT / name
        for path in base.rglob("*"):
            if path.is_file() or path.is_symlink():
                files.add(path.relative_to(ROOT).as_posix())
    return files


def main() -> int:
    errors: list[str] = []
    warnings: list[str] = []
    counters: Counter[str] = Counter()

    for name in REQUIRED_DIRS:
        path = ROOT / name
        if not path.is_dir():
            errors.append(f"missing required directory: {name}")

    if not REGISTER.is_file():
        print(f"FAIL missing register: {REGISTER}")
        return 1

    with REGISTER.open("r", encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        if tuple(reader.fieldnames or ()) != EXPECTED_COLUMNS:
            errors.append("register header differs from the pinned schema")
        rows = list(reader)

    ids: set[str] = set()
    registered_paths: set[str] = set()
    total_bytes = 0
    pdf_rows: list[tuple[dict[str, str], Path]] = []
    dmg_rows: list[tuple[dict[str, str], Path]] = []
    format_passes = 0

    for line_number, row in enumerate(rows, start=2):
        prefix = f"row {line_number} ({row.get('payload_id') or 'no-id'})"
        if None in row:
            errors.append(f"{prefix}: extra CSV fields")
            continue
        missing_values = [
            key
            for key in (
                "payload_id",
                "relative_path",
                "title",
                "publisher",
                "edition_date",
                "language",
                "audience",
                "canonical_url",
                "acquisition_url",
                "media_type",
                "byte_size",
                "sha256",
                "rights_statement",
                "rights_review_state",
                "redistribution_scope",
                "safety_class",
                "release_status",
                "operational_use",
                "format_check",
                "open_test_state",
                "retrieved_at_utc",
            )
            if not row.get(key, "").strip()
        ]
        if missing_values:
            errors.append(f"{prefix}: blank required fields: {','.join(missing_values)}")

        payload_id = row.get("payload_id", "")
        if payload_id in ids:
            errors.append(f"{prefix}: duplicate payload_id")
        ids.add(payload_id)

        relative = row.get("relative_path", "")
        if relative in registered_paths:
            errors.append(f"{prefix}: duplicate relative_path")
        registered_paths.add(relative)
        rel_path = Path(relative)
        if rel_path.is_absolute() or ".." in rel_path.parts:
            errors.append(f"{prefix}: unsafe relative_path: {relative}")
            continue
        if not rel_path.parts or rel_path.parts[0] not in PAYLOAD_ROOTS:
            errors.append(f"{prefix}: path is outside a payload root: {relative}")
            continue

        path = ROOT / rel_path
        if path.is_symlink():
            errors.append(f"{prefix}: payload must not be a symlink: {relative}")
            continue
        if not path.is_file():
            errors.append(f"{prefix}: payload is missing: {relative}")
            continue
        resolved = path.resolve()
        if not is_inside(resolved, ROOT):
            errors.append(f"{prefix}: resolved path escapes offline-library")
            continue

        try:
            expected_size = int(row.get("byte_size", ""))
        except ValueError:
            errors.append(f"{prefix}: byte_size is not an integer")
            continue
        actual_size = path.stat().st_size
        if expected_size <= 0 or actual_size != expected_size:
            errors.append(
                f"{prefix}: size mismatch expected={expected_size} actual={actual_size}"
            )
        else:
            counters["size"] += 1
            total_bytes += actual_size

        expected_sha256 = row.get("sha256", "")
        if not SHA256_RE.fullmatch(expected_sha256):
            errors.append(f"{prefix}: sha256 must be 64 lowercase hex characters")
        else:
            actual_sha256 = digest_file(path, "sha256")
            if actual_sha256 != expected_sha256:
                errors.append(
                    f"{prefix}: SHA-256 mismatch expected={expected_sha256} actual={actual_sha256}"
                )
            else:
                counters["sha256"] += 1

        upstream_algorithm = row.get("upstream_digest_algorithm", "").lower()
        upstream_digest = row.get("upstream_digest", "").lower()
        upstream_url = row.get("upstream_digest_url", "")
        if bool(upstream_algorithm) != bool(upstream_digest):
            errors.append(f"{prefix}: upstream digest algorithm/value must both be set or blank")
        elif upstream_algorithm:
            counters["upstream_expected"] += 1
            if upstream_algorithm not in {"sha256", "md5"}:
                errors.append(f"{prefix}: unsupported upstream digest algorithm")
            elif not HEX_RE.fullmatch(upstream_digest):
                errors.append(f"{prefix}: upstream digest is not lowercase hexadecimal")
            elif len(upstream_digest) != {"sha256": 64, "md5": 32}[upstream_algorithm]:
                errors.append(f"{prefix}: upstream digest has the wrong length")
            elif not upstream_url.startswith("https://"):
                errors.append(f"{prefix}: upstream digest URL must be HTTPS")
            elif digest_file(path, upstream_algorithm) != upstream_digest:
                errors.append(f"{prefix}: upstream digest mismatch")
            else:
                counters["upstream_digest"] += 1

        for url_field in ("canonical_url", "acquisition_url"):
            if not row.get(url_field, "").startswith("https://"):
                errors.append(f"{prefix}: {url_field} must be an HTTPS URL")
        rights_url = row.get("rights_url", "")
        if rights_url and not rights_url.startswith("https://"):
            errors.append(f"{prefix}: rights_url must be blank or HTTPS")

        status = row.get("release_status", "")
        if status not in ALLOWED_STATUSES:
            errors.append(f"{prefix}: unsupported release_status: {status}")
        root_name = rel_path.parts[0]
        if root_name == "released":
            if not status.startswith("RELEASED_"):
                errors.append(f"{prefix}: released path requires RELEASED status")
            if row.get("rights_review_state") not in RELEASED_RIGHTS:
                errors.append(f"{prefix}: released path lacks cleared rights state")
        elif root_name == "private-licensed" and status != "PRIVATE_PERSONAL_COPY_REFERENCE":
            errors.append(f"{prefix}: private-licensed path has incompatible status")
        elif root_name == "candidate" and status != "CANDIDATE_REFERENCE_NOT_OPERATIONAL":
            errors.append(f"{prefix}: candidate path has incompatible status")
        elif root_name == "readers" and status != "READER_VERIFIED_NOT_LAUNCHED":
            errors.append(f"{prefix}: readers path has incompatible status")

        safety_text = " ".join(
            (row.get("safety_class", ""), row.get("title", ""), relative)
        ).upper()
        if any(token in safety_text for token in ("MEDICAL", "FIRST_AID", "CLINICIAN", "EMERGENCY_CARE")):
            if "NOT_LAY_ACTION_CARD" not in row.get("operational_use", ""):
                errors.append(f"{prefix}: medical content lacks NOT_LAY_ACTION_CARD boundary")

        marker_text = " ".join(row.values())
        for marker in ("NOT_DOWNLOADED", "NOT_REVIEWED", "NOT_TESTED"):
            if marker in marker_text:
                counters[marker] += 1

        media_type = row.get("media_type", "")
        suffix = path.suffix.lower()
        with path.open("rb") as handle:
            head = handle.read(8)
        if media_type == "application/pdf" and suffix == ".pdf":
            if not head.startswith(b"%PDF-"):
                errors.append(f"{prefix}: PDF signature missing")
            else:
                format_passes += 1
                pdf_rows.append((row, path))
        elif media_type == "application/x-zim" and suffix == ".zim":
            if head[:4] != b"ZIM\x04":
                errors.append(f"{prefix}: ZIM magic mismatch: {head[:4].hex()}")
            else:
                format_passes += 1
        elif media_type == "application/x-apple-diskimage" and suffix == ".dmg":
            with path.open("rb") as handle:
                handle.seek(-512, os.SEEK_END)
                trailer = handle.read(4)
            if trailer != b"koly":
                errors.append(f"{prefix}: UDIF trailer magic mismatch: {trailer.hex()}")
            else:
                format_passes += 1
                dmg_rows.append((row, path))
        else:
            errors.append(f"{prefix}: media_type and filename extension disagree")

    actual_paths = payload_files()
    for extra in sorted(actual_paths - registered_paths):
        errors.append(f"unregistered payload file: {extra}")
    for missing in sorted(registered_paths - actual_paths):
        errors.append(f"registered path absent from payload roots: {missing}")

    pdfinfo = shutil.which("pdfinfo")
    if pdfinfo:
        for row, path in pdf_rows:
            result = subprocess.run(
                [pdfinfo, str(path)], capture_output=True, text=True, check=False
            )
            match = re.search(r"^Pages:\s+(\d+)\s*$", result.stdout, re.MULTILINE)
            if result.returncode != 0 or not match:
                errors.append(f"pdfinfo failed: {row['relative_path']}")
                continue
            if match.group(1) != row.get("page_count"):
                errors.append(
                    f"pdfinfo page mismatch: {row['relative_path']} "
                    f"manifest={row.get('page_count')} actual={match.group(1)}"
                )
                continue
            counters["pdfinfo"] += 1
    else:
        warnings.append("pdfinfo unavailable; PDF signature/hash checks only")

    hdiutil = shutil.which("hdiutil")
    if hdiutil:
        for row, path in dmg_rows:
            result = subprocess.run(
                [hdiutil, "verify", str(path)], capture_output=True, text=True, check=False
            )
            if result.returncode != 0:
                errors.append(f"hdiutil verify failed: {row['relative_path']}")
            else:
                counters["hdiutil"] += 1
    elif dmg_rows:
        warnings.append("hdiutil unavailable; DMG UDIF trailer/hash checks only")

    print(f"REGISTER rows={len(rows)}")
    print(f"PAYLOAD files={len(actual_paths)} bytes={total_bytes}")
    print(
        "INTEGRITY "
        f"size_pass={counters['size']}/{len(rows)} "
        f"sha256_pass={counters['sha256']}/{len(rows)} "
        f"upstream_digest_pass={counters['upstream_digest']}/{counters['upstream_expected']} "
        f"format_signature_pass={format_passes}/{len(rows)}"
    )
    if pdfinfo:
        print(f"PDFINFO pass={counters['pdfinfo']}/{len(pdf_rows)}")
    if hdiutil:
        print(f"HDIUTIL pass={counters['hdiutil']}/{len(dmg_rows)}")
    print(
        "MARKERS "
        f"NOT_DOWNLOADED={counters['NOT_DOWNLOADED']} "
        f"NOT_REVIEWED={counters['NOT_REVIEWED']} "
        f"NOT_TESTED={counters['NOT_TESTED']}"
    )
    for warning in warnings:
        print(f"WARN {warning}")
    for error in errors:
        print(f"FAIL {error}")
    print(f"RESULT errors={len(errors)} warnings={len(warnings)}")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
