#!/usr/bin/env python3
"""
Testes para carousel_structure_generator.py
"""

import sys
import os
import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from carousel_structure_generator import (
    ESTRUTURAS,
)


def test_estruturas_tem_tipos():
    tipos_esperados = ["educativo", "storytelling", "lista", "tutorial", "mito_verdade"]
    for tipo in tipos_esperados:
        assert tipo in ESTRUTURAS, f"Tipo {tipo} não encontrado"

def test_estruturas_tem_nome():
    for tipo, dados in ESTRUTURAS.items():
        assert "nome" in dados, f"Tipo {tipo} sem 'nome'"

def test_estruturas_tem_slides():
    for tipo, dados in ESTRUTURAS.items():
        assert "slides" in dados, f"Tipo {tipo} sem 'slides'"
        assert len(dados["slides"]) >= 5, f"Tipo {tipo} com menos de 5 slides"

def test_estruturas_slides_tem_campos():
    for tipo, dados in ESTRUTURAS.items():
        for slide in dados["slides"]:
            assert "num" in slide, f"Slide sem 'num' em {tipo}"
            assert "tipo" in slide, f"Slide sem 'tipo' em {tipo}"
            assert "elementos" in slide, f"Slide sem 'elementos' em {tipo}"
            assert "objetivo" in slide, f"Slide sem 'objetivo' em {tipo}"

def test_estruturas_primeiro_slide_capa():
    for tipo, dados in ESTRUTURAS.items():
        primeiro = dados["slides"][0]
        assert primeiro["num"] == 1
        assert "CAPA" in primeiro["tipo"]

def test_estruturas_ultimo_slide_cta():
    for tipo, dados in ESTRUTURAS.items():
        ultimo = dados["slides"][-1]
        assert "CTA" in ultimo["tipo"], f"Último slide de {tipo} não é CTA"

def test_estruturas_numeracao_sequencial():
    for tipo, dados in ESTRUTURAS.items():
        nums = [s["num"] for s in dados["slides"]]
        for i, num in enumerate(nums, 1):
            assert num == i, f"Numeração não sequencial em {tipo}: esperado {i}, got {num}"
