#!/usr/bin/env python3
"""
Testes para apify_tiktok.py — TikTok profile scraper via Apify.
"""

import os
import subprocess
import sys

import pytest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from apify_tiktok import (
    DEFAULT_MAX_VIDEOS,
    HARD_CAP_VIDEOS,
    TIKTOK_ACTOR_ID,
    build_input,
    format_summary_md,
    normalize_handle,
    parse_tiktok_results,
)


SCRIPT_PATH = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    "apify_tiktok.py",
)


# ---------------------------------------------------------------------------
# normalize_handle
# ---------------------------------------------------------------------------


class TestNormalizeHandle:
    def test_handle_simples(self):
        assert normalize_handle("usuario") == "usuario"

    def test_handle_com_arroba(self):
        assert normalize_handle("@usuario") == "usuario"

    def test_url_completa(self):
        assert normalize_handle("https://www.tiktok.com/@usuario") == "usuario"

    def test_url_sem_www(self):
        assert normalize_handle("https://tiktok.com/@usuario") == "usuario"

    def test_url_com_query_string(self):
        assert normalize_handle("https://tiktok.com/@usuario?lang=pt") == "usuario"

    def test_strip_espacos(self):
        assert normalize_handle("  @usuario  ") == "usuario"


# ---------------------------------------------------------------------------
# build_input
# ---------------------------------------------------------------------------


class TestBuildInput:
    def test_inclui_handle_no_profiles(self):
        inp = build_input("usuario", max_videos=30)
        # Actor aceita usernames OU URLs em "profiles"
        assert "profiles" in inp
        assert isinstance(inp["profiles"], list)
        assert "usuario" in inp["profiles"][0] or "tiktok.com" in inp["profiles"][0]

    def test_max_videos_propagado(self):
        inp = build_input("x", max_videos=50)
        assert inp["resultsPerPage"] == 50

    def test_max_videos_acima_do_cap_e_limitado(self):
        inp = build_input("x", max_videos=999)
        assert inp["resultsPerPage"] == HARD_CAP_VIDEOS

    def test_max_videos_zero_ou_negativo_vira_um(self):
        inp = build_input("x", max_videos=0)
        assert inp["resultsPerPage"] == 1

    def test_default_max_videos(self):
        inp = build_input("x")
        assert inp["resultsPerPage"] == DEFAULT_MAX_VIDEOS

    def test_should_download_videos_false(self):
        # Economia de banda; só queremos metadados
        inp = build_input("x")
        assert inp.get("shouldDownloadVideos") is False


# ---------------------------------------------------------------------------
# parse_tiktok_results
# ---------------------------------------------------------------------------


class TestParseTiktokResults:
    def test_extrai_videos(self):
        raw = [
            {
                "id": "v1",
                "text": "Legenda do video",
                "createTime": 1735689600,
                "playCount": 100000,
                "diggCount": 5000,
                "commentCount": 200,
                "shareCount": 100,
                "videoUrl": "https://tiktok.com/v/v1",
                "webVideoUrl": "https://www.tiktok.com/@u/video/v1",
                "authorMeta": {"name": "usuario", "nickName": "Nome do usuario"},
                "hashtags": [{"name": "marketing"}, {"name": "vendas"}],
            }
        ]
        parsed = parse_tiktok_results(raw)
        assert len(parsed["videos"]) == 1
        v = parsed["videos"][0]
        assert v["id"] == "v1"
        assert v["plays"] == 100000
        assert v["likes"] == 5000

    def test_extrai_perfil(self):
        raw = [
            {
                "id": "v1",
                "authorMeta": {"name": "usuario", "nickName": "Nome User"},
            }
        ]
        parsed = parse_tiktok_results(raw)
        assert parsed["profile"]["handle"] == "usuario"
        assert parsed["profile"]["nickname"] == "Nome User"

    def test_calcula_metricas_agregadas(self):
        raw = [
            {"id": "1", "playCount": 1000, "diggCount": 100, "commentCount": 10},
            {"id": "2", "playCount": 2000, "diggCount": 200, "commentCount": 20},
        ]
        parsed = parse_tiktok_results(raw)
        assert parsed["metrics"]["total_videos"] == 2
        assert parsed["metrics"]["avg_plays"] == 1500
        assert parsed["metrics"]["avg_likes"] == 150

    def test_top_hashtags_agregadas(self):
        raw = [
            {"id": "1", "hashtags": [{"name": "x"}, {"name": "y"}]},
            {"id": "2", "hashtags": [{"name": "x"}, {"name": "z"}]},
            {"id": "3", "hashtags": [{"name": "x"}]},
        ]
        parsed = parse_tiktok_results(raw)
        top = parsed["top_hashtags"]
        assert top[0][0] == "x"
        assert top[0][1] == 3

    def test_input_vazio(self):
        parsed = parse_tiktok_results([])
        assert parsed["videos"] == []
        assert parsed["profile"] == {}
        assert parsed["metrics"]["total_videos"] == 0

    def test_campos_ausentes_nao_crasham(self):
        raw = [{"id": "x"}]
        parsed = parse_tiktok_results(raw)
        assert len(parsed["videos"]) == 1
        assert parsed["videos"][0]["plays"] == 0


# ---------------------------------------------------------------------------
# format_summary_md
# ---------------------------------------------------------------------------


class TestFormatSummaryMd:
    def test_inclui_handle_no_titulo(self):
        parsed = {
            "videos": [],
            "profile": {"handle": "usuario", "nickname": "Nome"},
            "metrics": {"total_videos": 0, "avg_plays": 0, "avg_likes": 0, "avg_comments": 0},
            "top_hashtags": [],
        }
        md = format_summary_md(parsed, handle="usuario")
        assert "usuario" in md

    def test_inclui_metricas(self):
        parsed = {
            "videos": [],
            "profile": {"handle": "x"},
            "metrics": {"total_videos": 30, "avg_plays": 50000, "avg_likes": 5000, "avg_comments": 100},
            "top_hashtags": [],
        }
        md = format_summary_md(parsed, handle="x")
        assert "30" in md
        assert "50,000" in md or "50000" in md

    def test_inclui_top_videos(self):
        parsed = {
            "videos": [
                {
                    "id": "v1",
                    "text": "Video viral",
                    "plays": 1000000,
                    "likes": 50000,
                    "comments": 1000,
                    "shares": 500,
                    "url": "https://tiktok.com/v/v1",
                }
            ],
            "profile": {"handle": "x"},
            "metrics": {"total_videos": 1, "avg_plays": 1000000, "avg_likes": 50000, "avg_comments": 1000},
            "top_hashtags": [],
        }
        md = format_summary_md(parsed, handle="x")
        assert "Video viral" in md or "1,000,000" in md or "1000000" in md


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
        assert "custo" in result.stdout.lower()

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
