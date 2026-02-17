#!/usr/bin/env python3
"""
Testes para ab_generator.py
"""

import sys
import os
import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from ab_generator import (
    generate_variations,
    VARIATION_TEMPLATES,
)


def test_generate_variations_headline_retorna_lista():
    resultado = generate_variations("Aprenda marketing digital", "headline")
    assert "variations" in resultado
    assert isinstance(resultado["variations"], list)

def test_generate_variations_headline_com_contexto():
    contexto = {
        "benefit": "dobrar suas vendas",
        "action": "vender online",
        "time": "30 dias",
        "number": "7",
        "subject": "estratégias",
        "result": "10K por mês",
        "problem": "não conseguir clientes",
        "topic": "marketing",
        "percentage": "87",
    }
    resultado = generate_variations("marketing", "headline", contexto)
    variações = resultado["variations"]
    assert len(variações) > 0
    # Com contexto real, não devem ter placeholders
    for v in variações:
        assert "benefit" not in v["text"] or "dobrar suas vendas" in v["text"] or "[" not in v["text"]

def test_generate_variations_cta():
    resultado = generate_variations("teste", "cta")
    assert "variations" in resultado
    assert len(resultado["variations"]) > 0

def test_generate_variations_hook():
    resultado = generate_variations("marketing", "hook")
    assert "variations" in resultado
    assert len(resultado["variations"]) > 0

def test_generate_variations_headline_tem_psychology():
    resultado = generate_variations("tema", "headline")
    for v in resultado["variations"]:
        assert "psychology" in v

def test_generate_variations_cta_tem_categoria():
    resultado = generate_variations("tema", "cta")
    for v in resultado["variations"]:
        assert "category" in v

def test_generate_variations_elemento_invalido():
    resultado = generate_variations("tema", "elemento_inexistente")
    assert "variations" in resultado

def test_variation_templates_estrutura():
    assert "headline" in VARIATION_TEMPLATES
    assert "cta" in VARIATION_TEMPLATES
    assert "hook" in VARIATION_TEMPLATES

def test_variation_templates_headline_tem_estilos():
    estilos = VARIATION_TEMPLATES["headline"]
    assert len(estilos) >= 5

def test_variation_templates_cta_tem_categorias():
    categorias = VARIATION_TEMPLATES["cta"]
    assert "urgency" in categorias
    assert "benefit" in categorias
