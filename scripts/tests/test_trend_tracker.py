#!/usr/bin/env python3
"""
Testes para trend_tracker.py
"""

import sys
import os
import json
import pytest
from unittest.mock import patch

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from trend_tracker import (
    buscar_google_trends,
    buscar_reddit,
    buscar_hacker_news,
    buscar_twitter_trends,
    buscar_noticias_tech,
    buscar_youtube_trends,
    obter_trending_geral,
    formatar_resultado_tabela,
    formatar_resultado_markdown,
)


# =====================================================================
# TESTES DE buscar_google_trends
# =====================================================================

def test_buscar_google_trends_retorna_estrutura():
    with patch('trend_tracker.fazer_requisicao', return_value=None):
        resultado = buscar_google_trends("marketing digital")
    assert "plataforma" in resultado
    assert resultado["plataforma"] == "Google Trends"
    assert "termo_buscado" in resultado
    assert resultado["termo_buscado"] == "marketing digital"

def test_buscar_google_trends_campos_obrigatorios():
    with patch('trend_tracker.fazer_requisicao', return_value=None):
        resultado = buscar_google_trends("ia")
    assert "sugestoes_busca" in resultado
    assert "data_consulta" in resultado
    assert "status" in resultado

def test_buscar_google_trends_com_sugestoes():
    mock_response = json.dumps(["ia", ["inteligência artificial", "ia generativa", "ia brasil"]])
    with patch('trend_tracker.fazer_requisicao', return_value=mock_response):
        resultado = buscar_google_trends("ia")
    assert resultado["status"] == "sucesso"
    assert len(resultado["sugestoes_busca"]) > 0

def test_buscar_google_trends_regiao():
    with patch('trend_tracker.fazer_requisicao', return_value=None):
        resultado = buscar_google_trends("python", regiao="US")
    assert resultado["regiao"] == "US"


# =====================================================================
# TESTES DE buscar_reddit
# =====================================================================

def test_buscar_reddit_retorna_estrutura():
    with patch('trend_tracker.fazer_requisicao', return_value=None):
        resultado = buscar_reddit("marketing")
    assert "plataforma" in resultado
    assert resultado["plataforma"] == "Reddit"
    assert "posts" in resultado
    assert "termo_buscado" in resultado

def test_buscar_reddit_com_dados():
    mock_data = {
        "data": {
            "children": [
                {
                    "data": {
                        "title": "Post sobre marketing digital",
                        "subreddit": "marketing",
                        "score": 500,
                        "num_comments": 30,
                        "permalink": "/r/marketing/comments/abc/post",
                        "created_utc": 1700000000.0,
                        "upvote_ratio": 0.95
                    }
                }
            ]
        }
    }
    with patch('trend_tracker.fazer_requisicao', return_value=json.dumps(mock_data)):
        resultado = buscar_reddit("marketing")
    assert len(resultado["posts"]) == 1
    assert resultado["posts"][0]["titulo"] == "Post sobre marketing digital"
    assert resultado["posts"][0]["score"] == 500
    assert "metricas" in resultado

def test_buscar_reddit_sem_resultados():
    mock_data = {"data": {"children": []}}
    with patch('trend_tracker.fazer_requisicao', return_value=json.dumps(mock_data)):
        resultado = buscar_reddit("termo_inexistente")
    assert resultado["posts"] == []

def test_buscar_reddit_erro_rede():
    with patch('trend_tracker.fazer_requisicao', return_value=None):
        resultado = buscar_reddit("qualquer")
    assert isinstance(resultado["posts"], list)


# =====================================================================
# TESTES DE buscar_hacker_news
# =====================================================================

def test_buscar_hacker_news_retorna_estrutura():
    with patch('trend_tracker.fazer_requisicao', return_value=None):
        resultado = buscar_hacker_news("python")
    assert "plataforma" in resultado
    assert resultado["plataforma"] == "Hacker News"
    assert "posts" in resultado

def test_buscar_hacker_news_com_dados():
    mock_data = {
        "hits": [
            {
                "title": "Python 4.0 Released",
                "url": "https://python.org/news",
                "points": 450,
                "num_comments": 200,
                "author": "guido",
                "created_at": "2026-01-15T10:00:00.000Z",
                "objectID": "12345"
            }
        ]
    }
    with patch('trend_tracker.fazer_requisicao', return_value=json.dumps(mock_data)):
        resultado = buscar_hacker_news("python")
    assert len(resultado["posts"]) == 1
    assert resultado["posts"][0]["titulo"] == "Python 4.0 Released"
    assert resultado["posts"][0]["pontos"] == 450
    assert "metricas" in resultado

def test_buscar_hacker_news_metricas():
    mock_data = {
        "hits": [
            {"title": "Post 1", "url": "", "points": 100, "num_comments": 10, "author": "a", "created_at": "2026-01-01", "objectID": "1"},
            {"title": "Post 2", "url": "", "points": 200, "num_comments": 20, "author": "b", "created_at": "2026-01-02", "objectID": "2"},
        ]
    }
    with patch('trend_tracker.fazer_requisicao', return_value=json.dumps(mock_data)):
        resultado = buscar_hacker_news("ai")
    metricas = resultado["metricas"]
    assert metricas["pontos_total"] == 300
    assert metricas["pontos_medio"] == 150.0


# =====================================================================
# TESTES DE buscar_twitter_trends
# =====================================================================

def test_buscar_twitter_trends_retorna_estrutura():
    resultado = buscar_twitter_trends()
    assert "plataforma" in resultado
    assert "Twitter" in resultado["plataforma"]
    assert "instrucoes" in resultado
    assert "alternativas" in resultado

def test_buscar_twitter_trends_regiao():
    resultado = buscar_twitter_trends(regiao="US")
    assert resultado["regiao"] == "US"

def test_buscar_twitter_trends_instrucoes():
    resultado = buscar_twitter_trends()
    assert len(resultado["instrucoes"]) > 0

def test_buscar_twitter_trends_alternativas():
    resultado = buscar_twitter_trends()
    assert "trendsmap" in resultado["alternativas"]


# =====================================================================
# TESTES DE buscar_noticias_tech
# =====================================================================

def test_buscar_noticias_tech_retorna_estrutura():
    with patch('trend_tracker.fazer_requisicao', return_value=None):
        resultado = buscar_noticias_tech("python")
    assert "plataforma" in resultado
    assert resultado["plataforma"] == "Notícias Tech"
    assert "noticias" in resultado

def test_buscar_noticias_tech_sem_rede():
    with patch('trend_tracker.fazer_requisicao', return_value=None):
        resultado = buscar_noticias_tech("qualquer")
    assert resultado["noticias"] == []
    assert resultado["status"] == "sucesso"

def test_buscar_noticias_tech_com_feed():
    rss_mock = """
    <rss>
    <channel>
        <item>
            <title>Python AI Framework Released</title>
            <link>https://techcrunch.com/python-ai</link>
            <pubDate>Mon, 15 Jan 2026 10:00:00 GMT</pubDate>
        </item>
        <item>
            <title>JavaScript Update Notes</title>
            <link>https://techcrunch.com/js-update</link>
            <pubDate>Tue, 16 Jan 2026 10:00:00 GMT</pubDate>
        </item>
    </channel>
    </rss>
    """
    with patch('trend_tracker.fazer_requisicao', return_value=rss_mock):
        resultado = buscar_noticias_tech("python")
    # Só "Python AI Framework Released" deve aparecer (contém "python")
    assert len(resultado["noticias"]) >= 1
    assert "python" in resultado["noticias"][0]["titulo"].lower()


# =====================================================================
# TESTES DE buscar_youtube_trends
# =====================================================================

def test_buscar_youtube_trends_retorna_estrutura():
    with patch('trend_tracker.fazer_requisicao', return_value=None):
        resultado = buscar_youtube_trends("marketing")
    assert "plataforma" in resultado
    assert resultado["plataforma"] == "YouTube"
    assert "videos" in resultado
    assert "termo_buscado" in resultado

def test_buscar_youtube_trends_sem_rede():
    with patch('trend_tracker.fazer_requisicao', return_value=None):
        resultado = buscar_youtube_trends("qualquer")
    assert isinstance(resultado["videos"], list)


# =====================================================================
# TESTES DE obter_trending_geral
# =====================================================================

def test_obter_trending_geral_retorna_estrutura():
    with patch('trend_tracker.fazer_requisicao', return_value=None):
        resultado = obter_trending_geral("BR")
    assert "tipo" in resultado
    assert resultado["tipo"] == "Trending Geral"
    assert "regiao" in resultado
    assert "fontes" in resultado

def test_obter_trending_geral_regiao():
    with patch('trend_tracker.fazer_requisicao', return_value=None):
        resultado = obter_trending_geral("US")
    assert resultado["regiao"] == "US"


# =====================================================================
# TESTES DE FORMATAÇÃO
# =====================================================================

def test_formatar_resultado_tabela_reddit():
    dados = {
        "plataforma": "Reddit",
        "termo_buscado": "marketing",
        "data_consulta": "2026-01-15 10:00",
        "posts": [
            {"titulo": "Post 1", "score": 500, "comentarios": 30, "url": "https://reddit.com/r/1"},
            {"titulo": "Post 2", "score": 200, "comentarios": 15, "url": "https://reddit.com/r/2"},
        ],
        "metricas": {"total_posts": 2, "score_total": 700, "score_medio": 350.0, "comentarios_total": 45, "subreddits_unicos": 1}
    }
    resultado = formatar_resultado_tabela(dados)
    assert isinstance(resultado, str)
    assert "Reddit" in resultado
    assert "Post 1" in resultado or "Post" in resultado

def test_formatar_resultado_tabela_google():
    dados = {
        "plataforma": "Google Trends",
        "termo_buscado": "ia",
        "data_consulta": "2026-01-15 10:00",
        "sugestoes_busca": ["ia brasil", "ia generativa", "chatgpt"],
        "tendencias_do_dia": ["Trend 1", "Trend 2"],
        "trafego_aproximado": ["500K+", "300K+"]
    }
    resultado = formatar_resultado_tabela(dados)
    assert "Google Trends" in resultado
    assert "SUGESTOES DE BUSCA" in resultado or "ia brasil" in resultado

def test_formatar_resultado_markdown_posts():
    dados = {
        "plataforma": "Hacker News",
        "termo_buscado": "python",
        "data_consulta": "2026-01-15",
        "posts": [
            {"titulo": "Python Post", "pontos": 300, "comentarios": 50, "url": "https://hn.com/1"}
        ],
        "metricas": {"total_posts": 1, "pontos_total": 300, "pontos_medio": 300.0}
    }
    resultado = formatar_resultado_markdown(dados)
    assert isinstance(resultado, str)
    assert "# Hacker News" in resultado
    assert "python" in resultado.lower()

def test_formatar_resultado_markdown_videos():
    dados = {
        "plataforma": "YouTube",
        "termo_buscado": "marketing",
        "data_consulta": "2026-01-15",
        "videos": [
            {"titulo": "Vídeo Marketing", "canal": "Canal Teste", "visualizacoes": "10K", "duracao": "10:00", "url": "https://yt.com/v1"}
        ]
    }
    resultado = formatar_resultado_markdown(dados)
    assert "YouTube" in resultado
    assert "Vídeo Marketing" in resultado
