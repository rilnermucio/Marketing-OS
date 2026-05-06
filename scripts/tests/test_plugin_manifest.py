"""Validates plugin.json structure."""
from __future__ import annotations

import json
from pathlib import Path

import pytest


REQUIRED_FIELDS = {"name", "version", "description"}
EXPECTED_NAME = "marketing-os"


@pytest.fixture(scope="module")
def plugin_manifest(project_root: Path) -> dict:
    manifest_path = project_root / "plugin.json"
    assert manifest_path.exists(), f"plugin.json missing: {manifest_path}"
    return json.loads(manifest_path.read_text(encoding="utf-8"))


def test_plugin_manifest_is_valid_json(plugin_manifest: dict) -> None:
    assert isinstance(plugin_manifest, dict)


def test_plugin_manifest_has_required_fields(plugin_manifest: dict) -> None:
    missing = REQUIRED_FIELDS - set(plugin_manifest.keys())
    assert not missing, f"plugin.json missing required fields: {missing}"


def test_plugin_manifest_name(plugin_manifest: dict) -> None:
    assert plugin_manifest["name"] == EXPECTED_NAME


def test_plugin_manifest_version_is_semver(plugin_manifest: dict) -> None:
    version = plugin_manifest["version"]
    parts = version.split(".")
    assert len(parts) == 3, f"Version not semver: {version}"
    for part in parts:
        assert part.isdigit(), f"Non-numeric version part: {part}"


def test_plugin_manifest_skills_paths_exist(plugin_manifest: dict, project_root: Path) -> None:
    skills = plugin_manifest.get("skills", [])
    for skill_path in skills:
        full = project_root / skill_path
        assert full.exists(), f"plugin.json declares skill at {skill_path} but path does not exist"
