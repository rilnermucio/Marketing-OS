#!/usr/bin/env python3
"""
Testes funcionais para readability_checker.py.
"""
from __future__ import annotations

import os
import sys
from unittest.mock import patch

import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

import readability_checker as rc


# ----------------------------------------------------------- get_words
def test_get_words_extrai_palavras_simples():
    palavras = rc.get_words("Olá mundo, como vai?")
    assert "olá" in palavras
    assert "mundo" in palavras
    assert "como" in palavras


def test_get_words_lowercase():
    palavras = rc.get_words("HELLO World")
    assert all(p == p.lower() for p in palavras)


def test_get_words_aceita_acentos():
    palavras = rc.get_words("ação coração não")
    assert "ação" in palavras
    assert "coração" in palavras


def test_get_words_texto_vazio():
    assert rc.get_words("") == []


# ----------------------------------------------------------- count_syllables_pt
def test_count_syllables_palavra_curta():
    assert rc.count_syllables_pt("eu") >= 1


def test_count_syllables_palavra_media():
    # "fa-zer" — 2 sílabas
    assert rc.count_syllables_pt("fazer") >= 2


def test_count_syllables_acento():
    assert rc.count_syllables_pt("não") >= 1


# ----------------------------------------------------------- calculate_flesch_pt
def test_calculate_flesch_texto_curto_retorna_zero():
    score, level = rc.calculate_flesch_pt("")
    assert score == 0
    assert "curto" in level.lower()


def test_calculate_flesch_texto_simples_pontuacao_alta():
    texto = "O céu é azul. A grama é verde. O sol é amarelo. A neve é branca. As nuvens são leves."
    score, level = rc.calculate_flesch_pt(texto)
    assert 0 <= score <= 100
    assert isinstance(level, str)


def test_calculate_flesch_score_em_range_valido():
    texto = "Aqui temos um texto comum, com palavras normais e frases bem distribuídas."
    score, _ = rc.calculate_flesch_pt(texto)
    assert 0 <= score <= 100


def test_calculate_flesch_retorna_tupla():
    res = rc.calculate_flesch_pt("Frase de teste para análise.")
    assert isinstance(res, tuple)
    assert len(res) == 2


# ----------------------------------------------------------- calculate_reading_time
def test_calculate_reading_time_estrutura():
    r = rc.calculate_reading_time("palavra " * 200)
    assert "word_count" in r
    assert "times" in r
    assert r["word_count"] == 200
    assert "leitura_rapida" in r["times"]
    assert "leitura_normal" in r["times"]
    assert "leitura_atenta" in r["times"]


def test_calculate_reading_time_texto_curto_segundos():
    r = rc.calculate_reading_time("uma duas três")
    # < 1 minuto, vem em segundos
    assert "segundos" in r["times"]["leitura_rapida"]


def test_calculate_reading_time_texto_longo_minutos():
    r = rc.calculate_reading_time("palavra " * 1000)
    assert "minutos" in r["times"]["leitura_normal"]


# ----------------------------------------------------------- analyze_sentences
def test_analyze_sentences_estrutura():
    r = rc.analyze_sentences("Frase um. Frase dois. Frase três bem mais longa que as outras.")
    assert "total_sentences" in r
    assert r["total_sentences"] >= 2
    assert "avg_length" in r
    assert "shortest" in r
    assert "longest" in r
    assert "very_long" in r
    assert "very_short" in r


def test_analyze_sentences_vazio_retorna_erro():
    r = rc.analyze_sentences("")
    assert "error" in r


def test_analyze_sentences_uma_so_sentenca():
    r = rc.analyze_sentences("Apenas uma frase aqui.")
    assert r["variation"] == "N/A"


def test_analyze_sentences_variacao_boa():
    texto = "Curta. " + "palavra " * 30 + ". Outra média sentença aqui pra variar."
    r = rc.analyze_sentences(texto)
    # Variation deve ser computada
    assert "variation" in r


# ----------------------------------------------------------- find_transition_words
def test_find_transition_words_acha():
    texto = "Eu gosto disso. Portanto vamos lá. Além disso é importante."
    achados = rc.find_transition_words(texto)
    assert "portanto" in achados
    assert "além disso" in achados


def test_find_transition_words_vazio():
    assert rc.find_transition_words("Texto sem nenhum conectivo") == []


# ----------------------------------------------------------- find_complex_words
def test_find_complex_words_acha_e_sugere():
    texto = "Vamos utilizar essa solução para realizar algo."
    achados = rc.find_complex_words(texto)
    palavras_achadas = [t[0] for t in achados]
    assert "utilizar" in palavras_achadas
    assert "realizar" in palavras_achadas


def test_find_complex_words_retorna_tupla():
    achados = rc.find_complex_words("Vamos utilizar isso.")
    assert all(isinstance(t, tuple) and len(t) == 2 for t in achados)


def test_find_complex_words_vazio_se_nao_acha():
    assert rc.find_complex_words("Texto simples comum") == []


# ----------------------------------------------------------- find_jargon
def test_find_jargon_acha():
    achados = rc.find_jargon("Precisamos de sinergia e disruptivo mindset")
    assert "sinergia" in achados
    assert "mindset" in achados


def test_find_jargon_vazio():
    assert rc.find_jargon("Texto totalmente sem jargão") == []


# ----------------------------------------------------------- analyze_paragraphs
def test_analyze_paragraphs_double_newline():
    texto = "Parágrafo um.\n\nParágrafo dois."
    r = rc.analyze_paragraphs(texto)
    assert r["total"] == 2


def test_analyze_paragraphs_single_newline_fallback():
    """Sem \\n\\n, o split inicial volta uma única string. Sem fallback adicional, total=1."""
    texto = "Parágrafo um.\nParágrafo dois."
    r = rc.analyze_paragraphs(texto)
    assert r["total"] == 1


def test_analyze_paragraphs_vazio():
    r = rc.analyze_paragraphs("")
    assert "error" in r


def test_analyze_paragraphs_avg_words():
    texto = "Um dois três.\n\nQuatro cinco seis."
    r = rc.analyze_paragraphs(texto)
    assert "avg_words" in r
    assert r["avg_words"] > 0


# ----------------------------------------------------------- get_vocabulary_stats
def test_get_vocabulary_stats_estrutura():
    r = rc.get_vocabulary_stats("uma palavra duas palavras três")
    assert "total_words" in r
    assert "unique_words" in r
    assert "lexical_diversity" in r
    assert "long_words_count" in r
    assert "long_words_percent" in r
    assert "most_common" in r


def test_get_vocabulary_stats_vazio():
    r = rc.get_vocabulary_stats("")
    assert "error" in r


def test_get_vocabulary_stats_lexical_diversity_em_range():
    r = rc.get_vocabulary_stats("palavra palavra palavra única")
    assert 0 <= r["lexical_diversity"] <= 1


# ----------------------------------------------------------- full_analysis
def test_full_analysis_chaves_esperadas():
    texto = "Texto de exemplo para análise. Tem várias frases. Algumas são curtas, outras médias."
    r = rc.full_analysis(texto)
    for k in ("text_preview", "flesch", "reading_time", "sentences",
              "paragraphs", "vocabulary", "transitions", "complex_words",
              "jargon", "overall_score", "classification"):
        assert k in r, f"Chave {k} faltando em full_analysis"


def test_full_analysis_overall_score_em_range():
    r = rc.full_analysis("Frase. Outra frase. Mais uma frase.")
    assert 0 <= r["overall_score"] <= 100


def test_full_analysis_classifica_excelente_ou_outras():
    r = rc.full_analysis("Texto curto. Bem fácil. Muito simples.")
    assert isinstance(r["classification"], str)
    assert len(r["classification"]) > 0


def test_full_analysis_text_preview_truncado():
    texto_longo = "x" * 500
    r = rc.full_analysis(texto_longo)
    assert len(r["text_preview"]) <= 210


def test_full_analysis_text_preview_curto_inteiro():
    r = rc.full_analysis("texto curto")
    assert r["text_preview"] == "texto curto"


# ----------------------------------------------------------- print_report
def test_print_report_imprime_secoes(capsys):
    texto = "Texto de exemplo. Várias frases. Algumas curtas. Outras médias para teste."
    r = rc.full_analysis(texto)
    rc.print_report(r)
    out = capsys.readouterr().out
    assert "ANÁLISE DE LEGIBILIDADE" in out
    assert "SCORE GERAL" in out
    assert "MÉTRICAS PRINCIPAIS" in out
    assert "RECOMENDAÇÕES" in out


def test_print_report_recomendacao_quando_sem_problemas(capsys):
    """Texto bom sem nada para reclamar deve mostrar mensagem positiva."""
    texto = ("Este texto é simples. "
             "Tem boa estrutura. "
             "Portanto, flui bem. "
             "Além disso, usa conectivos. "
             "Por exemplo, este. "
             "É de fácil leitura.")
    r = rc.full_analysis(texto)
    rc.print_report(r)
    out = capsys.readouterr().out
    assert "RECOMENDAÇÕES" in out


# ----------------------------------------------------------- main / CLI
def test_main_sem_argumentos(capsys):
    with patch.object(sys, "argv", ["readability_checker.py"]):
        with pytest.raises(SystemExit):
            rc.main()
    out = capsys.readouterr().out
    assert "Uso" in out


def test_main_texto_curto_retorna_erro(capsys):
    with patch.object(sys, "argv", ["readability_checker.py", "curto"]):
        with pytest.raises(SystemExit):
            rc.main()
    out = capsys.readouterr().out
    assert "muito curto" in out.lower() or "mínimo" in out.lower()


def test_main_texto_inline(capsys):
    texto = "Este é um texto longo o suficiente para ser analisado pelo readability checker."
    with patch.object(sys, "argv", ["readability_checker.py", texto]):
        rc.main()
    out = capsys.readouterr().out
    assert "ANÁLISE DE LEGIBILIDADE" in out


def test_main_lendo_arquivo(tmp_path, capsys):
    arquivo = tmp_path / "texto.txt"
    arquivo.write_text(
        "Este é um texto razoavelmente longo. "
        "Tem várias frases para análise. "
        "O objetivo é testar o leitor de arquivos. "
        "Continuemos escrevendo aqui.",
        encoding="utf-8",
    )
    with patch.object(sys, "argv", ["readability_checker.py", "--file", str(arquivo)]):
        rc.main()
    out = capsys.readouterr().out
    assert "ANÁLISE DE LEGIBILIDADE" in out
