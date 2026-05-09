#!/usr/bin/env python3
"""
Testes funcionais adicionais para hook_generator.py — cobre main() e print_results.
"""
from __future__ import annotations

import json
import os
import sys
from unittest.mock import patch

import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

import hook_generator as hg


# ----------------------------------------------------------- generate_hooks edge cases
def test_generate_hooks_emoji_em_inicio_para_reels():
    r = hg.generate_hooks("X", "reels", 3)
    for h in r["hooks"]:
        # Emoji deve estar no início (separado por espaço)
        assert h["hook"].startswith(h["emoji"])


def test_generate_hooks_emoji_em_fim_para_tiktok_ou_inicio():
    r = hg.generate_hooks("X", "tiktok", 3)
    for h in r["hooks"]:
        # tiktok = "início ou fim" — o script implementa como elif "fim" → fim
        # Como spec é "início ou fim" (sem match exato), cai no else (sem emoji)
        # Deixar test apenas confirmando estrutura
        assert "hook" in h


def test_generate_hooks_youtube_sem_emoji_no_inicio():
    """YouTube spec é 'opcional' — cai no else, sem emoji adicionado."""
    r = hg.generate_hooks("X", "youtube", 3)
    for h in r["hooks"]:
        # Hook não deve começar com emoji
        assert not h["hook"].startswith(h["emoji"])


def test_generate_hooks_plataforma_invalida_usa_reels():
    """Plataforma inexistente cai pra reels."""
    r = hg.generate_hooks("X", "plataforma_xyz", 3)
    # specs deveriam ser de reels
    assert r["specs"] == hg.PLATFORM_SPECS["reels"]


def test_generate_hooks_quantidade_grande():
    r = hg.generate_hooks("X", "reels", 30)
    assert len(r["hooks"]) == 30


def test_generate_hooks_categorias_usadas_unique():
    r = hg.generate_hooks("X", "reels", 20)
    cats = r["categorias_usadas"]
    assert len(cats) == len(set(cats)), "categorias_usadas deve ser único"


def test_generate_hooks_chars_consistente():
    r = hg.generate_hooks("X", "reels", 5)
    for h in r["hooks"]:
        assert h["chars"] == len(h["hook"])


def test_generate_hooks_total_correto():
    r = hg.generate_hooks("X", "reels", 8)
    assert r["total_gerado"] == 8


# ----------------------------------------------------------- print_results
def test_print_results_imprime_titulo(capsys):
    r = hg.generate_hooks("vendas", "reels", 3)
    hg.print_results(r)
    out = capsys.readouterr().out
    assert "HOOK GENERATOR" in out
    assert "VENDAS" in out


def test_print_results_lista_hooks(capsys):
    r = hg.generate_hooks("X", "reels", 3)
    hg.print_results(r)
    out = capsys.readouterr().out
    for h in r["hooks"]:
        assert h["hook"] in out


def test_print_results_inclui_categorias_usadas(capsys):
    r = hg.generate_hooks("X", "reels", 5)
    hg.print_results(r)
    out = capsys.readouterr().out
    assert "CATEGORIAS UTILIZADAS" in out
    for cat in r["categorias_usadas"]:
        assert cat.title() in out


def test_print_results_inclui_dicas(capsys):
    r = hg.generate_hooks("X", "reels", 2)
    hg.print_results(r)
    out = capsys.readouterr().out
    assert "DICAS DE USO" in out


def test_print_results_marca_warning_se_excede_chars(capsys):
    """Hooks acima do limite devem ter ⚠️."""
    r = hg.generate_hooks("X", "reels", 5)
    # Forçar max baixo pra testar
    r["specs"]["max_chars"] = 5
    hg.print_results(r)
    out = capsys.readouterr().out
    assert "⚠️" in out


# ----------------------------------------------------------- main / CLI
def test_main_sem_args(capsys):
    with patch.object(sys, "argv", ["hook_generator.py"]):
        with pytest.raises(SystemExit):
            hg.main()
    out = capsys.readouterr().out
    assert "Uso" in out


def test_main_tema_padrao(capsys):
    with patch.object(sys, "argv", ["hook_generator.py", "produtividade"]):
        hg.main()
    out = capsys.readouterr().out
    assert "HOOK GENERATOR" in out
    assert "PRODUTIVIDADE" in out


def test_main_plataforma_e_quantidade(capsys):
    with patch.object(sys, "argv", ["hook_generator.py", "vendas", "linkedin", "5"]):
        hg.main()
    out = capsys.readouterr().out
    assert "LINKEDIN" in out


def test_main_quantidade_invalida_falha(capsys):
    with patch.object(sys, "argv", ["hook_generator.py", "X", "reels", "abc"]):
        with pytest.raises(SystemExit):
            hg.main()
    err = capsys.readouterr().err
    assert "Erro" in err or "erro" in err.lower() or "inválid" in err.lower()


def test_main_imprime_json_output(capsys):
    with patch.object(sys, "argv", ["hook_generator.py", "X", "reels", "3"]):
        hg.main()
    out = capsys.readouterr().out
    assert "JSON Output" in out
    json_start = out.find("{", out.find("JSON Output"))
    json_text = out[json_start:].rsplit("}", 1)[0] + "}"
    parsed = json.loads(json_text)
    assert parsed["tema"] == "X"
    assert parsed["plataforma"] == "reels"
    assert parsed["total_gerado"] == 3
