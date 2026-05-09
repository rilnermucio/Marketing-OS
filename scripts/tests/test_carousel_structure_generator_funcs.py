#!/usr/bin/env python3
"""
Testes funcionais para carousel_structure_generator.py.
"""
from __future__ import annotations

import json
import os
import sys
from unittest.mock import patch

import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

import carousel_structure_generator as csg


# ----------------------------------------------------------- gerar_estrutura
def test_gerar_estrutura_tipo_valido():
    r = csg.gerar_estrutura("tema X", "educativo", 5)
    assert r["tema"] == "tema X"
    assert r["tipo"] == csg.ESTRUTURAS["educativo"]["nome"]
    assert r["num_slides"] == 5


def test_gerar_estrutura_tipo_invalido_default_educativo():
    r = csg.gerar_estrutura("tema X", "tipo_inexistente", 5)
    assert r["tipo"] == csg.ESTRUTURAS["educativo"]["nome"]


def test_gerar_estrutura_tem_paleta_valida():
    r = csg.gerar_estrutura("X", "educativo", 5)
    assert "paleta" in r
    assert "nome" in r["paleta"]
    assert "cores" in r["paleta"]
    assert isinstance(r["paleta"]["cores"], list)
    assert len(r["paleta"]["cores"]) >= 3


def test_gerar_estrutura_tem_fontes():
    r = csg.gerar_estrutura("X", "educativo", 5)
    assert "fontes" in r
    assert "titulo" in r["fontes"]
    assert "corpo" in r["fontes"]
    assert "destaque" in r["fontes"]


def test_gerar_estrutura_slides_truncados():
    r = csg.gerar_estrutura("X", "educativo", 3)
    assert len(r["slides"]) == 3
    # Cada slide tem campos esperados
    for s in r["slides"]:
        assert "num" in s
        assert "tipo" in s
        assert "elementos" in s
        assert "objetivo" in s


def test_gerar_estrutura_pede_mais_slides_que_existe():
    """Pedir 50 slides quando há só 10 → retorna no máximo 10."""
    r = csg.gerar_estrutura("X", "educativo", 50)
    assert r["num_slides"] <= 10


def test_gerar_estrutura_todos_os_tipos():
    for tipo in csg.ESTRUTURAS:
        r = csg.gerar_estrutura("X", tipo, 5)
        assert r["tipo"] == csg.ESTRUTURAS[tipo]["nome"]


# ----------------------------------------------------------- formatar_saida
def test_formatar_saida_inclui_tema_e_tipo():
    r = csg.gerar_estrutura("Marketing Digital", "educativo", 5)
    out = csg.formatar_saida(r)
    assert "Marketing Digital" in out
    assert "ESTRUTURA DE CARROSSEL" in out


def test_formatar_saida_lista_paleta_e_fontes():
    r = csg.gerar_estrutura("X", "educativo", 5)
    out = csg.formatar_saida(r)
    assert r["paleta"]["nome"] in out
    assert r["fontes"]["titulo"] in out


def test_formatar_saida_lista_todos_slides():
    r = csg.gerar_estrutura("X", "tutorial", 5)
    out = csg.formatar_saida(r)
    for s in r["slides"]:
        assert s["tipo"] in out


def test_formatar_saida_inclui_dicas_design():
    r = csg.gerar_estrutura("X", "educativo", 5)
    out = csg.formatar_saida(r)
    assert "DICAS DE DESIGN" in out


# ----------------------------------------------------------- listar_tipos
def test_listar_tipos_imprime_todos(capsys):
    csg.listar_tipos()
    out = capsys.readouterr().out
    for k in csg.ESTRUTURAS:
        assert k in out


# ----------------------------------------------------------- main / CLI
def test_main_sem_args(capsys):
    with patch.object(sys, "argv", ["carousel_structure_generator.py"]):
        csg.main()
    out = capsys.readouterr().out
    assert "Uso" in out
    assert "TIPOS DE CARROSSEL" in out


def test_main_flag_tipos(capsys):
    with patch.object(sys, "argv", ["carousel_structure_generator.py", "--tipos"]):
        csg.main()
    out = capsys.readouterr().out
    assert "TIPOS DE CARROSSEL" in out


def test_main_tema_padrao_educativo(capsys):
    with patch.object(sys, "argv", ["carousel_structure_generator.py", "tema teste"]):
        csg.main()
    out = capsys.readouterr().out
    assert "tema teste" in out


def test_main_tema_tipo_e_slides(capsys):
    with patch.object(sys, "argv",
                      ["carousel_structure_generator.py", "tema X", "tutorial", "7"]):
        csg.main()
    out = capsys.readouterr().out
    assert "tema X" in out
    assert csg.ESTRUTURAS["tutorial"]["nome"] in out


def test_main_modo_json(capsys):
    with patch.object(sys, "argv",
                      ["carousel_structure_generator.py", "tema X", "lista", "5", "--json"]):
        csg.main()
    out = capsys.readouterr().out
    parsed = json.loads(out)
    assert parsed["tema"] == "tema X"
    assert parsed["num_slides"] == 5


def test_main_num_slides_alto_avisa_e_ajusta(capsys):
    """11 slides está fora do range recomendado, mas script ajusta."""
    with patch.object(sys, "argv",
                      ["carousel_structure_generator.py", "tema X", "educativo", "12"]):
        csg.main()
    out = capsys.readouterr().out
    assert "Recomendado" in out


def test_main_num_slides_baixo_avisa_e_ajusta(capsys):
    """3 slides ainda passa pela validação (min_val=3 no validar_inteiro)."""
    with patch.object(sys, "argv",
                      ["carousel_structure_generator.py", "tema X", "educativo", "3"]):
        csg.main()
    out = capsys.readouterr().out
    # 3 está dentro do limite, vai gerar
    assert "tema X" in out
