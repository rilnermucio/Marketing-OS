#!/usr/bin/env python3
"""
Testes para apify_twitter.py — Twitter/X profile scraper via Apify.
"""

import os
import subprocess
import sys

import pytest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from apify_twitter import (
    DEFAULT_MAX_TWEETS,
    HARD_CAP_TWEETS,
    TWITTER_ACTOR_ID,
    build_input,
    format_summary_md,
    normalize_handle,
    parse_twitter_results,
)


SCRIPT_PATH = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    "apify_twitter.py",
)


# ---------------------------------------------------------------------------
# normalize_handle
# ---------------------------------------------------------------------------


class TestNormalizeHandle:
    def test_handle_simples(self):
        assert normalize_handle("elonmusk") == "elonmusk"

    def test_handle_com_arroba(self):
        assert normalize_handle("@elonmusk") == "elonmusk"

    def test_url_x_com(self):
        assert normalize_handle("https://x.com/elonmusk") == "elonmusk"

    def test_url_twitter_com(self):
        assert normalize_handle("https://twitter.com/elonmusk") == "elonmusk"

    def test_url_com_query_string(self):
        assert normalize_handle("https://x.com/elonmusk?lang=en") == "elonmusk"

    def test_strip_espacos(self):
        assert normalize_handle("  @elonmusk  ") == "elonmusk"


# ---------------------------------------------------------------------------
# build_input
# ---------------------------------------------------------------------------


class TestBuildInput:
    def test_inclui_handle(self):
        inp = build_input("elonmusk", max_tweets=50)
        assert inp["twitterHandles"] == ["elonmusk"]

    def test_max_tweets_propagado(self):
        inp = build_input("x", max_tweets=100)
        assert inp["maxItems"] == 100

    def test_max_tweets_acima_do_cap_e_limitado(self):
        inp = build_input("x", max_tweets=9999)
        assert inp["maxItems"] == HARD_CAP_TWEETS

    def test_max_tweets_zero_ou_negativo_vira_um(self):
        inp = build_input("x", max_tweets=0)
        assert inp["maxItems"] == 1

    def test_default_max_tweets(self):
        inp = build_input("x")
        assert inp["maxItems"] == DEFAULT_MAX_TWEETS

    def test_aceita_handle_com_arroba(self):
        inp = build_input("@elonmusk")
        assert inp["twitterHandles"] == ["elonmusk"]


# ---------------------------------------------------------------------------
# parse_twitter_results
# ---------------------------------------------------------------------------


class TestParseTwitterResults:
    def test_extrai_tweets(self):
        raw = [
            {
                "id": "1",
                "text": "Hello world",
                "url": "https://x.com/u/status/1",
                "createdAt": "2026-01-01T00:00:00Z",
                "likeCount": 100,
                "retweetCount": 10,
                "replyCount": 5,
                "viewCount": 1000,
                "author": {"userName": "elonmusk", "name": "Elon Musk"},
            },
            {
                "id": "2",
                "text": "Another tweet",
                "url": "https://x.com/u/status/2",
                "createdAt": "2026-01-02T00:00:00Z",
                "likeCount": 200,
                "retweetCount": 20,
                "replyCount": 10,
                "author": {"userName": "elonmusk"},
            },
        ]
        parsed = parse_twitter_results(raw)
        assert len(parsed["tweets"]) == 2
        assert parsed["tweets"][0]["text"] == "Hello world"
        assert parsed["tweets"][0]["likes"] == 100
        assert parsed["tweets"][0]["retweets"] == 10

    def test_extrai_perfil_do_author(self):
        raw = [
            {
                "id": "1",
                "text": "x",
                "author": {"userName": "elonmusk", "name": "Elon Musk"},
            }
        ]
        parsed = parse_twitter_results(raw)
        assert parsed["profile"]["handle"] == "elonmusk"
        assert parsed["profile"]["name"] == "Elon Musk"

    def test_calcula_metricas_agregadas(self):
        raw = [
            {"id": "1", "text": "x", "likeCount": 100, "retweetCount": 10, "replyCount": 5},
            {"id": "2", "text": "y", "likeCount": 200, "retweetCount": 20, "replyCount": 10},
        ]
        parsed = parse_twitter_results(raw)
        assert parsed["metrics"]["total_tweets"] == 2
        assert parsed["metrics"]["avg_likes"] == 150
        assert parsed["metrics"]["avg_retweets"] == 15

    def test_input_vazio(self):
        parsed = parse_twitter_results([])
        assert parsed["tweets"] == []
        assert parsed["profile"] == {}
        assert parsed["metrics"]["total_tweets"] == 0

    def test_campos_ausentes_nao_crasham(self):
        raw = [{"id": "x"}]
        parsed = parse_twitter_results(raw)
        assert len(parsed["tweets"]) == 1
        assert parsed["tweets"][0]["likes"] == 0


# ---------------------------------------------------------------------------
# format_summary_md
# ---------------------------------------------------------------------------


class TestFormatSummaryMd:
    def test_inclui_handle_no_titulo(self):
        parsed = {
            "tweets": [],
            "profile": {"handle": "elonmusk", "name": "Elon Musk"},
            "metrics": {"total_tweets": 0, "avg_likes": 0, "avg_retweets": 0},
        }
        md = format_summary_md(parsed, handle="elonmusk")
        assert "elonmusk" in md

    def test_inclui_metricas(self):
        parsed = {
            "tweets": [],
            "profile": {"handle": "x"},
            "metrics": {"total_tweets": 50, "avg_likes": 1000, "avg_retweets": 100},
        }
        md = format_summary_md(parsed, handle="x")
        assert "50" in md
        assert "1,000" in md or "1000" in md

    def test_inclui_top_tweets(self):
        parsed = {
            "tweets": [
                {
                    "id": "1",
                    "text": "Tweet viral aqui",
                    "likes": 10000,
                    "retweets": 500,
                    "replies": 100,
                    "url": "https://x.com/u/status/1",
                }
            ],
            "profile": {"handle": "x"},
            "metrics": {"total_tweets": 1, "avg_likes": 10000, "avg_retweets": 500},
        }
        md = format_summary_md(parsed, handle="x")
        assert "Tweet viral aqui" in md or "10000" in md or "10,000" in md


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
