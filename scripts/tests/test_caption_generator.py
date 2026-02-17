#!/usr/bin/env python3
"""
Testes para caption_generator.py
"""

import sys
import os
import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from caption_generator import (
    ESTRUTURAS,
)


def test_estruturas_tem_objetivos():
    objetivos_esperados = ["engajamento", "educativo", "storytelling", "vendas", "autoridade"]
    for obj in objetivos_esperados:
        assert obj in ESTRUTURAS, f"Objetivo {obj} não encontrado"

def test_estruturas_tem_nome():
    for obj, dados in ESTRUTURAS.items():
        assert "nome" in dados, f"Objetivo {obj} sem 'nome'"

def test_estruturas_tem_formato():
    for obj, dados in ESTRUTURAS.items():
        assert "formato" in dados, f"Objetivo {obj} sem 'formato'"
        assert len(dados["formato"]) >= 3, f"Objetivo {obj} com menos de 3 elementos"

def test_estruturas_tem_tamanho():
    for obj, dados in ESTRUTURAS.items():
        assert "tamanho" in dados, f"Objetivo {obj} sem 'tamanho'"

def test_estruturas_engajamento_tem_pergunta():
    fmt = ESTRUTURAS["engajamento"]["formato"]
    fmt_str = " ".join(fmt).lower()
    assert "pergunta" in fmt_str or "hook" in fmt_str.lower()

def test_estruturas_vendas_tem_cta():
    fmt = ESTRUTURAS["vendas"]["formato"]
    fmt_str = " ".join(fmt).upper()
    assert "CTA" in fmt_str

def test_estruturas_storytelling_tem_historia():
    fmt = ESTRUTURAS["storytelling"]["formato"]
    fmt_str = " ".join(fmt).upper()
    assert "HISTÓRIA" in fmt_str or "STORY" in fmt_str or "CONFLITO" in fmt_str or "SETUP" in fmt_str
