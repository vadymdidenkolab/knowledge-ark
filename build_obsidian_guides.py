#!/usr/bin/env python3
"""Build read-only, human-named Obsidian mirrors of root narrative guides.

The source-of-truth files stay in the repository root.  This generator owns
only files recorded in the guide-layer ``.generated-guides-manifest.json``.
It can migrate its own former ``10_GUIDES`` output, but never deletes an
unmanifested file or a file without this generator's ownership markers.
It never treats a CSV, workbook, HTML page, or folder as a copied user guide.

Python standard library only; compatible with Python 3.9+.
"""

from __future__ import annotations

import hashlib
import html
import json
import os
import posixpath
import re
import tempfile
from pathlib import Path
from typing import Dict, Iterable, List, Mapping, MutableMapping, Optional, Sequence, Set, Tuple
from urllib.parse import quote, unquote, urlsplit, urlunsplit


ROOT = Path(__file__).resolve().parent
VAULT_DIR = ROOT / "Obsidian-Vault"
GUIDES_VAULT_NAME = "10 — Руководства"
LEGACY_GUIDES_VAULT_NAME = "10_GUIDES"
GUIDES_DIR = VAULT_DIR / GUIDES_VAULT_NAME
LEGACY_GUIDES_DIR = VAULT_DIR / LEGACY_GUIDES_VAULT_NAME
DATA_REGISTERS_DIR = VAULT_DIR / "80_DATA_REGISTERS"
MANIFEST_PATH = GUIDES_DIR / ".generated-guides-manifest.json"
LEGACY_MANIFEST_PATH = LEGACY_GUIDES_DIR / ".generated-guides-manifest.json"
GENERATOR_ID = "build_obsidian_guides.py"
INSTRUCTION_STATE = "MIRROR_ONLY_SOURCE_STATUS_UNCHANGED"
INDEX_FILENAME = "00 — Путеводитель по руководствам.md"

NUMBERED_MD_RE = re.compile(r"^(?:0[1-9]|1[0-9]|2[0-4])_.*\.md$")
EXTRA_MD_NAMES = {
    "README.md",
    "PRACTICAL_SCIENCE_WORKBOOK_QA.md",
    "VISUALIZATION_QA.md",
}
HTML_SOURCE_NAMES = (
    "START_HERE.html",
    "SEED_BANK_ORDER_RU.html",
    "SEED_CALORIE_LAYER_RU.html",
    "SEED_PURCHASE_LIST_RU.html",
)

# The source filenames remain stable machine identifiers.  The generated vault
# filenames are deliberately user-facing, sortable, and readable in Explorer.
GUIDE_FILENAMES: Mapping[str, str] = {
    "README.md": "00.1 — О комплекте.md",
    "START_HERE.html": "00.2 — Быстрый старт.md",
    "01_MASTER_BLUEPRINT_RU.md": "01 — Мастер-каркас автономного кита.md",
    "02_PERSONALIZATION_RU.md": "02 — Персонализация под людей и площадку.md",
    "03_INVENTORY_SCHEMA_RU.md": "03 — Инвентарь предметов и запасов.md",
    "04_SOURCE_REGISTER_RU.md": "04 — Источники и проверка происхождения.md",
    "05_BUILD_ROADMAP_RU.md": "05 — Дорожная карта сборки.md",
    "06_COVERAGE_MATRIX_RU.md": "06 — Матрица полноты системы.md",
    "VISUALIZATION_QA.md": "06.1 — Проверка интерактивной схемы.md",
    "07_MATERIAL_TECHNICAL_CONTOUR_RU.md": "07 — Материально-технический контур.md",
    "SEED_BANK_ORDER_RU.html": "07.1 — Овощной семенной фонд.md",
    "SEED_CALORIE_LAYER_RU.html": "07.2 — Калорийный семенной и посадочный слой.md",
    "SEED_PURCHASE_LIST_RU.html": "07.3 — Список закупки семян.md",
    "08_MEDICAL_KNOWLEDGE_CONTOUR_RU.md": "08 — Медицинский контур знаний.md",
    "09_MEDICAL_SOURCE_CATALOG_RU.md": "09 — Медицинские источники.md",
    "10_INFORMATION_AND_ARCHIVE_CONTOUR_RU.md": "10 — Информация и архив.md",
    "11_FIRST_AID_KIT_BASELINE_RU.md": "11 — Физические аптечки.md",
    "12_QA_AND_LIMITS_RU.md": "12 — Проверка качества и границы.md",
    "13_MAPS_GEODATA_NAVIGATION_RU.md": "13 — Карты, геоданные и маршруты.md",
    "14_GROUP_1_TO_7_OPERATIONS_RU.md": "14 — Группа от одного до семи человек.md",
    "15_ALL_HAZARDS_A_TO_Z_INDEX_RU.md": "15 — Индекс нештатных ситуаций от А до Я.md",
    "16_CENTURY_CONTINUITY_RU.md": "16 — Непрерывность на 15–100 лет.md",
    "17_OFFLINE_LIBRARY_100Y_RU.md": "17 — Офлайн-библиотека на 100 лет.md",
    "18_E5_REGISTERS_AND_GATES_RU.md": "18 — Реестры и допуски столетнего контура.md",
    "19_OFFLINE_CORPUS_RESEARCH_RU.md": "19 — Исследование офлайн-корпуса.md",
    "20_PRACTICAL_SCIENCE_PRESERVATION_RU.md": "20 — Сохранение практической науки.md",
    "PRACTICAL_SCIENCE_WORKBOOK_QA.md": "20.1 — Проверка атласа практической науки.md",
    "21_PRACTICAL_SCIENCE_SOURCE_RESEARCH_RU.md": "21 — Источники практической науки.md",
    "22_TOTAL_ISOLATION_READINESS_AUDIT_RU.md": "22 — Аудит готовности к полной изоляции.md",
    "23_TECHNOLOGY_DEPENDENCY_TREE_RU.md": "23 — Дерево технологических зависимостей.md",
    "24_MASTER_CATALOG_STATUS_RU.md": "24 — Мастер-статус каталога.md",
}

# Context blocks are authored, not inferred by numeric adjacency.  A link can
# therefore guide the reader back to a prerequisite or audit rather than to the
# next filename in the folder.
GUIDE_CONTEXT: Mapping[str, Mapping[str, object]] = {
    "README.md": {
        "purpose": "понять границы, статус и маршруты по всему комплекту",
        "related": ("START_HERE.html", "24_MASTER_CATALOG_STATUS_RU.md", "22_TOTAL_ISOLATION_READINESS_AUDIT_RU.md"),
        "when": "при первом знакомстве и перед любым заявлением о готовности",
        "next": "START_HERE.html",
    },
    "START_HERE.html": {
        "purpose": "быстро выбрать нужный контур по времени и ситуации",
        "related": ("README.md", "15_ALL_HAZARDS_A_TO_Z_INDEX_RU.md", "24_MASTER_CATALOG_STATUS_RU.md"),
        "when": "в самом начале работы или когда нужен кратчайший маршрут",
        "next": "24_MASTER_CATALOG_STATUS_RU.md",
    },
    "01_MASTER_BLUEPRINT_RU.md": {
        "purpose": "увидеть целевую архитектуру кита и связи между контурами",
        "related": ("06_COVERAGE_MATRIX_RU.md", "23_TECHNOLOGY_DEPENDENCY_TREE_RU.md", "24_MASTER_CATALOG_STATUS_RU.md"),
        "when": "при проектировании, расширении или пересборке системы",
        "next": "02_PERSONALIZATION_RU.md",
    },
    "02_PERSONALIZATION_RU.md": {
        "purpose": "привязать общую систему к людям, здоровью, рискам и площадке",
        "related": ("03_INVENTORY_SCHEMA_RU.md", "13_MAPS_GEODATA_NAVIGATION_RU.md", "14_GROUP_1_TO_7_OPERATIONS_RU.md"),
        "when": "до закупок, расчёта запасов и выбора локальных маршрутов",
        "next": "03_INVENTORY_SCHEMA_RU.md",
    },
    "03_INVENTORY_SCHEMA_RU.md": {
        "purpose": "учитывать фактическое наличие, количество, сроки, место и проверку запасов",
        "related": ("02_PERSONALIZATION_RU.md", "07_MATERIAL_TECHNICAL_CONTOUR_RU.md", "11_FIRST_AID_KIT_BASELINE_RU.md"),
        "when": "при инвентаризации, закупке, ротации и ежегодной сверке",
        "next": "11_FIRST_AID_KIT_BASELINE_RU.md",
    },
    "04_SOURCE_REGISTER_RU.md": {
        "purpose": "фиксировать происхождение, надёжность и статус источников",
        "related": ("09_MEDICAL_SOURCE_CATALOG_RU.md", "19_OFFLINE_CORPUS_RESEARCH_RU.md", "21_PRACTICAL_SCIENCE_SOURCE_RESEARCH_RU.md"),
        "when": "перед скачиванием, архивацией или доверием критической инструкции",
        "next": "19_OFFLINE_CORPUS_RESEARCH_RU.md",
    },
    "05_BUILD_ROADMAP_RU.md": {
        "purpose": "превратить целевую архитектуру в очерёдность сборки и проверок",
        "related": ("06_COVERAGE_MATRIX_RU.md", "22_TOTAL_ISOLATION_READINESS_AUDIT_RU.md", "24_MASTER_CATALOG_STATUS_RU.md"),
        "when": "при планировании следующего цикла работ и расстановке приоритетов",
        "next": "24_MASTER_CATALOG_STATUS_RU.md",
    },
    "06_COVERAGE_MATRIX_RU.md": {
        "purpose": "найти пустоты, неравномерную глубину и непокрытые связи между контурами",
        "related": ("01_MASTER_BLUEPRINT_RU.md", "22_TOTAL_ISOLATION_READINESS_AUDIT_RU.md", "24_MASTER_CATALOG_STATUS_RU.md"),
        "when": "при аудите полноты и перед закрытием очередной версии",
        "next": "22_TOTAL_ISOLATION_READINESS_AUDIT_RU.md",
    },
    "VISUALIZATION_QA.md": {
        "purpose": "понять, что именно проверено в интерактивной схеме и где её границы",
        "related": ("06_COVERAGE_MATRIX_RU.md", "12_QA_AND_LIMITS_RU.md", "README.md"),
        "when": "перед использованием визуализации как доказательства полноты",
        "next": "06_COVERAGE_MATRIX_RU.md",
    },
    "07_MATERIAL_TECHNICAL_CONTOUR_RU.md": {
        "purpose": "связать воду, энергию, укрытие, инструменты, ремонт и производство",
        "related": ("03_INVENTORY_SCHEMA_RU.md", "23_TECHNOLOGY_DEPENDENCY_TREE_RU.md", "13_MAPS_GEODATA_NAVIGATION_RU.md"),
        "when": "при выборе, сборке и обслуживании физических систем",
        "next": "23_TECHNOLOGY_DEPENDENCY_TREE_RU.md",
    },
    "SEED_BANK_ORDER_RU.html": {
        "purpose": "сформировать многолетний овощной семенной модуль без подмены плана фактом закупки",
        "related": ("SEED_CALORIE_LAYER_RU.html", "SEED_PURCHASE_LIST_RU.html", "07_MATERIAL_TECHNICAL_CONTOUR_RU.md"),
        "when": "при выборе видов, сортов, резерва и цикла обновления семян",
        "next": "SEED_CALORIE_LAYER_RU.html",
    },
    "SEED_CALORIE_LAYER_RU.html": {
        "purpose": "рассчитать калорийные культуры, посадочный материал, площадь, воду и ротацию",
        "related": ("SEED_BANK_ORDER_RU.html", "SEED_PURCHASE_LIST_RU.html", "07_MATERIAL_TECHNICAL_CONTOUR_RU.md"),
        "when": "при планировании реального пищевого резерва, а не только овощного ассортимента",
        "next": "SEED_BANK_ORDER_RU.html",
    },
    "SEED_PURCHASE_LIST_RU.html": {
        "purpose": "свести планируемые позиции закупки, не выдавая их за фактически купленные или хранящиеся",
        "related": ("SEED_BANK_ORDER_RU.html", "SEED_CALORIE_LAYER_RU.html", "03_INVENTORY_SCHEMA_RU.md"),
        "when": "перед сверкой цен, количеств, сроков и статуса каждой позиции",
        "next": "SEED_BANK_ORDER_RU.html",
    },
    "08_MEDICAL_KNOWLEDGE_CONTOUR_RU.md": {
        "purpose": "организовать медицинские знания, триаж, профилактику и границы самопомощи",
        "related": ("09_MEDICAL_SOURCE_CATALOG_RU.md", "11_FIRST_AID_KIT_BASELINE_RU.md", "12_QA_AND_LIMITS_RU.md"),
        "when": "при подготовке медицинского контура; в острой ситуации сначала ищите нужный протокол",
        "next": "11_FIRST_AID_KIT_BASELINE_RU.md",
    },
    "09_MEDICAL_SOURCE_CATALOG_RU.md": {
        "purpose": "выбирать и проверять авторитетные медицинские первоисточники",
        "related": ("08_MEDICAL_KNOWLEDGE_CONTOUR_RU.md", "11_FIRST_AID_KIT_BASELINE_RU.md", "04_SOURCE_REGISTER_RU.md"),
        "when": "перед офлайн-архивацией, обновлением или переводом медицинских материалов",
        "next": "08_MEDICAL_KNOWLEDGE_CONTOUR_RU.md",
    },
    "10_INFORMATION_AND_ARCHIVE_CONTOUR_RU.md": {
        "purpose": "задать архитектуру офлайн-доступа, копий, проверки и восстановления архива",
        "related": ("17_OFFLINE_LIBRARY_100Y_RU.md", "19_OFFLINE_CORPUS_RESEARCH_RU.md", "13_MAPS_GEODATA_NAVIGATION_RU.md"),
        "when": "до копирования библиотеки на носители и при каждой ревизии копий",
        "next": "17_OFFLINE_LIBRARY_100Y_RU.md",
    },
    "11_FIRST_AID_KIT_BASELINE_RU.md": {
        "purpose": "перевести медицинскую модель в физические аптечки с проверкой наличия и сроков",
        "related": ("08_MEDICAL_KNOWLEDGE_CONTOUR_RU.md", "09_MEDICAL_SOURCE_CATALOG_RU.md", "03_INVENTORY_SCHEMA_RU.md"),
        "when": "при сборке, укладке, инвентаризации и ротации аптечек",
        "next": "08_MEDICAL_KNOWLEDGE_CONTOUR_RU.md",
    },
    "12_QA_AND_LIMITS_RU.md": {
        "purpose": "отличать план, зеркало, проверенную инструкцию, физическое наличие и допущенную готовность",
        "related": ("22_TOTAL_ISOLATION_READINESS_AUDIT_RU.md", "23_TECHNOLOGY_DEPENDENCY_TREE_RU.md", "24_MASTER_CATALOG_STATUS_RU.md"),
        "when": "перед присвоением статуса ready, verified, released или allow",
        "next": "22_TOTAL_ISOLATION_READINESS_AUDIT_RU.md",
    },
    "13_MAPS_GEODATA_NAVIGATION_RU.md": {
        "purpose": "подготовить офлайн-карты, геоданные, маршруты, бумажные дубли и проверку на местности",
        "related": ("02_PERSONALIZATION_RU.md", "14_GROUP_1_TO_7_OPERATIONS_RU.md", "10_INFORMATION_AND_ARCHIVE_CONTOUR_RU.md"),
        "when": "после фиксации муниципалитета, точек и рисков; затем регулярно в поле",
        "next": "14_GROUP_1_TO_7_OPERATIONS_RU.md",
    },
    "14_GROUP_1_TO_7_OPERATIONS_RU.md": {
        "purpose": "задать роли, дублёров, правила связи, решений, конфликтов и передачи ответственности",
        "related": ("02_PERSONALIZATION_RU.md", "13_MAPS_GEODATA_NAVIGATION_RU.md", "18_E5_REGISTERS_AND_GATES_RU.md"),
        "when": "при формировании группы, смене состава и перед учениями",
        "next": "13_MAPS_GEODATA_NAVIGATION_RU.md",
    },
    "15_ALL_HAZARDS_A_TO_Z_INDEX_RU.md": {
        "purpose": "найти сценарий риска и перейти к нужным контурам, маршрутам и проверкам",
        "related": ("06_COVERAGE_MATRIX_RU.md", "13_MAPS_GEODATA_NAVIGATION_RU.md", "22_TOTAL_ISOLATION_READINESS_AUDIT_RU.md"),
        "when": "при выборе сценария подготовки или в начале реакции на конкретную угрозу",
        "next": "22_TOTAL_ISOLATION_READINESS_AUDIT_RU.md",
    },
    "16_CENTURY_CONTINUITY_RU.md": {
        "purpose": "учесть смену поколений, ремонтопригодность, ротацию запасов, обучение и преемственность",
        "related": ("17_OFFLINE_LIBRARY_100Y_RU.md", "18_E5_REGISTERS_AND_GATES_RU.md", "20_PRACTICAL_SCIENCE_PRESERVATION_RU.md"),
        "when": "после закрытия неотложных рисков и при каждом долгосрочном цикле",
        "next": "18_E5_REGISTERS_AND_GATES_RU.md",
    },
    "17_OFFLINE_LIBRARY_100Y_RU.md": {
        "purpose": "сформировать состав, форматы, копии и процедуры долговечной офлайн-библиотеки",
        "related": ("10_INFORMATION_AND_ARCHIVE_CONTOUR_RU.md", "19_OFFLINE_CORPUS_RESEARCH_RU.md", "21_PRACTICAL_SCIENCE_SOURCE_RESEARCH_RU.md"),
        "when": "при сборке, копировании, валидации и миграции офлайн-корпуса",
        "next": "19_OFFLINE_CORPUS_RESEARCH_RU.md",
    },
    "18_E5_REGISTERS_AND_GATES_RU.md": {
        "purpose": "задать реестры, роли, события и допуски для столетнего контура",
        "related": ("16_CENTURY_CONTINUITY_RU.md", "14_GROUP_1_TO_7_OPERATIONS_RU.md", "24_MASTER_CATALOG_STATUS_RU.md"),
        "when": "при настройке управления, передачи ролей и прохождении контрольных ворот",
        "next": "16_CENTURY_CONTINUITY_RU.md",
    },
    "19_OFFLINE_CORPUS_RESEARCH_RU.md": {
        "purpose": "определить, какой корпус документов нужен, где его брать и как оценивать пробелы",
        "related": ("17_OFFLINE_LIBRARY_100Y_RU.md", "04_SOURCE_REGISTER_RU.md", "21_PRACTICAL_SCIENCE_SOURCE_RESEARCH_RU.md"),
        "when": "до массового скачивания и при каждом пересмотре приоритетов корпуса",
        "next": "17_OFFLINE_LIBRARY_100Y_RU.md",
    },
    "20_PRACTICAL_SCIENCE_PRESERVATION_RU.md": {
        "purpose": "сохранить практическую науку как воспроизводимые знания, инструменты и учебные маршруты",
        "related": ("21_PRACTICAL_SCIENCE_SOURCE_RESEARCH_RU.md", "23_TECHNOLOGY_DEPENDENCY_TREE_RU.md", "PRACTICAL_SCIENCE_WORKBOOK_QA.md"),
        "when": "при построении офлайн-атласа навыков и проверке его практичности",
        "next": "21_PRACTICAL_SCIENCE_SOURCE_RESEARCH_RU.md",
    },
    "PRACTICAL_SCIENCE_WORKBOOK_QA.md": {
        "purpose": "увидеть метод и результаты проверки табличного атласа практической науки",
        "related": ("20_PRACTICAL_SCIENCE_PRESERVATION_RU.md", "21_PRACTICAL_SCIENCE_SOURCE_RESEARCH_RU.md", "12_QA_AND_LIMITS_RU.md"),
        "when": "перед доверием к атласу и после его значимых изменений",
        "next": "20_PRACTICAL_SCIENCE_PRESERVATION_RU.md",
    },
    "21_PRACTICAL_SCIENCE_SOURCE_RESEARCH_RU.md": {
        "purpose": "отобрать первичные источники и закрыть пробелы в практической науке",
        "related": ("20_PRACTICAL_SCIENCE_PRESERVATION_RU.md", "19_OFFLINE_CORPUS_RESEARCH_RU.md", "04_SOURCE_REGISTER_RU.md"),
        "when": "перед архивацией учебников, стандартов, чертежей и процедур",
        "next": "20_PRACTICAL_SCIENCE_PRESERVATION_RU.md",
    },
    "22_TOTAL_ISOLATION_READINESS_AUDIT_RU.md": {
        "purpose": "честно отделить собранное от несобранного, проверенное от плана и выпущенное от backlog",
        "related": ("06_COVERAGE_MATRIX_RU.md", "12_QA_AND_LIMITS_RU.md", "24_MASTER_CATALOG_STATUS_RU.md"),
        "when": "перед заявлением о готовности к изоляции и после каждого крупного цикла доработки",
        "next": "24_MASTER_CATALOG_STATUS_RU.md",
    },
    "23_TECHNOLOGY_DEPENDENCY_TREE_RU.md": {
        "purpose": "увидеть предпосылки, измерения, инструменты, риски и контрольные ворота до любой технологии",
        "related": ("07_MATERIAL_TECHNICAL_CONTOUR_RU.md", "20_PRACTICAL_SCIENCE_PRESERVATION_RU.md", "24_MASTER_CATALOG_STATUS_RU.md"),
        "when": "до перехода к новой технологии, веществу, механизму или ремонтной цепочке",
        "next": "07_MATERIAL_TECHNICAL_CONTOUR_RU.md",
    },
    "24_MASTER_CATALOG_STATUS_RU.md": {
        "purpose": "увидеть текущий честный статус каталога, активные реестры, пробелы и следующие работы",
        "related": ("22_TOTAL_ISOLATION_READINESS_AUDIT_RU.md", "23_TECHNOLOGY_DEPENDENCY_TREE_RU.md", "05_BUILD_ROADMAP_RU.md"),
        "when": "в начале каждой рабочей сессии и перед любым выводом о полноте или готовности",
        "next": "22_TOTAL_ISOLATION_READINESS_AUDIT_RU.md",
    },
}

MARKDOWN_LINK_RE = re.compile(
    r"(?P<image>!?)\[(?P<label>[^\]\n]+)\]"
    r"\((?P<target><[^>\n]+>|[^\s)\n]+)(?P<title>\s+(?:\"[^\"]*\"|'[^']*'))?\)"
)
WIKILINK_RE = re.compile(r"\[\[(?P<target>[^\]|]+)(?:\|(?P<label>[^\]]+))?\]\]")
HTML_ATTR_RE = re.compile(
    r"(?P<name>\b(?:href|src))\s*=\s*(?P<quote>[\"'])(?P<target>.*?)(?P=quote)",
    re.IGNORECASE | re.DOTALL,
)
HTML_ANCHOR_RE = re.compile(
    r"<a\b(?P<attrs>[^>]*)>(?P<body>.*?)</a\s*>",
    re.IGNORECASE | re.DOTALL,
)
HREF_ONLY_RE = re.compile(
    r"(?P<prefix>\bhref\s*=\s*)(?P<quote>[\"'])(?P<target>.*?)(?P=quote)",
    re.IGNORECASE | re.DOTALL,
)
SCRIPT_STYLE_RE = re.compile(
    r"<(?:script|style)\b[^>]*>.*?</(?:script|style)\s*>",
    re.IGNORECASE | re.DOTALL,
)
EVENT_ATTR_RE = re.compile(
    r"\s+on[a-z0-9_-]+\s*=\s*(?:\"[^\"]*\"|'[^']*'|[^\s>]+)",
    re.IGNORECASE,
)
STYLE_ATTR_RE = re.compile(
    r"\s+style\s*=\s*(?:\"[^\"]*\"|'[^']*'|[^\s>]+)",
    re.IGNORECASE,
)


class BuildError(RuntimeError):
    """Raised when a safe, deterministic mirror build is not possible."""


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def yaml_string(value: str) -> str:
    """Return a JSON string, which is also a valid YAML quoted scalar."""

    return json.dumps(value, ensure_ascii=False)


def discover_markdown_sources() -> List[Path]:
    sources = [
        path
        for path in ROOT.glob("*.md")
        if path.name in EXTRA_MD_NAMES or NUMBERED_MD_RE.fullmatch(path.name)
    ]

    expected_numbered = {f"{number:02d}" for number in range(1, 25)}
    found_numbered = {path.name[:2] for path in sources if NUMBERED_MD_RE.fullmatch(path.name)}
    missing_prefixes = sorted(expected_numbered - found_numbered)
    missing_extras = sorted(name for name in EXTRA_MD_NAMES if not (ROOT / name).is_file())
    if missing_prefixes or missing_extras:
        details = []
        if missing_prefixes:
            details.append("numbered prefixes " + ", ".join(missing_prefixes))
        if missing_extras:
            details.append("named files " + ", ".join(missing_extras))
        raise BuildError("required Markdown sources missing: " + "; ".join(details))

    def sort_key(path: Path) -> Tuple[int, str]:
        if path.name == "README.md":
            return (0, path.name)
        if NUMBERED_MD_RE.fullmatch(path.name):
            return (1, path.name)
        return (2, path.name)

    return sorted(sources, key=sort_key)


def discover_html_sources() -> List[Path]:
    paths = [ROOT / name for name in HTML_SOURCE_NAMES]
    missing = [path.name for path in paths if not path.is_file()]
    if missing:
        raise BuildError("required HTML sources missing: " + ", ".join(missing))
    return paths


def mirror_name_for_source(source: Path) -> str:
    try:
        return GUIDE_FILENAMES[source.name]
    except KeyError as exc:
        raise BuildError(f"no human guide filename configured for {source.name}") from exc


def legacy_mirror_name_for_source(source: Path) -> str:
    """Return the generator's pre-migration filename for audit output."""

    if source.suffix.lower() == ".html":
        return source.with_suffix(".md").name
    return source.name


def build_mirror_map(sources: Sequence[Path]) -> Dict[str, str]:
    source_names = {source.name for source in sources}
    configured_names = set(GUIDE_FILENAMES)
    if source_names != configured_names:
        missing = sorted(source_names - configured_names)
        extra = sorted(configured_names - source_names)
        raise BuildError(
            "human filename map does not match discovered sources: "
            f"missing={missing or 'none'} extra={extra or 'none'}"
        )
    context_names = set(GUIDE_CONTEXT)
    if source_names != context_names:
        missing = sorted(source_names - context_names)
        extra = sorted(context_names - source_names)
        raise BuildError(
            "guide context map does not match discovered sources: "
            f"missing={missing or 'none'} extra={extra or 'none'}"
        )

    mapping: Dict[str, str] = {}
    mirror_names: Set[str] = set()
    for source in sources:
        relative = source.relative_to(ROOT).as_posix()
        mirror_name = mirror_name_for_source(source)
        if mirror_name in mirror_names:
            raise BuildError(f"mirror filename collision: {mirror_name}")
        mirror_names.add(mirror_name)
        mapping[relative] = mirror_name
    return mapping


def split_local_target(target: str) -> Optional[Tuple[str, str, str]]:
    """Return decoded relative path, query, fragment; None means non-local."""

    raw = target[1:-1] if target.startswith("<") and target.endswith(">") else target
    if not raw or raw.startswith(("#", "//")):
        return None
    parsed = urlsplit(raw)
    if parsed.scheme or parsed.netloc or parsed.path.startswith("/"):
        return None
    decoded_path = unquote(parsed.path)
    if not decoded_path:
        return None
    normalized = posixpath.normpath(decoded_path)
    if normalized == ".":
        return None
    return normalized, parsed.query, parsed.fragment


def source_target_key(source: Path, normalized_target: str) -> Optional[str]:
    absolute = (source.parent / normalized_target).resolve()
    try:
        return absolute.relative_to(ROOT).as_posix()
    except ValueError:
        return None


def target_path_suffix(target: str) -> str:
    raw = target[1:-1] if target.startswith("<") and target.endswith(">") else target
    return Path(unquote(urlsplit(raw).path)).suffix.lower()


def data_register_mirror_name(source_key: str) -> str:
    """Map root/nested CSV paths to the shared 80_DATA_REGISTERS convention."""

    if not source_key.lower().endswith(".csv"):
        raise BuildError(f"not a CSV source key: {source_key}")
    without_suffix = source_key[:-4]
    return without_suffix.replace("/", "__") + ".md"


def register_data_mapping(
    source_key: Optional[str],
    mappings: MutableMapping[str, str],
) -> Optional[str]:
    if not source_key or not source_key.lower().endswith(".csv"):
        return None
    source_path = ROOT / source_key
    if not source_path.is_file():
        raise BuildError(f"linked CSV source does not exist: {source_key}")
    mirror_name = data_register_mirror_name(source_key)
    prior = mappings.get(source_key)
    if prior is not None and prior != mirror_name:
        raise BuildError(f"inconsistent CSV mirror mapping for {source_key}")
    mappings[source_key] = mirror_name
    return mirror_name


def data_register_title(mirror_name: str) -> Optional[str]:
    """Read a human title from an existing shared Markdown data page."""

    path = DATA_REGISTERS_DIR / mirror_name
    if not path.is_file():
        return None
    try:
        text = path.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError):
        return None
    match = re.search(r"^#\s+(.+?)\s*$", text, re.MULTILINE)
    return match.group(1).strip() if match else None


def humanize_csv_label(label: str, source_key: str, mirror_name: str) -> str:
    """Remove machine filename syntax when the visible label is itself a path."""

    plain = re.sub(r"[*_`]", "", html.unescape(label)).strip()
    filename_like = bool(re.fullmatch(r"[A-Za-z0-9А-Яа-яЁё./_-]+\.csv", plain, re.IGNORECASE))
    if filename_like:
        title = data_register_title(mirror_name)
        if title:
            return title
        words = Path(source_key).stem.replace("-", " ").replace("_", " ")
        return words[:1].upper() + words[1:]
    return re.sub(r"\.csv\b", "", label, flags=re.IGNORECASE)


def neutral_python_label(label: str, target: str) -> str:
    plain = re.sub(r"<[^>]+>", " ", label)
    plain = re.sub(r"[*`]", "", html.unescape(plain))
    plain = re.sub(r"\s+", " ", plain).strip()
    if not plain:
        plain = Path(unquote(urlsplit(target).path)).name or "административный инструмент"
    return plain.replace("`", "")


def data_wikilink(mirror_name: str, label: str) -> str:
    safe_label = label.replace("|", "\\|").replace("]", "\\]")
    return f"[[80_DATA_REGISTERS/{Path(mirror_name).stem}|{safe_label}]]"


def rebased_asset_target(
    source: Path,
    normalized_target: str,
    query_text: str,
    fragment: str,
) -> str:
    absolute = (source.parent / normalized_target).resolve()
    relative = os.path.relpath(str(absolute), str(GUIDES_DIR)).replace(os.sep, "/")
    encoded = quote(relative, safe="/@:+,;=-._~")
    return urlunsplit(("", "", encoded, query_text, fragment))


def mirror_display_label(mirror_name: str) -> str:
    return re.sub(r"^\d+(?:\.\d+)?\s+—\s+", "", Path(mirror_name).stem)


def humanize_guide_label(label: str, mirror_name: str) -> str:
    plain = re.sub(r"[*`]", "", html.unescape(label)).strip()
    filename_like = plain.lower().endswith((".md", ".html")) or bool(
        re.fullmatch(r"[A-Z0-9][A-Z0-9_-]+(?:_RU)?", plain)
    )
    return mirror_display_label(mirror_name) if filename_like else label


def wiki_target(mirror_name: str, fragment: str, label: str) -> str:
    stem = Path(mirror_name).stem
    target = f"{GUIDES_VAULT_NAME}/{stem}" + (
        "#" + unquote(fragment) if fragment else ""
    )
    label = humanize_guide_label(label, mirror_name)
    safe_label = label.replace("|", "\\|").replace("]", "\\]")
    return f"[[{target}|{safe_label}]]"


def rewrite_markdown_segment(
    source: Path,
    segment: str,
    mirror_map: Mapping[str, str],
    data_mappings: MutableMapping[str, str],
) -> str:
    def replace(match: re.Match[str]) -> str:
        target = match.group("target")
        suffix = target_path_suffix(target)
        if suffix == ".py" and not match.group("image"):
            label = neutral_python_label(match.group("label"), target)
            return f"`{label} — административный инструмент`"
        parsed = split_local_target(target)
        if parsed is None:
            return match.group(0)
        normalized, query_text, fragment = parsed
        key = source_target_key(source, normalized)
        if suffix == ".csv" and not match.group("image"):
            data_name = register_data_mapping(key, data_mappings)
            if data_name is None:
                raise BuildError(f"cannot map linked CSV outside the kit root: {target}")
            label = humanize_csv_label(match.group("label"), key or normalized, data_name)
            return data_wikilink(data_name, label)
        mirror_name = mirror_map.get(key or "")
        if mirror_name and not match.group("image"):
            return wiki_target(mirror_name, fragment, match.group("label"))

        rebased = rebased_asset_target(source, normalized, query_text, fragment)
        title = match.group("title") or ""
        return f"{match.group('image')}[{match.group('label')}]({rebased}{title})"

    return MARKDOWN_LINK_RE.sub(replace, segment)


def rewrite_markdown(
    source: Path,
    text: str,
    mirror_map: Mapping[str, str],
    data_mappings: MutableMapping[str, str],
) -> str:
    """Rewrite prose links while leaving fenced code blocks byte-for-byte."""

    chunks = re.split(r"(^```[^\n]*\n.*?^```[ \t]*$)", text, flags=re.MULTILINE | re.DOTALL)
    for index in range(0, len(chunks), 2):
        chunks[index] = rewrite_markdown_segment(source, chunks[index], mirror_map, data_mappings)
    return "".join(chunks)


def rewrite_html_target(
    source: Path,
    target: str,
    mirror_map: Mapping[str, str],
    data_mappings: MutableMapping[str, str],
) -> str:
    if target.startswith(("../80_DATA_REGISTERS/", "../90_ADMIN/")):
        return target
    parsed = split_local_target(target)
    if parsed is None:
        return target
    normalized, query_text, fragment = parsed
    key = source_target_key(source, normalized)
    if target_path_suffix(target) == ".csv":
        data_name = register_data_mapping(key, data_mappings)
        if data_name is None:
            raise BuildError(f"cannot map linked CSV outside the kit root: {target}")
        return urlunsplit(("", "", f"../80_DATA_REGISTERS/{data_name}", query_text, fragment))
    mirror_name = mirror_map.get(key or "")
    if mirror_name:
        return urlunsplit(("", "", mirror_name, query_text, fragment))
    return rebased_asset_target(source, normalized, query_text, fragment)


def rewrite_html_anchors(
    source: Path,
    body: str,
    data_mappings: MutableMapping[str, str],
) -> str:
    def replace_anchor(match: re.Match[str]) -> str:
        href_match = HREF_ONLY_RE.search(match.group("attrs"))
        if not href_match:
            return match.group(0)
        target = href_match.group("target")
        suffix = target_path_suffix(target)
        if suffix == ".py":
            label = neutral_python_label(match.group("body"), target)
            return f"<code>{html.escape(label)} — административный инструмент</code>"
        if suffix != ".csv":
            return match.group(0)

        parsed = split_local_target(target)
        if parsed is None:
            label = neutral_python_label(match.group("body"), target)
            return f"<code>{html.escape(label)} — внешний табличный источник</code>"
        normalized, query_text, fragment = parsed
        key = source_target_key(source, normalized)
        data_name = register_data_mapping(key, data_mappings)
        if data_name is None:
            raise BuildError(f"cannot map linked CSV outside the kit root: {target}")
        new_target = urlunsplit(("", "", f"../80_DATA_REGISTERS/{data_name}", query_text, fragment))
        attrs = HREF_ONLY_RE.sub(
            lambda href: (
                f"{href.group('prefix')}{href.group('quote')}"
                f"{html.escape(new_target, quote=True)}{href.group('quote')}"
            ),
            match.group("attrs"),
            count=1,
        )
        visible = re.sub(r"<[^>]+>", "", match.group("body"))
        human = humanize_csv_label(visible, key or normalized, data_name)
        if human != visible:
            anchor_body = html.escape(human)
        else:
            anchor_body = match.group("body")
        return f"<a{attrs}>{anchor_body}</a>"

    return HTML_ANCHOR_RE.sub(replace_anchor, body)


def extract_html_body(
    source: Path,
    text: str,
    mirror_map: Mapping[str, str],
    data_mappings: MutableMapping[str, str],
) -> str:
    cleaned = SCRIPT_STYLE_RE.sub("", text)
    main_match = re.search(r"<main\b[^>]*>(?P<body>.*?)</main\s*>", cleaned, re.IGNORECASE | re.DOTALL)
    if main_match:
        body = main_match.group("body")
    else:
        body_match = re.search(r"<body\b[^>]*>(?P<body>.*?)</body\s*>", cleaned, re.IGNORECASE | re.DOTALL)
        if not body_match:
            raise BuildError(f"HTML source has neither <main> nor <body>: {source.name}")
        body = body_match.group("body")

    body = SCRIPT_STYLE_RE.sub("", body)
    body = EVENT_ATTR_RE.sub("", body)
    body = STYLE_ATTR_RE.sub("", body)
    body = rewrite_html_anchors(source, body, data_mappings)

    def replace_attr(match: re.Match[str]) -> str:
        old_target = match.group("target")
        new_target = rewrite_html_target(source, old_target, mirror_map, data_mappings)
        if new_target == old_target:
            return match.group(0)
        escaped = html.escape(new_target, quote=True)
        return f"{match.group('name')}={match.group('quote')}{escaped}{match.group('quote')}"

    body = HTML_ATTR_RE.sub(replace_attr, body).strip()
    if re.search(r"<(?:script|style)\b", body, re.IGNORECASE):
        raise BuildError(f"unsafe script/style survived HTML cleanup: {source.name}")
    return body


def frontmatter(source: Path, digest: str, source_kind: str) -> str:
    mirror_source = "../../" + source.relative_to(ROOT).as_posix()
    return "\n".join(
        (
            "---",
            "generated: true",
            f"generator: {yaml_string(GENERATOR_ID)}",
            f"mirror_source: {yaml_string(mirror_source)}",
            f"mirror_sha256: {yaml_string(digest)}",
            f"mirror_source_kind: {yaml_string(source_kind)}",
            f"instruction_state: {yaml_string(INSTRUCTION_STATE)}",
            "---",
            "",
        )
    )


def mirror_warning(source: Path) -> str:
    source_ref = "../../" + source.relative_to(ROOT).as_posix()
    return (
        "> [!warning] Автоматическое зеркало — не источник истины\n"
        f"> Source-of-truth: `{source_ref}`. Не редактируйте эту копию: "
        "следующий запуск восстановит её из корневого файла. Само зеркалирование не повышает "
        "статус инструкции, review, допуска, наличия имущества или готовности.\n\n"
    )


def guide_display_label(source_name: str) -> str:
    stem = Path(GUIDE_FILENAMES[source_name]).stem
    return re.sub(r"^\d+(?:\.\d+)?\s+—\s+", "", stem)


def guide_wikilink(source_name: str, mirror_map: Mapping[str, str]) -> str:
    mirror_name = mirror_map[source_name]
    target = f"{GUIDES_VAULT_NAME}/{Path(mirror_name).stem}"
    return f"[[{target}|{guide_display_label(source_name)}]]"


def orientation_block(source: Path, mirror_map: Mapping[str, str]) -> str:
    """Render the authored, human-facing reading context for one mirror."""

    context = GUIDE_CONTEXT[source.name]
    related_value = context["related"]
    if not isinstance(related_value, tuple) or not related_value:
        raise BuildError(f"guide context has no related documents: {source.name}")
    related = ", ".join(guide_wikilink(name, mirror_map) for name in related_value)
    next_name = context["next"]
    if not isinstance(next_name, str):
        raise BuildError(f"guide context has an invalid next document: {source.name}")
    return (
        "## Как использовать этот документ\n\n"
        f"- **Для чего нужен:** {context['purpose']}.\n"
        f"- **Связан с:** {related}.\n"
        f"- **Когда читать:** {context['when']}.\n"
        f"- **Следующий документ:** {guide_wikilink(next_name, mirror_map)}.\n\n"
    )


def index_orientation(mirror_map: Mapping[str, str]) -> str:
    related = ", ".join(
        guide_wikilink(name, mirror_map)
        for name in (
            "README.md",
            "START_HERE.html",
            "24_MASTER_CATALOG_STATUS_RU.md",
        )
    )
    return (
        "## Как использовать эту страницу\n\n"
        "- **Для чего нужен:** найти любое полное руководство в одном отсортированном списке.\n"
        f"- **Связан с:** {related}.\n"
        "- **Когда читать:** при первом входе в раздел руководств и когда не знаете имя нужного файла.\n"
        f"- **Следующий документ:** {guide_wikilink('START_HERE.html', mirror_map)}.\n\n"
    )


def render_markdown_mirror(
    source: Path,
    digest: str,
    mirror_map: Mapping[str, str],
    data_mappings: MutableMapping[str, str],
) -> str:
    source_text = source.read_text(encoding="utf-8")
    rewritten = rewrite_markdown(source, source_text, mirror_map, data_mappings).rstrip() + "\n"
    return (
        frontmatter(source, digest, "MARKDOWN")
        + mirror_warning(source)
        + orientation_block(source, mirror_map)
        + rewritten
    )


def render_html_mirror(
    source: Path,
    digest: str,
    mirror_map: Mapping[str, str],
    data_mappings: MutableMapping[str, str],
) -> str:
    source_text = source.read_text(encoding="utf-8")
    body = extract_html_body(source, source_text, mirror_map, data_mappings)
    return (
        frontmatter(source, digest, "HTML_MAIN_OR_BODY")
        + mirror_warning(source)
        + orientation_block(source, mirror_map)
        + "<!-- Source scripting and styling removed; raw semantic HTML is intentional. -->\n"
        + '<div class="source-html-mirror">\n'
        + body
        + "\n</div>\n"
    )


def markdown_title(source: Path) -> str:
    text = source.read_text(encoding="utf-8")
    match = re.search(r"^#\s+(.+?)\s*$", text, re.MULTILINE)
    return match.group(1) if match else source.stem


def html_title(source: Path) -> str:
    text = source.read_text(encoding="utf-8")
    for tag in ("h1", "title"):
        match = re.search(rf"<{tag}\b[^>]*>(.*?)</{tag}\s*>", text, re.IGNORECASE | re.DOTALL)
        if match:
            plain = re.sub(r"<[^>]+>", " ", match.group(1))
            plain = re.sub(r"\s+", " ", html.unescape(plain)).strip()
            if plain:
                return plain
    return source.stem


def render_index(
    markdown_sources: Sequence[Path],
    html_sources: Sequence[Path],
    digests: Mapping[str, str],
    mirror_map: Mapping[str, str],
) -> str:
    digest_material = "".join(f"{name}\0{digests[name]}\n" for name in sorted(digests))
    aggregate_digest = sha256_bytes(digest_material.encode("utf-8"))
    lines = [
        "---",
        "generated: true",
        f"generator: {yaml_string(GENERATOR_ID)}",
        f"mirror_source: {yaml_string('MULTIPLE_ROOT_SOURCES')}",
        f"mirror_sha256: {yaml_string(aggregate_digest)}",
        f"instruction_state: {yaml_string('INDEX_ONLY_NOT_AN_INSTRUCTION')}",
        "---",
        "",
        "# Путеводитель по руководствам",
        "",
        "> [!warning] Навигационный индекс, не источник истины",
        "> Здесь перечислены только Markdown-зеркала руководств. Корневые файлы остаются source-of-truth. CSV — скрытый backend: пользователь читает их Markdown-представления в `80_DATA_REGISTERS` и сводные dashboards. HTML/XLSX и другие материалы открываются из руководств через безопасные локальные ссылки.",
        "",
        f"Зеркал руководств: **{len(markdown_sources) + len(html_sources)}**.",
        "",
    ]
    lines.extend(index_orientation(mirror_map).rstrip().splitlines())
    lines.extend(("", "## Все руководства", ""))
    all_sources = sorted(
        list(markdown_sources) + list(html_sources),
        key=lambda source: mirror_map[source.relative_to(ROOT).as_posix()],
    )
    for source in all_sources:
        source_key = source.relative_to(ROOT).as_posix()
        lines.append(f"- {guide_wikilink(source_key, mirror_map)}")
    lines.append("")
    return "\n".join(lines)


def load_owned_manifest(manifest_path: Path) -> Set[str]:
    if not manifest_path.exists():
        return set()
    try:
        data = json.loads(manifest_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise BuildError(f"cannot read generated manifest {manifest_path}: {exc}") from exc
    if data.get("generator") != GENERATOR_ID or not isinstance(data.get("generated_files"), list):
        raise BuildError(f"manifest is not owned by this generator: {manifest_path}")

    names: Set[str] = set()
    for value in data["generated_files"]:
        if not isinstance(value, str):
            raise BuildError("prior manifest contains a non-string path")
        path = Path(value)
        if path.name != value or value.startswith(".") or path.suffix != ".md":
            raise BuildError(f"unsafe generated path in prior manifest: {value!r}")
        names.add(value)
    return names


def remove_manifest_owned_files(directory: Path, manifest_path: Path) -> Tuple[int, bool]:
    """Remove only manifest-listed files with ownership markers, then empty dir."""

    owned_names = load_owned_manifest(manifest_path)
    deleted = 0
    for name in sorted(owned_names):
        path = directory / name
        if not path.exists():
            continue
        if not is_owned_generated_file(path):
            raise BuildError(f"refusing to delete changed or user-owned legacy file: {path}")
        path.unlink()
        deleted += 1

    if manifest_path.exists():
        remaining_owned = [name for name in owned_names if (directory / name).exists()]
        if remaining_owned:
            raise BuildError(
                "legacy ownership manifest still has existing files: "
                + ", ".join(sorted(remaining_owned))
            )
        manifest_path.unlink()

    removed_directory = False
    if directory.is_dir() and not any(directory.iterdir()):
        directory.rmdir()
        removed_directory = True
    return deleted, removed_directory


def is_owned_generated_file(path: Path) -> bool:
    if not path.is_file():
        return False
    try:
        prefix = path.read_text(encoding="utf-8")[:800]
    except (OSError, UnicodeDecodeError):
        return False
    return (
        "generated: true" in prefix
        and f"generator: {yaml_string(GENERATOR_ID)}" in prefix
        and "mirror_source:" in prefix
        and "mirror_sha256:" in prefix
    )


def write_atomic(path: Path, text: str) -> None:
    data = text.encode("utf-8")
    with tempfile.NamedTemporaryFile(dir=str(path.parent), prefix=".guide-tmp-", delete=False) as handle:
        temporary = Path(handle.name)
        handle.write(data)
        handle.flush()
        os.fsync(handle.fileno())
    try:
        os.replace(str(temporary), str(path))
    finally:
        if temporary.exists():
            temporary.unlink()


def safe_local_destination(raw_target: str, base: Path) -> Optional[Path]:
    parsed = split_local_target(raw_target)
    if parsed is None:
        return None
    normalized, _, _ = parsed
    return (base / normalized).resolve()


def verify_generated_links(
    generated_names: Iterable[str],
    data_mappings: Mapping[str, str],
) -> Dict[str, int]:
    markdown_links = 0
    wikilinks = 0
    html_links = 0
    clickable_csv = 0
    clickable_py = 0
    orientation_pages = 0
    errors: List[str] = []
    generated_set = set(generated_names)
    expected_data_names = set(data_mappings.values())
    referenced_data_names: Set[str] = set()

    for source_key, mirror_name in data_mappings.items():
        expected_name = data_register_mirror_name(source_key)
        if mirror_name != expected_name:
            errors.append(
                f"CSV mapping mismatch: {source_key} -> {mirror_name}; expected {expected_name}"
            )

    for name in sorted(generated_set):
        path = GUIDES_DIR / name
        text = path.read_text(encoding="utf-8")
        required_markers = (
            "generated: true",
            "mirror_source:",
            "mirror_sha256:",
            "instruction_state:",
        )
        for marker in required_markers:
            if marker not in text[:1000]:
                errors.append(f"{name}: missing frontmatter marker {marker}")
        orientation_markers = (
            "**Для чего нужен:**",
            "**Связан с:**",
            "**Когда читать:**",
            "**Следующий документ:**",
        )
        missing_orientation = [marker for marker in orientation_markers if marker not in text]
        if missing_orientation:
            errors.append(f"{name}: incomplete human orientation block")
        else:
            orientation_pages += 1

        for match in MARKDOWN_LINK_RE.finditer(text):
            markdown_links += 1
            suffix = target_path_suffix(match.group("target"))
            if suffix == ".csv":
                clickable_csv += 1
                errors.append(f"{name}: clickable CSV target {match.group('target')}")
            if suffix == ".py":
                clickable_py += 1
                errors.append(f"{name}: clickable Python target {match.group('target')}")
            destination = safe_local_destination(match.group("target"), path.parent)
            if destination is not None and not destination.exists():
                errors.append(f"{name}: missing Markdown target {match.group('target')}")

        for match in WIKILINK_RE.finditer(text):
            wikilinks += 1
            raw = match.group("target").split("#", 1)[0].strip()
            if not raw:
                continue
            candidate_name = posixpath.normpath(raw if raw.endswith(".md") else raw + ".md")
            if candidate_name.startswith("80_DATA_REGISTERS/"):
                data_name = Path(candidate_name).name
                if data_name not in expected_data_names:
                    errors.append(f"{name}: unknown data-register wikilink {raw}")
                else:
                    referenced_data_names.add(data_name)
                    if not (VAULT_DIR / candidate_name).is_file():
                        errors.append(f"{name}: missing data-register wikilink target {raw}")
                continue
            if candidate_name.startswith(GUIDES_VAULT_NAME + "/"):
                candidate = (VAULT_DIR / candidate_name).resolve()
            else:
                candidate = (GUIDES_DIR / candidate_name).resolve()
            if not candidate.is_file():
                errors.append(f"{name}: missing wikilink target {raw}")

        for match in HTML_ATTR_RE.finditer(text):
            html_links += 1
            suffix = target_path_suffix(match.group("target"))
            if suffix == ".csv":
                clickable_csv += 1
                errors.append(f"{name}: clickable HTML CSV target {match.group('target')}")
            if suffix == ".py":
                clickable_py += 1
                errors.append(f"{name}: clickable HTML Python target {match.group('target')}")
            parsed = split_local_target(match.group("target"))
            if parsed is not None:
                normalized_html_target = posixpath.normpath(parsed[0])
                if normalized_html_target.startswith("../80_DATA_REGISTERS/"):
                    data_name = Path(normalized_html_target).name
                    if data_name not in expected_data_names:
                        errors.append(
                            f"{name}: unknown data-register HTML target {match.group('target')}"
                        )
                    else:
                        referenced_data_names.add(data_name)
                        if not (GUIDES_DIR / normalized_html_target).resolve().is_file():
                            errors.append(
                                f"{name}: missing data-register HTML target {match.group('target')}"
                            )
                    continue
            destination = safe_local_destination(match.group("target"), path.parent)
            if destination is not None and not destination.exists():
                errors.append(f"{name}: missing HTML target {match.group('target')}")

    unreferenced_data = sorted(expected_data_names - referenced_data_names)
    if unreferenced_data:
        errors.append("unreferenced expected data targets: " + ", ".join(unreferenced_data))

    index_text = (GUIDES_DIR / INDEX_FILENAME).read_text(encoding="utf-8")
    for match in WIKILINK_RE.finditer(index_text):
        target = match.group("target").split("#", 1)[0].strip()
        candidate = posixpath.normpath(target if target.endswith(".md") else target + ".md")
        if not candidate.startswith(GUIDES_VAULT_NAME + "/") or Path(candidate).name not in generated_set:
            errors.append(f"{INDEX_FILENAME} points outside generated Markdown guides: {target}")
    if MARKDOWN_LINK_RE.search(index_text) or HTML_ATTR_RE.search(index_text):
        errors.append(f"{INDEX_FILENAME} must lead only to local Markdown guide wikilinks")

    if errors:
        raise BuildError("generated guide verification failed:\n- " + "\n- ".join(errors))
    existing_data_pages = sum(
        1 for mirror_name in data_mappings.values() if (DATA_REGISTERS_DIR / mirror_name).is_file()
    )
    return {
        "markdown_links": markdown_links,
        "wikilinks": wikilinks,
        "html_links": html_links,
        "clickable_csv": clickable_csv,
        "clickable_py": clickable_py,
        "data_targets": len(expected_data_names),
        "existing_data_pages": existing_data_pages,
        "orientation_pages": orientation_pages,
    }


def verify_source_hashes(
    sources: Sequence[Path],
    mirror_map: Mapping[str, str],
    digests: Mapping[str, str],
) -> int:
    matches = 0
    for source in sources:
        source_key = source.relative_to(ROOT).as_posix()
        digest = sha256_bytes(source.read_bytes())
        if digest != digests[source_key]:
            raise BuildError(f"source changed during guide build: {source_key}")
        mirror_text = (GUIDES_DIR / mirror_map[source_key]).read_text(encoding="utf-8")
        expected = f"mirror_sha256: {yaml_string(digest)}"
        if expected not in mirror_text[:1000]:
            raise BuildError(f"mirror hash does not match source: {source_key}")
        matches += 1
    return matches


def build() -> None:
    markdown_sources = discover_markdown_sources()
    html_sources = discover_html_sources()
    sources = list(markdown_sources) + list(html_sources)
    mirror_map = build_mirror_map(sources)

    digests = {
        source.relative_to(ROOT).as_posix(): sha256_bytes(source.read_bytes())
        for source in sources
    }
    rendered: MutableMapping[str, str] = {}
    data_mappings: MutableMapping[str, str] = {}
    for source in markdown_sources:
        relative = source.relative_to(ROOT).as_posix()
        rendered[mirror_map[relative]] = render_markdown_mirror(
            source, digests[relative], mirror_map, data_mappings
        )
    for source in html_sources:
        relative = source.relative_to(ROOT).as_posix()
        rendered[mirror_map[relative]] = render_html_mirror(
            source, digests[relative], mirror_map, data_mappings
        )
    rendered[INDEX_FILENAME] = render_index(
        markdown_sources, html_sources, digests, mirror_map
    )

    GUIDES_DIR.mkdir(parents=True, exist_ok=True)
    old_owned = load_owned_manifest(MANIFEST_PATH)
    desired = set(rendered)
    deleted_new = 0
    for stale_name in sorted(old_owned - desired):
        stale_path = GUIDES_DIR / stale_name
        if stale_path.exists():
            if not is_owned_generated_file(stale_path):
                raise BuildError(f"refusing to delete changed or user-owned stale file: {stale_path}")
            stale_path.unlink()
            deleted_new += 1

    created = 0
    updated = 0
    unchanged = 0
    for name in sorted(desired):
        target = GUIDES_DIR / name
        if target.exists() and name not in old_owned:
            raise BuildError(f"refusing to overwrite unmanifested user file: {target}")
        if target.exists() and not is_owned_generated_file(target):
            raise BuildError(f"refusing to overwrite changed or user-owned file: {target}")
        existing = target.read_text(encoding="utf-8") if target.exists() else None
        if existing == rendered[name]:
            unchanged += 1
            continue
        write_atomic(target, rendered[name])
        if existing is None:
            created += 1
        else:
            updated += 1

    filename_migrations = [
        {
            "source": source.relative_to(ROOT).as_posix(),
            "old": f"{LEGACY_GUIDES_VAULT_NAME}/{legacy_mirror_name_for_source(source)}",
            "new": f"{GUIDES_VAULT_NAME}/{mirror_map[source.relative_to(ROOT).as_posix()]}",
        }
        for source in sources
    ]
    filename_migrations.append(
        {
            "source": "MULTIPLE_ROOT_SOURCES",
            "old": f"{LEGACY_GUIDES_VAULT_NAME}/INDEX.md",
            "new": f"{GUIDES_VAULT_NAME}/{INDEX_FILENAME}",
        }
    )

    manifest = {
        "version": 4,
        "generator": GENERATOR_ID,
        "vault_directory": GUIDES_VAULT_NAME,
        "generated_files": sorted(desired),
        "filename_migrations": filename_migrations,
        "data_register_links": [
            {
                "source_csv": source_key,
                "guide_target": f"80_DATA_REGISTERS/{mirror_name}",
                "html_href_target": f"../80_DATA_REGISTERS/{mirror_name}",
            }
            for source_key, mirror_name in sorted(data_mappings.items())
        ],
        "sources": [
            {
                "source": source.relative_to(ROOT).as_posix(),
                "mirror": mirror_map[source.relative_to(ROOT).as_posix()],
                "sha256": digests[source.relative_to(ROOT).as_posix()],
                "kind": source.suffix.lower().lstrip("."),
            }
            for source in sources
        ],
    }
    manifest_text = json.dumps(manifest, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
    if not MANIFEST_PATH.exists() or MANIFEST_PATH.read_text(encoding="utf-8") != manifest_text:
        write_atomic(MANIFEST_PATH, manifest_text)

    link_report = verify_generated_links(desired, data_mappings)
    source_hash_matches = verify_source_hashes(sources, mirror_map, digests)

    legacy_deleted = 0
    legacy_dir_removed = False
    if LEGACY_GUIDES_DIR.is_dir():
        legacy_deleted, legacy_dir_removed = remove_manifest_owned_files(
            LEGACY_GUIDES_DIR, LEGACY_MANIFEST_PATH
        )
    legacy_remaining = (
        sum(1 for _ in LEGACY_GUIDES_DIR.iterdir()) if LEGACY_GUIDES_DIR.is_dir() else 0
    )
    html_table_count = sum(
        rendered[mirror_map[path.relative_to(ROOT).as_posix()]].lower().count("<table")
        for path in html_sources
    )
    html_list_count = sum(
        rendered[mirror_map[path.relative_to(ROOT).as_posix()]].lower().count("<ul")
        + rendered[mirror_map[path.relative_to(ROOT).as_posix()]].lower().count("<ol")
        for path in html_sources
    )
    print(
        "obsidian_guides_ok "
        f"sources={len(sources)} markdown_sources={len(markdown_sources)} "
        f"html_sources={len(html_sources)} guide_mirrors={len(sources)} "
        f"markdown_files={len(desired)} created={created} updated={updated} "
        f"unchanged={unchanged} deleted_new={deleted_new}"
    )
    print(
        "human_names "
        f"folder={yaml_string(GUIDES_VAULT_NAME)} filename_migrations={len(filename_migrations)} "
        f"orientation_pages={link_report['orientation_pages']}"
    )
    print(
        "legacy_migration "
        f"deleted_owned={legacy_deleted} directory_removed={int(legacy_dir_removed)} "
        f"remaining_entries={legacy_remaining}"
    )
    print(f"source_hash_match matches={source_hash_matches} total={len(sources)}")
    print(
        "link_check "
        f"markdown_links={link_report['markdown_links']} "
        f"wikilinks={link_report['wikilinks']} html_links={link_report['html_links']} "
        f"clickable_csv={link_report['clickable_csv']} "
        f"clickable_py={link_report['clickable_py']} missing_nondata=0"
    )
    print(
        "data_register_mapping "
        f"targets={link_report['data_targets']} "
        f"existing={link_report['existing_data_pages']} "
        f"pending={link_report['data_targets'] - link_report['existing_data_pages']} "
        "all_named_in_manifest=1"
    )
    print(f"html_visibility tables={html_table_count} lists={html_list_count} script_style_tags=0")


def main() -> int:
    try:
        build()
    except (BuildError, OSError, UnicodeError) as exc:
        print(f"obsidian_guides_error: {exc}")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
