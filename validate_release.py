#!/usr/bin/env python3
"""Fail-closed structural validator for Autonomous Life Kit v0.4.

This script performs offline checks only. It does not fetch URLs, validate
medical content, establish legal rights, or claim physical/E5 readiness.
Run from any directory:

    python3 validate_release.py
"""

from __future__ import annotations

import csv
import hashlib
import re
import sys
import zipfile
from collections import Counter, defaultdict
from pathlib import Path
from xml.etree import ElementTree


ROOT = Path(__file__).resolve().parent
ISSUES: list[str] = []


EXPECTED_CSV: dict[str, tuple[int, int]] = {
    "accountability-log-template.csv": (4, 20),
    "action-card-register-template.csv": (1, 27),
    "animal-profile-template.csv": (1, 25),
    "archive-media-register-template.csv": (1, 27),
    "asset-component-lifecycle-template.csv": (1, 38),
    "buddy-assignment-template.csv": (7, 24),
    "card-gate-snapshot-template.csv": (1, 30),
    "cascade-register-template.csv": (12, 26),
    "century-capability-register.csv": (32, 20),
    "century-gate-snapshot-template.csv": (1, 34),
    "climate-pathway-register-template.csv": (1, 29),
    "competency-lineage-template.csv": (1, 24),
    "decision-class-register.csv": (20, 5),
    "dependent-care-authorization-template.csv": (1, 22),
    "external-contact-template.csv": (1, 27),
    "format-migration-register-template.csv": (1, 24),
    "governance-policy-register-template.csv": (1, 24),
    "group-composition-snapshot-template.csv": (1, 19),
    "group-function-assignment-template.csv": (49, 26),
    "group-operational-roster-template.csv": (7, 16),
    "group-profile-template.csv": (7, 12),
    "group-revision-register-template.csv": (8, 16),
    "group-roster-template.csv": (7, 56),
    "horizon-register.csv": (6, 15),
    "incident-log-template.csv": (4, 59),
    "institution-register-template.csv": (1, 22),
    "inventory-template.csv": (5, 59),
    "knowledge-succession-register-template.csv": (1, 21),
    "land-parcel-register-template.csv": (1, 32),
    "legacy-scenario-map.csv": (25, 5),
    "map-register-template.csv": (8, 64),
    "offline-corpus-manifest.csv": (79, 37),
    "offline-restore-test-template.csv": (1, 28),
    "offline-storage-plan-template.csv": (1, 23),
    "population-capacity-snapshot-template.csv": (1, 26),
    "practical-science-domain-register.csv": (239, 16),
    "practical-science-instrument-register.csv": (73, 19),
    "practical-science-learning-paths.csv": (16, 13),
    "practical-science-package-register.csv": (259, 38),
    "practical-science-project-register.csv": (239, 29),
    "practical-science-protocol-template.csv": (1, 24),
    "practical-science-raw-log-template.csv": (12, 17),
    "practical-science-safety-gates.csv": (17, 6),
    "resource-scaling-template.csv": (10, 43),
    "resource-transaction-log-template.csv": (2, 17),
    "role-gate-record-template.csv": (1, 26),
    "route-register-template.csv": (6, 67),
    "scenario-register.csv": (133, 31),
    "seed-accession-template.csv": (1, 30),
    "site-register-template.csv": (7, 46),
    "soil-monitoring-template.csv": (1, 26),
    "source-manifest.csv": (39, 20),
    "succession-register-template.csv": (1, 26),
    "water-source-capacity-template.csv": (1, 30),
}


def issue(message: str) -> None:
    ISSUES.append(message)


def split_ids(value: str) -> list[str]:
    return [part.strip() for part in value.split("|") if part.strip()]


def unresolved(value: str) -> bool:
    return not value or value == "TBD" or value.startswith("TBD_")


tables: dict[str, list[dict[str, str]]] = {}
headers: dict[str, list[str]] = {}
primary_overrides = {
    "accountability-log-template.csv": "accountability_entry_id",
    "incident-log-template.csv": "entry_id",
    "resource-transaction-log-template.csv": "transaction_id",
}

actual_csv = {path.name for path in ROOT.glob("*.csv")}
if actual_csv != set(EXPECTED_CSV):
    issue(
        "CSV set mismatch: missing="
        f"{sorted(set(EXPECTED_CSV) - actual_csv)} extra="
        f"{sorted(actual_csv - set(EXPECTED_CSV))}"
    )

for filename, (expected_rows, expected_fields) in EXPECTED_CSV.items():
    path = ROOT / filename
    if not path.is_file():
        continue
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        raw_rows = list(csv.reader(handle))
    if not raw_rows:
        issue(f"{filename}: empty CSV")
        continue
    header = raw_rows[0]
    headers[filename] = header
    if len(header) != expected_fields:
        issue(f"{filename}: expected {expected_fields} fields, found {len(header)}")
    if len(raw_rows) - 1 != expected_rows:
        issue(f"{filename}: expected {expected_rows} data rows, found {len(raw_rows) - 1}")
    for line_no, row in enumerate(raw_rows[1:], start=2):
        if len(row) != len(header):
            issue(f"{filename}:{line_no}: width {len(row)} != header {len(header)}")
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        rows = list(csv.DictReader(handle))
    tables[filename] = rows
    if header:
        primary = primary_overrides.get(filename, header[0])
        values = [row.get(primary, "") for row in rows]
        if any(not value for value in values):
            issue(f"{filename}: blank primary key in {primary}")
        duplicates = sorted(value for value, count in Counter(values).items() if count > 1)
        if duplicates:
            issue(f"{filename}: duplicate {primary}: {duplicates}")


def ids(filename: str) -> set[str]:
    if filename not in tables or not headers.get(filename):
        return set()
    key = primary_overrides.get(filename, headers[filename][0])
    return {row[key] for row in tables[filename]}


def check_refs(filename: str, field: str, allowed: set[str]) -> None:
    for line_no, row in enumerate(tables.get(filename, []), start=2):
        if field not in row:
            issue(f"{filename}: missing reference field {field}")
            return
        for value in split_ids(row[field]):
            if field == "scenario_codes" and value == "ALL":
                continue
            if not unresolved(value) and value not in allowed:
                issue(f"{filename}:{line_no}: unresolved {field}={value}")


# Canonical horizons: exact boundaries and no accidental E5 inheritance.
horizons = tables.get("horizon-register.csv", [])
expected_horizon_rows = [
    ("E0", "0", "PT0S", "YES", "PT12H", "YES"),
    ("E1", "1", "PT12H", "NO", "P3D", "YES"),
    ("E2", "2", "P3D", "NO", "P14D", "YES"),
    ("E3", "3", "P14D", "NO", "P90D", "YES"),
    ("E4", "4", "P90D", "NO", "P15Y", "NO"),
    ("E5", "5", "P15Y", "YES", "P100Y", "YES"),
]
for row, expected in zip(horizons, expected_horizon_rows):
    actual = tuple(
        row[field]
        for field in (
            "horizon_code",
            "ordinal",
            "lower_bound_iso8601",
            "lower_inclusive",
            "upper_bound_iso8601",
            "upper_inclusive",
        )
    )
    if actual != expected:
        issue(f"horizon-register.csv: boundary mismatch {actual} != {expected}")
if horizons and horizons[-1]["allowed_claim"] != "ALLOW_FOR_CURRENT_REVIEW_PERIOD":
    issue("E5 allowed_claim must be ALLOW_FOR_CURRENT_REVIEW_PERIOD")

for filename in ("scenario-register.csv", "resource-scaling-template.csv"):
    field = "horizon_scope" if filename.startswith("scenario") else "horizon_code"
    for line_no, row in enumerate(tables.get(filename, []), start=2):
        values = split_ids(row[field].replace("_", "|"))
        if "ALL" in values or row[field] == "ALL":
            issue(f"{filename}:{line_no}: bare ALL forbidden in {field}")


# Scenario register remains an index; only new GEN rows enter E5.
scenario_rows = tables.get("scenario-register.csv", [])
family_counts = Counter(row["family"] for row in scenario_rows)
expected_families = {
    "BIO": 8,
    "CYB": 8,
    "ENV": 6,
    "GEN": 16,
    "INF": 13,
    "MED": 24,
    "NAT": 18,
    "OPS": 7,
    "SEC": 8,
    "SOC": 8,
    "TEC": 17,
}
if family_counts != Counter(expected_families):
    issue(f"scenario family distribution mismatch: {dict(sorted(family_counts.items()))}")
for line_no, row in enumerate(scenario_rows, start=2):
    is_gen = row["scenario_id"].startswith("GEN-")
    if row["card_status"] != "INDEX_ONLY":
        issue(f"scenario-register.csv:{line_no}: card_status must be INDEX_ONLY")
    if row["content_review_state"] != "NOT_REVIEWED":
        issue(f"scenario-register.csv:{line_no}: content must remain NOT_REVIEWED")
    if row["decision_provenance_state"] != "NOT_LINKED":
        issue(f"scenario-register.csv:{line_no}: provenance must remain NOT_LINKED")
    if is_gen:
        if row["family"] != "GEN" or row["horizon_scope"] != "E5" or row["e5_review_state"] != "ARCHITECTURE_ONLY":
            issue(f"scenario-register.csv:{line_no}: invalid GEN/E5 semantics")
    elif row["family"] == "GEN" or "E5" in row["horizon_scope"] or row["e5_review_state"] != "NOT_REVIEWED":
        issue(f"scenario-register.csv:{line_no}: legacy row accidentally expanded to E5")
    if row["decision_sequence"].split(">", 1)[0] != row["first_decision_class"]:
        issue(f"scenario-register.csv:{line_no}: first decision mismatch")

for line_no, row in enumerate(tables.get("resource-scaling-template.csv", []), start=2):
    if "E5" in row["horizon_code"] or row["e5_review_state"] != "NOT_REVIEWED":
        issue(f"resource-scaling-template.csv:{line_no}: accidental E5 claim")


# Key cross-register references.
scenario_ids = ids("scenario-register.csv")
decision_ids = ids("decision-class-register.csv")
source_ids = ids("source-manifest.csv")
map_ids = ids("map-register-template.csv")
route_ids = ids("route-register-template.csv")
site_ids = ids("site-register-template.csv")
person_ids = ids("group-roster-template.csv")
profile_ids = ids("group-profile-template.csv")
animal_ids = ids("animal-profile-template.csv")
revision_ids = ids("group-revision-register-template.csv")

for filename, field, allowed in [
    ("scenario-register.csv", "first_decision_class", decision_ids),
    ("scenario-register.csv", "source_ids", source_ids),
    ("scenario-register.csv", "map_ids", map_ids),
    ("scenario-register.csv", "route_ids", route_ids),
    ("scenario-register.csv", "site_ids", site_ids),
    ("map-register-template.csv", "scenario_codes", scenario_ids),
    ("map-register-template.csv", "source_id", source_ids),
    ("map-register-template.csv", "route_ids", route_ids),
    ("route-register-template.csv", "scenario_codes", scenario_ids),
    ("route-register-template.csv", "map_ids", map_ids),
    ("route-register-template.csv", "origin_id", site_ids),
    ("route-register-template.csv", "destination_id", site_ids),
    ("route-register-template.csv", "alternate_route_id", route_ids),
    ("site-register-template.csv", "scenario_codes", scenario_ids),
    ("site-register-template.csv", "source_id", source_ids),
    ("site-register-template.csv", "map_ids", map_ids),
    ("site-register-template.csv", "route_ids", route_ids),
    ("cascade-register-template.csv", "from_scenario_id", scenario_ids),
    ("cascade-register-template.csv", "to_scenario_id", scenario_ids),
    ("cascade-register-template.csv", "map_ids", map_ids),
    ("cascade-register-template.csv", "relation_source_ids", source_ids),
    ("cascade-register-template.csv", "action_source_ids", source_ids),
    ("group-profile-template.csv", "active_person_ids", person_ids),
    ("group-profile-template.csv", "animal_entity_ids", animal_ids),
    ("group-profile-template.csv", "profile_revision_id", revision_ids),
]:
    check_refs(filename, field, allowed)


# N=1..7 cardinality and assignment confinement.
profile_people: dict[str, set[str]] = {}
for row in tables.get("group-profile-template.csv", []):
    members = set(split_ids(row["active_person_ids"]))
    profile_people[row["group_profile_id"]] = members
    expected_n = int(row["group_profile_id"].removeprefix("GP-N"))
    if int(row["human_count"]) != expected_n or len(members) != expected_n:
        issue(f"{row['group_profile_id']}: profile cardinality mismatch")

assignment_counts: Counter[str] = Counter()
for line_no, row in enumerate(tables.get("group-function-assignment-template.csv", []), start=2):
    profile = row["group_profile_id"]
    assignment_counts[profile] += 1
    if profile not in profile_people:
        issue(f"group-function-assignment-template.csv:{line_no}: unknown profile {profile}")
        continue
    for field in ("primary_person_id", "backup_person_id", "successor_person_ids"):
        for person in split_ids(row[field]):
            if person not in profile_people[profile]:
                issue(f"group-function-assignment-template.csv:{line_no}: {person} outside {profile}")
    if row["assignment_status"] != "PLANNED" or row["assignment_activation_gate_state"] != "BLOCKED":
        issue(f"group-function-assignment-template.csv:{line_no}: assignment not fail-closed")
for profile in profile_ids:
    if assignment_counts[profile] != 7:
        issue(f"{profile}: expected 7 function assignments, found {assignment_counts[profile]}")

buddy_coverage: dict[int, list[str]] = defaultdict(list)
for row in tables.get("buddy-assignment-template.csv", []):
    for scope in split_ids(row["activation_scope"]):
        if re.fullmatch(r"N[1-7]", scope):
            buddy_coverage[int(scope[1:])].extend(split_ids(row["member_person_ids"]))
for n in range(1, 8):
    expected_people = [f"P{i:02d}" for i in range(1, n + 1)]
    if sorted(buddy_coverage[n]) != expected_people:
        issue(f"N{n}: buddy coverage mismatch")


# E5 examples remain fail-closed.
for row in tables.get("century-capability-register.csv", []):
    if row["evidence_state"] != "MISSING" or row["lifecycle_state"] != "PLANNED" or row["gate_decision"] != "DENY":
        issue(f"century-capability-register.csv:{row['capability_id']}: unsafe example state")

fail_closed_fields = {
    "century-gate-snapshot-template.csv": {"all_required_gates_state": "BLOCKED", "computed_decision": "DENY"},
    "institution-register-template.csv": {"institution_status": "DRAFT", "gate_decision": "DENY"},
    "governance-policy-register-template.csv": {"policy_state": "NOT_ADOPTED", "gate_decision": "DENY"},
    "succession-register-template.csv": {"succession_gate_state": "BLOCKED", "gate_decision": "DENY"},
    "land-parcel-register-template.csv": {"tenure_gate_state": "BLOCKED", "gate_decision": "DENY"},
    "water-source-capacity-template.csv": {"gate_decision": "DENY"},
    "soil-monitoring-template.csv": {"result_state": "NO_SAMPLE", "gate_decision": "DENY"},
    "seed-accession-template.csv": {"accession_status": "CANDIDATE", "gate_decision": "DENY"},
    "asset-component-lifecycle-template.csv": {"lifecycle_state": "PLANNED", "gate_decision": "DENY"},
    "competency-lineage-template.csv": {"competency_gate_state": "BLOCKED", "gate_decision": "DENY"},
    "population-capacity-snapshot-template.csv": {"snapshot_state": "DRAFT", "gate_decision": "DENY"},
    "climate-pathway-register-template.csv": {"pathway_state": "CANDIDATE", "gate_decision": "DENY"},
    "archive-media-register-template.csv": {"media_state": "PLANNED", "gate_decision": "DENY"},
    "format-migration-register-template.csv": {"migration_state": "PLANNED", "gate_decision": "DENY"},
    "offline-restore-test-template.csv": {"test_state": "PLANNED", "gate_decision": "DENY"},
    "offline-storage-plan-template.csv": {"plan_state": "PLANNED", "gate_decision": "DENY"},
    "knowledge-succession-register-template.csv": {"succession_state": "BLOCKED", "gate_decision": "DENY"},
}
for filename, checks in fail_closed_fields.items():
    for line_no, row in enumerate(tables.get(filename, []), start=2):
        for field, expected in checks.items():
            if row[field] != expected:
                issue(f"{filename}:{line_no}: {field}={row[field]} expected {expected}")


# Offline candidates are a queue, not a downloaded corpus.
offline_rows = tables.get("offline-corpus-manifest.csv", [])
blocked_packages = {"PKG-DGS-PT", "PKG-INFARMED", "PKG-DRE-PT"}
for line_no, row in enumerate(offline_rows, start=2):
    blocked = row["package_id"] in blocked_packages
    expected_download = "DO_NOT_INGEST" if blocked else "NOT_DOWNLOADED"
    if row["download_state"] != expected_download:
        issue(f"offline-corpus-manifest.csv:{line_no}: unexpected download_state")
    if blocked and (
        row["license_review_state"] != "LOCAL_REPRODUCTION_RIGHTS_UNVERIFIED"
        or row["redistribution_state"] != "DO_NOT_INGEST"
    ):
        issue(f"offline-corpus-manifest.csv:{line_no}: protected package not blocked")
    for field, expected in (
        ("content_review_state", "NOT_REVIEWED"),
        ("section_review_state", "NOT_REVIEWED"),
        ("offline_open_state", "NOT_TESTED"),
        ("search_index_state", "NOT_INDEXED"),
    ):
        if row[field] != expected:
            issue(f"offline-corpus-manifest.csv:{line_no}: {field}={row[field]}")
    for field in ("downloaded_version", "retrieved_at", "local_path", "byte_size", "sha256"):
        if row[field]:
            issue(f"offline-corpus-manifest.csv:{line_no}: premature {field}")


# Practical science remains a measured framework and acquisition backlog.
science_domains = tables.get("practical-science-domain-register.csv", [])
science_packages = tables.get("practical-science-package-register.csv", [])
science_projects = tables.get("practical-science-project-register.csv", [])
science_instruments = tables.get("practical-science-instrument-register.csv", [])
science_gates = tables.get("practical-science-safety-gates.csv", [])
science_paths = tables.get("practical-science-learning-paths.csv", [])

expected_science_groups = {
    "AGRI": 16,
    "ARCH": 12,
    "CHEM": 16,
    "CIVIL": 16,
    "COMP": 17,
    "EARTH": 14,
    "EDU": 12,
    "ELEC": 17,
    "HEALTH": 16,
    "LIFE": 16,
    "MATH": 18,
    "MECH": 16,
    "METH": 14,
    "OPS": 12,
    "PHYS": 17,
    "PORT": 10,
}
expected_science_safety = {
    "S0_OBSERVE_READ": 116,
    "S1_LOW_RISK_HOUSEHOLD": 75,
    "S2_TRAINED_SUPERVISED": 33,
    "S3_LICENSED_PROFESSIONAL": 11,
    "S4_REFERENCE_ONLY_PROHIBITED_HOUSEHOLD": 4,
}
if Counter(row["group_code"] for row in science_domains) != Counter(expected_science_groups):
    issue("practical-science-domain-register.csv: group distribution mismatch")
if Counter(row["safety_class"] for row in science_domains) != Counter(expected_science_safety):
    issue("practical-science-domain-register.csv: safety distribution mismatch")
for line_no, row in enumerate(science_domains, start=2):
    if row["implementation_state"] != "FRAMEWORK_ONLY_NOT_TRAINED":
        issue(f"practical-science-domain-register.csv:{line_no}: premature implementation state")
    if row["release_version"] != "0.4":
        issue(f"practical-science-domain-register.csv:{line_no}: release_version must be 0.4")

science_domain_ids = {row["domain_id"] for row in science_domains}
science_prerequisites: dict[str, list[str]] = {}
for line_no, row in enumerate(science_domains, start=2):
    prerequisites = split_ids(row["prerequisite_domains"])
    if len(prerequisites) != len(set(prerequisites)):
        issue(f"practical-science-domain-register.csv:{line_no}: duplicate prerequisite")
    for prerequisite in prerequisites:
        if prerequisite not in science_domain_ids:
            issue(f"practical-science-domain-register.csv:{line_no}: unknown prerequisite {prerequisite}")
        if prerequisite == row["domain_id"]:
            issue(f"practical-science-domain-register.csv:{line_no}: self prerequisite")
    science_prerequisites[row["domain_id"]] = prerequisites

visit_state: dict[str, int] = {}


def visit_science_domain(domain_id: str, trail: list[str]) -> None:
    state = visit_state.get(domain_id, 0)
    if state == 1:
        issue(f"practical science prerequisite cycle: {' > '.join(trail + [domain_id])}")
        return
    if state == 2:
        return
    visit_state[domain_id] = 1
    for prerequisite in science_prerequisites.get(domain_id, []):
        if prerequisite in science_prerequisites:
            visit_science_domain(prerequisite, trail + [domain_id])
    visit_state[domain_id] = 2


for science_domain_id in sorted(science_domain_ids):
    visit_science_domain(science_domain_id, [])

allowed_rights_states = {
    "DO_NOT_INGEST_UNTIL_RIGHTS_CLEARED",
    "LOCAL_AUTHORING_REQUIRED",
    "LOCAL_REPRODUCTION_RIGHTS_UNVERIFIED",
    "REFERENCE_ONLY_NO_COPY",
    "REQUIRES_ASSET_INVENTORY",
    "REQUIRES_ITEM_REVIEW",
    "REQUIRES_LOCALIZATION",
    "REQUIRES_PERSONALIZATION",
}
expected_science_tiers = {"L0": 10, "L1": 72, "L2": 135, "L3": 28, "L4": 14}
if Counter(row["tier"] for row in science_packages) != Counter(expected_science_tiers):
    issue("practical-science-package-register.csv: tier distribution mismatch")
for line_no, row in enumerate(science_packages, start=2):
    expected_acquisition = "NOT_CREATED" if row["rights_state"] == "LOCAL_AUTHORING_REQUIRED" else "NOT_DOWNLOADED"
    for field, expected in (
        ("release_state", "CANDIDATE"),
        ("acquisition_state", expected_acquisition),
        ("content_review_state", "NOT_REVIEWED"),
        ("offline_open_state", "NOT_TESTED"),
    ):
        if row[field] != expected:
            issue(f"practical-science-package-register.csv:{line_no}: {field}={row[field]}")
    if row["rights_state"] not in allowed_rights_states:
        issue(f"practical-science-package-register.csv:{line_no}: unknown rights_state")
    for field in ("sha256", "local_path", "retrieved_at", "review_due", "priority_score"):
        if row[field]:
            issue(f"practical-science-package-register.csv:{line_no}: premature {field}")

science_url_classes = Counter(
    "HTTP" if row["canonical_url"].startswith(("http://", "https://"))
    else "LOCAL" if row["canonical_url"].startswith("local://")
    else "TBD"
    for row in science_packages
)
if science_url_classes != Counter({"HTTP": 254, "TBD": 3, "LOCAL": 2}):
    issue(f"practical-science-package-register.csv: URL class mismatch {dict(science_url_classes)}")

safety_rank = {
    "S0_OBSERVE_READ": 0,
    "S1_LOW_RISK_HOUSEHOLD": 1,
    "S2_TRAINED_SUPERVISED": 2,
    "S3_LICENSED_PROFESSIONAL": 3,
    "S4_REFERENCE_ONLY_PROHIBITED_HOUSEHOLD": 4,
}
science_by_url: dict[str, list[dict[str, str]]] = defaultdict(list)
for row in science_packages:
    if row["canonical_url"].startswith(("http://", "https://")):
        science_by_url[row["canonical_url"].rstrip("/").lower()].append(row)
for canonical_url, rows in science_by_url.items():
    observed = {row["safety_class"] for row in rows}
    if len(observed) > 1:
        issue(f"practical-science-package-register.csv: safety floor differs for duplicate URL {canonical_url}")
    if any(value not in safety_rank for value in observed):
        issue(f"practical-science-package-register.csv: unknown package safety class at {canonical_url}")

mode_for_safety = {
    "S0_OBSERVE_READ": "OBSERVATION_DATA_OR_CALCULATION",
    "S1_LOW_RISK_HOUSEHOLD": "LOW_RISK_BENCH_OR_FIELD",
    "S2_TRAINED_SUPERVISED": "SUPERVISED_DEMONSTRATION_ONLY",
    "S3_LICENSED_PROFESSIONAL": "DATASET_SIMULATION_OR_PRO_OBSERVATION_ONLY",
    "S4_REFERENCE_ONLY_PROHIBITED_HOUSEHOLD": "REFERENCE_ONLY_NO_EXECUTION",
}
domain_by_id = {row["domain_id"]: row for row in science_domains}
science_package_ids = {row["package_id"] for row in science_packages}
for line_no, row in enumerate(science_projects, start=2):
    domain = domain_by_id.get(row["domain_id"])
    if not domain:
        issue(f"practical-science-project-register.csv:{line_no}: unknown domain_id")
    elif row["safety_class"] != domain["safety_class"]:
        issue(f"practical-science-project-register.csv:{line_no}: safety differs from domain")
    if row["mode"] != mode_for_safety.get(row["safety_class"]):
        issue(f"practical-science-project-register.csv:{line_no}: unsafe mode for safety class")
    if row["status"] != "DESIGN_ONLY_NOT_EXECUTED":
        issue(f"practical-science-project-register.csv:{line_no}: project execution overclaim")
    if row["source_binding_state"] != "PROVISIONAL_TOPIC_CANDIDATES_NOT_METHOD_REVIEWED":
        issue(f"practical-science-project-register.csv:{line_no}: source binding overclaim")
    if row["execution_gate"] != "BLOCKED_UNTIL_EXACT_METHOD_SOURCE_SAFETY_AND_LOCAL_REVIEW":
        issue(f"practical-science-project-register.csv:{line_no}: execution gate not blocked")
    linked_packages = split_ids(row["linked_package_ids"])
    if not linked_packages:
        issue(f"practical-science-project-register.csv:{line_no}: no topical source candidate")
    for package_id in linked_packages:
        if package_id not in science_package_ids:
            issue(f"practical-science-project-register.csv:{line_no}: unknown package {package_id}")
    if row["safety_class"] in {"S1_LOW_RISK_HOUSEHOLD", "S2_TRAINED_SUPERVISED"}:
        for field, prefix in (
            ("inputs_tools", "TBD_NON_EXECUTABLE:"),
            ("expected_pattern", "TBD_BEFORE_EXECUTION_FROM_EXACT_METHOD:"),
            ("uncertainty_method", "TBD_METHOD_SPECIFIC:"),
            ("waste_disposal", "TBD_ITEM_SPECIFIC_AND_LOCAL:"),
        ):
            if not row[field].startswith(prefix):
                issue(f"practical-science-project-register.csv:{line_no}: {field} lost fail-closed placeholder")
    if row["release_version"] != "0.4":
        issue(f"practical-science-project-register.csv:{line_no}: release_version must be 0.4")

project_by_domain = {row["domain_id"]: row for row in science_projects}
for domain_id in ("SCI-CHEM-10", "SCI-CHEM-12", "SCI-ELEC-01", "SCI-AGRI-16"):
    if project_by_domain.get(domain_id, {}).get("safety_class") != "S2_TRAINED_SUPERVISED":
        issue(f"practical-science-project-register.csv: {domain_id} must remain S2")
for domain_id in ("SCI-PHYS-15", "SCI-PHYS-16", "SCI-ELEC-01", "SCI-ELEC-02"):
    measurement = project_by_domain.get(domain_id, {}).get("raw_measurements", "")
    if "5 V" not in measurement or "100 mA" not in measurement:
        issue(f"practical-science-project-register.csv: {domain_id} missing explicit low-energy boundary")
if project_by_domain.get("SCI-AGRI-16", {}).get("linked_package_ids") != "PSP-046":
    issue("practical-science-project-register.csv: canning project not bound to PSP-046 candidate")

for line_no, row in enumerate(science_instruments, start=2):
    if row["status"] != "CANDIDATE_NOT_INVENTORIED":
        issue(f"practical-science-instrument-register.csv:{line_no}: instrument inventory overclaim")
    if row["release_version"] != "0.4":
        issue(f"practical-science-instrument-register.csv:{line_no}: release_version must be 0.4")
    for field in ("range_hint", "resolution_hint", "reference_required"):
        if not row[field].startswith("TBD_PER_EXACT_"):
            issue(f"practical-science-instrument-register.csv:{line_no}: {field} overclaims exact specification")

instrument_by_id = {row["instrument_id"]: row for row in science_instruments}
for instrument_id in ("INS-033", "INS-051"):
    if instrument_by_id.get(instrument_id, {}).get("safety_class") != "S2_TRAINED_SUPERVISED":
        issue(f"practical-science-instrument-register.csv: {instrument_id} must remain S2")

expected_gate_ids = {f"SG-{n:02d}" for n in range(1, 18)}
if ids("practical-science-safety-gates.csv") != expected_gate_ids:
    issue("practical-science-safety-gates.csv: gate ID set mismatch")
for line_no, row in enumerate(science_gates, start=2):
    if row["safety_class"] not in {"S3_LICENSED_PROFESSIONAL", "S4_REFERENCE_ONLY_PROHIBITED_HOUSEHOLD"}:
        issue(f"practical-science-safety-gates.csv:{line_no}: gate not fail-closed")
    if row["release_version"] != "0.4":
        issue(f"practical-science-safety-gates.csv:{line_no}: release_version must be 0.4")

if {row["group_code"] for row in science_paths} != set(expected_science_groups):
    issue("practical-science-learning-paths.csv: group coverage mismatch")
for line_no, row in enumerate(science_paths, start=2):
    if row["status"] != "CURRICULUM_DESIGN_ONLY":
        issue(f"practical-science-learning-paths.csv:{line_no}: curriculum overclaim")

protocol_rows = tables.get("practical-science-protocol-template.csv", [])
for line_no, row in enumerate(protocol_rows, start=2):
    if row["result"] != "NOT_RUN" or row["interpretation"] != "NOT_RUN":
        issue(f"practical-science-protocol-template.csv:{line_no}: example must remain NOT_RUN")
    if row["release_state"] != "TEMPLATE_EXAMPLE_NOT_EXECUTED" or row["evidence_hash"]:
        issue(f"practical-science-protocol-template.csv:{line_no}: premature evidence")
    if "35–40 °C" not in row["question"] or ">40 °C" not in row["stop_conditions"]:
        issue(f"practical-science-protocol-template.csv:{line_no}: warm-water safety boundary missing")
    if row["hazards"].startswith(("не использовать", "STOP")):
        issue(f"practical-science-protocol-template.csv:{line_no}: hazards/controls semantics conflated")

for line_no, row in enumerate(tables.get("practical-science-raw-log-template.csv", []), start=2):
    if row["experiment_id"] != "TBD" or row["row_lock_state"] != "BLANK_TEMPLATE":
        issue(f"practical-science-raw-log-template.csv:{line_no}: row is not a blank template")
    for field in ("timestamp_iso8601", "operator_id", "independent_value", "dependent_value", "photo_or_file_ref"):
        if row[field]:
            issue(f"practical-science-raw-log-template.csv:{line_no}: premature {field}")


# Local links and standalone visualization hash.
markdown_link = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
html_link = re.compile(r"href=[\"']([^\"']+)[\"']", re.IGNORECASE)
for path in sorted(ROOT.glob("*.md")):
    text = path.read_text(encoding="utf-8")
    for target in markdown_link.findall(text):
        target = target.strip().strip("<>")
        if target.startswith(("http://", "https://", "mailto:", "#")):
            continue
        local = target.split("#", 1)[0]
        if local and not (ROOT / local).exists():
            issue(f"{path.name}: unresolved Markdown link {target}")
for path in sorted(ROOT.glob("*.html")):
    text = path.read_text(encoding="utf-8")
    for target in html_link.findall(text):
        if target.startswith(("http://", "https://", "mailto:", "#", "data:")):
            continue
        local = target.split("#", 1)[0]
        if local and not (ROOT / local).exists():
            issue(f"{path.name}: unresolved HTML link {target}")

visualization = ROOT / "framework-visualization.html"
visualization_qa = ROOT / "VISUALIZATION_QA.md"
if not visualization.is_file() or not visualization_qa.is_file():
    issue("visualization or VISUALIZATION_QA.md missing")
else:
    digest = hashlib.sha256(visualization.read_bytes()).hexdigest()
    if digest not in visualization_qa.read_text(encoding="utf-8"):
        issue("visualization SHA-256 does not match VISUALIZATION_QA.md")

for required in ("START_HERE.txt", "START_HERE.html", "offline_library.py"):
    if not (ROOT / required).is_file():
        issue(f"missing required offline entry/tool: {required}")
for python_file in ROOT.glob("*.py"):
    try:
        compile(python_file.read_text(encoding="utf-8"), str(python_file), "exec")
    except SyntaxError as exc:
        issue(f"{python_file.name}: syntax error: {exc}")

science_workbook = ROOT / "practical-science-preservation-atlas.xlsx"
expected_workbook_sheets = [
    "Overview",
    "Domains",
    "Packages",
    "Projects",
    "Instruments",
    "Safety Gates",
    "Learning Paths",
    "Protocol",
    "Raw Log",
]
if not science_workbook.is_file():
    issue("practical science workbook missing")
else:
    try:
        with zipfile.ZipFile(science_workbook) as archive:
            workbook_xml = ElementTree.fromstring(archive.read("xl/workbook.xml"))
            ns = {"x": "http://schemas.openxmlformats.org/spreadsheetml/2006/main"}
            sheet_names = [element.attrib["name"] for element in workbook_xml.findall("x:sheets/x:sheet", ns)]
            if sheet_names != expected_workbook_sheets:
                issue(f"practical science workbook sheets mismatch: {sheet_names}")
            formula_count = 0
            for name in archive.namelist():
                if re.fullmatch(r"xl/worksheets/sheet\d+\.xml", name):
                    sheet_xml = ElementTree.fromstring(archive.read(name))
                    formula_count += len(sheet_xml.findall(".//x:f", ns))
            # 9 dashboard KPIs + 259 per-package priority formulas.
            if formula_count != 268:
                issue(f"practical science workbook formula count: expected 268, found {formula_count}")
    except (KeyError, OSError, zipfile.BadZipFile, ElementTree.ParseError) as exc:
        issue(f"practical science workbook invalid: {exc}")


expected_suffix_counts = {".md": 24, ".csv": 54, ".html": 2, ".py": 2, ".txt": 1, ".xlsx": 1}
actual_suffix_counts = Counter(path.suffix for path in ROOT.iterdir() if path.is_file())
for suffix, expected in expected_suffix_counts.items():
    if actual_suffix_counts[suffix] != expected:
        issue(f"file count {suffix}: expected {expected}, found {actual_suffix_counts[suffix]}")
if sum(actual_suffix_counts.values()) != 84:
    issue(f"total file count: expected 84, found {sum(actual_suffix_counts.values())}")


print(
    "release_summary "
    f"files={sum(actual_suffix_counts.values())} csv={actual_suffix_counts['.csv']} "
    f"scenarios={len(scenario_rows)} capabilities={len(tables.get('century-capability-register.csv', []))} "
    f"offline_candidates={len(offline_rows)} science_domains={len(science_domains)} "
    f"science_packages={len(science_packages)} science_projects={len(science_projects)} "
    f"science_instruments={len(science_instruments)} issues={len(ISSUES)}"
)
for message in ISSUES:
    print(f"ISSUE\t{message}")
if ISSUES:
    print("result=FAIL")
    raise SystemExit(1)
print("result=PASS")
