#!/usr/bin/env python3
"""
Testes funcionais para trend_adapter.py.
"""
from __future__ import annotations

import json
import os
import sys
from unittest.mock import patch

import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

import trend_adapter as ta


# ----------------------------------------------------------- adaptar_trend
def test_adaptar_trend_chave_existente():
    r = ta.adaptar_trend("storytime", "marketing")
    assert r["trend"]["nome"] == ta.TRENDS["storytime"]["nome"]
    assert r["nicho"] == "marketing"
    assert isinstance(r["adaptacao"], str)
    assert "ideias_adicionais" in r


def test_adaptar_trend_chave_inexistente_cai_default():
    r = ta.adaptar_trend("trend_que_nao_existe_mesmo", "tech")
    # Deve cair pra tutorial_rapido
    assert r["trend"]["nome"] == ta.TRENDS["tutorial_rapido"]["nome"]


def test_adaptar_trend_match_parcial_de_chave():
    """Chave parcial deve achar trend similar."""
    r = ta.adaptar_trend("get_ready", "lifestyle")
    # 'get_ready' está contido em 'get_ready_with_me'
    assert r["trend"]["nome"] == ta.TRENDS["get_ready_with_me"]["nome"]


def test_adaptar_trend_nicho_invalido_cai_para_lifestyle():
    r = ta.adaptar_trend("storytime", "nicho_inexistente")
    assert r["nicho"] == "lifestyle"


def test_adaptar_trend_retorna_estrutura_completa():
    r = ta.adaptar_trend("pov", "tech")
    assert "trend" in r
    assert "nicho" in r
    assert "adaptacao" in r
    assert "ideias_adicionais" in r
    assert isinstance(r["ideias_adicionais"], list)


# ----------------------------------------------------------- gerar_ideias_adicionais
def test_gerar_ideias_adicionais_chave_conhecida():
    ideias = ta.gerar_ideias_adicionais("get_ready_with_me", "marketing")
    assert isinstance(ideias, list)
    assert len(ideias) >= 1


def test_gerar_ideias_adicionais_chave_desconhecida_default():
    ideias = ta.gerar_ideias_adicionais("trend_xyz", "marketing")
    assert isinstance(ideias, list)
    assert len(ideias) >= 1
    # Default deve mencionar nicho
    assert any("marketing" in i for i in ideias)


# ----------------------------------------------------------- formatar_saida
def test_formatar_saida_inclui_nome_trend():
    r = ta.adaptar_trend("storytime", "tech")
    out = ta.formatar_saida(r)
    assert r["trend"]["nome"] in out


def test_formatar_saida_inclui_nicho_uppercase():
    r = ta.adaptar_trend("storytime", "marketing")
    out = ta.formatar_saida(r)
    assert "MARKETING" in out


def test_formatar_saida_inclui_estrutura_numerada():
    r = ta.adaptar_trend("storytime", "marketing")
    out = ta.formatar_saida(r)
    assert "1. " in out


def test_formatar_saida_inclui_ideias_adicionais():
    r = ta.adaptar_trend("storytime", "marketing")
    out = ta.formatar_saida(r)
    assert "IDEIAS ADICIONAIS" in out
    for ideia in r["ideias_adicionais"]:
        assert ideia in out


def test_formatar_saida_inclui_dicas_gerais():
    r = ta.adaptar_trend("storytime", "marketing")
    out = ta.formatar_saida(r)
    assert "DICAS PARA VIRALIZAR" in out


# ----------------------------------------------------------- listar_*
def test_listar_trends_imprime_todas(capsys):
    ta.listar_trends()
    out = capsys.readouterr().out
    for k, v in ta.TRENDS.items():
        assert k in out
        assert v["nome"] in out


def test_listar_nichos_imprime_todos(capsys):
    ta.listar_nichos()
    out = capsys.readouterr().out
    for nicho in ta.ADAPTACOES.keys():
        assert nicho in out


# ----------------------------------------------------------- main / CLI
def test_main_sem_args_lista_help(capsys):
    with patch.object(sys, "argv", ["trend_adapter.py"]):
        ta.main()
    out = capsys.readouterr().out
    assert "Uso" in out
    assert "TRENDS DISPONÍVEIS" in out
    assert "NICHOS DISPONÍVEIS" in out


def test_main_flag_trends_lista(capsys):
    with patch.object(sys, "argv", ["trend_adapter.py", "--trends"]):
        ta.main()
    out = capsys.readouterr().out
    assert "TRENDS DISPONÍVEIS" in out


def test_main_flag_nichos_lista(capsys):
    with patch.object(sys, "argv", ["trend_adapter.py", "--nichos"]):
        ta.main()
    out = capsys.readouterr().out
    assert "NICHOS DISPONÍVEIS" in out


def test_main_trend_e_nicho_imprime_saida(capsys):
    with patch.object(sys, "argv", ["trend_adapter.py", "storytime", "marketing"]):
        ta.main()
    out = capsys.readouterr().out
    assert "TREND ADAPTER" in out
    assert "MARKETING" in out


def test_main_modo_json(capsys):
    with patch.object(sys, "argv", ["trend_adapter.py", "storytime", "marketing", "--json"]):
        ta.main()
    out = capsys.readouterr().out
    parsed = json.loads(out)
    assert parsed["nicho"] == "marketing"
    assert "trend" in parsed
    assert "adaptacao" in parsed


def test_main_normaliza_espacos_e_traços(capsys):
    """'get ready with me' (espaços) → 'get_ready_with_me' (chave)"""
    with patch.object(sys, "argv", ["trend_adapter.py", "get ready with me", "tech", "--json"]):
        ta.main()
    out = capsys.readouterr().out
    parsed = json.loads(out)
    assert parsed["trend"]["nome"] == ta.TRENDS["get_ready_with_me"]["nome"]
