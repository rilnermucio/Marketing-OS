#!/usr/bin/env python3
"""
Testes funcionais adicionais para hashtag_generator.py — cobre main() e prints.
"""
from __future__ import annotations

import json
import os
import sys
from unittest.mock import patch

import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

import hashtag_generator as hg


# ----------------------------------------------------------- get_hashtags edge cases
def test_get_hashtags_normaliza_espacos_e_traços():
    """'marketing-digital' deve casar com 'marketing_digital'."""
    r = hg.get_hashtags("marketing-digital", "instagram")
    assert "error" not in r


def test_get_hashtags_normaliza_uppercase():
    r = hg.get_hashtags("MARKETING_DIGITAL", "instagram")
    assert "error" not in r


def test_get_hashtags_plataforma_invalida_usa_instagram():
    r = hg.get_hashtags("tecnologia", "plataforma_x")
    assert "error" not in r
    # Deve ter caído pra config do instagram
    assert r["recommended"]["count"] == hg.PLATFORM_LIMITS["instagram"]["recommended"]


def test_get_hashtags_custom_keywords_adiciona():
    r = hg.get_hashtags("tecnologia", "instagram", custom_keywords=["chatgpt", "ai"])
    extended = r["extended"]["hashtags"]
    # Custom keywords devem aparecer como #
    assert any("chatgpt" in h for h in extended) or any("ai" in h for h in extended)


def test_get_hashtags_custom_keywords_normalizadas():
    r = hg.get_hashtags("tecnologia", "instagram", custom_keywords=["machine learning"])
    extended = r["extended"]["hashtags"]
    # Espaços removidos
    assert any("machinelearning" in h for h in extended)


def test_get_hashtags_custom_keywords_max_5():
    """Keywords são truncadas a 5."""
    r = hg.get_hashtags("tecnologia", "instagram",
                        custom_keywords=["k1", "k2", "k3", "k4", "k5", "k6", "k7"])
    extended = r["extended"]["hashtags"]
    # k6 e k7 não devem aparecer
    assert not any("#k6" in h for h in extended)


def test_get_hashtags_estrutura_completa():
    r = hg.get_hashtags("financas", "instagram")
    assert "recommended" in r
    assert "extended" in r
    assert "all_available" in r
    assert "platform_tips" in r
    assert "best_practices" in r
    assert isinstance(r["best_practices"], list)


def test_get_hashtags_recommended_menor_que_extended():
    r = hg.get_hashtags("financas", "instagram")
    assert r["recommended"]["count"] <= r["extended"]["count"]


# ----------------------------------------------------------- main / CLI
def test_main_sem_args(capsys):
    with patch.object(sys, "argv", ["hashtag_generator.py"]):
        with pytest.raises(SystemExit):
            hg.main()
    out = capsys.readouterr().out
    assert "Uso" in out
    assert "Nichos disponíveis" in out


def test_main_nicho_valido(capsys):
    with patch.object(sys, "argv", ["hashtag_generator.py", "marketing_digital", "instagram"]):
        hg.main()
    out = capsys.readouterr().out
    assert "HASHTAGS" in out
    assert "RECOMENDADAS" in out


def test_main_nicho_invalido_falha(capsys):
    with patch.object(sys, "argv", ["hashtag_generator.py", "nicho_inventado_xyz"]):
        with pytest.raises(SystemExit):
            hg.main()
    out = capsys.readouterr().out
    assert "não encontrado" in out


def test_main_com_keywords_customizadas(capsys):
    with patch.object(sys, "argv",
                      ["hashtag_generator.py", "tecnologia", "instagram", "ia", "chatgpt"]):
        hg.main()
    out = capsys.readouterr().out
    assert "HASHTAGS" in out
    # JSON output deve estar presente
    assert "JSON Output" in out
    json_start = out.find("{", out.find("JSON Output"))
    json_text = out[json_start:].rsplit("}", 1)[0] + "}"
    parsed = json.loads(json_text)
    extended = parsed["extended"]["hashtags"]
    assert any("ia" in h or "chatgpt" in h for h in extended)


def test_main_plataforma_invalida_falha_validacao(capsys):
    with patch.object(sys, "argv",
                      ["hashtag_generator.py", "tecnologia", "plataforma_inexistente"]):
        with pytest.raises(SystemExit):
            hg.main()
    err = capsys.readouterr().err
    # validar_plataforma deve gerar erro de validação
    assert "Erro" in err or "erro" in err.lower() or "inválid" in err.lower()
