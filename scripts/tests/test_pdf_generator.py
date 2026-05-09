"""Tests for pdf_generator.py (markdown → PDF, white-label aware)."""
from __future__ import annotations

import json
import os
import sys
from pathlib import Path

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pytest

from pdf_generator import generate, _build_html


class TestBasicGenerate:
    def test_generate_creates_non_empty_pdf(self, tmp_path: Path):
        md_path = tmp_path / "report.md"
        md_path.write_text("# Test\n\nSome content.")
        out_path = tmp_path / "report.pdf"
        result = generate(md_path, out_path)
        assert result == out_path
        assert out_path.exists()
        assert out_path.stat().st_size > 100

    def test_generate_renders_tables(self, tmp_path: Path):
        md_path = tmp_path / "report.md"
        md_path.write_text("| A | B |\n|---|---|\n| 1 | 2 |\n")
        out_path = tmp_path / "report.pdf"
        generate(md_path, out_path)
        assert out_path.exists()


class TestBuildHTML:
    def test_html_contains_markdown_h1(self):
        html = _build_html("# Hello\n\nBody.", config=None)
        assert "<h1>" in html
        assert "Hello" in html

    def test_html_default_theme_when_no_config(self):
        html = _build_html("# X", config=None)
        assert "marketing-os" in html.lower()
        assert "#1a73e8" in html
