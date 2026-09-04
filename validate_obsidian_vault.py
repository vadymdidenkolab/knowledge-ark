#!/usr/bin/env python3
"""Fail-closed structural checks for the offline Obsidian catalog.

This validator proves catalog integrity and linkability only. It never promotes a
note to executable, tested, released, or physically available status.
"""

from __future__ import annotations

import csv
from pathlib import Path, PurePosixPath
import re
import sys
from typing import Dict, List, Optional, Set, Tuple


ROOT = Path(__file__).resolve().parent
VAULT = ROOT / "Obsidian-Vault"
GENERATED = VAULT / "90_GENERATED_CATALOG"
MANIFEST = GENERATED / "_GENERATED_MANIFEST.txt"

DATASETS = [
    ("technology-dependency-register.csv", "node_id"),
    ("practical-science-domain-register.csv", "domain_id"),
    ("practical-science-project-register.csv", "project_id"),
    ("practical-science-instrument-register.csv", "instrument_id"),
    ("practical-science-learning-paths.csv", "path_id"),
    ("practical-science-safety-gates.csv", "gate_id"),
    ("scenario-register.csv", "scenario_id"),
    ("century-capability-register.csv", "capability_id"),
    ("source-manifest.csv", "id"),
    ("offline-corpus-manifest.csv", "package_id"),
    ("practical-science-package-register.csv", "package_id"),
    ("offline-library/offline-payload-register.csv", "payload_id"),
    ("technology-service-level-register.csv", "service_requirement_id"),
    ("capability-crosswalk.csv", "crosswalk_id"),
    ("payload-source-crosswalk.csv", "payload_crosswalk_id"),
    ("known-gap-register.csv", "gap_id"),
]

REQUIRED_MOCS = {
    "MOCs/MOC_WATER.md",
    "MOCs/MOC_FOOD_AGRI.md",
    "MOCs/MOC_HEALTH.md",
    "MOCs/MOC_SHELTER.md",
    "MOCs/MOC_ENERGY_FUELS.md",
    "MOCs/MOC_WORKSHOP.md",
    "MOCs/MOC_MATERIALS_CHEMISTRY.md",
    "MOCs/MOC_MAPS_COMMS.md",
    "MOCs/MOC_KNOWLEDGE_COMPUTING.md",
    "MOCs/MOC_GOVERNANCE.md",
    "MOCs/MOC_PORTUGAL.md",
    "MOCs/MOC_SAFETY.md",
}

VALID_PRIORITIES = {"P0_RED", "P1_ORANGE", "P2_YELLOW", "P3_GREEN", "P4_BLUE"}
WIKI_RE = re.compile(r"\[\[([^\]]+)\]\]")


def fail(issues: List[str], message: str) -> None:
    issues.append(message)


def row_count(path: Path, id_field: str, issues: List[str], ids: Set[str]) -> int:
    try:
        with path.open("r", encoding="utf-8-sig", newline="") as handle:
            rows = list(csv.DictReader(handle))
    except (OSError, csv.Error) as exc:
        fail(issues, f"registry unreadable: {path.name}: {exc}")
        return 0
    for line_number, row in enumerate(rows, start=2):
        identifier = (row.get(id_field) or "").strip()
        if not identifier:
            fail(issues, f"blank id: {path.name}:{line_number}:{id_field}")
        elif identifier in ids:
            fail(issues, f"duplicate global id: {identifier}")
        else:
            ids.add(identifier)
    return len(rows)


def parse_frontmatter(text: str) -> Optional[Dict[str, str]]:
    if not text.startswith("---\n"):
        return None
    end = text.find("\n---\n", 4)
    if end < 0:
        return None
    fields: Dict[str, str] = {}
    for line in text[4:end].splitlines():
        if ":" not in line or line[:1].isspace():
            continue
        key, value = line.split(":", 1)
        fields[key.strip()] = value.strip().strip('"')
    return fields


def normalize_link(source: Path, raw: str) -> Tuple[str, bool]:
    # Inside Markdown tables Obsidian requires the alias separator to be
    # escaped as ``\|``. It is still the target/label boundary semantically.
    target_part = raw.split("\\|", 1)[0] if "\\|" in raw else raw.split("|", 1)[0]
    target = target_part.split("#", 1)[0].split("^", 1)[0].strip()
    if not target:
        return "", False
    target = target[:-3] if target.endswith(".md") else target
    if "/" in target:
        # Obsidian vault-root paths are used by this vault. Also accept a true
        # path relative to the source note for hand-authored additions.
        return PurePosixPath(target).as_posix(), True
    return target, False


def main() -> int:
    issues: List[str] = []
    if not VAULT.is_dir():
        print(f"obsidian_vault_error missing {VAULT}", file=sys.stderr)
        return 1

    expected_ids: Set[str] = set()
    expected_atomic = sum(row_count(ROOT / name, id_field, issues, expected_ids) for name, id_field in DATASETS)

    if not MANIFEST.is_file():
        fail(issues, "generated manifest missing")
        manifest_lines: List[str] = []
        declared_atomic = -1
    else:
        manifest_lines = MANIFEST.read_text(encoding="utf-8").splitlines()
        declared = [line for line in manifest_lines if line.startswith("atomic_note_count=")]
        try:
            declared_atomic = int(declared[0].split("=", 1)[1]) if len(declared) == 1 else -1
        except ValueError:
            declared_atomic = -1
        if declared_atomic != expected_atomic:
            fail(issues, f"manifest count {declared_atomic} != registry rows {expected_atomic}")

    manifest_paths = {
        line.strip()
        for line in manifest_lines
        if line.strip() and not line.startswith("#") and "=" not in line
    }
    actual_atomic_paths = {
        path.relative_to(VAULT).as_posix()
        for path in GENERATED.rglob("*.md")
        if path.name not in {"_INDEX.md", "_EDGE_SUMMARY.md", "INDEX.md", "PRIORITY_INDEX.md"}
    }
    if manifest_paths != actual_atomic_paths:
        missing = sorted(manifest_paths - actual_atomic_paths)[:5]
        unlisted = sorted(actual_atomic_paths - manifest_paths)[:5]
        fail(issues, f"manifest/file mismatch missing={missing} unlisted={unlisted}")
    if len(actual_atomic_paths) != expected_atomic:
        fail(issues, f"atomic files {len(actual_atomic_paths)} != expected {expected_atomic}")

    generated_ids: Set[str] = set()
    priority_counts = {priority: 0 for priority in sorted(VALID_PRIORITIES)}
    for relative in sorted(actual_atomic_paths):
        path = VAULT / relative
        text = path.read_text(encoding="utf-8")
        fields = parse_frontmatter(text)
        if fields is None:
            fail(issues, f"frontmatter missing: {relative}")
            continue
        identifier = fields.get("id", "")
        if not identifier:
            fail(issues, f"generated id missing: {relative}")
        elif identifier in generated_ids:
            fail(issues, f"duplicate generated id: {identifier}")
        else:
            generated_ids.add(identifier)
        priority = fields.get("priority_tier", "")
        if priority not in VALID_PRIORITIES:
            fail(issues, f"invalid priority {priority!r}: {relative}")
        else:
            priority_counts[priority] += 1
        if fields.get("generated") != "true":
            fail(issues, f"generated marker missing: {relative}")
        if fields.get("instruction_state") != "CATALOG_ONLY_NOT_EXECUTABLE":
            fail(issues, f"unsafe instruction state: {relative}")
        if fields.get("status") in {"EXECUTABLE", "TESTED", "RELEASED"}:
            fail(issues, f"unsupported readiness status: {relative}")
        safety = fields.get("safety_class", "")
        gate = fields.get("execution_gate", "")
        if safety.startswith("S3_") and gate != "BLACK_GATE_LICENSED_ONLY":
            fail(issues, f"S3 gate mismatch: {relative}")
        if safety.startswith("S4_") and gate != "BLACK_GATE_REFERENCE_ONLY":
            fail(issues, f"S4 gate mismatch: {relative}")

    if generated_ids != expected_ids:
        fail(
            issues,
            f"generated/registry id mismatch missing={sorted(expected_ids-generated_ids)[:5]} extra={sorted(generated_ids-expected_ids)[:5]}",
        )

    for required in sorted(REQUIRED_MOCS | {"00 — НАЧАТЬ.md", "README.md"}):
        if not (VAULT / required).is_file():
            fail(issues, f"required vault note missing: {required}")

    all_markdown = sorted(VAULT.rglob("*.md"))
    all_canvas = sorted(VAULT.rglob("*.canvas"))
    # Markdown links conventionally omit ``.md``. Canvas links retain their
    # extension so the target stays unambiguous and opens in Canvas mode.
    path_targets = {path.relative_to(VAULT).with_suffix("").as_posix() for path in all_markdown}
    path_targets.update(path.relative_to(VAULT).as_posix() for path in all_canvas)
    stem_targets: Dict[str, List[str]] = {}
    for target in path_targets:
        stem_targets.setdefault(PurePosixPath(target).name, []).append(target)
    unresolved: List[str] = []
    ambiguous: List[str] = []
    for path in all_markdown:
        relative = path.relative_to(VAULT).as_posix()
        text = path.read_text(encoding="utf-8")
        for raw in WIKI_RE.findall(text):
            target, has_path = normalize_link(path, raw)
            if not target:
                continue
            if has_path:
                if target not in path_targets:
                    # Secondary interpretation: link relative to the note.
                    rel_target = (PurePosixPath(relative).parent / target).as_posix()
                    if rel_target not in path_targets:
                        unresolved.append(f"{relative} -> {target}")
            else:
                matches = stem_targets.get(target, [])
                if not matches:
                    unresolved.append(f"{relative} -> {target}")
                elif len(matches) > 1:
                    # Obsidian prefers a same-folder note for a bare wikilink.
                    # Mirror directories intentionally contain names such as
                    # README.md that also exist at vault root, so model that
                    # deterministic local resolution before reporting an
                    # ambiguity.
                    same_folder = (PurePosixPath(relative).parent / target).as_posix()
                    if same_folder not in matches:
                        ambiguous.append(f"{relative} -> {target}: {matches[:4]}")
    if unresolved:
        fail(issues, f"unresolved wiki links ({len(unresolved)}): {unresolved[:8]}")
    if ambiguous:
        fail(issues, f"ambiguous wiki links ({len(ambiguous)}): {ambiguous[:8]}")

    home_path = VAULT / "00 — НАЧАТЬ.md"
    home_text = home_path.read_text(encoding="utf-8") if home_path.is_file() else ""
    if f"generated_atomic_notes: {expected_atomic}" not in home_text:
        fail(issues, f"HOME generated_atomic_notes is not {expected_atomic}")
    if "[[20 — Рабочие разделы/00 — Панели автономного кита" not in home_text:
        fail(issues, "HOME does not link the user-facing dashboard index")
    if "[[01 — КАРТОТЕКА ЗНАНИЙ/01 — Маршруты/02 — Маршрут на первые 72 часа" not in home_text:
        fail(issues, "HOME does not link the human P0 route")
    if "[[10 — Руководства/00 — Путеводитель по руководствам" not in home_text:
        fail(issues, "HOME does not link the in-vault guide mirrors")
    if "[[01 — КАРТОТЕКА ЗНАНИЙ/" not in home_text:
        fail(issues, "HOME does not link the human knowledge-card routes")
    if "[[90_GENERATED_CATALOG/" in home_text:
        fail(issues, "HOME exposes the technical generated catalog")

    print(
        "obsidian_vault_summary "
        f"registry_ids={expected_atomic} atomic_notes={len(actual_atomic_paths)} "
        f"markdown_files={len(all_markdown)} canvas_files={len(all_canvas)} "
        f"wiki_unresolved={len(unresolved)} wiki_ambiguous={len(ambiguous)}"
    )
    print("priorities " + " ".join(f"{key}={priority_counts[key]}" for key in sorted(priority_counts)))
    if issues:
        for issue in issues:
            print(f"ERROR {issue}", file=sys.stderr)
        print(f"result=FAIL issues={len(issues)}", file=sys.stderr)
        return 1
    print("result=PASS scope=STRUCTURE_AND_LINKS_ONLY")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
