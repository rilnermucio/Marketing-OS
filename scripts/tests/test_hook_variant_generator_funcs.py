#!/usr/bin/env python3
"""
Testes funcionais para hook_variant_generator.py — cobre as funções de geração.
"""
from __future__ import annotations

import json
import os
import random
import sys
from unittest.mock import patch

import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

import hook_variant_generator as hvg


# ------------------------------------------------ preencher_variaveis
def test_preencher_variaveis_substitui_tema():
    formula = "O segredo de {tema} que ninguém conta"
    resultado = hvg.preencher_variaveis(formula, "produtividade", "geral")
    assert "produtividade" in resultado
    assert "{tema}" not in resultado


def test_preencher_variaveis_nicho_invalido_usa_geral():
    formula = "Os {coisas_tema} de {tema}"
    # nicho inexistente cai pro 'geral'
    resultado = hvg.preencher_variaveis(formula, "vendas", "nicho_inexistente")
    assert "{tema}" not in resultado
    assert "{coisas_tema}" not in resultado


def test_preencher_variaveis_substitui_genericas():
    formula = "Como passar de {antes} para {depois}"
    resultado = hvg.preencher_variaveis(formula, "X", "geral")
    assert "{antes}" not in resultado
    assert "{depois}" not in resultado


def test_preencher_variaveis_numero_eh_string():
    formula = "{numero} dicas matadoras"
    resultado = hvg.preencher_variaveis(formula, "vendas", "geral")
    # {numero} é substituído por string
    assert "{numero}" not in resultado


def test_preencher_variaveis_sem_placeholder_retorna_igual():
    formula = "Texto plano sem nenhum placeholder"
    resultado = hvg.preencher_variaveis(formula, "tema", "geral")
    assert resultado == formula


# ------------------------------------------------ adaptar_para_formato
def test_adaptar_para_formato_reels_respeita_limite():
    hook_longo = "x" * 200
    resultado = hvg.adaptar_para_formato(hook_longo, "reels")
    assert len(resultado) <= hvg.ADAPTACOES_FORMATO["reels"]["max_caracteres"]


def test_adaptar_para_formato_carrossel_respeita_limite():
    hook_longo = "y" * 200
    resultado = hvg.adaptar_para_formato(hook_longo, "carrossel")
    assert len(resultado) <= hvg.ADAPTACOES_FORMATO["carrossel"]["max_caracteres"]


def test_adaptar_para_formato_card_respeita_limite():
    hook_longo = "z" * 200
    resultado = hvg.adaptar_para_formato(hook_longo, "card")
    assert len(resultado) <= hvg.ADAPTACOES_FORMATO["card"]["max_caracteres"]


def test_adaptar_para_formato_invalido_usa_card_default():
    resultado = hvg.adaptar_para_formato("hook curto", "formato_inexistente")
    assert isinstance(resultado, str)
    assert len(resultado) > 0


def test_adaptar_para_formato_nao_quebra_string_curta():
    resultado = hvg.adaptar_para_formato("Curto", "card")
    assert "Curto" in resultado or len(resultado) > 0


# ------------------------------------------------ gerar_variantes
def test_gerar_variantes_quantidade_solicitada():
    variantes = hvg.gerar_variantes("marketing", quantidade=5, nicho="marketing")
    assert len(variantes) <= 5
    assert len(variantes) > 0


def test_gerar_variantes_estrutura_dos_dicts():
    variantes = hvg.gerar_variantes("vendas", quantidade=3, nicho="geral")
    for v in variantes:
        assert "hook" in v
        assert "categoria" in v
        assert "formato" in v
        assert "caracteres" in v
        assert isinstance(v["caracteres"], int)
        assert v["caracteres"] == len(v["hook"])


def test_gerar_variantes_filtro_de_categoria():
    categorias = ["curiosidade"]
    variantes = hvg.gerar_variantes("X", quantidade=5, categorias=categorias)
    for v in variantes:
        assert v["categoria"] == "curiosidade"


def test_gerar_variantes_categorias_none_usa_todas():
    variantes = hvg.gerar_variantes("X", quantidade=10, categorias=None)
    assert len(variantes) > 0


def test_gerar_variantes_nao_repete_formula():
    # Como o gerador evita formulas repetidas, garantir hooks distintos
    variantes = hvg.gerar_variantes("teste", quantidade=20, nicho="geral")
    hooks = [v["hook"] for v in variantes]
    # Não exigimos 100% único (substituições aleatórias podem coincidir),
    # mas a maioria deve diferir
    assert len(set(hooks)) >= len(hooks) // 2


# ------------------------------------------------ formatar_saida_*
def test_formatar_saida_tabela_contem_tema():
    variantes = hvg.gerar_variantes("Tema XPTO", quantidade=3)
    out = hvg.formatar_saida_tabela(variantes, "Tema XPTO")
    assert "Tema XPTO" in out
    assert "HOOK VARIANT GENERATOR" in out


def test_formatar_saida_tabela_lista_todas():
    variantes = hvg.gerar_variantes("X", quantidade=3)
    out = hvg.formatar_saida_tabela(variantes, "X")
    for v in variantes:
        assert v["hook"] in out


def test_formatar_saida_markdown_inclui_categorias():
    variantes = hvg.gerar_variantes("X", quantidade=3)
    out = hvg.formatar_saida_markdown(variantes, "X")
    assert "# Variantes de Hook" in out
    assert "X" in out


def test_formatar_saida_json_eh_valido():
    variantes = hvg.gerar_variantes("X", quantidade=3)
    out = hvg.formatar_saida_json(variantes, "X")
    parsed = json.loads(out)
    assert parsed["tema"] == "X"
    assert parsed["total_variantes"] == len(variantes)
    assert parsed["variantes"] == variantes


def test_formatar_saida_json_tem_timestamp():
    out = hvg.formatar_saida_json([], "tema")
    parsed = json.loads(out)
    assert "gerado_em" in parsed


# ------------------------------------------------ main / CLI
def test_main_sem_args_mostra_ajuda(capsys):
    with patch.object(sys, "argv", ["hook_variant_generator.py"]):
        hvg.main()
    out = capsys.readouterr().out
    assert "HOOK VARIANT GENERATOR" in out
    assert "USO:" in out


def test_main_help_mostra_ajuda(capsys):
    with patch.object(sys, "argv", ["hook_variant_generator.py", "--help"]):
        hvg.main()
    out = capsys.readouterr().out
    assert "HOOK VARIANT GENERATOR" in out


def test_main_tema_apenas_gera_tabela(capsys):
    with patch.object(sys, "argv", ["hook_variant_generator.py", "vendas"]):
        hvg.main()
    out = capsys.readouterr().out
    assert "vendas" in out
    assert "HOOK VARIANT GENERATOR" in out


def test_main_output_json(capsys):
    with patch.object(sys, "argv", ["hook_variant_generator.py", "tema", "--output", "json", "--quantidade", "3"]):
        hvg.main()
    out = capsys.readouterr().out
    parsed = json.loads(out)
    assert parsed["tema"] == "tema"
    assert parsed["total_variantes"] <= 3


def test_main_output_markdown(capsys):
    with patch.object(sys, "argv", ["hook_variant_generator.py", "tema", "--output", "markdown"]):
        hvg.main()
    out = capsys.readouterr().out
    assert "# Variantes de Hook" in out


def test_main_nicho_invalido_usa_geral(capsys):
    with patch.object(sys, "argv", ["hook_variant_generator.py", "X", "--nicho", "inexistente"]):
        hvg.main()
    out = capsys.readouterr().out
    assert "não encontrado" in out


def test_main_formato_invalido_usa_card(capsys):
    with patch.object(sys, "argv", ["hook_variant_generator.py", "X", "--formato", "invalido"]):
        hvg.main()
    out = capsys.readouterr().out
    assert "não encontrado" in out


def test_main_categoria_invalida_avisa(capsys):
    with patch.object(sys, "argv", ["hook_variant_generator.py", "X", "--categoria", "fake_cat"]):
        hvg.main()
    out = capsys.readouterr().out
    assert "não encontrada" in out


def test_main_categoria_valida_filtra(capsys):
    with patch.object(sys, "argv", ["hook_variant_generator.py", "X", "--categoria", "curiosidade", "--output", "json"]):
        hvg.main()
    out = capsys.readouterr().out
    parsed = json.loads(out)
    for v in parsed["variantes"]:
        assert v["categoria"] == "curiosidade"


def test_main_args_ignora_desconhecidos(capsys):
    with patch.object(sys, "argv", ["hook_variant_generator.py", "tema", "--unknown", "valor"]):
        hvg.main()
    out = capsys.readouterr().out
    assert "tema" in out


def test_main_sem_tema_avisa(capsys):
    with patch.object(sys, "argv", ["hook_variant_generator.py", "--quantidade", "5"]):
        hvg.main()
    out = capsys.readouterr().out
    assert "tema" in out.lower()
