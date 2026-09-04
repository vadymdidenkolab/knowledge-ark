#!/usr/bin/env python3
"""Validate the human Obsidian topic graph, metadata contract and canvases.

Passing proves structure, controlled vocabulary, deterministic ownership and
graph/canvas consistency only. It does not prove that planned knowledge has
been written, reviewed, physically supplied, tested or released.
"""

from __future__ import annotations

from collections import Counter, defaultdict, deque
import hashlib
import json
from pathlib import Path
import re
import sys
from typing import Dict, List, Mapping, Set, Tuple


ROOT = Path(__file__).resolve().parent
VAULT = ROOT / "Obsidian-Vault"
KNOWLEDGE = VAULT / "01 — КАРТОТЕКА ЗНАНИЙ"
ROUTES = KNOWLEDGE / "01 — Маршруты"
TOPICS = KNOWLEDGE / "02 — Темы"
CANVASES = KNOWLEDGE / "03 — Карты связей"
INDEX = KNOWLEDGE / "00 — Карта всех знаний.md"
MANIFEST = KNOWLEDGE / ".generated-knowledge-routes-manifest.json"
CANVAS_MANIFEST = CANVASES / ".generated-semantic-canvas-manifest.json"
GRAPH = VAULT / ".obsidian" / "graph.json"
PROJECT_GRAPH = ROOT / ".obsidian" / "graph.json"
PROJECT_APPEARANCE = ROOT / ".obsidian" / "appearance.json"
PROJECT_SNIPPET = ROOT / ".obsidian" / "snippets" / "01-понятный-режим.css"
PARENT_VAULT = ROOT.parent
PARENT_GRAPH = PARENT_VAULT / ".obsidian" / "graph.json"
PARENT_APPEARANCE = PARENT_VAULT / ".obsidian" / "appearance.json"
PARENT_SNIPPET = PARENT_VAULT / ".obsidian" / "snippets" / "01-понятный-режим.css"
SCHEMA = ROOT / "standards" / "obsidian-topic-schema-v1.json"
STANDARD_NOTE = VAULT / "40 — Стандарт картотеки" / "00 — Стандарт данных, тегов и связей.md"

TOPIC_PREFIX = "01 — КАРТОТЕКА ЗНАНИЙ/02 — Темы/"
POSITIVE_GRAPH_FILTER = 'path:"01 — КАРТОТЕКА ЗНАНИЙ/02 — Темы"'
PROJECT_POSITIVE_GRAPH_FILTER = f'path:"{VAULT.name}/01 — КАРТОТЕКА ЗНАНИЙ/02 — Темы"'
PARENT_POSITIVE_GRAPH_FILTER = f'path:"{ROOT.name}/{VAULT.name}/01 — КАРТОТЕКА ЗНАНИЙ/02 — Темы"'
WIKILINK_RE = re.compile(r"\[\[([^\]|#]+)(?:#[^\]|]+)?(?:\|[^\]]+)?\]\]")
RELATION_RE = re.compile(
    r"^- \*\*(Нужно до|Следующий шаг|Открывает|При аварии):\*\* "
    r"\[\[([^\]|#]+)(?:\|[^\]]+)?\]\]$",
    re.MULTILINE,
)
EXPECTED_RELATION_COUNTS = {
    "Нужно до": 53,
    "Следующий шаг": 9,
    "Открывает": 15,
    "При аварии": 5,
}
EXPECTED_CANVASES = {
    "01 — Что нужно сначала.canvas",
    "02 — Следующие шаги и возможности.canvas",
    "03 — Что открывать при аварии.canvas",
    "04 — Образовательная лестница.canvas",
    "05 — Все смысловые связи.canvas",
}


def display_path(path: Path) -> str:
    try:
        return path.relative_to(ROOT).as_posix()
    except ValueError:
        return str(path)


def section(text: str, heading: str) -> str:
    marker = f"## {heading}\n"
    start = text.find(marker)
    if start < 0:
        return ""
    start += len(marker)
    end = text.find("\n## ", start)
    return text[start:] if end < 0 else text[start:end]


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def semantic_json_hash(path: Path) -> str:
    value = json.loads(path.read_text(encoding="utf-8"))
    canonical = json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(canonical.encode("utf-8")).hexdigest()


def load_json(path: Path, issues: List[str]) -> Dict[str, object]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        issues.append(f"cannot read {display_path(path)}: {exc}")
        return {}
    if not isinstance(value, dict):
        issues.append(f"JSON root is not an object: {display_path(path)}")
        return {}
    return value


def parse_frontmatter(text: str, path: Path, issues: List[str]) -> Dict[str, object]:
    if not text.startswith("---\n"):
        issues.append(f"missing frontmatter: {path.name}")
        return {}
    end = text.find("\n---", 4)
    if end < 0:
        issues.append(f"unterminated frontmatter: {path.name}")
        return {}
    result: Dict[str, object] = {}
    active_list: str | None = None
    for raw in text[4:end].splitlines():
        if raw.startswith("  - ") and active_list:
            value = raw[4:].strip()
            try:
                parsed = json.loads(value) if value.startswith('"') else value
            except json.JSONDecodeError:
                parsed = value
            cast = result.setdefault(active_list, [])
            if isinstance(cast, list):
                cast.append(parsed)
            continue
        active_list = None
        if ":" not in raw:
            continue
        key, value = raw.split(":", 1)
        key = key.strip()
        value = value.strip()
        if not value:
            result[key] = []
            active_list = key
        else:
            try:
                result[key] = json.loads(value) if value[0] in '["' or value in ("true", "false", "null") else value
            except (json.JSONDecodeError, IndexError):
                result[key] = value
    return result


def expected_id(path: Path) -> str:
    return f"картотека-тема-{path.name.split(' — ', 1)[0]}"


def validate_manifest_hashes(
    manifest: Mapping[str, object],
    base: Path,
    expected_names: Set[str],
    issues: List[str],
    label: str,
) -> None:
    names = manifest.get("generated_files")
    hashes = manifest.get("generated_sha256")
    if not isinstance(names, list) or set(map(str, names)) != expected_names:
        issues.append(f"{label} manifest file ownership differs from disk")
    if not isinstance(hashes, dict) or set(map(str, hashes)) != expected_names:
        issues.append(f"{label} manifest does not hash every owned file")
        return
    for name in sorted(expected_names):
        path = base / name
        actual_hash = semantic_json_hash(path) if manifest.get("hash_mode") == "canonical-json" else sha256_file(path)
        if path.is_file() and hashes.get(name) != actual_hash:
            issues.append(f"{label} generated hash mismatch: {name}")


def validate_graph_config(
    graph: Mapping[str, object],
    contour_tags: Mapping[str, Set[str]],
    expected_filter: str,
    issues: List[str],
    label: str,
) -> None:
    if graph.get("search") != expected_filter:
        issues.append(f"{label} graph search must be exact positive topic filter: {expected_filter}")
    for key, expected in (
        ("hideUnresolved", True),
        ("showOrphans", False),
        ("showArrow", True),
        ("showTags", False),
        ("showAttachments", False),
    ):
        if graph.get(key) is not expected:
            issues.append(f"{label} graph setting {key}={graph.get(key)!r}, expected {expected!r}")
    distance = graph.get("linkDistance")
    if not isinstance(distance, (int, float)) or not 130 <= distance <= 220:
        issues.append(f"{label} graph linkDistance must be 130..220, got {distance!r}")

    raw_groups = graph.get("colorGroups")
    if not isinstance(raw_groups, list) or len(raw_groups) != len(contour_tags):
        issues.append(f"{label} graph must have {len(contour_tags)} color groups")
        return
    actual_tag_sets: List[frozenset[str]] = []
    colors: Set[int] = set()
    for group in raw_groups:
        if not isinstance(group, dict):
            issues.append(f"{label} graph color group is not an object")
            continue
        query = group.get("query")
        if not isinstance(query, str):
            issues.append(f"{label} graph color group lacks query")
            continue
        terms = frozenset(re.findall(r"tag:#([^\s)]+)", query))
        if not terms or query.count("tag:#") != len(terms):
            issues.append(f"{label} graph color group has empty or duplicate exact tag terms: {query}")
        actual_tag_sets.append(terms)
        color = group.get("color")
        if not isinstance(color, dict) or color.get("a") != 1 or not isinstance(color.get("rgb"), int):
            issues.append(f"{label} graph color must be opaque numeric RGB: {color!r}")
        else:
            colors.add(int(color["rgb"]))
    if set(actual_tag_sets) != {frozenset(tags) for tags in contour_tags.values()}:
        issues.append(f"{label} graph color groups do not exactly cover frozen area tags")
    if len(colors) != len(contour_tags):
        issues.append(f"{label} graph contour colors must be unique")


def validate_outer_graph_guard(
    graph: Mapping[str, object],
    expected_filter: str,
    issues: List[str],
    label: str,
) -> None:
    """Outer vaults must suppress noise; they are not semantic runtimes."""
    if graph.get("search") != expected_filter:
        issues.append(f"{label} guard search must be exact positive topic path: {expected_filter}")
    for key, expected in (
        ("hideUnresolved", True),
        ("showOrphans", False),
        ("showTags", False),
        ("showAttachments", False),
    ):
        if graph.get(key) is not expected:
            issues.append(f"{label} guard setting {key}={graph.get(key)!r}, expected {expected!r}")


def validate_canvas(
    path: Path,
    expected_rows: Set[Tuple[str, str, str]],
    expected_topic_files: Set[str],
    issues: List[str],
) -> Tuple[int, int]:
    data = load_json(path, issues)
    nodes = data.get("nodes")
    edges = data.get("edges")
    if not isinstance(nodes, list) or not isinstance(edges, list):
        issues.append(f"canvas lacks node/edge arrays: {path.name}")
        return 0, 0
    ids: Set[str] = set()
    node_to_file: Dict[str, str] = {}
    for node in nodes:
        if not isinstance(node, dict) or not isinstance(node.get("id"), str):
            issues.append(f"invalid canvas node: {path.name}")
            continue
        node_id = str(node["id"])
        if node_id in ids:
            issues.append(f"duplicate canvas node id: {path.name}:{node_id}")
        ids.add(node_id)
        if node.get("type") == "file":
            file = node.get("file")
            if not isinstance(file, str) or not file.startswith(TOPIC_PREFIX) or not file.endswith(".md"):
                issues.append(f"canvas file node leaves topic layer: {path.name}:{file!r}")
            else:
                node_to_file[node_id] = file
    if set(node_to_file.values()) != expected_topic_files:
        issues.append(f"canvas topic-node set mismatch: {path.name}")

    actual_rows: Set[Tuple[str, str, str]] = set()
    edge_ids: Set[str] = set()
    labels = {"нужно сначала", "следующий шаг", "открывает", "при аварии"}
    for edge in edges:
        if not isinstance(edge, dict) or not isinstance(edge.get("id"), str):
            issues.append(f"invalid canvas edge: {path.name}")
            continue
        edge_id = str(edge["id"])
        if edge_id in edge_ids:
            issues.append(f"duplicate canvas edge id: {path.name}:{edge_id}")
        edge_ids.add(edge_id)
        source = edge.get("fromNode")
        target = edge.get("toNode")
        label = edge.get("label")
        if source not in node_to_file or target not in node_to_file:
            issues.append(f"dangling or non-topic canvas edge: {path.name}:{edge_id}")
            continue
        if edge.get("toEnd") != "arrow" or label not in labels:
            issues.append(f"canvas edge lacks controlled label/direction: {path.name}:{edge_id}")
            continue
        row = (node_to_file[str(source)], str(label), node_to_file[str(target)])
        if row in actual_rows:
            issues.append(f"duplicate semantic canvas edge: {path.name}:{row}")
        actual_rows.add(row)
    if actual_rows != expected_rows:
        issues.append(
            f"canvas semantic edge set mismatch: {path.name}; "
            f"missing={sorted(expected_rows - actual_rows)[:3]} extra={sorted(actual_rows - expected_rows)[:3]}"
        )
    return len(node_to_file), len(actual_rows)


def main() -> int:
    issues: List[str] = []
    required_files = [
        INDEX,
        MANIFEST,
        CANVAS_MANIFEST,
        GRAPH,
        SCHEMA,
        STANDARD_NOTE,
    ]
    project_vault_enabled = (ROOT / ".obsidian").is_dir()
    parent_vault_enabled = (PARENT_VAULT / ".obsidian").is_dir()
    if project_vault_enabled:
        required_files.extend((PROJECT_GRAPH, PROJECT_APPEARANCE, PROJECT_SNIPPET))
    if parent_vault_enabled:
        required_files.extend((PARENT_GRAPH, PARENT_APPEARANCE, PARENT_SNIPPET))
    for path in required_files:
        if not path.is_file():
            issues.append(f"required file missing: {display_path(path)}")
    for path in (ROUTES, TOPICS, CANVASES):
        if not path.is_dir():
            issues.append(f"required directory missing: {display_path(path)}")
    if issues:
        for issue in issues:
            print(f"ERROR {issue}", file=sys.stderr)
        return 1

    schema = load_json(SCHEMA, issues)
    graph = load_json(GRAPH, issues)
    project_graph = load_json(PROJECT_GRAPH, issues) if project_vault_enabled else {}
    project_appearance = load_json(PROJECT_APPEARANCE, issues) if project_vault_enabled else {}
    parent_graph = load_json(PARENT_GRAPH, issues) if parent_vault_enabled else {}
    parent_appearance = load_json(PARENT_APPEARANCE, issues) if parent_vault_enabled else {}
    manifest = load_json(MANIFEST, issues)
    canvas_manifest = load_json(CANVAS_MANIFEST, issues)

    properties = schema.get("properties") if isinstance(schema.get("properties"), dict) else {}
    tags_spec = properties.get("tags") if isinstance(properties.get("tags"), dict) else {}
    items_spec = tags_spec.get("items") if isinstance(tags_spec.get("items"), dict) else {}
    allowed_tags = set(map(str, items_spec.get("enum", []))) if isinstance(items_spec.get("enum"), list) else set()
    required_dimensions = schema.get("x-required-tag-dimensions")
    optional_dimensions = schema.get("x-optional-tag-dimensions")
    relation_types = schema.get("x-relation-types")
    expected_dimensions = ["область", "готовность", "проверка", "география", "горизонт", "риск"]
    if required_dimensions != expected_dimensions:
        issues.append("schema required tag dimensions differ from v1 contract")
        required_dimensions = []
    if optional_dimensions != ["возраст"]:
        issues.append("schema optional tag dimensions differ from v1 contract")
    if relation_types != ["нужно до", "следующий шаг", "открывает", "при аварии"]:
        issues.append("schema relation vocabulary differs from v1 contract")
    if not allowed_tags:
        issues.append("schema controlled tag vocabulary is empty")

    topic_files = sorted(TOPICS.glob("*.md"))
    route_files = sorted(ROUTES.glob("*.md"))
    canvas_files = sorted(CANVASES.glob("*.canvas"))
    if len(topic_files) != 32:
        issues.append(f"topic count is {len(topic_files)}, expected 32")
    if len(route_files) != 9:
        issues.append(f"route count is {len(route_files)}, expected 9")
    if {path.name for path in canvas_files} != EXPECTED_CANVASES:
        issues.append("canvas filenames differ from controlled set")

    markdown_names = {path.relative_to(KNOWLEDGE).as_posix() for path in KNOWLEDGE.rglob("*.md")}
    validate_manifest_hashes(manifest, KNOWLEDGE, markdown_names, issues, "knowledge")
    if manifest.get("version") != 2:
        issues.append("knowledge manifest must be version 2 with overwrite protection")
    canvas_names = {path.name for path in canvas_files}
    validate_manifest_hashes(canvas_manifest, CANVASES, canvas_names, issues, "canvas")

    topic_targets = {TOPIC_PREFIX + path.stem: path for path in topic_files}
    target_to_id: Dict[str, str] = {}
    id_to_tags: Dict[str, Tuple[str, ...]] = {}
    contour_tags: Dict[str, Set[str]] = defaultdict(set)
    relation_counts: Counter[str] = Counter()
    semantic_rows: List[Tuple[str, str, str]] = []
    outgoing: Counter[str] = Counter()
    incoming: Counter[str] = Counter()
    future_cards = 0
    education_ids = {"картотека-тема-30", "картотека-тема-31", "картотека-тема-32"}

    for path in topic_files:
        text = path.read_text(encoding="utf-8")
        source = TOPIC_PREFIX + path.stem
        props = parse_frontmatter(text, path, issues)
        identifier = str(props.get("id", ""))
        if identifier != expected_id(path):
            issues.append(f"topic id mismatch: {path.name} -> {identifier!r}")
        if identifier in id_to_tags:
            issues.append(f"duplicate topic id: {identifier}")
        if props.get("версия_схемы") != "1.0":
            issues.append(f"topic schema version is not 1.0: {path.name}")
        if props.get("тип") != "тип/тема":
            issues.append(f"topic type property is uncontrolled: {path.name}")
        title = props.get("title")
        if not isinstance(title, str) or not re.search(r"[А-Яа-яЁё]", title):
            issues.append(f"topic title must be human-readable Russian: {path.name}")
        tags = props.get("tags")
        if not isinstance(tags, list) or not all(isinstance(tag, str) for tag in tags):
            issues.append(f"topic tags are not a YAML list of strings: {path.name}")
            tags = []
        tags_tuple = tuple(str(tag) for tag in tags)
        id_to_tags[identifier] = tags_tuple
        expected_count = 7 if identifier in education_ids else 6
        if len(tags_tuple) != expected_count or len(set(tags_tuple)) != expected_count:
            issues.append(f"topic must have exactly {expected_count} unique tags: {path.name}")
        unknown = set(tags_tuple) - allowed_tags
        if unknown:
            issues.append(f"topic uses tags outside frozen vocabulary: {path.name}:{sorted(unknown)}")
        for tag in tags_tuple:
            if re.search(r"[A-Za-z]", tag) or " " in tag or not re.fullmatch(r"[\w\-/Ёё]+", tag, re.UNICODE):
                issues.append(f"invalid controlled tag format: {path.name}:{tag}")
        for dimension in required_dimensions:
            if sum(tag.startswith(str(dimension) + "/") for tag in tags_tuple) != 1:
                issues.append(f"topic needs exactly one {dimension}/ tag: {path.name}")
        age = [tag for tag in tags_tuple if tag.startswith("возраст/")]
        if (identifier in education_ids and len(age) != 1) or (identifier not in education_ids and age):
            issues.append(f"age tag cardinality mismatch: {path.name}")
        area = [tag for tag in tags_tuple if tag.startswith("область/")]
        if len(area) == 1:
            parts = area[0].split("/")
            if len(parts) != 3:
                issues.append(f"area tag must be exactly area/contour/topic: {path.name}:{area[0]}")
            else:
                contour_tags[parts[1]].add(area[0])
        body = text[text.find("\n---", 4) + 4 :]
        for line in body.splitlines():
            if not line.lstrip().startswith("#") and re.search(r"(?<!\S)#[\wА-Яа-яЁё][\wА-Яа-яЁё/-]*", line):
                issues.append(f"inline tag is forbidden in topic body: {path.name}")
                break

        links = WIKILINK_RE.findall(text)
        relations = RELATION_RE.findall(section(text, "Смысловые связи"))
        if len(links) != len(relations) or not 2 <= len(relations) <= 4:
            issues.append(f"topic must contain only 2..4 semantic topic links: {path.name}")
        if links != [target for _, target in relations]:
            issues.append(f"topic link order/content differs from semantic relation block: {path.name}")
        for kind, target in relations:
            relation_counts[kind] += 1
            if target not in topic_targets:
                issues.append(f"topic points outside existing semantic layer: {path.name}->{target}")
                continue
            if target == source:
                issues.append(f"self-link in semantic graph: {path.name}")
                continue
            semantic_rows.append((source, kind, target))
            outgoing[source] += 1
            incoming[target] += 1
        target_to_id[source] = identifier
        table_rows = [line for line in section(text, "Будущие конкретные карточки").splitlines() if line.startswith("| ")]
        future_cards += max(0, len(table_rows) - 1)

    if len(contour_tags) != 10:
        issues.append(f"area contour count is {len(contour_tags)}, expected 10")
    if relation_counts != Counter(EXPECTED_RELATION_COUNTS):
        issues.append(f"relation counts differ from v1 contract: {dict(relation_counts)}")
    if future_cards != 890:
        issues.append(f"future-card count is {future_cards}, expected 890")
    if len(semantic_rows) != 82:
        issues.append(f"semantic edge count is {len(semantic_rows)}, expected 82")
    directed_pairs = {(source, target) for source, _, target in semantic_rows}
    if len(directed_pairs) != len(semantic_rows):
        issues.append("duplicate directed topic pair detected")
    reciprocals = {tuple(sorted((source, target))) for source, target in directed_pairs if (target, source) in directed_pairs}
    if reciprocals:
        issues.append(f"reciprocal topic pairs detected: {sorted(reciprocals)[:3]}")
    orphans = [target for target in topic_targets if not outgoing[target] and not incoming[target]]
    if orphans:
        issues.append(f"orphan topics: {orphans}")

    children: Dict[str, List[str]] = {target: [] for target in topic_targets}
    indegree: Dict[str, int] = {target: 0 for target in topic_targets}
    for source, kind, target in semantic_rows:
        if kind == "Нужно до":
            children[target].append(source)
            indegree[source] += 1
    queue = deque(key for key, degree in indegree.items() if degree == 0)
    visited = 0
    while queue:
        current = queue.popleft()
        visited += 1
        for child in children[current]:
            indegree[child] -= 1
            if indegree[child] == 0:
                queue.append(child)
    if visited != len(topic_targets):
        issues.append("cycle detected in «Нужно до» prerequisites")

    route_links = {link for path in route_files for link in WIKILINK_RE.findall(path.read_text(encoding="utf-8"))}
    unreachable = sorted(set(topic_targets) - route_links)
    if unreachable:
        issues.append(f"topics unreachable from routes: {unreachable}")

    manifest_schema = manifest.get("topic_schema")
    if not isinstance(manifest_schema, dict):
        issues.append("knowledge manifest lacks transparent topic_schema block")
    else:
        if manifest_schema.get("version") != "1.0" or manifest_schema.get("type_property") != "тип/тема":
            issues.append("manifest topic schema version/type mismatch")
        if manifest_schema.get("required_tag_dimensions") != expected_dimensions:
            issues.append("manifest required tag dimensions differ from schema v1")
        if manifest_schema.get("optional_tag_dimensions") != ["возраст"]:
            issues.append("manifest optional tag dimensions differ from schema v1")
        if manifest_schema.get("relation_types") != ["нужно до", "следующий шаг", "открывает", "при аварии"]:
            issues.append("manifest relation vocabulary differs from schema v1")
        vocabulary = manifest_schema.get("controlled_tag_vocabulary")
        expected_vocabulary_keys = set(expected_dimensions) | {"возраст"}
        flattened_vocabulary: List[str] = []
        if not isinstance(vocabulary, dict) or set(map(str, vocabulary)) != expected_vocabulary_keys:
            issues.append("manifest controlled vocabulary dimensions differ from schema v1")
        else:
            for dimension in sorted(expected_vocabulary_keys):
                values = vocabulary.get(dimension)
                if not isinstance(values, list) or not all(isinstance(value, str) for value in values):
                    issues.append(f"manifest vocabulary dimension is not a string list: {dimension}")
                    continue
                if len(values) != len(set(values)):
                    issues.append(f"manifest vocabulary contains duplicates: {dimension}")
                if any(not value.startswith(dimension + "/") for value in values):
                    issues.append(f"manifest vocabulary has wrong tag prefix: {dimension}")
                flattened_vocabulary.extend(values)
        if len(flattened_vocabulary) != len(set(flattened_vocabulary)):
            issues.append("manifest controlled vocabulary contains cross-dimension duplicates")
        if set(flattened_vocabulary) != allowed_tags or len(flattened_vocabulary) != len(allowed_tags):
            issues.append("manifest controlled vocabulary does not exactly match schema enum")
        manifest_tags = manifest_schema.get("topic_tags")
        rendered_tags = {key: list(value) for key, value in id_to_tags.items()}
        if not isinstance(manifest_tags, dict) or rendered_tags != manifest_tags:
            issues.append("manifest topic_tags do not exactly match rendered topics")
        if set(map(str, manifest_schema.get("area_contours", []))) != set(contour_tags):
            issues.append("manifest area contours do not match rendered topics")

    validate_graph_config(graph, contour_tags, POSITIVE_GRAPH_FILTER, issues, "portable")
    if project_vault_enabled:
        validate_outer_graph_guard(project_graph, PROJECT_POSITIVE_GRAPH_FILTER, issues, "project")
    if parent_vault_enabled:
        validate_outer_graph_guard(parent_graph, PARENT_POSITIVE_GRAPH_FILTER, issues, "parent")
    for label, appearance, snippet_path, tokens in (
        (
            "project",
            project_appearance,
            PROJECT_SNIPPET,
            (
                'data-path="standards"',
                'data-path="Obsidian-Vault/90_GENERATED_CATALOG"',
                '.nav-file[data-path]:not([data-path*="/"])',
            ),
        ),
        (
            "parent",
            parent_appearance,
            PARENT_SNIPPET,
            (
                'data-path="autonomous-life-kit/standards"',
                'data-path="autonomous-life-kit/Obsidian-Vault/90_GENERATED_CATALOG"',
                'data-path^="autonomous-life-kit/"]:not([data-path^="autonomous-life-kit/Obsidian-Vault/"])',
            ),
        ),
    ):
        if label == "project" and not project_vault_enabled:
            continue
        if label == "parent" and not parent_vault_enabled:
            continue
        enabled_snippets = appearance.get("enabledCssSnippets")
        if not isinstance(enabled_snippets, list) or "01-понятный-режим" not in enabled_snippets:
            issues.append(f"{label} vault does not enable the human-readable CSS snippet")
        snippet_text = snippet_path.read_text(encoding="utf-8")
        for token in tokens:
            if token not in snippet_text:
                issues.append(f"{label} human-readable CSS snippet lacks selector: {token}")

    visual_rows: Set[Tuple[str, str, str]] = set()
    rows_by_kind: Dict[str, Set[Tuple[str, str, str]]] = defaultdict(set)
    for source, kind, target in semantic_rows:
        if kind == "Нужно до":
            visual_source, visual_target, label = target, source, "нужно сначала"
        else:
            visual_source, visual_target, label = source, target, kind.casefold()
        row = (visual_source + ".md", label, visual_target + ".md")
        visual_rows.add(row)
        rows_by_kind[kind].add(row)

    focused_education_ids = education_ids | {"картотека-тема-19", "картотека-тема-23", "картотека-тема-25", "картотека-тема-27"}
    education_files = {target + ".md" for target, identifier in target_to_id.items() if identifier in focused_education_ids}
    education_rows = {row for row in visual_rows if row[0] in education_files and row[2] in education_files}
    all_topic_files = {target + ".md" for target in topic_targets}
    emergency_files = {value for row in rows_by_kind["При аварии"] for value in (row[0], row[2])}
    canvas_expectations = {
        "01 — Что нужно сначала.canvas": (rows_by_kind["Нужно до"], all_topic_files),
        "02 — Следующие шаги и возможности.canvas": (rows_by_kind["Следующий шаг"] | rows_by_kind["Открывает"], all_topic_files),
        "03 — Что открывать при аварии.canvas": (rows_by_kind["При аварии"], emergency_files),
        "04 — Образовательная лестница.canvas": (education_rows, education_files),
        "05 — Все смысловые связи.canvas": (visual_rows, all_topic_files),
    }
    canvas_counts: Dict[str, Tuple[int, int]] = {}
    for path in canvas_files:
        expected_rows, expected_files = canvas_expectations[path.name]
        canvas_counts[path.name] = validate_canvas(path, expected_rows, expected_files, issues)

    no_incoming = sum(1 for target in topic_targets if not incoming[target])
    print(
        "obsidian_semantic_graph_summary "
        f"topics={len(topic_files)} routes={len(route_files)} semantic_edges={len(semantic_rows)} "
        f"future_cards={future_cards} contours={len(contour_tags)} no_incoming={no_incoming} "
        f"orphans={len(orphans)} reciprocal_pairs={len(reciprocals)} prerequisite_cycles={0 if visited == len(topic_targets) else 1}"
    )
    print("relation_types " + " ".join(f"{key}={relation_counts[key]}" for key in EXPECTED_RELATION_COUNTS))
    print("canvas_maps " + " ".join(f"{name}:{counts[0]}n/{counts[1]}e" for name, counts in sorted(canvas_counts.items())))
    print("runtime_boundary canonical_vault=Obsidian-Vault outer_vaults=guard_only_not_semantic_runtime")
    print(
        "PROOF_BOUNDARY structure_and_schema_only; not_card_content; not_specialist_review; "
        "not_physical_inventory; not_functional_test; not_release"
    )
    if issues:
        for issue in issues:
            print(f"ERROR {issue}", file=sys.stderr)
        print(f"result=FAIL issues={len(issues)}", file=sys.stderr)
        return 1
    print("result=PASS scope=CANONICAL_OBSIDIAN_TOPIC_GRAPH_METADATA_AND_CANVAS_STRUCTURE_ONLY")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
