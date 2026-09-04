#!/usr/bin/env python3
"""Build edge semantics, node priorities, service levels and ID crosswalks.

All generated planning decisions are explicitly provisional.  They organize the
catalog; they do not authorize execution or prove capacity.
"""

from __future__ import annotations

import csv
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parent
NODE_REGISTER = ROOT / "technology-dependency-register.csv"
EDGE_REGISTER = ROOT / "technology-dependency-edges.csv"
PLAN_REGISTER = ROOT / "technology-node-planning-register.csv"
SERVICE_REGISTER = ROOT / "technology-service-level-register.csv"
CROSSWALK_REGISTER = ROOT / "capability-crosswalk.csv"

PRIORITY_HORIZON = {
    "P0_RED": "SECONDS_TO_72_HOURS",
    "P1_ORANGE": "3_TO_14_DAYS",
    "P2_YELLOW": "15_TO_90_DAYS",
    "P3_GREEN": "3_MONTHS_TO_15_YEARS",
    "P4_BLUE": "15_TO_100_YEARS",
}

ROOT_ROLES = {
    "TD-BASE": ("REQUIRED", "SL0"),
    "TD-PEOPLE": ("REQUIRED", "SL0"),
    "TD-WATER": ("REQUIRED", "SL0"),
    "TD-FOOD": ("REQUIRED", "SL1"),
    "TD-SHELTER": ("REQUIRED", "SL0"),
    "TD-ENERGY": ("REQUIRED", "SL1"),
    "TD-HEALTH": ("REQUIRED", "SL0"),
    "TD-MAPS-COMMS": ("REQUIRED", "SL0"),
    "TD-KNOWLEDGE": ("REQUIRED", "SL2"),
    "TD-GOV": ("REQUIRED", "SL0"),
    "TD-WORKSHOP": ("REQUIRED", "SL3"),
    "TD-TRANSPORT": ("REQUIRED", "SL2"),
    "TD-SECURITY": ("REQUIRED", "SL0"),
    "TD-EDUCATION": ("REQUIRED", "SL3"),
    "TD-MATERIALS-PRODUCTION": ("CONDITIONAL", "SL5"),
    "TD-ENVIRONMENT": ("REQUIRED", "SL2"),
    "TD-PORTUGAL": ("REQUIRED", "SL0"),
    "TD-FUELS": ("CONDITIONAL", "SL2"),
    "TD-CONSTRUCTION": ("CONDITIONAL", "SL3"),
    "TD-ANIMALS": ("CONDITIONAL", "SL3"),
    "TD-HAZARDS": ("HAZARD_ONLY", "SL0"),
}

ALTERNATIVE_GROUPS = {
    "WATER_SOURCE": {
        "TD-WATER-RAIN", "TD-WATER-DELIVERED", "TD-WATER-WELL", "TD-WATER-SURFACE"
    },
    "WATER_DELIVERY": {
        "TD-WATER-GRAVITY", "TD-WATER-HAND-PUMP", "TD-WATER-LOWE-PUMP"
    },
    "ENERGY_SUPPLY": {"TD-ENERGY-GENERATION", "TD-ENERGY-SOURCE"},
    "TRANSPORT_MODE": {
        "TD-TRANSPORT-WALK", "TD-TRANSPORT-CART", "TD-TRANSPORT-BICYCLE", "TD-TRANSPORT-VEHICLE"
    },
    "CROP_PORTFOLIO": {
        "TD-AGRI-STAPLES", "TD-AGRI-LEGUMES", "TD-AGRI-OILSEEDS", "TD-AGRI-VEGETABLES", "TD-AGRI-PERENNIALS"
    },
    "FERTILITY_STRATEGY": {
        "TD-FERT-CROP-ROTATION", "TD-FERT-COMPOST", "TD-FERT-MANURE", "TD-FERT-LEGUMES",
        "TD-FERT-RESIDUES", "TD-FERT-LABELED"
    },
}

ALTERNATIVE_SOURCE = {
    "WATER_SOURCE": "TD-WATER",
    "WATER_DELIVERY": "TD-WATER",
    "ENERGY_SUPPLY": "TD-ENERGY",
    "TRANSPORT_MODE": "TD-TRANSPORT",
    "CROP_PORTFOLIO": "TD-FOOD",
    "FERTILITY_STRATEGY": "TD-FERTILIZERS",
}

OPTIONAL_PREFIXES = (
    "TD-FUEL-CHARCOAL-MAKING",
    "TD-FUEL-VEGOIL",
    "TD-FUEL-WOODLOT",
    "TD-FUEL-WOOD-DRY",
    "TD-WORKSHOP-BICYCLE",
    "TD-WORKSHOP-CART",
    "TD-WORKSHOP-FOOTWEAR",
)

CONDITIONAL_PREFIXES = (
    "TD-ANIMALS-",
    "TD-CONSTRUCTION-",
    "TD-HEALTH-ANAPHYLAXIS",
    "TD-HEALTH-RESP",
    "TD-HEALTH-DIABETES",
    "TD-HEALTH-MATERNAL",
    "TD-HEALTH-PEDIATRIC",
    "TD-HEALTH-COLD-CHAIN",
    "TD-HEALTH-MEDS",
    "TD-HEALTH-MEDICATION",
    "TD-FERT-ASH",
    "TD-FERT-LIME-USE",
    "TD-FERT-MICRONUTRIENTS",
    "TD-FERT-STORAGE",
    "TD-TRANSPORT-VEHICLE",
    "TD-TRANSPORT-DRIVER",
    "TD-TRANSPORT-ANIMAL",
    "TD-PORTUGAL-WATER-RIGHTS",
    "TD-PORTUGAL-RAIN-REUSE",
    "TD-PORTUGAL-SEPTIC",
    "TD-PORTUGAL-BURN",
    "TD-PORTUGAL-FORESTRY",
    "TD-PORTUGAL-SEEDS",
    "TD-PORTUGAL-LIVESTOCK",
    "TD-PORTUGAL-FUEL",
    "TD-PORTUGAL-RADIO",
    "TD-PORTUGAL-BUILD",
    "TD-PORTUGAL-PROTECTED",
)


def split_ids(value: str) -> list[str]:
    return [part.strip() for part in value.split("|") if part.strip()]


def priority(node: dict[str, str]) -> str:
    node_id = node["node_id"]
    domain = node["domain"]
    if node_id.startswith("TD-HAZ"):
        return "P0_RED"
    if node_id.startswith(("TD-PEOPLE", "TD-SECURITY")) and not node_id.endswith("DEMOGRAPHY"):
        return "P0_RED"
    if node_id.startswith("TD-HEALTH"):
        # Health is split by response horizon and audience.  The order is
        # deliberate: professional and century-continuity shelves must never
        # be promoted to the lay P0 queue merely because they share the
        # TD-HEALTH prefix.
        if any(term in node_id for term in (
            "-P4-", "SUCCESSION", "GMP", "VACCINE-MANUFACTURE",
            "DEVICE-MAKE", "RESEARCH", "GENETICS", "LEGACY",
            "INSTITUTION", "GUIDELINE", "QA-PEER", "PUBLIC-RECORDS",
        )):
            return "P4_BLUE"
        if any(term in node_id for term in (
            "-PROF-", "-PRO-", "PROFESSIONAL", "CLINICIAN",
            "DELAYED", "REHAB", "PALLIATIVE", "DEATH",
        )):
            return "P3_GREEN"
        if any(term in node_id for term in (
            "PREVENT-VACCINE", "CHILD-GROWTH", "FALLS", "OCC-HEALTH",
            "VECTOR", "SURVEILLANCE", "ISOLATION-ROOM",
            "SUPPLY-REGISTER", "DEVICE-QC", "AED-LIFECYCLE",
            "SKILL-MATRIX", "REFERRAL-NET", "CARE-ROOM",
            "CASUALTY-CAPACITY",
        )):
            return "P2_YELLOW"
        if any(term in node_id for term in (
            "-CONT-", "-CARE-", "POSTPARTUM", "REPRODUCTIVE",
            "ASSISTIVE", "GRIEF", "PREVENTION", "WOUNDS", "DENTAL",
            "IPC", "MEDICATION", "COLD-CHAIN", "MED-WASTE",
        )):
            return "P1_ORANGE"
        return "P0_RED"
    if node["node_type"] == "HAZARD_BOUNDARY":
        return "P0_RED"
    if node_id.startswith("TD-WATER"):
        if any(term in node_id for term in ("P0", "DEMAND", "RATION", "VULNERABLE", "CARRY", "CROSS-CONTAM", "LABEL", "EMERGENCY", "CONTAINER")):
            return "P0_RED"
        if any(term in node_id for term in ("PORTFOLIO", "RAIN", "DELIVERED", "GRAVITY", "HAND-PUMP", "LOWE-PUMP", "DISTRIBUTION", "LEAK", "SPARES", "REDUNDANCY")):
            return "P1_ORANGE"
        return "P2_YELLOW"
    if node_id.startswith("TD-SAN"):
        return "P0_RED" if any(term in node_id for term in ("TOILET", "HANDWASH", "ZONING", "SOAP", "MENSTRUAL", "DIAPERS", "INCONTINENCE")) else "P1_ORANGE"
    if node_id.startswith("TD-FOOD"):
        if any(term in node_id for term in ("P0", "NO-COOK", "MENU", "ALLERGEN", "SPECIAL", "INFANT", "COOK-WATER", "HAND-TOOLS")):
            return "P0_RED"
        if any(term in node_id for term in ("P1", "COOK", "PEST", "WASTE", "ROTATION", "RATION", "PRESERVATION", "NUTRITION")):
            return "P1_ORANGE"
        return "P2_YELLOW"
    if node_id.startswith(("TD-AGRI", "TD-SEED", "TD-CROP", "TD-HARVEST", "TD-FERT")):
        return "P2_YELLOW" if node["safety_class"] not in {"S4_REFERENCE_ONLY_PROHIBITED_HOUSEHOLD"} else "P3_GREEN"
    if node_id.startswith("TD-SHELTER") or node_id in {"TD-EXITS-SHUTOFFS", "TD-FIRE-CO", "TD-VENTILATION", "TD-THERMAL"}:
        return "P0_RED" if any(term in node_id for term in ("EXIT", "FIRE", "ALARM", "SHUTOFF", "SAFE-ZONE", "LIGHT", "HEAT-ZONE", "COLD-ZONE", "DEPENDENTS")) else "P1_ORANGE"
    if node_id.startswith("TD-ENERGY"):
        return "P0_RED" if any(term in node_id for term in ("LIGHT", "COMMS", "MEDICAL", "COLD-CHAIN", "FLASHLIGHT")) else "P1_ORANGE"
    if node_id.startswith(("TD-MAPS", "TD-ROUTES", "TD-NAVIGATION", "TD-COMMS", "TD-TIME")):
        return "P0_RED" if any(term in node_id for term in ("CONTACTS", "WARNING", "CHECKIN", "MISSED", "ACCOUNTABILITY", "REUNION", "MESSAGE", "BUILDING", "SERVICE-POINTS")) else "P1_ORANGE"
    if node_id.startswith("TD-PORTUGAL"):
        return "P0_RED" if any(term in node_id for term in ("112", "SNS24", "CIAV", "MUNICIPAL-PC", "HOSPITAL", "ANEPC", "IPMA", "MUNICIPIO", "HAZARDS")) else "P2_YELLOW"
    if node_id.startswith("TD-TRANSPORT"):
        return "P1_ORANGE"
    if node_id.startswith("TD-BASE"):
        return "P0_RED" if any(term in node_id for term in ("SAFETY", "SITE", "INVENTORY")) else "P2_YELLOW"
    if node_id.startswith("TD-METRO"):
        return "P2_YELLOW"
    if node_id.startswith("TD-KNOWLEDGE"):
        return "P1_ORANGE" if any(term in node_id for term in ("CORPUS", "READERS", "INDEX", "SEARCH", "PRINT-CORE", "RESTORE")) else "P3_GREEN"
    if node_id.startswith("TD-GOV"):
        return "P0_RED" if any(term in node_id for term in ("ROLES", "SAFEGUARD", "LEDGER", "CONFLICT", "LIMITS", "VULNERABLE", "LABOR")) else "P4_BLUE"
    if node_id.startswith("TD-EDUCATION"):
        return "P2_YELLOW" if any(term in node_id for term in ("LITERACY", "NUMERACY", "SKILL", "PREREQ", "PAPER")) else "P4_BLUE"
    if node_id.startswith("TD-ENVIRONMENT"):
        return "P1_ORANGE" if any(term in node_id for term in ("WEATHER", "DROUGHT", "HEAT", "COLD", "WIND", "FLOOD", "FIRE", "COAST", "SEISMIC")) else "P3_GREEN"
    if node_id.startswith(("TD-WORKSHOP", "TD-FUELS", "TD-FUEL")):
        return "P2_YELLOW" if node["safety_class"] in {"S1_LOW_RISK_HOUSEHOLD", "S2_TRAINED_SUPERVISED"} else "P3_GREEN"
    if node_id.startswith(("TD-MATERIALS", "TD-CONSTRUCTION", "TD-ANIMALS")):
        return "P3_GREEN"
    if node_id in {"TD-ROOT", "TD-PEOPLE-DEMOGRAPHY"}:
        return "P4_BLUE"
    return "P3_GREEN"


def service_level(node: dict[str, str], node_priority: str) -> str:
    node_id = node["node_id"]
    if node_id.startswith(("TD-HEALTH-BLS", "TD-HEALTH-AIRWAY", "TD-HEALTH-BLEED", "TD-HEALTH-CONTACTS", "TD-HEALTH-SCENE", "TD-HEALTH-PRIMARY")):
        return "SL0"
    if node_id.startswith(("TD-EXITS", "TD-FIRE", "TD-SHELTER-ALARM", "TD-COMMS-WARNING", "TD-PORTUGAL-112")):
        return "SL0"
    if node_priority == "P0_RED":
        return "SL1"
    if node_priority == "P1_ORANGE":
        return "SL2"
    if node_priority == "P2_YELLOW":
        return "SL3"
    if node_priority == "P3_GREEN":
        return "SL5" if node["domain"] in {"MATERIALS", "CONSTRUCTION", "ENERGY_FUELS"} else "SL4"
    return "SL6"


def capacity_model(node: dict[str, str]) -> str:
    domain = node["domain"]
    return {
        "PEOPLE_CARE": "PERSON_HOURS_DEPENDENCY_AND_SHIFT_CAPACITY",
        "HEALTH": "PERSON_SPECIFIC_RESPONSE_TIME_AND_CARE_HOURS",
        "WATER_WASH": "LITRES_PER_PERSON_DAY_PLUS_PEAK_AND_STORAGE_DAYS",
        "FOOD_AGRI": "KCAL_NUTRIENTS_PER_PERSON_DAY_YIELD_AREA_AND_LOSS",
        "ANIMALS": "HEAD_COUNT_FEED_WATER_AREA_AND_HANDLER_HOURS",
        "SHELTER": "OCCUPANTS_M2_TEMPERATURE_AIR_AND_EGRESS_TIME",
        "ENERGY": "WH_PER_DAY_PEAK_W_AUTONOMY_AND_RECHARGE_TIME",
        "ENERGY_FUELS": "LITRES_OR_KG_PER_SERVICE_DAY_AND_SAFE_STORAGE",
        "MAPS_COMMS": "PEOPLE_CHANNELS_COVERAGE_CHECKIN_AND_ROUTE_TIME",
        "TRANSPORT": "PEOPLE_KG_KM_RANGE_AND_TURNAROUND_TIME",
        "WORKSHOP": "JOBS_PER_PERIOD_LABOR_HOURS_AND_SPARES",
        "MATERIALS": "MASS_VOLUME_THROUGHPUT_YIELD_AND_REJECT_RATE",
        "CONSTRUCTION": "AREA_LOAD_WEATHER_WINDOW_LABOR_AND_INSPECTION",
        "EDUCATION": "LEARNERS_HOURS_COMPETENCY_AND_DUPLICATES",
        "KNOWLEDGE": "BYTES_DOCUMENTS_READERS_RESTORE_TIME_AND_COPIES",
        "GOVERNANCE": "DECISIONS_RESOURCES_LABOR_HOURS_AND_AUDIT_INTERVAL",
        "ENVIRONMENT": "SITE_SERIES_SEASONAL_RANGE_AND_TRIGGER_THRESHOLDS",
        "PORTUGAL": "AUTHORITY_JURISDICTION_VERSION_COVERAGE_AND_CHECKED_DATE",
        "BASE": "OBJECT_COUNT_COVERAGE_REVIEW_INTERVAL_AND_EVIDENCE",
    }.get(domain, "SERVICE_SPECIFIC_UNIT_AND_TIME_WINDOW_TBD")


def alternative_group(source: str, target: str) -> str:
    for group, members in ALTERNATIVE_GROUPS.items():
        if ALTERNATIVE_SOURCE[group] == source and target in members:
            return group
    return ""


def edge_role(source: dict[str, str], target: dict[str, str]) -> tuple[str, str, str]:
    source_id = source["node_id"]
    target_id = target["node_id"]
    if source_id == "TD-ROOT" and target_id in ROOT_ROLES:
        role, _ = ROOT_ROLES[target_id]
        condition = {
            "TD-FUELS": "fuel_dependent_service_present",
            "TD-CONSTRUCTION": "construction_or_structural_work_present",
            "TD-ANIMALS": "animals_present",
            "TD-MATERIALS-PRODUCTION": "household_repair_or_intergroup_production_path_selected",
            "TD-HAZARDS": "always_visible_as_stop_boundary",
        }.get(target_id, "")
        return role, "", condition
    if target["node_type"] == "HAZARD_BOUNDARY":
        return "HAZARD_ONLY", "", "not_an_operational_prerequisite"
    if target["safety_class"] == "S4_REFERENCE_ONLY_PROHIBITED_HOUSEHOLD" or target["release_gate"] == "REFERENCE_ONLY":
        return "REFERENCE", "", "professional_or_historical_reference_only"
    group = alternative_group(source_id, target_id)
    if group:
        return "ALTERNATIVE", group, "select_at_least_one_verified_path_for_applicable_service"
    if target_id.startswith(OPTIONAL_PREFIXES):
        return "OPTIONAL", "", "use_only_if_selected_technology_requires_it"
    if target_id.startswith(CONDITIONAL_PREFIXES) or target["safety_class"] == "S3_LICENSED_PROFESSIONAL":
        return "CONDITIONAL", "", "applicable_profile_site_or_qualified_role_required"
    if target_id == "TD-HEALTH-PRO":
        return "REFERENCE", "", "professional_shelf_does_not_block_lay_first_aid"
    return "REQUIRED", "", ""


SERVICE_LEVELS = {
    "SL0": ("SECONDS_TO_12_HOURS", "Немедленно сохранить жизнь; выйти из опасности; вызвать помощь и учесть людей"),
    "SL1": ("12_TO_72_HOURS", "Поддержать воду; пищу; санитарный минимум; тепло; свет; связь и личные лекарства"),
    "SL2": ("3_TO_14_DAYS", "Обеспечить ротационные резервы; уход; отходы; карты; транспорт и отказ одного канала"),
    "SL3": ("15_TO_90_DAYS", "Развернуть ремонт; обучение; запасы; полевые испытания и сезонную подготовку"),
    "SL4": ("ONE_SEASON_TO_ONE_YEAR", "Пройти полный сезон воды; пищи; семян; энергии и обслуживания с измеренными потерями"),
    "SL5": ("ONE_TO_15_YEARS", "Поддерживать инфраструктуру; материалы; профессиональную сеть; замену и миграцию знаний"),
    "SL6": ("15_TO_100_YEARS", "Передать права; навыки; архив; землю; институты и межгрупповые зависимости следующему поколению"),
}

SERVICE_REQUIREMENTS = {
    "SL0": ["TD-BASE", "TD-PEOPLE", "TD-HEALTH", "TD-WATER", "TD-SHELTER", "TD-MAPS-COMMS", "TD-GOV", "TD-SECURITY", "TD-PORTUGAL"],
    "SL1": ["TD-WATER", "TD-FOOD", "TD-SANITATION", "TD-SHELTER", "TD-ENERGY", "TD-HEALTH", "TD-MAPS-COMMS"],
    "SL2": ["TD-KNOWLEDGE", "TD-TRANSPORT", "TD-ENVIRONMENT", "TD-GOV", "TD-WATER", "TD-FOOD", "TD-HEALTH"],
    "SL3": ["TD-WORKSHOP", "TD-EDUCATION", "TD-TRANSPORT", "TD-ENERGY", "TD-SEED-BANK", "TD-FERTILIZERS"],
    "SL4": ["TD-WATER-YIELD", "TD-CROP-TRIAL", "TD-SEED-REGEN", "TD-HARVEST-STORAGE", "TD-ENERGY-GENERATION", "TD-KNOWLEDGE-RESTORE"],
    "SL5": ["TD-MATERIALS-PRODUCTION", "TD-CONSTRUCTION", "TD-WORKSHOP", "TD-KNOWLEDGE", "TD-GOV-COMMUNITY"],
    "SL6": ["TD-GOV-SUCCESSION", "TD-EDUCATION-INSTRUCTOR", "TD-KNOWLEDGE-MIGRATION", "TD-PEOPLE-DEMOGRAPHY", "TD-GOV-LAW", "TD-GOV-COMMUNITY"],
}

CONDITIONAL_SERVICE_NODES = {"TD-CONSTRUCTION", "TD-FUELS", "TD-ANIMALS"}

CROSSWALK = {
    "AGR": ("TD-FOOD|TD-FERTILIZERS", "CAP-AGR-SOIL|CAP-AGR-SEED", "MOC-FOOD-AGRI", "SCI-AGRI-01|SCI-AGRI-05|SCI-AGRI-06"),
    "AIR": ("TD-VENTILATION|TD-SHELTER-COMBUSTION-AIR", "CAP-AIR", "MOC-SHELTER", "SCI-CIVIL-09"),
    "COM": ("TD-MAPS-COMMS|TD-COMMS-PACE", "CAP-COMMS", "MOC-MAPS-COMMS", "SCI-OPS-04"),
    "COMM": ("TD-GOV-COMMUNITY", "CAP-COMMUNITY", "MOC-GOVERNANCE", "SCI-OPS-12"),
    "CYB": ("TD-KNOWLEDGE-TOOLCHAINS|TD-KNOWLEDGE-HARDWARE", "CAP-SOFTWARE-READ", "MOC-KNOWLEDGE-COMPUTING", "SCI-COMP-12"),
    "DEAD": ("TD-HEALTH-DEATH|TD-SAN-HUMAN-DEATH", "CAP-DOC-IDENTITY", "MOC-HEALTH", "SCI-HEALTH-16"),
    "DOC": ("TD-GOV-BIRTH-DEATH|TD-PEOPLE-CONSENT", "CAP-DOC-IDENTITY", "MOC-GOVERNANCE", "SCI-PORT-10"),
    "EDU": ("TD-EDUCATION", "CAP-EDUCATION|CAP-SKILL-SUCCESSION", "MOC-KNOWLEDGE-COMPUTING", "SCI-EDU-01"),
    "ENE": ("TD-ENERGY", "CAP-ENERGY-CRITICAL", "MOC-ENERGY-FUELS", "SCI-ELEC-01|SCI-ELEC-10"),
    "FIN": ("TD-GOV-LEDGER|TD-GOV-TRADE", "CAP-FIN-LIFECYCLE", "MOC-GOVERNANCE", "SCI-OPS-07"),
    "FIRE": ("TD-FIRE-CO|TD-SHELTER-ALARMS|TD-SHELTER-EXTINGUISHER", "CAP-FIRE", "MOC-SHELTER", "SCI-CIVIL-12"),
    "FOOD": ("TD-FOOD|TD-FOOD-P0-RESERVE", "CAP-FOOD-NUTRITION", "MOC-FOOD-AGRI", "SCI-AGRI-09|SCI-HEALTH-07"),
    "GOV": ("TD-GOV", "CAP-GOV-SUCCESSION|CAP-GOV-SAFEGUARD", "MOC-GOVERNANCE", "SCI-OPS-01|SCI-OPS-02"),
    "HOME": ("TD-SHELTER|TD-CONSTRUCTION", "CAP-SHELTER", "MOC-SHELTER", "SCI-CIVIL-01"),
    "INFO": ("TD-KNOWLEDGE", "CAP-INFO-TRUST|CAP-ARCHIVE-RESTORE", "MOC-KNOWLEDGE-COMPUTING", "SCI-ARCH-01"),
    "LEG": ("TD-GOV-LAW|TD-PORTUGAL-LAW", "CAP-LAW-TENURE", "MOC-PORTUGAL", "SCI-PORT-01"),
    "MED": ("TD-HEALTH", "CAP-MED-PRIMARY|CAP-MED-PUBLIC-HEALTH", "MOC-HEALTH", "SCI-HEALTH-01"),
    "MED-BLS": ("TD-HEALTH-BLS-AED|TD-HEALTH-AIRWAY", "CAP-MED-PRIMARY", "MOC-HEALTH", "SCI-HEALTH-04"),
    "MED-ILL": ("TD-HEALTH-PREVENTION|TD-HEALTH-DELAYED-CARE", "CAP-MED-PRIMARY", "MOC-HEALTH", "SCI-HEALTH-02|SCI-HEALTH-05"),
    "MED-MH": ("TD-HEALTH-MENTAL-CRISIS", "CAP-MED-PRIMARY", "MOC-HEALTH", "SCI-HEALTH-08"),
    "MED-NCD": ("TD-HEALTH-MEDICATION-INVENTORY|TD-HEALTH-COLD-CHAIN", "CAP-MED-PRIMARY", "MOC-HEALTH", "SCI-HEALTH-09"),
    "MED-TRAUMA": ("TD-HEALTH-BLEED-SHOCK|TD-HEALTH-HEAD-SPINE|TD-HEALTH-FRACTURE", "CAP-MED-PRIMARY", "MOC-HEALTH", "SCI-HEALTH-04"),
    "NAV": ("TD-NAVIGATION|TD-ROUTES", "CAP-NAV", "MOC-MAPS-COMMS", "SCI-EARTH-11"),
    "PET": ("TD-ANIMALS|TD-PEOPLE-ANIMALS", "CAP-ANIMAL-CARE", "MOC-FOOD-AGRI", "SCI-HEALTH-15|SCI-AGRI-13"),
    "PPE": ("TD-HEALTH-SCENE-PPE|TD-WORKSHOP-PPE", "CAP-TOOLS", "MOC-SAFETY", "SCI-HEALTH-05"),
    "PRES": ("TD-FOOD-PRESERVATION|TD-HARVEST-STORAGE", "CAP-FOOD-NUTRITION", "MOC-FOOD-AGRI", "SCI-AGRI-09"),
    "REC": ("TD-GOV-RECOVERY|TD-GOV-RELOCATION", "CAP-RECOVERY|CAP-RELOCATION", "MOC-GOVERNANCE", "SCI-OPS-10"),
    "SAFE": ("TD-BASE-SAFETY|TD-SECURITY", "CAP-GOV-SAFEGUARD", "MOC-SAFETY", "SCI-METH-14"),
    "SAN": ("TD-SANITATION", "CAP-SANITATION", "MOC-WATER", "SCI-CIVIL-07"),
    "SHEL": ("TD-SHELTER", "CAP-SHELTER", "MOC-SHELTER", "SCI-CIVIL-01"),
    "TOOL": ("TD-WORKSHOP|TD-BASE-METROLOGY", "CAP-TOOLS|CAP-REPAIR", "MOC-WORKSHOP", "SCI-MECH-01"),
    "TRANS": ("TD-TRANSPORT", "CAP-TRANSPORT", "MOC-MAPS-COMMS", "SCI-MECH-12"),
    "WAT": ("TD-WATER", "CAP-WATER-SAFE", "MOC-WATER", "SCI-CIVIL-07|SCI-AGRI-03"),
}


def write_csv(path: Path, fieldnames: list[str], rows: list[dict[str, str]]) -> None:
    tmp = path.with_suffix(path.suffix + ".tmp")
    with tmp.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, quoting=csv.QUOTE_ALL, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)
    tmp.replace(path)


def main() -> int:
    try:
        with NODE_REGISTER.open("r", encoding="utf-8-sig", newline="") as handle:
            nodes = list(csv.DictReader(handle))
    except (OSError, csv.Error) as exc:
        print(f"planning_error {exc}", file=sys.stderr)
        return 1
    by_id = {row["node_id"]: row for row in nodes}
    if len(by_id) != len(nodes):
        print("planning_error duplicate technology node ids", file=sys.stderr)
        return 1

    plan_rows: list[dict[str, str]] = []
    node_levels: dict[str, str] = {}
    for node in nodes:
        p = priority(node)
        level = service_level(node, p)
        node_levels[node["node_id"]] = level
        plan_rows.append(
            {
                "plan_id": f"PLAN-{node['node_id']}",
                "node_id": node["node_id"],
                "priority_tier": p,
                "priority_horizon": PRIORITY_HORIZON[p],
                "earliest_service_level": level,
                "life_criticality": "IMMEDIATE_OR_SAFETY_BOUNDARY" if p == "P0_RED" else "DEFERRED_WITHIN_STATED_HORIZON",
                "build_sequence_tier": p,
                "acquisition_priority": p,
                "knowledge_priority": p,
                "safety_lane": node["safety_class"],
                "group_size_scope": "N1|N2|N3_TO_N7",
                "capacity_model": capacity_model(node),
                "capacity_value": "TBD_PERSON_AND_SITE_PROFILE",
                "capacity_unit": "TBD_BY_CAPABILITY",
                "labor_hours": "TBD",
                "failure_domain": "TBD_SITE_AND_IMPLEMENTATION",
                "redundancy_target": "TWO_PATHS_OR_EXPLICIT_RESIDUAL_RISK" if p in {"P0_RED", "P1_ORANGE"} else "TBD_BY_SERVICE_LEVEL",
                "owner_role": "UNASSIGNED",
                "backup_role": "UNASSIGNED",
                "drill_id": "NOT_ASSIGNED",
                "next_due": "TBD",
                "human_review_state": "PROVISIONAL_AUTO_REVIEW_REQUIRED",
                "release_gate": "DENY",
                "release_version": "0.5-draft",
            }
        )

    edge_rows: list[dict[str, str]] = []
    for source in nodes:
        source_id = source["node_id"]
        for index, target_id in enumerate(split_ids(source["prerequisite_node_ids"]), start=1):
            if target_id not in by_id:
                print(f"planning_error unknown target {source_id}->{target_id}", file=sys.stderr)
                return 1
            target = by_id[target_id]
            role, group, condition = edge_role(source, target)
            level = ROOT_ROLES.get(target_id, ("", node_levels[target_id]))[1] if source_id == "TD-ROOT" else node_levels[target_id]
            edge_rows.append(
                {
                    "edge_id": f"EDGE-{source_id}-{index:03d}",
                    "from_node_id": source_id,
                    "to_node_id": target_id,
                    "edge_role": role,
                    "alternative_group": group,
                    "minimum_required_count": "1" if role == "ALTERNATIVE" else "",
                    "service_level": level,
                    "applicable_if": condition,
                    "rationale": "Generated provisional semantics; human domain review required",
                    "review_state": "PROVISIONAL_AUTO_REVIEW_REQUIRED",
                    "release_gate": "DENY",
                    "release_version": "0.5-draft",
                }
            )

    service_rows: list[dict[str, str]] = []
    for level, requirements in SERVICE_REQUIREMENTS.items():
        horizon, summary = SERVICE_LEVELS[level]
        for node_id in requirements:
            if node_id not in by_id:
                print(f"planning_error service requirement missing node {node_id}", file=sys.stderr)
                return 1
            service_rows.append(
                {
                    "service_requirement_id": f"SR-{level}-{node_id}",
                    "service_level": level,
                    "time_horizon": horizon,
                    "outcome_node_id": node_id,
                    "requirement_role": "CONDITIONAL" if node_id in CONDITIONAL_SERVICE_NODES else "REQUIRED",
                    "minimum_outcome": summary,
                    "group_size_scope": "N1|N2|N3_TO_N7",
                    "capacity_basis": capacity_model(by_id[node_id]),
                    "evidence_required": "Measured capacity; duration; inventory; test; owner; backup; accepted residual risk",
                    "status": "CATALOG_ONLY_NOT_EVALUATED",
                    "human_review_state": "PROVISIONAL_AUTO_REVIEW_REQUIRED",
                    "release_gate": "DENY",
                    "release_version": "0.5-draft",
                }
            )

    crosswalk_rows = []
    for legacy_id, (technology_ids, century_ids, moc_ids, science_ids) in CROSSWALK.items():
        crosswalk_rows.append(
            {
                "crosswalk_id": f"XW-{legacy_id}",
                "legacy_capability_id": legacy_id,
                "canonical_technology_ids": technology_ids,
                "century_capability_ids": century_ids,
                "moc_ids": moc_ids,
                "science_domain_ids": science_ids,
                "mapping_status": "PROVISIONAL_HUMAN_REVIEW_REQUIRED",
                "notes": "Links scenario vocabulary to canonical capability layers; does not prove execution",
                "release_version": "0.5-draft",
            }
        )

    write_csv(
        PLAN_REGISTER,
        [
            "plan_id", "node_id", "priority_tier", "priority_horizon", "earliest_service_level",
            "life_criticality", "build_sequence_tier", "acquisition_priority", "knowledge_priority",
            "safety_lane", "group_size_scope", "capacity_model", "capacity_value", "capacity_unit",
            "labor_hours", "failure_domain", "redundancy_target", "owner_role", "backup_role", "drill_id",
            "next_due", "human_review_state", "release_gate", "release_version",
        ],
        plan_rows,
    )
    write_csv(
        EDGE_REGISTER,
        [
            "edge_id", "from_node_id", "to_node_id", "edge_role", "alternative_group",
            "minimum_required_count", "service_level", "applicable_if", "rationale", "review_state",
            "release_gate", "release_version",
        ],
        edge_rows,
    )
    write_csv(
        SERVICE_REGISTER,
        [
            "service_requirement_id", "service_level", "time_horizon", "outcome_node_id", "requirement_role",
            "minimum_outcome", "group_size_scope", "capacity_basis", "evidence_required", "status",
            "human_review_state", "release_gate", "release_version",
        ],
        service_rows,
    )
    write_csv(
        CROSSWALK_REGISTER,
        [
            "crosswalk_id", "legacy_capability_id", "canonical_technology_ids", "century_capability_ids",
            "moc_ids", "science_domain_ids", "mapping_status", "notes", "release_version",
        ],
        crosswalk_rows,
    )
    print(
        f"planning_ok nodes={len(nodes)} edges={len(edge_rows)} service_requirements={len(service_rows)} "
        f"crosswalk={len(crosswalk_rows)}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
