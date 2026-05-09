#!/usr/bin/env python3
"""
Testes funcionais para content_calendar.py.
"""
from __future__ import annotations

import json
import os
import sys
from datetime import datetime, timedelta
from unittest.mock import patch

import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

import content_calendar as cc


# ----------------------------------------------------------- generate_calendar
def test_generate_calendar_estrutura_basica():
    r = cc.generate_calendar("2026-01-05", weeks=2, platforms=["instagram"])
    assert "calendar" in r
    assert "summary" in r
    assert "recommendations" in r
    assert "content_pillars" in r


def test_generate_calendar_quantidade_de_semanas():
    r = cc.generate_calendar("2026-01-05", weeks=4, platforms=["instagram"])
    assert len(r["calendar"]) == 4
    for week in r["calendar"]:
        assert len(week["days"]) == 7


def test_generate_calendar_default_instagram_se_sem_plataformas():
    r = cc.generate_calendar("2026-01-05", weeks=1)
    assert r["summary"]["platforms"] == ["instagram"]


def test_generate_calendar_multiplas_plataformas():
    r = cc.generate_calendar("2026-01-05", weeks=1, platforms=["instagram", "linkedin"])
    assert "instagram" in r["summary"]["platforms"]
    assert "linkedin" in r["summary"]["platforms"]
    # Todos os dias têm ambas as plataformas
    for week in r["calendar"]:
        for day in week["days"]:
            assert "instagram" in day["platforms"]
            assert "linkedin" in day["platforms"]


def test_generate_calendar_fim_de_semana_usa_horarios_weekend():
    r = cc.generate_calendar("2026-01-03", weeks=1, platforms=["instagram"])
    # 2026-01-03 é sábado
    sat = r["calendar"][0]["days"][0]
    assert sat["day_of_week"] == "Saturday"
    assert sat["platforms"]["instagram"]["suggested_times"] == cc.BEST_TIMES["instagram"]["weekend"]


def test_generate_calendar_dia_de_semana_usa_horarios_weekday():
    # 2026-01-05 é segunda
    r = cc.generate_calendar("2026-01-05", weeks=1, platforms=["instagram"])
    mon = r["calendar"][0]["days"][0]
    assert mon["day_of_week"] == "Monday"
    assert mon["platforms"]["instagram"]["suggested_times"] == cc.BEST_TIMES["instagram"]["weekday"]


def test_generate_calendar_tema_corresponde_ao_dia():
    r = cc.generate_calendar("2026-01-05", weeks=1, platforms=["instagram"])
    monday = r["calendar"][0]["days"][0]  # 2026-01-05 = segunda
    assert monday["theme"] == cc.CONTENT_THEMES["monday"]["theme"]


def test_generate_calendar_plataforma_desconhecida_usa_instagram_horarios():
    """Plataforma sem horários específicos → fallback pra instagram."""
    r = cc.generate_calendar("2026-01-05", weeks=1, platforms=["plataforma_inventada"])
    assert "plataforma_inventada" in r["summary"]["platforms"]
    times = r["calendar"][0]["days"][0]["platforms"]["plataforma_inventada"]["suggested_times"]
    # Deve ter caído pro instagram
    assert times == cc.BEST_TIMES["instagram"]["weekday"]


def test_generate_calendar_summary_correto():
    r = cc.generate_calendar("2026-01-05", weeks=2)
    s = r["summary"]
    assert s["total_weeks"] == 2
    assert s["start_date"] == "2026-01-05"
    # End date é 13 dias depois
    end = datetime.strptime(s["end_date"], "%Y-%m-%d")
    assert end == datetime(2026, 1, 5) + timedelta(weeks=1, days=6)


def test_generate_calendar_pillars_somam_100():
    r = cc.generate_calendar("2026-01-05", weeks=1)
    total = sum(p["percentage"] for p in r["content_pillars"])
    assert total == 100


def test_generate_calendar_recommendations_nao_vazias():
    r = cc.generate_calendar("2026-01-05", weeks=1)
    for k, v in r["recommendations"].items():
        assert isinstance(v, str) and len(v) > 0


# ----------------------------------------------------------- main / CLI
def test_main_sem_args(capsys):
    with patch.object(sys, "argv", ["content_calendar.py"]):
        with pytest.raises(SystemExit):
            cc.main()
    out = capsys.readouterr().out
    assert "Uso" in out


def test_main_data_invalida_falha(capsys):
    with patch.object(sys, "argv", ["content_calendar.py", "data_invalida"]):
        with pytest.raises(SystemExit):
            cc.main()
    err = capsys.readouterr().err
    assert "Erro" in err or "validação" in err.lower()


def test_main_data_valida_imprime_calendario(tmp_path, monkeypatch, capsys):
    # Roda com cwd em tmp_path porque o script salva JSON
    monkeypatch.chdir(tmp_path)
    with patch.object(sys, "argv", ["content_calendar.py", "2026-01-05", "1", "instagram"]):
        cc.main()
    out = capsys.readouterr().out
    assert "CALENDÁRIO EDITORIAL" in out
    assert "PILARES DE CONTEÚDO" in out
    # Arquivo JSON deve ter sido criado
    arquivos = list(tmp_path.glob("calendar_*.json"))
    assert len(arquivos) == 1
    parsed = json.loads(arquivos[0].read_text(encoding="utf-8"))
    assert parsed["summary"]["start_date"] == "2026-01-05"


def test_main_data_valida_default_4_semanas(tmp_path, monkeypatch, capsys):
    monkeypatch.chdir(tmp_path)
    with patch.object(sys, "argv", ["content_calendar.py", "2026-01-05"]):
        cc.main()
    out = capsys.readouterr().out
    assert "Semanas: 4" in out


def test_main_multiplas_plataformas(tmp_path, monkeypatch, capsys):
    monkeypatch.chdir(tmp_path)
    with patch.object(sys, "argv",
                      ["content_calendar.py", "2026-01-05", "1", "instagram", "linkedin"]):
        cc.main()
    out = capsys.readouterr().out
    assert "instagram" in out
    assert "linkedin" in out
