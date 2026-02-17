"""Testes para seo_analyzer.py — análise SEO de conteúdo."""

import pytest
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from seo_analyzer import analyze_content, calculate_seo_score


class TestAnalyzeContent:
    """Testes para análise de conteúdo SEO."""

    def test_basic_metrics(self):
        content = "Palavra um. Palavra dois. Palavra três."
        result = analyze_content(content)
        assert result["metrics"]["word_count"] == 6
        assert result["metrics"]["sentence_count"] == 3

    def test_header_detection(self):
        content = "# Título H1\n\n## Subtítulo H2\n\n## Outro H2\n\n### H3\n\nConteúdo."
        result = analyze_content(content)
        assert result["structure"]["headers"]["h1"] == 1
        assert result["structure"]["headers"]["h2"] == 2
        assert result["structure"]["headers"]["h3"] == 1

    def test_keyword_analysis(self):
        content = "# Marketing digital é essencial\n\nO marketing digital cresceu muito. Marketing digital em 2026."
        result = analyze_content(content, "marketing digital")
        kw = result["keyword_analysis"]
        assert kw["keyword"] == "marketing digital"
        assert kw["count"] >= 2
        assert kw["in_h1"] is True
        assert kw["in_first_100_words"] is True

    def test_no_keyword(self):
        result = analyze_content("Conteúdo sem análise de keyword.")
        assert result["keyword_analysis"] is None

    def test_keyword_density(self):
        words = ["marketing digital"] * 5 + ["outras palavras"] * 95
        content = ". ".join(words)
        result = analyze_content(content, "marketing digital")
        density = result["keyword_analysis"]["density"]
        assert isinstance(density, float)

    def test_link_detection(self):
        content = "Texto com [link interno](/blog/post) e [link externo](https://example.com)."
        result = analyze_content(content)
        assert result["structure"]["internal_links"] == 1
        assert result["structure"]["external_links"] == 1

    def test_readability_score_range(self):
        content = "Frases curtas. Texto simples. Fácil de ler."
        result = analyze_content(content)
        assert 0 <= result["metrics"]["readability_score"] <= 100

    def test_recommendations_short_content(self):
        content = "Conteúdo curto."
        result = analyze_content(content)
        short_recs = [r for r in result["recommendations"] if "curto" in r.lower() or "expandir" in r.lower()]
        assert len(short_recs) > 0

    def test_recommendations_no_h1(self):
        content = "Conteúdo sem nenhum header markdown. Apenas texto simples."
        result = analyze_content(content)
        h1_recs = [r for r in result["recommendations"] if "H1" in r]
        assert len(h1_recs) > 0

    def test_result_structure(self):
        result = analyze_content("Conteúdo teste.")
        assert "metrics" in result
        assert "structure" in result
        assert "keyword_analysis" in result
        assert "recommendations" in result
        assert "seo_score" in result

    def test_full_article(self, sample_article):
        result = analyze_content(sample_article, "marketing digital")
        assert result["seo_score"] > 0
        assert result["metrics"]["word_count"] > 100
        assert result["structure"]["headers"]["h1"] >= 1


class TestCalculateSeoScore:
    """Testes para cálculo do score SEO."""

    def test_perfect_score(self):
        headers = {"h1": 1, "h2": 3, "h3": 2}
        keyword = {
            "in_h1": True,
            "in_first_100_words": True,
            "density": 1.5,
        }
        score = calculate_seo_score(1500, headers, keyword, 3)
        assert score == 100

    def test_minimum_score(self):
        headers = {"h1": 0, "h2": 0, "h3": 0}
        score = calculate_seo_score(50, headers, None, 0)
        assert score >= 0

    def test_word_count_tiers(self):
        headers = {"h1": 0, "h2": 0, "h3": 0}
        score_short = calculate_seo_score(100, headers, None, 0)
        score_medium = calculate_seo_score(600, headers, None, 0)
        score_long = calculate_seo_score(1500, headers, None, 0)
        assert score_short < score_medium < score_long

    def test_header_scoring(self):
        headers_good = {"h1": 1, "h2": 3, "h3": 1}
        headers_bad = {"h1": 0, "h2": 0, "h3": 0}
        score_good = calculate_seo_score(500, headers_good, None, 0)
        score_bad = calculate_seo_score(500, headers_bad, None, 0)
        assert score_good > score_bad

    def test_external_links_scoring(self):
        headers = {"h1": 1, "h2": 2, "h3": 0}
        score_no_links = calculate_seo_score(1000, headers, None, 0)
        score_with_links = calculate_seo_score(1000, headers, None, 3)
        assert score_with_links > score_no_links

    def test_keyword_bonus(self):
        headers = {"h1": 1, "h2": 2, "h3": 0}
        keyword = {
            "in_h1": True,
            "in_first_100_words": True,
            "density": 1.5,
        }
        score_with = calculate_seo_score(1000, headers, keyword, 0)
        score_without = calculate_seo_score(1000, headers, None, 0)
        assert score_with > score_without

    def test_score_range(self):
        headers = {"h1": 1, "h2": 2, "h3": 1}
        score = calculate_seo_score(500, headers, None, 1)
        assert 0 <= score <= 100
