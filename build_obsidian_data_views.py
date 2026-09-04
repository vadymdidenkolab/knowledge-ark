#!/usr/bin/env python3
"""Build complete, read-only Markdown views of the kit's CSV backend.

The CSV files remain the machine-readable source of truth.  This generator
creates a user-readable, static Obsidian layer in
``Obsidian-Vault/80_DATA_REGISTERS``.  It does not turn a registry row into an
instruction, evidence, a physical asset, or permission to act.

Only files listed in the generator's own manifest are considered for stale
cleanup, and a generated ownership marker is checked before deletion or
replacement.  Unowned user files are never modified or removed.

Python standard library only; compatible with Python 3.9+.
"""

from __future__ import annotations

import argparse
import csv
from dataclasses import dataclass
import hashlib
import html
import json
import os
from pathlib import Path
import re
import stat
import sys
import tempfile
from typing import Dict, Iterable, List, Mapping, Optional, Sequence, Tuple


ROOT = Path(__file__).resolve().parent
VAULT = ROOT / "Obsidian-Vault"
OUT = VAULT / "80_DATA_REGISTERS"
MANIFEST_PATH = OUT / ".generated-data-registers-manifest.json"
GENERATOR = "build_obsidian_data_views.py"
GENERATOR_VERSION = "1"
INSTRUCTION_STATE = "CATALOG_ONLY_NOT_EXECUTABLE"
OWNED_MARKER = f'generated_by: "{GENERATOR}"'
GENERATED_FILE_MODE = 0o644

# Payload/archive folders can contain future exports or attachments that are
# not backend registries.  The register at offline-library/ itself remains in
# scope; only descendants of the payload-storage folders are excluded.
EXCLUDED_DIRECTORY_NAMES = {
    ".git",
    "__pycache__",
    "Obsidian-Vault",
    "attachments",
    "attachment",
    "archives",
    "archive",
    "payloads",
    "payload",
    "candidate",
    "private-licensed",
    "quarantine",
    "readers",
    "released",
    "superseded",
}

WIKILINK_RE = re.compile(r"\[\[([^\]|]+)(?:\|[^\]]*)?\]\]")
MARKDOWN_LINK_RE = re.compile(r"!?\[[^\]\n]*\]\(([^)\n]+)\)")


TITLE_RU: Mapping[str, str] = {
    "accountability-log-template.csv": "Журнал подотчётности — шаблон",
    "action-card-register-template.csv": "Реестр карточек действий — шаблон",
    "animal-profile-template.csv": "Профиль животного — шаблон",
    "archive-media-register-template.csv": "Реестр архивных носителей — шаблон",
    "asset-component-lifecycle-template.csv": "Жизненный цикл имущества и компонентов — шаблон",
    "buddy-assignment-template.csv": "Назначения напарников — шаблон",
    "capability-crosswalk.csv": "Связи прежних возможностей с каноническим деревом",
    "card-gate-snapshot-template.csv": "Снимок допуска карточки — шаблон",
    "cascade-register-template.csv": "Реестр каскадов отказов — шаблон",
    "century-capability-register.csv": "Возможности столетней непрерывности",
    "century-gate-snapshot-template.csv": "Снимок допуска столетней непрерывности — шаблон",
    "climate-pathway-register-template.csv": "Реестр климатических траекторий — шаблон",
    "competency-lineage-template.csv": "Преемственность компетенций — шаблон",
    "decision-class-register.csv": "Классы решений и полномочий",
    "dependent-care-authorization-template.csv": "Полномочия по уходу за зависимым человеком — шаблон",
    "external-contact-template.csv": "Внешние контакты — шаблон",
    "format-migration-register-template.csv": "Миграция форматов архива — шаблон",
    "governance-policy-register-template.csv": "Политики управления — шаблон",
    "group-composition-snapshot-template.csv": "Снимок состава группы — шаблон",
    "group-function-assignment-template.csv": "Назначение функций в группе — шаблон",
    "group-operational-roster-template.csv": "Оперативный состав группы — шаблон",
    "group-profile-template.csv": "Профиль группы — шаблон",
    "group-revision-register-template.csv": "Ревизии данных группы — шаблон",
    "group-roster-template.csv": "Состав участников группы — шаблон",
    "horizon-register.csv": "Горизонты автономности",
    "incident-log-template.csv": "Журнал происшествий — шаблон",
    "institution-register-template.csv": "Реестр институтов и организаций — шаблон",
    "inventory-template.csv": "Физический инвентарь — шаблон",
    "knowledge-succession-register-template.csv": "Преемственность знаний — шаблон",
    "known-gap-register.csv": "Известные пробелы и блокеры",
    "land-parcel-register-template.csv": "Земельные участки — шаблон",
    "legacy-scenario-map.csv": "Соответствие прежних и текущих сценариев",
    "map-register-template.csv": "Реестр карт — шаблон",
    "offline-corpus-manifest.csv": "Манифест офлайн-корпуса",
    "offline-library/offline-payload-register.csv": "Офлайн-библиотека: сохранённые файлы",
    "offline-restore-test-template.csv": "Испытание восстановления офлайн-библиотеки — шаблон",
    "offline-storage-plan-template.csv": "План хранения офлайн-библиотеки — шаблон",
    "payload-source-crosswalk.csv": "Связи локальных файлов с источниками",
    "population-capacity-snapshot-template.csv": "Снимок обеспечиваемой численности — шаблон",
    "practical-science-domain-register.csv": "Отрасли практической науки",
    "practical-science-instrument-register.csv": "Измерительные приборы практической науки",
    "practical-science-learning-paths.csv": "Учебные траектории практической науки",
    "practical-science-package-register.csv": "Пакеты источников практической науки",
    "practical-science-project-register.csv": "Проекты практической науки",
    "practical-science-protocol-template.csv": "Научный протокол — шаблон",
    "practical-science-raw-log-template.csv": "Журнал исходных научных наблюдений — шаблон",
    "practical-science-safety-gates.csv": "Допуски безопасности практической науки",
    "resource-scaling-template.csv": "Масштабирование ресурсов для группы — шаблон",
    "resource-transaction-log-template.csv": "Движение и передача ресурсов — шаблон",
    "role-gate-record-template.csv": "Допуск роли к действию — шаблон",
    "route-register-template.csv": "Реестр маршрутов — шаблон",
    "scenario-register.csv": "Сценарии нештатных ситуаций",
    "seed-accession-template.csv": "Партии и образцы семян — шаблон",
    "site-register-template.csv": "Объекты и площадки — шаблон",
    "soil-monitoring-template.csv": "Мониторинг почвы — шаблон",
    "source-manifest.csv": "Основной манифест источников",
    "succession-register-template.csv": "Передача полномочий — шаблон",
    "technology-dependency-edges.csv": "Типизированные зависимости технологий",
    "technology-dependency-register.csv": "Каноническое дерево технологий",
    "technology-node-planning-register.csv": "Планирование технологических узлов",
    "technology-service-level-register.csv": "Требования уровней сервиса",
    "water-source-capacity-template.csv": "Мощность источников воды — шаблон",
}


GROUPS: Sequence[Tuple[str, str, Sequence[str]]] = (
    (
        "SYSTEM_READINESS",
        "Архитектура системы, готовность и сценарии",
        (
            "action-card-register-template.csv",
            "capability-crosswalk.csv",
            "card-gate-snapshot-template.csv",
            "cascade-register-template.csv",
            "horizon-register.csv",
            "known-gap-register.csv",
            "legacy-scenario-map.csv",
            "scenario-register.csv",
            "technology-dependency-edges.csv",
            "technology-dependency-register.csv",
            "technology-node-planning-register.csv",
            "technology-service-level-register.csv",
        ),
    ),
    (
        "PEOPLE_GOVERNANCE",
        "Люди, роли, операции и управление",
        (
            "accountability-log-template.csv",
            "buddy-assignment-template.csv",
            "decision-class-register.csv",
            "dependent-care-authorization-template.csv",
            "external-contact-template.csv",
            "governance-policy-register-template.csv",
            "group-composition-snapshot-template.csv",
            "group-function-assignment-template.csv",
            "group-operational-roster-template.csv",
            "group-profile-template.csv",
            "group-revision-register-template.csv",
            "group-roster-template.csv",
            "incident-log-template.csv",
            "resource-transaction-log-template.csv",
            "role-gate-record-template.csv",
        ),
    ),
    (
        "PHYSICAL_RESOURCES",
        "Имущество, участок, вода, почва, семена и животные",
        (
            "animal-profile-template.csv",
            "asset-component-lifecycle-template.csv",
            "inventory-template.csv",
            "land-parcel-register-template.csv",
            "resource-scaling-template.csv",
            "seed-accession-template.csv",
            "site-register-template.csv",
            "soil-monitoring-template.csv",
            "water-source-capacity-template.csv",
        ),
    ),
    (
        "MAPS_ENVIRONMENT",
        "Карты, маршруты и климат",
        (
            "climate-pathway-register-template.csv",
            "map-register-template.csv",
            "route-register-template.csv",
        ),
    ),
    (
        "CENTURY_CONTINUITY",
        "Преемственность и столетний горизонт",
        (
            "century-capability-register.csv",
            "century-gate-snapshot-template.csv",
            "competency-lineage-template.csv",
            "institution-register-template.csv",
            "knowledge-succession-register-template.csv",
            "population-capacity-snapshot-template.csv",
            "succession-register-template.csv",
        ),
    ),
    (
        "OFFLINE_KNOWLEDGE",
        "Источники, архив и офлайн-библиотека",
        (
            "archive-media-register-template.csv",
            "format-migration-register-template.csv",
            "offline-corpus-manifest.csv",
            "offline-library/offline-payload-register.csv",
            "offline-restore-test-template.csv",
            "offline-storage-plan-template.csv",
            "payload-source-crosswalk.csv",
            "source-manifest.csv",
        ),
    ),
    (
        "PRACTICAL_SCIENCE",
        "Практическая наука, приборы и безопасность",
        (
            "practical-science-domain-register.csv",
            "practical-science-instrument-register.csv",
            "practical-science-learning-paths.csv",
            "practical-science-package-register.csv",
            "practical-science-project-register.csv",
            "practical-science-protocol-template.csv",
            "practical-science-raw-log-template.csv",
            "practical-science-safety-gates.csv",
        ),
    ),
)

GROUP_TITLES = {code: title for code, title, _ in GROUPS}
GROUP_BY_SOURCE = {
    source: code
    for code, _title, sources in GROUPS
    for source in sources
}


EXACT_FIELD_LABELS: Mapping[str, str] = {
    "id": "Идентификатор",
    "node_id": "Идентификатор узла",
    "parent_id": "Родительский узел",
    "edge_id": "Идентификатор связи",
    "from_node_id": "Исходный узел",
    "to_node_id": "Целевой узел",
    "edge_role": "Роль связи",
    "alternative_group": "Группа альтернатив",
    "minimum_required_count": "Минимальное обязательное количество",
    "applicable_if": "Условие применимости",
    "rationale": "Обоснование",
    "review_state": "Состояние проверки",
    "title": "Название",
    "title_ru": "Название на русском",
    "description": "Описание",
    "notes": "Примечания",
    "status": "Статус",
    "release_gate": "Допуск к применению",
    "release_status": "Статус выпуска",
    "release_version": "Версия выпуска",
    "source_path": "Путь источника",
    "source_ids": "Идентификаторы источников",
    "source_package_ids": "Пакеты источников",
    "source_url": "Адрес источника в сети",
    "canonical_url": "Канонический адрес в сети",
    "acquisition_url": "Адрес получения",
    "relative_path": "Относительный путь к локальному файлу",
    "sha256": "Хеш SHA-256",
    "byte_size": "Размер в байтах",
    "page_count": "Число страниц",
    "publisher": "Издатель",
    "edition_date": "Дата редакции",
    "audience": "Целевая аудитория",
    "media_type": "Тип носителя",
    "domain": "Отрасль",
    "domain_code": "Код отрасли",
    "domain_id": "Идентификатор отрасли",
    "domain_title_ru": "Название отрасли на русском",
    "priority_tier": "Приоритет",
    "priority_horizon": "Горизонт приоритета",
    "service_level": "Уровень сервиса",
    "earliest_service_level": "Самый ранний уровень сервиса",
    "minimum_outcome": "Минимально требуемый результат",
    "required_evidence": "Требуемые доказательства",
    "current_evidence": "Имеющиеся доказательства",
    "evidence_state": "Состояние доказательств",
    "safety_class": "Класс безопасности",
    "risk_class": "Класс риска",
    "execution_policy": "Политика исполнения",
    "execution_gate": "Допуск к исполнению",
    "stop_conditions": "Условия остановки",
    "owner": "Владелец",
    "owner_role": "Ответственная роль",
    "backup_role": "Резервная роль",
    "due": "Срок",
    "next_due": "Следующая проверка",
    "group_size_scope": "Размер группы",
    "capacity_value": "Значение мощности",
    "capacity_unit": "Единица мощности",
    "capability_status": "Состояние возможности",
    "prerequisite_node_ids": "Предварительные технологические узлы",
    "instrument_ids": "Измерительные приборы",
    "materials_tools_state": "Состояние материалов и инструментов",
    "measurement_acceptance": "Критерий приёмки измерений",
    "localization_state": "Состояние локализации",
    "rights_review_state": "Проверка прав",
    "rights_statement": "Условия прав и использования",
    "rights_url": "Адрес условий прав",
    "redistribution_scope": "Допустимый объём распространения",
    "upstream_digest_algorithm": "Алгоритм контрольной суммы издателя",
    "upstream_digest": "Контрольная сумма издателя",
    "upstream_digest_url": "Адрес контрольной суммы издателя",
    "operational_use": "Допустимое операционное применение",
    "format_check": "Результат проверки формата",
    "open_test_state": "Результат проверки открытия",
    "retrieved_at_utc": "Время получения, UTC",
}


TOKEN_RU: Mapping[str, str] = {
    "id": "ID",
    "ids": "ID",
    "state": "состояние",
    "status": "статус",
    "source": "источник",
    "target": "целевой",
    "current": "текущий",
    "previous": "предыдущий",
    "next": "следующий",
    "person": "человек",
    "people": "люди",
    "group": "группа",
    "role": "роль",
    "owner": "владелец",
    "backup": "резервный",
    "primary": "основной",
    "secondary": "вторичный",
    "required": "требуемый",
    "requirement": "требование",
    "evidence": "доказательство",
    "gate": "допуск",
    "review": "проверка",
    "reviewed": "проверенный",
    "verified": "подтверждённый",
    "verification": "подтверждение",
    "validation": "валидация",
    "result": "результат",
    "method": "метод",
    "policy": "правило",
    "scope": "область",
    "class": "класс",
    "type": "тип",
    "code": "код",
    "name": "название",
    "title": "название",
    "description": "описание",
    "note": "примечание",
    "notes": "примечания",
    "ref": "ссылка",
    "refs": "ссылки",
    "reference": "ссылка",
    "record": "запись",
    "register": "реестр",
    "entry": "запись",
    "item": "предмет",
    "asset": "имущество",
    "component": "компонент",
    "resource": "ресурс",
    "capacity": "мощность",
    "quantity": "количество",
    "count": "количество",
    "unit": "единица",
    "value": "значение",
    "minimum": "минимальный",
    "maximum": "максимальный",
    "actual": "фактический",
    "planned": "плановый",
    "available": "доступный",
    "availability": "доступность",
    "location": "место",
    "site": "объект",
    "route": "маршрут",
    "map": "карта",
    "water": "вода",
    "food": "пища",
    "seed": "семена",
    "soil": "почва",
    "animal": "животное",
    "health": "здоровье",
    "medical": "медицинский",
    "care": "уход",
    "knowledge": "знания",
    "archive": "архив",
    "offline": "офлайн",
    "file": "файл",
    "format": "формат",
    "media": "носитель",
    "payload": "локальный файл",
    "path": "путь",
    "url": "адрес в сети",
    "hash": "хеш",
    "sha256": "SHA-256",
    "digest": "контрольная сумма",
    "version": "версия",
    "revision": "ревизия",
    "date": "дата",
    "time": "время",
    "at": "время",
    "by": "кем",
    "from": "из",
    "to": "в",
    "until": "до",
    "due": "срок",
    "interval": "интервал",
    "duration": "длительность",
    "hours": "часы",
    "language": "язык",
    "jurisdiction": "юрисдикция",
    "legal": "правовой",
    "rights": "права",
    "license": "лицензия",
    "privacy": "приватность",
    "safety": "безопасность",
    "risk": "риск",
    "hazard": "опасность",
    "failure": "отказ",
    "emergency": "аварийный",
    "incident": "происшествие",
    "action": "действие",
    "decision": "решение",
    "authority": "полномочие",
    "authorization": "разрешение",
    "consent": "согласие",
    "assignment": "назначение",
    "function": "функция",
    "contact": "контакт",
    "training": "обучение",
    "skill": "навык",
    "competency": "компетенция",
    "instrument": "прибор",
    "equipment": "оборудование",
    "tool": "инструмент",
    "materials": "материалы",
    "storage": "хранение",
    "maintenance": "обслуживание",
    "repair": "ремонт",
    "replacement": "замена",
    "restore": "восстановление",
    "migration": "миграция",
    "test": "испытание",
    "tested": "испытанный",
    "check": "проверка",
    "acceptance": "приёмка",
    "release": "выпуск",
    "approved": "утверждённый",
    "prohibited": "запрещённый",
    "allowed": "разрешённый",
    "condition": "условие",
    "boundary": "граница",
    "trigger": "триггер",
    "protocol": "протокол",
    "plan": "план",
    "profile": "профиль",
    "snapshot": "снимок",
    "transaction": "операция",
    "lifecycle": "жизненный цикл",
    "succession": "преемственность",
    "horizon": "горизонт",
    "scenario": "сценарий",
    "domain": "отрасль",
    "capability": "возможность",
    "service": "сервис",
    "level": "уровень",
    "priority": "приоритет",
    "dependency": "зависимость",
    "relation": "отношение",
    "relationship": "отношение",
    "linked": "связанный",
    "canonical": "канонический",
    "legacy": "прежний",
    "external": "внешний",
    "local": "локальный",
    "physical": "физический",
    "operational": "операционный",
    "professional": "профессиональный",
    "human": "человеческий",
    "public": "публичный",
    "private": "приватный",
    "ru": "на русском",
}


@dataclass(frozen=True)
class CsvTable:
    path: Path
    relative_path: str
    title_ru: str
    group_code: str
    output_name: str
    source_sha256: str
    source_bytes: int
    headers: Tuple[str, ...]
    rows: Tuple[Tuple[str, ...], ...]
    blank_row_count: int

    @property
    def row_count(self) -> int:
        return len(self.rows)

    @property
    def column_count(self) -> int:
        return len(self.headers)

    @property
    def cell_count(self) -> int:
        return self.row_count * self.column_count


class BuildError(RuntimeError):
    """Raised when a safe and complete build cannot be produced."""


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def yaml_string(value: str) -> str:
    return json.dumps(value, ensure_ascii=False)


def discover_csv_paths() -> List[Path]:
    paths: List[Path] = []
    for path in ROOT.rglob("*.csv"):
        relative = path.relative_to(ROOT)
        if any(part in EXCLUDED_DIRECTORY_NAMES for part in relative.parts[:-1]):
            continue
        if path.is_file():
            paths.append(path)
    return sorted(paths, key=lambda item: item.relative_to(ROOT).as_posix().casefold())


def stable_output_name(relative_path: str) -> str:
    relative = Path(relative_path)
    parts = list(relative.with_suffix("").parts)
    safe_parts = []
    for part in parts:
        safe = re.sub(r"[^0-9A-Za-zА-Яа-яЁё._-]+", "-", part).strip("-.")
        if not safe:
            raise BuildError(f"cannot derive a safe output name from {relative_path!r}")
        safe_parts.append(safe)
    return "__".join(safe_parts) + ".md"


def title_for(relative_path: str) -> str:
    if relative_path in TITLE_RU:
        return TITLE_RU[relative_path]
    filename = Path(relative_path).name
    if filename in TITLE_RU:
        return TITLE_RU[filename]
    stem = Path(relative_path).stem.replace("-", " ").replace("_", " ")
    return "Табличный реестр: " + stem


def group_for(relative_path: str) -> str:
    return GROUP_BY_SOURCE.get(relative_path, GROUP_BY_SOURCE.get(Path(relative_path).name, "OTHER"))


def read_csv_table(path: Path) -> CsvTable:
    relative_path = path.relative_to(ROOT).as_posix()
    raw = path.read_bytes()
    try:
        text = raw.decode("utf-8-sig")
    except UnicodeDecodeError as exc:
        raise BuildError(f"CSV is not UTF-8/UTF-8-BOM: {relative_path}: {exc}") from exc

    try:
        parsed = list(csv.reader(text.splitlines(keepends=True), strict=True))
    except csv.Error as exc:
        raise BuildError(f"malformed CSV {relative_path}: {exc}") from exc

    if not parsed:
        raise BuildError(f"CSV has no header row: {relative_path}")
    headers = tuple(parsed[0])
    if not headers:
        raise BuildError(f"CSV has an empty header row: {relative_path}")
    if any(header == "" for header in headers):
        raise BuildError(f"CSV has an unnamed column: {relative_path}")
    if len(set(headers)) != len(headers):
        raise BuildError(f"CSV has duplicate column names: {relative_path}")

    rows: List[Tuple[str, ...]] = []
    blank_row_count = 0
    for physical_row_number, row in enumerate(parsed[1:], start=2):
        if not row or all(value == "" for value in row):
            blank_row_count += 1
            continue
        if len(row) != len(headers):
            raise BuildError(
                f"CSV row width mismatch in {relative_path}:{physical_row_number}: "
                f"expected {len(headers)}, got {len(row)}"
            )
        rows.append(tuple(row))

    return CsvTable(
        path=path,
        relative_path=relative_path,
        title_ru=title_for(relative_path),
        group_code=group_for(relative_path),
        output_name=stable_output_name(relative_path),
        source_sha256=sha256_bytes(raw),
        source_bytes=len(raw),
        headers=headers,
        rows=tuple(rows),
        blank_row_count=blank_row_count,
    )


def load_tables() -> List[CsvTable]:
    tables = [read_csv_table(path) for path in discover_csv_paths()]
    if not tables:
        raise BuildError("no CSV backend sources discovered")

    collisions: Dict[str, List[str]] = {}
    by_name: Dict[str, List[str]] = {}
    for table in tables:
        by_name.setdefault(table.output_name.casefold(), []).append(table.relative_path)
    for output_name, sources in by_name.items():
        if len(sources) > 1:
            collisions[output_name] = sources
    if collisions:
        details = "; ".join(f"{name}: {', '.join(paths)}" for name, paths in collisions.items())
        raise BuildError("stable output filename collision: " + details)
    return tables


def field_label(field_name: str) -> str:
    exact = EXACT_FIELD_LABELS.get(field_name)
    if exact:
        return exact
    tokens = [token for token in field_name.lower().split("_") if token]
    if not tokens:
        return "Безымянное техническое поле"
    translated = [TOKEN_RU.get(token, f"«{token}»") for token in tokens]
    label = " ".join(translated)
    return label[:1].upper() + label[1:]


def html_code(value: str) -> str:
    """Render a value losslessly enough for review without activating links."""

    serialized = json.dumps(value, ensure_ascii=False)
    escaped = html.escape(serialized, quote=True)
    # Square brackets are encoded so source values containing Markdown links or
    # wikilinks remain data, never navigation generated by this mirror.
    escaped = escaped.replace("[", "&#91;").replace("]", "&#93;")
    return f"<code>{escaped}</code>"


def heading_text(value: str, limit: int = 140) -> str:
    compact = " ".join(value.split())
    if len(compact) > limit:
        compact = compact[: limit - 1].rstrip() + "…"
    return html.escape(compact, quote=False)


def row_summary(table: CsvTable, row: Sequence[str], ordinal: int) -> str:
    positions = {name: index for index, name in enumerate(table.headers)}
    id_candidates = (
        "id",
        "node_id",
        "edge_id",
        "gap_id",
        "scenario_id",
        "capability_id",
        "service_requirement_id",
        "package_id",
        "payload_id",
        "source_id",
        "item_id",
        "person_id",
        "group_profile_id",
        "route_id",
        "map_id",
        "site_id",
        "accession_id",
    )
    title_candidates = (
        "title_ru",
        "name_ru",
        "item_name_ru",
        "domain_title_ru",
        "path_title_ru",
        "group_title_ru",
        "gap_ru",
        "service_outcome",
        "minimum_outcome",
        "title",
        "display_name",
        "common_name",
        "route_name",
    )

    identifier = ""
    for candidate in id_candidates:
        index = positions.get(candidate)
        if index is not None and row[index]:
            identifier = row[index]
            break
    if not identifier:
        for index, header in enumerate(table.headers):
            if header.endswith("_id") and row[index]:
                identifier = row[index]
                break

    title = ""
    for candidate in title_candidates:
        index = positions.get(candidate)
        if index is not None and row[index] and row[index] != identifier:
            title = row[index]
            break

    parts = [f"Запись {ordinal} из {table.row_count}"]
    if identifier:
        parts.append(identifier)
    if title:
        parts.append(title)
    return heading_text(" — ".join(parts))


def render_frontmatter(table: CsvTable) -> List[str]:
    stable_id = hashlib.sha256(table.relative_path.encode("utf-8")).hexdigest()[:16]
    return [
        "---",
        f'id: "DATA-REGISTER-{stable_id}"',
        'type: "generated-data-register-view"',
        f"title: {yaml_string(table.title_ru)}",
        "generated: true",
        f'generated_by: "{GENERATOR}"',
        f'generator_version: "{GENERATOR_VERSION}"',
        f"source_path: {yaml_string(table.relative_path)}",
        f'source_sha256: "{table.source_sha256}"',
        f"source_bytes: {table.source_bytes}",
        f"source_row_count: {table.row_count}",
        f"source_column_count: {table.column_count}",
        f"source_cell_count: {table.cell_count}",
        f"ignored_blank_row_count: {table.blank_row_count}",
        f"semantic_group: {yaml_string(table.group_code)}",
        f'instruction_state: "{INSTRUCTION_STATE}"',
        'release_gate: "DENY"',
        "---",
    ]


def render_table_page(table: CsvTable) -> str:
    lines = render_frontmatter(table)
    lines.extend(
        [
            "",
            f"<!-- backend-source: {html.escape(table.relative_path, quote=True)} -->",
            "",
            f"# {table.title_ru}",
            "",
            "[[80_DATA_REGISTERS/INDEX|← Все реестры]]",
            "",
            "> [!warning] Доказательная граница",
            "> Эта страница дословно зеркалирует машинный реестр. Запись не доказывает наличие вещи, безопасность метода, квалификацию, испытание или разрешение на действие.",
            "> Для опасных, медицинских, химических, топливных или профессиональных ветвей сохранённое значение остаётся только справочным, если отдельно не доказан более высокий статус.",
            "",
            "## Сводка",
            "",
            f"- **Смысловая группа:** {GROUP_TITLES.get(table.group_code, 'Прочие реестры')}",
            f"- **Записей:** {table.row_count}",
            f"- **Полей в каждой записи:** {table.column_count}",
            f"- **Ячеек данных, включая пустые:** {table.cell_count}",
            f"- **Пустых физических строк пропущено:** {table.blank_row_count}",
            f"- **Целостность источника:** SHA-256 `{table.source_sha256}`",
            "- **Состояние:** каталог; не исполнимая инструкция",
            "",
            "## Структура полей",
            "",
            "Исходное техническое имя каждого поля сохранено рядом с русским пояснением. Кавычки в значениях и последовательности `\\n`, `\\r`, `\\t` — часть точного текстового представления.",
            "",
            "| № | Русское пояснение | Имя backend-поля |",
            "|---:|---|---|",
        ]
    )
    for index, field_name in enumerate(table.headers, start=1):
        lines.append(
            f"| {index} | {field_label(field_name)} | {html_code(field_name)} |"
        )

    lines.extend(["", "## Полное содержимое", ""])
    if not table.rows:
        lines.extend(
            [
                "> [!info] В реестре нет записей",
                "> Структура полей сохранена выше; фактические строки отсутствуют.",
                "",
            ]
        )
    else:
        lines.append(
            "Каждая запись показана отдельной сворачиваемой карточкой. Пустое значение отображается как <code>&quot;&quot;</code>; поля не опускаются."
        )
        lines.append("")

    for ordinal, row in enumerate(table.rows, start=1):
        lines.append(f"<!-- record:{ordinal} cells:{len(row)} -->")
        lines.append(f"> [!abstract]- {row_summary(table, row, ordinal)}")
        for field_name, value in zip(table.headers, row):
            lines.append(
                f"> - **{field_label(field_name)}** ({html_code(field_name)}): {html_code(value)}"
            )
        lines.append(">")
        lines.append("")

    lines.extend(
        [
            "---",
            "",
            "Эта страница создана автоматически. Исправления вносятся в машинный источник, после чего зеркало пересобирается.",
            "",
        ]
    )
    return "\n".join(lines)


def render_index(tables: Sequence[CsvTable]) -> str:
    total_rows = sum(table.row_count for table in tables)
    total_columns = sum(table.column_count for table in tables)
    total_cells = sum(table.cell_count for table in tables)
    lines = [
        "---",
        'id: "DATA-REGISTERS-INDEX"',
        'type: "generated-data-register-index"',
        'title: "Полное зеркало табличных реестров"',
        "generated: true",
        f'generated_by: "{GENERATOR}"',
        f'generator_version: "{GENERATOR_VERSION}"',
        f"source_count: {len(tables)}",
        f"register_page_count: {len(tables)}",
        f"total_source_rows: {total_rows}",
        f"total_source_columns: {total_columns}",
        f"total_source_cells: {total_cells}",
        f'instruction_state: "{INSTRUCTION_STATE}"',
        'release_gate: "DENY"',
        "---",
        "",
        "# Полное зеркало табличных реестров",
        "",
        "> [!warning] Это каталог, а не набор разрешённых действий",
        "> Здесь полностью отображены машинные реестры системы. Наличие строки не доказывает наличие физического ресурса, безопасность, квалификацию, испытание или готовность. Опасные и профессиональные сведения сохраняют только исходный справочный статус.",
        "",
        "## Сводка",
        "",
        f"- **Источников данных:** {len(tables)}",
        f"- **Страниц реестров:** {len(tables)}",
        f"- **Записей во всех источниках:** {total_rows}",
        f"- **Сумма полей по структурам источников:** {total_columns}",
        f"- **Ячеек данных, включая пустые:** {total_cells}",
        "- **Формат:** статический Markdown без обязательных плагинов",
        "- **Доказательный статус:** каталог; не исполнимая инструкция",
        "",
        "Каждая ссылка ниже открывает человекочитаемую Markdown-страницу внутри Obsidian. Машинные файлы остаются backend и не используются как пользовательская навигация.",
        "",
    ]

    emitted = set()
    by_group: Dict[str, List[CsvTable]] = {}
    for table in tables:
        by_group.setdefault(table.group_code, []).append(table)

    for group_code, group_title, _sources in GROUPS:
        group_tables = sorted(by_group.get(group_code, []), key=lambda item: item.title_ru.casefold())
        if not group_tables:
            continue
        emitted.add(group_code)
        lines.extend([f"## {group_title}", ""])
        for table in group_tables:
            target = f"80_DATA_REGISTERS/{Path(table.output_name).stem}"
            lines.append(
                f"- [[{target}|{table.title_ru}]] — записей: {table.row_count}; полей: {table.column_count}"
            )
        lines.append("")

    remaining = [
        table
        for table in tables
        if table.group_code not in emitted
    ]
    if remaining:
        lines.extend(["## Прочие реестры", ""])
        for table in sorted(remaining, key=lambda item: item.title_ru.casefold()):
            target = f"80_DATA_REGISTERS/{Path(table.output_name).stem}"
            lines.append(
                f"- [[{target}|{table.title_ru}]] — записей: {table.row_count}; полей: {table.column_count}"
            )
        lines.append("")

    lines.extend(
        [
            "## Как читать статусы",
            "",
            "- `CATALOG_ONLY_NOT_EXECUTABLE` — данные перенесены в каталог, но не стали инструкцией.",
            "- `DENY` — исполнение не разрешено одним фактом наличия записи.",
            "- `REFERENCE_ONLY` — справка; не бытовая рецептура.",
            "- Локальный файл, карточка, URL или номер в реестре не заменяют ручную проверку, физическое наличие, обучение и испытание.",
            "",
        ]
    )
    return "\n".join(lines)


def expected_outputs(tables: Sequence[CsvTable]) -> Dict[str, str]:
    outputs = {table.output_name: render_table_page(table) for table in tables}
    outputs["INDEX.md"] = render_index(tables)
    return dict(sorted(outputs.items(), key=lambda item: item[0].casefold()))


def output_digest(text: str) -> str:
    return sha256_bytes(text.encode("utf-8"))


def build_manifest(tables: Sequence[CsvTable], outputs: Mapping[str, str]) -> Dict[str, object]:
    entries = []
    for table in tables:
        entries.append(
            {
                "source_path": table.relative_path,
                "source_sha256": table.source_sha256,
                "source_bytes": table.source_bytes,
                "row_count": table.row_count,
                "column_count": table.column_count,
                "cell_count": table.cell_count,
                "blank_row_count": table.blank_row_count,
                "semantic_group": table.group_code,
                "output_file": table.output_name,
                "output_sha256": output_digest(outputs[table.output_name]),
            }
        )
    return {
        "schema_version": 1,
        "generator": GENERATOR,
        "generator_version": GENERATOR_VERSION,
        "instruction_state": INSTRUCTION_STATE,
        "source_count": len(tables),
        "register_page_count": len(tables),
        "owned_markdown_count": len(outputs),
        "total_source_rows": sum(table.row_count for table in tables),
        "total_source_cells": sum(table.cell_count for table in tables),
        "index_file": "INDEX.md",
        "index_sha256": output_digest(outputs["INDEX.md"]),
        "owned_files": sorted(outputs),
        "sources": sorted(entries, key=lambda entry: str(entry["source_path"]).casefold()),
    }


def manifest_text(manifest: Mapping[str, object]) -> str:
    return json.dumps(manifest, ensure_ascii=False, indent=2, sort_keys=True) + "\n"


def load_existing_manifest() -> Optional[Dict[str, object]]:
    if not MANIFEST_PATH.exists():
        return None
    try:
        payload = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise BuildError(f"cannot safely read existing manifest: {exc}") from exc
    if not isinstance(payload, dict) or payload.get("generator") != GENERATOR:
        raise BuildError("existing data-register manifest is not owned by this generator")
    owned = payload.get("owned_files")
    if not isinstance(owned, list) or not all(isinstance(item, str) for item in owned):
        raise BuildError("existing data-register manifest has an invalid owned_files list")
    return payload


def safe_output_path(relative_name: str) -> Path:
    if Path(relative_name).is_absolute():
        raise BuildError(f"unsafe absolute owned path: {relative_name}")
    path = (OUT / relative_name).resolve()
    try:
        path.relative_to(OUT.resolve())
    except ValueError as exc:
        raise BuildError(f"unsafe owned path outside output directory: {relative_name}") from exc
    return path


def is_owned_generated_markdown(path: Path) -> bool:
    if not path.is_file() or path.suffix.lower() != ".md":
        return False
    try:
        prefix = path.read_text(encoding="utf-8")[:2000]
    except OSError:
        return False
    return OWNED_MARKER in prefix and "generated: true" in prefix


def preflight_outputs(outputs: Mapping[str, str]) -> None:
    for relative_name in outputs:
        path = safe_output_path(relative_name)
        if path.exists() and not is_owned_generated_markdown(path):
            raise BuildError(
                f"refusing to replace unowned user file: {path.relative_to(ROOT).as_posix()}"
            )


def atomic_write_if_changed(path: Path, text: str) -> bool:
    encoded = text.encode("utf-8")
    if path.exists() and path.read_bytes() == encoded:
        if stat.S_IMODE(path.stat().st_mode) != GENERATED_FILE_MODE:
            path.chmod(GENERATED_FILE_MODE)
            return True
        return False
    path.parent.mkdir(parents=True, exist_ok=True)
    descriptor, temporary_name = tempfile.mkstemp(prefix=f".{path.name}.", dir=str(path.parent))
    temporary = Path(temporary_name)
    try:
        with os.fdopen(descriptor, "wb") as handle:
            handle.write(encoded)
            handle.flush()
            os.fsync(handle.fileno())
            os.fchmod(handle.fileno(), GENERATED_FILE_MODE)
        os.replace(str(temporary), str(path))
    finally:
        if temporary.exists():
            temporary.unlink()
    return True


def remove_stale_owned(existing_manifest: Optional[Mapping[str, object]], desired: Iterable[str]) -> List[str]:
    if existing_manifest is None:
        return []
    desired_set = set(desired)
    stale = sorted(set(existing_manifest.get("owned_files", [])) - desired_set)
    removed: List[str] = []
    for relative_name in stale:
        path = safe_output_path(str(relative_name))
        if not path.exists():
            continue
        if not is_owned_generated_markdown(path):
            print(
                f"WARNING: stale path is no longer an owned generated Markdown file; left untouched: {path}",
                file=sys.stderr,
            )
            continue
        path.unlink()
        removed.append(str(relative_name))
    return removed


def parse_markdown_link_target(raw_target: str) -> str:
    target = raw_target.strip()
    if target.startswith("<") and ">" in target:
        target = target[1 : target.index(">")]
    else:
        # Optional Markdown title follows the target after whitespace.
        target = target.split(maxsplit=1)[0] if target else ""
    return target


def find_clickable_csv_links(text: str) -> List[str]:
    findings = []
    for match in MARKDOWN_LINK_RE.finditer(text):
        target = parse_markdown_link_target(match.group(1))
        path_part = target.split("#", 1)[0].split("?", 1)[0]
        if path_part.lower().endswith(".csv"):
            findings.append(match.group(0))
    for match in WIKILINK_RE.finditer(text):
        target = match.group(1).split("#", 1)[0].strip()
        if target.lower().endswith(".csv"):
            findings.append(match.group(0))
    return findings


def vault_note_targets() -> Tuple[set, Dict[str, int]]:
    paths = set()
    stem_counts: Dict[str, int] = {}
    for note in VAULT.rglob("*.md"):
        relative = note.relative_to(VAULT).with_suffix("").as_posix()
        paths.add(relative)
        stem_counts[note.stem] = stem_counts.get(note.stem, 0) + 1
    return paths, stem_counts


def missing_wikilinks(owned_paths: Iterable[Path]) -> List[str]:
    available_paths, stem_counts = vault_note_targets()
    missing = []
    for note in owned_paths:
        text = note.read_text(encoding="utf-8")
        for match in WIKILINK_RE.finditer(text):
            raw_target = match.group(1).strip()
            target = raw_target.split("#", 1)[0].split("^", 1)[0].strip()
            if not target:
                continue
            target = target.removesuffix(".md")
            if target in available_paths:
                continue
            relative_target = (note.parent / target).resolve()
            try:
                relative_to_vault = relative_target.relative_to(VAULT.resolve()).as_posix()
            except ValueError:
                relative_to_vault = ""
            if relative_to_vault in available_paths:
                continue
            if "/" not in target and stem_counts.get(target, 0) == 1:
                continue
            missing.append(f"{note.relative_to(VAULT).as_posix()}: {match.group(0)}")
    return missing


def validate_outputs(
    tables: Sequence[CsvTable],
    outputs: Mapping[str, str],
    manifest: Mapping[str, object],
) -> Dict[str, int]:
    errors: List[str] = []

    if manifest.get("source_count") != len(tables):
        errors.append("manifest source_count does not match discovered CSV count")
    if manifest.get("register_page_count") != len(tables):
        errors.append("manifest register_page_count does not match discovered CSV count")
    if manifest.get("owned_markdown_count") != len(outputs):
        errors.append("manifest owned_markdown_count does not match expected output count")

    actual_manifest = load_existing_manifest()
    if actual_manifest != manifest:
        errors.append("on-disk manifest differs from deterministic expected manifest")
    if MANIFEST_PATH.is_file() and stat.S_IMODE(MANIFEST_PATH.stat().st_mode) != GENERATED_FILE_MODE:
        errors.append("generated manifest mode is not 0644")

    owned_paths: List[Path] = []
    clickable_csv_count = 0
    for relative_name, expected_text in outputs.items():
        path = safe_output_path(relative_name)
        owned_paths.append(path)
        if not path.is_file():
            errors.append(f"missing generated page: {relative_name}")
            continue
        if stat.S_IMODE(path.stat().st_mode) != GENERATED_FILE_MODE:
            errors.append(f"generated page mode is not 0644: {relative_name}")
        actual_text = path.read_text(encoding="utf-8")
        if actual_text != expected_text:
            errors.append(f"generated page differs from source-derived expected content: {relative_name}")
        findings = find_clickable_csv_links(actual_text)
        clickable_csv_count += len(findings)
        if findings:
            errors.append(f"clickable CSV link in {relative_name}: {findings[0]}")

    source_entries = {
        str(entry.get("source_path")): entry
        for entry in manifest.get("sources", [])
        if isinstance(entry, dict)
    }
    for table in tables:
        entry = source_entries.get(table.relative_path)
        if entry is None:
            errors.append(f"manifest is missing source: {table.relative_path}")
            continue
        if entry.get("source_sha256") != table.source_sha256:
            errors.append(f"source hash mismatch: {table.relative_path}")
        if entry.get("row_count") != table.row_count:
            errors.append(f"source row count mismatch: {table.relative_path}")
        if entry.get("column_count") != table.column_count:
            errors.append(f"source column count mismatch: {table.relative_path}")
        if entry.get("cell_count") != table.cell_count:
            errors.append(f"source cell count mismatch: {table.relative_path}")
        expected_page = outputs[table.output_name]
        if entry.get("output_sha256") != output_digest(expected_page):
            errors.append(f"output hash mismatch in manifest: {table.output_name}")
        marker_count = len(re.findall(r"^<!-- record:\d+ cells:\d+ -->$", expected_page, re.MULTILINE))
        if marker_count != table.row_count:
            errors.append(f"rendered record marker count mismatch: {table.output_name}")

    missing_links = missing_wikilinks(path for path in owned_paths if path.is_file())
    if missing_links:
        errors.extend("missing wikilink: " + item for item in missing_links[:20])
        if len(missing_links) > 20:
            errors.append(f"and {len(missing_links) - 20} more missing wikilinks")

    if errors:
        raise BuildError("validation failed:\n- " + "\n- ".join(errors))

    return {
        "sources": len(tables),
        "register_pages": len(tables),
        "owned_markdown_pages": len(outputs),
        "rows": sum(table.row_count for table in tables),
        "source_columns": sum(table.column_count for table in tables),
        "cells": sum(table.cell_count for table in tables),
        "source_hashes_verified": len(tables),
        "output_hashes_verified": len(outputs),
        "clickable_csv_links": clickable_csv_count,
        "missing_wikilinks": len(missing_links),
        "file_mode_mismatches": 0,
    }


def run(check_only: bool) -> Dict[str, object]:
    tables = load_tables()
    outputs = expected_outputs(tables)
    manifest = build_manifest(tables, outputs)

    changed: List[str] = []
    removed: List[str] = []
    if not check_only:
        OUT.mkdir(parents=True, exist_ok=True)
        existing_manifest = load_existing_manifest()
        preflight_outputs(outputs)
        for relative_name, text in outputs.items():
            if atomic_write_if_changed(safe_output_path(relative_name), text):
                changed.append(relative_name)
        removed = remove_stale_owned(existing_manifest, outputs)
        if atomic_write_if_changed(MANIFEST_PATH, manifest_text(manifest)):
            changed.append(MANIFEST_PATH.name)

    stats = validate_outputs(tables, outputs, manifest)
    return {
        "mode": "check" if check_only else "build",
        **stats,
        "changed_files": len(changed),
        "removed_stale_owned_files": len(removed),
        "output_directory": OUT.relative_to(ROOT).as_posix(),
        "manifest": MANIFEST_PATH.relative_to(ROOT).as_posix(),
    }


def parse_args(argv: Optional[Sequence[str]] = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Build or verify complete Obsidian Markdown views of all kit CSV registries."
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help="verify existing generated views without writing or deleting files",
    )
    return parser.parse_args(argv)


def main(argv: Optional[Sequence[str]] = None) -> int:
    args = parse_args(argv)
    try:
        result = run(check_only=args.check)
    except (BuildError, OSError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1
    print(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
