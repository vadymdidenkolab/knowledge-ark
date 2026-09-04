#!/usr/bin/env python3
"""Fail-closed structural checks for the technology dependency graph.

This validator proves only that the graph is internally coherent and that
high-risk nodes cannot be accidentally marked as household-executable.  It
does not prove that a source is correct, an item exists, a person is trained,
or a process is safe in a particular jurisdiction or location.
"""

from __future__ import annotations

import csv
from collections import Counter, defaultdict
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parent
REGISTER = ROOT / "technology-dependency-register.csv"
EDGE_REGISTER = ROOT / "technology-dependency-edges.csv"
PLAN_REGISTER = ROOT / "technology-node-planning-register.csv"
SERVICE_REGISTER = ROOT / "technology-service-level-register.csv"
CROSSWALK_REGISTER = ROOT / "capability-crosswalk.csv"
PAYLOAD_SOURCE_CROSSWALK = ROOT / "payload-source-crosswalk.csv"
PAYLOAD_REGISTER = ROOT / "offline-library" / "offline-payload-register.csv"

SOURCE_ID_REGISTERS = [
    ("source-manifest.csv", "id"),
    ("offline-corpus-manifest.csv", "package_id"),
    ("practical-science-package-register.csv", "package_id"),
    ("offline-library/offline-payload-register.csv", "payload_id"),
    ("practical-science-safety-gates.csv", "gate_id"),
]

EXPECTED_FIELDS = [
    "node_id",
    "parent_id",
    "domain",
    "node_type",
    "title_ru",
    "outcome",
    "safety_class",
    "execution_policy",
    "prerequisite_node_ids",
    "source_package_ids",
    "materials_tools_state",
    "instrument_ids",
    "measurement_acceptance",
    "calibration_reference",
    "drawings_bom_state",
    "localization_state",
    "waste_storage",
    "stop_conditions",
    "maintenance_spares",
    "successor_proof",
    "evidence_required",
    "evidence_state",
    "capability_status",
    "release_gate",
    "notes",
    "release_version",
]

NODE_TYPES = {
    "OUTCOME",
    "KNOWLEDGE",
    "SITE_DATA",
    "MATERIAL",
    "TOOL",
    "INSTRUMENT",
    "DRAWING",
    "PROCESS",
    "TEST",
    "MAINTENANCE",
    "TRAINING",
    "GOVERNANCE",
    "HAZARD_BOUNDARY",
}

SAFETY_CLASSES = {
    "S0_OBSERVE_READ",
    "S1_LOW_RISK_HOUSEHOLD",
    "S2_TRAINED_SUPERVISED",
    "S3_LICENSED_PROFESSIONAL",
    "S4_REFERENCE_ONLY_PROHIBITED_HOUSEHOLD",
}

EXECUTION_POLICIES = {
    "HOUSEHOLD_S0",
    "HOUSEHOLD_S1_AFTER_GATE",
    "TRAINED_SUPERVISED",
    "LICENSED_ONLY",
    "REFERENCE_ONLY_NO_BUILD",
}

EVIDENCE_STATES = {
    "MISSING",
    "ARCHITECTURE_ONLY",
    "LOCAL_UNREVIEWED",
    "VERIFIED_LOCAL",
    "TESTED",
    "SUCCESSOR_REPEATED",
    "BOUNDARY_DEFINED",
}

CAPABILITY_STATES = {
    "MISSING",
    "ARCHITECTURE_ONLY",
    "EXECUTABLE",
    "TESTED",
    "SUCCESSOR_REPEATED",
    "REFERENCE_ONLY",
}

RELEASE_GATES = {"DENY", "REFERENCE_ONLY", "ALLOW"}
EDGE_ROLES = {"REQUIRED", "OPTIONAL", "ALTERNATIVE", "CONDITIONAL", "REFERENCE", "HAZARD_ONLY"}
SERVICE_LEVELS = {"SL0", "SL1", "SL2", "SL3", "SL4", "SL5", "SL6"}
PRIORITIES = {"P0_RED", "P1_ORANGE", "P2_YELLOW", "P3_GREEN", "P4_BLUE"}
PAYLOAD_SOURCE_RELATIONS = {"DIRECT", "UMBRELLA", "NO_CONFIDENT_MATCH"}
PAYLOAD_CROSSWALK_REVIEW_STATES = {"HUMAN_REVIEW_REQUIRED", "REVIEWED"}

ISSUES: list[str] = []


def issue(message: str) -> None:
    ISSUES.append(message)


def split_ids(value: str) -> list[str]:
    return [part.strip() for part in value.split("|") if part.strip()]


def placeholder(value: str) -> bool:
    upper = value.upper().strip()
    return (
        not upper
        or "MISSING" in upper
        or "TBD" in upper
        or upper.startswith("NO_")
        or "NOT_TESTED" in upper
        or "CANDIDATE" in upper
    )


def read_table(path: Path) -> list[dict[str, str]]:
    if not path.is_file():
        issue(f"missing supplemental register {path.name}")
        return []
    try:
        with path.open("r", encoding="utf-8-sig", newline="") as handle:
            return list(csv.DictReader(handle))
    except (OSError, csv.Error) as exc:
        issue(f"cannot read supplemental register {path.name}: {exc}")
        return []


if not REGISTER.is_file():
    print(f"ISSUE missing register: {REGISTER}", file=sys.stderr)
    raise SystemExit(1)

known_source_ids: set[str] = set()
for source_name, id_field in SOURCE_ID_REGISTERS:
    source_path = ROOT / source_name
    if not source_path.is_file():
        issue(f"missing source-id register {source_name}")
        continue
    try:
        with source_path.open("r", encoding="utf-8-sig", newline="") as source_handle:
            source_rows = list(csv.DictReader(source_handle))
    except (OSError, csv.Error) as exc:
        issue(f"cannot read source-id register {source_name}: {exc}")
        continue
    for source_line, source_row in enumerate(source_rows, start=2):
        source_id = (source_row.get(id_field) or "").strip()
        if not source_id:
            issue(f"{source_name}:{source_line}: blank {id_field}")
        else:
            known_source_ids.add(source_id)

instrument_rows = read_table(ROOT / "practical-science-instrument-register.csv")
known_instrument_ids = {
    (row.get("instrument_id") or "").strip()
    for row in instrument_rows
    if (row.get("instrument_id") or "").strip()
}

with REGISTER.open("r", encoding="utf-8-sig", newline="") as handle:
    reader = csv.DictReader(handle)
    if list(reader.fieldnames or []) != EXPECTED_FIELDS:
        issue(
            "unexpected header: "
            f"expected={EXPECTED_FIELDS!r} actual={list(reader.fieldnames or [])!r}"
        )
    rows = list(reader)

by_id: dict[str, dict[str, str]] = {}
line_by_id: dict[str, int] = {}

for line_no, row in enumerate(rows, start=2):
    node_id = row.get("node_id", "").strip()
    if not node_id:
        issue(f"line {line_no}: blank node_id")
        continue
    if node_id in by_id:
        issue(f"line {line_no}: duplicate node_id {node_id}")
        continue
    by_id[node_id] = row
    line_by_id[node_id] = line_no

roots = [node_id for node_id, row in by_id.items() if not row["parent_id"].strip()]
if roots != ["TD-ROOT"]:
    issue(f"expected one TD-ROOT, found {roots}")

for node_id, row in by_id.items():
    line_no = line_by_id[node_id]
    for required in (
        "domain",
        "node_type",
        "title_ru",
        "outcome",
        "safety_class",
        "execution_policy",
        "measurement_acceptance",
        "calibration_reference",
        "drawings_bom_state",
        "localization_state",
        "stop_conditions",
        "successor_proof",
        "evidence_required",
        "evidence_state",
        "capability_status",
        "release_gate",
        "release_version",
    ):
        if not row.get(required, "").strip():
            issue(f"{node_id} line {line_no}: blank required field {required}")

    if row["node_type"] not in NODE_TYPES:
        issue(f"{node_id}: invalid node_type {row['node_type']}")
    if row["safety_class"] not in SAFETY_CLASSES:
        issue(f"{node_id}: invalid safety_class {row['safety_class']}")
    if row["execution_policy"] not in EXECUTION_POLICIES:
        issue(f"{node_id}: invalid execution_policy {row['execution_policy']}")
    if row["evidence_state"] not in EVIDENCE_STATES:
        issue(f"{node_id}: invalid evidence_state {row['evidence_state']}")
    if row["capability_status"] not in CAPABILITY_STATES:
        issue(f"{node_id}: invalid capability_status {row['capability_status']}")
    if row["release_gate"] not in RELEASE_GATES:
        issue(f"{node_id}: invalid release_gate {row['release_gate']}")

    parent = row["parent_id"].strip()
    if node_id != "TD-ROOT" and not parent:
        issue(f"{node_id}: non-root node has no parent")
    if parent and parent not in by_id:
        issue(f"{node_id}: missing parent {parent}")
    if parent == node_id:
        issue(f"{node_id}: self parent")

    for dependency in split_ids(row["prerequisite_node_ids"]):
        if dependency not in by_id:
            issue(f"{node_id}: unknown prerequisite {dependency}")
        if dependency == node_id:
            issue(f"{node_id}: self prerequisite")

    for source_id in split_ids(row["source_package_ids"]):
        if source_id not in known_source_ids:
            issue(f"{node_id}: unknown source_package_id {source_id}")

    for instrument_id in split_ids(row["instrument_ids"]):
        if instrument_id not in known_instrument_ids:
            issue(f"{node_id}: unknown instrument_id {instrument_id}")

    safety = row["safety_class"]
    policy = row["execution_policy"]
    status = row["capability_status"]
    gate = row["release_gate"]
    evidence = row["evidence_state"]

    if safety == "S0_OBSERVE_READ" and policy != "HOUSEHOLD_S0":
        issue(f"{node_id}: S0 must use HOUSEHOLD_S0")
    if safety == "S1_LOW_RISK_HOUSEHOLD" and policy != "HOUSEHOLD_S1_AFTER_GATE":
        issue(f"{node_id}: S1 must use HOUSEHOLD_S1_AFTER_GATE")
    if safety == "S2_TRAINED_SUPERVISED" and policy != "TRAINED_SUPERVISED":
        issue(f"{node_id}: S2 must use TRAINED_SUPERVISED")
    if safety == "S3_LICENSED_PROFESSIONAL" and policy != "LICENSED_ONLY":
        issue(f"{node_id}: S3 must use LICENSED_ONLY")
    if safety == "S4_REFERENCE_ONLY_PROHIBITED_HOUSEHOLD":
        if policy != "REFERENCE_ONLY_NO_BUILD":
            issue(f"{node_id}: S4 must use REFERENCE_ONLY_NO_BUILD")
        if status != "REFERENCE_ONLY" or gate != "REFERENCE_ONLY":
            issue(f"{node_id}: S4 must remain REFERENCE_ONLY")

    if row["node_type"] == "HAZARD_BOUNDARY":
        if status != "REFERENCE_ONLY" or gate != "REFERENCE_ONLY":
            issue(f"{node_id}: HAZARD_BOUNDARY must remain REFERENCE_ONLY")
        if policy not in {"REFERENCE_ONLY_NO_BUILD", "LICENSED_ONLY"}:
            issue(f"{node_id}: HAZARD_BOUNDARY has unsafe policy {policy}")

    if status == "REFERENCE_ONLY" and gate != "REFERENCE_ONLY":
        issue(f"{node_id}: REFERENCE_ONLY status requires REFERENCE_ONLY gate")

    if gate == "ALLOW":
        if status not in {"EXECUTABLE", "TESTED", "SUCCESSOR_REPEATED"}:
            issue(f"{node_id}: ALLOW without executable/tested status")
        if evidence not in {"VERIFIED_LOCAL", "TESTED", "SUCCESSOR_REPEATED"}:
            issue(f"{node_id}: ALLOW without sufficient evidence")
        if safety in {
            "S3_LICENSED_PROFESSIONAL",
            "S4_REFERENCE_ONLY_PROHIBITED_HOUSEHOLD",
        }:
            issue(f"{node_id}: household graph cannot ALLOW S3/S4")
        for field in (
            "materials_tools_state",
            "measurement_acceptance",
            "calibration_reference",
            "drawings_bom_state",
            "localization_state",
            "stop_conditions",
            "maintenance_spares",
            "successor_proof",
            "evidence_required",
        ):
            if placeholder(row[field]):
                issue(f"{node_id}: ALLOW contains placeholder in {field}")

    title_blob = " ".join(
        [
            row["title_ru"],
            row["outcome"],
            row["notes"],
        ]
    ).lower()
    high_hazard_terms = (
        "порох",
        "взрыв",
        "зажигатель",
        "селитр",
        "окислител",
        "синтез лекар",
        "высокое напряж",
        "сосуд",
    )
    if any(term in title_blob for term in high_hazard_terms):
        if policy not in {"REFERENCE_ONLY_NO_BUILD", "LICENSED_ONLY"}:
            issue(f"{node_id}: high-hazard term with unsafe execution policy")
        if gate == "ALLOW":
            issue(f"{node_id}: high-hazard term cannot be ALLOW")


# Detect cycles in actual prerequisite edges.  parent_id is taxonomy/navigation,
# not an execution dependency: an aggregate OUTCOME legitimately lists child
# capabilities while those children point back to the aggregate as their parent.
graph: dict[str, list[str]] = {}
for node_id, row in by_id.items():
    edges = split_ids(row["prerequisite_node_ids"])
    graph[node_id] = edges

state: dict[str, int] = {}
stack: list[str] = []


def visit(node_id: str) -> None:
    marker = state.get(node_id, 0)
    if marker == 2:
        return
    if marker == 1:
        try:
            start = stack.index(node_id)
            cycle = stack[start:] + [node_id]
        except ValueError:
            cycle = stack + [node_id]
        issue("dependency cycle: " + " -> ".join(cycle))
        return
    state[node_id] = 1
    stack.append(node_id)
    for target in graph.get(node_id, []):
        if target in graph:
            visit(target)
    stack.pop()
    state[node_id] = 2


for node_id in sorted(graph):
    visit(node_id)


# Dependency semantics: prerequisite_node_ids is the compact adjacency list;
# the edge register decides whether an edge is required, alternative,
# conditional, optional, reference-only, or merely a hazard boundary.
edge_rows = read_table(EDGE_REGISTER)
edge_ids: set[str] = set()
actual_pairs: Counter[tuple[str, str]] = Counter()
expected_pairs: Counter[tuple[str, str]] = Counter()
edges_by_source: dict[str, list[dict[str, str]]] = defaultdict(list)
alternative_sets: dict[tuple[str, str], list[dict[str, str]]] = defaultdict(list)

for source_id, row in by_id.items():
    for target_id in split_ids(row["prerequisite_node_ids"]):
        expected_pairs[(source_id, target_id)] += 1

for line_no, edge in enumerate(edge_rows, start=2):
    edge_id = (edge.get("edge_id") or "").strip()
    source_id = (edge.get("from_node_id") or "").strip()
    target_id = (edge.get("to_node_id") or "").strip()
    role = (edge.get("edge_role") or "").strip()
    group = (edge.get("alternative_group") or "").strip()
    minimum = (edge.get("minimum_required_count") or "").strip()
    level = (edge.get("service_level") or "").strip()
    if not edge_id or edge_id in edge_ids:
        issue(f"{EDGE_REGISTER.name}:{line_no}: blank or duplicate edge_id {edge_id!r}")
    edge_ids.add(edge_id)
    if source_id not in by_id or target_id not in by_id:
        issue(f"{edge_id}: unknown edge endpoint {source_id}->{target_id}")
        continue
    actual_pairs[(source_id, target_id)] += 1
    edges_by_source[source_id].append(edge)
    if role not in EDGE_ROLES:
        issue(f"{edge_id}: invalid edge_role {role!r}")
    if level not in SERVICE_LEVELS:
        issue(f"{edge_id}: invalid service_level {level!r}")
    if edge.get("review_state") != "PROVISIONAL_AUTO_REVIEW_REQUIRED":
        issue(f"{edge_id}: edge review state must remain provisional")
    if edge.get("release_gate") != "DENY":
        issue(f"{edge_id}: edge register cannot authorize execution")
    target = by_id[target_id]
    if target["safety_class"] == "S4_REFERENCE_ONLY_PROHIBITED_HOUSEHOLD":
        if role not in {"REFERENCE", "HAZARD_ONLY"}:
            issue(f"{edge_id}: S4 target must be REFERENCE or HAZARD_ONLY, found {role}")
    if role == "ALTERNATIVE":
        if not group:
            issue(f"{edge_id}: ALTERNATIVE missing alternative_group")
        if minimum != "1":
            issue(f"{edge_id}: current ALTERNATIVE groups require minimum_required_count=1")
        alternative_sets[(source_id, group)].append(edge)
    else:
        if group or minimum:
            issue(f"{edge_id}: non-ALTERNATIVE edge has alternative metadata")

if actual_pairs != expected_pairs:
    missing_pairs = list((expected_pairs - actual_pairs).elements())[:8]
    extra_pairs = list((actual_pairs - expected_pairs).elements())[:8]
    issue(f"edge adjacency mismatch missing={missing_pairs} extra={extra_pairs}")

for (source_id, group), group_edges in alternative_sets.items():
    if len(group_edges) < 2:
        issue(f"{source_id}:{group}: alternative group has fewer than two paths")
    if not any(
        by_id[edge["to_node_id"]]["safety_class"]
        in {"S0_OBSERVE_READ", "S1_LOW_RISK_HOUSEHOLD", "S2_TRAINED_SUPERVISED"}
        for edge in group_edges
    ):
        issue(f"{source_id}:{group}: no S0-S2 alternative path")

required_root_edges = {
    "TD-BASE", "TD-PEOPLE", "TD-WATER", "TD-FOOD", "TD-SHELTER", "TD-ENERGY",
    "TD-HEALTH", "TD-MAPS-COMMS", "TD-KNOWLEDGE", "TD-GOV", "TD-WORKSHOP",
    "TD-TRANSPORT", "TD-SECURITY", "TD-EDUCATION", "TD-ENVIRONMENT", "TD-PORTUGAL",
}
observed_required_root = {
    edge["to_node_id"] for edge in edges_by_source.get("TD-ROOT", []) if edge["edge_role"] == "REQUIRED"
}
if observed_required_root != required_root_edges:
    issue(
        "TD-ROOT required outcomes mismatch "
        f"missing={sorted(required_root_edges-observed_required_root)} "
        f"extra={sorted(observed_required_root-required_root_edges)}"
    )

# Node planning must cover every node exactly once, while remaining provisional.
plan_rows = read_table(PLAN_REGISTER)
plan_ids: set[str] = set()
planned_nodes: set[str] = set()
for line_no, plan in enumerate(plan_rows, start=2):
    plan_id = (plan.get("plan_id") or "").strip()
    node_id = (plan.get("node_id") or "").strip()
    if not plan_id or plan_id in plan_ids:
        issue(f"{PLAN_REGISTER.name}:{line_no}: blank or duplicate plan_id {plan_id!r}")
    plan_ids.add(plan_id)
    if node_id not in by_id:
        issue(f"{plan_id}: unknown planned node {node_id}")
    if node_id in planned_nodes:
        issue(f"{plan_id}: duplicate planning row for {node_id}")
    planned_nodes.add(node_id)
    if plan.get("priority_tier") not in PRIORITIES:
        issue(f"{plan_id}: invalid priority {plan.get('priority_tier')!r}")
    if plan.get("earliest_service_level") not in SERVICE_LEVELS:
        issue(f"{plan_id}: invalid earliest service level")
    if plan.get("human_review_state") != "PROVISIONAL_AUTO_REVIEW_REQUIRED":
        issue(f"{plan_id}: planning row must remain provisional")
    if plan.get("release_gate") != "DENY":
        issue(f"{plan_id}: planning row cannot authorize execution")
    for required_field in ("capacity_model", "group_size_scope", "failure_domain", "redundancy_target"):
        if not (plan.get(required_field) or "").strip():
            issue(f"{plan_id}: blank {required_field}")
if planned_nodes != set(by_id):
    issue(
        f"planning/node mismatch missing={sorted(set(by_id)-planned_nodes)[:8]} "
        f"extra={sorted(planned_nodes-set(by_id))[:8]}"
    )

# Root service levels must exist for every horizon and reference real outcomes.
service_rows = read_table(SERVICE_REGISTER)
service_ids: set[str] = set()
seen_levels: set[str] = set()
for line_no, service in enumerate(service_rows, start=2):
    service_id = (service.get("service_requirement_id") or "").strip()
    level = (service.get("service_level") or "").strip()
    outcome_id = (service.get("outcome_node_id") or "").strip()
    if not service_id or service_id in service_ids:
        issue(f"{SERVICE_REGISTER.name}:{line_no}: blank or duplicate requirement id")
    service_ids.add(service_id)
    if level not in SERVICE_LEVELS:
        issue(f"{service_id}: invalid service level {level!r}")
    else:
        seen_levels.add(level)
    if outcome_id not in by_id:
        issue(f"{service_id}: unknown outcome_node_id {outcome_id}")
    if service.get("requirement_role") not in {"REQUIRED", "CONDITIONAL"}:
        issue(f"{service_id}: invalid requirement role")
    if service.get("status") != "CATALOG_ONLY_NOT_EVALUATED":
        issue(f"{service_id}: service status must remain unevaluated")
    if service.get("human_review_state") != "PROVISIONAL_AUTO_REVIEW_REQUIRED":
        issue(f"{service_id}: service requirement must remain provisional")
    if service.get("release_gate") != "DENY":
        issue(f"{service_id}: service requirement cannot authorize execution")
if seen_levels != SERVICE_LEVELS:
    issue(f"service levels incomplete: missing={sorted(SERVICE_LEVELS-seen_levels)}")

# Crosswalk every legacy scenario capability into canonical technology,
# century-capability, MOC and science namespaces.
scenario_rows = read_table(ROOT / "scenario-register.csv")
legacy_capabilities = {
    capability
    for scenario in scenario_rows
    for capability in split_ids((scenario.get("capability_ids") or ""))
}
century_ids = {
    (row.get("capability_id") or "").strip()
    for row in read_table(ROOT / "century-capability-register.csv")
    if (row.get("capability_id") or "").strip()
}
science_ids = {
    (row.get("domain_id") or "").strip()
    for row in read_table(ROOT / "practical-science-domain-register.csv")
    if (row.get("domain_id") or "").strip()
}
moc_ids: set[str] = set()
for moc_path in (ROOT / "Obsidian-Vault" / "MOCs").glob("*.md"):
    for text_line in moc_path.read_text(encoding="utf-8").splitlines()[:20]:
        if text_line.startswith("id:"):
            moc_ids.add(text_line.split(":", 1)[1].strip().strip('"'))
            break

crosswalk_rows = read_table(CROSSWALK_REGISTER)
mapped_legacy: set[str] = set()
crosswalk_ids: set[str] = set()
for line_no, mapping in enumerate(crosswalk_rows, start=2):
    mapping_id = (mapping.get("crosswalk_id") or "").strip()
    legacy_id = (mapping.get("legacy_capability_id") or "").strip()
    if not mapping_id or mapping_id in crosswalk_ids:
        issue(f"{CROSSWALK_REGISTER.name}:{line_no}: blank or duplicate crosswalk_id")
    crosswalk_ids.add(mapping_id)
    if legacy_id in mapped_legacy:
        issue(f"{mapping_id}: duplicate mapping for legacy capability {legacy_id}")
    mapped_legacy.add(legacy_id)
    for target_id in split_ids(mapping.get("canonical_technology_ids") or ""):
        if target_id not in by_id:
            issue(f"{mapping_id}: unknown technology id {target_id}")
    for target_id in split_ids(mapping.get("century_capability_ids") or ""):
        if target_id not in century_ids:
            issue(f"{mapping_id}: unknown century capability id {target_id}")
    for target_id in split_ids(mapping.get("moc_ids") or ""):
        if target_id not in moc_ids:
            issue(f"{mapping_id}: unknown MOC id {target_id}")
    for target_id in split_ids(mapping.get("science_domain_ids") or ""):
        if target_id not in science_ids:
            issue(f"{mapping_id}: unknown science domain id {target_id}")
    if mapping.get("mapping_status") != "PROVISIONAL_HUMAN_REVIEW_REQUIRED":
        issue(f"{mapping_id}: mapping must remain provisional")
if mapped_legacy != legacy_capabilities:
    issue(
        f"scenario crosswalk mismatch missing={sorted(legacy_capabilities-mapped_legacy)} "
        f"extra={sorted(mapped_legacy-legacy_capabilities)}"
    )

# Every byte-bearing offline payload must have exactly one explicit crosswalk
# row.  The three namespaces stay separate so an identifier that happens to
# collide across registries cannot silently satisfy the wrong relationship.
payload_rows = read_table(PAYLOAD_REGISTER)
expected_payload_ids: set[str] = set()
for line_no, payload in enumerate(payload_rows, start=2):
    payload_id = (payload.get("payload_id") or "").strip()
    if not payload_id:
        issue(f"{PAYLOAD_REGISTER.name}:{line_no}: blank payload_id")
    elif payload_id in expected_payload_ids:
        issue(f"{PAYLOAD_REGISTER.name}:{line_no}: duplicate payload_id {payload_id}")
    else:
        expected_payload_ids.add(payload_id)

payload_target_namespaces = (
    (
        "source_manifest_ids",
        "source_relation",
        {
            (row.get("id") or "").strip()
            for row in read_table(ROOT / "source-manifest.csv")
            if (row.get("id") or "").strip()
        },
    ),
    (
        "offline_package_ids",
        "offline_relation",
        {
            (row.get("package_id") or "").strip()
            for row in read_table(ROOT / "offline-corpus-manifest.csv")
            if (row.get("package_id") or "").strip()
        },
    ),
    (
        "science_package_ids",
        "science_relation",
        {
            (row.get("package_id") or "").strip()
            for row in read_table(ROOT / "practical-science-package-register.csv")
            if (row.get("package_id") or "").strip()
        },
    ),
)

payload_crosswalk_rows = read_table(PAYLOAD_SOURCE_CROSSWALK)
payload_crosswalk_ids: set[str] = set()
mapped_payload_ids: set[str] = set()
for line_no, mapping in enumerate(payload_crosswalk_rows, start=2):
    mapping_id = (mapping.get("payload_crosswalk_id") or "").strip()
    payload_id = (mapping.get("payload_id") or "").strip()
    if not mapping_id or mapping_id in payload_crosswalk_ids:
        issue(
            f"{PAYLOAD_SOURCE_CROSSWALK.name}:{line_no}: "
            f"blank or duplicate payload_crosswalk_id {mapping_id!r}"
        )
    else:
        payload_crosswalk_ids.add(mapping_id)
    if not payload_id:
        issue(f"{PAYLOAD_SOURCE_CROSSWALK.name}:{line_no}: blank payload_id")
    elif payload_id not in expected_payload_ids:
        issue(f"{mapping_id or PAYLOAD_SOURCE_CROSSWALK.name}: unknown payload_id {payload_id}")
    elif payload_id in mapped_payload_ids:
        issue(f"{mapping_id or PAYLOAD_SOURCE_CROSSWALK.name}: duplicate mapping for payload_id {payload_id}")
    else:
        mapped_payload_ids.add(payload_id)

    for id_field, relation_field, known_ids in payload_target_namespaces:
        target_ids = split_ids(mapping.get(id_field) or "")
        relation = (mapping.get(relation_field) or "").strip()
        if relation not in PAYLOAD_SOURCE_RELATIONS:
            issue(f"{mapping_id}: invalid {relation_field} {relation!r}")
        if relation == "NO_CONFIDENT_MATCH" and target_ids:
            issue(f"{mapping_id}: {id_field} must be blank for NO_CONFIDENT_MATCH")
        if relation in {"DIRECT", "UMBRELLA"} and not target_ids:
            issue(f"{mapping_id}: {id_field} is required for {relation}")
        for target_id in target_ids:
            if target_id not in known_ids:
                issue(f"{mapping_id}: unknown {id_field} target {target_id}")

    review_state = (mapping.get("review_state") or "").strip()
    if review_state not in PAYLOAD_CROSSWALK_REVIEW_STATES:
        issue(f"{mapping_id}: invalid payload crosswalk review_state {review_state!r}")
    if (mapping.get("release_version") or "").strip() != "0.5-draft":
        issue(f"{mapping_id}: payload crosswalk release_version must be 0.5-draft")

if mapped_payload_ids != expected_payload_ids:
    issue(
        "payload/source crosswalk mismatch "
        f"missing={sorted(expected_payload_ids-mapped_payload_ids)} "
        f"extra={sorted(mapped_payload_ids-expected_payload_ids)}"
    )

# Future ALLOW status must respect edge roles rather than treating every link
# as an AND dependency.  Conditional applicability is decided in a reviewed
# profile, so this static validator cannot silently assume it.
for node_id, row in by_id.items():
    if row["release_gate"] != "ALLOW":
        continue
    node_edges = edges_by_source.get(node_id, [])
    for edge in node_edges:
        if edge["edge_role"] == "REQUIRED" and by_id[edge["to_node_id"]]["release_gate"] != "ALLOW":
            issue(f"{node_id}: ALLOW has blocked REQUIRED edge to {edge['to_node_id']}")
    grouped = defaultdict(list)
    for edge in node_edges:
        if edge["edge_role"] == "ALTERNATIVE":
            grouped[edge["alternative_group"]].append(edge)
    for group, alternatives in grouped.items():
        if not any(by_id[edge["to_node_id"]]["release_gate"] == "ALLOW" for edge in alternatives):
            issue(f"{node_id}: ALLOW has no allowed path in alternative group {group}")


counts = Counter(row["release_gate"] for row in rows)
status_counts = Counter(row["capability_status"] for row in rows)
safety_counts = Counter(row["safety_class"] for row in rows)
print(
    "technology_tree_summary "
    f"nodes={len(rows)} roots={len(roots)} "
    f"allow={counts['ALLOW']} deny={counts['DENY']} "
    f"reference_only={counts['REFERENCE_ONLY']} edges={len(edge_rows)} "
    f"service_requirements={len(service_rows)} crosswalk={len(crosswalk_rows)} "
    f"payload_crosswalk={len(payload_crosswalk_rows)} issues={len(ISSUES)}"
)
print("capability_statuses " + " ".join(f"{k}={v}" for k, v in sorted(status_counts.items())))
print("safety_classes " + " ".join(f"{k}={v}" for k, v in sorted(safety_counts.items())))
for message in ISSUES:
    print(f"ISSUE {message}")
print(f"result={'PASS' if not ISSUES else 'FAIL'}")
raise SystemExit(0 if not ISSUES else 1)
