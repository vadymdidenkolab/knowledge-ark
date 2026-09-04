#!/usr/bin/env python3
"""Write the canonical graph and quiet guards for accidentally opened parents.

Only ``Obsidian-Vault`` is a semantic runtime: its wiki links and Canvas file
paths are relative to that root.  The two optional outer-vault configurations
are deliberately noise-suppression guards, not alternative working graphs.
"""

from __future__ import annotations

from collections import defaultdict
import json
import os
from pathlib import Path
import tempfile
from typing import Dict, List, Tuple

from build_obsidian_knowledge_routes import ROOT, TOPIC_DOMAIN_TAG, VAULT
from build_obsidian_semantic_canvas import CONTOUR_COLORS


PORTABLE_GRAPH = VAULT / ".obsidian" / "graph.json"
PROJECT_GRAPH = ROOT / ".obsidian" / "graph.json"
PARENT_VAULT_ROOT = ROOT.parent
PARENT_GRAPH = PARENT_VAULT_ROOT / ".obsidian" / "graph.json"
PORTABLE_TOPIC_FILTER = 'path:"01 — КАРТОТЕКА ЗНАНИЙ/02 — Темы"'
PROJECT_TOPIC_FILTER = f'path:"{VAULT.name}/01 — КАРТОТЕКА ЗНАНИЙ/02 — Темы"'
PARENT_TOPIC_FILTER = f'path:"{ROOT.name}/{VAULT.name}/01 — КАРТОТЕКА ЗНАНИЙ/02 — Темы"'
BACKUP_NAME = "graph.before-autonomous-standardization.json"


def color_groups() -> List[Dict[str, object]]:
    by_contour: Dict[str, List[str]] = defaultdict(list)
    for tag in sorted(set(TOPIC_DOMAIN_TAG.values())):
        parts = tag.split("/")
        if len(parts) != 3 or parts[0] != "область":
            raise ValueError(f"invalid area tag: {tag}")
        by_contour[parts[1]].append(tag)
    if set(by_contour) != set(CONTOUR_COLORS):
        raise ValueError(f"contour mismatch: tags={sorted(by_contour)} colors={sorted(CONTOUR_COLORS)}")

    groups: List[Dict[str, object]] = []
    for contour, hex_color in CONTOUR_COLORS.items():
        exact_terms = [f"tag:#{tag}" for tag in by_contour[contour]]
        groups.append(
            {
                "query": "(" + " OR ".join(exact_terms) + ")",
                "color": {"a": 1, "rgb": int(hex_color[1:], 16)},
            }
        )
    return groups


def build_config(topic_filter: str) -> Dict[str, object]:
    return {
        "collapse-filter": False,
        "search": topic_filter,
        "showTags": False,
        "showAttachments": False,
        "hideUnresolved": True,
        "showOrphans": False,
        "collapse-color-groups": True,
        "colorGroups": color_groups(),
        "collapse-display": False,
        "showArrow": True,
        "textFadeMultiplier": 0.58,
        "nodeSizeMultiplier": 1.16,
        "lineSizeMultiplier": 1.2,
        "collapse-forces": False,
        "centerStrength": 0.42,
        "repelStrength": 12,
        "linkStrength": 0.82,
        "linkDistance": 170,
        "scale": 0.72,
        "close": False,
    }


def validate_target(vault_root: Path, path: Path) -> None:
    """Refuse ambiguous vaults and every symlinked write path."""
    obsidian = vault_root / ".obsidian"
    if vault_root.is_symlink() or obsidian.is_symlink() or path.is_symlink():
        raise OSError(f"refusing symlinked vault/config path: {path}")
    if not vault_root.is_dir() or not obsidian.is_dir():
        raise OSError(f"not an existing Obsidian vault: {vault_root}")
    expected_parent = vault_root.resolve(strict=True) / ".obsidian"
    if obsidian.resolve(strict=True) != expected_parent or path.parent.resolve(strict=True) != expected_parent:
        raise OSError(f"graph target escapes expected vault: {path}")


def write_atomic(path: Path, text: str) -> None:
    if path.parent.is_symlink() or path.is_symlink():
        raise OSError(f"refusing symlink target: {path}")
    with tempfile.NamedTemporaryFile("w", encoding="utf-8", dir=path.parent, prefix=".graph-tmp-", delete=False) as handle:
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


def load_existing(path: Path) -> Tuple[Dict[str, object], str | None]:
    if not path.exists():
        return {}, None
    text = path.read_text(encoding="utf-8")
    value = json.loads(text)
    if not isinstance(value, dict):
        raise ValueError(f"graph config root must be an object: {path}")
    return value, text


def standardized_config(existing: Dict[str, object], topic_filter: str) -> Dict[str, object]:
    """Own standard graph fields while preserving unknown Obsidian/plugin keys."""
    merged = dict(existing)
    merged.update(build_config(topic_filter))
    return merged


def main() -> int:
    candidates = (
        (VAULT, PORTABLE_GRAPH, PORTABLE_TOPIC_FILTER, "portable"),
        (ROOT, PROJECT_GRAPH, PROJECT_TOPIC_FILTER, "project"),
        (PARENT_VAULT_ROOT, PARENT_GRAPH, PARENT_TOPIC_FILTER, "parent"),
    )
    targets = []
    skipped: List[str] = []
    for vault_root, path, topic_filter, label in candidates:
        obsidian = vault_root / ".obsidian"
        if not obsidian.exists() and label != "portable":
            skipped.append(label)
            continue
        validate_target(vault_root, path)
        existing, original_text = load_existing(path)
        targets.append((path, standardized_config(existing, topic_filter), original_text, label))

    changed: Dict[str, bool] = {}
    prepared = []
    missing_backups = []
    for path, desired, original_text, label in targets:
        existing = json.loads(original_text) if original_text is not None else None
        changed[label] = existing != desired
        if not changed[label]:
            continue
        rendered = json.dumps(desired, ensure_ascii=False, indent=2) + "\n"
        if original_text is not None:
            backup = path.with_name(BACKUP_NAME)
            if os.path.lexists(backup):
                if backup.is_symlink() or not backup.is_file():
                    raise OSError(f"invalid graph backup target: {backup}")
            else:
                missing_backups.append((backup, original_text))
        prepared.append((path, rendered))

    # No mutation occurs before every config and backup target has passed the
    # common preflight above.  Backups are then persisted before graph files.
    for backup, original_text in missing_backups:
        write_atomic(backup, original_text)
    for path, rendered in prepared:
        write_atomic(path, rendered)

    status = " ".join(
        f"{label}_changed={str(changed.get(label, False)).lower()}" for label in ("portable", "project", "parent")
    )
    print(
        "obsidian_graph_config_ok "
        f"{status} skipped={json.dumps(skipped, ensure_ascii=False)} "
        "canonical_vault=Obsidian-Vault outer_vaults=guard_only_not_semantic_runtime "
        f"portable_filter={json.dumps(PORTABLE_TOPIC_FILTER, ensure_ascii=False)} "
        f"project_filter={json.dumps(PROJECT_TOPIC_FILTER, ensure_ascii=False)} "
        f"parent_filter={json.dumps(PARENT_TOPIC_FILTER, ensure_ascii=False)} "
        f"color_groups={len(color_groups())} arrows=true unresolved=false orphans=false"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
