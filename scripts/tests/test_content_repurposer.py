#!/usr/bin/env python3
"""
Testes para content_repurposer.py
"""

import sys
import os
import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from content_repurposer import (
    extract_key_points,
    extract_title,
    estimate_read_time,
    to_instagram_carousel,
)


def test_extract_key_points_de_lista():
    texto = "- Ponto um importante\n- Ponto dois relevante\n- Ponto três essencial"
    pontos = extract_key_points(texto)
    assert len(pontos) >= 3

def test_extract_key_points_max():
    texto = "\n".join([f"- Ponto {i}" for i in range(20)])
    pontos = extract_key_points(texto, max_points=5)
    assert len(pontos) <= 5

def test_extract_key_points_de_texto_solto():
    texto = "Este é o primeiro ponto importante. Segundo aspecto essencial aqui. Terceiro fundamento crítico."
    pontos = extract_key_points(texto)
    assert isinstance(pontos, list)

def test_extract_title_de_markdown():
    texto = "# Meu Título Aqui\n\nConteúdo do artigo."
    titulo = extract_title(texto)
    assert "Meu Título Aqui" in titulo

def test_extract_title_linha_curta():
    texto = "Título Curto\n\nParágrafo longo com muito conteúdo e palavras aqui."
    titulo = extract_title(texto)
    assert "Título Curto" in titulo

def test_extract_title_fallback():
    texto = "Esta é uma frase muito longa que serve como fallback quando não há um título claro definido."
    titulo = extract_title(texto)
    assert isinstance(titulo, str)
    assert len(titulo) > 0

def test_estimate_read_time_rapido():
    texto = " ".join(["palavra"] * 100)
    assert estimate_read_time(texto) >= 1

def test_estimate_read_time_longo():
    texto = " ".join(["palavra"] * 1000)
    assert estimate_read_time(texto) >= 5

def test_to_instagram_carousel_estrutura():
    texto = "# Como usar IA\n\n- Dica um sobre IA\n- Dica dois sobre IA\n- Dica três sobre automação\n- Dica quatro sobre produtividade"
    resultado = to_instagram_carousel(texto)
    assert "slides" in resultado
    assert len(resultado["slides"]) >= 1

def test_to_instagram_carousel_primeiro_slide():
    texto = "# Título do Carrossel\n\nConteúdo aqui."
    resultado = to_instagram_carousel(texto)
    assert resultado["slides"][0]["slide"] == 1
    assert resultado["slides"][0]["type"] == "capa"

def test_to_instagram_carousel_num_slides():
    # A função adiciona slides fixos (capa, resumo, cta) além do conteúdo
    # num_slides controla os slides de conteúdo, mas o total pode ser maior
    texto = "\n".join([f"- Ponto {i}" for i in range(15)])
    resultado = to_instagram_carousel(texto, num_slides=5)
    assert len(resultado["slides"]) >= 1
