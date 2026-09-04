#!/usr/bin/env python3
"""Generate atomic Obsidian catalog notes from the kit's machine registries.

Generated notes are inventory stubs, not instructions or evidence of readiness.
Only Obsidian-Vault/90_GENERATED_CATALOG is written. User-authored notes are
never deleted.
"""

from __future__ import annotations

import csv
from collections import Counter, defaultdict
from datetime import date
import json
from pathlib import Path
import re
import sys
from typing import Optional


ROOT = Path(__file__).resolve().parent
VAULT = ROOT / "Obsidian-Vault"
OUT = VAULT / "90_GENERATED_CATALOG"
TODAY = date.today().isoformat()

DATASETS = [
    ("technology-dependency-register.csv", "node_id", "title_ru", "domain", "capability_status", "technology", "TEC"),
    ("practical-science-domain-register.csv", "domain_id", "domain_title_ru", "group_code", "implementation_state", "science-domain", "SCI"),
    ("practical-science-project-register.csv", "project_id", "title_ru", "group_code", "status", "science-project", "PRJ"),
    ("practical-science-instrument-register.csv", "instrument_id", "instrument_ru", "category", "status", "instrument", "INS"),
    ("practical-science-learning-paths.csv", "path_id", "path_title_ru", "group_code", "status", "learning-path", "LRN"),
    ("practical-science-safety-gates.csv", "gate_id", "hazard_class", "safety_class", "safety_class", "safety-gate", "SAFE"),
    ("scenario-register.csv", "scenario_id", "title_ru", "family", "card_status", "scenario", "SCN"),
    ("century-capability-register.csv", "capability_id", "service_outcome", "domain_code", "lifecycle_state", "century-capability", "CAP"),
    ("source-manifest.csv", "id", "title", "issuer", "link_status", "source-core", "SRC"),
    ("offline-corpus-manifest.csv", "package_id", "title", "category", "download_state", "source-offline", "OFF"),
    ("practical-science-package-register.csv", "package_id", "title", "publisher", "acquisition_state", "source-science", "PKG"),
    ("offline-library/offline-payload-register.csv", "payload_id", "title", "publisher", "release_status", "source-payload", "PAY"),
    ("technology-service-level-register.csv", "service_requirement_id", "minimum_outcome", "service_level", "status", "service-level", "SR"),
    ("capability-crosswalk.csv", "crosswalk_id", "legacy_capability_id", "legacy_capability_id", "mapping_status", "capability-crosswalk", "XW"),
    ("payload-source-crosswalk.csv", "payload_crosswalk_id", "payload_id", "source_relation", "review_state", "payload-crosswalk", "PXW"),
    ("known-gap-register.csv", "gap_id", "gap_ru", "domain", "status", "known-gap", "GAP"),
]

LINK_FIELDS = {
    "parent_id",
    "prerequisite_node_ids",
    "source_package_ids",
    "prerequisite_domains",
    "offline_package_target",
    "practical_project_target",
    "linked_package_ids",
    "manual_package_id",
    "source_ids",
    "source_package_ids",
    "instrument_ids",
    "outcome_node_id",
    "canonical_technology_ids",
    "century_capability_ids",
    "science_domain_ids",
    "dependency_capability_ids",
    "payload_id",
    "source_manifest_ids",
    "offline_package_ids",
    "science_package_ids",
}

MOC_LINKS = {
    "MOC-WATER": "MOCs/MOC_WATER",
    "MOC-FOOD-AGRI": "MOCs/MOC_FOOD_AGRI",
    "MOC-HEALTH": "MOCs/MOC_HEALTH",
    "MOC-SHELTER": "MOCs/MOC_SHELTER",
    "MOC-ENERGY-FUELS": "MOCs/MOC_ENERGY_FUELS",
    "MOC-WORKSHOP": "MOCs/MOC_WORKSHOP",
    "MOC-MATERIALS-CHEMISTRY": "MOCs/MOC_MATERIALS_CHEMISTRY",
    "MOC-MAPS-COMMS": "MOCs/MOC_MAPS_COMMS",
    "MOC-KNOWLEDGE-COMPUTING": "MOCs/MOC_KNOWLEDGE_COMPUTING",
    "MOC-GOVERNANCE": "MOCs/MOC_GOVERNANCE",
    "MOC-PORTUGAL": "MOCs/MOC_PORTUGAL",
    "MOC-SAFETY": "MOCs/MOC_SAFETY",
}


def read_rows(name: str) -> list[dict[str, str]]:
    with (ROOT / name).open("r", encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def clean(value: Optional[str]) -> str:
    return (value or "").replace("\x00", "").strip()


def yaml(value: str) -> str:
    return json.dumps(value, ensure_ascii=False)


def note_filename(prefix: str, identifier: str) -> str:
    safe_id = re.sub(r"[^A-Za-z0-9_.-]+", "-", identifier).strip("-")
    if not safe_id:
        raise ValueError(f"unsafe identifier {identifier!r}")
    return f"{prefix} {safe_id}.md"


def wiki(note: str, label: Optional[str] = None) -> str:
    stem = Path(note).stem
    return f"[[{stem}|{label}]]" if label else f"[[{stem}]]"


def split_ids(value: str) -> list[str]:
    return [part.strip() for part in value.split("|") if part.strip()]


def earliest_horizon(value: str) -> str:
    for code, priority in [
        ("E0", "P0_RED"),
        ("E1", "P0_RED"),
        ("E2", "P1_ORANGE"),
        ("E3", "P2_YELLOW"),
        ("E4", "P3_GREEN"),
        ("E5", "P4_BLUE"),
    ]:
        if code in value:
            return priority
    return "P3_GREEN"


def technology_priority(node_id: str) -> str:
    p0 = (
        "TD-BASE-SAFETY",
        "TD-BASE-SITE",
        "TD-BASE-INVENTORY",
        "TD-WATER-SOURCE",
        "TD-WATER-STORAGE",
        "TD-HEALTH",
        "TD-SHELTER",
        "TD-EXITS",
        "TD-FIRE",
        "TD-MAPS",
        "TD-ROUTES",
        "TD-COMMS",
        "TD-TIME",
        "TD-GOV-ROLES",
        "TD-GOV-SAFEGUARD",
    )
    p1 = (
        "TD-WATER",
        "TD-SANITATION",
        "TD-FOOD",
        "TD-THERMAL",
        "TD-DRAINAGE",
        "TD-ENERGY-LOADS",
        "TD-FUEL-DEMAND",
        "TD-FUEL-STORAGE",
        "TD-KNOWLEDGE-CORPUS",
        "TD-KNOWLEDGE-READERS",
        "TD-KNOWLEDGE-RESTORE",
        "TD-BASE-ARCHIVE",
    )
    p2 = (
        "TD-SEED",
        "TD-CROP",
        "TD-HARVEST",
        "TD-NUTRITION",
        "TD-ENERGY",
        "TD-WORKSHOP",
        "TD-FERT-COMPOST",
        "TD-FERT-CROP",
    )
    p4 = ("TD-ROOT", "TD-GOV-SUCCESSION")
    if node_id in p4:
        return "P4_BLUE"
    if node_id.startswith(p0):
        return "P0_RED"
    if node_id.startswith(p1):
        return "P1_ORANGE"
    if node_id.startswith(p2):
        return "P2_YELLOW"
    return "P3_GREEN"


def inferred_priority(kind: str, row: dict[str, str], planning: dict[str, dict[str, str]]) -> str:
    if kind == "technology":
        node_id = clean(row.get("node_id"))
        if node_id in planning:
            return clean(planning[node_id].get("priority_tier")) or technology_priority(node_id)
        return technology_priority(clean(row.get("node_id")))
    if kind == "scenario":
        return earliest_horizon(clean(row.get("horizon_scope")))
    if kind == "century-capability":
        return "P4_BLUE"
    if kind == "source-offline":
        return {
            "L0": "P0_RED",
            "L1": "P1_ORANGE",
            "L2": "P2_YELLOW",
            "L3": "P3_GREEN",
        }.get(clean(row.get("priority_tier")), "P3_GREEN")
    if kind in {"science-domain", "science-project", "learning-path"}:
        group = clean(row.get("group_code"))
        if group == "HEALTH":
            return "P1_ORANGE"
        if group in {"AGRI", "EARTH", "CIVIL", "OPS"}:
            return "P2_YELLOW"
        return "P3_GREEN"
    if kind == "instrument":
        category = clean(row.get("category"))
        if category in {"HEALTH", "SAFETY", "WATER", "NAVIGATION", "TIME"}:
            return "P1_ORANGE"
        if category in {"METROLOGY", "ENVIRONMENT", "THERMAL", "ENERGY"}:
            return "P2_YELLOW"
        return "P3_GREEN"
    if kind == "safety-gate":
        return "P0_RED"
    if kind == "source-core":
        audience = clean(row.get("audience"))
        title = clean(row.get("title")).lower()
        if audience == "LAY" and any(term in title for term in ("first aid", "emergency", "sismos", "tsunami", "water", "power")):
            return "P0_RED"
        return "P2_YELLOW"
    if kind == "source-science":
        groups = clean(row.get("domain_group_codes"))
        if "HEALTH" in groups:
            return "P1_ORANGE"
        if any(group in groups for group in ("AGRI", "EARTH", "CIVIL", "MECH", "ELEC")):
            return "P2_YELLOW"
        return "P3_GREEN"
    if kind == "source-payload":
        path = clean(row.get("relative_path")).lower()
        title = clean(row.get("title")).lower()
        if any(term in path or term in title for term in ("first-aid", "emergency-care", "sismos", "tsunami")):
            return "P0_RED"
        if any(term in path or term in title for term in ("wash", "water", "excreta", "hygiene", "kiwix")):
            return "P1_ORANGE"
        if any(term in path or term in title for term in ("metrology", "systems-engineering", "wood-handbook")):
            return "P2_YELLOW"
        return "P3_GREEN"
    if kind == "service-level":
        return {
            "SL0": "P0_RED",
            "SL1": "P0_RED",
            "SL2": "P1_ORANGE",
            "SL3": "P2_YELLOW",
            "SL4": "P3_GREEN",
            "SL5": "P3_GREEN",
            "SL6": "P4_BLUE",
        }.get(clean(row.get("service_level")), "P3_GREEN")
    if kind == "capability-crosswalk":
        return "P2_YELLOW"
    if kind == "known-gap":
        return clean(row.get("priority_tier")) or "P3_GREEN"
    return "P3_GREEN"


def audience_for(row: dict[str, str]) -> str:
    if clean(row.get("audience")):
        return clean(row.get("audience"))
    safety = clean(row.get("safety_class"))
    if safety.startswith("S0_") or safety.startswith("S1_"):
        return "LAY_OR_TRAINED_AS_NOTED"
    if safety.startswith("S2_"):
        return "TRAINED_SUPERVISED"
    if safety.startswith("S3_"):
        return "LICENSED_PROFESSIONAL"
    if safety.startswith("S4_"):
        return "REFERENCE_ONLY_NO_HOUSEHOLD_EXECUTION"
    return "UNASSIGNED"


def execution_gate(row: dict[str, str]) -> str:
    safety = clean(row.get("safety_class"))
    if safety.startswith("S4_"):
        return "BLACK_GATE_REFERENCE_ONLY"
    if safety.startswith("S3_"):
        return "BLACK_GATE_LICENSED_ONLY"
    return clean(row.get("release_gate")) or clean(row.get("execution_gate")) or "DENY_UNTIL_REVIEWED"


def field_value(field: str, value: str, lookup: dict[str, str]) -> str:
    value = clean(value)
    if not value:
        return "не заполнено"
    if field in LINK_FIELDS or field in {"moc_ids", "capability_ids"}:
        rendered = []
        for identifier in split_ids(value):
            if identifier in lookup:
                rendered.append(wiki(lookup[identifier], identifier))
            elif identifier in MOC_LINKS:
                rendered.append(f"[[{MOC_LINKS[identifier]}|{identifier}]]")
            elif field == "capability_ids" and f"XW-{identifier}" in lookup:
                rendered.append(wiki(lookup[f"XW-{identifier}"], identifier))
            else:
                rendered.append(identifier)
        return ", ".join(rendered)
    if field == "relative_path":
        return f"[локальный файл](../../../offline-library/{value})"
    return value


def main() -> int:
    OUT.mkdir(parents=True, exist_ok=True)
    planning_rows = read_rows("technology-node-planning-register.csv")
    planning = {clean(row.get("node_id")): row for row in planning_rows if clean(row.get("node_id"))}
    edge_rows = read_rows("technology-dependency-edges.csv")
    edges_by_source: dict[str, list[dict[str, str]]] = defaultdict(list)
    for edge in edge_rows:
        edges_by_source[clean(edge.get("from_node_id"))].append(edge)

    loaded = []
    lookup: dict[str, str] = {}
    for spec in DATASETS:
        source, id_field, title_field, group_field, status_field, kind, prefix = spec
        data = read_rows(source)
        loaded.append((spec, data))
        for row in data:
            identifier = clean(row.get(id_field))
            if not identifier:
                raise ValueError(f"{source}: blank {id_field}")
            if identifier in lookup:
                raise ValueError(f"duplicate global id {identifier}")
            lookup[identifier] = note_filename(prefix, identifier)

    total = 0
    priority_links: dict[str, list[tuple[str, str]]] = defaultdict(list)
    root_indexes: list[tuple[str, str]] = []
    generated_manifest: list[str] = []

    for spec, data in loaded:
        source, id_field, title_field, group_field, status_field, kind, _ = spec
        directory = OUT / kind
        directory.mkdir(parents=True, exist_ok=True)
        grouped: dict[str, list[tuple[str, str]]] = defaultdict(list)
        for row in data:
            identifier = clean(row[id_field])
            title = clean(row.get(title_field)) or identifier
            status = clean(row.get(status_field)) or "CATALOG_ONLY"
            priority = inferred_priority(kind, row, planning)
            note = lookup[identifier]
            body = [
                "---",
                f"id: {yaml(identifier)}",
                f"kind: {yaml(kind)}",
                f"title: {yaml(title)}",
                f"priority_tier: {yaml(priority)}",
                "priority_state: PROVISIONAL_AUTO_REVIEW_REQUIRED",
                f"audience: {yaml(audience_for(row))}",
                f"safety_class: {yaml(clean(row.get('safety_class')) or 'UNASSIGNED')}",
                f"execution_gate: {yaml(execution_gate(row))}",
                f"status: {yaml(status)}",
                "backend_provenance: INTERNAL_MANIFEST_ONLY",
                f"generated_on: {yaml(TODAY)}",
                "generated: true",
                "instruction_state: CATALOG_ONLY_NOT_EXECUTABLE",
                "---",
                "",
                f"# {title}",
                "",
                "> [!warning] Каталожная карточка",
                "> Это место в карте знаний. Оно не доказывает наличие вещи, проверенный метод, квалификацию или разрешение выполнять работу.",
                "",
                "## Краткий статус",
                "",
                f"- **ID:** `{identifier}`",
                f"- **Статус:** `{status}`",
                f"- **Приоритет:** `{priority}`",
                f"- **Аудитория:** `{audience_for(row)}`",
                f"- **Класс безопасности:** `{clean(row.get('safety_class')) or 'UNASSIGNED'}`",
                f"- **Допуск:** `{execution_gate(row)}`",
                "",
                "<details>",
                "<summary>Технические данные backend (для аудита)</summary>",
                "",
                f"<!-- backend-source: {source} -->",
            ]
            for field, value in row.items():
                body.append(f"- **{field}:** {field_value(field, value, lookup)}")
            body.extend(["", "</details>"])
            if kind == "technology" and identifier in planning:
                body.extend(
                    [
                        "",
                        "<details>",
                        "<summary>Служебные поля планирования</summary>",
                        "",
                    ]
                )
                for field, value in planning[identifier].items():
                    if field not in {"plan_id", "node_id"}:
                        body.append(f"- **{field}:** {field_value(field, value, lookup)}")
                body.extend(["", "</details>"])
            if kind == "technology" and edges_by_source.get(identifier):
                body.extend(
                    [
                        "",
                        "<details>",
                        "<summary>Типизированные зависимости</summary>",
                        "",
                        "| Роль | Узел | Service level | Условие / группа |",
                        "|---|---|---|---|",
                    ]
                )
                for edge in edges_by_source[identifier]:
                    target_id = clean(edge.get("to_node_id"))
                    target = wiki(lookup[target_id], target_id) if target_id in lookup else target_id
                    condition = clean(edge.get("alternative_group")) or clean(edge.get("applicable_if")) or "—"
                    body.append(
                        f"| {clean(edge.get('edge_role'))} | {target} | {clean(edge.get('service_level'))} | {condition} |"
                    )
                body.extend(["", "</details>"])
            if execution_gate(row).startswith("BLACK_GATE"):
                body.extend(
                    [
                        "",
                        "> [!danger] Закрытая ветка",
                        "> Сохраняются распознавание опасности, профессиональная теория и аварийный маршрут. Домашнее исполнение не разрешено.",
                    ]
                )
            body.extend(
                [
                    "",
                    "## Связи и наполнение",
                    "",
                    "- Добавлять проверенные постоянные заметки рядом, не редактируя generated-карточку.",
                    "- До инструкции нужны точный источник, локальная применимость, safety review и доказательные критерии.",
                    "",
                ]
            )
            path = directory / note
            path.write_text("\n".join(body), encoding="utf-8")
            relative = path.relative_to(VAULT).as_posix()
            generated_manifest.append(relative)
            group = clean(row.get(group_field)) or "Без группы"
            label = f"{identifier} — {title}"
            grouped[group].append((note, label))
            priority_links[priority].append((note, label))
            total += 1

        index_path = directory / "_INDEX.md"
        lines = [
            "---",
            "kind: MOC_GENERATED",
            "generated: true",
            "instruction_state: CATALOG_ONLY_NOT_EXECUTABLE",
            "---",
            "",
            f"# {kind}: полный перечень",
            "",
            "> [!warning] Перечень не равен готовности.",
            "",
        ]
        for group in sorted(grouped, key=str.casefold):
            lines.extend([f"## {group}", ""])
            for note, label in sorted(grouped[group], key=lambda item: item[1].casefold()):
                lines.append(f"- {wiki(note, label)}")
            lines.append("")
        index_path.write_text("\n".join(lines), encoding="utf-8")
        root_indexes.append((kind, index_path.relative_to(VAULT).with_suffix("").as_posix()))

    priority_path = OUT / "PRIORITY_INDEX.md"
    priority_order = ["P0_RED", "P1_ORANGE", "P2_YELLOW", "P3_GREEN", "P4_BLUE"]
    lines = [
        "---",
        "kind: MOC_PRIORITY",
        "generated: true",
        "priority_state: PROVISIONAL_AUTO_REVIEW_REQUIRED",
        "---",
        "",
        "# Служебный индекс приоритетов",
        "",
        "> [!warning] Технический backend, не очередь действий. Пользовательская очередь: [[20 — Рабочие разделы/02 — Первые 72 часа|Что нужно обеспечить в первые 72 часа]].",
        "",
        "- **P0 RED:** секунды–72 часа; жизнь, немедленная безопасность, вода, пожар/CO, лекарства, связь и учёт.",
        "- **P1 ORANGE:** 3–14 дней; санитария, питание, температура, карты, базовая энергия и восстановление документов.",
        "- **P2 YELLOW:** 15–90 дней; ротация, выращивание, мастерская, резервные системы и обучение дублёров.",
        "- **P3 GREEN:** 3 месяца–15 лет; производство, агросистема, материалы, инфраструктура и профессиональные знания.",
        "- **P4 BLUE:** 15–100 лет; преемственность, образование, архивы и институты.",
        "- **BLACK GATE:** показывается внутри карточки отдельно от приоритета; S3/S4 нельзя трактовать как household instruction.",
        "",
    ]
    for priority in priority_order:
        lines.extend([f"## {priority}", ""])
        for note, label in sorted(priority_links.get(priority, []), key=lambda item: item[1].casefold()):
            lines.append(f"- {wiki(note, label)}")
        lines.append("")
    priority_path.write_text("\n".join(lines), encoding="utf-8")

    root_path = OUT / "INDEX.md"
    root_lines = [
        "---",
        "kind: MOC_GENERATED_ROOT",
        "generated: true",
        "instruction_state: CATALOG_ONLY_NOT_EXECUTABLE",
        "---",
        "",
        "# Технический каталог backend",
        "",
        f"Атомарных карточек: **{total}**.",
        "",
        "> [!warning] Это служебный слой для аудита и связей. Основная работа начинается с [[20 — Рабочие разделы/00 — Панели автономного кита|рабочих разделов]].",
        "",
        "- [[PRIORITY_INDEX|Служебный индекс приоритетов]]",
    ]
    for kind, index_stem in root_indexes:
        root_lines.append(f"- [[{index_stem}|{kind}]]")
    root_lines.append("- [[technology/_EDGE_SUMMARY|семантика технологических рёбер]]")
    root_lines.extend(
        [
            "",
            "## Правило",
            "",
            "Сначала проверяется полнота перечня и приоритет. Затем создаются постоянные источниковые заметки и безопасные production packages. Generated-карточки не являются инструкциями.",
            "",
        ]
    )
    root_path.write_text("\n".join(root_lines), encoding="utf-8")

    edge_summary = OUT / "technology" / "_EDGE_SUMMARY.md"
    edge_counts = Counter(clean(edge.get("edge_role")) for edge in edge_rows)
    level_counts = Counter(clean(edge.get("service_level")) for edge in edge_rows)
    edge_lines = [
        "---",
        "kind: MOC_TECHNOLOGY_EDGES",
        "generated: true",
        "instruction_state: CATALOG_ONLY_NOT_EXECUTABLE",
        "---",
        "",
        "# Семантика технологических зависимостей",
        "",
        f"Типизированных рёбер: **{len(edge_rows)}**. Человекочитаемый обзор: [[20 — Рабочие разделы/07 — Области знаний и систем|области знаний и систем]].",
        "",
        "> [!warning] Роли и service levels пока PROVISIONAL_AUTO_REVIEW_REQUIRED и не являются разрешением на работу.",
        "",
        "## По роли",
        "",
    ]
    for role, count in sorted(edge_counts.items()):
        edge_lines.append(f"- **{role}:** {count}")
    edge_lines.extend(["", "## По service level", ""])
    for level, count in sorted(level_counts.items()):
        edge_lines.append(f"- **{level}:** {count}")
    edge_lines.extend(["", "## Корневые зависимости", ""])
    for edge in edges_by_source.get("TD-ROOT", []):
        target_id = clean(edge.get("to_node_id"))
        target = wiki(lookup[target_id], target_id) if target_id in lookup else target_id
        edge_lines.append(
            f"- **{clean(edge.get('edge_role'))} / {clean(edge.get('service_level'))}:** {target}"
            + (f" — {clean(edge.get('applicable_if'))}" if clean(edge.get("applicable_if")) else "")
        )
    edge_lines.append("")
    edge_summary.write_text("\n".join(edge_lines), encoding="utf-8")

    manifest = OUT / "_GENERATED_MANIFEST.txt"
    manifest.write_text(
        "\n".join(
            [
                "# generated catalog manifest",
                f"generated_on={TODAY}",
                f"atomic_note_count={total}",
                "generator=build_obsidian_catalog.py",
                "",
            ]
            + sorted(generated_manifest)
        )
        + "\n",
        encoding="utf-8",
    )
    print(f"obsidian_catalog_ok notes={total} datasets={len(DATASETS)} root={OUT}")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (OSError, csv.Error, KeyError, ValueError) as exc:
        print(f"obsidian_catalog_error {exc}", file=sys.stderr)
        raise SystemExit(1)
