"""Tests for audit_premium_template.py."""
from __future__ import annotations

import os
import sys
from pathlib import Path

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pytest

from audit_premium_template import render, _render_cover, _render_dimension_section


SAMPLE_DATA = {
    "client_url": "https://stripe.com",
    "client_name": "stripe.com",
    "audit_type": "landing",
    "timestamp": "2026-05-09 10:25:07",
    "overall_score": 76,
    "partial": False,
    "exec_summary": "Stripe entrega execução de classe mundial...",
    "dimensions": {
        "Conversão (CTA, friction, funil)": {
            "score": 71,
            "weight": 25,
            "evidences": [
                "Pricing com fees ocultos",
                "Sem lead magnet ativo",
                "CTA único pra audiências heterogêneas",
            ],
            "fixes": [
                {"text": "Adicionar CTA secundário", "priority": "alta"},
            ],
            "prose": "Esta é a maior alavanca de melhoria identificada na auditoria...",
            "before_after": [
                {"before": "Start now", "after": "Start building free (devs)"},
            ],
            "agent_citation": "Conforme análise mos-funnel: 'O caminho é linear...'",
        },
    },
    "competitive": {
        "competitors": [
            {"name": "Adyen", "differentiation": "..."},
            {"name": "PayPal", "differentiation": "..."},
        ],
        "table_md": "| Dimensão | Cliente | Adyen | PayPal |\n|---|---|---|---|\n| ... |",
    },
    "roadmap": {
        "30_days": [{"action": "X", "dimension": "Y", "effort": "S", "impact": "alto", "owner": "Z"}],
        "90_days": [],
        "180_days": [],
    },
    "appendix": {
        "research": "raw output...",
        "seo": "raw output...",
    },
}

SAMPLE_SCREENSHOTS = {
    "homepage": "/tmp/homepage.png",
    "internals": ["/tmp/pricing.png"],
}

SAMPLE_CHARTS = {
    "radar": "/tmp/radar.png",
}


class TestRender:
    def test_render_returns_valid_html(self):
        html = render(SAMPLE_DATA, SAMPLE_SCREENSHOTS, SAMPLE_CHARTS, config=None)
        assert html.startswith("<!DOCTYPE html>")
        assert "</html>" in html

    def test_html_contains_all_sections(self):
        html = render(SAMPLE_DATA, SAMPLE_SCREENSHOTS, SAMPLE_CHARTS, config=None)
        # Cover
        assert "stripe.com" in html
        # Exec summary
        assert "Stripe entrega" in html
        # Scorecard with score
        assert "76" in html
        # Dimension prose
        assert "Esta é a maior alavanca" in html
        # Roadmap
        assert "30 dias" in html or "30_days" in html
        # Appendix
        assert "raw output" in html

    def test_html_includes_premium_palette(self):
        html = render(SAMPLE_DATA, SAMPLE_SCREENSHOTS, SAMPLE_CHARTS, config=None)
        assert "#0a2540" in html  # primary
        assert "#ff6b35" in html  # accent

    def test_white_label_overrides_palette(self):
        config = {"brand_name": "Acme", "primary_color": "#000000", "accent_color": "#ff0000"}
        html = render(SAMPLE_DATA, SAMPLE_SCREENSHOTS, SAMPLE_CHARTS, config=config)
        assert "#000000" in html
        assert "#ff0000" in html
        assert "Acme" in html


class TestCover:
    def test_cover_includes_client_name(self):
        html = _render_cover(SAMPLE_DATA, config=None)
        assert "stripe.com" in html

    def test_cover_full_bleed(self):
        html = _render_cover(SAMPLE_DATA, config=None)
        assert "cover" in html.lower()


class TestDimensionSection:
    def test_dimension_section_renders_prose(self):
        dim_data = SAMPLE_DATA["dimensions"]["Conversão (CTA, friction, funil)"]
        html = _render_dimension_section("Conversão (CTA, friction, funil)", dim_data, screenshot=None)
        assert "Esta é a maior alavanca" in html
        assert "71" in html
        assert "25" in html  # weight

    def test_dimension_section_renders_before_after(self):
        dim_data = SAMPLE_DATA["dimensions"]["Conversão (CTA, friction, funil)"]
        html = _render_dimension_section("Conversão (CTA, friction, funil)", dim_data, screenshot=None)
        assert "Start now" in html
        assert "Start building free" in html

    def test_priority_class_applied(self):
        dim_data = SAMPLE_DATA["dimensions"]["Conversão (CTA, friction, funil)"]
        html = _render_dimension_section("Conversão (CTA, friction, funil)", dim_data, screenshot=None)
        assert "priority-alta" in html
