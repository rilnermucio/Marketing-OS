#!/usr/bin/env python3
"""
Testes para hashtag_generator.py
"""

import sys
import os
import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from hashtag_generator import (
    get_hashtags,
    HASHTAG_DATABASE,
    PLATFORM_LIMITS,
)


def test_get_hashtags_nicho_valido():
    resultado = get_hashtags("marketing_digital", "instagram")
    assert "error" not in resultado
    # A API retorna hashtas em resultado["recommended"]["hashtags"]
    assert "recommended" in resultado or "all_available" in resultado

def test_get_hashtags_nicho_invalido():
    resultado = get_hashtags("nicho_invalido_xyz", "instagram")
    assert "error" in resultado
    assert "available_niches" in resultado

def test_get_hashtags_plataformas():
    plataformas = ["instagram", "linkedin", "twitter", "tiktok", "facebook"]
    for plataforma in plataformas:
        resultado = get_hashtags("tecnologia", plataforma)
        assert "error" not in resultado, f"Erro na plataforma {plataforma}"

def test_get_hashtags_respeita_limite_instagram():
    resultado = get_hashtags("marketing_digital", "instagram")
    if "recommended" in resultado:
        hashtags = resultado["recommended"]["hashtags"]
        limite = PLATFORM_LIMITS["instagram"]["max"]
        assert len(hashtags) <= limite

def test_get_hashtags_respeita_limite_twitter():
    resultado = get_hashtags("tecnologia", "twitter")
    if "recommended" in resultado:
        hashtags = resultado["recommended"]["hashtags"]
        limite = PLATFORM_LIMITS["twitter"]["max"]
        assert len(hashtags) <= limite

def test_get_hashtags_formato_correto():
    resultado = get_hashtags("empreendedorismo", "instagram")
    if "recommended" in resultado:
        for h in resultado["recommended"]["hashtags"]:
            assert h.startswith("#"), f"Hashtag sem #: {h}"

def test_get_hashtags_custom_keywords():
    keywords_custom = ["#minhahashtag", "#customizada"]
    resultado = get_hashtags("financas", "instagram", custom_keywords=keywords_custom)
    assert "error" not in resultado

def test_hashtag_database_tem_nichos():
    assert len(HASHTAG_DATABASE) >= 6

def test_platform_limits_tem_plataformas():
    assert "instagram" in PLATFORM_LIMITS
    assert "linkedin" in PLATFORM_LIMITS
    assert "twitter" in PLATFORM_LIMITS
    assert "tiktok" in PLATFORM_LIMITS

def test_platform_limits_estrutura():
    for plataforma, config in PLATFORM_LIMITS.items():
        assert "max" in config
        assert "recommended" in config
        assert config["recommended"] <= config["max"]
