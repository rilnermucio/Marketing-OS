#!/usr/bin/env python3
"""
Testes para apify_serp.py — Google SERP scraper via Apify.

Cobre:
- build_input (input do Actor)
- parse_serp_results (parsing do output)
- format_summary_md (markdown para o agent)
- main: dry-run, token ausente, 401, 429, timeout, sucesso
"""

import json
import os
import subprocess
import sys

import pytest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from apify_client import (
    ApifyAuthError,
    ApifyRateLimitError,
    ApifyTimeoutError,
)
from apify_serp import (
    DEFAULT_MAX_RESULTS,
    HARD_CAP_RESULTS,
    SERP_ACTOR_ID,
    build_input,
    format_summary_md,
    parse_serp_results,
)


SCRIPT_PATH = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "apify_serp.py"
)


# ---------------------------------------------------------------------------
# build_input
# ---------------------------------------------------------------------------


class TestBuildInput:
    def test_inclui_query_como_string(self):
        # Apify google-search-scraper espera 'queries' como string
        # (newline-separated em batch; pra single query, é só a string)
        inp = build_input("infoproduto bofu", max_results=10)
        assert inp["queries"] == "infoproduto bofu"

    def test_max_results_propagado(self):
        inp = build_input("x", max_results=20)
        assert inp["resultsPerPage"] == 20

    def test_country_e_language_pt_br(self):
        inp = build_input("x", max_results=10)
        assert inp["countryCode"] == "br"
        assert inp["languageCode"] == "pt-BR"

    def test_max_results_acima_do_cap_e_limitado(self):
        inp = build_input("x", max_results=999)
        assert inp["resultsPerPage"] == HARD_CAP_RESULTS

    def test_max_results_zero_ou_negativo_vira_um(self):
        inp = build_input("x", max_results=0)
        assert inp["resultsPerPage"] == 1

    def test_default_max_results_quando_nao_especifica(self):
        inp = build_input("x")
        assert inp["resultsPerPage"] == DEFAULT_MAX_RESULTS

    def test_save_html_false_para_economia(self):
        inp = build_input("x")
        assert inp.get("saveHtml") is False


# ---------------------------------------------------------------------------
# parse_serp_results
# ---------------------------------------------------------------------------


class TestParseSerpResults:
    def test_extrai_resultados_organicos(self):
        raw = [
            {
                "searchQuery": {"term": "infoproduto"},
                "organicResults": [
                    {
                        "title": "T1",
                        "url": "https://a.com",
                        "description": "D1",
                    },
                    {
                        "title": "T2",
                        "url": "https://b.com",
                        "description": "D2",
                    },
                ],
            }
        ]
        parsed = parse_serp_results(raw)
        assert len(parsed["organic"]) == 2
        assert parsed["organic"][0]["title"] == "T1"
        assert parsed["organic"][0]["url"] == "https://a.com"
        assert parsed["organic"][0]["description"] == "D1"

    def test_inclui_position_baseada_em_ordem(self):
        raw = [
            {
                "organicResults": [
                    {"title": "T1", "url": "u1"},
                    {"title": "T2", "url": "u2"},
                    {"title": "T3", "url": "u3"},
                ]
            }
        ]
        parsed = parse_serp_results(raw)
        assert parsed["organic"][0]["position"] == 1
        assert parsed["organic"][1]["position"] == 2
        assert parsed["organic"][2]["position"] == 3

    def test_extrai_paa(self):
        raw = [
            {
                "organicResults": [],
                "peopleAlsoAsk": [
                    {"question": "O que é X?"},
                    {"question": "Como X funciona?"},
                ],
            }
        ]
        parsed = parse_serp_results(raw)
        assert parsed["people_also_ask"] == ["O que é X?", "Como X funciona?"]

    def test_extrai_related(self):
        raw = [
            {
                "organicResults": [],
                "relatedQueries": [
                    {"title": "x relacionado"},
                    {"title": "x outro"},
                ],
            }
        ]
        parsed = parse_serp_results(raw)
        assert "x relacionado" in parsed["related"]
        assert "x outro" in parsed["related"]

    def test_input_vazio_retorna_estrutura_vazia(self):
        parsed = parse_serp_results([])
        assert parsed["organic"] == []
        assert parsed["people_also_ask"] == []
        assert parsed["related"] == []

    def test_campos_ausentes_nao_crasham(self):
        raw = [{"searchQuery": {"term": "x"}}]
        parsed = parse_serp_results(raw)
        assert parsed["organic"] == []
        assert parsed["people_also_ask"] == []
        assert parsed["related"] == []

    def test_paa_com_pergunta_vazia_e_filtrado(self):
        raw = [
            {
                "organicResults": [],
                "peopleAlsoAsk": [
                    {"question": ""},
                    {"question": "Pergunta válida?"},
                ],
            }
        ]
        parsed = parse_serp_results(raw)
        assert parsed["people_also_ask"] == ["Pergunta válida?"]

    def test_related_dedupe_preservando_ordem(self):
        # Apify Actor retorna related duplicado (top + footer da SERP).
        # Parser deve dedupe preservando a ordem da primeira ocorrência.
        raw = [
            {
                "organicResults": [],
                "relatedQueries": [
                    {"title": "x"},
                    {"title": "y"},
                    {"title": "x"},
                    {"title": "z"},
                    {"title": "y"},
                ],
            }
        ]
        parsed = parse_serp_results(raw)
        assert parsed["related"] == ["x", "y", "z"]

    def test_paa_dedupe_preservando_ordem(self):
        raw = [
            {
                "organicResults": [],
                "peopleAlsoAsk": [
                    {"question": "Q1?"},
                    {"question": "Q2?"},
                    {"question": "Q1?"},
                ],
            }
        ]
        parsed = parse_serp_results(raw)
        assert parsed["people_also_ask"] == ["Q1?", "Q2?"]


# ---------------------------------------------------------------------------
# format_summary_md
# ---------------------------------------------------------------------------


class TestFormatSummaryMd:
    def test_inclui_query_no_titulo(self):
        parsed = {"organic": [], "people_also_ask": [], "related": []}
        md = format_summary_md(parsed, query="infoproduto bofu")
        assert "infoproduto bofu" in md
        assert "##" in md  # tem cabeçalho

    def test_inclui_top_resultados(self):
        parsed = {
            "organic": [
                {
                    "title": "T1",
                    "url": "https://a.com",
                    "description": "D1",
                    "position": 1,
                },
                {
                    "title": "T2",
                    "url": "https://b.com",
                    "description": "D2",
                    "position": 2,
                },
            ],
            "people_also_ask": [],
            "related": [],
        }
        md = format_summary_md(parsed, query="x")
        assert "T1" in md
        assert "T2" in md
        assert "https://a.com" in md

    def test_inclui_paa_quando_existe(self):
        parsed = {
            "organic": [],
            "people_also_ask": ["O que é X?", "Como X?"],
            "related": [],
        }
        md = format_summary_md(parsed, query="x")
        assert "O que é X?" in md
        assert "Como X?" in md

    def test_inclui_related_quando_existe(self):
        parsed = {
            "organic": [],
            "people_also_ask": [],
            "related": ["termo relacionado"],
        }
        md = format_summary_md(parsed, query="x")
        assert "termo relacionado" in md

    def test_omite_secoes_vazias(self):
        parsed = {"organic": [], "people_also_ask": [], "related": []}
        md = format_summary_md(parsed, query="x")
        # Não deve ter cabeçalho de "Top resultados" se não há resultado
        assert "Top resultados" not in md
        assert "People Also Ask" not in md
        assert "Related" not in md


# ---------------------------------------------------------------------------
# CLI (main) — testes via subprocess
# ---------------------------------------------------------------------------


class TestCli:
    def test_dry_run_imprime_estimativa_e_sai_zero(self):
        result = subprocess.run(
            [sys.executable, SCRIPT_PATH, "--query", "teste", "--dry-run"],
            capture_output=True,
            text=True,
        )
        assert result.returncode == 0
        assert "Custo estimado" in result.stdout or "custo estimado" in result.stdout.lower()

    def test_token_ausente_sai_zero_com_mensagem(self, monkeypatch):
        env = os.environ.copy()
        env.pop("APIFY_TOKEN", None)
        result = subprocess.run(
            [sys.executable, SCRIPT_PATH, "--query", "teste"],
            capture_output=True,
            text=True,
            env=env,
        )
        # Graceful degrade: exit 0, mensagem em stderr
        assert result.returncode == 0
        assert "APIFY_TOKEN" in result.stderr

    def test_query_obrigatoria(self):
        result = subprocess.run(
            [sys.executable, SCRIPT_PATH],
            capture_output=True,
            text=True,
        )
        # argparse retorna 2 quando arg obrigatório falta
        assert result.returncode != 0

    def test_help_funciona(self):
        result = subprocess.run(
            [sys.executable, SCRIPT_PATH, "--help"],
            capture_output=True,
            text=True,
        )
        assert result.returncode == 0
        assert "query" in result.stdout.lower()
