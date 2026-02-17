#!/usr/bin/env python3
"""
Testes para readability_checker.py
"""

import sys
import os
import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from readability_checker import (
    count_syllables_pt,
    get_sentences,
    TRANSITION_WORDS,
    COMPLEX_WORDS,
    JARGON_WORDS,
)


def test_count_syllables_vogais_simples():
    # "ca-sa" = 2 sílabas
    assert count_syllables_pt("casa") >= 2

def test_count_syllables_minimo_um():
    assert count_syllables_pt("a") >= 1
    assert count_syllables_pt("x") >= 1

def test_count_syllables_palavra_longa():
    # "pro-du-ti-vi-da-de" = 6 sílabas
    resultado = count_syllables_pt("produtividade")
    assert resultado >= 4

def test_count_syllables_sem_vogais():
    resultado = count_syllables_pt("xyz")
    assert resultado >= 1

def test_get_sentences_ponto():
    texto = "Frase um. Frase dois. Frase três."
    sentencas = get_sentences(texto)
    assert len(sentencas) >= 2

def test_get_sentences_exclamacao():
    texto = "Ótimo! Muito bom! Excelente!"
    sentencas = get_sentences(texto)
    assert len(sentencas) >= 2

def test_get_sentences_interrogacao():
    texto = "O que é isso? Como funciona? Por que usar?"
    sentencas = get_sentences(texto)
    assert len(sentencas) >= 2

def test_get_sentences_texto_simples():
    texto = "Uma única frase sem pontuação no final"
    sentencas = get_sentences(texto)
    assert isinstance(sentencas, list)

def test_transition_words_nao_vazio():
    assert len(TRANSITION_WORDS) >= 10

def test_transition_words_portugues():
    palavras_esperadas = ["portanto", "porém", "além disso", "ou seja"]
    for p in palavras_esperadas:
        assert p in TRANSITION_WORDS, f"'{p}' não encontrado"

def test_complex_words_tem_substituicoes():
    assert len(COMPLEX_WORDS) >= 5
    for original, substituto in COMPLEX_WORDS.items():
        assert isinstance(original, str)
    assert substituto is not None

def test_jargon_words_nao_vazio():
    assert len(JARGON_WORDS) >= 5

def test_jargon_words_comuns():
    assert "sinergia" in JARGON_WORDS or "paradigma" in JARGON_WORDS
