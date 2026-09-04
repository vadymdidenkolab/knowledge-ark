#!/usr/bin/env python3
"""Expand the central technology graph with catalog-only capability nodes.

The script is deterministic and idempotent.  It does not create instructions,
approve work, or claim that any physical capability exists.  Every added node
starts fail-closed.  S4 nodes remain reference-only.
"""

from __future__ import annotations

import csv
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parent
REGISTER = ROOT / "technology-dependency-register.csv"

S0 = "S0_OBSERVE_READ"
S1 = "S1_LOW_RISK_HOUSEHOLD"
S2 = "S2_TRAINED_SUPERVISED"
S3 = "S3_LICENSED_PROFESSIONAL"
S4 = "S4_REFERENCE_ONLY_PROHIBITED_HOUSEHOLD"

POLICY = {
    S0: "HOUSEHOLD_S0",
    S1: "HOUSEHOLD_S1_AFTER_GATE",
    S2: "TRAINED_SUPERVISED",
    S3: "LICENSED_ONLY",
    S4: "REFERENCE_ONLY_NO_BUILD",
}

ADDITIONS: list[dict[str, str]] = []
BRANCH_CHILDREN: dict[str, list[str]] = {}


def add(
    node_id: str,
    parent_id: str,
    domain: str,
    node_type: str,
    title_ru: str,
    safety: str = S1,
    prerequisites: str = "TD-BASE-SAFETY|TD-BASE-SITE|TD-BASE-INVENTORY",
    outcome: str = "",
    notes: str = "",
) -> None:
    is_reference = safety == S4 or node_type == "HAZARD_BOUNDARY"
    ADDITIONS.append(
        {
            "node_id": node_id,
            "parent_id": parent_id,
            "domain": domain,
            "node_type": node_type,
            "title_ru": title_ru,
            "outcome": outcome or f"Иметь измеримую и проверяемую способность: {title_ru.lower()}",
            "safety_class": safety,
            "execution_policy": POLICY[safety],
            "prerequisite_node_ids": prerequisites,
            "source_package_ids": "",
            "materials_tools_state": "NO_BUILD_MATERIALS" if is_reference else "MISSING",
            "instrument_ids": "",
            "measurement_acceptance": (
                "Граница распознавания и профессиональный маршрут определены; household execution отсутствует"
                if is_reference
                else "До использования задать service level, единицу, объём, срок и критерий приёмки"
            ),
            "calibration_reference": (
                "Official professional references only"
                if is_reference
                else "Точный метод, прибор/reference и неопределённость TBD до исполнения"
            ),
            "drawings_bom_state": "NO_BUILD_DRAWINGS" if is_reference else "MISSING_OR_NOT_APPLICABLE",
            "localization_state": "PORTUGAL_AND_SITE_REVIEW_REQUIRED",
            "waste_storage": "Потоки, совместимость, хранение и законный маршрут TBD до исполнения",
            "stop_conditions": (
                "Неизвестная идентичность; отсутствующее полномочие; опасная среда; непроверенный источник; выход за подготовку"
            ),
            "maintenance_spares": "Периодичность, расходники, запасные части и failure signs TBD",
            "successor_proof": "Другой назначенный участник находит карточку и демонстрирует допустимую часть без устной помощи автора",
            "evidence_required": "Профиль; источник; инвентарь; измерения; acceptance log; reviewer; дата",
            "evidence_state": "BOUNDARY_DEFINED" if is_reference else "MISSING",
            "capability_status": "REFERENCE_ONLY" if is_reference else "MISSING",
            "release_gate": "REFERENCE_ONLY" if is_reference else "DENY",
            "notes": notes or "Каталожный узел; процедуры и рабочие параметры ещё не созданы",
            "release_version": "0.5-draft",
        }
    )


def branch(
    outcome_id: str,
    domain: str,
    title: str,
    children: list[tuple[str, str, str, str]],
    outcome_safety: str = S1,
) -> None:
    child_ids: list[str] = []
    for suffix, child_title, safety, node_type in children:
        child_id = f"{outcome_id}-{suffix}"
        child_ids.append(child_id)
        add(child_id, outcome_id, domain, node_type, child_title, safety)
    add(
        outcome_id,
        "TD-ROOT",
        domain,
        "OUTCOME",
        title,
        outcome_safety,
        "TD-BASE|" + "|".join(child_ids),
        notes="Агрегат: обязательность дочерних узлов определяется technology-dependency-edges.csv",
    )
    BRANCH_CHILDREN[outcome_id] = child_ids


# People, care, composition and human constraints.
branch(
    "TD-PEOPLE",
    "PEOPLE_CARE",
    "Люди; зависимости ухода и пределы группы",
    [
        ("PROFILE", "Профиль каждого человека", S1, "SITE_DATA"),
        ("MEDICAL", "Аллергии; диагнозы; лекарства и медицинские устройства", S2, "SITE_DATA"),
        ("AGE-MASS", "Возраст; масса и возрастные ограничения там; где это необходимо", S2, "SITE_DATA"),
        ("PREGNANCY", "Беременность; новорождённые и репродуктивные потребности", S3, "SITE_DATA"),
        ("CHILD", "Младенцы; дети и зависимые несовершеннолетние", S2, "GOVERNANCE"),
        ("ELDER", "Пожилые люди и возрастная уязвимость", S2, "GOVERNANCE"),
        ("ACCESS", "Инвалидность; мобильность; зрение; слух и когнитивные ограничения", S2, "SITE_DATA"),
        ("LANGUAGE", "Языки; грамотность и доступный формат информации", S1, "SITE_DATA"),
        ("CARE-DEPS", "Caregiver dependencies и объём ухода", S2, "GOVERNANCE"),
        ("ANIMALS", "Домашние и сельскохозяйственные животные в составе", S1, "SITE_DATA"),
        ("CONSENT", "Контакты; согласия; доверенные лица и приватность", S1, "GOVERNANCE"),
        ("CAPACITY", "Физическая и навыковая способность выполнять функции", S2, "TEST"),
        ("SINGLE-POINT", "Одиночный оператор и human single points of failure", S1, "TEST"),
        ("REST", "Сон; смены; усталость и безопасная нагрузка", S1, "PROCESS"),
        ("ABSENCE", "Потеря; болезнь или отсутствие ключевого человека", S2, "GOVERNANCE"),
        ("DEMOGRAPHY", "Демографические пределы и необходимость межгрупповой сети", S0, "KNOWLEDGE"),
    ],
    S2,
)

# Medical capabilities.  These are capability boundaries, not treatment cards.
health_children = [
    ("SCENE-PPE", "Безопасность места происшествия и PPE", S2, "TRAINING"),
    ("CONTACTS", "112; SNS 24; CIAV и структурированный вызов", S1, "PROCESS"),
    ("PRIMARY-ASSESS", "Первичная оценка; наблюдение и передача информации", S2, "TRAINING"),
    ("BLS-AED", "BLS и AED", S2, "TRAINING"),
    ("AIRWAY", "Удушье и острая непроходимость дыхательных путей", S2, "TRAINING"),
    ("BLEED-SHOCK", "Массивное кровотечение и признаки шока", S2, "TRAINING"),
    ("ANAPHYLAXIS", "Анафилаксия и персональные rescue medicines", S3, "TRAINING"),
    ("CHEST-STROKE", "Боль в груди и признаки инсульта", S2, "KNOWLEDGE"),
    ("RESP", "Острая дыхательная проблема; астма и COPD", S3, "TRAINING"),
    ("SEIZURE", "Судороги и изменённое сознание", S2, "TRAINING"),
    ("DIABETES", "Диабетическая неотложная ситуация", S3, "TRAINING"),
    ("BURNS", "Термические и химические ожоги", S2, "TRAINING"),
    ("ELECTRIC", "Электротравма и молния", S2, "TRAINING"),
    ("DROWNING", "Утопление и инцидент в воде", S2, "TRAINING"),
    ("THERMAL-STRESS", "Гипотермия; перегрев и тепловая болезнь", S2, "TRAINING"),
    ("DEHYDRATION", "Обезвоживание; диарея и рвота", S2, "TRAINING"),
    ("POISON", "Отравление; передозировка и токсикологический маршрут", S3, "TRAINING"),
    ("HEAD-SPINE", "Травма головы; шеи и позвоночника", S2, "TRAINING"),
    ("FRACTURE", "Перелом; вывих и повреждение конечности", S2, "TRAINING"),
    ("WOUNDS", "Малые раны; перевязочный цикл и красные флаги", S2, "PROCESS"),
    ("MATERNAL-NEONATAL", "Акушерские и неонатальные красные флаги", S3, "KNOWLEDGE"),
    ("PEDIATRIC", "Педиатрические красные флаги и возрастные ограничения", S3, "KNOWLEDGE"),
    ("MENTAL-CRISIS", "Кризис психического здоровья и непосредственный риск", S2, "TRAINING"),
    ("RECORDS", "Медицинская карта; аллергии; согласия и handover", S1, "GOVERNANCE"),
    ("KIT-INVENTORY", "Физический инвентарь аптечек и расходников", S1, "MATERIAL"),
    ("MEDICATION-INVENTORY", "Инвентаризация назначенных лекарств без изменения назначения", S2, "MATERIAL"),
    ("COLD-CHAIN", "Холодовая цепь лекарств и медпитания", S3, "PROCESS"),
    ("IPC", "Инфекционный контроль; руки; поверхности и вентиляция", S2, "PROCESS"),
    ("MED-WASTE", "Острые и загрязнённые медицинские отходы", S3, "PROCESS"),
    ("DELAYED-CARE", "Поддерживающий уход при задержке профессиональной помощи", S3, "KNOWLEDGE"),
    ("DENTAL", "Профилактическая стоматология и срочная маршрутизация", S2, "PROCESS"),
    ("REHAB", "Мобильность; реабилитация и профилактика повреждения давлением", S3, "PROCESS"),
    ("PALLIATIVE", "Паллиативная поддержка; достоинство и advance plan", S3, "KNOWLEDGE"),
    ("DEATH", "Смерть; записи; санитарные и правовые действия", S4, "HAZARD_BOUNDARY"),
]
health_children += [
    # P0 sub-capabilities and population variants.
    ("LONE-PERSON", "Самопомощь; SOS и check-in для одного человека", S2, "GOVERNANCE"),
    ("GEO-LANGUAGE", "Передача геолокации и языковая экстренная карточка", S1, "PROCESS"),
    ("BLS-ADULT", "BLS/AED для взрослого по очному курсу", S2, "TRAINING"),
    ("BLS-CHILD", "BLS/AED для ребёнка по очному курсу", S2, "TRAINING"),
    ("BLS-INFANT", "BLS для младенца по очному курсу", S2, "TRAINING"),
    ("BLS-PREGNANCY", "Особенности BLS при беременности по очному курсу", S2, "TRAINING"),
    ("BLS-DROWNING", "Реанимация после утопления по очному курсу", S2, "TRAINING"),
    ("AMPUTATION-IMPALED", "Ампутация; открытый перелом и застрявший предмет", S2, "TRAINING"),
    ("TRAUMA-CHEST", "Тяжёлая травма груди", S3, "KNOWLEDGE"),
    ("TRAUMA-ABDOMEN", "Тяжёлая травма живота и таза", S3, "KNOWLEDGE"),
    ("TRAUMA-CRUSH-BLAST", "Crush и blast injury", S3, "KNOWLEDGE"),
    ("MOVE-HANDOVER", "Безопасное перемещение; повторная оценка и handover", S2, "TRAINING"),
    ("BURN-THERMAL", "Термический ожог и красные флаги", S2, "TRAINING"),
    ("BURN-CHEMICAL", "Химический ожог и идентификация продукта", S3, "TRAINING"),
    ("BURN-ELECTRICAL", "Электрический ожог и скрытый риск", S3, "KNOWLEDGE"),
    ("EYE-CHEMICAL", "Химическое поражение глаза", S3, "TRAINING"),
    ("SMOKE-CO", "Дым; CO и ингаляционное поражение", S2, "KNOWLEDGE"),
    ("FROSTBITE", "Переохлаждение и обморожение", S2, "TRAINING"),
    ("SYNCOPE", "Обморок и внезапная слабость", S2, "KNOWLEDGE"),
    ("ACUTE-ABDOMEN", "Острая боль в животе и красные флаги", S3, "KNOWLEDGE"),
    ("HEADACHE", "Тяжёлая внезапная головная боль и красные флаги", S3, "KNOWLEDGE"),
    ("URINARY", "Острая задержка мочи и срочная маршрутизация", S3, "KNOWLEDGE"),
    ("FEVER", "Лихорадка с опасными признаками", S2, "KNOWLEDGE"),
    ("BITES-STINGS", "Укусы; ужаления и аллергический риск", S2, "KNOWLEDGE"),
    ("SNAKE-MARINE", "Змеи и морские животные: запрет импровизации и маршрут", S3, "KNOWLEDGE"),
    ("RABIES-TETANUS", "Риск бешенства и столбняка; история вакцинации и referral", S3, "KNOWLEDGE"),
    ("OB-BLEED", "Кровотечение при беременности", S3, "KNOWLEDGE"),
    ("OB-ECTOPIC", "Признаки возможной внематочной беременности", S3, "KNOWLEDGE"),
    ("OB-PREECLAMPSIA", "Признаки преэклампсии и эклампсии", S3, "KNOWLEDGE"),
    ("OB-BIRTH", "Роды до прибытия профессиональной помощи", S4, "HAZARD_BOUNDARY"),
    ("OB-POSTPARTUM-BLEED", "Послеродовое кровотечение", S3, "KNOWLEDGE"),
    ("NEWBORN", "Опасные признаки у новорождённого", S3, "KNOWLEDGE"),
    ("SEXUAL-VIOLENCE", "Сексуальное насилие; согласие; safeguarding и конфиденциальная помощь", S3, "GOVERNANCE"),
    ("MH-SUICIDE", "Суицидальный риск и непосредственная безопасность", S3, "TRAINING"),
    ("MH-PSYCHOSIS", "Психоз и безопасная маршрутизация", S3, "KNOWLEDGE"),
    ("MH-AGITATION", "Тяжёлое возбуждение и безопасность помощника", S3, "TRAINING"),
    ("MH-WITHDRAWAL", "Опасная отмена алкоголя или веществ", S3, "KNOWLEDGE"),
    ("DEVICE-OXYGEN-CPAP", "Потеря кислорода; CPAP или респираторного устройства", S3, "SITE_DATA"),
    ("DEVICE-DIALYSIS", "Потеря диализа или почечной поддержки", S3, "SITE_DATA"),
    ("DEVICE-TUBE-FEED", "Потеря зондового питания или медпитания", S3, "SITE_DATA"),
    ("ISOLATION-IMMEDIATE", "Немедленная изоляция симптомного человека", S2, "PROCESS"),
    ("CONTACT-LOG", "Первичный журнал контактов с защитой приватности", S2, "GOVERNANCE"),
    ("EVAC-ACCESS", "Медицинская эвакуация маломобильного; ребёнка или зависимого человека", S3, "PROCESS"),
    ("TEAM-ROLES", "Командные роли N2–N7 при неотложной помощи", S2, "GOVERNANCE"),
    ("CASUALTY-CAPACITY", "Мощность ухода и порог перегрузки группы", S2, "TEST"),
    # P1 continuity modules.
    ("CARE-NURSING", "Базовый caregiver/nursing support в пределах подготовки", S3, "TRAINING"),
    ("CARE-SWALLOW", "Безопасное питание; глотание и риск аспирации", S3, "KNOWLEDGE"),
    ("CONT-CARDIO", "Непрерывность сердечно-сосудистого лечения", S3, "SITE_DATA"),
    ("CONT-DIABETES", "Непрерывность лечения диабета", S3, "SITE_DATA"),
    ("CONT-RESP", "Непрерывность лечения астмы и COPD", S3, "SITE_DATA"),
    ("CONT-EPILEPSY", "Непрерывность лечения эпилепсии", S3, "SITE_DATA"),
    ("CONT-ENDOCRINE", "Щитовидная и надпочечниковая недостаточность", S3, "SITE_DATA"),
    ("CONT-ANTICOAG", "Антикоагуляция и person-specific plan", S3, "SITE_DATA"),
    ("CONT-PSYCH", "Психиатрические лекарства и опасность внезапной отмены", S3, "SITE_DATA"),
    ("CONT-RENAL", "Почечная недостаточность и диализ", S3, "SITE_DATA"),
    ("CONT-ONCOLOGY", "Онкологическое лечение и иммуносупрессия", S3, "SITE_DATA"),
    ("CONT-TRANSPLANT", "Трансплантация и иммуносупрессия", S3, "SITE_DATA"),
    ("CONT-HIV-TB", "HIV/TB и непрерывность лечения", S3, "SITE_DATA"),
    ("CONT-AUTOIMMUNE", "Аутоиммунные заболевания", S3, "SITE_DATA"),
    ("CONT-HEMOPHILIA", "Нарушения свёртывания и гемофилия", S3, "SITE_DATA"),
    ("CONT-PAIN", "Хроническая боль и законный персональный план", S3, "SITE_DATA"),
    ("CONT-STOMA-CATH", "Стома; катетер и расходники", S3, "SITE_DATA"),
    ("ASSISTIVE", "Очки; слуховые аппараты; кресла; ходунки и протезы", S2, "MATERIAL"),
    ("POSTPARTUM", "Послеродовой уход и грудное вскармливание", S3, "KNOWLEDGE"),
    ("REPRODUCTIVE", "Добровольное репродуктивное планирование и STI-маршрут", S3, "KNOWLEDGE"),
    ("SKIN-EYE-EAR", "Повседневные кожные; глазные и слуховые проблемы с красными флагами", S3, "KNOWLEDGE"),
    ("GRIEF-CAREGIVER", "Горе; нагрузка caregiver и психологическая поддержка", S2, "PROCESS"),
    ("CARE-HANDOVER", "Смена caregiver и журнал наблюдения", S2, "GOVERNANCE"),
    # P2 preparedness, supply and public health.
    ("PREVENT-VACCINE", "Профилактика и вакцинация по персональному плану", S3, "GOVERNANCE"),
    ("CHILD-GROWTH", "Рост; питание и функциональное состояние детей", S3, "TEST"),
    ("FALLS-DECONDITION", "Профилактика падений и декондиционирования", S2, "PROCESS"),
    ("OCC-HEALTH", "Шум; пыль; химикаты; вибрация; тепло и усталость", S3, "SITE_DATA"),
    ("VECTOR", "Переносчики и environmental health", S3, "PROCESS"),
    ("SURVEILLANCE", "Синдромный журнал группы и outbreak reporting", S3, "GOVERNANCE"),
    ("ISOLATION-ROOM", "Изоляционное помещение; вентиляция и потоки", S3, "DRAWING"),
    ("SUPPLY-REGISTER", "Медицинский supply register; минимум; расход; срок и fallback", S2, "GOVERNANCE"),
    ("DEVICE-QC", "Контроль; отказ и вывод медицинских приборов", S3, "TEST"),
    ("AED-LIFECYCLE", "AED; батареи; электроды; осмотр и тренажёр", S2, "MAINTENANCE"),
    ("SKILL-MATRIX", "Матрица first-aid/caregiver навыков и currency", S2, "GOVERNANCE"),
    ("REFERRAL-NET", "Сеть врача; аптеки; стоматолога; роддома; лаборатории и транспорта", S2, "SITE_DATA"),
    ("CARE-ROOM", "Помещение ухода: вода; санитария; свет; тепло; энергия и приватность", S3, "DRAWING"),
    # P3/P4 professional and institutional shelves.
    ("PROF-ANATOMY", "Профессиональная анатомия; физиология и патология", S3, "KNOWLEDGE"),
    ("PROF-EMERGENCY", "Emergency и critical care", S4, "HAZARD_BOUNDARY"),
    ("PROF-PRIMARY", "Primary и community medicine", S3, "KNOWLEDGE"),
    ("PROF-NURSING", "Сестринское дело и long-term care", S3, "KNOWLEDGE"),
    ("PROF-PHARMACY", "Фармация; medication safety и lawful formulary", S3, "KNOWLEDGE"),
    ("PROF-INTERNAL", "Внутренняя медицина и NCD", S3, "KNOWLEDGE"),
    ("PROF-INFECTIOUS", "Инфекционные болезни; IPC и antimicrobial stewardship", S3, "KNOWLEDGE"),
    ("PROF-OB", "Акушерство; midwifery и гинекология", S4, "HAZARD_BOUNDARY"),
    ("PROF-PEDIATRICS", "Неонатология и педиатрия", S3, "KNOWLEDGE"),
    ("PROF-GERIATRICS", "Гериатрия", S3, "KNOWLEDGE"),
    ("PROF-MENTAL", "Психиатрия и substance-use care", S3, "KNOWLEDGE"),
    ("PROF-REHAB", "Реабилитация и assistive technology", S3, "KNOWLEDGE"),
    ("PROF-PALLIATIVE", "Паллиативная помощь и конец жизни", S3, "KNOWLEDGE"),
    ("PROF-DENTISTRY", "Стоматология", S4, "HAZARD_BOUNDARY"),
    ("PROF-OPHTH-ENT", "Офтальмология; ЛОР и аудиология", S3, "KNOWLEDGE"),
    ("PROF-DERM", "Дерматология", S3, "KNOWLEDGE"),
    ("PROF-NUTRITION", "Клиническое питание; malnutrition и refeeding", S3, "KNOWLEDGE"),
    ("PROF-TOX", "Клиническая токсикология", S4, "HAZARD_BOUNDARY"),
    ("PROF-SURGERY", "Хирургия; анестезия и trauma surgery", S4, "HAZARD_BOUNDARY"),
    ("PROF-BLOOD", "Кровь; совместимость и трансфузия", S4, "HAZARD_BOUNDARY"),
    ("PROF-LAB", "Лабораторная медицина; samples и quality control", S4, "HAZARD_BOUNDARY"),
    ("PROF-IMAGING", "УЗИ; рентген и медицинская визуализация", S4, "HAZARD_BOUNDARY"),
    ("PROF-OXYGEN", "Медицинский кислород и respiratory equipment", S4, "HAZARD_BOUNDARY"),
    ("PROF-BIOMED", "Biomedical engineering; сервис и вывод приборов", S3, "KNOWLEDGE"),
    ("PROF-STERILE", "Стерилизация и healthcare facility IPC", S4, "HAZARD_BOUNDARY"),
    ("PROF-CLINIC", "Clinic design; triage flow; registry; referral и transport", S3, "KNOWLEDGE"),
    ("PROF-SUPPLY", "Medical supply chain; anti-counterfeit и recalls", S3, "KNOWLEDGE"),
    ("PROF-RECORDS", "Health records; privacy; backup и patient matching", S3, "KNOWLEDGE"),
    ("PROF-EPIDEMIOLOGY", "Эпидемиология; surveillance и outbreak management", S3, "KNOWLEDGE"),
    ("PROF-ENVIRONMENT", "Environmental и climate health", S3, "KNOWLEDGE"),
    ("PROF-OCCUPATIONAL", "Профессиональная медицина", S3, "KNOWLEDGE"),
    ("PROF-ONE-HEALTH", "Ветеринарная медицина и One Health", S3, "KNOWLEDGE"),
    ("PROF-ETHICS", "Медицинская этика; согласие; capacity; safeguarding и rationing", S3, "KNOWLEDGE"),
    ("PROF-PORTUGAL", "SNS; INEM; DGS; INFARMED и португальский medical overlay", S3, "KNOWLEDGE"),
    ("P4-EDUCATION", "Профессиональная медицинская образовательная линия", S4, "HAZARD_BOUNDARY"),
    ("P4-SUCCESSION", "Преемственность врачебных; nursing; pharmacy и public-health ролей", S4, "HAZARD_BOUNDARY"),
    ("P4-QA-PEER", "Peer review; incident и morbidity/mortality review", S4, "HAZARD_BOUNDARY"),
    ("P4-GUIDELINE", "Guideline governance; evidence synthesis и pharmacovigilance", S4, "HAZARD_BOUNDARY"),
    ("P4-INSTITUTION", "Преемственность клиники; аптеки; лаборатории и referral network", S4, "HAZARD_BOUNDARY"),
    ("P4-PUBLIC-RECORDS", "Public-health records; демография и outbreak history", S3, "KNOWLEDGE"),
    ("P4-GMP-PHARMA", "GMP и регулируемое производство лекарств", S4, "HAZARD_BOUNDARY"),
    ("P4-VACCINE", "Производство вакцин и biological safety", S4, "HAZARD_BOUNDARY"),
    ("P4-DEVICE-MAKE", "Регулируемое производство медицинских изделий", S4, "HAZARD_BOUNDARY"),
    ("P4-RESEARCH", "Clinical research и trials governance", S4, "HAZARD_BOUNDARY"),
    ("P4-GENETICS", "Генетика; counselling; этика и privacy", S4, "HAZARD_BOUNDARY"),
    ("P4-LEGACY", "Устаревшие медицинские методы вне оперативного поиска", S0, "KNOWLEDGE"),
]
for suffix, title, safety, node_type in health_children:
    add(f"TD-HEALTH-{suffix}", "TD-HEALTH", "HEALTH", node_type, title, safety)
BRANCH_CHILDREN["TD-HEALTH"] = [f"TD-HEALTH-{item[0]}" for item in health_children]

# Water supply from immediate stock to diversified long-term sources.
water_children = [
    ("P0-RESERVE", "Закрытый запас питьевой воды на первые 72 часа", S1, "MATERIAL"),
    ("DEMAND", "Расчёт потребности 1–7 человек и животных", S1, "TEST"),
    ("RATION", "Выдача; учёт и приоритеты воды", S1, "GOVERNANCE"),
    ("VULNERABLE", "Вода для лекарств; младенцев и уязвимых людей", S2, "SITE_DATA"),
    ("COLLECTION", "Законный сбор воды", S2, "PROCESS"),
    ("CARRY", "Ручная переноска без травмы и загрязнения", S1, "PROCESS"),
    ("CROSS-CONTAM", "Предотвращение перекрёстного загрязнения", S2, "PROCESS"),
    ("LABEL", "Разделение и маркировка питьевой и технической воды", S1, "PROCESS"),
    ("EMERGENCY-PRODUCT", "Аварийная обработка точным готовым продуктом по официальной инструкции", S2, "PROCESS"),
    ("CONTAINER-CLEAN", "Очистка; ротация и браковка ёмкостей", S2, "MAINTENANCE"),
    ("PORTFOLIO", "Портфель независимых источников воды", S1, "OUTCOME"),
    ("RAIN", "Дождевая вода; право; first flush и отдельный risk profile", S2, "PROCESS"),
    ("DELIVERED", "Привозная вода и приёмка партии", S1, "PROCESS"),
    ("WELL", "Колодец или скважина; строительство и эксплуатация", S3, "PROCESS"),
    ("SURFACE", "Поверхностная вода как высокорисковый источник", S3, "PROCESS"),
    ("GRAVITY", "Гравитационная подача", S2, "PROCESS"),
    ("HAND-PUMP", "Ручной насос и его ремонт", S2, "TOOL"),
    ("LOWE-PUMP", "Низкоэнергетический насос и резерв питания", S2, "PROCESS"),
    ("DISTRIBUTION", "Распределение воды и точки отбора", S2, "DRAWING"),
    ("BACKFLOW", "Защита от обратного потока", S3, "PROCESS"),
    ("LEAK", "Испытание на утечки и потери", S2, "TEST"),
    ("SPARES", "Запас фитингов; уплотнений и ремонтных деталей", S1, "MAINTENANCE"),
    ("LAB", "Маршрут лабораторного анализа воды", S3, "PROCESS"),
    ("REDUNDANCY", "Отказ одного источника и независимый резерв", S2, "TEST"),
]
for suffix, title, safety, node_type in water_children:
    add(f"TD-WATER-{suffix}", "TD-WATER", "WATER_WASH", node_type, title, safety)
BRANCH_CHILDREN["TD-WATER"] = [f"TD-WATER-{item[0]}" for item in water_children]

# Sanitation and all waste streams.
sanitation_children = [
    ("TOILET", "Аварийный туалет и пропускная способность", S2, "PROCESS"),
    ("HANDWASH", "Станция мытья рук", S1, "PROCESS"),
    ("ZONING", "Чистая и грязная зоны", S2, "DRAWING"),
    ("SOAP", "Мыло; расходники и ротация", S1, "MATERIAL"),
    ("MENSTRUAL", "Менструальная гигиена", S1, "MATERIAL"),
    ("DIAPERS", "Подгузники и детские санитарные потребности", S1, "MATERIAL"),
    ("INCONTINENCE", "Недержание и caregiver hygiene", S2, "PROCESS"),
    ("BATHING", "Безопасное купание и личная гигиена", S1, "PROCESS"),
    ("LAUNDRY", "Стирка; сушка и разделение загрязнённого белья", S2, "PROCESS"),
    ("BLACKWATER", "Чёрные стоки и фекальные загрязнения", S4, "HAZARD_BOUNDARY"),
    ("GREYWATER", "Серые воды и законный сброс/повторное использование", S3, "PROCESS"),
    ("HOUSEHOLD-WASTE", "Твёрдые бытовые отходы", S1, "PROCESS"),
    ("FOOD-WASTE", "Пищевые отходы", S2, "PROCESS"),
    ("HAZARDOUS-WASTE", "Опасные химические отходы", S4, "HAZARD_BOUNDARY"),
    ("BATTERIES", "Отработанные батареи и аккумуляторы", S3, "PROCESS"),
    ("OILS", "Отработанные масла и топливо", S3, "PROCESS"),
    ("SHARPS", "Острые предметы", S3, "PROCESS"),
    ("MEDICAL", "Загрязнённые медицинские материалы", S3, "PROCESS"),
    ("ANIMAL", "Отходы животных", S3, "PROCESS"),
    ("CONSTRUCTION", "Строительные отходы и опасные материалы", S3, "PROCESS"),
    ("DEAD-ANIMAL", "Павшие животные", S4, "HAZARD_BOUNDARY"),
    ("HUMAN-DEATH", "Санитарная и правовая маршрутизация смерти человека", S4, "HAZARD_BOUNDARY"),
    ("PESTS", "Вредители и переносчики", S2, "PROCESS"),
]
for suffix, title, safety, node_type in sanitation_children:
    add(f"TD-SAN-{suffix}", "TD-SANITATION", "WATER_WASH", node_type, title, safety)
BRANCH_CHILDREN["TD-SANITATION"] = [f"TD-SAN-{item[0]}" for item in sanitation_children]

# Immediate food resilience.
food_immediate = [
    ("P0-RESERVE", "Пищевой запас на первые 72 часа", S1, "MATERIAL"),
    ("P1-PANTRY", "Ротационная кладовая на 14 дней", S1, "MATERIAL"),
    ("NO-COOK", "Пища без готовки при потере энергии", S1, "MATERIAL"),
    ("MENU", "Фактическое меню и порции для состава группы", S1, "TEST"),
    ("ALLERGENS", "Аллергены и перекрёстный контакт", S2, "PROCESS"),
    ("SPECIAL-DIET", "Лечебные; возрастные и религиозные диеты", S2, "SITE_DATA"),
    ("INFANT", "Безопасное питание младенцев", S3, "PROCESS"),
    ("COOK-WATER", "Питьевая вода для приготовления пищи", S1, "MATERIAL"),
    ("HAND-TOOLS", "Ручной открыватель; посуда и базовые кухонные инструменты", S1, "TOOL"),
    ("COOK-SAFETY", "Пожар; CO; вентиляция и пищевая безопасность при готовке", S2, "PROCESS"),
    ("COOK-FUEL", "Измеренный расход топлива для готовки", S2, "TEST"),
    ("PEST", "Защита запасов от вредителей", S2, "PROCESS"),
    ("WASTE", "Пищевые отходы без загрязнения воды и хранилища", S2, "PROCESS"),
    ("ROTATION", "FEFO; сроки; осмотр и пополнение", S1, "MAINTENANCE"),
    ("RATION", "Распределение пищи и журнал дефицита", S1, "GOVERNANCE"),
]
for suffix, title, safety, node_type in food_immediate:
    add(f"TD-FOOD-{suffix}", "TD-FOOD", "FOOD_AGRI", node_type, title, safety)

# Agriculture and reproducible seed cycles.
agri_children = [
    ("LAND-RIGHTS", "Право пользования землёй и водой", S0, "GOVERNANCE"),
    ("TOPO", "Топография; уклоны и зоны стока участка", S2, "SITE_DATA"),
    ("SOIL-MAP", "Карта почв и неоднородности", S1, "SITE_DATA"),
    ("SOIL-TEST", "Анализ почвы и корректная интерпретация", S2, "TEST"),
    ("SOIL-OM", "Органическое вещество и структура почвы", S1, "TEST"),
    ("SOIL-PH", "pH почвы", S2, "TEST"),
    ("SOIL-SALINITY", "Солёность и электропроводность почвы", S2, "TEST"),
    ("IRRIGATION-BUDGET", "Водный бюджет орошения", S2, "TEST"),
    ("MICROCLIMATE", "Микроклимат; мороз; жара; ветер и экспозиция", S1, "SITE_DATA"),
    ("PT-CALENDAR", "Календарь культур для конкретной зоны Португалии", S1, "KNOWLEDGE"),
    ("NURSERY", "Питомник и рассада", S2, "PROCESS"),
    ("GREENHOUSE", "Теплица; вентиляция и перегрев", S2, "PROCESS"),
    ("IRRIGATION", "Орошение и обслуживание", S2, "PROCESS"),
    ("IRRIGATION-UNIFORM", "Равномерность полива", S2, "TEST"),
    ("DRAINAGE", "Дренаж; эрозия и заболачивание", S2, "PROCESS"),
    ("STAPLES", "Калорийные основные культуры", S2, "PROCESS"),
    ("LEGUMES", "Бобовые и пищевой белок", S2, "PROCESS"),
    ("OILSEEDS", "Масличные культуры", S2, "PROCESS"),
    ("VEGETABLES", "Овощные культуры и нутриентное разнообразие", S2, "PROCESS"),
    ("PERENNIALS", "Многолетние плодовые и орехоплодные", S2, "PROCESS"),
    ("CLONAL", "Клоновые культуры и санитарный посадочный материал", S3, "PROCESS"),
    ("POTATO", "Посадочный картофель", S2, "MATERIAL"),
    ("GARLIC", "Посадочный чеснок", S2, "MATERIAL"),
    ("SWEET-POTATO", "Батат и вегетативное размножение", S2, "MATERIAL"),
    ("VARIETY-STATUS", "OP; landrace; F1 hybrid и правовой статус сорта", S1, "SITE_DATA"),
    ("TWO-LOTS", "Два независимых лота критических культур", S1, "MATERIAL"),
    ("OFFSITE", "Географически разнесённая копия семенного фонда", S1, "MATERIAL"),
    ("SEED-STORAGE", "Температура; влажность; упаковка и мониторинг семян", S2, "PROCESS"),
    ("RESEED", "Резерв пересева после отказа", S1, "MATERIAL"),
    ("ISOLATION", "Видоспецифическая изоляция при семеноводстве", S2, "PROCESS"),
    ("POPULATION", "Размер репродуктивной популяции", S2, "TEST"),
    ("POLLINATION", "Опыление и управление опылителями", S2, "PROCESS"),
    ("PURITY", "Сортовая идентичность и чистота", S2, "TEST"),
    ("QUARANTINE", "Карантин болезней и неизвестного посадочного материала", S3, "PROCESS"),
    ("IPM", "Интегрированная защита растений", S2, "PROCESS"),
    ("THRESH", "Обмолот и отделение семян", S2, "PROCESS"),
    ("CLEAN", "Очистка семян и урожая", S2, "PROCESS"),
    ("DRY", "Сушка урожая и семян", S2, "PROCESS"),
    ("LOSS", "Измерение потерь при хранении", S1, "TEST"),
    ("CROP-FAIL", "Резерв при неурожае и повторный сезон", S2, "GOVERNANCE"),
]
for suffix, title, safety, node_type in agri_children:
    add(f"TD-AGRI-{suffix}", "TD-FOOD", "FOOD_AGRI", node_type, title, safety)
BRANCH_CHILDREN["TD-FOOD"] = (
    [f"TD-FOOD-{item[0]}" for item in food_immediate]
    + [f"TD-AGRI-{item[0]}" for item in agri_children]
    + ["TD-FERTILIZERS"]
)

# Fertility details missing from the original fertilizer aggregate.
fert_children = [
    ("CROP-REMOVAL", "Вынос питательных веществ урожаем", S2, "TEST"),
    ("LEGUMES", "Бобовые; покровные культуры и сидераты", S2, "PROCESS"),
    ("RESIDUES", "Возврат известных растительных остатков", S2, "PROCESS"),
    ("LABELED", "Готовые маркированные удобрения по анализу и этикетке", S2, "MATERIAL"),
    ("MICRONUTRIENTS", "Микроэлементы и риск передозировки", S3, "PROCESS"),
    ("RUNOFF", "Сток; вымывание и защита воды", S2, "TEST"),
    ("TRACEABILITY", "Партия; состав; применение и результат", S1, "GOVERNANCE"),
]
for suffix, title, safety, node_type in fert_children:
    add(f"TD-FERT-{suffix}", "TD-FERTILIZERS", "FOOD_AGRI", node_type, title, safety)
BRANCH_CHILDREN["TD-FERTILIZERS"] = [f"TD-FERT-{item[0]}" for item in fert_children]

# Animal systems are conditional and modular.
branch(
    "TD-ANIMALS",
    "ANIMALS",
    "Животные; корма; welfare и ветеринарная непрерывность",
    [
        ("WELFARE", "Welfare; ежедневное наблюдение и stop-критерии", S2, "PROCESS"),
        ("WATER", "Вода для животных", S2, "PROCESS"),
        ("FEED", "Корма; питание и запас", S2, "MATERIAL"),
        ("PASTURE", "Пастбище и carrying capacity", S2, "SITE_DATA"),
        ("SHELTER", "Укрытие; температура и вентиляция", S2, "PROCESS"),
        ("BIOSECURITY", "Биобезопасность; карантин и zoonoses", S3, "PROCESS"),
        ("BREEDING", "Размножение и генетическое разнообразие", S3, "PROCESS"),
        ("VET", "Ветеринарная помощь и лекарства", S3, "KNOWLEDGE"),
        ("WASTE", "Навоз; подстилка и защита воды", S3, "PROCESS"),
        ("EGGS", "Яйца; сбор и пищевая безопасность", S2, "PROCESS"),
        ("MILK", "Молоко; гигиена и холодовая цепь", S3, "PROCESS"),
        ("SLAUGHTER", "Убой; ветеринарный контроль и пищевая безопасность", S4, "HAZARD_BOUNDARY"),
        ("BEES", "Пчёлы; опыление и продукты пчеловодства", S3, "PROCESS"),
        ("AQUACULTURE", "Аквакультура и качество воды", S3, "PROCESS"),
        ("HANDLER", "Дублёр handler и безопасное обращение", S2, "TRAINING"),
    ],
    S2,
)

# Immediate shelter and safe occupancy.
shelter_children = [
    ("SHELTER-IN-PLACE", "Shelter-in-place и критерии эвакуации", S2, "PROCESS"),
    ("SAFE-ZONE", "Безопасная внутренняя зона", S2, "SITE_DATA"),
    ("ACCESSIBLE-EXIT", "Доступный путь выхода", S2, "DRAWING"),
    ("SHUTOFF-WATER", "Штатное отключение воды", S2, "TRAINING"),
    ("SHUTOFF-GAS", "Штатное отключение газа квалифицированным способом", S3, "TRAINING"),
    ("SHUTOFF-ELECTRIC", "Штатное отключение электричества без работ в щите", S2, "TRAINING"),
    ("ALARMS", "Дымовые и CO извещатели; питание и тест", S1, "MAINTENANCE"),
    ("EXTINGUISHER", "Сертифицированный огнетушитель и предел применения", S2, "TRAINING"),
    ("FIRE-BLANKET", "Пожарное покрывало и размещение", S2, "TOOL"),
    ("DARK-EXIT", "Тренировка выхода в темноте", S2, "TEST"),
    ("COLLAPSE", "Признаки риска обрушения и запрет входа", S4, "HAZARD_BOUNDARY"),
    ("HEAT-ZONE", "Безопасная прохладная зона при жаре", S1, "PROCESS"),
    ("COLD-ZONE", "Безопасная тёплая зона при холоде", S2, "PROCESS"),
    ("COMBUSTION-AIR", "Вентиляция при готовке и отоплении", S3, "PROCESS"),
    ("LIGHT", "Аварийное освещение путей выхода", S1, "MATERIAL"),
    ("DEPENDENTS", "Выход и укрытие для маломобильных людей; детей и животных", S2, "DRAWING"),
    ("KITCHEN", "Кухонная санитария и безопасное хранение", S2, "PROCESS"),
    ("PESTS", "Вредители; точки входа и безопасный контроль", S2, "PROCESS"),
]
for suffix, title, safety, node_type in shelter_children:
    add(f"TD-SHELTER-{suffix}", "TD-SHELTER", "SHELTER", node_type, title, safety)
BRANCH_CHILDREN["TD-SHELTER"] = [f"TD-SHELTER-{item[0]}" for item in shelter_children]

# Construction remains a separate long-horizon branch.
branch(
    "TD-CONSTRUCTION",
    "CONSTRUCTION",
    "Строительство; обследование и as-built обслуживание",
    [
        ("SITE", "Обследование площадки; геология и склон", S3, "SITE_DATA"),
        ("EARTHWORKS", "Земляные работы и устойчивость выемок", S4, "HAZARD_BOUNDARY"),
        ("FOUNDATION", "Фундаменты", S4, "HAZARD_BOUNDARY"),
        ("FRAME", "Несущий каркас", S4, "HAZARD_BOUNDARY"),
        ("WALLS", "Стены и ненесущие ремонтные работы", S3, "PROCESS"),
        ("FLOORS", "Перекрытия и полы", S3, "PROCESS"),
        ("ROOF", "Крыша; высота и временная погодозащита", S4, "HAZARD_BOUNDARY"),
        ("WEATHER", "Ветрозащита и водозащитная оболочка", S3, "PROCESS"),
        ("WINDOWS", "Окна; остекление и временное закрытие", S3, "PROCESS"),
        ("DOORS", "Двери; выход и доступность", S3, "PROCESS"),
        ("INSULATION", "Теплоизоляция и безопасные материалы", S3, "PROCESS"),
        ("MOISTURE", "Влага; плесень и контроль источника", S3, "PROCESS"),
        ("PLUMBING", "Сантехника; давление и обратный поток", S3, "PROCESS"),
        ("SANITATION", "Канализация; septic и санитарные разрывы", S4, "HAZARD_BOUNDARY"),
        ("ELECTRICAL", "Стационарная электрика 230 V", S4, "HAZARD_BOUNDARY"),
        ("VENTILATION", "Расчёт и обслуживание вентиляции", S3, "PROCESS"),
        ("HVAC", "Отопление и охлаждение здания", S3, "PROCESS"),
        ("FIRE", "Пожарные преграды и безопасная эвакуация", S4, "HAZARD_BOUNDARY"),
        ("SEISMIC", "Сейсмическая оценка", S4, "HAZARD_BOUNDARY"),
        ("WIND", "Ветровая устойчивость", S4, "HAZARD_BOUNDARY"),
        ("FLOOD", "Наводнение; отметки и водоустойчивость", S3, "SITE_DATA"),
        ("WILDFIRE", "Wildfire interface и defensible space", S3, "PROCESS"),
        ("ACCESS", "Доступность и универсальный дизайн", S3, "DRAWING"),
        ("TEMP", "Временные сооружения и пределы нагрузки", S3, "PROCESS"),
        ("PERMITS", "Разрешения; PDM и профессиональные подписи", S0, "GOVERNANCE"),
        ("INSPECTION", "Инспекция; дефекты и запрет эксплуатации", S3, "TEST"),
        ("AS-BUILT", "As-built чертежи; скрытые сети и ревизии", S2, "DRAWING"),
    ],
    S3,
)

# Critical energy is split by service rather than by an imagined power plant.
energy_children = [
    ("LIGHT", "Критическое освещение", S1, "OUTCOME"),
    ("COMMS", "Заряд и питание связи", S1, "OUTCOME"),
    ("MEDICAL", "Питание медицинских устройств", S2, "OUTCOME"),
    ("COLD-CHAIN", "Энергия для холодовой цепи", S2, "OUTCOME"),
    ("LOAD-SHED", "Приоритетное отключение нагрузок", S2, "GOVERNANCE"),
    ("FLASHLIGHT", "Автономные фонари и запас питания", S1, "MATERIAL"),
    ("BATTERY-STANDARD", "Стандартные батарейные платформы", S2, "MATERIAL"),
    ("POWERBANK", "Сертифицированные power banks", S2, "MATERIAL"),
    ("SOURCE", "Сертифицированный автономный источник", S2, "MATERIAL"),
    ("CHARGE", "Безопасная зарядка; кабели и совместимость", S2, "PROCESS"),
    ("FAILURE", "Отказ; изоляция и восстановление критических нагрузок", S2, "TEST"),
    ("SPARES", "Предохранители; кабели; адаптеры и запасные части", S2, "MAINTENANCE"),
]
for suffix, title, safety, node_type in energy_children:
    add(f"TD-ENERGY-{suffix}", "TD-ENERGY", "ENERGY", node_type, title, safety)
BRANCH_CHILDREN["TD-ENERGY"] = [f"TD-ENERGY-{item[0]}" for item in energy_children]

# Fuels: safe product lifecycle separated from professional production.
fuel_children = [
    ("USE-COOK", "Топливо для готовки и измеренный расход", S2, "PROCESS"),
    ("USE-HEAT", "Топливо для тепла и измеренный расход", S3, "PROCESS"),
    ("USE-POWER", "Топливо для генерации; выхлоп и CO", S3, "PROCESS"),
    ("USE-TRANSPORT", "Топливо для транспорта", S3, "PROCESS"),
    ("PRODUCT-ID", "Идентичность и спецификация готового топлива", S2, "SITE_DATA"),
    ("BATCH-ACCEPT", "Приёмка партии без самодельного анализа", S2, "TEST"),
    ("ROTATION", "Ротация и срок хранения готового топлива", S2, "MAINTENANCE"),
    ("SPILL", "Разлив; изоляция и законная очистка", S3, "PROCESS"),
    ("EXHAUST", "Выхлоп; CO; вентиляция и дымоход", S3, "PROCESS"),
    ("ASH", "Зола и безопасный маршрут", S3, "PROCESS"),
    ("CONSUMPTION", "Измеренный расход по конкретному прибору", S2, "TEST"),
    ("ALTERNATIVE", "Резервная более безопасная альтернатива функции", S1, "GOVERNANCE"),
    ("WOODLOT", "Законное древесное хозяйство и восстановление", S3, "PROCESS"),
    ("WOOD-DRY", "Сушка и измерение влажности древесины", S2, "PROCESS"),
]
for suffix, title, safety, node_type in fuel_children:
    add(f"TD-FUEL-{suffix}", "TD-FUELS", "ENERGY_FUELS", node_type, title, safety)
BRANCH_CHILDREN["TD-FUELS"] = [f"TD-FUEL-{item[0]}" for item in fuel_children]

# Maps, communications and accountability.
maps_children = [
    ("CONTACTS-PAPER", "Бумажные контакты и точки помощи", S1, "MATERIAL"),
    ("WARNINGS", "Официальный приём предупреждений", S1, "PROCESS"),
    ("CHECKIN", "План check-in", S1, "PROCESS"),
    ("MISSED", "Missed-check-in escalation", S2, "PROCESS"),
    ("ACCOUNTABILITY", "Учёт людей и последнего известного места", S2, "GOVERNANCE"),
    ("REUNION", "Reunification plan", S2, "PROCESS"),
    ("LOCAL-SIGNAL", "Локальные визуальные и звуковые сигналы", S1, "PROCESS"),
    ("MESSAGE", "Короткий формат сообщения и read-back", S1, "PROCESS"),
    ("LOG", "Журнал сообщений; время и решения", S1, "GOVERNANCE"),
    ("BUILDING-MAP", "План здания; выходы; отключения и огнетушители", S2, "DRAWING"),
    ("LOCAL-MAP", "Локальная бумажная и офлайн-карта", S1, "MATERIAL"),
    ("SERVICE-POINTS", "Медицина; пожар; вода; укрытие и аптеки", S1, "SITE_DATA"),
    ("HAZARD-MAP", "Пожар; наводнение; склон; цунами и промышленные риски", S2, "SITE_DATA"),
    ("R1-R3", "Независимые маршруты R1/R2/R3", S2, "DRAWING"),
    ("SLOWEST", "Полевой маршрут для самого медленного участника", S2, "TEST"),
    ("PRIVACY", "Защита координат людей; запасов и убежищ", S1, "GOVERNANCE"),
]
for suffix, title, safety, node_type in maps_children:
    add(f"TD-COMMS-{suffix}", "TD-MAPS-COMMS", "MAPS_COMMS", node_type, title, safety)
BRANCH_CHILDREN["TD-MAPS-COMMS"] = [f"TD-COMMS-{item[0]}" for item in maps_children]

# Transport and load movement.
branch(
    "TD-TRANSPORT",
    "TRANSPORT",
    "Перемещение людей; грузов и критических ресурсов",
    [
        ("WALK", "Пешая мобильность и доступность", S1, "PROCESS"),
        ("CARRY", "Безопасная переноска груза", S2, "TRAINING"),
        ("CART", "Ручная тележка и полезная нагрузка", S2, "TOOL"),
        ("BICYCLE", "Велосипед и грузовая конфигурация", S2, "TOOL"),
        ("VEHICLE", "Автомобиль; ограничения и эксплуатационный статус", S3, "MATERIAL"),
        ("DRIVER", "Водитель; право; навыки и документы", S3, "TRAINING"),
        ("RESTRAINT", "Удерживающие системы детей; людей и животных", S2, "MATERIAL"),
        ("RANGE", "Дальность; запас и точки возврата", S2, "TEST"),
        ("PAYLOAD", "Полезная нагрузка и центр тяжести", S2, "TEST"),
        ("TIRES", "Шины; давление; износ и запас", S2, "MAINTENANCE"),
        ("BRAKES", "Тормоза и критерий запрета движения", S3, "MAINTENANCE"),
        ("STEERING", "Рулевое и критерий запрета движения", S3, "MAINTENANCE"),
        ("PUMP", "Насос; манометр и переходники", S2, "TOOL"),
        ("JACK", "Домкрат; опоры и запрет работы под грузом", S3, "TOOL"),
        ("TOW", "Буксировка; точки крепления и правовая граница", S3, "PROCESS"),
        ("REPAIR", "Ремкомплект и послеремонтная приёмка", S3, "MAINTENANCE"),
        ("SPARES", "Запасные части и стандартные интерфейсы", S2, "MATERIAL"),
        ("ROUTE", "Маршрут; высота; покрытие и сезон", S2, "DRAWING"),
        ("ABANDON", "Abandonment plan и переход на ручную переноску", S2, "PROCESS"),
        ("ANIMAL", "Тягловые животные при наличии; welfare и handler", S3, "PROCESS"),
        ("BOAT", "Лодка и побережье только при локальной применимости", S4, "HAZARD_BOUNDARY"),
    ],
    S2,
)

# Personal safety and safeguarding without offensive systems.
branch(
    "TD-SECURITY",
    "SECURITY",
    "Безопасность людей; доступ и safeguarding",
    [
        ("SAFE-DIRECTION", "Распознать опасность; уйти; создать дистанцию", S1, "TRAINING"),
        ("DEESCALATION", "Деэскалация и отказ от самоуправства", S2, "TRAINING"),
        ("ACCESS", "Механический контроль доступа и ключей", S2, "PROCESS"),
        ("VISITORS", "Учёт посетителей без незаконного удержания", S1, "GOVERNANCE"),
        ("CHILD", "Защита детей и зависимых людей", S2, "GOVERNANCE"),
        ("DV", "Домашнее насилие; конфиденциальный безопасный маршрут", S3, "KNOWLEDGE"),
        ("MISSING", "Пропавший участник и последняя известная точка", S2, "PROCESS"),
        ("SAFE-PLACE", "Заранее выбранное безопасное место", S2, "SITE_DATA"),
        ("CONFLICT", "Конфликт интересов; жалоба и независимый review", S1, "GOVERNANCE"),
        ("LIGHT", "Освещение; обзор и устранение скрытых опасных зон", S2, "PROCESS"),
        ("INCIDENT", "Журнал инцидентов с минимизацией персональных данных", S1, "GOVERNANCE"),
        ("NO-OFFENSE", "Запрет наступательных; взрывных и токсичных систем", S4, "HAZARD_BOUNDARY"),
    ],
    S2,
)

# Workshop details.
workshop_children = [
    ("SPACE", "Рабочее пространство; проходы и уборка", S2, "SITE_DATA"),
    ("LIGHT", "Освещение рабочего места", S1, "MATERIAL"),
    ("VENT", "Вентиляция; пыль и пары", S3, "PROCESS"),
    ("FIRE", "Пожарная безопасность мастерской", S2, "PROCESS"),
    ("PPE", "PPE по конкретной операции", S2, "MATERIAL"),
    ("CUSTODY", "Выдача; возврат и состояние инструмента", S1, "GOVERNANCE"),
    ("MARK", "Разметка и reference surfaces", S1, "PROCESS"),
    ("TEMPLATES", "Шаблоны; кондукторы и повторяемость", S2, "DRAWING"),
    ("HOLD", "Удержание детали и workholding", S2, "TOOL"),
    ("CUT", "Ручная резка", S2, "TRAINING"),
    ("DRILL", "Ручное и маломощное сверление", S2, "TRAINING"),
    ("FILE", "Опиливание и снятие заусенцев", S2, "TRAINING"),
    ("PLANE", "Строгание древесины", S2, "TRAINING"),
    ("ABRASIVE", "Абразивная обработка и контроль пыли", S3, "PROCESS"),
    ("SHARPEN", "Заточка и проверка режущего инструмента", S2, "PROCESS"),
    ("FASTEN", "Крепёж; резьбы и стандартные размеры", S2, "PROCESS"),
    ("TORQUE", "Момент затяжки и критические соединения", S3, "TEST"),
    ("ADHESIVE", "Клеевые соединения по маркировке и совместимости", S2, "PROCESS"),
    ("SEW", "Швы; ремонт ткани и мягкого снаряжения", S1, "PROCESS"),
    ("ROPE", "Канаты; узлы; сети и такелаж без life-safety импровизации", S2, "TRAINING"),
    ("METAL-COLD", "Холодная обработка металла", S3, "PROCESS"),
    ("PLUMBING", "Низкорисковый ремонт сантехники", S2, "PROCESS"),
    ("PUMPS", "Насосы; клапаны и уплотнения", S3, "MAINTENANCE"),
    ("BICYCLE", "Обслуживание велосипеда", S2, "MAINTENANCE"),
    ("CART", "Обслуживание ручной тележки", S2, "MAINTENANCE"),
    ("FOOTWEAR", "Ремонт обуви", S2, "PROCESS"),
    ("DONOR", "Сортировка доноров и карантин неизвестных компонентов", S2, "PROCESS"),
    ("CONSUMABLES", "Расходники и минимальные остатки", S1, "MATERIAL"),
    ("INTERFACES", "Стандартизация размеров; резьб; напряжений и разъёмов", S2, "GOVERNANCE"),
    ("POST-TEST", "Послеремонтное испытание и карантин брака", S2, "TEST"),
]
for suffix, title, safety, node_type in workshop_children:
    add(f"TD-WORKSHOP-{suffix}", "TD-WORKSHOP", "WORKSHOP", node_type, title, safety)
BRANCH_CHILDREN["TD-WORKSHOP"] = [f"TD-WORKSHOP-{item[0]}" for item in workshop_children]

# Metrology network.
metrology_children = [
    ("SI", "SI; единицы и преобразования", S0, "KNOWLEDGE"),
    ("LENGTH", "Длина; площадь и геометрия", S1, "INSTRUMENT"),
    ("MASS", "Масса", S1, "INSTRUMENT"),
    ("TIME", "Время и интервал", S1, "INSTRUMENT"),
    ("TEMP", "Температура", S2, "INSTRUMENT"),
    ("HUMIDITY", "Относительная влажность", S2, "INSTRUMENT"),
    ("PRESSURE", "Давление без вмешательства в опасную систему", S3, "INSTRUMENT"),
    ("FLOW", "Расход жидкости", S2, "INSTRUMENT"),
    ("VOLUME", "Объём", S1, "INSTRUMENT"),
    ("ANGLE", "Угол; уровень и уклон", S1, "INSTRUMENT"),
    ("ELECTRIC", "Низковольтные V; A; ohm; W и Wh", S2, "INSTRUMENT"),
    ("LIGHT", "Освещённость", S1, "INSTRUMENT"),
    ("CO-SMOKE", "CO и дым штатными извещателями", S2, "INSTRUMENT"),
    ("PH", "pH с ограничением интерпретации", S2, "INSTRUMENT"),
    ("EC", "Электропроводность", S2, "INSTRUMENT"),
    ("TURBIDITY", "Мутность как операционный показатель", S2, "INSTRUMENT"),
    ("CHLORINE", "Остаточный хлор по точному методу", S2, "INSTRUMENT"),
    ("SOIL", "Полевые измерения почвы", S2, "INSTRUMENT"),
    ("MOISTURE", "Влажность зерна; семян и древесины", S2, "INSTRUMENT"),
    ("RAIN", "Осадки", S2, "INSTRUMENT"),
    ("WIND", "Ветер", S2, "INSTRUMENT"),
    ("POSITION", "Координаты; азимут и высота", S2, "INSTRUMENT"),
    ("MEDICAL", "Разрешённые неинвазивные медицинские измерения", S3, "INSTRUMENT"),
    ("REFERENCE", "Reference/check; zero и контрольная точка", S2, "TEST"),
    ("UNCERTAINTY", "Неопределённость и decision rule", S2, "KNOWLEDGE"),
    ("HISTORY", "История калибровок и межприборное сравнение", S2, "GOVERNANCE"),
    ("SPARES", "Питание; реактивы и расходники измерений", S2, "MATERIAL"),
    ("FAILURE", "Признаки отказа и ручной fallback", S2, "TEST"),
]
for suffix, title, safety, node_type in metrology_children:
    add(f"TD-METRO-{suffix}", "TD-BASE-METROLOGY", "BASE", node_type, title, safety, "TD-BASE-SAFETY|TD-BASE-INVENTORY")
BRANCH_CHILDREN["TD-BASE-METROLOGY"] = [f"TD-METRO-{item[0]}" for item in metrology_children]

# Materials and manufacturing chains.
branch(
    "TD-MATERIALS-PRODUCTION",
    "MATERIALS",
    "Материалы; компоненты и производственные цепочки",
    [
        ("IDENTITY", "Идентификация материала; партии и неизвестных примесей", S2, "SITE_DATA"),
        ("STORAGE", "Совместимое хранение материалов", S2, "PROCESS"),
        ("WOOD-HARVEST", "Законная заготовка древесины и лесовосстановление", S3, "PROCESS"),
        ("WOOD-SAW", "Распил древесины", S3, "PROCESS"),
        ("WOOD-DRY", "Сушка и хранение древесины", S2, "PROCESS"),
        ("WOOD-JOIN", "Деревянные соединения и ремонт", S2, "PROCESS"),
        ("METAL-SORT", "Идентификация и сортировка металлолома", S3, "PROCESS"),
        ("CORROSION", "Коррозия; защита и inspection", S2, "PROCESS"),
        ("METAL-COLD", "Холодная обработка и механические соединения металла", S3, "PROCESS"),
        ("WELD", "Сварка и hot work", S4, "HAZARD_BOUNDARY"),
        ("SMELT", "Плавка; литьё; ковка и термообработка", S4, "HAZARD_BOUNDARY"),
        ("CLAY", "Идентификация и подготовка глины", S3, "PROCESS"),
        ("CERAMIC", "Керамика; кирпич; черепица и огнеупоры", S3, "PROCESS"),
        ("KILN", "Печь и обжиг", S4, "HAZARD_BOUNDARY"),
        ("GLASS-REPAIR", "Безопасное обращение; резка и ремонт стекла", S3, "PROCESS"),
        ("GLASS-MAKE", "Производство стекла", S4, "HAZARD_BOUNDARY"),
        ("STONE", "Камень; кладка и пылевая опасность", S3, "PROCESS"),
        ("LIME", "Готовая известь; растворы и маркировка", S3, "MATERIAL"),
        ("CEMENT", "Цемент; бетон и контроль смеси", S3, "PROCESS"),
        ("STRUCTURAL", "Конструктивное применение материалов", S4, "HAZARD_BOUNDARY"),
        ("FIBER", "Растительные и животные волокна", S2, "MATERIAL"),
        ("WOOL", "Шерсть; очистка и хранение", S2, "PROCESS"),
        ("FLAX", "Лён и локально допустимые волокнистые культуры", S2, "PROCESS"),
        ("CARD", "Очистка и кардование волокон", S2, "PROCESS"),
        ("SPIN", "Прядение", S2, "PROCESS"),
        ("WEAVE", "Ткачество", S2, "PROCESS"),
        ("KNIT", "Вязание", S1, "PROCESS"),
        ("FELT", "Валяние", S2, "PROCESS"),
        ("ROPE", "Канаты и сети; не для life-safety без сертификации", S3, "PROCESS"),
        ("LEATHER", "Кожа; ремонт и обувь", S3, "PROCESS"),
        ("TANNING", "Дубление кожи", S4, "HAZARD_BOUNDARY"),
        ("PAPER", "Бумага и долговременное хранение", S2, "PROCESS"),
        ("PRINT", "Печать и тиражирование", S2, "PROCESS"),
        ("INK", "Чернила и маркировка", S3, "PROCESS"),
        ("BIND", "Переплёт и ремонт книг", S2, "PROCESS"),
        ("POLYMER", "Полимеры; резина и совместимость", S3, "MATERIAL"),
        ("POLYMER-MAKE", "Промышленное производство полимеров", S4, "HAZARD_BOUNDARY"),
        ("ADHESIVE", "Готовые клеи; герметики и покрытия", S3, "MATERIAL"),
        ("SEAL", "Уплотнения и совместимость с жидкостью/температурой", S3, "MATERIAL"),
        ("FASTENER", "Крепёж и стандартные резьбы", S2, "MATERIAL"),
        ("WIRE", "Проволока и безопасная механическая работа", S3, "MATERIAL"),
        ("SPRING", "Пружины и stored energy", S4, "HAZARD_BOUNDARY"),
        ("BEARING", "Подшипники и посадки", S3, "MATERIAL"),
        ("GEAR", "Шестерни; цепи и ремни", S3, "MATERIAL"),
        ("ABRASIVE", "Абразивы и режущий инструмент", S3, "MATERIAL"),
        ("LUBRICANT", "Смазки и технические жидкости", S3, "MATERIAL"),
        ("INTERFACE", "Стандартизация интерфейсов и взаимозаменяемость", S2, "GOVERNANCE"),
        ("MACHINE-DRILL", "Ручная стойка и drill press", S3, "TOOL"),
        ("MACHINE-LATHE", "Токарный станок", S4, "HAZARD_BOUNDARY"),
        ("MACHINE-MILL", "Фрезерование", S4, "HAZARD_BOUNDARY"),
        ("MACHINE-GRIND", "Станочное шлифование", S4, "HAZARD_BOUNDARY"),
        ("MACHINE-GUARD", "Привод; ограждения; LOTO и stored energy", S4, "HAZARD_BOUNDARY"),
        ("MACHINE-ALIGN", "Выравнивание; биение и workholding", S3, "TEST"),
        ("CRITICAL-PART", "Ответственные детали транспорта; давления; медицины и PPE", S4, "HAZARD_BOUNDARY"),
    ],
    S3,
)

# Education and competency succession.
branch(
    "TD-EDUCATION",
    "EDUCATION",
    "Образование; подготовка и передача компетенций",
    [
        ("LITERACY", "Грамотность и понимание инструкций", S1, "TRAINING"),
        ("NUMERACY", "Арифметика; единицы и пропорции", S1, "TRAINING"),
        ("LANG", "Русский; украинский; португальский и английский", S1, "TRAINING"),
        ("TECH-READ", "Чтение технического текста и чертежей", S2, "TRAINING"),
        ("SKILL-MATRIX", "Матрица навыков; роли и дублёры", S1, "GOVERNANCE"),
        ("PREREQ", "Предварительные знания и допуски", S1, "GOVERNANCE"),
        ("APPRENTICE", "Ученичество и наблюдаемая практика", S2, "TRAINING"),
        ("SUPERVISED", "Практика под надзором", S2, "TRAINING"),
        ("MASTERY", "Проверка мастерства по критериям", S2, "TEST"),
        ("RECERT", "Переоценка; срок навыка и recertification", S2, "MAINTENANCE"),
        ("TEACHBACK", "Teach-back и слепое повторение", S2, "TEST"),
        ("INSTRUCTOR", "Преемственность инструкторов", S2, "GOVERNANCE"),
        ("ACCESS", "Доступность обучения для разных возможностей", S1, "PROCESS"),
        ("CHILD", "Безопасная учебная программа для детей", S2, "GOVERNANCE"),
        ("PAPER", "Бумажная учебная программа и экзамены", S1, "KNOWLEDGE"),
    ],
    S2,
)

# Knowledge, computing, print fallback and restoration.
knowledge_children = [
    ("FIXITY", "Регулярная fixity-проверка ранее записанных хешей", S1, "TEST"),
    ("COPIES", "Независимые локальные и offsite копии", S1, "MATERIAL"),
    ("MIGRATION", "Миграция форматов и носителей", S2, "PROCESS"),
    ("SEARCH", "Локальный полнотекстовый индекс", S1, "PROCESS"),
    ("PRINT-CORE", "Печатное P0/P1 ядро", S1, "MATERIAL"),
    ("SOURCE-CODE", "Исходный код критических инструментов", S1, "KNOWLEDGE"),
    ("COMPILERS", "Компиляторы; runtimes и reproducible build", S2, "KNOWLEDGE"),
    ("GIS", "Офлайн GIS и открытые форматы", S2, "KNOWLEDGE"),
    ("EDA-CAD", "CAD/EDA и открытые редактируемые форматы", S2, "KNOWLEDGE"),
    ("HARDWARE", "Ремонт вычислительной техники и donor plan", S3, "MAINTENANCE"),
    ("READERS-SPARE", "Запасные readers и установщики", S1, "MATERIAL"),
    ("PAPER-FALLBACK", "Механические и бумажные fallback-системы", S1, "PROCESS"),
    ("LANGUAGE", "Перевод; словари и терминологические соответствия", S1, "KNOWLEDGE"),
    ("RIGHTS", "Права; provenance и допустимая локальная копия", S0, "GOVERNANCE"),
    ("SUCCESSOR", "Восстановление и поиск преемником с чистого устройства", S2, "TEST"),
]
for suffix, title, safety, node_type in knowledge_children:
    add(f"TD-KNOWLEDGE-{suffix}", "TD-KNOWLEDGE", "KNOWLEDGE", node_type, title, safety, "TD-BASE-SAFETY|TD-BASE-ARCHIVE")
BRANCH_CHILDREN["TD-KNOWLEDGE"] = [f"TD-KNOWLEDGE-{item[0]}" for item in knowledge_children]

# Governance, economy, logistics and inter-group cooperation.
governance_children = [
    ("LIMITS", "Ограничение чрезвычайных полномочий и сроков", S1, "GOVERNANCE"),
    ("AUDIT", "Независимый аудит решений и ресурсов", S1, "GOVERNANCE"),
    ("GRIEVANCE", "Жалоба; апелляция и защита от возмездия", S1, "GOVERNANCE"),
    ("VULNERABLE", "Защита уязвимых и зависимых участников", S2, "GOVERNANCE"),
    ("LAW", "Земля; имущество; договоры и применимое право", S0, "KNOWLEDGE"),
    ("BIRTH-DEATH", "Записи рождения; смерти и идентичности", S3, "GOVERNANCE"),
    ("TRADE", "Законный обмен; специализация и договорённости", S1, "GOVERNANCE"),
    ("COMMUNITY", "Межгрупповая кооперация и взаимопомощь", S1, "GOVERNANCE"),
    ("PROCUREMENT", "Закупка; приёмка и provenance", S1, "PROCESS"),
    ("STOCK", "Минимальные остатки; reorder point и ротация", S1, "GOVERNANCE"),
    ("WAREHOUSE", "Склад; зоны совместимости и доступ", S2, "SITE_DATA"),
    ("DISTRIBUTION", "Выдача ресурсов и chain of custody", S1, "PROCESS"),
    ("LABOR", "Бюджет труда; смены и неэксплуатирующие нормы", S1, "GOVERNANCE"),
    ("RECOVERY", "After-action review и восстановление", S1, "PROCESS"),
    ("RELOCATION", "Законный перенос людей; архивов и функций", S2, "PROCESS"),
]
for suffix, title, safety, node_type in governance_children:
    add(f"TD-GOV-{suffix}", "TD-GOV", "GOVERNANCE", node_type, title, safety)
BRANCH_CHILDREN["TD-GOV"] = [f"TD-GOV-{item[0]}" for item in governance_children]

# Environmental monitoring and adaptation.
branch(
    "TD-ENVIRONMENT",
    "ENVIRONMENT",
    "Среда; погода; климат и экосистемные пределы",
    [
        ("WEATHER", "Погода и локальные наблюдения", S1, "SITE_DATA"),
        ("DROUGHT", "Засуха и водный дефицит", S2, "SITE_DATA"),
        ("HEAT", "Жара и тепловой риск", S2, "SITE_DATA"),
        ("COLD", "Холод и мороз", S2, "SITE_DATA"),
        ("WIND", "Шторм и ветер", S2, "SITE_DATA"),
        ("FLOOD", "Наводнение и поверхностный сток", S2, "SITE_DATA"),
        ("FIRE", "Природный пожар; дым и эвакуация", S3, "SITE_DATA"),
        ("COAST", "Побережье; штормовой нагон и цунами", S3, "SITE_DATA"),
        ("SEISMIC", "Землетрясение и вторичные опасности", S2, "SITE_DATA"),
        ("SOIL-DEGRADE", "Эрозия; уплотнение и деградация почвы", S2, "TEST"),
        ("FOREST", "Лес; многолетние культуры и wildfire interface", S3, "PROCESS"),
        ("BIODIVERSITY", "Биоразнообразие и запрет неизвестных интродукций", S2, "GOVERNANCE"),
        ("CLIMATE", "Климатические траектории и adaptive pathways", S1, "KNOWLEDGE"),
    ],
    S2,
)

# Portugal overlay: authority, law, climate and local service bindings.
branch(
    "TD-PORTUGAL",
    "PORTUGAL",
    "Португалия: право; службы; карты и конкретная площадка",
    [
        ("112", "112 и экстренные службы", S0, "KNOWLEDGE"),
        ("SNS24", "SNS 24 и клиническая навигация", S0, "KNOWLEDGE"),
        ("CIAV", "CIAV и токсикологическая информация", S0, "KNOWLEDGE"),
        ("MUNICIPAL-PC", "Муниципальная Proteção Civil", S0, "SITE_DATA"),
        ("HOSPITAL", "Ближайшие больницы; centros de saúde и аптеки", S0, "SITE_DATA"),
        ("WATER-UTILITY", "Водоканал и аварийные контакты", S0, "SITE_DATA"),
        ("LABS", "Лаборатории воды и почвы", S0, "SITE_DATA"),
        ("ANEPC", "ANEPC: риски; планы и предупреждения", S0, "KNOWLEDGE"),
        ("IPMA", "IPMA: погода; сейсмика и цунами", S0, "KNOWLEDGE"),
        ("APA", "APA: вода; засуха; наводнения и среда", S0, "KNOWLEDGE"),
        ("ICNF", "ICNF: лес; пожар и охраняемые территории", S0, "KNOWLEDGE"),
        ("DGAV", "DGAV: животные; корма; растения и здоровье", S0, "KNOWLEDGE"),
        ("INIAV", "INIAV: агрономия; почвы; семена и исследования", S0, "KNOWLEDGE"),
        ("DGT", "DGT/SNIG/CAOP: карты и административные границы", S0, "KNOWLEDGE"),
        ("ENERGY", "DGEG/ERSE: энергия и топливо", S0, "KNOWLEDGE"),
        ("ANACOM", "ANACOM: радио и связь", S0, "KNOWLEDGE"),
        ("IMT", "IMT: транспорт и водительские требования", S0, "KNOWLEDGE"),
        ("ASAE", "ASAE: пища; рынок и безопасность продукции", S0, "KNOWLEDGE"),
        ("LAW", "Diário da República и контроль редакции закона", S0, "KNOWLEDGE"),
        ("WASTE", "Лицензированные операторы отходов", S0, "SITE_DATA"),
        ("PDM", "PDM и муниципальные строительные правила", S0, "KNOWLEDGE"),
        ("WATER-RIGHTS", "Право на воду; captação; колодец и скважина", S3, "GOVERNANCE"),
        ("RAIN-REUSE", "Дождевая вода и повторное использование", S3, "GOVERNANCE"),
        ("SEPTIC", "Канализация; fossa séptica и санитарные нормы", S3, "GOVERNANCE"),
        ("BURN", "Ограничения сжигания и пожарный период", S3, "GOVERNANCE"),
        ("FORESTRY", "Лесопользование и расчистка растительности", S3, "GOVERNANCE"),
        ("SEEDS", "Семена; сорта; plant health и pesticides", S3, "GOVERNANCE"),
        ("LIVESTOCK", "Животные; welfare; slaughter и ветеринарные нормы", S3, "GOVERNANCE"),
        ("FUEL", "Хранение топлива и пожарные ограничения", S3, "GOVERNANCE"),
        ("RADIO", "Радио; частоты; мощность и лицензии", S3, "GOVERNANCE"),
        ("BUILD", "Разрешения; проекты и professional sign-off", S3, "GOVERNANCE"),
        ("PROTECTED", "Охраняемые земли; побережье и ограничения", S3, "GOVERNANCE"),
        ("HAZARDS", "Пожар; засуха; жара; наводнение; цунами и землетрясение", S2, "SITE_DATA"),
        ("MUNICIPIO", "Конкретные município; freguesia; адрес и checked date", S1, "SITE_DATA"),
        ("OFFLINE", "Локальные копии; права; язык и дата проверки", S1, "KNOWLEDGE"),
    ],
    S1,
)


def append_unique(current: str, additions: list[str]) -> str:
    values = [value.strip() for value in current.split("|") if value.strip()]
    for value in additions:
        if value not in values:
            values.append(value)
    return "|".join(values)


def main() -> int:
    try:
        with REGISTER.open("r", encoding="utf-8-sig", newline="") as handle:
            reader = csv.DictReader(handle)
            fieldnames = list(reader.fieldnames or [])
            rows = list(reader)
    except (OSError, csv.Error) as exc:
        print(f"expand_catalog_error {exc}", file=sys.stderr)
        return 1
    if not fieldnames or "node_id" not in fieldnames:
        print("expand_catalog_error invalid technology register", file=sys.stderr)
        return 1

    order = [row["node_id"] for row in rows]
    by_id = {row["node_id"]: row for row in rows}
    for row in ADDITIONS:
        node_id = row["node_id"]
        if node_id not in by_id:
            order.append(node_id)
        by_id[node_id] = {field: row.get(field, "") for field in fieldnames}

    aggregate_updates = {
        "TD-ROOT": [
            "TD-BASE", "TD-PEOPLE", "TD-WATER", "TD-FOOD", "TD-SHELTER", "TD-ENERGY",
            "TD-HEALTH", "TD-MAPS-COMMS", "TD-KNOWLEDGE", "TD-GOV", "TD-WORKSHOP",
            "TD-FUELS", "TD-TRANSPORT", "TD-SECURITY", "TD-EDUCATION",
            "TD-MATERIALS-PRODUCTION", "TD-CONSTRUCTION", "TD-ANIMALS", "TD-ENVIRONMENT",
            "TD-PORTUGAL", "TD-HAZARDS",
        ],
        "TD-HEALTH": BRANCH_CHILDREN["TD-HEALTH"],
        "TD-WATER": BRANCH_CHILDREN["TD-WATER"],
        "TD-SANITATION": BRANCH_CHILDREN["TD-SANITATION"],
        "TD-FOOD": BRANCH_CHILDREN["TD-FOOD"] + ["TD-ANIMALS"],
        "TD-FERTILIZERS": BRANCH_CHILDREN["TD-FERTILIZERS"],
        "TD-SHELTER": BRANCH_CHILDREN["TD-SHELTER"] + ["TD-CONSTRUCTION"],
        "TD-ENERGY": BRANCH_CHILDREN["TD-ENERGY"],
        "TD-FUELS": BRANCH_CHILDREN["TD-FUELS"],
        "TD-MAPS-COMMS": BRANCH_CHILDREN["TD-MAPS-COMMS"],
        "TD-WORKSHOP": BRANCH_CHILDREN["TD-WORKSHOP"],
        "TD-BASE-METROLOGY": BRANCH_CHILDREN["TD-BASE-METROLOGY"],
        "TD-KNOWLEDGE": BRANCH_CHILDREN["TD-KNOWLEDGE"],
        "TD-GOV": BRANCH_CHILDREN["TD-GOV"],
    }
    for node_id, children in aggregate_updates.items():
        if node_id not in by_id:
            print(f"expand_catalog_error missing aggregate {node_id}", file=sys.stderr)
            return 1
        by_id[node_id]["prerequisite_node_ids"] = append_unique(
            by_id[node_id]["prerequisite_node_ids"], children
        )

    tmp = REGISTER.with_suffix(".csv.tmp")
    with tmp.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, quoting=csv.QUOTE_ALL, lineterminator="\n")
        writer.writeheader()
        writer.writerows(by_id[node_id] for node_id in order)
    tmp.replace(REGISTER)
    print(
        f"expand_catalog_ok original={len(rows)} additions={len(ADDITIONS)} total={len(order)} "
        f"aggregates_updated={len(aggregate_updates)}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
