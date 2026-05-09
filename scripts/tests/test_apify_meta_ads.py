#!/usr/bin/env python3
"""
Testes para apify_meta_ads.py — Meta Ad Library scraper via Apify.

Cobre:
- build_search_url (constrói URL da Ad Library a partir de query + país)
- build_input (input do Actor)
- parse_meta_ads_results (parsing do output)
- format_summary_md (markdown para o agent)
- main: dry-run, token ausente, query obrigatória, help
"""

import os
import subprocess
import sys

import pytest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from apify_meta_ads import (
    DEFAULT_COUNTRY,
    DEFAULT_MAX_ADS,
    HARD_CAP_ADS,
    META_ADS_ACTOR_ID,
    MIN_ADS,
    build_input,
    build_search_url,
    format_summary_md,
    parse_meta_ads_results,
)


SCRIPT_PATH = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    "apify_meta_ads.py",
)


# ---------------------------------------------------------------------------
# build_search_url
# ---------------------------------------------------------------------------


class TestBuildSearchUrl:
    def test_inclui_query_url_encoded(self):
        url = build_search_url("hotmart", country="BR")
        assert "facebook.com/ads/library" in url
        assert "hotmart" in url
        assert "country=BR" in url

    def test_query_com_espaco_e_encoded(self):
        url = build_search_url("infoproduto digital", country="BR")
        # %20 ou + para espaço
        assert "infoproduto" in url
        assert ("%20" in url) or ("+" in url)

    def test_country_default_e_br(self):
        url = build_search_url("x")
        assert "country=BR" in url

    def test_active_status_all_e_ad_type_all(self):
        url = build_search_url("x", country="BR")
        # Pra varrer tudo, não só ativos
        assert "active_status=all" in url
        assert "ad_type=all" in url


# ---------------------------------------------------------------------------
# build_input
# ---------------------------------------------------------------------------


class TestBuildInput:
    def test_inclui_url_construida_da_query(self):
        inp = build_input("hotmart", max_ads=30, country="BR")
        assert "urls" in inp
        assert isinstance(inp["urls"], list)
        assert "facebook.com/ads/library" in inp["urls"][0]["url"]

    def test_max_ads_acima_do_cap_e_limitado(self):
        inp = build_input("x", max_ads=999)
        assert inp["count"] == HARD_CAP_ADS

    def test_max_ads_zero_ou_negativo_vira_min(self):
        # Actor exige count >= MIN_ADS pra rodar; valores menores são elevados
        inp = build_input("x", max_ads=0)
        assert inp["count"] == MIN_ADS

    def test_max_ads_abaixo_do_min_e_elevado(self):
        inp = build_input("x", max_ads=5)
        assert inp["count"] == MIN_ADS

    def test_max_ads_acima_do_min_e_preservado(self):
        inp = build_input("x", max_ads=25)
        assert inp["count"] == 25

    def test_default_max_ads(self):
        inp = build_input("x")
        assert inp["count"] == DEFAULT_MAX_ADS

    def test_country_propagado_pra_url(self):
        inp = build_input("x", country="US")
        assert "country=US" in inp["urls"][0]["url"]


# ---------------------------------------------------------------------------
# parse_meta_ads_results
# ---------------------------------------------------------------------------


class TestParseMetaAdsResults:
    def test_extrai_anuncios_formato_legacy(self):
        # Formato apify/facebook-ads-scraper (legacy, sem snapshot)
        raw = [
            {
                "ad_archive_id": "ad1",
                "page_name": "Hotmart",
                "page_id": "12345",
                "ad_creative_bodies": ["Compre agora"],
                "ad_creative_link_titles": ["Hotmart Curso"],
                "ad_snapshot_url": "https://fb.com/snapshot/ad1",
                "publisher_platforms": ["facebook", "instagram"],
                "start_date": "2026-01-01",
                "end_date": None,
            },
        ]
        parsed = parse_meta_ads_results(raw)
        assert len(parsed["ads"]) == 1
        assert parsed["ads"][0]["id"] == "ad1"
        assert parsed["ads"][0]["page_name"] == "Hotmart"
        assert "Compre agora" in parsed["ads"][0]["body"]

    def test_extrai_anuncios_formato_curious_coder_com_snapshot(self):
        # Formato curious_coder/facebook-ads-library-scraper (default atual)
        raw = [
            {
                "ad_archive_id": "ad1",
                "page_name": "Hotmart",
                "page_id": "12345",
                "publisher_platform": ["FACEBOOK", "INSTAGRAM"],
                "is_active": True,
                "start_date_formatted": "2026-01-01",
                "end_date_formatted": None,
                "ad_library_url": "https://fb.com/lib/ad1",
                "snapshot": {
                    "body": {"text": "Aprenda copy de vendas"},
                    "title": "Curso Master",
                    "caption": "hotm.art",
                    "cta_text": "Saiba mais",
                    "cta_type": "LEARN_MORE",
                    "link_url": "https://hotm.art/abc",
                },
            },
        ]
        parsed = parse_meta_ads_results(raw)
        ad = parsed["ads"][0]
        assert ad["id"] == "ad1"
        assert ad["page_name"] == "Hotmart"
        assert ad["body"] == "Aprenda copy de vendas"
        assert ad["title"] == "Curso Master"
        assert ad["caption"] == "hotm.art"
        assert ad["cta_text"] == "Saiba mais"
        assert ad["link_url"] == "https://hotm.art/abc"
        assert "FACEBOOK" in ad["platforms"]

    def test_body_com_placeholder_dinamico_preserva(self):
        # Ads com creative dinâmico vêm com placeholder {{product.brand}}
        raw = [
            {
                "ad_archive_id": "ad1",
                "page_name": "Hotmart",
                "snapshot": {"body": {"text": "{{product.brand}}"}},
            }
        ]
        parsed = parse_meta_ads_results(raw)
        assert parsed["ads"][0]["body"] == "{{product.brand}}"

    def test_calcula_metricas_agregadas(self):
        raw = [
            {"ad_archive_id": "1", "page_name": "A", "publisher_platforms": ["facebook"]},
            {"ad_archive_id": "2", "page_name": "A", "publisher_platforms": ["instagram"]},
            {"ad_archive_id": "3", "page_name": "B", "publisher_platforms": ["facebook", "instagram"]},
        ]
        parsed = parse_meta_ads_results(raw)
        assert parsed["metrics"]["total_ads"] == 3
        # 2 unique pages
        assert parsed["metrics"]["unique_pages"] == 2

    def test_top_pages_agregadas(self):
        raw = [
            {"ad_archive_id": "1", "page_name": "Hotmart"},
            {"ad_archive_id": "2", "page_name": "Hotmart"},
            {"ad_archive_id": "3", "page_name": "Kiwify"},
            {"ad_archive_id": "4", "page_name": "Hotmart"},
        ]
        parsed = parse_meta_ads_results(raw)
        top = parsed["top_pages"]
        assert top[0][0] == "Hotmart"
        assert top[0][1] == 3

    def test_input_vazio(self):
        parsed = parse_meta_ads_results([])
        assert parsed["ads"] == []
        assert parsed["metrics"]["total_ads"] == 0

    def test_campos_ausentes_nao_crasham(self):
        raw = [{"ad_archive_id": "x"}]
        parsed = parse_meta_ads_results(raw)
        assert len(parsed["ads"]) == 1
        assert parsed["ads"][0]["page_name"] == ""


# ---------------------------------------------------------------------------
# format_summary_md
# ---------------------------------------------------------------------------


class TestFormatSummaryMd:
    def test_inclui_query_no_titulo(self):
        parsed = {
            "ads": [],
            "metrics": {"total_ads": 0, "unique_pages": 0},
            "top_pages": [],
        }
        md = format_summary_md(parsed, query="hotmart")
        assert "hotmart" in md

    def test_inclui_metricas(self):
        parsed = {
            "ads": [],
            "metrics": {"total_ads": 30, "unique_pages": 5},
            "top_pages": [],
        }
        md = format_summary_md(parsed, query="x")
        assert "30" in md
        assert "5" in md

    def test_inclui_top_pages(self):
        parsed = {
            "ads": [],
            "metrics": {"total_ads": 10, "unique_pages": 2},
            "top_pages": [("Hotmart", 7), ("Kiwify", 3)],
        }
        md = format_summary_md(parsed, query="x")
        assert "Hotmart" in md
        assert "Kiwify" in md

    def test_inclui_amostra_de_ads(self):
        parsed = {
            "ads": [
                {
                    "id": "1",
                    "page_name": "Hotmart",
                    "body": "Copy do anúncio aqui",
                    "title": "Curso Vendas",
                    "platforms": ["facebook", "instagram"],
                    "snapshot_url": "https://fb.com/x",
                    "start_date": "2026-01-01",
                    "end_date": None,
                }
            ],
            "metrics": {"total_ads": 1, "unique_pages": 1},
            "top_pages": [("Hotmart", 1)],
        }
        md = format_summary_md(parsed, query="x")
        assert "Copy do anúncio aqui" in md or "Curso Vendas" in md


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------


class TestCli:
    def test_dry_run_imprime_estimativa_e_sai_zero(self):
        result = subprocess.run(
            [sys.executable, SCRIPT_PATH, "--query", "hotmart", "--dry-run"],
            capture_output=True,
            text=True,
        )
        assert result.returncode == 0
        assert "custo" in result.stdout.lower() or "Custo" in result.stdout

    def test_token_ausente_sai_zero_com_mensagem(self):
        env = os.environ.copy()
        env.pop("APIFY_TOKEN", None)
        result = subprocess.run(
            [sys.executable, SCRIPT_PATH, "--query", "x"],
            capture_output=True,
            text=True,
            env=env,
        )
        assert result.returncode == 0
        assert "APIFY_TOKEN" in result.stderr

    def test_query_obrigatoria(self):
        result = subprocess.run(
            [sys.executable, SCRIPT_PATH],
            capture_output=True,
            text=True,
        )
        assert result.returncode != 0

    def test_help_funciona(self):
        result = subprocess.run(
            [sys.executable, SCRIPT_PATH, "--help"],
            capture_output=True,
            text=True,
        )
        assert result.returncode == 0
        assert "query" in result.stdout.lower()
