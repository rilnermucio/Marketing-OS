#!/usr/bin/env python3
"""
Testes funcionais adicionais para headline_scorer.py — cobre print_report,
compare_headlines e main().
"""
from __future__ import annotations

import os
import sys
from unittest.mock import patch

import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

import headline_scorer as hs


# ----------------------------------------------------------- score_headline
def test_score_headline_excelente():
    """Headline com vários sinais positivos."""
    r = hs.score_headline("7 segredos comprovados para dobrar suas vendas em 30 dias")
    assert r["total_score"] >= 60
    assert "Excelente" in r["classification"] or "Boa" in r["classification"]


def test_score_headline_fraca():
    """Headline pobre."""
    r = hs.score_headline("texto")
    assert r["total_score"] <= 50


def test_score_headline_inclui_classificacao():
    r = hs.score_headline("Como aprender programação em 2026")
    assert "classification" in r
    assert isinstance(r["classification"], str)


def test_score_headline_sugestoes_quando_fraca():
    r = hs.score_headline("muito ruim mesmo")
    assert len(r["suggestions"]) > 0


def test_score_headline_total_em_range():
    r = hs.score_headline("Como dominar marketing em 30 dias")
    assert 0 <= r["total_score"] <= 100


def test_score_headline_clarity_palavras_curtas():
    r = hs.score_headline("Faça já hoje sem demora pra ti")
    # Palavras curtas → clarity alto
    assert r["scores"]["clarity"] >= 15


def test_score_headline_clarity_palavras_longas():
    r = hs.score_headline("Implementação multidimensional revolucionária transformacional disruptiva")
    # Palavras longas → clarity baixo
    assert r["scores"]["clarity"] <= 10


def test_score_headline_specificity_com_numero_e_tempo():
    r = hs.score_headline("Aprenda 5 técnicas em 7 dias")
    assert r["has_number"] is True
    assert r["has_timeframe"] is True
    assert r["scores"]["specificity"] == 15


def test_score_headline_specificity_sem_nada():
    r = hs.score_headline("Como melhorar")
    assert r["has_number"] is False
    assert r["has_timeframe"] is False
    assert r["scores"]["specificity"] == 0


def test_score_headline_penalidade_por_palavras_fracas():
    fraca = "talvez seja basicamente algo simplesmente legal"
    r = hs.score_headline(fraca)
    # 'talvez' e 'basicamente' e 'simplesmente' são penalty words
    assert r["scores"]["penalties"] < 0


# ----------------------------------------------------------- print_report
def test_print_report_imprime_titulo(capsys):
    r = hs.score_headline("7 segredos comprovados")
    hs.print_report(r)
    out = capsys.readouterr().out
    assert "ANÁLISE DE HEADLINE" in out
    assert "PONTUAÇÃO TOTAL" in out
    assert "DETALHAMENTO" in out


def test_print_report_inclui_headline(capsys):
    r = hs.score_headline("Como dominar marketing")
    hs.print_report(r)
    out = capsys.readouterr().out
    assert "Como dominar marketing" in out


def test_print_report_mostra_padroes_se_existem(capsys):
    r = hs.score_headline("7 dicas para você")
    hs.print_report(r)
    out = capsys.readouterr().out
    if r["patterns"]:
        assert "PADRÕES IDENTIFICADOS" in out


def test_print_report_mostra_palavras_fracas(capsys):
    r = hs.score_headline("Talvez seja simplesmente bom")
    hs.print_report(r)
    out = capsys.readouterr().out
    # Tem penalidades, deve mostrar
    assert "ENFRAQUECEM" in out or "SUGESTÕES" in out


def test_print_report_mostra_sugestoes(capsys):
    r = hs.score_headline("X")  # headline ruim
    hs.print_report(r)
    out = capsys.readouterr().out
    assert "SUGESTÕES" in out


def test_print_report_mostra_palavras_de_poder(capsys):
    r = hs.score_headline("Segredo comprovado revelado agora")
    hs.print_report(r)
    out = capsys.readouterr().out
    if r["power_words"]:
        assert "PALAVRAS DE PODER" in out


# ----------------------------------------------------------- compare_headlines
def test_compare_headlines_imprime(capsys):
    headlines = [
        "Como dobrar vendas em 30 dias",
        "Aprenda algo",
        "7 segredos comprovados que vão revolucionar"
    ]
    hs.compare_headlines(headlines)
    out = capsys.readouterr().out
    assert "COMPARATIVO DE HEADLINES" in out
    assert "VENCEDOR" in out
    # Todos devem aparecer
    for h in headlines:
        assert h in out


def test_compare_headlines_ordena_por_score(capsys):
    """Vencedor deve ser o de maior score."""
    headlines = [
        "ruim",
        "7 segredos comprovados que vão revolucionar suas vendas em 30 dias garantido"
    ]
    hs.compare_headlines(headlines)
    out = capsys.readouterr().out
    # O segundo (com mais sinais positivos) deve ser o vencedor
    vencedor_section = out.split("VENCEDOR")[1]
    assert "7 segredos" in vencedor_section


def test_compare_headlines_mostra_medalhas(capsys):
    headlines = ["A", "B", "C"]
    hs.compare_headlines(headlines)
    out = capsys.readouterr().out
    assert "🥇" in out
    assert "🥈" in out
    assert "🥉" in out


# ----------------------------------------------------------- main / CLI
def test_main_sem_args(capsys):
    with patch.object(sys, "argv", ["headline_scorer.py"]):
        with pytest.raises(SystemExit):
            hs.main()
    out = capsys.readouterr().out
    assert "Uso" in out


def test_main_headline_unica(capsys):
    with patch.object(sys, "argv",
                      ["headline_scorer.py", "Como dominar marketing em 30 dias"]):
        hs.main()
    out = capsys.readouterr().out
    assert "ANÁLISE DE HEADLINE" in out


def test_main_compare_mode(capsys):
    with patch.object(sys, "argv",
                      ["headline_scorer.py", "--compare", "Headline A", "Headline B"]):
        hs.main()
    out = capsys.readouterr().out
    assert "COMPARATIVO DE HEADLINES" in out


def test_main_lendo_arquivo(tmp_path, capsys):
    arquivo = tmp_path / "headlines.txt"
    arquivo.write_text(
        "7 dicas para vender mais\n"
        "Como aumentar suas vendas\n"
        "O segredo do marketing\n",
        encoding="utf-8",
    )
    with patch.object(sys, "argv", ["headline_scorer.py", "--file", str(arquivo)]):
        hs.main()
    out = capsys.readouterr().out
    # Quando há mais de uma headline, vai pro modo comparação
    assert "COMPARATIVO" in out


def test_main_arquivo_uma_headline(tmp_path, capsys):
    arquivo = tmp_path / "single.txt"
    arquivo.write_text("Como dominar marketing em 30 dias\n", encoding="utf-8")
    with patch.object(sys, "argv", ["headline_scorer.py", "--file", str(arquivo)]):
        hs.main()
    out = capsys.readouterr().out
    # Apenas uma headline → análise individual
    assert "ANÁLISE DE HEADLINE" in out
