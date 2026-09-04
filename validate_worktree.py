#!/usr/bin/env python3
"""Validate the evolving v0.5 worktree without pretending it is a release.

The immutable v0.4 ZIP has its own seed lock and validator. This script checks
the newer catalog, dependency graph, real offline payloads, and frozen archive
sidecar. Passing proves file/registry structure and payload integrity only.
"""

from __future__ import annotations

import csv
import hashlib
from pathlib import Path
import subprocess
import sys
import zipfile


ROOT = Path(__file__).resolve().parent
PARENT = ROOT.parent

CHECKS = [
    ROOT / "validate_technology_tree.py",
    ROOT / "validate_obsidian_vault.py",
    ROOT / "validate_obsidian_user_layer.py",
    ROOT / "validate_obsidian_semantic_graph.py",
    ROOT / "offline-library" / "verify_offline_payload.py",
]

REQUIRED = [
    ROOT / "22_TOTAL_ISOLATION_READINESS_AUDIT_RU.md",
    ROOT / "23_TECHNOLOGY_DEPENDENCY_TREE_RU.md",
    ROOT / "24_MASTER_CATALOG_STATUS_RU.md",
    ROOT / "technology-dependency-register.csv",
    ROOT / "technology-dependency-edges.csv",
    ROOT / "technology-node-planning-register.csv",
    ROOT / "technology-service-level-register.csv",
    ROOT / "capability-crosswalk.csv",
    ROOT / "payload-source-crosswalk.csv",
    ROOT / "known-gap-register.csv",
    ROOT / "build_obsidian_catalog.py",
    ROOT / "build_obsidian_guides.py",
    ROOT / "build_obsidian_data_views.py",
    ROOT / "build_obsidian_user_views.py",
    ROOT / "build_obsidian_knowledge_routes.py",
    ROOT / "build_obsidian_semantic_canvas.py",
    ROOT / "build_obsidian_graph_config.py",
    ROOT / "validate_obsidian_semantic_graph.py",
    ROOT / "standards" / "obsidian-topic-schema-v1.json",
    ROOT / "ОТКРЫТЬ_КАРТОТЕКУ.command",
    ROOT / "Obsidian-Vault" / "00 — НАЧАТЬ.md",
    ROOT / "Obsidian-Vault" / "01 — КАРТОТЕКА ЗНАНИЙ" / "00 — Карта всех знаний.md",
    ROOT / "Obsidian-Vault" / "01 — КАРТОТЕКА ЗНАНИЙ" / "03 — Карты связей" / "01 — Что нужно сначала.canvas",
    ROOT / "Obsidian-Vault" / "01 — КАРТОТЕКА ЗНАНИЙ" / "03 — Карты связей" / "04 — Образовательная лестница.canvas",
    ROOT / "Obsidian-Vault" / "10 — Руководства" / "00 — Путеводитель по руководствам.md",
    ROOT / "Obsidian-Vault" / "20 — Рабочие разделы" / "00 — Панели автономного кита.md",
    ROOT / "Obsidian-Vault" / "20 — Рабочие разделы" / "11 — Физический инвентарь.md",
    ROOT / "Obsidian-Vault" / "40 — Стандарт картотеки" / "00 — Стандарт данных, тегов и связей.md",
    ROOT / "Obsidian-Vault" / "80_DATA_REGISTERS" / "INDEX.md",
    ROOT / "Obsidian-Vault" / "90_ADMIN" / "INDEX.md",
    ROOT / "Obsidian-Vault" / "90_GENERATED_CATALOG" / "INDEX.md",
    ROOT / "Obsidian-Vault" / "90_GENERATED_CATALOG" / "PRIORITY_INDEX.md",
    ROOT / "offline-library" / "offline-payload-register.csv",
    ROOT / "offline-library" / "metadata" / "obsidian-vault-index.sqlite",
]


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def validate_frozen_v04(issues: list[str]) -> None:
    archive = PARENT / "autonomous-life-kit-v0.4.zip"
    sidecar = PARENT / "autonomous-life-kit-v0.4.sha256"
    seed_lock = PARENT / "autonomous-life-kit-v0.4.seed-lock.csv"
    for path in (archive, sidecar, seed_lock):
        if not path.is_file():
            issues.append(f"frozen v0.4 artifact missing: {path.name}")
    if not archive.is_file() or not sidecar.is_file():
        return
    parts = sidecar.read_text(encoding="utf-8").strip().split()
    if len(parts) < 2 or parts[-1].lstrip("*") != archive.name:
        issues.append("v0.4 sha256 sidecar format mismatch")
    elif sha256(archive) != parts[0].lower():
        issues.append("v0.4 archive sha256 mismatch")
    try:
        with zipfile.ZipFile(archive) as bundle:
            corrupt = bundle.testzip()
        if corrupt:
            issues.append(f"v0.4 ZIP corrupt member: {corrupt}")
    except (OSError, zipfile.BadZipFile) as exc:
        issues.append(f"v0.4 ZIP unreadable: {exc}")


def payload_summary(issues: list[str]) -> tuple[int, int]:
    register = ROOT / "offline-library" / "offline-payload-register.csv"
    try:
        with register.open("r", encoding="utf-8-sig", newline="") as handle:
            rows = list(csv.DictReader(handle))
    except (OSError, csv.Error) as exc:
        issues.append(f"payload register unreadable: {exc}")
        return 0, 0
    total_bytes = 0
    for line_number, row in enumerate(rows, start=2):
        try:
            total_bytes += int(row.get("byte_size", ""))
        except ValueError:
            issues.append(f"payload register invalid byte_size at line {line_number}")
    if not rows:
        issues.append("payload register is empty")
    return len(rows), total_bytes


def validate_known_gaps(issues: list[str]) -> int:
    path = ROOT / "known-gap-register.csv"
    required_fields = {
        "gap_id", "domain", "scope_layer", "priority_tier",
        "earliest_service_level", "gap_ru", "blocks_service_level",
        "blocker", "required_evidence", "current_evidence", "status",
        "owner", "due", "release_gate", "release_version", "notes",
    }
    valid_priorities = {"P0_RED", "P1_ORANGE", "P2_YELLOW", "P3_GREEN", "P4_BLUE"}
    valid_levels = {f"SL{number}" for number in range(7)}
    try:
        with path.open("r", encoding="utf-8-sig", newline="") as handle:
            reader = csv.DictReader(handle)
            rows = list(reader)
            fields = set(reader.fieldnames or [])
    except (OSError, csv.Error) as exc:
        issues.append(f"known-gap register unreadable: {exc}")
        return 0
    if fields != required_fields:
        issues.append(
            "known-gap fields mismatch "
            f"missing={sorted(required_fields - fields)} extra={sorted(fields - required_fields)}"
        )
    seen: set[str] = set()
    for line_number, row in enumerate(rows, start=2):
        gap_id = (row.get("gap_id") or "").strip()
        if not gap_id or gap_id in seen:
            issues.append(f"known-gap invalid/duplicate id at line {line_number}: {gap_id!r}")
        seen.add(gap_id)
        if (row.get("priority_tier") or "").strip() not in valid_priorities:
            issues.append(f"{gap_id}: invalid priority_tier")
        if (row.get("earliest_service_level") or "").strip() not in valid_levels:
            issues.append(f"{gap_id}: invalid earliest_service_level")
        blocked = {part.strip() for part in (row.get("blocks_service_level") or "").split("|") if part.strip()}
        if not blocked or not blocked <= valid_levels:
            issues.append(f"{gap_id}: invalid blocks_service_level")
        if not (row.get("status") or "").strip().startswith("OPEN_"):
            issues.append(f"{gap_id}: status must remain OPEN_* until independently closed")
        if not (row.get("release_gate") or "").strip().startswith("DENY_"):
            issues.append(f"{gap_id}: release_gate must remain DENY_* while gap is open")
        if (row.get("release_version") or "").strip() != "0.5-draft":
            issues.append(f"{gap_id}: release_version must be 0.5-draft")
        for field in ("domain", "scope_layer", "gap_ru", "required_evidence", "current_evidence", "owner", "due"):
            if not (row.get(field) or "").strip():
                issues.append(f"{gap_id}: blank {field}")
    if not rows:
        issues.append("known-gap register is empty")
    return len(rows)


def main() -> int:
    issues: list[str] = []
    print("WORKTREE v0.5-draft status=NOT_RELEASED")
    for path in REQUIRED:
        if not path.is_file():
            issues.append(f"required file missing: {path.relative_to(ROOT)}")

    for check in CHECKS:
        if not check.is_file():
            issues.append(f"validator missing: {check.relative_to(ROOT)}")
            continue
        print(f"RUN {check.relative_to(ROOT)}")
        result = subprocess.run(
            [sys.executable, str(check)],
            cwd=str(ROOT),
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            check=False,
        )
        print(result.stdout.rstrip())
        if result.returncode:
            issues.append(f"validator failed: {check.relative_to(ROOT)} rc={result.returncode}")

    validate_frozen_v04(issues)
    payload_count, payload_bytes = payload_summary(issues)
    gap_count = validate_known_gaps(issues)
    file_count = sum(1 for path in ROOT.rglob("*") if path.is_file())
    print(
        "WORKTREE_SUMMARY "
        f"files={file_count} payloads={payload_count} payload_bytes={payload_bytes} known_gaps={gap_count} "
        "maps_site_specific=0 production_packages_released=0 physical_inventory_verified=0"
    )
    print(
        "PROOF_BOUNDARY structure_and_payload_integrity_only; "
        "not_personalized; not_physically_inventoried; not_executable; not_released"
    )
    if issues:
        for issue in issues:
            print(f"ERROR {issue}", file=sys.stderr)
        print(f"RESULT FAIL issues={len(issues)}", file=sys.stderr)
        return 1
    print("RESULT PASS scope=WORKTREE_STRUCTURE_AND_PAYLOAD_INTEGRITY_ONLY")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
