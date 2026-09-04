#!/usr/bin/env python3
"""Build human-readable Obsidian dashboards from the kit CSV registries.

The CSV files remain the machine backend. This generator writes only the
Obsidian-Vault/20 — Рабочие разделы directory and safely removes its own legacy
generated files from Obsidian-Vault/20_DASHBOARDS. It never edits hand-authored
MOCs, 00_HOME.md, or the atomic catalog under 90_GENERATED_CATALOG.

The generated pages are navigation and status views. They are not operational
instructions, medical advice, evidence of physical inventory, or permission to
perform hazardous work.
"""

from __future__ import annotations

import csv
from collections import Counter, defaultdict
import json
from pathlib import Path
import re
import sys
from typing import Dict, Iterable, List, Mapping, NoReturn, Sequence, Tuple
from urllib.parse import quote


ROOT = Path(__file__).resolve().parent
VAULT = ROOT / "Obsidian-Vault"
ATOMIC = VAULT / "90_GENERATED_CATALOG"
LEGACY_OUT = VAULT / "20_DASHBOARDS"
OUT = VAULT / "20 — Рабочие разделы"

DASHBOARD_FILES = {
    "index": "00 — Панели автономного кита.md",
    "readiness": "01 — Что реально готово.md",
    "p0": "02 — Первые 72 часа.md",
    "medicine": "03 — Медицинская помощь.md",
    "gaps": "04 — Что ещё не готово.md",
    "services": "05 — Уровни автономности.md",
    "offline": "06 — Офлайн-библиотека.md",
    "domains": "07 — Области знаний и систем.md",
    "food": "08 — Семена и питание.md",
    "portugal": "09 — Португалия.md",
    "safety": "10 — Границы безопасности.md",
    "inventory": "11 — Физический инвентарь.md",
}
EXPECTED_PAGES = tuple(DASHBOARD_FILES.values())

LEGACY_GENERATED_PAGES = (
    "00_INDEX.md",
    "01_READINESS.md",
    "02_P0_FIRST.md",
    "03_MEDICINE.md",
    "04_OPEN_GAPS.md",
    "05_SERVICE_LEVELS.md",
    "06_OFFLINE_LIBRARY.md",
    "07_TECHNOLOGY_DOMAINS.md",
    "08_SEEDS_AND_FOOD.md",
    "09_PORTUGAL.md",
    "10_SAFETY_BOUNDARIES.md",
    "11_PHYSICAL_INVENTORY.md",
)

PAGE_GUIDANCE = {
    "dashboard-index": (
        "Даёт один понятный вход во все рабочие разделы и сразу отделяет каталог от доказанной готовности.",
        "Нужно понимать только одно правило: запись, PDF или ссылка не равны физической вещи, навыку или разрешению.",
        (("readiness", "Что реально готово"), ("p0", "Первые 72 часа"), ("inventory", "Физический инвентарь")),
        "Сначала откройте честный статус, затем первые 72 часа и фактический инвентарь.",
    ),
    "dashboard-readiness": (
        "Показывает, какие части существуют только как каталог, а где есть файл, проверка, имущество или тест.",
        "Для точного вывода нужны заполненные профили людей, адреса и физический инвентарь; сейчас эти данные неполны.",
        (("gaps", "Что ещё не готово"), ("inventory", "Физический инвентарь"), ("services", "Уровни автономности")),
        "Выберите самый ранний незакрытый уровень и назначьте владельца следующего доказательства.",
    ),
    "dashboard-p0-first": (
        "Собирает реальные блокеры первых 72 часов и отделяет их от ограниченных профессиональных тем.",
        "Должны быть известны текущая опасность, состав людей, адрес, способ вызвать официальную помощь и личные медицинские зависимости.",
        (("medicine", "Медицинская помощь"), ("inventory", "Физический инвентарь"), ("safety", "Границы безопасности")),
        "Закрывайте 19 незакрытых работ по требуемым доказательствам; низко- и среднерисковые узлы материализуйте только после проверки разрешения.",
    ),
    "dashboard-medicine": (
        "Показывает весь медицинский охват и границы между неспециалистом, обученным помощником, клиницистом и справкой.",
        "Нужны персональная медицинская карточка, назначения, аллергии, контакты 112/SNS/CIAV и подтверждённая квалификация для обученного и профессионального уровня.",
        (("p0", "Первые 72 часа"), ("inventory", "Физический инвентарь"), ("safety", "Границы безопасности")),
        "Создайте рецензированные карточки действий для неспециалиста, соберите реальные комплекты и подтвердите обучение очной практикой.",
    ),
    "dashboard-open-gaps": (
        "Это честная очередь того, без чего нельзя объявлять систему готовой.",
        "Нужно различать требуемое и текущее доказательство, а также понимать, кто отвечает, к какому сроку и разрешено ли считать работу закрытой.",
        (("readiness", "Что реально готово"), ("p0", "Первые 72 часа"), ("inventory", "Физический инвентарь")),
        "Назначьте ответственного и срок, получите указанное доказательство и только затем пересматривайте решение о готовности.",
    ),
    "dashboard-service-levels": (
        "Переводит абстрактную автономность в проверяемые результаты от немедленного спасения до межпоколенческой передачи.",
        "Должны быть известны люди, место, требуемый горизонт, измеренная мощность, резервирование и допустимый остаточный риск.",
        (("readiness", "Что реально готово"), ("domains", "Области знаний"), ("gaps", "Что ещё не готово")),
        "Начните с немедленного спасения и не переходите выше, пока обязательные результаты нижнего уровня не проверены.",
    ),
    "dashboard-offline-library": (
        "Показывает, какие источники реально сохранены локально и чем доказана целостность файла.",
        "Нужны рабочее устройство, совместимая программа чтения, место хранения, права использования и понимание, что машинная проверка не равна рецензии.",
        (("readiness", "Что реально готово"), ("safety", "Границы безопасности"), ("gaps", "Что ещё не готово")),
        "Откройте локальные копии без сети, выполните предметную проверку и затем протестируйте резервное восстановление.",
    ),
    "dashboard-technology-domains": (
        "Даёт обзор всех областей, чтобы видеть перекосы и не забывать зависимые системы.",
        "Нужно знать приоритетный горизонт и не интерпретировать число узлов как полноту или готовность.",
        (("medicine", "Медицинская помощь"), ("food", "Семена и питание"), ("portugal", "Португалия"), ("safety", "Границы безопасности")),
        "Выберите нужную область, откройте атомарные карточки и закройте её обязательные пробелы доказательствами.",
    ),
    "dashboard-seeds-food": (
        "Собирает питание, культуры, семена, почву, хранение и воспроизводимость урожая в одном срезе.",
        "Нужны состав людей и диеты, климат и участок, вода, почва, площадь, хранение и реальные партии семян.",
        (("inventory", "Физический инвентарь"), ("portugal", "Португалия"), ("gaps", "Что ещё не готово")),
        "Создайте реестр каждой партии семян, проверьте всхожесть и дублирование, затем испытайте рацион и сезонный план.",
    ),
    "dashboard-portugal": (
        "Отделяет изменяемые португальские службы, право, риски и климат от общего знания.",
        "Нужны точный адрес, муниципалитет, язык группы и дата последней проверки официальных сведений.",
        (("p0", "Первые 72 часа"), ("offline", "Офлайн-библиотека"), ("gaps", "Что ещё не готово")),
        "Проверьте официальные контакты и три слоя карт, затем распечатайте и испытайте локальные маршруты.",
    ),
    "dashboard-safety-boundaries": (
        "Не даёт срочности или интересу темы превратиться в опасную бытовую инструкцию.",
        "Нужно знать границу безопасности, решение о допуске, требуемую квалификацию, законный объект и контроль отходов.",
        (("p0", "Первые 72 часа"), ("medicine", "Медицинская помощь"), ("domains", "Области знаний")),
        "Оставляйте лицензированные и справочные темы в профессиональном контуре и выбирайте низкорисковую альтернативу.",
    ),
    "dashboard-physical-inventory": (
        "Отвечает на вопрос, какие вещи реально находятся у группы, а какие существуют лишь в плане.",
        "Нужен физический доступ к месту хранения, профиль людей и объекта, возможность зафиксировать количество, фото, серийный номер и результат проверки.",
        (("p0", "Первые 72 часа"), ("gaps", "Что ещё не готово"), ("offline", "Офлайн-библиотека")),
        "Осмотрите каждую позицию, заполните фактическое количество, место и ответственного, приложите доказательство и выполните проверку до пересмотра решения о готовности.",
    ),
}

PRIORITY_ORDER = {
    "P0_RED": 0,
    "P1_ORANGE": 1,
    "P2_YELLOW": 2,
    "P3_GREEN": 3,
    "P4_BLUE": 4,
}
SERVICE_ORDER = {f"SL{number}": number for number in range(7)}

PRIORITY_LABELS = {
    "P0_RED": "Первая необходимость — секунды–72 часа",
    "P1_ORANGE": "Критично в течение 3–14 дней",
    "P2_YELLOW": "Стабилизация — 15–90 дней",
    "P3_GREEN": "Долгий срок — 3 месяца–15 лет",
    "P4_BLUE": "Межпоколенческая задача — 15–100 лет",
}

SERVICE_LABELS = {
    "SL0": "Немедленное спасение — секунды–12 часов",
    "SL1": "Первые трое суток — 12–72 часа",
    "SL2": "Устойчивость на 3–14 дней",
    "SL3": "Стабилизация на 15–90 дней",
    "SL4": "Полный сезон — до 1 года",
    "SL5": "Долгий срок — 1–15 лет",
    "SL6": "Передача следующим поколениям — 15–100 лет",
}

DOMAIN_LABELS = {
    "SYSTEM": "Система в целом",
    "BASE": "Базовая готовность",
    "PEOPLE_CARE": "Люди и забота",
    "HEALTH": "Медицинская помощь и здоровье",
    "WATER_WASH": "Вода, санитария и гигиена",
    "FOOD_AGRI": "Питание, сельское хозяйство и семена",
    "ANIMALS": "Животные",
    "SHELTER": "Жильё и укрытие",
    "CONSTRUCTION": "Строительство и ремонт",
    "ENERGY": "Электроэнергия",
    "ENERGY_FUELS": "Топливо и тепловая энергия",
    "MAPS_COMMS": "Карты, навигация и связь",
    "TRANSPORT": "Транспорт",
    "SECURITY": "Безопасность и деэскалация",
    "WORKSHOP": "Мастерская и инструменты",
    "MATERIALS": "Материалы и производство",
    "EDUCATION": "Обучение",
    "KNOWLEDGE": "Знания и офлайн-архив",
    "GOVERNANCE": "Управление и организация группы",
    "ENVIRONMENT": "Окружающая среда и природные риски",
    "PORTUGAL": "Португалия — локальный слой",
    "HAZARD": "Опасные темы — только с ограничениями",
}

SAFETY_LABELS = {
    "S0_OBSERVE_READ": "Только наблюдение и чтение",
    "S1_LOW_RISK_HOUSEHOLD": "Низкий бытовой риск после проверки",
    "S2_TRAINED_SUPERVISED": "Только после обучения или под надзором",
    "S3_LICENSED_PROFESSIONAL": "Только лицензированный специалист",
    "S4_REFERENCE_ONLY_PROHIBITED_HOUSEHOLD": "Только справка; бытовое выполнение запрещено",
}

CAPABILITY_LABELS = {
    "MISSING": "Не создано или не подтверждено",
    "ARCHITECTURE_ONLY": "Есть только структура",
    "REFERENCE_ONLY": "Только справочный материал",
    "ALLOW": "Разрешено после проверки",
}

ROLE_LABELS = {
    "REQUIRED": "Обязательно",
    "OPTIONAL": "Дополнительно",
    "ALTERNATIVE": "Допустимая альтернатива",
    "CONDITIONAL": "Требуется при указанных условиях",
    "REFERENCE": "Справочная связь",
    "HAZARD_ONLY": "Только указатель опасности",
}

SCOPE_LABELS = {
    "PERSON": "Человек",
    "GROUP": "Группа",
    "SITE": "Дом или участок",
    "LOCAL": "Местный уровень",
    "PORTUGAL": "Португалия",
    "PORTUGAL_REGION": "Португалия и регион",
    "GENERAL": "Общий слой",
    "GENERAL_PORTUGAL": "Общий слой и Португалия",
    "GENERAL_PORTUGAL_PERSON": "Общий слой, Португалия и человек",
    "GENERAL_PORTUGAL_SITE": "Общий слой, Португалия и объект",
    "GENERAL_SITE": "Общий слой и объект",
    "PERSON_GROUP": "Человек и группа",
    "PERSON_GROUP_SITE": "Человек, группа и объект",
    "SITE_PERSON": "Объект и человек",
}

COMMON_LABELS = {
    "UNASSIGNED": "Не назначен",
    "TBD": "Не определено",
    "TBD_NOT_SCHEDULED": "Срок не назначен",
    "UNKNOWN": "Неизвестно",
    "UNSELECTED": "Не выбрано",
    "NOT_TESTED": "Не проверено",
    "NOT_REQUIRED": "Не требуется",
    "N/A": "Не применяется",
    "planned": "Запланировано",
    "MISSING_LOCAL_FILE": "Локальный файл отсутствует",
}

MEDIA_LABELS = {
    "application/pdf": "Документ PDF",
    "application/x-zim": "Офлайн-архив ZIM",
    "application/x-apple-diskimage": "Установочный образ macOS",
}

GROUP_LABELS = {
    "N1|N2|N3_TO_N7": "Для 1 человека, 2 человек или группы 3–7 человек",
    "N1": "Для одного человека",
    "N2": "Для двух человек",
    "N3_TO_N7": "Для группы 3–7 человек",
}

CAPACITY_LABELS = {
    "OBJECT_COUNT_COVERAGE_REVIEW_INTERVAL_AND_EVIDENCE": "Количество объектов, охват, интервал проверки и доказательство",
    "PERSON_HOURS_DEPENDENCY_AND_SHIFT_CAPACITY": "Человеко-часы, зависимости и сменная мощность",
    "PERSON_SPECIFIC_RESPONSE_TIME_AND_CARE_HOURS": "Время реагирования и часы ухода для конкретных людей",
    "LITRES_PER_PERSON_DAY_PLUS_PEAK_AND_STORAGE_DAYS": "Литры на человека в сутки, пик потребления и дни хранения",
    "OCCUPANTS_M2_TEMPERATURE_AIR_AND_EGRESS_TIME": "Люди, площадь, температура, воздух и время выхода",
    "PEOPLE_CHANNELS_COVERAGE_CHECKIN_AND_ROUTE_TIME": "Люди, каналы связи, покрытие, контрольные сеансы и время маршрута",
    "DECISIONS_RESOURCES_LABOR_HOURS_AND_AUDIT_INTERVAL": "Решения, ресурсы, трудозатраты и интервал аудита",
    "AUTHORITY_JURISDICTION_VERSION_COVERAGE_AND_CHECKED_DATE": "Орган, юрисдикция, версия, охват и дата проверки",
    "SERVICE_SPECIFIC_UNIT_AND_TIME_WINDOW_TBD": "Единица и временное окно должны быть определены для конкретной функции",
    "KCAL_NUTRIENTS_PER_PERSON_DAY_YIELD_AREA_AND_LOSS": "Калории и питательные вещества на человека, урожайность, площадь и потери",
    "WH_PER_DAY_PEAK_W_AUTONOMY_AND_RECHARGE_TIME": "Энергия в сутки, пиковая мощность, автономия и время перезарядки",
    "BYTES_DOCUMENTS_READERS_RESTORE_TIME_AND_COPIES": "Объём данных, документы, программы чтения, копии и время восстановления",
    "PEOPLE_KG_KM_RANGE_AND_TURNAROUND_TIME": "Люди или груз, расстояние, запас хода и время оборота",
    "SITE_SERIES_SEASONAL_RANGE_AND_TRIGGER_THRESHOLDS": "Ряд измерений на объекте, сезонный диапазон и пороги действий",
    "JOBS_PER_PERIOD_LABOR_HOURS_AND_SPARES": "Число работ за период, трудозатраты и запасные части",
    "LEARNERS_HOURS_COMPETENCY_AND_DUPLICATES": "Число учеников, часы, подтверждённая компетенция и дублёры",
    "MASS_VOLUME_THROUGHPUT_YIELD_AND_REJECT_RATE": "Масса, объём, производительность, выход годного и доля брака",
    "AREA_LOAD_WEATHER_WINDOW_LABOR_AND_INSPECTION": "Площадь, нагрузка, погодное окно, трудозатраты и осмотр",
}

STATUS_LABELS = {
    "CATALOG_ONLY_NOT_EVALUATED": "Есть только запись в каталоге; достижение не оценено",
    "PROVISIONAL_AUTO_REVIEW_REQUIRED": "Предварительно; нужна ручная проверка",
    "CANDIDATE_REFERENCE_NOT_OPERATIONAL": "Кандидат в справочный архив; не для практического применения",
    "PRIVATE_PERSONAL_COPY_REFERENCE": "Личная локальная копия для справки",
    "READER_VERIFIED_NOT_LAUNCHED": "Установочный файл проверен, программа не запущена",
    "RELEASED_REFERENCE": "Выпущено только как справочный материал",
    "RELEASED_TRAINING_ONLY": "Только учебный материал",
}

RIGHTS_LABELS = {
    "PARTIAL_REVIEW_DEFAULT_CC_BY_SA_WITH_EXCEPTIONS": "Частичная проверка: базовая открытая лицензия, возможны исключения",
    "NOT_REVIEWED_FOR_REDISTRIBUTION": "Право на распространение не проверено",
    "PARTIAL_REVIEW_NONCOMMERCIAL_COPYING_NOTICE": "Частичная проверка: указано некоммерческое копирование",
    "RESTRICTED_ALL_RIGHTS_RESERVED": "Все права защищены; только разрешённое личное хранение",
    "PARTIAL_REVIEW_GPL_PROJECT_DISTRIBUTION_OBLIGATIONS_NOT_AUDITED": "Частичная проверка: обязательства распространения программы не аудированы",
    "CLEARED_PUBLIC_USE": "Разрешено публичное использование",
    "CLEARED_OPEN_LICENSE": "Подтверждена открытая лицензия",
    "CLEARED_US_GOVERNMENT_WORK": "Подтверждён материал правительства США; вложения требуют отдельной проверки",
}

OPEN_TEST_LABELS = {
    "ZIM_HEADER_AND_UPSTREAM_SHA256_PASS;NOT_TESTED_IN_KIWIX": "Заголовок и контрольная сумма ZIM проверены; открытие в Kiwix не испытано",
    "PDFINFO_PASS;VISUAL_FIRST_PAGE_PASS": "Структура PDF и первая страница проверены",
    "UPSTREAM_MD5_PASS;BUNDLE_SHORT_VERSION_3.16.1;NOT_TESTED_RUNTIME_LAUNCH": "Контрольная сумма и версия установщика проверены; запуск программы не испытан",
}

OPERATIONAL_LABELS = {
    "UNREVIEWED_ENCYCLOPEDIC_REFERENCE_NOT_OPERATIONAL": "Нерецензированная энциклопедическая справка; не рабочая инструкция",
    "TRAINING_REFERENCE_ONLY_NOT_LAY_ACTION_CARD": "Учебная справка; не карточка действий для неспециалиста",
    "TRAINER_REFERENCE_ONLY_NOT_LAY_ACTION_CARD": "Материал для инструкторов; не карточка действий для неспециалиста",
    "PUBLIC_PREPAREDNESS_REFERENCE_CHECK_CURRENT_ANEPC_ALERTS": "Публичная памятка; при возможности сверять текущие сообщения ANEPC",
    "PUBLIC_PREPAREDNESS_REFERENCE_CHECK_CURRENT_IPMA_AND_ANEPC_ALERTS": "Публичная памятка; при возможности сверять текущие сообщения IPMA и ANEPC",
    "TRAINED_WASH_REFERENCE_NOT_UNSUPERVISED_DOSING_INSTRUCTION": "Справка для обученных специалистов по воде и санитарии; не инструкция по самостоятельному дозированию",
    "TRAINED_WASH_PLANNING_REFERENCE": "Планировочная справка для обученных специалистов по воде и санитарии",
    "TRAINED_WASH_COMMUNICATION_REFERENCE": "Коммуникационная справка для обученных специалистов по воде и санитарии",
    "TRAINED_WASH_MEASUREMENT_REFERENCE_NOT_UNSUPERVISED_DOSING_INSTRUCTION": "Измерительная справка для обученных специалистов; не инструкция по самостоятельному дозированию",
    "TRAINED_WASH_SANITATION_REFERENCE_CHECK_LOCAL_ENVIRONMENTAL_RULES": "Справка по санитарии для обученных специалистов; сверять местные экологические правила",
    "READER_INSTALLER_NOT_LAUNCHED": "Установщик программы чтения; запуск не подтверждён",
    "REFERENCE_ONLY_NOT_A_DESIGN_CERTIFICATION": "Только инженерная справка; не сертификация проекта",
    "REFERENCE_ONLY_VERIFY_LOADS_CODES_SPECIES_GRADE_AND_MOISTURE": "Только справка; отдельно проверять нагрузки, нормы, породу, сорт и влажность",
    "CLINICIAN_TRAINING_ONLY_NOT_LAY_ACTION_CARD": "Учебный материал для клинициста; не карточка для неспециалиста",
    "REFERENCE_ONLY_CHECK_CURRENT_SI_AND_LOCAL_REGULATION": "Только справка; сверять действующие единицы и местные нормы",
    "REFERENCE_ONLY_CHECK_CURRENT_LAB_AND_REGULATORY_REQUIREMENTS": "Только справка; сверять лабораторные и нормативные требования",
}

RELATION_LABELS = {
    "DIRECT": "прямая связь",
    "UMBRELLA": "связь с более широким пакетом",
    "NO_CONFIDENT_MATCH": "надёжная связь не найдена",
}

MEDICAL_LANE_LABELS = {
    "LAY": "Неспециалист",
    "TRAINED": "Обученный помощник",
    "CLINICIAN": "Лицензированный медицинский специалист",
    "REFERENCE": "Только справочный материал",
}

LANGUAGE_LABELS = {
    "en": "Английский",
    "pt-PT": "Португальский (Португалия)",
    "multilingual UI": "Многоязычный интерфейс",
}

INVENTORY_CATEGORY_LABELS = {
    "WATER": "Вода",
    "MED": "Медицинская готовность",
    "COMMS": "Связь и оповещение",
    "FIRE": "Пожар и угарный газ",
    "DOCS": "Критические документы",
}

INVENTORY_FORMULA_LABELS = {
    "baseline + people + days + heat/illness/pregnancy/pets + reserve": "базовая норма + люди × дни + поправки на жару, болезнь, беременность и животных + резерв",
    "1 * persons": "одна на каждого человека",
    "1 household": "один на домохозяйство",
    "per manufacturer siting": "по схеме размещения производителя",
    "2 independent copies": "две независимые копии",
}

INVENTORY_LIMITATION_LABELS = {
    "Item not acquired": "Не приобретено",
    "Archive and restore path not built": "Архив и путь восстановления не созданы",
    "Exact model local source and siting not selected": "Конкретная модель, местный источник и место установки не выбраны",
    "Item not created": "Не создано",
}


def die(message: str) -> NoReturn:
    raise RuntimeError(message)


def translated(value: str, mapping: Mapping[str, str], fallback: str) -> str:
    value = (value or "").strip()
    if not value:
        return "Не заполнено"
    return mapping.get(value, fallback)


def human_priority(value: str) -> str:
    return translated(value, PRIORITY_LABELS, "Приоритет требует ручного пояснения")


def human_service(value: str) -> str:
    return translated(value, SERVICE_LABELS, "Уровень автономности требует ручного пояснения")


def human_domain(value: str) -> str:
    return translated(value, DOMAIN_LABELS, "Другая область; откройте техническую карточку")


def human_safety(value: str) -> str:
    return translated(value, SAFETY_LABELS, "Граница безопасности требует ручной проверки")


def human_capability(value: str) -> str:
    return translated(value, CAPABILITY_LABELS, "Состояние возможности требует ручной проверки")


def human_gate(value: str) -> str:
    value = (value or "").strip()
    if value == "ALLOW":
        return "Разрешено после проверки"
    if value == "REFERENCE_ONLY" or "REFERENCE_ONLY" in value:
        return "Только справка; практическое выполнение запрещено"
    if value.startswith("DENY_UNTIL_"):
        return "Не разрешено до получения указанного доказательства"
    if value == "DENY" or value.startswith("BLACK_GATE_"):
        return "Не разрешено: доказательств или полномочий недостаточно"
    if not value:
        return "Не разрешено: решение не заполнено"
    return "Решение требует ручной проверки; выполнение не разрешено"


def human_common(value: str) -> str:
    value = (value or "").strip()
    if value in COMMON_LABELS:
        return COMMON_LABELS[value]
    if value in STATUS_LABELS:
        return STATUS_LABELS[value]
    if value in CAPABILITY_LABELS:
        return CAPABILITY_LABELS[value]
    if value.startswith("OPEN_"):
        return "Открыто: требуемое доказательство ещё не получено"
    return value or "Не заполнено"


def human_scope(value: str) -> str:
    return translated(value, SCOPE_LABELS, "Комбинированный слой; подробности в карточке")


def human_role(value: str) -> str:
    return translated(value, ROLE_LABELS, "Роль требования нуждается в пояснении")


def human_group(value: str) -> str:
    return translated(value, GROUP_LABELS, "Состав группы должен быть уточнён")


def human_capacity(value: str) -> str:
    return translated(value, CAPACITY_LABELS, "Способ расчёта мощности нужно описать по-русски")


def human_media(value: str) -> str:
    return translated(value, MEDIA_LABELS, "Другой локальный формат")


def human_relation(value: str) -> str:
    return translated(value, RELATION_LABELS, "тип связи требует ручной проверки")


def human_medical_lane(value: str) -> str:
    return translated(value, MEDICAL_LANE_LABELS, "Аудитория должна быть уточнена")


def human_language(value: str) -> str:
    return translated(value, LANGUAGE_LABELS, "Язык нужно уточнить")


def human_inventory_category(value: str) -> str:
    return translated(value, INVENTORY_CATEGORY_LABELS, "Другая категория")


def human_inventory_formula(value: str) -> str:
    return translated(value, INVENTORY_FORMULA_LABELS, "формулу нужно описать по-русски")


def human_inventory_limitation(value: str) -> str:
    return translated(value, INVENTORY_LIMITATION_LABELS, "ограничение доказательства нужно уточнить")


def human_execution_policy(value: str, safety: str) -> str:
    if safety.startswith("S4_") or "REFERENCE_ONLY" in value:
        return "Только справочное хранение; не выполнять в быту"
    if safety.startswith("S3_") or "LICENSED" in value:
        return "Только лицензированный специалист в законных условиях"
    if safety.startswith("S2_"):
        return "Только после обучения или под надзором"
    if safety.startswith("S1_"):
        return "Бытовая работа после проверки условий и инструкции"
    return "Только наблюдение, чтение и планирование"


def human_prose(value: str) -> str:
    """Hide backend shorthand when registry prose is shown to the user."""
    result = value or ""
    phrase_replacements = (
        ("Рецензированные P0-карточки первой помощи", "Рецензированные карточки первой помощи для первых 72 часов"),
        ("P0-карточки", "карточки первой необходимости"),
        ("P0-карточек", "карточек первой необходимости"),
        ("P0/P1 сценариев", "сценариев первых двух уровней срочности"),
        ("P0/P1-сценариев", "сценариев первых двух уровней срочности"),
        ("Печатное P0/P1 ядро", "Печатное ядро первых двух уровней срочности"),
        ("lay action cards", "карточек действий для неспециалиста"),
        ("lay action card", "карточка действий для неспециалиста"),
        ("action cards", "карточки действий"),
        ("action card", "карточка действий"),
        ("Safety gates", "проверки безопасности"),
        ("CO detection", "обнаружение угарного газа"),
        ("DC архитектура", "архитектура постоянного тока"),
        ("backfeed", "обратная подача энергии"),
        ("Black start", "запуск после полного обесточивания"),
        ("BLS и AED", "базовая реанимация и автоматический наружный дефибриллятор"),
        ("BLS/AED", "базовая реанимация и автоматический наружный дефибриллятор"),
        ("BLS", "базовая реанимация"),
        ("continuity plans", "планы непрерывности"),
        ("map pack", "комплект карт"),
        ("Blank-device restore", "восстановление на чистом устройстве"),
        ("readers", "программы чтения"),
        ("released-корпуса", "выпущенного корпуса"),
        ("primary", "основной ответственный"),
        ("digesters and gas storage", "реакторы и хранение газа"),
        ("producer gas and syngas", "генераторный газ и синтез-газ"),
        ("urine diversion and biosolids", "отведение мочи и биотвёрдые остатки"),
        ("biofertilizers", "биоудобрения"),
        ("Caregiver dependencies", "зависимости от ухаживающих"),
        ("human single points of failure", "единичные точки отказа персонала"),
        ("rescue medicines", "экстренные препараты"),
        ("advance plan", "заранее согласованный план"),
        ("first flush", "отвод первого стока"),
        ("risk profile", "профиль риска"),
        ("caregiver hygiene", "гигиена ухода"),
        ("carrying capacity", "допустимая нагрузка"),
        ("zoonoses", "зоонозы"),
        ("Shelter-in-place", "укрытие на месте"),
        ("power banks", "внешние аккумуляторы"),
        ("Missed-check-in escalation", "порядок эскалации при пропуске контрольной связи"),
        ("Reunification plan", "план воссоединения"),
        ("read-back", "повторное подтверждение"),
        ("Abandonment plan", "план отказа от транспорта"),
        ("safeguarding", "защита уязвимых людей"),
        ("reference surfaces", "эталонные поверхности"),
        ("workholding", "фиксация детали"),
        ("life-safety", "жизнеобеспечение"),
        ("decision rule", "правило принятия решения"),
        ("fallback", "резервный способ"),
        ("inspection", "осмотр"),
        ("hot work", "огневые работы"),
        ("stored energy", "накопленная энергия"),
        ("drill press", "сверлильный станок"),
        ("recertification", "повторная сертификация"),
        ("Teach-back", "обратное объяснение"),
        ("fixity-проверка", "проверка неизменности"),
        ("offsite", "удалённые"),
        ("runtimes", "среды выполнения"),
        ("reproducible build", "воспроизводимая сборка"),
        ("donor plan", "план донорских деталей"),
        ("provenance", "происхождение и история"),
        ("reorder point", "точка повторного заказа"),
        ("chain of custody", "цепочка ответственного хранения"),
        ("After-action review", "разбор после действий"),
        ("adaptive pathways", "адаптивные сценарии"),
        ("Guideline governance; evidence synthesis и pharmacovigilance", "управление клиническими руководствами, синтез доказательств и фармаконадзор"),
        ("environmental health", "гигиена окружающей среды"),
        ("Environmental и climate health", "экологическое и климатическое здоровье"),
        ("One Health", "единое здоровье людей, животных и среды"),
        ("medication safety", "безопасность лекарств"),
        ("lawful formulary", "законный перечень лекарств"),
        ("Health records; privacy; backup и patient matching", "медицинские записи, приватность, дублирование и сопоставление пациента"),
        ("Public-health records; демография и outbreak history", "записи общественного здравоохранения, демография и история вспышек"),
        ("nursing; pharmacy и public-health", "сестринских, фармацевтических и общественного здравоохранения"),
        ("biological safety", "биологическая безопасность"),
        ("plant health и pesticides", "здоровье растений и пестициды"),
        ("professional sign-off", "подпись уполномоченного специалиста"),
        ("checked date", "дата проверки"),
        ("welfare; slaughter", "благополучие животных, убой"),
        ("Crush и blast injury", "сдавление и взрывная травма"),
        ("caregiver/nursing support", "повседневный уход и сестринская поддержка"),
        ("person-specific plan", "индивидуальный план"),
        ("HIV/TB", "ВИЧ и туберкулёз"),
        ("STI-маршрут", "маршрут по инфекциям, передаваемым половым путём"),
        ("outbreak reporting", "учёт вспышек"),
        ("supply register", "реестр медицинского снабжения"),
        ("first-aid/caregiver", "первой помощи и ухода"),
        ("Emergency и critical care", "неотложная и интенсивная помощь"),
        ("Primary и community medicine", "первичная и общественная медицина"),
        ("long-term care", "долгосрочный уход"),
        ("NCD", "неинфекционные заболевания"),
        ("IPC и antimicrobial stewardship", "профилактика и контроль инфекций и рациональное применение антимикробных препаратов"),
        ("midwifery", "акушерская практика"),
        ("substance-use care", "помощь при зависимостях"),
        ("assistive technology", "вспомогательные технологии"),
        ("malnutrition и refeeding", "недостаточность питания и возобновление питания"),
        ("trauma surgery", "травматологическая хирургия"),
        ("samples и quality control", "пробы и контроль качества"),
        ("respiratory equipment", "дыхательное оборудование"),
        ("Biomedical engineering", "медицинская инженерия"),
        ("healthcare facility IPC", "инфекционный контроль в медицинском учреждении"),
        ("Clinic design; triage flow; registry; referral и transport", "проектирование клиники, поток сортировки, реестр, направление и транспорт"),
        ("Medical supply chain; anti-counterfeit и recalls", "цепочка медицинского снабжения, защита от подделок и отзывы"),
        ("surveillance и outbreak management", "эпиднадзор и управление вспышками"),
        ("medical overlay", "медицинская локализация"),
        ("Peer review; incident и morbidity/mortality review", "коллегиальная проверка, разбор инцидентов, заболеваемости и смертности"),
        ("referral network", "сеть направлений к специалистам"),
        ("referral", "направление к специалисту"),
        ("GMP и регулируемое", "надлежащая производственная практика и регулируемое"),
        ("Clinical research и trials governance", "клинические исследования и управление испытаниями"),
        ("counselling", "консультирование"),
        ("accession-level", "учётом каждой партии"),
        ("accession-register", "реестр партий"),
        ("open-pollinated", "сорт с открытым опылением"),
        ("OP; landrace; F1 hybrid", "сорт с открытым опылением; местный сорт; гибрид первого поколения"),
        ("harvest-to-seed protocol", "протокол получения семян из урожая"),
        ("germination test", "проверка всхожести"),
        ("duplicate store", "отдельное резервное хранилище"),
        ("Portugal overlay", "локализация для Португалии"),
        ("Portugal-узлов", "узлов португальского слоя"),
        ("site-specific", "привязанных к конкретному объекту"),
        ("item-level", "каждой позиции"),
        ("medication list", "список назначенных лекарств"),
        ("treatment train", "проверенная цепочка очистки"),
        ("production package", "производственного пакета"),
        ("load profile", "профиля нагрузки"),
        ("PACE-связь", "связь с основным и резервными каналами"),
        ("Primary/Alternate/Contingency/Emergency", "основные, альтернативные, резервные и аварийные"),
        ("check-in", "контрольной связи"),
        ("rights review", "проверка прав"),
        ("human review", "ручная предметная проверка"),
        ("фактических payload", "фактических локальных файлов"),
        ("по каждому payload", "по каждому локальному файлу"),
        ("несколько payload", "несколько локальных файлов"),
        ("payload", "локальный файл"),
        ("keep/replace/quarantine", "сохранить, заменить или изолировать"),
        ("ZIM open", "открытие архива ZIM"),
        ("end-to-end", "сквозной"),
        ("manifest/hash", "манифест и контрольные суммы"),
        ("restore drill", "тренировка восстановления"),
        ("Role matrix", "матрица ролей"),
        ("handover drill", "тренировка передачи управления"),
        ("handover", "передача информации и ответственности"),
        ("Site walk", "обход объекта"),
        ("smoke/CO alarms", "извещатели дыма и угарного газа"),
        ("CO alarm", "извещатель угарного газа"),
        ("near misses", "опасные почти-инциденты"),
        ("corrective action", "корректирующие действия"),
        ("Asset/source owner", "ответственный за имущество или источник"),
        ("next_due", "следующий срок"),
        ("spare level", "уровень запасных частей"),
        ("work log", "журнал работ"),
        ("failure history", "история отказов"),
        ("trigger for replacement", "условие замены"),
        ("facility controls", "меры контроля объекта"),
        ("incident plan", "план действий при инциденте"),
        ("annual review", "ежегодная проверка"),
        ("drills", "тренировок"),
        ("drill", "тренировка"),
        ("reader", "программа чтения"),
        ("launch", "запуск"),
        ("consent", "согласие"),
        ("accession", "зарегистрированных партий"),
        ("lot", "номер партии"),
        ("N1|N2|N3_TO_N7", "1 человек / 2 человека / группа 3–7 человек"),
        ("Командные роли N2–N7 при неотложной помощи", "Роли участников группы из 2–7 человек при неотложной помощи"),
        ("N2–N7", "группа 2–7 человек"),
        ("backup", "дублёр"),
        ("interval", "интервал"),
        ("capacity", "мощность"),
        ("owner", "ответственный"),
        ("review", "проверка"),
    )
    for source, replacement in phrase_replacements:
        result = result.replace(source, replacement)
    replacements = (
        (r"\bUNASSIGNED/TBD\b", "ответственный и срок не назначены"),
        (r"\bREFERENCE_ONLY\b", "только справочный материал"),
        (r"\bN3_TO_N7\b", "группа 3–7 человек"),
        (r"\bP0/P1\b", "первая и следующая необходимость"),
        (r"\bP0(?=[-‑–— ])", "первая необходимость"),
        (r"\bS3/S4\b", "профессиональные и справочные темы"),
        (r"\bBOM\b", "ведомость материалов"),
        (r"\bPACE(?=[-‑–— ])", "схема основных и резервных каналов"),
        (r"\bWASH(?=[-‑–— ]|\b)", "вода, санитария и гигиена"),
        (r"\bPPE\b", "средства индивидуальной защиты"),
        (r"\bCO\b", "угарный газ"),
        (r"\bDMG\b", "образ установщика"),
    )
    for pattern, replacement in replacements:
        result = re.sub(pattern, replacement, result)
    return result


def short_label(value: str, limit: int = 90) -> str:
    label = " ".join((value or "").replace("|", "/").replace("]", ")").split())
    if not label:
        return "Открыть карточку"
    return label if len(label) <= limit else label[: limit - 1].rstrip() + "…"


def read_csv(relative_path: str) -> List[Dict[str, str]]:
    path = ROOT / relative_path
    if not path.is_file():
        die(f"required registry is missing: {relative_path}")
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        rows = list(csv.DictReader(handle))
    if not rows:
        die(f"required registry is empty: {relative_path}")
    return [{key: (value or "").strip() for key, value in row.items()} for row in rows]


def unique_by(rows: Sequence[Mapping[str, str]], key: str, source: str) -> Dict[str, Mapping[str, str]]:
    result: Dict[str, Mapping[str, str]] = {}
    for number, row in enumerate(rows, start=2):
        identifier = row.get(key, "").strip()
        if not identifier:
            die(f"blank {key}: {source}:{number}")
        if identifier in result:
            die(f"duplicate {key}={identifier}: {source}:{number}")
        result[identifier] = row
    return result


def safe_identifier(identifier: str) -> str:
    safe = re.sub(r"[^A-Za-z0-9_.-]+", "-", identifier).strip("-")
    if not safe:
        die(f"unsafe identifier: {identifier!r}")
    return safe


def atomic_link(kind: str, prefix: str, identifier: str, label: str) -> str:
    stem = f"{prefix} {safe_identifier(identifier)}"
    path = ATOMIC / kind / f"{stem}.md"
    if not path.is_file():
        die(f"atomic note target is missing: {path.relative_to(VAULT)}")
    return f"[[90_GENERATED_CATALOG/{kind}/{stem}|{short_label(label)}]]"


def dashboard_link(filename: str, label: str) -> str:
    if filename not in EXPECTED_PAGES:
        die(f"unknown dashboard target: {filename}")
    return f"[[{OUT.name}/{Path(filename).stem}|{label}]]"


def yaml_string(value: str) -> str:
    return json.dumps(value, ensure_ascii=False)


def cell(value: object) -> str:
    text = str(value).strip() if value is not None else ""
    if not text:
        return "—"
    # A table cell must escape Obsidian's wikilink alias separator. Protect
    # whole wikilinks while converting ordinary pipes from raw CSV values.
    protected: List[str] = []

    def hold(match: "re.Match[str]") -> str:
        link = match.group(0)
        if "|" in link:
            link = link.replace("|", r"\|", 1)
        protected.append(link)
        return f"@@WIKILINK_{len(protected) - 1}@@"

    text = re.sub(r"\[\[[^\]]+\]\]", hold, text)
    text = text.replace("\r\n", "<br>").replace("\n", "<br>").replace("|", "<br>")
    for number, link in enumerate(protected):
        text = text.replace(f"@@WIKILINK_{number}@@", link)
    return text


def table(headers: Sequence[str], rows: Iterable[Sequence[object]]) -> str:
    rendered = ["| " + " | ".join(cell(header) for header in headers) + " |"]
    rendered.append("| " + " | ".join("---" for _ in headers) + " |")
    count = 0
    for row in rows:
        values = list(row)
        if len(values) != len(headers):
            die(f"table row has {len(values)} cells, expected {len(headers)}")
        rendered.append("| " + " | ".join(cell(value) for value in values) + " |")
        count += 1
    if count == 0:
        rendered.append("| " + " | ".join("—" for _ in headers) + " |")
    return "\n".join(rendered)


def frontmatter(identifier: str, title: str, release_version: str) -> str:
    return "\n".join(
        [
            "---",
            f"id: {yaml_string(identifier)}",
            "kind: dashboard",
            f"title: {yaml_string(title)}",
            "generated: true",
            "generator: build_obsidian_user_views.py",
            f"release_version: {yaml_string(release_version)}",
            "proof_state: CATALOG_VIEW_NOT_OPERATIONAL_PROOF",
            "instruction_state: NAVIGATION_ONLY_NOT_EXECUTABLE",
            "---",
        ]
    )


def proof_boundary(extra: str = "") -> str:
    lines = [
        "> [!warning] Граница доказательства",
        "> Эта страница показывает строки реестров и ссылки на каталожные карточки. Она не доказывает наличие вещей, готовность процедуры, квалификацию, актуальность локальных правил или успешное испытание.",
    ]
    if extra:
        lines.append(f"> {extra}")
    return "\n".join(lines)


def guidance_blocks(identifier: str) -> str:
    if identifier not in PAGE_GUIDANCE:
        die(f"page guidance is missing: {identifier}")
    why, before, related_items, after = PAGE_GUIDANCE[identifier]
    related = " · ".join(
        dashboard_link(DASHBOARD_FILES[key], label) for key, label in related_items
    )
    return "\n\n".join(
        [
            "## Зачем нужен этот документ\n\n" + why,
            "## Что должно быть известно/готово до него\n\n" + before,
            "## Что связано\n\n" + related,
            "## Что делать после\n\n" + after,
        ]
    )


def page(identifier: str, title: str, release_version: str, body: str, extra_warning: str = "") -> str:
    return (
        frontmatter(identifier, title, release_version)
        + "\n\n# "
        + title
        + "\n\n"
        + proof_boundary(extra_warning)
        + "\n\n"
        + guidance_blocks(identifier)
        + "\n\n"
        + body.rstrip()
        + "\n"
    )


def visible_markdown(markdown: str) -> str:
    """Return what a reader sees: no frontmatter and wikilink targets replaced by aliases."""
    visible = markdown
    if visible.startswith("---\n"):
        parts = visible.split("\n---\n", 1)
        if len(parts) != 2:
            die("generated dashboard has malformed frontmatter")
        visible = parts[1]

    def show_alias(match: "re.Match[str]") -> str:
        raw = match.group(1)
        if r"\|" in raw:
            return raw.split(r"\|", 1)[1]
        if "|" in raw:
            return raw.split("|", 1)[1]
        return raw

    return re.sub(r"\[\[([^\]]+)\]\]", show_alias, visible)


def validate_generated_pages(pages: Mapping[str, str]) -> None:
    """Fail closed on presentation regressions before touching the Vault."""
    legacy_names = set(LEGACY_GENERATED_PAGES) | {"20_DASHBOARDS"}
    visible_raw_code = re.compile(
        r"\b(?:"
        r"P[0-4](?:_[A-Z]+)?|SL[0-6]|S[0-4](?:_[A-Z0-9_]+)?|N[1-7]|"
        r"UNASSIGNED|TBD(?:_NOT_SCHEDULED)?|DENY(?:_[A-Z0-9_]+)?|MISSING|"
        r"ARCHITECTURE_ONLY|REFERENCE_ONLY|ALLOW|"
        r"HEALTH|WATER_WASH|FOOD_AGRI|PEOPLE_CARE|MAPS_COMMS|ENERGY_FUELS|"
        r"GOVERNANCE|PORTUGAL|HAZARD|SYSTEM|BASE|CONSTRUCTION|EDUCATION|"
        r"ENERGY|ENVIRONMENT|KNOWLEDGE|MATERIALS|SECURITY|SHELTER|TRANSPORT|"
        r"WORKSHOP|ANIMALS"
        r")\b"
    )
    visible_backend_word = re.compile(r"\b(?:gap|gaps|payload|backend)\b", re.IGNORECASE)
    visible_english_heading = re.compile(
        r"\b(?:Owner|Due|Gate|Capability|Outcome|Role|Capacity|Target|Actual|"
        r"Payload|Crosswalk|Architecture|Missing|Reference|Allow)\b"
    )
    guidance_headings = (
        "## Зачем нужен этот документ",
        "## Что должно быть известно/готово до него",
        "## Что связано",
        "## Что делать после",
    )

    for filename, markdown in pages.items():
        for heading in guidance_headings:
            if markdown.count(heading) != 1:
                die(f"dashboard guidance block mismatch: {filename}: {heading}")
        if any(name in markdown for name in legacy_names):
            die(f"legacy dashboard reference leaked into {filename}")

        identifier_match = re.search(r'^id:\s*(.+)$', markdown, re.MULTILINE)
        if not identifier_match:
            die(f"dashboard id is missing: {filename}")
        identifier = json.loads(identifier_match.group(1))

        dashboard_targets: List[str] = []
        for raw in re.findall(r"\[\[([^\]]+)\]\]", markdown):
            separator = r"\|" if r"\|" in raw else "|" if "|" in raw else ""
            target = (raw.split(separator, 1)[0] if separator else raw).split("#", 1)[0].strip()
            if target.startswith("90_GENERATED_CATALOG/"):
                if not separator or not raw.split(separator, 1)[1].strip():
                    die(f"atomic link without a user-facing alias: {filename}: {raw}")
            if target.startswith(f"{OUT.name}/"):
                dashboard_targets.append(target)

        if filename != DASHBOARD_FILES["index"]:
            expected_targets = {
                f"{OUT.name}/{Path(DASHBOARD_FILES[key]).stem}"
                for key, _label in PAGE_GUIDANCE[identifier][2]
            }
            actual_targets = set(dashboard_targets)
            if actual_targets != expected_targets or len(dashboard_targets) != len(expected_targets):
                die(
                    f"dashboard semantic-link mismatch: {filename}: "
                    f"expected={sorted(expected_targets)} actual={dashboard_targets}"
                )
            if not 2 <= len(expected_targets) <= 4:
                die(f"dashboard must have 2-4 semantic links: {filename}")
            index_target = f"{OUT.name}/{Path(DASHBOARD_FILES['index']).stem}"
            if index_target in actual_targets:
                die(f"non-index dashboard must not backlink to the index: {filename}")

        visible = visible_markdown(markdown)
        for pattern, label in (
            (visible_raw_code, "raw backend code"),
            (visible_backend_word, "backend jargon"),
            (visible_english_heading, "English presentation label"),
        ):
            match = pattern.search(visible)
            if match:
                line = visible.count("\n", 0, match.start()) + 1
                die(f"{label} is visible in {filename}:{line}: {match.group(0)}")


def priority_key(row: Mapping[str, str]) -> Tuple[int, int, str, str]:
    return (
        PRIORITY_ORDER.get(row.get("priority_tier", ""), 99),
        SERVICE_ORDER.get(row.get("earliest_service_level", ""), 99),
        row.get("domain", ""),
        row.get("node_id", ""),
    )


def gap_key(row: Mapping[str, str]) -> Tuple[int, int, str]:
    return (
        PRIORITY_ORDER.get(row.get("priority_tier", ""), 99),
        SERVICE_ORDER.get(row.get("earliest_service_level", ""), 99),
        row.get("gap_id", ""),
    )


def service_key(row: Mapping[str, str]) -> Tuple[int, str, str]:
    return (
        SERVICE_ORDER.get(row.get("service_level", ""), 99),
        row.get("outcome_node_id", ""),
        row.get("service_requirement_id", ""),
    )


def release_version_from(*row_groups: Sequence[Mapping[str, str]]) -> str:
    versions = Counter(
        row.get("release_version", "")
        for rows in row_groups
        for row in rows
        if row.get("release_version", "")
    )
    return versions.most_common(1)[0][0] if versions else "UNVERSIONED"


def tech_table_rows(rows: Sequence[Mapping[str, str]]) -> Iterable[Sequence[object]]:
    for row in sorted(rows, key=priority_key):
        yield (
            human_priority(row["priority_tier"]),
            human_service(row["earliest_service_level"]),
            human_domain(row["domain"]),
            atomic_link("technology", "TEC", row["node_id"], human_prose(row["title_ru"])),
            human_safety(row["safety_class"]),
            human_capability(row["capability_status"]),
            human_gate(row["release_gate"]),
        )


def tech_table(rows: Sequence[Mapping[str, str]]) -> str:
    return table(
        ("Срочность", "Когда должна работать", "Область", "Открыть карточку", "Граница безопасности", "Состояние", "Разрешение"),
        tech_table_rows(rows),
    )


def medical_lane(row: Mapping[str, str]) -> str:
    safety = row.get("safety_class", "")
    # Legacy methods are intentionally kept outside the lay operational view
    # even when their registry row is S0/read-only.
    if row.get("node_id", "").endswith("-P4-LEGACY"):
        return "REFERENCE"
    if safety.startswith("S4_"):
        return "REFERENCE"
    if safety.startswith("S3_"):
        return "CLINICIAN"
    if safety.startswith("S2_"):
        return "TRAINED"
    return "LAY"


def local_payload_link(relative_path: str) -> str:
    payload = ROOT / "offline-library" / relative_path
    if not payload.is_file():
        return "Локальный файл отсутствует"
    encoded = quote(relative_path, safe="/-_.")
    return f"[открыть файл](../../offline-library/{encoded})"


def make_pages() -> Tuple[Dict[str, str], Dict[str, int]]:
    technology_raw = read_csv("technology-dependency-register.csv")
    planning = read_csv("technology-node-planning-register.csv")
    services = read_csv("technology-service-level-register.csv")
    gaps = read_csv("known-gap-register.csv")
    payloads = read_csv("offline-library/offline-payload-register.csv")
    payload_crosswalks = read_csv("payload-source-crosswalk.csv")
    inventory = read_csv("inventory-template.csv")

    tech_by_id = unique_by(technology_raw, "node_id", "technology-dependency-register.csv")
    plan_by_id = unique_by(planning, "node_id", "technology-node-planning-register.csv")
    unique_by(services, "service_requirement_id", "technology-service-level-register.csv")
    unique_by(gaps, "gap_id", "known-gap-register.csv")
    unique_by(payloads, "payload_id", "offline-library/offline-payload-register.csv")
    crosswalk_by_payload = unique_by(payload_crosswalks, "payload_id", "payload-source-crosswalk.csv")
    unique_by(inventory, "item_id", "inventory-template.csv")

    missing_plans = sorted(set(tech_by_id) - set(plan_by_id))
    extra_plans = sorted(set(plan_by_id) - set(tech_by_id))
    if missing_plans or extra_plans:
        die(f"technology/planning mismatch missing={missing_plans[:5]} extra={extra_plans[:5]}")

    missing_payload_links = sorted({row["payload_id"] for row in payloads} - set(crosswalk_by_payload))
    extra_payload_links = sorted(set(crosswalk_by_payload) - {row["payload_id"] for row in payloads})
    if missing_payload_links or extra_payload_links:
        die(
            "payload/crosswalk mismatch "
            f"missing={missing_payload_links[:5]} extra={extra_payload_links[:5]}"
        )

    technology: List[Dict[str, str]] = []
    for row in technology_raw:
        merged = dict(row)
        plan = plan_by_id[row["node_id"]]
        merged["priority_tier"] = plan.get("priority_tier", "")
        merged["priority_horizon"] = plan.get("priority_horizon", "")
        merged["earliest_service_level"] = plan.get("earliest_service_level", "")
        merged["group_size_scope"] = plan.get("group_size_scope", "")
        merged["owner_role"] = plan.get("owner_role", "")
        merged["next_due"] = plan.get("next_due", "")
        technology.append(merged)

    release_version = release_version_from(technology_raw, planning, services, gaps, payload_crosswalks)
    p0_technology = [row for row in technology if row["priority_tier"] == "P0_RED"]
    p0_materializable = [
        row
        for row in p0_technology
        if not row["safety_class"].startswith("S3_")
        and not row["safety_class"].startswith("S4_")
    ]
    p0_restricted = [
        row
        for row in p0_technology
        if row["safety_class"].startswith("S3_")
        or row["safety_class"].startswith("S4_")
    ]
    p0_gaps = [row for row in gaps if row["priority_tier"] == "P0_RED"]
    health = [row for row in technology if row["domain"] == "HEALTH"]
    food = [row for row in technology if row["domain"] == "FOOD_AGRI"]
    portugal = [row for row in technology if row["domain"] == "PORTUGAL"]
    restricted = [
        row
        for row in technology
        if row["safety_class"].startswith("S3_") or row["safety_class"].startswith("S4_")
    ]

    seed_pattern = re.compile(
        r"SEED|CROP|GERM|POLLIN|PROPAG|ACCESSION|VARIET|NURSERY|HARVEST|BREED",
        re.IGNORECASE,
    )
    seed_title_pattern = re.compile(r"семен|всхож|сорт|опыл|культур|урож", re.IGNORECASE)
    seed_focus = [
        row
        for row in food
        if seed_pattern.search(row["node_id"]) or seed_title_pattern.search(row["title_ru"])
    ]

    status_counts = Counter(row["capability_status"] for row in technology)
    priority_counts = Counter(row["priority_tier"] for row in technology)
    safety_counts = Counter(row["safety_class"] for row in technology)
    domain_counts = Counter(row["domain"] for row in technology)
    open_gap_count = sum(row["status"].startswith("OPEN") for row in gaps)
    allow_count = sum(
        row["capability_status"] == "ALLOW" or row["release_gate"] == "ALLOW"
        for row in technology
    )
    byte_total = sum(int(row["byte_size"] or 0) for row in payloads)
    media_counts = Counter(row["media_type"] for row in payloads)
    inventory_actual_filled = sum(bool(row["actual_quantity"]) for row in inventory)
    inventory_allow = sum(row["gate_decision"] == "ALLOW" for row in inventory)
    inventory_physically_verified = sum(
        bool(row["actual_quantity"])
        and row["item_status"].lower() not in {"", "planned"}
        and row["evidence_type"] not in {"", "UNSELECTED"}
        and row["check_result"] not in {"", "UNKNOWN", "NOT_TESTED"}
        for row in inventory
    )

    pages: Dict[str, str] = {}

    index_body = "\n".join(
        [
            "**CSV — внутренний машинный источник данных; пользователю открывать его не нужно.** Все основные срезы ниже уже собраны в обычные страницы Obsidian с кликабельными карточками.",
            "",
            "## Начать здесь",
            "",
            f"1. {dashboard_link(DASHBOARD_FILES['readiness'], 'Честный статус готовности')} — что реально есть и где доказательств нет.",
            f"2. {dashboard_link(DASHBOARD_FILES['p0'], 'Первые 72 часа')} — {len(p0_technology)} узла первой необходимости: {len(p0_materializable)} низко- и среднерисковых для дальнейшей работы, {len(p0_restricted)} только в профессиональном или справочном контуре и {len(p0_gaps)} реальных блокеров.",
            f"3. {dashboard_link(DASHBOARD_FILES['inventory'], 'Физический инвентарь')} — {len(inventory)} плановых позиций, физически подтверждено {inventory_physically_verified}.",
            f"4. {dashboard_link(DASHBOARD_FILES['medicine'], 'Медицинская помощь')} — все {len(health)} медицинских узлов с разделением для неспециалиста, обученного помощника, клинициста и чисто справочного уровня.",
            f"5. {dashboard_link(DASHBOARD_FILES['gaps'], 'Что ещё не готово')} — все {len(gaps)} незакрытые работы и нужные доказательства.",
            f"6. {dashboard_link(DASHBOARD_FILES['services'], 'Уровни автономности')} — все {len(services)} требований от немедленного спасения до межпоколенческой передачи.",
            f"7. {dashboard_link(DASHBOARD_FILES['offline'], 'Офлайн-библиотека')} — все {len(payloads)} реально сохранённые локальные файлы и их связи.",
            f"8. {dashboard_link(DASHBOARD_FILES['domains'], 'Области знаний и систем')} — распределение всех {len(technology)} узлов.",
            f"9. {dashboard_link(DASHBOARD_FILES['food'], 'Семена и питание')} — все {len(food)} узлов питания, земледелия и семян.",
            f"10. {dashboard_link(DASHBOARD_FILES['portugal'], 'Португалия')} — все {len(portugal)} локализованных узлов.",
            f"11. {dashboard_link(DASHBOARD_FILES['safety'], 'Границы безопасности')} — пять уровней ограничений и все {len(restricted)} профессиональных и справочных узла без опасных рецептур.",
            "",
            "## Короткий статус",
            "",
            table(
                ("Показатель", "Сейчас", "Интерпретация"),
                [
                    ("Технологические узлы", len(technology), "ширина каталога, не готовность"),
                    ("Разрешено к исполнению", allow_count, "ни одна возможность не выпущена к исполнению"),
                    ("Открытые работы", open_gap_count, "требуют ответственного, срока и доказательства"),
                    ("Файлы на диске", len(payloads), "файл на диске, не готовая инструкция"),
                    ("Суммарный объём файлов", f"{byte_total} байт", "машинно проверяемый корпус"),
                ],
            ),
            "",
            "## Как читать карточки",
            "",
            "- **Не создано или не подтверждено** — результата и доказательства нет.",
            "- **Есть только структура** — описана архитектура, но она не реализована.",
            "- **Только справочный материал** — бытовое исполнение не разрешено.",
            "- **Не разрешено** — узел нельзя считать готовым или рекомендованным к исполнению.",
            "- Файл, PDF, таблица или ссылка сами по себе не доказывают физическую возможность и навык.",
        ]
    )
    pages[DASHBOARD_FILES["index"]] = page(
        "dashboard-index",
        "Пользовательские панели автономного кита",
        release_version,
        index_body,
    )

    readiness_status_rows = [
        (human_capability(status), status_counts.get(status, 0))
        for status in ("ARCHITECTURE_ONLY", "MISSING", "REFERENCE_ONLY", "ALLOW")
    ]
    readiness_priority_rows = [
        (human_priority(priority), priority_counts.get(priority, 0)) for priority in PRIORITY_ORDER
    ]
    critical_gap_ids = (
        "GAP-001",
        "GAP-002",
        "GAP-003",
        "GAP-004",
        "GAP-005",
        "GAP-006",
        "GAP-007",
        "GAP-008",
        "GAP-009",
        "GAP-010",
        "GAP-011",
        "GAP-012",
        "GAP-013",
        "GAP-014",
        "GAP-020",
        "GAP-021",
        "GAP-026",
        "GAP-027",
        "GAP-028",
    )
    gap_lookup = {row["gap_id"]: row for row in gaps}
    readiness_gaps = [gap_lookup[identifier] for identifier in critical_gap_ids if identifier in gap_lookup]
    readiness_body = "\n".join(
        [
            "## Итог",
            "",
            f"Каталог содержит **{len(technology)}** технологических узлов, но к исполнению разрешено **{allow_count}**. Это список работ и зависимостей, а не готовый автономный комплекс. Все **{len(gaps)}** незакрытые работы остаются открытыми.",
            "",
            "## Состояние возможностей",
            "",
            table(("Статус", "Узлов"), readiness_status_rows),
            "",
            "## Очерёдность",
            "",
            table(("Приоритет", "Узлов"), readiness_priority_rows),
            "",
            "## Границы безопасности",
            "",
            table(("Граница", "Узлов"), ((human_safety(key), value) for key, value in sorted(safety_counts.items()))),
            "",
            "## Критические незакрытые доказательства",
            "",
            table(
                ("Незакрытая работа", "Срочность", "Когда нужна", "Что блокирует", "Текущее доказательство", "Разрешение"),
                (
                    (
                        atomic_link("known-gap", "GAP", row["gap_id"], human_prose(row["gap_ru"])),
                        human_priority(row["priority_tier"]),
                        human_service(row["earliest_service_level"]),
                        human_prose(row["gap_ru"]),
                        human_prose(row["current_evidence"]),
                        human_gate(row["release_gate"]),
                    )
                    for row in sorted(readiness_gaps, key=gap_key)
                ),
            ),
            "",
            "## Лестница доказательств",
            "",
            "1. Узел только перечислен в каталоге.",
            "2. Файл фактически сохранён и машинно проверен.",
            "3. Компетентный человек проверил содержание и локальную применимость.",
            "4. Выпущена короткая процедура, чертёж или ведомость материалов с критериями и стоп-условиями.",
            "5. Имущество и место физически осмотрены.",
            "6. Выполнено испытание или тренировка.",
            "7. Есть ответственный, дублёр, срок и повторная проверка.",
            "",
            "Текущий кит в основном находится на ступени 1; отдельные 16 локальных файлов имеют машинную часть ступени 2. Нельзя автоматически повышать их до следующих ступеней.",
        ]
    )
    pages[DASHBOARD_FILES["readiness"]] = page(
        "dashboard-readiness",
        "Готовность: что доказано, а что нет",
        release_version,
        readiness_body,
    )

    p0_domain_counts = Counter(row["domain"] for row in p0_materializable)
    p0_body = "\n".join(
        [
            "Первая необходимость охватывает горизонт от секунд до 72 часов, но не даёт разрешения на исполнение. Автоматический приоритет ещё должен быть пересчитан под людей и объект. На этой странице сначала показаны реальные незакрытые доказательства, затем только низко- и среднерисковые кандидаты. Профессиональные и справочные темы из очереди действий исключены.",
            "",
            "## Сводка первой необходимости",
            "",
            table(
                ("Срез", "Количество", "Что это значит"),
                [
                    ("Все узлы первой необходимости", len(p0_technology), "общая каталожная срочность; не очередь действий"),
                    ("Низко- и среднерисковый контур", len(p0_materializable), "кандидаты на дальнейшую рецензию, комплектацию и тест; текущее решение о допуске всё равно обязательно"),
                    ("Профессиональный и справочный контур", len(p0_restricted), "не бытовая инструкция; не входит в очередь действий"),
                    ("Открытые блокеры первой необходимости", len(p0_gaps), "реальные блокеры, для которых нужно следующее доказательство"),
                ],
            ),
            "",
            f"## A. Реальные незакрытые задачи и блокеры первой необходимости — {len(p0_gaps)}",
            "",
            table(
                ("Незакрытая работа", "Когда нужна", "Область", "Что блокирует", "Следующее требуемое доказательство", "Текущее доказательство", "Ответственный", "Срок", "Разрешение"),
                (
                    (
                        atomic_link("known-gap", "GAP", row["gap_id"], human_prose(row["gap_ru"])),
                        human_service(row["earliest_service_level"]),
                        human_domain(row["domain"]),
                        human_prose(row["gap_ru"]),
                        human_prose(row["required_evidence"]),
                        human_prose(row["current_evidence"]),
                        human_common(row["owner"]),
                        human_common(row["due"]),
                        human_gate(row["release_gate"]),
                    )
                    for row in sorted(p0_gaps, key=gap_key)
                ),
            ),
            "",
            f"## B. Низко- и среднерисковые узлы для дальнейшей материализации — {len(p0_materializable)}",
            "",
            "Это означает только допустимый низко- или среднерисковый контур для дальнейшей работы. Перед исполнением всё равно нужны применимость, надёжный источник, выпущенная карточка действий, физическое наличие, обучение там, где требуется, и тест. Текущее решение «не разрешено» запрещает считать узел готовым.",
            "",
            "### Низко- и среднерисковые узлы по областям",
            "",
            table(("Область", "Узлов"), ((human_domain(key), value) for key, value in sorted(p0_domain_counts.items(), key=lambda item: (-item[1], item[0])))),
            "",
            tech_table(p0_materializable),
            "",
            f"## C. Профессиональные и справочные темы — {len(p0_restricted)}",
            "",
            f"Эти {len(p0_restricted)} узлов входят в общий счёт {len(p0_technology)} узлов первой необходимости из-за срочности связанной функции, но **не являются бытовой очередью действий** и намеренно не показаны здесь построчно. Их разбор вынесен в связанную панель «Границы безопасности» выше. Срочность никогда не отменяет лицензию, квалификацию, законный объект, контроль или ограничение «только справка».",
        ]
    )
    pages[DASHBOARD_FILES["p0"]] = page(
        "dashboard-p0-first",
        "Первые 72 часа: что делать сначала",
        release_version,
        p0_body,
        "При реальной непосредственной угрозе приоритет имеют выход из опасности и вызов официальных экстренных служб, а не чтение полного каталога.",
    )

    lane_order = ("LAY", "TRAINED", "CLINICIAN", "REFERENCE")
    lanes: Dict[str, List[Mapping[str, str]]] = defaultdict(list)
    for row in health:
        lanes[medical_lane(row)].append(row)
    medicine_sections = [
        "Медицинская страница — каталог охвата, не руководство по лечению. Линия для неспециалиста означает только предполагаемую аудиторию низкорисковой карточки; пока её выпуск не разрешён, это не карточка действий. Линия обученного помощника требует обучения, клиническая линия — лицензированной компетенции, а справочная — только сохранение знаний.",
        "",
        "## Медицинские линии",
        "",
        table(("Линия", "Узлов", "Граница"), [
            (human_medical_lane("LAY"), len(lanes["LAY"]), "только рецензированные короткие карточки в пределах первой помощи"),
            (human_medical_lane("TRAINED"), len(lanes["TRAINED"]), "обучение и регулярная практика"),
            (human_medical_lane("CLINICIAN"), len(lanes["CLINICIAN"]), "законный объект, допуск и оснащение"),
            (human_medical_lane("REFERENCE"), len(lanes["REFERENCE"]), "бытовое исполнение запрещено"),
        ]),
    ]
    for lane in lane_order:
        lane_rows = sorted(lanes[lane], key=priority_key)
        medicine_sections.extend(
            [
                "",
                f"## {human_medical_lane(lane)} — {len(lane_rows)}",
                "",
                tech_table(lane_rows),
            ]
        )
    medicine_sections.extend(
        [
            "",
            f"**Контроль полноты представления:** показано {sum(len(lanes[lane]) for lane in lane_order)} из {len(health)} узлов медицинской помощи и здоровья.",
        ]
    )
    pages[DASHBOARD_FILES["medicine"]] = page(
        "dashboard-medicine",
        f"Медицинская помощь: {len(health)} тем",
        release_version,
        "\n".join(medicine_sections),
        "Не использовать эту страницу для самодиагностики, изменения назначений, инвазивных вмешательств или изготовления лекарств.",
    )

    gap_priority_counts = Counter(row["priority_tier"] for row in gaps)
    gaps_body = "\n".join(
        [
            "Открытая незакрытая работа — это явный запрет считать связанную возможность готовой. Статусы «ответственный не назначен» и «срок не назначен» означают, что работа ещё никому не поручена и не поставлена в календарь.",
            "",
            "## Сводка",
            "",
            table(("Срочность", "Открытых работ"), [(human_priority(p), gap_priority_counts.get(p, 0)) for p in PRIORITY_ORDER]),
            "",
            f"## Все незакрытые работы — {len(gaps)}",
            "",
            table(
                ("Незакрытая работа", "Срочность", "Когда нужна", "Слой", "Область", "Что блокирует", "Нужное доказательство", "Текущее доказательство", "Ответственный", "Срок", "Разрешение"),
                (
                    (
                        atomic_link("known-gap", "GAP", row["gap_id"], human_prose(row["gap_ru"])),
                        human_priority(row["priority_tier"]),
                        human_service(row["earliest_service_level"]),
                        human_scope(row["scope_layer"]),
                        human_domain(row["domain"]),
                        human_prose(row["gap_ru"]),
                        human_prose(row["required_evidence"]),
                        human_prose(row["current_evidence"]),
                        human_common(row["owner"]),
                        human_common(row["due"]),
                        human_gate(row["release_gate"]),
                    )
                    for row in sorted(gaps, key=gap_key)
                ),
            ),
        ]
    )
    pages[DASHBOARD_FILES["gaps"]] = page(
        "dashboard-open-gaps",
        f"Что ещё не готово: {len(gaps)} открытые работы",
        release_version,
        gaps_body,
    )

    services_by_level: Dict[str, List[Mapping[str, str]]] = defaultdict(list)
    for row in services:
        services_by_level[row["service_level"]].append(row)
    service_sections: List[str] = [
        "Уровень автономности — требуемый результат на определённом временном горизонте. Он не достигнут, пока нет измеренной мощности для группы, инвентаря, испытания, ответственного, дублёра и принятого остаточного риска.",
    ]
    for level in sorted(services_by_level, key=lambda value: SERVICE_ORDER.get(value, 99)):
        rows = sorted(services_by_level[level], key=service_key)
        service_sections.extend(
            [
                "",
                f"## {human_service(level)} — {len(rows)} требований",
                "",
                table(
                    ("Требование", "Связанный результат", "Роль", "Минимальный результат", "Группа", "Как считать мощность", "Состояние", "Разрешение"),
                    (
                        (
                            atomic_link("service-level", "SR", row["service_requirement_id"], human_prose(row["minimum_outcome"])),
                            atomic_link("technology", "TEC", row["outcome_node_id"], human_prose(tech_by_id[row["outcome_node_id"]]["title_ru"])),
                            human_role(row["requirement_role"]),
                            row["minimum_outcome"],
                            human_group(row["group_size_scope"]),
                            human_capacity(row["capacity_basis"]),
                            human_common(row["status"]),
                            human_gate(row["release_gate"]),
                        )
                        for row in rows
                    ),
                ),
            ]
        )
    service_sections.extend(
        [
            "",
            f"**Контроль полноты представления:** показано {sum(len(rows) for rows in services_by_level.values())} из {len(services)} требований.",
        ]
    )
    pages[DASHBOARD_FILES["services"]] = page(
        "dashboard-service-levels",
        f"Уровни автономности: {len(services)} требований",
        release_version,
        "\n".join(service_sections),
    )

    payload_rows = []
    for payload in sorted(payloads, key=lambda row: (row["publisher"], row["title"], row["payload_id"])):
        crosswalk = crosswalk_by_payload[payload["payload_id"]]
        relations = "; ".join(
            [
                f"источник: {human_relation(crosswalk['source_relation'])}",
                f"офлайн-пакет: {human_relation(crosswalk['offline_relation'])}",
                f"научный пакет: {human_relation(crosswalk['science_relation'])}",
            ]
        )
        payload_rows.append(
            (
                atomic_link("source-payload", "PAY", payload["payload_id"], payload["title"]),
                payload["title"],
                payload["publisher"],
                human_language(payload["language"]),
                human_media(payload["media_type"]),
                payload["page_count"],
                payload["byte_size"],
                local_payload_link(payload["relative_path"]),
                translated(payload["open_test_state"], OPEN_TEST_LABELS, "Результат открытия требует ручной проверки"),
                translated(payload["rights_review_state"], RIGHTS_LABELS, "Права на использование требуют ручной проверки"),
                translated(payload["operational_use"], OPERATIONAL_LABELS, "Применимость требует ручной проверки"),
                atomic_link("payload-crosswalk", "PXW", crosswalk["payload_crosswalk_id"], f"Связи источника: {payload['title']}"),
                relations,
            )
        )
    offline_body = "\n".join(
        [
            f"На диске зарегистрировано **{len(payloads)}** локальных файлов общим размером **{byte_total} байт** (примерно {byte_total / 1024 / 1024:.2f} МиБ). Фактический файл и его атомарная карточка — не одно и то же, а машинное открытие формата — не предметная рецензия.",
            "",
            "## Форматы",
            "",
            table(("Формат", "Файлов"), ((human_media(key), value) for key, value in sorted(media_counts.items()))),
            "",
            f"## Все локальные файлы и связи — {len(payloads)}",
            "",
            table(
                ("Карточка файла", "Название", "Издатель", "Язык", "Формат", "Страниц", "Байт", "Локальный файл", "Проверка открытия", "Права на использование", "Допустимое применение", "Карточка связей", "Связи"),
                payload_rows,
            ),
            "",
            "## Что ещё не доказано",
            "",
            "- Полное предметное чтение и медицинская/техническая рецензия всех документов.",
            "- Актуальность каждой инструкции для Португалии и конкретного места.",
            "- Право перераспространять каждый материал за пределами личного архива.",
            "- Сквозной запуск Kiwix и открытие сохранённого архива ZIM без сети.",
            "- Превращение материалов в проверенные короткие карточки действий.",
        ]
    )
    pages[DASHBOARD_FILES["offline"]] = page(
        "dashboard-offline-library",
        f"Офлайн-библиотека: {len(payloads)} локальных файлов",
        release_version,
        offline_body,
    )

    domain_rows = []
    for domain in sorted(domain_counts):
        rows = [row for row in technology if row["domain"] == domain]
        priorities = Counter(row["priority_tier"] for row in rows)
        statuses = Counter(row["capability_status"] for row in rows)
        restricted_count = sum(
            row["safety_class"].startswith("S3_") or row["safety_class"].startswith("S4_")
            for row in rows
        )
        domain_rows.append(
            (
                human_domain(domain),
                len(rows),
                priorities.get("P0_RED", 0),
                priorities.get("P1_ORANGE", 0),
                priorities.get("P2_YELLOW", 0),
                priorities.get("P3_GREEN", 0),
                priorities.get("P4_BLUE", 0),
                statuses.get("ARCHITECTURE_ONLY", 0),
                statuses.get("MISSING", 0),
                statuses.get("REFERENCE_ONLY", 0),
                statuses.get("ALLOW", 0),
                restricted_count,
            )
        )
    domains_body = "\n".join(
        [
            "Количество узлов показывает ширину каталога, а не полноту науки или готовность области. Для работы открывайте тематическую панель либо атомарную карточку, а затем проверяйте решение о допуске и доказательства.",
            "",
            f"## Все области — {len(domain_counts)}, всего {len(technology)} узлов",
            "",
            table(
                ("Область", "Всего", "Секунды–72 часа", "3–14 дней", "15–90 дней", "3 месяца–15 лет", "15–100 лет", "Только структура", "Не создано", "Только справка", "Разрешено", "Профессиональные и справочные"),
                domain_rows,
            ),
            "",
            "Тематические срезы медицины, питания и семян, Португалии и ограниченных тем даны в блоке «Что связано» выше.",
        ]
    )
    pages[DASHBOARD_FILES["domains"]] = page(
        "dashboard-technology-domains",
        f"Области знаний и систем: {len(technology)} узлов",
        release_version,
        domains_body,
    )

    seed_body = "\n".join(
        [
            "Эта страница не обещает срок хранения семян. Реальный семенной банк требует реестра каждой партии, исходной всхожести, контролируемых влажности и температуры, периодических тестов, выращивания для обновления, контроля опыления и географически отделённого дубля.",
            "",
            f"## Быстрый семенной контур — {len(seed_focus)} узлов",
            "",
            tech_table(seed_focus),
            "",
            f"## Все темы питания, земледелия и семян — {len(food)}",
            "",
            tech_table(food),
            "",
            "**Контроль полноты представления:** полная таблица выше содержит все узлы области питания, сельского хозяйства и семян; быстрый семенной контур является только поисковым срезом и может требовать ручного уточнения.",
        ]
    )
    pages[DASHBOARD_FILES["food"]] = page(
        "dashboard-seeds-food",
        f"Семена и питание: {len(food)} тем",
        release_version,
        seed_body,
        "Каталог сортов или одна пачка семян не доказывают продовольственную автономность или воспроизводимость следующего урожая.",
    )

    portugal_body = "\n".join(
        [
            "Португальский слой должен храниться отдельно от общего знания. Контакты, право, предупреждения, доступность служб и процедуры имеют дату проверки и могут измениться. Всегда сверяйте с действующими официальными источниками при наличии связи.",
            "",
            f"## Все темы локального слоя Португалии — {len(portugal)}",
            "",
            tech_table(portugal),
            "",
            "## Что требуется для локальной готовности",
            "",
            "- точный адрес и муниципалитет;",
            "- официальные номера, точки помощи и дата проверки;",
            "- три слоя карт: страна/регион, локальные маршруты/службы, объект/коммуникации;",
            "- португальский оригинал и понятный группе перевод;",
            "- отдельная проверка применимости к человеку, зданию и участку.",
        ]
    )
    pages[DASHBOARD_FILES["portugal"]] = page(
        "dashboard-portugal",
        f"Португалия: все {len(portugal)} локальных узлов",
        release_version,
        portugal_body,
    )

    restricted_rows = []
    for row in sorted(restricted, key=priority_key):
        restricted_rows.append(
            (
                human_safety(row["safety_class"]),
                human_priority(row["priority_tier"]),
                human_service(row["earliest_service_level"]),
                human_domain(row["domain"]),
                atomic_link("technology", "TEC", row["node_id"], human_prose(row["title_ru"])),
                human_execution_policy(row["execution_policy"], row["safety_class"]),
                human_capability(row["capability_status"]),
                human_gate(row["release_gate"]),
            )
        )
    safety_body = "\n".join(
        [
            "## Пять уровней ограничений",
            "",
            table(
                ("Граница", "Узлов", "Что разрешено"),
                [
                    (human_safety("S0_OBSERVE_READ"), safety_counts.get("S0_OBSERVE_READ", 0), "наблюдение, чтение и распознавание границ"),
                    (human_safety("S1_LOW_RISK_HOUSEHOLD"), safety_counts.get("S1_LOW_RISK_HOUSEHOLD", 0), "низкорисковая бытовая работа после проверки условий"),
                    (human_safety("S2_TRAINED_SUPERVISED"), safety_counts.get("S2_TRAINED_SUPERVISED", 0), "обучение, надзор, средства индивидуальной защиты и проверенная процедура"),
                    (human_safety("S3_LICENSED_PROFESSIONAL"), safety_counts.get("S3_LICENSED_PROFESSIONAL", 0), "лицензированный специалист, законный объект и контроль"),
                    (human_safety("S4_REFERENCE_ONLY_PROHIBITED_HOUSEHOLD"), safety_counts.get("S4_REFERENCE_ONLY_PROHIBITED_HOUSEHOLD", 0), "только справочное сохранение; бытовое исполнение запрещено"),
                ],
            ),
            "",
            "## Непереходимая граница",
            "",
            "На этой панели нет параметров, пропорций, последовательностей или бытовых рецептов для взрывчатых веществ, пороха, импровизированных топлив, синтеза лекарств, токсичных газов, высокорисковой химии, высокого давления или высокого напряжения. Ссылка на карточку показывает место темы в каталоге, а не разрешение выполнять её.",
            "",
            f"## Все профессиональные и справочные темы — {len(restricted)}",
            "",
            table(
                ("Граница безопасности", "Срочность", "Когда нужна", "Область", "Карточка", "Допустимое исполнение", "Состояние", "Разрешение"),
                restricted_rows,
            ),
        ]
    )
    pages[DASHBOARD_FILES["safety"]] = page(
        "dashboard-safety-boundaries",
        f"Границы безопасности: {len(restricted)} ограниченных тем",
        release_version,
        safety_body,
        "Не переносить профессиональный или справочный материал в бытовую карточку действий и не обходить лицензионные, объектовые или правовые ограничения.",
    )

    inventory_rows = []
    for row in sorted(inventory, key=lambda value: (value["category"], value["item_id"])):
        target = (
            f"{row['target_quantity']} {row['unit']}"
            if row["target_quantity"]
            else f"Не рассчитано; принцип расчёта: {human_inventory_formula(row['quantity_formula'])}"
        )
        actual = (
            f"{row['actual_quantity']} {row['unit']}"
            if row["actual_quantity"]
            else f"Не заполнено ({row['unit']})"
        )
        state = "; ".join(
            [
                f"позиция: {human_common(row['item_status'])}",
                f"оснащение: {human_capability(row['equipment_state'])}",
                f"доказательство: {human_common(row['evidence_type'])}",
                f"ограничение: {human_inventory_limitation(row['evidence_limitations'])}",
            ]
        )
        check = "; ".join(
            [
                f"дата: {row['last_checked'] or 'не проверено'}",
                f"метод: {row['check_method'] or 'не задан'}",
                f"результат: {human_common(row['check_result'])}",
            ]
        )
        next_evidence = (
            "Рассчитать целевое количество по профилю людей и объекта; физически создать или приобрести; "
            "заполнить фактическое количество, место и ответственного; приложить фото, чек или серийный номер, где применимо; "
            "выполнить проверку; записать дату, метод, результат и решение о готовности."
        )
        inventory_rows.append(
            (
                row["item_name_ru"],
                human_inventory_category(row["category"]),
                human_prose(row["purpose"]),
                target,
                actual,
                row["location"] or "Не заполнено",
                human_common(row["owner"]),
                state,
                check,
                human_gate(row["gate_decision"]),
                next_evidence,
            )
        )
    inventory_body = "\n".join(
        [
            f"# ПОДТВЕРЖДЕНО ФИЗИЧЕСКИ: **{inventory_physically_verified}**",
            "",
            "> [!danger] План не равен наличию",
            f"> В реестре {len(inventory)} строк, но все они являются запланированными позициями. Пустое количество, место или владелец нельзя интерпретировать как имеющуюся вещь.",
            "",
            table(
                ("Контроль", "Значение", "Вывод"),
                [
                    ("Подтверждено физически", inventory_physically_verified, "нет достаточной записи о наличии + доказательстве + проверке"),
                    ("Фактическое количество заполнено", inventory_actual_filled, "количество на руках не зафиксировано"),
                    ("Разрешено как проверенное", inventory_allow, "ни одна плановая позиция не разрешена как проверенная"),
                    ("Плановых строк", len(inventory), "это будущая работа, а не имущество"),
                ],
            ),
            "",
            "Полный реестр: [[80_DATA_REGISTERS/inventory-template|полное Markdown-зеркало реестра]]",
            "",
            f"## Все плановые позиции — {len(inventory)}",
            "",
            table(
                ("Предмет", "Категория", "Назначение", "Нужно", "Есть фактически", "Место", "Ответственный", "Состояние", "Проверка", "Разрешение", "Следующее доказательство"),
                inventory_rows,
            ),
            "",
            "Строка может перейти из плана в подтверждённое имущество только после физического осмотра и заполнения фактического количества, места, ответственного, доказательства, результата проверки и пересмотра решения о готовности. Само наличие чека без осмотра и рабочего теста недостаточно.",
        ]
    )
    pages[DASHBOARD_FILES["inventory"]] = page(
        "dashboard-physical-inventory",
        "Физический инвентарь: что у нас реально есть",
        release_version,
        inventory_body,
        "Все пять строк сейчас являются планом. Эта страница намеренно не делает вывод о наличии по целевому количеству, названию или шаблону.",
    )

    if set(pages) != set(EXPECTED_PAGES):
        die(f"page set mismatch: expected={EXPECTED_PAGES} actual={sorted(pages)}")
    validate_generated_pages(pages)

    counts = {
        "files": len(pages),
        "technology": len(technology),
        "p0_technology": len(p0_technology),
        "p0_s0_s2": len(p0_materializable),
        "p0_s3_s4": len(p0_restricted),
        "health": len(health),
        "gaps": len(gaps),
        "p0_gaps": len(p0_gaps),
        "services": len(services),
        "payloads": len(payloads),
        "food_agri": len(food),
        "seed_focus": len(seed_focus),
        "portugal": len(portugal),
        "restricted": len(restricted),
        "bytes": byte_total,
        "inventory_rows": len(inventory),
        "inventory_actual_filled": inventory_actual_filled,
        "inventory_physically_verified": inventory_physically_verified,
        "inventory_allow": inventory_allow,
    }
    return pages, counts


def is_owned_generated_dashboard(path: Path) -> bool:
    if not path.is_file():
        return False
    text = path.read_text(encoding="utf-8")
    return (
        text.startswith("---\n")
        and "kind: dashboard" in text
        and "generated: true" in text
        and "generator: build_obsidian_user_views.py" in text
    )


def write_pages(pages: Mapping[str, str]) -> Tuple[int, int]:
    legacy_paths: List[Path] = []
    if LEGACY_OUT.is_dir():
        for filename in LEGACY_GENERATED_PAGES:
            path = LEGACY_OUT / filename
            if not path.exists():
                continue
            if not is_owned_generated_dashboard(path):
                die(f"refusing to delete non-owned legacy dashboard: {path}")
            legacy_paths.append(path)

    OUT.mkdir(parents=True, exist_ok=True)
    for filename in EXPECTED_PAGES:
        content = pages[filename]
        if not content.startswith("---\n") or "proof_state: CATALOG_VIEW_NOT_OPERATIONAL_PROOF" not in content:
            die(f"unsafe or malformed generated page: {filename}")
        destination = OUT / filename
        if destination.exists() and not is_owned_generated_dashboard(destination):
            die(f"refusing to overwrite non-owned dashboard: {destination}")
        destination.write_text(content, encoding="utf-8")

    for path in legacy_paths:
        path.unlink()

    legacy_dir_removed = 0
    if LEGACY_OUT.is_dir() and not any(LEGACY_OUT.iterdir()):
        LEGACY_OUT.rmdir()
        legacy_dir_removed = 1
    return len(legacy_paths), legacy_dir_removed


def main() -> int:
    try:
        pages, counts = make_pages()
        legacy_files_removed, legacy_dir_removed = write_pages(pages)
    except (OSError, csv.Error, RuntimeError, ValueError) as exc:
        print(f"dashboard_build_error {exc}", file=sys.stderr)
        return 1

    counts["legacy_files_removed"] = legacy_files_removed
    counts["legacy_dir_removed"] = legacy_dir_removed
    print("dashboard_build_ok " + " ".join(f"{key}={value}" for key, value in counts.items()))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
