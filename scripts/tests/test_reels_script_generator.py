#!/usr/bin/env python3
"""
Testes para reels_script_generator.py
"""

import sys
import os
import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from reels_script_generator import (
    ESTRUTURAS,
)


def test_estruturas_tem_formatos():
    formatos_esperados = ["tutorial", "listicle", "storytime", "antes_depois", "pov", "trend", "problema_solucao"]
    for fmt in formatos_esperados:
        assert fmt in ESTRUTURAS, f"Formato {fmt} não encontrado"

def test_estruturas_tem_nome():
    for formato, dados in ESTRUTURAS.items():
        assert "nome" in dados, f"Formato {formato} sem 'nome'"

def test_estruturas_tem_sequencia():
    for formato, dados in ESTRUTURAS.items():
        assert "estrutura" in dados, f"Formato {formato} sem 'estrutura'"
        assert len(dados["estrutura"]) >= 3, f"Formato {formato} com menos de 3 segmentos"

def test_estruturas_segmentos_tem_campos():
    for formato, dados in ESTRUTURAS.items():
        for segmento in dados["estrutura"]:
            assert "tempo" in segmento, f"Segmento sem 'tempo' em {formato}"
            assert "tipo" in segmento, f"Segmento sem 'tipo' em {formato}"
            assert "descricao" in segmento, f"Segmento sem 'descricao' em {formato}"

def test_estruturas_primeiro_segmento_hook():
    # Todo formato deve começar com hook ou setup
    formatos_com_hook = ["tutorial", "listicle", "storytime", "antes_depois", "problema_solucao"]
    for fmt in formatos_com_hook:
        primeiro = ESTRUTURAS[fmt]["estrutura"][0]
        assert "HOOK" in primeiro["tipo"] or "SETUP" in primeiro["tipo"] or "SYNC" in primeiro["tipo"]
