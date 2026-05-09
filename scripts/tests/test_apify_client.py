#!/usr/bin/env python3
"""
Testes para apify_client.py — wrapper do Apify Run-Sync API.

Cobre:
- _get_token (env var APIFY_TOKEN)
- _actor_url (formatação username/name -> username~name)
- run_actor_sync (chamada do endpoint, mapeamento de erros)
- estimate_cost (heurística por Actor)
- save_result (escrita de JSON em diretório)
- Exceções: ApifyAPIError, ApifyAuthError, ApifyRateLimitError, ApifyTimeoutError

Não realiza chamadas reais à Apify — mocka _http_post_json.
"""

import json
import os
import sys

import pytest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from apify_client import (
    APIFY_API_BASE,
    ENV_TOKEN,
    ApifyAPIError,
    ApifyAuthError,
    ApifyRateLimitError,
    ApifyTimeoutError,
    _actor_url,
    _get_token,
    _slugify,
    estimate_cost,
    run_actor_sync,
    save_result,
)


# ---------------------------------------------------------------------------
# _get_token
# ---------------------------------------------------------------------------


class TestGetToken:
    def test_retorna_token_da_env(self, monkeypatch):
        monkeypatch.setenv(ENV_TOKEN, "apify_api_xxx")
        assert _get_token() == "apify_api_xxx"

    def test_token_ausente_levanta_auth_error(self, monkeypatch):
        monkeypatch.delenv(ENV_TOKEN, raising=False)
        with pytest.raises(ApifyAuthError):
            _get_token()

    def test_token_apenas_espacos_levanta_auth_error(self, monkeypatch):
        monkeypatch.setenv(ENV_TOKEN, "   ")
        with pytest.raises(ApifyAuthError):
            _get_token()

    def test_token_com_espacos_em_volta_e_strip(self, monkeypatch):
        monkeypatch.setenv(ENV_TOKEN, "  apify_api_yyy  ")
        assert _get_token() == "apify_api_yyy"


# ---------------------------------------------------------------------------
# _actor_url
# ---------------------------------------------------------------------------


class TestActorUrl:
    def test_converte_slash_para_til(self):
        url = _actor_url("apify/google-search-scraper")
        assert "apify~google-search-scraper" in url
        assert "/" not in url.split("/acts/")[1].split("/")[0]

    def test_inclui_endpoint_run_sync(self):
        url = _actor_url("apify/x")
        assert "run-sync-get-dataset-items" in url

    def test_usa_api_base_correto(self):
        url = _actor_url("apify/x")
        assert url.startswith(APIFY_API_BASE)


# ---------------------------------------------------------------------------
# run_actor_sync
# ---------------------------------------------------------------------------


class TestRunActorSync:
    def test_chama_endpoint_correto(self, monkeypatch):
        captured = {}

        def fake_post(url, data, headers, timeout):
            captured["url"] = url
            captured["headers"] = headers
            return [{"item": 1}]

        monkeypatch.setattr("apify_client._http_post_json", fake_post)
        run_actor_sync(
            "apify/google-search-scraper", {"q": "test"}, token="tok", timeout=60
        )
        assert "apify~google-search-scraper" in captured["url"]
        assert captured["headers"]["Authorization"] == "Bearer tok"
        assert captured["headers"]["Content-Type"] == "application/json"

    def test_retorna_lista_de_items(self, monkeypatch):
        monkeypatch.setattr(
            "apify_client._http_post_json",
            lambda url, data, headers, timeout: [{"a": 1}, {"a": 2}],
        )
        result = run_actor_sync("apify/x", {}, token="tok")
        assert result == [{"a": 1}, {"a": 2}]

    def test_propaga_input_data_como_json(self, monkeypatch):
        captured = {}

        def fake_post(url, data, headers, timeout):
            captured["data"] = data
            return []

        monkeypatch.setattr("apify_client._http_post_json", fake_post)
        run_actor_sync("apify/x", {"foo": "bar"}, token="tok")
        body = json.loads(captured["data"].decode("utf-8"))
        assert body == {"foo": "bar"}

    def test_propaga_timeout_para_http(self, monkeypatch):
        captured = {}

        def fake_post(url, data, headers, timeout):
            captured["timeout"] = timeout
            return []

        monkeypatch.setattr("apify_client._http_post_json", fake_post)
        run_actor_sync("apify/x", {}, token="tok", timeout=120)
        assert captured["timeout"] == 120

    def test_401_levanta_auth_error(self, monkeypatch):
        def raise_auth(url, data, headers, timeout):
            raise ApifyAuthError("Invalid token", status=401)

        monkeypatch.setattr("apify_client._http_post_json", raise_auth)
        with pytest.raises(ApifyAuthError):
            run_actor_sync("apify/x", {}, token="tok")

    def test_429_levanta_rate_limit(self, monkeypatch):
        def raise_rate(url, data, headers, timeout):
            raise ApifyRateLimitError("Rate limited", status=429)

        monkeypatch.setattr("apify_client._http_post_json", raise_rate)
        with pytest.raises(ApifyRateLimitError):
            run_actor_sync("apify/x", {}, token="tok")

    def test_timeout_levanta_timeout_error(self, monkeypatch):
        def raise_timeout(url, data, headers, timeout):
            raise ApifyTimeoutError("Timed out after 60s")

        monkeypatch.setattr("apify_client._http_post_json", raise_timeout)
        with pytest.raises(ApifyTimeoutError):
            run_actor_sync("apify/x", {}, token="tok")


# ---------------------------------------------------------------------------
# estimate_cost
# ---------------------------------------------------------------------------


class TestEstimateCost:
    def test_serp_baseado_em_queries_e_results(self):
        cost = estimate_cost(
            "apify/google-search-scraper",
            {"queries": ["a", "b"], "resultsPerPage": 10},
        )
        # 2 queries × 10 results × $0.005 = $0.10
        assert cost > 0
        assert cost < 1.0

    def test_serp_uma_query_dez_resultados(self):
        cost = estimate_cost(
            "apify/google-search-scraper",
            {"queries": ["x"], "resultsPerPage": 10},
        )
        # 1 × 10 × 0.005 = 0.05
        assert 0.04 < cost < 0.06

    def test_instagram_baseado_em_results_limit(self):
        cost_30 = estimate_cost(
            "apify/instagram-scraper",
            {"directUrls": ["https://instagram.com/x"], "resultsLimit": 30},
        )
        cost_100 = estimate_cost(
            "apify/instagram-scraper",
            {"directUrls": ["https://instagram.com/x"], "resultsLimit": 100},
        )
        assert cost_30 > 0
        assert cost_100 > cost_30

    def test_actor_desconhecido_retorna_zero(self):
        cost = estimate_cost("apify/unknown-actor", {})
        assert cost == 0.0

    def test_input_vazio_nao_crasha(self):
        # Defensive: input incompleto não deve crashar, apenas estimar mínimo
        cost = estimate_cost("apify/google-search-scraper", {})
        assert cost >= 0.0


# ---------------------------------------------------------------------------
# _slugify
# ---------------------------------------------------------------------------


class TestSlugify:
    def test_converte_para_minuscula(self):
        assert _slugify("HELLO WORLD") == "hello-world"

    def test_remove_caracteres_especiais(self):
        assert _slugify("hello, world!") == "hello-world"

    def test_acentos_removidos_ou_mantidos_consistentes(self):
        # Não exigimos remoção de acentos; só que o resultado seja não-vazio
        slug = _slugify("infoproduto bofu")
        assert slug == "infoproduto-bofu"

    def test_string_vazia_retorna_default(self):
        assert _slugify("") == "result"

    def test_apenas_simbolos_retorna_default(self):
        assert _slugify("!!!") == "result"

    def test_trunca_para_max_length(self):
        long = "a" * 100
        assert len(_slugify(long, max_length=20)) == 20


# ---------------------------------------------------------------------------
# save_result
# ---------------------------------------------------------------------------


class TestSaveResult:
    def test_cria_arquivo_no_diretorio(self, tmp_path):
        data = {"source": "test", "results": []}
        path = save_result(data, slug="test-query", output_dir=str(tmp_path))
        assert os.path.exists(path)

    def test_arquivo_e_json_valido(self, tmp_path):
        data = {"source": "test", "results": [{"a": 1, "title": "Olá"}]}
        path = save_result(data, slug="test-query", output_dir=str(tmp_path))
        with open(path, encoding="utf-8") as f:
            loaded = json.load(f)
        assert loaded == data

    def test_filename_contem_slug(self, tmp_path):
        path = save_result({"x": 1}, slug="instagram-handle", output_dir=str(tmp_path))
        assert "instagram-handle" in os.path.basename(path)

    def test_filename_contem_timestamp(self, tmp_path):
        path = save_result({"x": 1}, slug="q", output_dir=str(tmp_path))
        basename = os.path.basename(path)
        assert basename.endswith(".json")
        # Timestamp ISO-ish: 2026-... ou 2025-... (UTC)
        assert basename[:4].isdigit()
        assert int(basename[:4]) >= 2025

    def test_cria_diretorio_se_nao_existir(self, tmp_path):
        nested = tmp_path / "research" / "apify"
        path = save_result({"x": 1}, slug="q", output_dir=str(nested))
        assert os.path.exists(path)
        assert nested.exists()

    def test_preserva_acentuacao_pt_br(self, tmp_path):
        data = {"query": "informação", "summary": "São Paulo"}
        path = save_result(data, slug="info", output_dir=str(tmp_path))
        with open(path, encoding="utf-8") as f:
            content = f.read()
        # ensure_ascii=False deve preservar acentos
        assert "informação" in content
        assert "São Paulo" in content
