"""Tests for pdf_generator.py (markdown → PDF, white-label aware)."""
from __future__ import annotations

import json
import os
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pytest

from pdf_generator import generate, _build_html

SCRIPT = Path(__file__).resolve().parent.parent / "pdf_generator.py"


def _run_cli(args, out_path: Path, retries: int = 1, timeout: int = 120):
    """Run the pdf_generator CLI robustly.

    weasyprint (fontconfig/pango/cairo) can fail transiently under load, so we
    retry once and only assert on the final attempt. A real breakage (rc != 0
    on every try) surfaces stderr instead of a bare CalledProcessError.
    """
    last = None
    for _ in range(retries + 1):
        last = subprocess.run(
            [sys.executable, str(SCRIPT), *args],
            capture_output=True, text=True, timeout=timeout,
        )
        if last.returncode == 0 and out_path.exists():
            return last
    raise AssertionError(
        f"pdf_generator CLI falhou após {retries + 1} tentativas "
        f"(rc={last.returncode}):\nSTDERR:\n{last.stderr[:800]}"
    )


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


class TestWhiteLabel:
    def test_config_brand_name_in_html(self, tmp_path: Path):
        config = {"brand_name": "Agência X"}
        html = _build_html("# X", config=config)
        assert "Agência X" in html

    def test_config_accent_color_in_html(self):
        config = {"brand_name": "X", "accent_color": "#ff0000"}
        html = _build_html("# X", config=config)
        assert "#ff0000" in html
        assert "#1a73e8" not in html

    def test_config_footer_text_in_html(self):
        config = {"brand_name": "X", "footer_text": "© Cliente Y"}
        html = _build_html("# X", config=config)
        assert "© Cliente Y" in html

    def test_logo_present_when_path_exists(self, tmp_path: Path):
        logo = tmp_path / "logo.png"
        logo.write_bytes(b"fake png")
        config = {"brand_name": "X", "logo_path": str(logo)}
        html = _build_html("# X", config=config)
        assert '<img class="header-logo"' in html

    def test_logo_omitted_when_path_missing(self, tmp_path: Path):
        config = {"brand_name": "X", "logo_path": str(tmp_path / "nonexistent.png")}
        html = _build_html("# X", config=config)
        assert '<img class="header-logo"' not in html

    def test_logo_missing_warning_to_stderr(self, tmp_path: Path, capsys):
        config = {"brand_name": "X", "logo_path": str(tmp_path / "nonexistent.png")}
        _build_html("# X", config=config)
        captured = capsys.readouterr()
        assert "não encontrado" in captured.err

    def test_generate_with_config_path(self, tmp_path: Path):
        md = tmp_path / "r.md"
        md.write_text("# Title")
        cfg = tmp_path / "cfg.json"
        cfg.write_text(json.dumps({"brand_name": "Acme"}))
        out = tmp_path / "r.pdf"
        generate(md, out, cfg)
        assert out.exists()
        assert out.stat().st_size > 100

    def test_footer_with_double_quotes_escaped(self):
        config = {"brand_name": "X", "footer_text": 'He said "hi"'}
        html = _build_html("# X", config=config)
        # Backslash-escaped double quotes appear in CSS
        assert 'said \\"hi\\"' in html


class TestBuildHTMLBraces:
    def test_html_handles_braces_in_markdown(self):
        # Markdown with code block containing braces should not crash format()
        md_text = '# Title\n\nExample: `{"key": "value"}` and `{x: 1, y: 2}`'
        html = _build_html(md_text, config=None)
        # markdown-it HTML-encodes quotes inside code spans: " → &quot;
        assert "key" in html
        assert "y: 2" in html
        # Verify <code> tags rendered, not crashed
        assert "<code>" in html


class TestPDFCLI:
    def test_cli_basic(self, tmp_path: Path):
        md = tmp_path / "r.md"
        md.write_text("# CLI Test")
        out = tmp_path / "r.pdf"
        _run_cli([str(md), str(out)], out)
        assert out.exists()

    def test_cli_with_config(self, tmp_path: Path):
        md = tmp_path / "r.md"
        md.write_text("# Configured")
        cfg = tmp_path / "cfg.json"
        cfg.write_text(json.dumps({"brand_name": "Brand X"}))
        out = tmp_path / "r.pdf"
        _run_cli([str(md), str(out), str(cfg)], out)
        assert out.exists()

    def test_cli_too_few_args_exits_nonzero(self):
        script = Path(__file__).resolve().parent.parent / "pdf_generator.py"
        result = subprocess.run(
            [sys.executable, str(script)],
            capture_output=True, text=True,
        )
        assert result.returncode != 0
        assert "Usage" in result.stderr


class TestFromHtml:
    def test_from_html_generates_pdf(self, tmp_path: Path):
        html_path = tmp_path / "report.html"
        html_path.write_text("<!DOCTYPE html><html><body><h1>HTML Test</h1></body></html>")
        out_path = tmp_path / "report.pdf"
        result = generate(html_path, out_path, from_html=True)
        assert result == out_path
        assert out_path.exists()
        assert out_path.stat().st_size > 100

    def test_html_extension_auto_detects(self, tmp_path: Path):
        html_path = tmp_path / "report.html"
        html_path.write_text("<!DOCTYPE html><html><body>Auto</body></html>")
        out_path = tmp_path / "report.pdf"
        # Default from_html=False, but extension is .html → auto-detect
        result = generate(html_path, out_path)
        assert out_path.exists()

    def test_cli_from_html_flag(self, tmp_path: Path):
        html = tmp_path / "x.html"
        html.write_text("<html><body>X</body></html>")
        out = tmp_path / "x.pdf"
        script = Path(__file__).resolve().parent.parent / "pdf_generator.py"
        result = subprocess.run(
            [sys.executable, str(script), "--from-html", str(html), str(out)],
            capture_output=True, text=True, check=True,
        )
        assert out.exists()
