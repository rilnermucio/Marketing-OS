"""Validates skills/marketing-os/SKILL.md frontmatter."""
from __future__ import annotations

from pathlib import Path

import pytest


REQUIRED_SKILL_FIELDS = {"name", "description"}


def _parse_frontmatter(content: str) -> dict | None:
    if not content.startswith("---\n"):
        return None
    end = content.find("\n---", 4)
    if end == -1:
        return None
    fm = content[4:end]
    result: dict = {}
    for line in fm.splitlines():
        line = line.strip()
        if not line or line.startswith("#") or ":" not in line:
            continue
        key, _, value = line.partition(":")
        result[key.strip()] = value.strip().strip('"').strip("'")
    return result


@pytest.fixture(scope="module")
def skill_md(project_root: Path) -> tuple[dict, str]:
    skill_path = project_root / "skills" / "marketing-os" / "SKILL.md"
    assert skill_path.exists(), f"SKILL.md missing: {skill_path}"
    content = skill_path.read_text(encoding="utf-8")
    fm = _parse_frontmatter(content)
    assert fm is not None, "SKILL.md has no YAML frontmatter"
    return fm, content


def test_skill_md_has_required_fields(skill_md: tuple[dict, str]) -> None:
    fm, _ = skill_md
    missing = REQUIRED_SKILL_FIELDS - set(fm.keys())
    assert not missing, f"SKILL.md missing required frontmatter fields: {missing}"


def test_skill_md_name_matches_plugin(skill_md: tuple[dict, str], project_root: Path) -> None:
    import json
    fm, _ = skill_md
    plugin = json.loads((project_root / ".claude-plugin" / "plugin.json").read_text(encoding="utf-8"))
    assert fm["name"] == plugin["name"], (
        f"SKILL.md name='{fm['name']}' should match plugin.json name='{plugin['name']}'"
    )


def test_skill_md_body_not_empty(skill_md: tuple[dict, str]) -> None:
    _, content = skill_md
    body_after_fm = content.split("---", 2)[-1]
    assert len(body_after_fm.strip()) > 100
