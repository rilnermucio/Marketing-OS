#!/usr/bin/env python3
"""
Testes para trend_adapter.py
"""

import sys
import os
import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from trend_adapter import (
    TRENDS,
)


def test_trends_nao_vazio():
    assert len(TRENDS) >= 8

def test_trends_tem_campos_obrigatorios():
    for trend_key, dados in TRENDS.items():
        assert "nome" in dados, f"Trend {trend_key} sem 'nome'"
        assert "original" in dados, f"Trend {trend_key} sem 'original'"
        assert "estrutura" in dados, f"Trend {trend_key} sem 'estrutura'"
        assert "duracao" in dados, f"Trend {trend_key} sem 'duração'"
        assert "audio" in dados, f"Trend {trend_key} sem 'audio'"

def test_trends_estrutura_nao_vazia():
    for trend_key, dados in TRENDS.items():
        assert len(dados["estrutura"]) >= 2, f"Trend {trend_key} com menos de 2 passos"

def test_trends_tem_get_ready_with_me():
    assert "get_ready_with_me" in TRENDS

def test_trends_tem_storytime():
    assert "storytime" in TRENDS

def test_trends_tem_antes_depois():
    assert "antes_depois" in TRENDS

def test_trends_duracao_formato():
    for trend_key, dados in TRENDS.items():
        duracao = dados["duracao"]
        assert isinstance(duracao, str)
        assert len(duracao) > 0
