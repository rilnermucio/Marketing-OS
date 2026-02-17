#!/usr/bin/env python3
"""
Testes para content_idea_generator.py
"""

import sys
import os
import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from content_idea_generator import (
    PILARES,
)


def test_pilares_tem_nichos():
    nichos_esperados = ["tecnologia", "marketing_digital", "empreendedorismo"]
    for nicho in nichos_esperados:
        assert nicho in PILARES, f"Nicho {nicho} não encontrado"

def test_pilares_estrutura():
    for nicho, dados in PILARES.items():
        assert "pilares" in dados, f"Nicho {nicho} sem 'pilares'"
        assert "temas" in dados, f"Nicho {nicho} sem 'temas'"
        assert "problemas" in dados, f"Nicho {nicho} sem 'problemas'"

def test_pilares_nao_vazio():
    for nicho, dados in PILARES.items():
        assert len(dados["pilares"]) > 0
        assert len(dados["temas"]) > 0
        assert len(dados["problemas"]) > 0

def test_pilares_tecnologia_tem_ia():
    temas = PILARES["tecnologia"]["temas"]
    temas_lower = [t.lower() for t in temas]
    assert any("ia" in t or "chatgpt" in t or "automação" in t.lower() for t in temas)
