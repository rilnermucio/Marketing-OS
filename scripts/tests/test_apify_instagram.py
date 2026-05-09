#!/usr/bin/env python3
"""
Testes para apify_instagram.py — Instagram profile scraper via Apify.

Cobre:
- normalize_handle (aceita @handle, handle, URL completa)
- build_input (input do Actor)
- parse_instagram_results (parsing de posts e perfil)
- format_summary_md (markdown para o agent)
- main: dry-run, token ausente, help, handle obrigatório
"""

import os
import subprocess
import sys

import pytest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from apify_instagram import (
    DEFAULT_MAX_POSTS,
    HARD_CAP_POSTS,
    INSTAGRAM_ACTOR_ID,
    build_input,
    format_summary_md,
    normalize_handle,
    parse_instagram_results,
)


SCRIPT_PATH = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    "apify_instagram.py",
)


# ---------------------------------------------------------------------------
# normalize_handle
# ---------------------------------------------------------------------------


class TestNormalizeHandle:
    def test_handle_simples(self):
        assert normalize_handle("conrado") == "conrado"

    def test_handle_com_arroba(self):
        assert normalize_handle("@conrado") == "conrado"

    def test_url_completa_https(self):
        assert normalize_handle("https://www.instagram.com/conrado/") == "conrado"

    def test_url_sem_www(self):
        assert normalize_handle("https://instagram.com/conrado/") == "conrado"

    def test_url_sem_trailing_slash(self):
        assert normalize_handle("https://www.instagram.com/conrado") == "conrado"

    def test_remove_query_string(self):
        assert normalize_handle("https://instagram.com/conrado/?hl=pt-br") == "conrado"

    def test_strip_espacos(self):
        assert normalize_handle("  @conrado  ") == "conrado"

    def test_handle_com_underscore_e_ponto(self):
        # Instagram permite . e _ em handles
        assert normalize_handle("@user.name_123") == "user.name_123"


# ---------------------------------------------------------------------------
# build_input
# ---------------------------------------------------------------------------


class TestBuildInput:
    def test_constroi_url_a_partir_do_handle(self):
        inp = build_input("conrado", max_posts=30)
        assert inp["directUrls"] == ["https://www.instagram.com/conrado/"]

    def test_max_posts_propagado(self):
        inp = build_input("x", max_posts=50)
        assert inp["resultsLimit"] == 50

    def test_max_posts_acima_do_cap_e_limitado(self):
        inp = build_input("x", max_posts=999)
        assert inp["resultsLimit"] == HARD_CAP_POSTS

    def test_max_posts_zero_ou_negativo_vira_um(self):
        inp = build_input("x", max_posts=0)
        assert inp["resultsLimit"] == 1

    def test_default_max_posts(self):
        inp = build_input("x")
        assert inp["resultsLimit"] == DEFAULT_MAX_POSTS

    def test_results_type_posts(self):
        inp = build_input("x")
        assert inp["resultsType"] == "posts"

    def test_aceita_handle_com_arroba(self):
        inp = build_input("@conrado", max_posts=10)
        assert inp["directUrls"] == ["https://www.instagram.com/conrado/"]


# ---------------------------------------------------------------------------
# parse_instagram_results
# ---------------------------------------------------------------------------


class TestParseInstagramResults:
    def test_extrai_posts(self):
        raw = [
            {
                "id": "post1",
                "type": "Image",
                "caption": "Legenda 1",
                "likesCount": 100,
                "commentsCount": 10,
                "timestamp": "2026-01-01T00:00:00Z",
                "hashtags": ["a", "b"],
                "ownerUsername": "conrado",
                "ownerFullName": "Conrado Adolpho",
                "url": "https://instagram.com/p/post1",
            },
            {
                "id": "post2",
                "type": "Video",
                "caption": "Legenda 2",
                "likesCount": 200,
                "commentsCount": 20,
                "timestamp": "2026-01-02T00:00:00Z",
                "hashtags": [],
                "ownerUsername": "conrado",
                "url": "https://instagram.com/p/post2",
                "videoViewCount": 5000,
            },
        ]
        parsed = parse_instagram_results(raw)
        assert len(parsed["posts"]) == 2
        assert parsed["posts"][0]["id"] == "post1"
        assert parsed["posts"][0]["likes"] == 100
        assert parsed["posts"][0]["comments"] == 10
        assert parsed["posts"][1]["video_views"] == 5000

    def test_extrai_perfil_do_owner(self):
        raw = [
            {
                "id": "p1",
                "ownerUsername": "conrado",
                "ownerFullName": "Conrado Adolpho",
                "likesCount": 50,
                "commentsCount": 5,
            }
        ]
        parsed = parse_instagram_results(raw)
        assert parsed["profile"]["handle"] == "conrado"
        assert parsed["profile"]["full_name"] == "Conrado Adolpho"

    def test_calcula_metricas_agregadas(self):
        raw = [
            {"id": "p1", "likesCount": 100, "commentsCount": 10},
            {"id": "p2", "likesCount": 200, "commentsCount": 20},
            {"id": "p3", "likesCount": 300, "commentsCount": 30},
        ]
        parsed = parse_instagram_results(raw)
        # Soma de likes = 600, soma de comments = 60
        assert parsed["metrics"]["total_posts"] == 3
        assert parsed["metrics"]["avg_likes"] == 200
        assert parsed["metrics"]["avg_comments"] == 20

    def test_input_vazio_retorna_estrutura_vazia(self):
        parsed = parse_instagram_results([])
        assert parsed["posts"] == []
        assert parsed["profile"] == {}
        assert parsed["metrics"]["total_posts"] == 0

    def test_top_hashtags_agregadas(self):
        raw = [
            {"id": "p1", "hashtags": ["marketing", "vendas"]},
            {"id": "p2", "hashtags": ["marketing", "growth"]},
            {"id": "p3", "hashtags": ["marketing", "vendas"]},
        ]
        parsed = parse_instagram_results(raw)
        # marketing = 3, vendas = 2, growth = 1
        top = parsed["top_hashtags"]
        assert top[0][0] == "marketing"
        assert top[0][1] == 3

    def test_campos_ausentes_nao_crasham(self):
        raw = [{"id": "p1"}]  # só id, sem likes/comments/etc
        parsed = parse_instagram_results(raw)
        assert len(parsed["posts"]) == 1
        assert parsed["posts"][0]["likes"] == 0
        assert parsed["posts"][0]["comments"] == 0


# ---------------------------------------------------------------------------
# format_summary_md
# ---------------------------------------------------------------------------


class TestFormatSummaryMd:
    def test_inclui_handle_no_titulo(self):
        parsed = {
            "profile": {"handle": "conrado", "full_name": "Conrado Adolpho"},
            "posts": [],
            "metrics": {"total_posts": 0, "avg_likes": 0, "avg_comments": 0},
            "top_hashtags": [],
        }
        md = format_summary_md(parsed, handle="conrado")
        assert "conrado" in md

    def test_inclui_metricas_agregadas(self):
        parsed = {
            "profile": {"handle": "x"},
            "posts": [],
            "metrics": {"total_posts": 30, "avg_likes": 150, "avg_comments": 12},
            "top_hashtags": [],
        }
        md = format_summary_md(parsed, handle="x")
        assert "30" in md  # total posts
        assert "150" in md  # avg likes

    def test_inclui_top_posts(self):
        parsed = {
            "profile": {"handle": "x"},
            "posts": [
                {
                    "id": "p1",
                    "caption": "Post viral",
                    "likes": 10000,
                    "comments": 500,
                    "url": "https://instagram.com/p/p1",
                    "type": "Video",
                    "video_views": 100000,
                }
            ],
            "metrics": {"total_posts": 1, "avg_likes": 10000, "avg_comments": 500},
            "top_hashtags": [],
        }
        md = format_summary_md(parsed, handle="x")
        assert "Post viral" in md or "10000" in md or "10,000" in md

    def test_inclui_top_hashtags(self):
        parsed = {
            "profile": {"handle": "x"},
            "posts": [],
            "metrics": {"total_posts": 0, "avg_likes": 0, "avg_comments": 0},
            "top_hashtags": [("marketing", 5), ("vendas", 3)],
        }
        md = format_summary_md(parsed, handle="x")
        assert "marketing" in md
        assert "vendas" in md


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------


class TestCli:
    def test_dry_run_imprime_estimativa_e_sai_zero(self):
        result = subprocess.run(
            [sys.executable, SCRIPT_PATH, "--handle", "@x", "--dry-run"],
            capture_output=True,
            text=True,
        )
        assert result.returncode == 0
        assert "Custo estimado" in result.stdout or "custo" in result.stdout.lower()

    def test_token_ausente_sai_zero_com_mensagem(self):
        env = os.environ.copy()
        env.pop("APIFY_TOKEN", None)
        result = subprocess.run(
            [sys.executable, SCRIPT_PATH, "--handle", "@x"],
            capture_output=True,
            text=True,
            env=env,
        )
        assert result.returncode == 0
        assert "APIFY_TOKEN" in result.stderr

    def test_handle_obrigatorio(self):
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
        assert "handle" in result.stdout.lower()
