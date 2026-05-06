"""Validates subagents/ knowledge base files."""
from __future__ import annotations

from pathlib import Path

import pytest


_SUBAGENTS = sorted((Path(__file__).parent.parent.parent / "subagents").rglob("*.md"))


def test_subagents_dir_exists(project_root: Path) -> None:
    assert (project_root / "subagents").is_dir()


def test_subagents_dir_has_files(project_root: Path) -> None:
    md_files = list((project_root / "subagents").rglob("*.md"))
    assert len(md_files) > 0


@pytest.mark.parametrize("path", _SUBAGENTS, ids=lambda p: p.name)
def test_subagent_file_readable_and_nonempty(path: Path) -> None:
    content = path.read_text(encoding="utf-8")
    assert len(content) > 50, f"Subagent file suspiciously short: {path.name}"


@pytest.mark.parametrize("path", _SUBAGENTS, ids=lambda p: p.name)
def test_subagent_has_heading(path: Path) -> None:
    content = path.read_text(encoding="utf-8")
    assert "# " in content or "## " in content, f"No markdown headings in {path.name}"
