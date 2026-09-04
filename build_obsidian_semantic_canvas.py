#!/usr/bin/env python3
"""Build readable, labelled JSON Canvas maps for the Obsidian topic graph.

The Core Graph remains a compact 32-node overview.  These canvases carry the
relationship labels that Core Graph cannot display.  A ``нужно до`` edge is
reversed visually so every prerequisite canvas reads left-to-right as
``что нужно сначала -> что оно позволяет делать``.
"""

from __future__ import annotations

from collections import Counter, defaultdict, deque
import hashlib
import json
import os
from pathlib import Path
import tempfile
from typing import Dict, Iterable, List, Mapping, Sequence, Set, Tuple

from build_obsidian_knowledge_routes import (
    OUT as KNOWLEDGE_ROOT,
    RELATION_TYPES,
    SEMANTIC_RELATIONS,
    TOPIC_DOMAIN_TAG,
    TOPICS,
    VAULT,
)


OUT = KNOWLEDGE_ROOT / "03 — Карты связей"
MANIFEST = OUT / ".generated-semantic-canvas-manifest.json"
GENERATOR_ID = "build_obsidian_semantic_canvas.py"

CANVAS_NAMES = {
    "prerequisites": "01 — Что нужно сначала.canvas",
    "progress": "02 — Следующие шаги и возможности.canvas",
    "emergency": "03 — Что открывать при аварии.canvas",
    "education": "04 — Образовательная лестница.canvas",
    "all": "05 — Все смысловые связи.canvas",
}

CONTOUR_COLORS: Mapping[str, str] = {
    "безопасность": "#D1495B",
    "жизнеобеспечение": "#2A9D8F",
    "здоровье": "#E76F51",
    "питание": "#6A994E",
    "место": "#457B9D",
    "энергия": "#F4A261",
    "мастерская": "#8D6E63",
    "общество": "#7B2CBF",
    "знания": "#3A86FF",
    "готовность": "#F6BD60",
}

RELATION_LABELS: Mapping[str, str] = {
    "нужно до": "нужно сначала",
    "следующий шаг": "следующий шаг",
    "открывает": "открывает",
    "при аварии": "при аварии",
}

RELATION_COLORS: Mapping[str, str] = {
    "нужно до": "#5B6472",
    "следующий шаг": "#2A9D8F",
    "открывает": "#3A86FF",
    "при аварии": "#D1495B",
}


class CanvasBuildError(RuntimeError):
    pass


def stable_id(kind: str, *parts: str) -> str:
    digest = hashlib.sha256("\0".join((kind, *parts)).encode("utf-8")).hexdigest()
    return digest[:16]


def contour(topic_key: str) -> str:
    parts = TOPIC_DOMAIN_TAG[topic_key].split("/")
    if len(parts) != 3 or parts[0] != "область":
        raise CanvasBuildError(f"invalid domain tag for {topic_key}: {TOPIC_DOMAIN_TAG[topic_key]}")
    if parts[1] not in CONTOUR_COLORS:
        raise CanvasBuildError(f"missing canvas color for contour {parts[1]}")
    return parts[1]


def topic_number(topic_key: str) -> int:
    return int(Path(TOPICS[topic_key].filename).name.split(" — ", 1)[0])


def topic_node(topic_key: str, x: int, y: int) -> Dict[str, object]:
    return {
        "id": stable_id("node", topic_key),
        "type": "file",
        "file": f"{KNOWLEDGE_ROOT.name}/{TOPICS[topic_key].filename}",
        "x": int(x),
        "y": int(y),
        "width": 420,
        "height": 170,
        "color": CONTOUR_COLORS[contour(topic_key)],
    }


def text_node(key: str, text: str, x: int, y: int, width: int = 760, height: int = 220) -> Dict[str, object]:
    return {
        "id": stable_id("text", key),
        "type": "text",
        "text": text,
        "x": int(x),
        "y": int(y),
        "width": int(width),
        "height": int(height),
    }


def selected_relations(kinds: Iterable[str], topic_keys: Set[str] | None = None) -> List[Tuple[str, str, str]]:
    allowed = set(kinds)
    rows: List[Tuple[str, str, str]] = []
    for source, relations in SEMANTIC_RELATIONS.items():
        for relation_type, target in relations:
            if relation_type not in allowed:
                continue
            if topic_keys is not None and (source not in topic_keys or target not in topic_keys):
                continue
            rows.append((source, relation_type, target))
    return rows


def visual_direction(source: str, relation_type: str, target: str) -> Tuple[str, str]:
    # Markdown reads "A needs B first".  Canvas reads chronologically B -> A.
    return (target, source) if relation_type == "нужно до" else (source, target)


def relation_edges(rows: Sequence[Tuple[str, str, str]]) -> List[Dict[str, object]]:
    result: List[Dict[str, object]] = []
    seen: Set[Tuple[str, str, str]] = set()
    for source, relation_type, target in rows:
        if relation_type not in RELATION_TYPES:
            raise CanvasBuildError(f"unknown relation type: {relation_type}")
        visual_from, visual_to = visual_direction(source, relation_type, target)
        key = (visual_from, relation_type, visual_to)
        if key in seen:
            raise CanvasBuildError(f"duplicate canvas edge: {key}")
        seen.add(key)
        result.append(
            {
                "id": stable_id("edge", visual_from, relation_type, visual_to),
                "fromNode": stable_id("node", visual_from),
                "fromSide": "right",
                "toNode": stable_id("node", visual_to),
                "toSide": "left",
                "toEnd": "arrow",
                "label": RELATION_LABELS[relation_type],
                "color": RELATION_COLORS[relation_type],
            }
        )
    return result


def topological_positions(topic_keys: Set[str], rows: Sequence[Tuple[str, str, str]]) -> Dict[str, Tuple[int, int]]:
    children: Dict[str, List[str]] = {key: [] for key in topic_keys}
    indegree: Dict[str, int] = {key: 0 for key in topic_keys}
    for source, relation_type, target in rows:
        if relation_type != "нужно до":
            continue
        prerequisite, dependent = target, source
        children[prerequisite].append(dependent)
        indegree[dependent] += 1

    queue = deque(sorted((key for key, value in indegree.items() if value == 0), key=topic_number))
    layer: Dict[str, int] = {key: 0 for key in topic_keys}
    visited = 0
    while queue:
        current = queue.popleft()
        visited += 1
        for child in sorted(children[current], key=topic_number):
            layer[child] = max(layer[child], layer[current] + 1)
            indegree[child] -= 1
            if indegree[child] == 0:
                queue.append(child)
    if visited != len(topic_keys):
        raise CanvasBuildError("цикл в связях «нужно до»")

    by_layer: Dict[int, List[str]] = defaultdict(list)
    for key in topic_keys:
        by_layer[layer[key]].append(key)
    positions: Dict[str, Tuple[int, int]] = {}
    for layer_number, keys in sorted(by_layer.items()):
        ordered = sorted(keys, key=lambda key: (contour(key), topic_number(key)))
        for row_number, key in enumerate(ordered):
            positions[key] = (layer_number * 620, row_number * 240)
    return positions


def domain_layout(topic_keys: Set[str]) -> Tuple[List[Dict[str, object]], Dict[str, Tuple[int, int]]]:
    by_contour: Dict[str, List[str]] = defaultdict(list)
    for key in topic_keys:
        by_contour[contour(key)].append(key)
    groups: List[Dict[str, object]] = []
    positions: Dict[str, Tuple[int, int]] = {}
    for index, contour_name in enumerate(CONTOUR_COLORS):
        keys = sorted(by_contour.get(contour_name, []), key=topic_number)
        if not keys:
            continue
        column = index % 5
        row = index // 5
        x = column * 600
        y = row * 1700
        height = max(390, 130 + len(keys) * 205)
        groups.append(
            {
                "id": stable_id("group", contour_name),
                "type": "group",
                "label": contour_name.capitalize(),
                "x": x,
                "y": y,
                "width": 520,
                "height": height,
                "color": CONTOUR_COLORS[contour_name],
            }
        )
        for item, key in enumerate(keys):
            positions[key] = (x + 50, y + 90 + item * 195)
    return groups, positions


def canvas(
    title: str,
    explanation: str,
    rows: Sequence[Tuple[str, str, str]],
    topic_keys: Set[str],
    *,
    layout: str,
) -> Dict[str, object]:
    if layout == "prerequisites":
        positions = topological_positions(topic_keys, rows)
        groups: List[Dict[str, object]] = []
    elif layout == "domains":
        groups, positions = domain_layout(topic_keys)
    else:
        raise CanvasBuildError(f"unknown layout: {layout}")
    legend_y = min((y for _, y in positions.values()), default=0) - 330
    nodes: List[Dict[str, object]] = list(groups)
    nodes.append(text_node(title, f"# {title}\n\n{explanation}", 0, legend_y, 1050, 230))
    nodes.extend(topic_node(key, *positions[key]) for key in sorted(topic_keys, key=topic_number))
    edges = relation_edges(rows)
    node_ids = {str(node["id"]) for node in nodes}
    for edge in edges:
        if edge["fromNode"] not in node_ids or edge["toNode"] not in node_ids:
            raise CanvasBuildError(f"dangling edge in {title}: {edge}")
    return {"nodes": nodes, "edges": edges}


def build_canvases() -> Dict[str, Dict[str, object]]:
    all_keys = set(TOPICS)
    prerequisites = selected_relations(("нужно до",))
    progress = selected_relations(("следующий шаг", "открывает"))
    emergency = selected_relations(("при аварии",))
    emergency_keys = {key for source, _, target in emergency for key in (source, target)}
    education_keys = {
        "group",
        "offline",
        "measurement",
        "early_education",
        "school_education",
        "higher_education",
        "recovery",
    }
    education = selected_relations(RELATION_TYPES, education_keys)
    all_rows = selected_relations(RELATION_TYPES)

    return {
        CANVAS_NAMES["prerequisites"]: canvas(
            "Что нужно сначала",
            "Читайте слева направо. Стрелка ведёт от предпосылки к тому, что она позволяет делать. Это карта порядка, а не доказательство готовности.",
            prerequisites,
            all_keys,
            layout="prerequisites",
        ),
        CANVAS_NAMES["progress"]: canvas(
            "Следующие шаги и возможности",
            "Зелёная линия — логичный следующий шаг. Синяя — что тема открывает. Узлы собраны в десять понятных областей.",
            progress,
            all_keys,
            layout="domains",
        ),
        CANVAS_NAMES["emergency"]: canvas(
            "Что открывать при аварии",
            "Красная линия ведёт от области происшествия к медицинскому порядку реагирования. Карта не заменяет экстренную службу или обучение.",
            emergency,
            emergency_keys,
            layout="domains",
        ),
        CANVAS_NAMES["education"]: canvas(
            "Образовательная лестница",
            "От безопасной среды и офлайн-архива — к дошкольной, школьной, профессиональной и университетской ступени; далее — к межпоколенческому восстановлению технологий.",
            education,
            education_keys,
            layout="prerequisites",
        ),
        CANVAS_NAMES["all"]: canvas(
            "Все смысловые связи",
            "Полная аудиторская карта. Она намеренно плотная: для обычной работы лучше открывать три разделённые карты выше. Каждая линия подписана и направлена.",
            all_rows,
            all_keys,
            layout="domains",
        ),
    }


def encoded(value: object) -> str:
    return json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True) + "\n"


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def semantic_hash(value: object) -> str:
    canonical = json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
    return sha256_text(canonical)


def semantic_file_hash(path: Path) -> str:
    return semantic_hash(json.loads(path.read_text(encoding="utf-8")))


def write_atomic(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile("w", encoding="utf-8", dir=path.parent, prefix=".canvas-tmp-", delete=False) as handle:
        temporary = Path(handle.name)
        handle.write(text)
        handle.flush()
        os.fsync(handle.fileno())
    try:
        os.chmod(temporary, 0o644)
        os.replace(temporary, path)
        os.chmod(path, 0o644)
    finally:
        if temporary.exists():
            temporary.unlink()


def load_manifest() -> Tuple[Set[str], Dict[str, str], str]:
    if not MANIFEST.exists():
        return set(), {}, "canonical-json"
    data = json.loads(MANIFEST.read_text(encoding="utf-8"))
    if data.get("generator") != GENERATOR_ID:
        raise CanvasBuildError("canvas manifest belongs to another generator")
    names = data.get("generated_files")
    hashes = data.get("generated_sha256")
    if not isinstance(names, list) or not isinstance(hashes, dict):
        raise CanvasBuildError("invalid canvas manifest")
    return set(names), {str(key): str(value) for key, value in hashes.items()}, str(data.get("hash_mode", "raw-bytes"))


def safe_target(name: str) -> Path:
    relative = Path(name)
    if relative.name != name or relative.suffix != ".canvas" or name.startswith("."):
        raise CanvasBuildError(f"unsafe canvas name: {name!r}")
    target = OUT / name
    if OUT.is_symlink():
        raise CanvasBuildError(f"refusing symlinked canvas directory: {OUT}")
    resolved_out = OUT.resolve()
    if resolved_out.parent != KNOWLEDGE_ROOT.resolve():
        raise CanvasBuildError(f"canvas directory escapes knowledge root: {OUT}")
    resolved_parent = target.parent.resolve()
    if resolved_parent != resolved_out:
        raise CanvasBuildError(f"canvas path escapes owned directory through a symlink: {target}")
    if target.is_symlink():
        raise CanvasBuildError(f"refusing symlink target: {target}")
    return target


def write_canvases(values: Mapping[str, Dict[str, object]]) -> Dict[str, int]:
    OUT.mkdir(parents=True, exist_ok=True)
    rendered = {name: encoded(value) for name, value in values.items()}
    old_names, old_hashes, old_hash_mode = load_manifest()
    desired = set(rendered)
    counts = {"created": 0, "updated": 0, "unchanged": 0, "deleted": 0}

    for name in sorted(old_names - desired):
        target = safe_target(name)
        if target.exists():
            current_hash = semantic_file_hash(target) if old_hash_mode == "canonical-json" else hashlib.sha256(target.read_bytes()).hexdigest()
            if name in old_hashes and current_hash != old_hashes[name]:
                raise CanvasBuildError(f"refusing to delete manually changed canvas: {target}")
            target.unlink()
            counts["deleted"] += 1

    for name in sorted(desired):
        target = safe_target(name)
        if target.exists() and name not in old_names:
            raise CanvasBuildError(f"refusing to overwrite unmanifested canvas: {target}")
        current = target.read_text(encoding="utf-8") if target.exists() else None
        if current == rendered[name]:
            os.chmod(target, 0o644)
            counts["unchanged"] += 1
            continue
        if target.exists() and json.loads(current) == values[name]:
            # Obsidian canonically rewrites whitespace/order when a canvas is
            # opened.  Preserve that harmless formatting while comparing the
            # actual JSON structure for overwrite protection.
            os.chmod(target, 0o644)
            counts["unchanged"] += 1
            continue
        current_hash = semantic_file_hash(target) if target.exists() and old_hash_mode == "canonical-json" else hashlib.sha256(target.read_bytes()).hexdigest() if target.exists() else ""
        if target.exists() and name in old_hashes and current_hash != old_hashes[name]:
            raise CanvasBuildError(f"refusing to overwrite manually changed canvas: {target}")
        write_atomic(target, rendered[name])
        counts["created" if current is None else "updated"] += 1

    relation_counts = Counter(kind for relations in SEMANTIC_RELATIONS.values() for kind, _ in relations)
    manifest = {
        "version": 2,
        "generator": GENERATOR_ID,
        "hash_mode": "canonical-json",
        "generated_files": sorted(desired),
        "generated_sha256": {name: semantic_hash(values[name]) for name in sorted(desired)},
        "topic_nodes": len(TOPICS),
        "semantic_edges": sum(relation_counts.values()),
        "relation_counts": dict(sorted(relation_counts.items())),
        "visual_direction_rule": {"нужно до": "предпосылка -> зависимая тема"},
        "proof_boundary": "Карта связей, не доказательство готовности или верности процедур.",
    }
    manifest_text = encoded(manifest)
    if not MANIFEST.exists() or MANIFEST.read_text(encoding="utf-8") != manifest_text:
        write_atomic(MANIFEST, manifest_text)
    else:
        os.chmod(MANIFEST, 0o644)
    return counts


def main() -> int:
    try:
        values = build_canvases()
        counts = write_canvases(values)
    except (CanvasBuildError, OSError, ValueError, json.JSONDecodeError) as exc:
        print(f"semantic_canvas_build_error {exc}", file=os.sys.stderr)
        return 1
    print(
        "semantic_canvas_build_ok "
        f"canvases={len(values)} topics={len(TOPICS)} "
        f"semantic_edges={sum(len(value) for value in SEMANTIC_RELATIONS.values())} "
        + " ".join(f"{key}={value}" for key, value in counts.items())
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
