#!/usr/bin/env python3
"""
Testes funcionais adicionais para ab_generator.py — cobre helpers e main().
"""
from __future__ import annotations

import json
import os
import sys
from unittest.mock import patch

import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

import ab_generator as ag


# ----------------------------------------------------------- analyze_copy
def test_analyze_copy_detecta_pergunta():
    r = ag.analyze_copy("Você sabe disso?")
    assert "question" in r["techniques_detected"]


def test_analyze_copy_detecta_numeros():
    r = ag.analyze_copy("7 estratégias matadoras")
    assert "numbers" in r["techniques_detected"]


def test_analyze_copy_detecta_personalizacao():
    r = ag.analyze_copy("Sua jornada começa aqui")
    assert "personalization" in r["techniques_detected"]


def test_analyze_copy_detecta_urgencia():
    r = ag.analyze_copy("Garante agora, é urgente!")
    assert "urgency" in r["techniques_detected"]


def test_analyze_copy_detecta_value():
    r = ag.analyze_copy("Acesso grátis ao curso")
    assert "value" in r["techniques_detected"]


def test_analyze_copy_detecta_curiosity():
    r = ag.analyze_copy("Descobrir o segredo")
    assert "curiosity" in r["techniques_detected"]


def test_analyze_copy_word_count_correto():
    r = ag.analyze_copy("uma duas três quatro")
    assert r["word_count"] == 4


def test_analyze_copy_char_count_correto():
    r = ag.analyze_copy("texto")
    assert r["char_count"] == 5


def test_analyze_copy_detecta_emoji():
    r = ag.analyze_copy("Vamos lá! 🚀")
    assert r["has_emoji"] is True


def test_analyze_copy_sem_emoji():
    r = ag.analyze_copy("Sem emoji aqui")
    assert r["has_emoji"] is False


def test_analyze_copy_detecta_caps():
    r = ag.analyze_copy("Eu disse AGORA pra você")
    assert r["has_caps"] is True


def test_analyze_copy_sem_caps():
    r = ag.analyze_copy("texto normal sem grito")
    assert r["has_caps"] is False


# ----------------------------------------------------------- get_psychology / get_cta_psychology / get_hook_psychology
def test_get_psychology_estilo_conhecido():
    msg = ag.get_psychology("question")
    assert "curiosidade" in msg.lower() or "cérebro" in msg.lower()


def test_get_psychology_estilo_desconhecido():
    assert ag.get_psychology("estilo_inexistente") == "N/A"


def test_get_cta_psychology_categoria_conhecida():
    msg = ag.get_cta_psychology("urgency")
    assert "FOMO" in msg or "escassez" in msg.lower()


def test_get_cta_psychology_desconhecida():
    assert ag.get_cta_psychology("xxx") == "N/A"


def test_get_hook_psychology_estilo_conhecido():
    msg = ag.get_hook_psychology("story")
    assert "identif" in msg.lower() or "história" in msg.lower() or "jornada" in msg.lower()


def test_get_hook_psychology_desconhecido():
    assert ag.get_hook_psychology("xxx") == "N/A"


# ----------------------------------------------------------- get_recommended_tests
def test_get_recommended_tests_headline():
    tests = ag.get_recommended_tests("headline")
    assert isinstance(tests, list)
    assert len(tests) > 0


def test_get_recommended_tests_cta():
    tests = ag.get_recommended_tests("cta")
    assert len(tests) > 0


def test_get_recommended_tests_hook():
    tests = ag.get_recommended_tests("hook")
    assert len(tests) > 0


def test_get_recommended_tests_desconhecido():
    assert ag.get_recommended_tests("xxx") == []


# ----------------------------------------------------------- generate_variations cta e hook
def test_generate_variations_cta_estrutura():
    r = ag.generate_variations("Compre agora", "cta")
    assert len(r["variations"]) > 0
    for v in r["variations"]:
        assert "category" in v
        assert "text" in v
        assert "psychology" in v


def test_generate_variations_hook_estrutura():
    r = ag.generate_variations("Imagine se", "hook")
    assert len(r["variations"]) > 0
    for v in r["variations"]:
        assert "style" in v
        assert "text" in v
        assert "psychology" in v


def test_generate_variations_tipo_invalido_sem_variations():
    r = ag.generate_variations("texto", "tipo_inexistente")
    assert r["variations"] == []


def test_generate_variations_inclui_testing_tips():
    r = ag.generate_variations("texto", "headline")
    assert "testing_tips" in r
    assert isinstance(r["testing_tips"], list)
    assert len(r["testing_tips"]) > 0


# ----------------------------------------------------------- main / CLI
def test_main_sem_args(capsys):
    with patch.object(sys, "argv", ["ab_generator.py"]):
        with pytest.raises(SystemExit):
            ag.main()
    out = capsys.readouterr().out
    assert "Uso" in out


def test_main_apenas_um_arg(capsys):
    """Precisa de 2 args; com apenas 1 sai com 1."""
    with patch.object(sys, "argv", ["ab_generator.py", "headline"]):
        with pytest.raises(SystemExit):
            ag.main()
    out = capsys.readouterr().out
    assert "Uso" in out


def test_main_tipo_e_texto(capsys):
    with patch.object(sys, "argv",
                      ["ab_generator.py", "headline", "Aprenda marketing digital"]):
        ag.main()
    out = capsys.readouterr().out
    assert "VARIAÇÕES A/B" in out
    assert "HEADLINE" in out


def test_main_com_contexto_json(capsys):
    contexto = json.dumps({"benefit": "dobrar suas vendas", "time": "30 dias"})
    with patch.object(sys, "argv",
                      ["ab_generator.py", "headline", "Aprenda algo", contexto]):
        ag.main()
    out = capsys.readouterr().out
    assert "VARIAÇÕES A/B" in out


def test_main_cta_imprime_categorias(capsys):
    with patch.object(sys, "argv", ["ab_generator.py", "cta", "Compre agora"]):
        ag.main()
    out = capsys.readouterr().out
    assert "CTA" in out


def test_main_hook_imprime_estilos(capsys):
    with patch.object(sys, "argv", ["ab_generator.py", "hook", "Olha só isso"]):
        ag.main()
    out = capsys.readouterr().out
    assert "HOOK" in out


def test_main_inclui_json_output(capsys):
    with patch.object(sys, "argv", ["ab_generator.py", "headline", "X"]):
        ag.main()
    out = capsys.readouterr().out
    assert "JSON Output" in out
    json_start = out.find("{", out.find("JSON Output"))
    parsed = json.loads(out[json_start:out.rfind("}") + 1])
    assert "variations" in parsed
