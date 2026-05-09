"""Tests for audit_screenshot.py.

Real Playwright runs are marked @pytest.mark.smoke (slow, network).
Unit tests use mocking.
"""
from __future__ import annotations

import os
import sys
from pathlib import Path
from unittest.mock import MagicMock, patch

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pytest

from audit_screenshot import _detect_internal_pages, capture


class TestDetectInternalPages:
    def test_finds_pricing_link(self):
        html = '<html><body><a href="/pricing">Pricing</a></body></html>'
        result = _detect_internal_pages(html, "https://example.com")
        assert "https://example.com/pricing" in result

    def test_finds_signup_link(self):
        html = '<a href="/signup">Sign up</a>'
        result = _detect_internal_pages(html, "https://example.com")
        assert "https://example.com/signup" in result

    def test_ignores_external_links(self):
        html = '<a href="https://other.com/pricing">Other</a>'
        result = _detect_internal_pages(html, "https://example.com")
        assert all("other.com" not in u for u in result)

    def test_max_3_pages(self):
        html = ('<a href="/pricing">P</a><a href="/signup">S</a>'
                '<a href="/contact">C</a><a href="/features">F</a>'
                '<a href="/about">A</a>')
        result = _detect_internal_pages(html, "https://example.com")
        assert len(result) <= 3

    def test_dedupes_urls(self):
        html = '<a href="/pricing">P1</a><a href="/pricing">P2</a>'
        result = _detect_internal_pages(html, "https://example.com")
        assert len([u for u in result if "pricing" in u]) == 1


class TestCaptureMocked:
    @patch("audit_screenshot.sync_playwright")
    def test_capture_returns_dict(self, mock_pw, tmp_path: Path):
        # Mock Playwright context
        mock_browser = MagicMock()
        mock_page = MagicMock()
        mock_page.content.return_value = "<html><body></body></html>"
        mock_browser.new_page.return_value = mock_page
        mock_pw.return_value.__enter__.return_value.chromium.launch.return_value = mock_browser

        result = capture("https://example.com", tmp_path)
        assert "homepage" in result
        assert "internals" in result
        assert "errors" in result

    def test_invalid_url_raises(self, tmp_path: Path):
        with pytest.raises(ValueError, match="URL inválida"):
            capture("not-a-url", tmp_path)


class TestCaptureRealSmoke:
    """Smoke tests with real Playwright. Slow; excluded from default CI."""

    @pytest.mark.smoke
    def test_real_capture_example_com(self, tmp_path: Path):
        result = capture("https://example.com", tmp_path, timeout_ms=15000)
        assert result["homepage"].exists()
        assert result["homepage"].stat().st_size > 1000  # PNG with content
