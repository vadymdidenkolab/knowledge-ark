#!/usr/bin/env python3
"""Validate the human-facing Obsidian layer against its machine backend.

Passing proves deterministic mirroring, link hygiene and view coverage. It does
not prove physical inventory, medical suitability, site readiness, training,
functional testing or release permission.
"""

from __future__ import annotations

import csv
import hashlib
import json
from pathlib import Path
import re
import sys
from typing import Dict, Iterable, List, Mapping, Sequence, Set
from urllib.parse import unquote


ROOT = Path(__file__).resolve().parent
VAULT = ROOT / "Obsidian-Vault"
GUIDES = VAULT / "10 — Руководства"
DASHBOARDS = VAULT / "20 — Рабочие разделы"
DATA = VAULT / "80_DATA_REGISTERS"

GUIDE_MANIFEST = GUIDES / ".generated-guides-manifest.json"
DATA_MANIFEST = DATA / ".generated-data-registers-manifest.json"

REQUIRED_DASHBOARDS = {
    "00 — Панели автономного кита.md",
    "01 — Что реально готово.md",
    "02 — Первые 72 часа.md",
    "03 — Медицинская помощь.md",
    "04 — Что ещё не готово.md",
    "05 — Уровни автономности.md",
    "06 — Офлайн-библиотека.md",
    "07 — Области знаний и систем.md",
    "08 — Семена и питание.md",
    "09 — Португалия.md",
    "10 — Границы безопасности.md",
    "11 — Физический инвентарь.md",
}

MD_LINK_RE = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
HTML_LINK_RE = re.compile(r"\b(?:href|src)\s*=\s*['\"]([^'\"]+)['\"]", re.IGNORECASE)
TECH_WIKI_RE = re.compile(r"\[\[90_GENERATED_CATALOG/technology/TEC ([A-Za-z0-9_.-]+)(?:\\?\|[^\]]*)?\]\]")
GAP_WIKI_RE = re.compile(r"\[\[90_GENERATED_CATALOG/known-gap/GAP ([A-Za-z0-9_.-]+)(?:\\?\|[^\]]*)?\]\]")
SERVICE_WIKI_RE = re.compile(r"\[\[90_GENERATED_CATALOG/service-level/SR ([A-Za-z0-9_.-]+)(?:\\?\|[^\]]*)?\]\]")
PAYLOAD_WIKI_RE = re.compile(r"\[\[90_GENERATED_CATALOG/source-payload/PAY ([A-Za-z0-9_.-]+)(?:\\?\|[^\]]*)?\]\]")


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def read_json(path: Path, issues: List[str]) -> Mapping[str, object]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        issues.append(f"manifest unreadable: {path.relative_to(ROOT)}: {exc}")
        return {}
    if not isinstance(value, dict):
        issues.append(f"manifest is not an object: {path.relative_to(ROOT)}")
        return {}
    return value


def read_csv(relative: str, issues: List[str]) -> List[Dict[str, str]]:
    path = ROOT / relative
    try:
        with path.open("r", encoding="utf-8-sig", newline="") as handle:
            return [
                {key: (value or "").strip() for key, value in row.items()}
                for row in csv.DictReader(handle)
            ]
    except (OSError, csv.Error) as exc:
        issues.append(f"registry unreadable: {relative}: {exc}")
        return []


def values(rows: Sequence[Mapping[str, str]], field: str) -> Set[str]:
    return {row.get(field, "").strip() for row in rows if row.get(field, "").strip()}


def check_exact_links(
    page: Path,
    pattern: re.Pattern[str],
    expected: Set[str],
    label: str,
    issues: List[str],
) -> None:
    try:
        actual = set(pattern.findall(page.read_text(encoding="utf-8")))
    except OSError as exc:
        issues.append(f"cannot read {page.relative_to(ROOT)}: {exc}")
        return
    if actual != expected:
        issues.append(
            f"{label} coverage mismatch missing={sorted(expected - actual)[:8]} "
            f"extra={sorted(actual - expected)[:8]}"
        )


def user_markdown() -> Iterable[Path]:
    for path in (VAULT / "00 — НАЧАТЬ.md", VAULT / "README.md"):
        if path.is_file():
            yield path
    for directory in (
        VAULT / "01 — КАРТОТЕКА ЗНАНИЙ",
        VAULT / "MOCs",
        GUIDES,
        DASHBOARDS,
        DATA,
        VAULT / "90_ADMIN",
    ):
        if directory.is_dir():
            yield from directory.rglob("*.md")


def clickable_backend_target(target: str) -> bool:
    cleaned = unquote(target).split("#", 1)[0].split("?", 1)[0].lower().rstrip("/")
    return cleaned.endswith(".csv") or cleaned.endswith(".py")


def validate_link_hygiene(issues: List[str]) -> int:
    checked = 0
    for path in user_markdown():
        text = path.read_text(encoding="utf-8")
        relative = path.relative_to(VAULT).as_posix()
        for target in MD_LINK_RE.findall(text) + HTML_LINK_RE.findall(text):
            if clickable_backend_target(target):
                issues.append(f"clickable machine-backend link in user layer: {relative} -> {target}")
            checked += 1
        if re.search(r"^##\s+Поля исходного реестра\s*$", text, re.MULTILINE):
            issues.append(f"raw registry heading exposed: {relative}")
    return checked


def validate_guides(issues: List[str]) -> tuple[int, int]:
    manifest = read_json(GUIDE_MANIFEST, issues)
    sources = manifest.get("sources", [])
    generated = manifest.get("generated_files", [])
    if not isinstance(sources, list) or len(sources) != 31:
        issues.append(f"guide source count is not 31: {len(sources) if isinstance(sources, list) else 'invalid'}")
        sources = []
    if not isinstance(generated, list) or len(generated) != 32:
        issues.append(f"guide generated file count is not 32: {len(generated) if isinstance(generated, list) else 'invalid'}")
        generated = []
    for entry in sources:
        if not isinstance(entry, dict):
            issues.append("invalid guide source manifest entry")
            continue
        source = ROOT / str(entry.get("source", ""))
        mirror = GUIDES / str(entry.get("mirror", ""))
        expected_hash = str(entry.get("sha256", ""))
        if not source.is_file() or not mirror.is_file():
            issues.append(f"guide source/mirror missing: {entry}")
            continue
        actual_hash = sha256(source)
        if actual_hash != expected_hash:
            issues.append(f"guide source hash stale: {source.relative_to(ROOT)}")
        mirror_text = mirror.read_text(encoding="utf-8")
        if f'mirror_sha256: "{actual_hash}"' not in mirror_text:
            issues.append(f"guide mirror hash marker stale: {mirror.relative_to(VAULT)}")
    return len(sources), len(generated)


def discover_backend_csv() -> Set[str]:
    result: Set[str] = set()
    for path in ROOT.rglob("*.csv"):
        if VAULT in path.parents:
            continue
        result.add(path.relative_to(ROOT).as_posix())
    return result


def validate_data_views(issues: List[str]) -> tuple[int, int, int]:
    manifest = read_json(DATA_MANIFEST, issues)
    sources = manifest.get("sources", [])
    if not isinstance(sources, list):
        issues.append("data source manifest is not a list")
        return 0, 0, 0
    declared_sources = {str(entry.get("source_path", "")) for entry in sources if isinstance(entry, dict)}
    actual_sources = discover_backend_csv()
    if declared_sources != actual_sources:
        issues.append(
            f"data source coverage mismatch missing={sorted(actual_sources-declared_sources)[:8]} "
            f"extra={sorted(declared_sources-actual_sources)[:8]}"
        )
    declared_files = manifest.get("owned_files", [])
    if not isinstance(declared_files, list):
        issues.append("data owned_files is not a list")
        declared_files = []
    actual_files = {path.name for path in DATA.glob("*.md")}
    if set(str(value) for value in declared_files) != actual_files:
        issues.append("data owned-file manifest does not match generated Markdown files")

    total_rows = 0
    total_columns = 0
    for entry in sources:
        if not isinstance(entry, dict):
            issues.append("invalid data source manifest entry")
            continue
        source_rel = str(entry.get("source_path", ""))
        output_name = str(entry.get("output_file", ""))
        source = ROOT / source_rel
        output = DATA / output_name
        if not source.is_file() or not output.is_file():
            issues.append(f"data source/output missing: {source_rel} -> {output_name}")
            continue
        if sha256(source) != str(entry.get("source_sha256", "")):
            issues.append(f"data source hash stale: {source_rel}")
        if sha256(output) != str(entry.get("output_sha256", "")):
            issues.append(f"data output hash stale: {output_name}")
        row_count = int(entry.get("row_count", -1))
        column_count = int(entry.get("column_count", -1))
        total_rows += max(row_count, 0)
        total_columns += max(column_count, 0)
        text = output.read_text(encoding="utf-8")
        if f"source_row_count: {row_count}" not in text:
            issues.append(f"data row marker mismatch: {output_name}")
        if f"source_column_count: {column_count}" not in text:
            issues.append(f"data column marker mismatch: {output_name}")
        record_markers = len(re.findall(r"^<!-- record:\d+ cells:\d+ -->$", text, re.MULTILINE))
        if record_markers != row_count:
            issues.append(f"data record-marker count {record_markers} != {row_count}: {output_name}")
    if int(manifest.get("source_count", -1)) != len(actual_sources):
        issues.append("data manifest source_count mismatch")
    if int(manifest.get("register_page_count", -1)) != len(actual_sources):
        issues.append("data manifest register_page_count mismatch")
    return len(sources), total_rows, total_columns


def validate_dashboards(issues: List[str]) -> Dict[str, int]:
    actual = {path.name for path in DASHBOARDS.glob("*.md")}
    if actual != REQUIRED_DASHBOARDS:
        issues.append(
            f"dashboard set mismatch missing={sorted(REQUIRED_DASHBOARDS-actual)} "
            f"extra={sorted(actual-REQUIRED_DASHBOARDS)}"
        )
    for filename in sorted(REQUIRED_DASHBOARDS & actual):
        text = (DASHBOARDS / filename).read_text(encoding="utf-8")
        for marker in (
            "generated: true",
            "proof_state: CATALOG_VIEW_NOT_OPERATIONAL_PROOF",
            "instruction_state: NAVIGATION_ONLY_NOT_EXECUTABLE",
        ):
            if marker not in text:
                issues.append(f"dashboard marker missing {marker!r}: {filename}")

    technology = read_csv("technology-dependency-register.csv", issues)
    planning = read_csv("technology-node-planning-register.csv", issues)
    gaps = read_csv("known-gap-register.csv", issues)
    services = read_csv("technology-service-level-register.csv", issues)
    payloads = read_csv("offline-library/offline-payload-register.csv", issues)
    inventory = read_csv("inventory-template.csv", issues)
    planning_by_id = {row["node_id"]: row for row in planning}

    health = {row["node_id"] for row in technology if row.get("domain") == "HEALTH"}
    food = {row["node_id"] for row in technology if row.get("domain") == "FOOD_AGRI"}
    portugal = {row["node_id"] for row in technology if row.get("domain") == "PORTUGAL"}
    restricted = {
        row["node_id"]
        for row in technology
        if row.get("safety_class", "").startswith(("S3_", "S4_"))
    }
    p0 = {
        row["node_id"]
        for row in technology
        if planning_by_id.get(row["node_id"], {}).get("priority_tier") == "P0_RED"
    }
    p0_safe = p0 - restricted
    p0_gaps = {row["gap_id"] for row in gaps if row.get("priority_tier") == "P0_RED"}

    check_exact_links(DASHBOARDS / "02 — Первые 72 часа.md", TECH_WIKI_RE, p0_safe, "P0 S0-S2", issues)
    p0_text = (DASHBOARDS / "02 — Первые 72 часа.md").read_text(encoding="utf-8")
    p0_actual_gaps = set(GAP_WIKI_RE.findall(p0_text))
    if p0_actual_gaps != p0_gaps:
        issues.append(f"P0 gap coverage mismatch missing={sorted(p0_gaps-p0_actual_gaps)} extra={sorted(p0_actual_gaps-p0_gaps)}")
    if set(TECH_WIKI_RE.findall(p0_text)) & restricted:
        issues.append("restricted S3/S4 technology leaked into the P0 action table")

    check_exact_links(DASHBOARDS / "03 — Медицинская помощь.md", TECH_WIKI_RE, health, "medicine", issues)
    check_exact_links(DASHBOARDS / "04 — Что ещё не готово.md", GAP_WIKI_RE, values(gaps, "gap_id"), "known gaps", issues)
    check_exact_links(DASHBOARDS / "05 — Уровни автономности.md", SERVICE_WIKI_RE, values(services, "service_requirement_id"), "service levels", issues)
    check_exact_links(DASHBOARDS / "06 — Офлайн-библиотека.md", PAYLOAD_WIKI_RE, values(payloads, "payload_id"), "offline payloads", issues)
    check_exact_links(DASHBOARDS / "08 — Семена и питание.md", TECH_WIKI_RE, food, "food and seeds", issues)
    check_exact_links(DASHBOARDS / "09 — Португалия.md", TECH_WIKI_RE, portugal, "Portugal", issues)
    check_exact_links(DASHBOARDS / "10 — Границы безопасности.md", TECH_WIKI_RE, restricted, "S3/S4 safety", issues)

    inventory_text = (DASHBOARDS / "11 — Физический инвентарь.md").read_text(encoding="utf-8")
    for marker in (
        f"Подтверждено физически | 0",
        f"Фактическое количество заполнено | 0",
        f"Разрешено как проверенное | 0",
        f"Плановых строк | {len(inventory)}",
    ):
        if marker not in inventory_text:
            issues.append(f"physical-inventory proof marker missing: {marker}")

    payload_page = (DASHBOARDS / "06 — Офлайн-библиотека.md").read_text(encoding="utf-8")
    local_targets = re.findall(r"\]\((\.\./\.\./offline-library/[^)]+)\)", payload_page)
    if len(local_targets) != len(payloads):
        issues.append(f"offline local-copy links {len(local_targets)} != payload rows {len(payloads)}")
    for target in local_targets:
        path = (DASHBOARDS / unquote(target)).resolve()
        if not path.is_file():
            issues.append(f"offline payload target missing: {target}")
    if re.search(r"https?://", payload_page, re.IGNORECASE):
        issues.append("offline dashboard exposes online URL as a primary path")

    return {
        "dashboards": len(actual),
        "technology": len(technology),
        "p0": len(p0),
        "p0_safe": len(p0_safe),
        "p0_restricted": len(p0 & restricted),
        "health": len(health),
        "gaps": len(gaps),
        "p0_gaps": len(p0_gaps),
        "services": len(services),
        "payloads": len(payloads),
        "food": len(food),
        "portugal": len(portugal),
        "restricted": len(restricted),
        "inventory": len(inventory),
    }


def validate_home(issues: List[str]) -> None:
    path = VAULT / "00 — НАЧАТЬ.md"
    if not path.is_file():
        issues.append("HOME missing")
        return
    text = path.read_text(encoding="utf-8")
    for target in (
        "[[01 — КАРТОТЕКА ЗНАНИЙ/01 — Маршруты/02 — Маршрут на первые 72 часа",
        "[[01 — КАРТОТЕКА ЗНАНИЙ/01 — Маршруты/05 — Маршрут медицины и аптечек",
        "[[20 — Рабочие разделы/00 — Панели автономного кита",
        "[[20 — Рабочие разделы/11 — Физический инвентарь",
        "[[20 — Рабочие разделы/04 — Что ещё не готово",
        "[[10 — Руководства/00 — Путеводитель по руководствам",
        "[[80_DATA_REGISTERS/INDEX",
    ):
        if target not in text:
            issues.append(f"HOME route missing: {target}")
    if "[[90_GENERATED_CATALOG/" in text:
        issues.append("HOME exposes technical raw catalog")
    if re.search(r"\]\(\.\./", text):
        issues.append("HOME links outside the vault")


def main() -> int:
    issues: List[str] = []
    if not VAULT.is_dir():
        print(f"obsidian_user_layer_error missing {VAULT}", file=sys.stderr)
        return 1

    validate_home(issues)
    clickable_links = validate_link_hygiene(issues)
    guide_sources, guide_files = validate_guides(issues)
    data_sources, data_rows, data_columns = validate_data_views(issues)
    counts = validate_dashboards(issues)

    print(
        "obsidian_user_layer_summary "
        + " ".join(f"{key}={value}" for key, value in counts.items())
        + f" guide_sources={guide_sources} guide_files={guide_files}"
        + f" data_sources={data_sources} data_rows={data_rows} data_columns={data_columns}"
        + f" clickable_links_checked={clickable_links}"
    )
    print(
        "PROOF_BOUNDARY markdown_mirror_and_view_coverage_only; "
        "not_personalized; not_physically_inventoried; not_medically_reviewed; "
        "not_functionally_tested; not_released"
    )
    if issues:
        for issue in issues:
            print(f"ERROR {issue}", file=sys.stderr)
        print(f"result=FAIL issues={len(issues)}", file=sys.stderr)
        return 1
    print("result=PASS scope=OBSIDIAN_USER_LAYER_MIRROR_AND_VIEW_COVERAGE_ONLY")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
