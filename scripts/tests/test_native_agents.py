"""Wraps scripts/validate_agents.py in pytest. Validates .claude/agents/ native subagents."""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

import pytest


def test_validate_agents_script_exists(project_root: Path) -> None:
    script = project_root / "scripts" / "validate_agents.py"
    assert script.exists(), f"validate_agents.py missing: {script}"


def test_native_agents_dir_exists_or_skip(project_root: Path) -> None:
    agents_dir = project_root / ".claude" / "agents"
    if not agents_dir.is_dir():
        pytest.skip(f".claude/agents/ does not exist (gitignored, only on main local checkout)")


def test_native_agents_validate_clean(project_root: Path) -> None:
    """Run validate_agents.py and ensure exit code 0 (no errors, warnings allowed)."""
    agents_dir = project_root / ".claude" / "agents"
    if not agents_dir.is_dir():
        pytest.skip(".claude/agents/ does not exist in this checkout")
    result = subprocess.run(
        [sys.executable, "scripts/validate_agents.py"],
        capture_output=True,
        text=True,
        cwd=str(project_root),
        timeout=60,
    )
    assert result.returncode == 0, (
        f"validate_agents.py failed (exit {result.returncode}):\n"
        f"STDOUT:\n{result.stdout}\nSTDERR:\n{result.stderr}"
    )
