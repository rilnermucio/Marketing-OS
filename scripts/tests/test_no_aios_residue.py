"""Detects residual references to the AIOS framework after Phase 3."""
from __future__ import annotations

from pathlib import Path

import pytest


AIOS_PATTERNS = [
    "@aios-master",
    "@aios",
    ".aios-core",
    "Synkra AIOS",
    "AIOS-MANAGED",
    "story-driven development",
    "IDS gate",
    "@po ",
    "@sm ",
    "@architect",
    "@devops",
    "QA Loop",
]

# Search inside tracked plugin content
SEARCH_ROOTS = ["skills", "subagents", "commands", "workflows", "assets", "references", "scripts", "docs"]
EXCLUDE_FILES = {
    # Historical/contextual mentions are legitimate
    "CHANGELOG.md",
    "2026-05-06-marketing-os-plugin-first-refactor-design.md",
    "2026-05-06-marketing-os-plugin-first-refactor.md",
    # User-facing docs rewritten in Phase 4
    "README.md",
    "GUIA-DE-USO.md",
    "INSTALACAO-SKILL.md",
    # Tests that legitimately reference AIOS strings as patterns to detect
    "test_no_aios_residue.py",
}
EXCLUDE_DIRS = {"snapshots", "clones"}  # voice clones may legitimately mention domain terms


@pytest.mark.aios_removed
def test_no_aios_strings_in_content(project_root: Path) -> None:
    leaks: list[str] = []
    for root in SEARCH_ROOTS:
        d = project_root / root
        if not d.exists():
            continue
        for path in d.rglob("*"):
            if not path.is_file():
                continue
            if path.name in EXCLUDE_FILES:
                continue
            if any(part in EXCLUDE_DIRS for part in path.parts):
                continue
            if path.suffix not in {".md", ".yaml", ".yml", ".json", ".py", ".txt"}:
                continue
            try:
                content = path.read_text(encoding="utf-8")
            except UnicodeDecodeError:
                continue
            for pattern in AIOS_PATTERNS:
                if pattern in content:
                    leaks.append(f"{path.relative_to(project_root)}: contains '{pattern}'")
                    break
    assert not leaks, "AIOS residue found:\n" + "\n".join(sorted(set(leaks))[:30])
