#!/usr/bin/env python3
"""
Testes funcionais para content_idea_generator.py.
"""
from __future__ import annotations

import json
import os
import sys
from unittest.mock import patch

import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

import content_idea_generator as cig


# ----------------------------------------------------------- generate_ideas
def test_generate_ideas_retorna_dict_com_chaves():
    r = cig.generate_ideas("tecnologia", 5)
    assert "nicho" in r
    assert "pilares" in r
    assert "total_ideias" in r
    assert "ideias" in r
    assert "ideias_por_pilar" in r
    assert "formatos_usados" in r


def test_generate_ideas_quantidade_correta():
    r = cig.generate_ideas("tecnologia", 7)
    assert r["total_ideias"] == 7
    assert len(r["ideias"]) == 7


def test_generate_ideas_nicho_invalido_cai_para_tecnologia():
    r = cig.generate_ideas("nicho_que_nao_existe", 3)
    assert r["nicho"] == "tecnologia"


def test_generate_ideas_estrutura_de_cada_ideia():
    r = cig.generate_ideas("financas", 5)
    for ideia in r["ideias"]:
        assert "idea" in ideia
        assert "pilar" in ideia
        assert "tema_principal" in ideia
        assert "formato" in ideia
        assert "prioridade" in ideia
        assert ideia["prioridade"] in ("alta", "média", "baixa")


def test_generate_ideas_organiza_por_pilar():
    r = cig.generate_ideas("marketing_digital", 10)
    # Soma das ideias por pilar = total
    soma = sum(len(v) for v in r["ideias_por_pilar"].values())
    assert soma == r["total_ideias"]


def test_generate_ideas_pilares_consistentes():
    r = cig.generate_ideas("empreendedorismo", 5)
    for pilar in r["ideias_por_pilar"]:
        assert pilar in r["pilares"]


def test_generate_ideas_quantidade_pequena():
    r = cig.generate_ideas("tecnologia", 1)
    assert len(r["ideias"]) == 1


def test_generate_ideas_quantidade_grande():
    r = cig.generate_ideas("desenvolvimento_pessoal", 50)
    assert len(r["ideias"]) == 50


# ----------------------------------------------------------- print_results
def test_print_results_imprime_titulo(capsys):
    r = cig.generate_ideas("tecnologia", 3)
    cig.print_results(r)
    out = capsys.readouterr().out
    assert "CONTENT IDEA GENERATOR" in out
    assert "TECNOLOGIA" in out


def test_print_results_lista_ideias(capsys):
    r = cig.generate_ideas("financas", 3)
    cig.print_results(r)
    out = capsys.readouterr().out
    for ideia in r["ideias"]:
        assert ideia["idea"] in out


def test_print_results_mostra_distribuicao_formato(capsys):
    r = cig.generate_ideas("tecnologia", 5)
    cig.print_results(r)
    out = capsys.readouterr().out
    assert "Distribuição por formato" in out


def test_print_results_mostra_proximos_passos(capsys):
    r = cig.generate_ideas("tecnologia", 2)
    cig.print_results(r)
    out = capsys.readouterr().out
    assert "PRÓXIMOS PASSOS" in out


# ----------------------------------------------------------- main / CLI
def test_main_sem_args_mostra_ajuda(capsys):
    with patch.object(sys, "argv", ["content_idea_generator.py"]):
        with pytest.raises(SystemExit) as exc:
            cig.main()
    assert exc.value.code == 1
    out = capsys.readouterr().out
    assert "Uso" in out or "uso" in out.lower()


def test_main_nicho_valido(capsys):
    with patch.object(sys, "argv", ["content_idea_generator.py", "tecnologia", "5"]):
        cig.main()
    out = capsys.readouterr().out
    assert "TECNOLOGIA" in out
    # Deve incluir bloco JSON ao final
    assert "JSON Output" in out


def test_main_quantidade_default_20(capsys):
    with patch.object(sys, "argv", ["content_idea_generator.py", "marketing_digital"]):
        cig.main()
    out = capsys.readouterr().out
    assert "Total de ideias: 20" in out


def test_main_nicho_invalido_avisa(capsys):
    with patch.object(sys, "argv", ["content_idea_generator.py", "nicho_inventado", "3"]):
        with pytest.raises(SystemExit) as exc:
            cig.main()
    assert exc.value.code == 1
    out = capsys.readouterr().out
    assert "não encontrado" in out


def test_main_quantidade_invalida_levanta_validacao(capsys):
    with patch.object(sys, "argv", ["content_idea_generator.py", "tecnologia", "abc"]):
        with pytest.raises(SystemExit):
            cig.main()
    err = capsys.readouterr().err
    # validar_inteiro deve gerar erro de validação no stderr
    assert "Erro" in err or "erro" in err.lower() or "válido" in err.lower() or "inválido" in err.lower()


def test_main_json_output_no_print(capsys):
    """Verifica que parte do output é JSON parseável."""
    with patch.object(sys, "argv", ["content_idea_generator.py", "tecnologia", "3"]):
        cig.main()
    out = capsys.readouterr().out
    # Achar o JSON no output
    json_start = out.find("{")
    json_end = out.rfind("}")
    assert json_start != -1 and json_end != -1
    parsed = json.loads(out[json_start:json_end + 1])
    assert parsed["nicho"] == "tecnologia"
