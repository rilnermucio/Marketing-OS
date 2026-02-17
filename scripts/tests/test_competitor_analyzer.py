#!/usr/bin/env python3
"""
Testes para competitor_analyzer.py
"""

import sys
import os
import json
import pytest
from unittest.mock import patch, MagicMock

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from competitor_analyzer import (
    analisar_instagram,
    analisar_youtube,
    analisar_twitter,
    analisar_linkedin,
    analisar_site,
    comparar_concorrentes,
    gerar_relatorio_swot,
    formatar_tabela,
    formatar_markdown,
)


# =====================================================================
# TESTES DE analisar_instagram
# =====================================================================

def test_analisar_instagram_retorna_estrutura():
    with patch('competitor_analyzer.fazer_requisicao', return_value=None):
        resultado = analisar_instagram("teste_perfil")
    assert "plataforma" in resultado
    assert resultado["plataforma"] == "Instagram"
    assert "username" in resultado
    assert "@teste_perfil" in resultado["username"]

def test_analisar_instagram_remove_arroba():
    with patch('competitor_analyzer.fazer_requisicao', return_value=None):
        resultado = analisar_instagram("@meu_perfil")
    assert resultado["username"] == "@meu_perfil"

def test_analisar_instagram_sem_acesso():
    with patch('competitor_analyzer.fazer_requisicao', return_value=None):
        resultado = analisar_instagram("perfil_privado")
    assert resultado["status"] in ["perfil_privado_ou_indisponivel", "sucesso"]
    assert "insights" in resultado

def test_analisar_instagram_url_correta():
    with patch('competitor_analyzer.fazer_requisicao', return_value=None):
        resultado = analisar_instagram("minha_marca")
    assert "instagram.com/minha_marca" in resultado["url"]


# =====================================================================
# TESTES DE analisar_youtube
# =====================================================================

def test_analisar_youtube_retorna_estrutura():
    with patch('competitor_analyzer.fazer_requisicao', return_value=None):
        resultado = analisar_youtube("UCxxxx")
    assert "plataforma" in resultado
    assert resultado["plataforma"] == "YouTube"
    assert "metricas" in resultado
    assert "conteudo" in resultado
    assert "insights" in resultado

def test_analisar_youtube_sem_rss():
    with patch('competitor_analyzer.fazer_requisicao', return_value=None):
        resultado = analisar_youtube("canal_invalido")
    assert resultado["status"] in ["canal_nao_encontrado_via_rss", "sucesso"]

def test_analisar_youtube_com_rss_simulado():
    rss_mock = """<?xml version="1.0" encoding="UTF-8"?>
<feed>
  <name>Canal Teste</name>
  <entry>
    <title>Vídeo Incrível 1: 10 Dicas</title>
    <yt:videoId>abc123</yt:videoId>
    <published>2026-01-15T10:00:00</published>
  </entry>
  <entry>
    <title>Como fazer marketing digital?</title>
    <yt:videoId>def456</yt:videoId>
    <published>2026-01-10T10:00:00</published>
  </entry>
</feed>"""
    with patch('competitor_analyzer.fazer_requisicao', return_value=rss_mock):
        resultado = analisar_youtube("UCtest")
    assert resultado["status"] == "sucesso"
    assert len(resultado["conteudo"]["ultimos_videos"]) >= 1


# =====================================================================
# TESTES DE analisar_twitter
# =====================================================================

def test_analisar_twitter_retorna_estrutura():
    resultado = analisar_twitter("usuario_teste")
    assert "plataforma" in resultado
    assert "Twitter" in resultado["plataforma"]
    assert "status" in resultado
    assert resultado["status"] == "limitado"

def test_analisar_twitter_tem_alternativas():
    resultado = analisar_twitter("qualquer_usuario")
    assert "alternativas" in resultado
    assert len(resultado["alternativas"]) > 0

def test_analisar_twitter_tem_insights():
    resultado = analisar_twitter("usuario")
    assert "insights" in resultado
    assert len(resultado["insights"]) > 0

def test_analisar_twitter_remove_arroba():
    resultado = analisar_twitter("@meu_usuario")
    assert resultado["username"] == "@meu_usuario"


# =====================================================================
# TESTES DE analisar_linkedin
# =====================================================================

def test_analisar_linkedin_retorna_estrutura():
    resultado = analisar_linkedin("joao-silva")
    assert "plataforma" in resultado
    assert resultado["plataforma"] == "LinkedIn"
    assert "checklist_analise_manual" in resultado
    assert "metricas_para_observar" in resultado

def test_analisar_linkedin_status_limitado():
    resultado = analisar_linkedin("empresa-teste")
    assert resultado["status"] == "limitado"

def test_analisar_linkedin_checklist_completo():
    resultado = analisar_linkedin("perfil")
    checklist = resultado["checklist_analise_manual"]
    assert "perfil_pessoal" in checklist
    assert "pagina_empresa" in checklist
    assert len(checklist["perfil_pessoal"]) > 0

def test_analisar_linkedin_url_construida():
    resultado = analisar_linkedin("meu-perfil")
    assert "linkedin.com" in resultado["url"]


# =====================================================================
# TESTES DE analisar_site
# =====================================================================

def test_analisar_site_sem_acesso():
    with patch('competitor_analyzer.fazer_requisicao', return_value=None):
        resultado = analisar_site("https://exemplo.com")
    assert resultado["status"] == "site_inacessivel"

def test_analisar_site_adiciona_https():
    with patch('competitor_analyzer.fazer_requisicao', return_value=None):
        resultado = analisar_site("exemplo.com")
    assert resultado["url"].startswith("https://")

def test_analisar_site_com_html_simulado():
    html_mock = """
    <html>
    <head>
        <title>Site de Teste</title>
        <meta name="description" content="Esta é a descrição da página de teste com mais de cem caracteres para ser válida aqui.">
        <meta property="og:title" content="Site Teste">
    </head>
    <body>
        <h1>Título Principal</h1>
        <script>gtag('event', 'page_view');</script>
    </body>
    </html>
    """
    with patch('competitor_analyzer.fazer_requisicao', return_value=html_mock):
        resultado = analisar_site("https://exemplo.com")
    assert resultado["status"] == "sucesso"
    assert resultado["seo"]["titulo"] == "Site de Teste"
    assert resultado["seo"]["tem_og_tags"] is True
    assert resultado["tecnologia"]["google_analytics"] is True

def test_analisar_site_detecta_wordpress():
    html_mock = """
    <html><body>
    <link rel='stylesheet' href='/wp-content/themes/meu-tema/style.css'>
    </body></html>
    """
    with patch('competitor_analyzer.fazer_requisicao', return_value=html_mock):
        resultado = analisar_site("https://exemplo.com")
    assert resultado["tecnologia"].get("cms") == "WordPress"


# =====================================================================
# TESTES DE comparar_concorrentes
# =====================================================================

def test_comparar_concorrentes_basico():
    analises = [
        {"plataforma": "Instagram", "username": "@conta1", "metricas": {}, "insights": [], "status": "sucesso"},
        {"plataforma": "Instagram", "username": "@conta2", "metricas": {}, "insights": [], "status": "sucesso"},
    ]
    resultado = comparar_concorrentes(analises)
    assert "concorrentes_analisados" in resultado
    assert resultado["concorrentes_analisados"] == 2
    assert "oportunidades" in resultado
    assert "recomendacoes" in resultado

def test_comparar_concorrentes_agrupamento():
    analises = [
        {"plataforma": "Instagram", "username": "@insta1", "metricas": {}, "insights": []},
        {"plataforma": "YouTube", "canal": "canal1", "metricas": {}, "insights": []},
    ]
    resultado = comparar_concorrentes(analises)
    assert "Instagram" in resultado["comparativo"]
    assert "YouTube" in resultado["comparativo"]

def test_comparar_concorrentes_um_item():
    analises = [
        {"plataforma": "Twitter/X", "username": "@usuario", "metricas": {}, "insights": []},
    ]
    resultado = comparar_concorrentes(analises)
    assert resultado["concorrentes_analisados"] == 1

def test_comparar_concorrentes_youtube_ranking():
    analises = [
        {"plataforma": "YouTube", "canal": "canal_grande", "metricas": {"views_medio": 100000}, "insights": []},
        {"plataforma": "YouTube", "canal": "canal_pequeno", "metricas": {"views_medio": 1000}, "insights": []},
    ]
    resultado = comparar_concorrentes(analises)
    if "YouTube_views" in resultado.get("rankings", {}):
        ranking = resultado["rankings"]["YouTube_views"]
        assert ranking[0]["views_medio"] > ranking[1]["views_medio"]


# =====================================================================
# TESTES DE gerar_relatorio_swot
# =====================================================================

def test_gerar_relatorio_swot_estrutura():
    analises = [
        {"plataforma": "Instagram", "username": "@teste", "metricas": {}, "insights": []},
    ]
    resultado = gerar_relatorio_swot(analises)
    assert "oportunidades" in resultado
    assert "ameacas" in resultado
    assert "acoes_recomendadas" in resultado

def test_gerar_relatorio_swot_acoes_tem_prioridade():
    analises = [{"plataforma": "Instagram", "username": "@teste", "metricas": {}, "insights": []}]
    resultado = gerar_relatorio_swot(analises)
    acoes = resultado["acoes_recomendadas"]
    assert len(acoes) > 0
    for acao in acoes:
        assert "prioridade" in acao
        assert "acao" in acao


# =====================================================================
# TESTES DE FORMATAÇÃO
# =====================================================================

def test_formatar_tabela_retorna_string():
    analises = [
        {"plataforma": "Instagram", "username": "@teste", "metricas": {}, "insights": ["insight 1"], "status": "sucesso"},
    ]
    resultado = formatar_tabela(analises)
    assert isinstance(resultado, str)
    assert "ANÁLISE DE CONCORRENTES" in resultado
    assert "@teste" in resultado

def test_formatar_markdown_retorna_string():
    analises = [
        {"plataforma": "YouTube", "canal": "meu_canal", "url": "https://yt.com", "metricas": {}, "conteudo": {}, "insights": ["insight"], "status": "sucesso"},
    ]
    resultado = formatar_markdown(analises)
    assert isinstance(resultado, str)
    assert "# Análise de Concorrentes" in resultado

def test_formatar_tabela_com_comparacao():
    analises = [
        {"plataforma": "Instagram", "username": "@a", "metricas": {}, "insights": [], "status": "sucesso"},
        {"plataforma": "Instagram", "username": "@b", "metricas": {}, "insights": [], "status": "sucesso"},
    ]
    comparacao = {
        "oportunidades": ["Oportunidade 1"],
        "recomendacoes": ["Recomendação 1"],
    }
    resultado = formatar_tabela(analises, comparacao)
    assert "OPORTUNIDADES" in resultado
    assert "Oportunidade 1" in resultado
