#!/usr/bin/env python3
"""
Testes para hook_variant_generator.py
"""

import sys
import os
import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from hook_variant_generator import (
    FORMULAS_HOOKS,
)


def test_formulas_hooks_tem_categorias():
    categorias_esperadas = ["curiosidade", "numeros", "dor", "transformacao", "urgencia"]
    for cat in categorias_esperadas:
        assert cat in FORMULAS_HOOKS, f"Categoria {cat} não encontrada"

def test_formulas_hooks_nao_vazias():
    for categoria, formulas in FORMULAS_HOOKS.items():
        assert len(formulas) >= 5, f"Categoria {categoria} com menos de 5 fórmulas"

def test_formulas_hooks_tem_placeholder_tema():
    for categoria, formulas in FORMULAS_HOOKS.items():
        for formula in formulas:
            assert "{tema}" in formula or "{" in formula, f"Fórmula sem placeholder: {formula}"

def test_formulas_hooks_strings():
    for categoria, formulas in FORMULAS_HOOKS.items():
        for formula in formulas:
            assert isinstance(formula, str)
