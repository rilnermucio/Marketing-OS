"""Detects broken symlinks in the project tree."""
from __future__ import annotations

import subprocess
from pathlib import Path


EXCLUDE_DIRS = {".git", "node_modules", ".pytest_cache", "__pycache__"}


def test_no_dangling_symlinks(project_root: Path) -> None:
    result = subprocess.run(
        ["find", str(project_root), "-type", "l", "!", "-name", ".git"],
        capture_output=True, text=True,
    )
    all_symlinks = [Path(line) for line in result.stdout.splitlines() if line.strip()]
    filtered = [
        s for s in all_symlinks
        if not any(part in EXCLUDE_DIRS for part in s.parts)
    ]
    dangling = [s for s in filtered if not s.resolve().exists()]
    assert not dangling, f"Dangling symlinks found:\n" + "\n".join(str(d) for d in dangling)
