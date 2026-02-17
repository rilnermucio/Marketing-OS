#!/usr/bin/env python3
"""
Testes para content_calendar.py
"""

import sys
import os
import json
import pytest
from datetime import datetime

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from content_calendar import (
    CONTENT_THEMES,
    BEST_TIMES,
    FREQUENCY,
)


def test_content_themes_tem_sete_dias():
    dias = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
    for dia in dias:
        assert dia in CONTENT_THEMES, f"Dia {dia} não encontrado"

def test_content_themes_estrutura():
    for dia, dados in CONTENT_THEMES.items():
        assert "theme" in dados, f"Dia {dia} sem 'theme'"
        assert "ideas" in dados, f"Dia {dia} sem 'ideas'"
        assert "formats" in dados, f"Dia {dia} sem 'formats'"
        assert len(dados["ideas"]) > 0
        assert len(dados["formats"]) > 0

def test_best_times_plataformas():
    plataformas_esperadas = ["instagram", "linkedin", "twitter", "tiktok", "facebook"]
    for p in plataformas_esperadas:
        assert p in BEST_TIMES, f"Plataforma {p} não encontrada"

def test_best_times_estrutura():
    for plataforma, horarios in BEST_TIMES.items():
        assert "weekday" in horarios
        assert "weekend" in horarios
        assert len(horarios["weekday"]) > 0

def test_best_times_formato_hora():
    for plataforma, horarios in BEST_TIMES.items():
        for h in horarios["weekday"] + horarios["weekend"]:
            assert ":" in h, f"Horário inválido em {plataforma}: {h}"

def test_frequency_plataformas():
    plataformas = ["instagram", "linkedin", "twitter", "tiktok"]
    for p in plataformas:
        assert p in FREQUENCY, f"Plataforma {p} não encontrada"

def test_frequency_nao_vazio():
    for plataforma, freq in FREQUENCY.items():
        assert len(freq) > 0
