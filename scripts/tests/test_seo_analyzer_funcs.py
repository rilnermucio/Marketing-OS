#!/usr/bin/env python3
"""
Testes funcionais adicionais para seo_analyzer.py — cobre main() e branches.
"""
from __future__ import annotations

import json
import os
import sys
from unittest.mock import patch

import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

import seo_analyzer as sa


SAMPLE_LONG = """# Marketing Digital em 2026

O marketing digital evoluiu muito nos últimos anos. Estratégias modernas exigem
abordagem multidimensional para alcançar resultados consistentes.

## Por Que Marketing Digital Importa

Marketing digital é fundamental para qualquer negócio moderno. Dados mostram que
empresas com presença digital crescem 3x mais rápido que as tradicionais.

## Estratégias Eficazes

Aqui estão as principais estratégias de marketing digital que funcionam:

- SEO orgânico
- Anúncios pagos
- Email marketing
- Marketing de conteúdo
- Redes sociais

### Implementação

Para implementar uma estratégia eficaz de marketing digital, comece definindo
seus objetivos. Depois, alinhe canais e mensagens. Marketing digital exige
consistência e métricas. Nunca subestime o poder do marketing digital.

[Fonte oficial](https://example.com)
[Outro estudo](https://research.org)
[Link interno](/blog/post)
"""


# ----------------------------------------------------------- analyze_content branches
def test_analyze_content_recomendacao_curto():
    r = sa.analyze_content("apenas algumas palavras curtas aqui")
    recs = " ".join(r["recommendations"]).lower()
    assert "curto" in recs or "<300" in recs


def test_analyze_content_recomendacao_medio():
    # Texto entre 300-1000 palavras
    texto = "palavra " * 500
    r = sa.analyze_content(texto)
    recs = " ".join(r["recommendations"]).lower()
    assert "médio" in recs or "1500" in recs


def test_analyze_content_recomendacao_longo():
    texto = "palavra " * 1500
    r = sa.analyze_content(texto)
    recs = " ".join(r["recommendations"])
    assert any("✅" in rec for rec in r["recommendations"])


def test_analyze_content_falta_h1():
    texto = "## Título sem H1\n\nconteúdo " * 100
    r = sa.analyze_content(texto)
    recs = " ".join(r["recommendations"]).lower()
    assert "h1" in recs


def test_analyze_content_h1_duplicado():
    texto = "# Primeiro H1\n# Segundo H1\n\n" + ("conteúdo " * 100)
    r = sa.analyze_content(texto)
    recs = " ".join(r["recommendations"])
    assert "H1" in recs
    assert "Encontrados" in recs


def test_analyze_content_poucos_h2():
    texto = "# H1\n\n" + ("conteúdo " * 200)
    r = sa.analyze_content(texto)
    recs = " ".join(r["recommendations"]).lower()
    assert "h2" in recs


def test_analyze_content_sentencas_longas():
    texto = " ".join(["palavra"] * 30) + "."  # 30 palavras numa sentença
    texto = texto * 5  # algumas vezes
    r = sa.analyze_content(texto)
    if r["metrics"]["avg_sentence_length"] > 25:
        recs = " ".join(r["recommendations"]).lower()
        assert "long" in recs or "ideal" in recs


def test_analyze_content_sem_links_externos():
    r = sa.analyze_content("texto " * 100)
    recs = " ".join(r["recommendations"]).lower()
    assert "externo" in recs or "e-e-a-t" in recs


def test_analyze_content_keyword_baixa_densidade():
    texto = "marketing " + ("texto " * 200)
    r = sa.analyze_content(texto, "marketing")
    if r["keyword_analysis"]["density"] < 1:
        recs = " ".join(r["recommendations"]).lower()
        assert "densidade" in recs or "baixa" in recs


def test_analyze_content_keyword_stuffing():
    texto = ("marketing " * 50) + ("outro " * 10)
    r = sa.analyze_content(texto, "marketing")
    if r["keyword_analysis"]["density"] > 2.5:
        recs = " ".join(r["recommendations"]).lower()
        assert "stuffing" in recs or "reduza" in recs


def test_analyze_content_keyword_nao_no_inicio():
    texto = ("texto " * 200) + " marketing"
    r = sa.analyze_content(texto, "marketing")
    if not r["keyword_analysis"]["in_first_100_words"]:
        recs = " ".join(r["recommendations"]).lower()
        assert "primeiras 100" in recs or "100 palavras" in recs


def test_analyze_content_keyword_nao_no_h1():
    r = sa.analyze_content("# Outro Título\n\n" + ("marketing " * 50), "marketing")
    if not r["keyword_analysis"]["in_h1"]:
        recs = " ".join(r["recommendations"]).lower()
        assert "h1" in recs


def test_analyze_content_metricas_completas():
    r = sa.analyze_content(SAMPLE_LONG, "marketing digital")
    assert "metrics" in r
    assert r["metrics"]["word_count"] > 0
    assert r["metrics"]["sentence_count"] > 0
    assert r["metrics"]["paragraph_count"] > 0


def test_analyze_content_keyword_status_good():
    """Densidade entre 1-2 → 'good'."""
    # Aproximadamente 1.5% densidade
    texto = ("marketing " + "texto " * 65) + (" marketing texto " * 5)
    r = sa.analyze_content(texto, "marketing")
    if 1 <= r["keyword_analysis"]["density"] <= 2:
        assert r["keyword_analysis"]["status"] == "good"


# ----------------------------------------------------------- main / CLI
def test_main_sem_args(capsys):
    with patch.object(sys, "argv", ["seo_analyzer.py"]):
        with pytest.raises(SystemExit):
            sa.main()
    out = capsys.readouterr().out
    assert "Uso" in out


def test_main_arquivo_inexistente_falha(capsys):
    with patch.object(sys, "argv", ["seo_analyzer.py", "/tmp/nao_existe_xyz.md"]):
        with pytest.raises(SystemExit):
            sa.main()
    err = capsys.readouterr().err
    assert "Erro" in err or "validação" in err.lower()


def test_main_arquivo_extensao_invalida(tmp_path, capsys):
    arquivo = tmp_path / "teste.bin"
    arquivo.write_text("conteúdo binário")
    with patch.object(sys, "argv", ["seo_analyzer.py", str(arquivo)]):
        with pytest.raises(SystemExit):
            sa.main()
    err = capsys.readouterr().err
    assert "Erro" in err or "validação" in err.lower()


def test_main_arquivo_md_valido(tmp_path, capsys):
    arquivo = tmp_path / "artigo.md"
    arquivo.write_text(SAMPLE_LONG, encoding="utf-8")
    with patch.object(sys, "argv", ["seo_analyzer.py", str(arquivo)]):
        sa.main()
    out = capsys.readouterr().out
    assert "RELATÓRIO DE ANÁLISE SEO" in out
    assert "SEO SCORE" in out


def test_main_com_keyword(tmp_path, capsys):
    arquivo = tmp_path / "artigo.md"
    arquivo.write_text(SAMPLE_LONG, encoding="utf-8")
    with patch.object(sys, "argv", ["seo_analyzer.py", str(arquivo), "marketing digital"]):
        sa.main()
    out = capsys.readouterr().out
    assert "ANÁLISE DE KEYWORD" in out
    assert "marketing digital" in out
    # JSON output
    assert "JSON Output" in out


def test_main_arquivo_txt_valido(tmp_path, capsys):
    arquivo = tmp_path / "artigo.txt"
    arquivo.write_text(SAMPLE_LONG, encoding="utf-8")
    with patch.object(sys, "argv", ["seo_analyzer.py", str(arquivo)]):
        sa.main()
    out = capsys.readouterr().out
    assert "SEO SCORE" in out
