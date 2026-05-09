"""Tests for audit_radar_chart.py."""
from __future__ import annotations

import os
import sys
from pathlib import Path

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pytest

from audit_radar_chart import generate, _compute_potential_scores


SAMPLE_SCORES = {
    "Conversão (CTA, friction, funil)": 71,
    "Copy (headline, value prop)": 77,
    "SEO (technical + content)": 66,
    "Trust signals": 82,
    "Design (hierarquia visual)": 87,
    "Brand (consistência, voice)": 87,
    "Diferenciação competitiva": 78,
}

SAMPLE_FIXES = {
    "Conversão (CTA, friction, funil)": {"priority": "alta"},
    "Copy (headline, value prop)": {"priority": "alta"},
    "SEO (technical + content)": {"priority": "alta"},
    "Trust signals": {"priority": "media"},
    "Design (hierarquia visual)": {"priority": "media"},
    "Brand (consistência, voice)": {"priority": "media"},
    "Diferenciação competitiva": {"priority": "alta"},
}


class TestGenerate:
    def test_generates_non_empty_png(self, tmp_path: Path):
        out = tmp_path / "radar.png"
        result = generate(SAMPLE_SCORES, SAMPLE_FIXES, out)
        assert result == out
        assert out.exists()
        assert out.stat().st_size > 1000  # PNG with content

    def test_custom_colors_applied(self, tmp_path: Path):
        out = tmp_path / "radar.png"
        generate(SAMPLE_SCORES, SAMPLE_FIXES, out,
                 primary_color="#0a2540", accent_color="#ff6b35")
        assert out.exists()

    def test_handles_partial_scores(self, tmp_path: Path):
        partial = dict(SAMPLE_SCORES)
        partial["SEO (technical + content)"] = None
        out = tmp_path / "radar.png"
        generate(partial, SAMPLE_FIXES, out)
        assert out.exists()


class TestPotentialScores:
    def test_alta_priority_adds_15_points(self):
        scores = {"A": 50}
        fixes = {"A": {"priority": "alta"}}
        potential = _compute_potential_scores(scores, fixes)
        assert potential["A"] == 65  # 50 + 15

    def test_media_priority_adds_5_points(self):
        scores = {"A": 50}
        fixes = {"A": {"priority": "media"}}
        potential = _compute_potential_scores(scores, fixes)
        assert potential["A"] == 55  # 50 + 5

    def test_baixa_priority_adds_2_points(self):
        scores = {"A": 50}
        fixes = {"A": {"priority": "baixa"}}
        potential = _compute_potential_scores(scores, fixes)
        assert potential["A"] == 52

    def test_caps_at_100(self):
        scores = {"A": 95}
        fixes = {"A": {"priority": "alta"}}
        potential = _compute_potential_scores(scores, fixes)
        assert potential["A"] == 100

    def test_none_scores_remain_none(self):
        scores = {"A": None}
        fixes = {"A": {"priority": "alta"}}
        potential = _compute_potential_scores(scores, fixes)
        assert potential["A"] is None
