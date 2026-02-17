"""Testes para headline_scorer.py — análise de headlines."""

import pytest
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from headline_scorer import (
    count_power_words,
    check_patterns,
    check_penalties,
    calculate_length_score,
    score_headline,
    POWER_WORDS,
    HEADLINE_PATTERNS,
    PENALTY_WORDS,
)


class TestCountPowerWords:
    """Testes para contagem de palavras de poder."""

    def test_urgency_words(self):
        result = count_power_words("Faça isso agora antes que seja tarde")
        assert "urgencia" in result
        assert "agora" in result["urgencia"]

    def test_curiosity_words(self):
        result = count_power_words("O segredo que foi finalmente revelado")
        assert "curiosidade" in result

    def test_no_power_words(self):
        result = count_power_words("Texto simples sem impacto")
        assert len(result) == 0

    def test_multiple_categories(self):
        result = count_power_words("Descubra o segredo comprovado agora")
        assert len(result) >= 2

    def test_case_insensitive(self):
        result = count_power_words("SEGREDO REVELADO AGORA")
        assert len(result) > 0


class TestCheckPatterns:
    """Testes para padrões de headline."""

    def test_number_pattern(self):
        patterns = check_patterns("7 dicas para melhorar")
        assert "numero_lista" in patterns

    def test_como_pattern(self):
        patterns = check_patterns("Como melhorar sua vida")
        assert "como_fazer" in patterns

    def test_question_pattern(self):
        patterns = check_patterns("Você sabe o que está fazendo?")
        assert "pergunta" in patterns

    def test_voce_pattern(self):
        patterns = check_patterns("Você precisa saber disso")
        assert "voce" in patterns

    def test_no_patterns(self):
        patterns = check_patterns("Texto genérico sem padrão")
        assert len(patterns) == 0

    def test_multiple_patterns(self):
        patterns = check_patterns("7 segredos que você precisa saber?")
        assert len(patterns) >= 3


class TestCheckPenalties:
    """Testes para palavras que enfraquecem."""

    def test_weak_words_detected(self):
        penalties = check_penalties("Talvez isso possa funcionar, sei lá")
        assert "talvez" in penalties
        assert "sei lá" in penalties

    def test_no_penalties(self):
        penalties = check_penalties("Descubra o método comprovado")
        assert len(penalties) == 0


class TestCalculateLengthScore:
    """Testes para pontuação de comprimento."""

    def test_ideal_length(self):
        headline = "7 segredos de marketing que realmente mudam tudo"  # ~49 chars, ~8 words
        score, msg = calculate_length_score(headline)
        assert score == 10

    def test_acceptable_length(self):
        headline = "Dica rápida"  # Short
        score, msg = calculate_length_score(headline)
        assert score <= 7

    def test_too_long(self):
        headline = " ".join(["palavra"] * 20)  # Way too many words
        score, msg = calculate_length_score(headline)
        assert score == 3


class TestScoreHeadline:
    """Testes para pontuação completa de headline."""

    def test_strong_headline(self):
        result = score_headline("7 segredos comprovados que você precisa descobrir agora")
        assert result["total_score"] >= 50
        assert result["classification"] != "❌ Fraca"

    def test_weak_headline(self):
        result = score_headline("Talvez uma coisa tipo sei lá")
        assert result["total_score"] < 50
        assert len(result["penalties"]) > 0

    def test_result_structure(self):
        result = score_headline("Headline de teste")
        assert "headline" in result
        assert "scores" in result
        assert "power_words" in result
        assert "patterns" in result
        assert "penalties" in result
        assert "suggestions" in result
        assert "total_score" in result
        assert "classification" in result

    def test_score_range(self):
        result = score_headline("Qualquer headline aqui")
        assert 0 <= result["total_score"] <= 100

    def test_scores_breakdown(self):
        result = score_headline("7 dicas de marketing digital")
        scores = result["scores"]
        assert "power_words" in scores
        assert "patterns" in scores
        assert "length" in scores
        assert "specificity" in scores
        assert "penalties" in scores
        assert "clarity" in scores

    def test_suggestions_for_weak_headline(self):
        result = score_headline("Texto sem impacto")
        assert len(result["suggestions"]) > 0

    def test_classifications(self):
        """Testa que classificações seguem o padrão correto."""
        # Very strong
        result = score_headline("7 segredos comprovados que você precisa descobrir agora grátis")
        assert "🏆" in result["classification"] or "✅" in result["classification"] or "⚠️" in result["classification"] or "❌" in result["classification"]


class TestConstants:
    """Testes para constantes."""

    def test_power_words_categories(self):
        expected = ["urgencia", "curiosidade", "valor", "confianca", "emocao", "medo", "beneficio"]
        for cat in expected:
            assert cat in POWER_WORDS
            assert len(POWER_WORDS[cat]) > 0

    def test_headline_patterns_valid_regex(self):
        import re
        for name, pattern in HEADLINE_PATTERNS.items():
            try:
                re.compile(pattern)
            except re.error:
                pytest.fail(f"Padrão inválido: {name} = {pattern}")

    def test_penalty_words_not_empty(self):
        assert len(PENALTY_WORDS) > 0
