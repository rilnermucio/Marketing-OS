#!/usr/bin/env python3
"""
Testes para apify_youtube.py — YouTube channel scraper via Apify.
"""

import os
import subprocess
import sys

import pytest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from apify_youtube import (
    DEFAULT_MAX_VIDEOS,
    HARD_CAP_VIDEOS,
    YOUTUBE_ACTOR_ID,
    build_channel_url,
    build_input,
    format_summary_md,
    parse_youtube_results,
)


SCRIPT_PATH = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    "apify_youtube.py",
)


# ---------------------------------------------------------------------------
# build_channel_url
# ---------------------------------------------------------------------------


class TestBuildChannelUrl:
    def test_handle_com_arroba(self):
        url = build_channel_url("@mrbeast")
        assert url == "https://www.youtube.com/@mrbeast/videos"

    def test_handle_sem_arroba_assume_at(self):
        url = build_channel_url("mrbeast")
        assert "@mrbeast" in url

    def test_url_completa_passthrough(self):
        url = build_channel_url("https://www.youtube.com/@mrbeast")
        # Adiciona /videos se não estiver presente
        assert "youtube.com" in url
        assert "@mrbeast" in url

    def test_url_com_videos_path_preserva(self):
        url = build_channel_url("https://www.youtube.com/@mrbeast/videos")
        assert "/videos" in url

    def test_channel_id_format(self):
        url = build_channel_url("https://www.youtube.com/channel/UCabc123")
        assert "channel/UCabc123" in url

    def test_strip_espacos(self):
        url = build_channel_url("  @mrbeast  ")
        assert "@mrbeast" in url


# ---------------------------------------------------------------------------
# build_input
# ---------------------------------------------------------------------------


class TestBuildInput:
    def test_inclui_url_em_start_urls(self):
        inp = build_input("@mrbeast", max_videos=20)
        assert "startUrls" in inp
        assert isinstance(inp["startUrls"], list)
        assert "youtube.com" in inp["startUrls"][0]["url"]

    def test_max_videos_propagado(self):
        inp = build_input("x", max_videos=30)
        assert inp["maxResults"] == 30

    def test_max_videos_acima_do_cap_e_limitado(self):
        inp = build_input("x", max_videos=999)
        assert inp["maxResults"] == HARD_CAP_VIDEOS

    def test_max_videos_zero_ou_negativo_vira_um(self):
        inp = build_input("x", max_videos=0)
        assert inp["maxResults"] == 1

    def test_default_max_videos(self):
        inp = build_input("x")
        assert inp["maxResults"] == DEFAULT_MAX_VIDEOS


# ---------------------------------------------------------------------------
# parse_youtube_results
# ---------------------------------------------------------------------------


class TestParseYoutubeResults:
    def test_extrai_videos(self):
        raw = [
            {
                "id": "v1",
                "title": "Video Title 1",
                "url": "https://youtube.com/watch?v=v1",
                "viewCount": 1000000,
                "likes": 50000,
                "commentsCount": 1000,
                "duration": "10:30",
                "date": "2026-01-01",
                "channelName": "MrBeast",
                "channelUrl": "https://youtube.com/@mrbeast",
            }
        ]
        parsed = parse_youtube_results(raw)
        assert len(parsed["videos"]) == 1
        v = parsed["videos"][0]
        assert v["title"] == "Video Title 1"
        assert v["views"] == 1000000
        assert v["likes"] == 50000

    def test_extrai_canal(self):
        raw = [
            {
                "id": "v1",
                "channelName": "MrBeast",
                "channelUrl": "https://youtube.com/@mrbeast",
            }
        ]
        parsed = parse_youtube_results(raw)
        assert parsed["channel"]["name"] == "MrBeast"

    def test_calcula_metricas_agregadas(self):
        raw = [
            {"id": "1", "viewCount": 1000000, "likes": 50000, "commentsCount": 1000},
            {"id": "2", "viewCount": 2000000, "likes": 100000, "commentsCount": 2000},
        ]
        parsed = parse_youtube_results(raw)
        assert parsed["metrics"]["total_videos"] == 2
        assert parsed["metrics"]["avg_views"] == 1500000
        assert parsed["metrics"]["avg_likes"] == 75000

    def test_input_vazio(self):
        parsed = parse_youtube_results([])
        assert parsed["videos"] == []
        assert parsed["channel"] == {}
        assert parsed["metrics"]["total_videos"] == 0

    def test_campos_ausentes_nao_crasham(self):
        raw = [{"id": "x"}]
        parsed = parse_youtube_results(raw)
        assert len(parsed["videos"]) == 1
        assert parsed["videos"][0]["views"] == 0


# ---------------------------------------------------------------------------
# format_summary_md
# ---------------------------------------------------------------------------


class TestFormatSummaryMd:
    def test_inclui_canal_no_titulo(self):
        parsed = {
            "videos": [],
            "channel": {"name": "MrBeast"},
            "metrics": {"total_videos": 0, "avg_views": 0, "avg_likes": 0, "avg_comments": 0},
        }
        md = format_summary_md(parsed, target="@mrbeast")
        assert "MrBeast" in md or "mrbeast" in md

    def test_inclui_metricas(self):
        parsed = {
            "videos": [],
            "channel": {"name": "x"},
            "metrics": {
                "total_videos": 20,
                "avg_views": 5000000,
                "avg_likes": 250000,
                "avg_comments": 5000,
            },
        }
        md = format_summary_md(parsed, target="x")
        assert "20" in md
        assert "5,000,000" in md or "5000000" in md

    def test_inclui_top_videos(self):
        parsed = {
            "videos": [
                {
                    "id": "v1",
                    "title": "Video viral",
                    "views": 100000000,
                    "likes": 5000000,
                    "comments": 100000,
                    "duration": "12:34",
                    "url": "https://youtube.com/watch?v=v1",
                }
            ],
            "channel": {"name": "x"},
            "metrics": {"total_videos": 1, "avg_views": 100000000, "avg_likes": 5000000, "avg_comments": 100000},
        }
        md = format_summary_md(parsed, target="x")
        assert "Video viral" in md


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------


class TestCli:
    def test_dry_run_imprime_estimativa_e_sai_zero(self):
        result = subprocess.run(
            [sys.executable, SCRIPT_PATH, "--channel", "@x", "--dry-run"],
            capture_output=True,
            text=True,
        )
        assert result.returncode == 0
        assert "custo" in result.stdout.lower()

    def test_token_ausente_sai_zero_com_mensagem(self):
        env = os.environ.copy()
        env.pop("APIFY_TOKEN", None)
        result = subprocess.run(
            [sys.executable, SCRIPT_PATH, "--channel", "@x"],
            capture_output=True,
            text=True,
            env=env,
        )
        assert result.returncode == 0
        assert "APIFY_TOKEN" in result.stderr

    def test_channel_obrigatorio(self):
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
        assert "channel" in result.stdout.lower()
