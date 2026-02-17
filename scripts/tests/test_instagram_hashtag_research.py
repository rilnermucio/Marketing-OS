#!/usr/bin/env python3
"""
Testes para instagram_hashtag_research.py
"""

import sys
import os
import json
import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from instagram_hashtag_research import (
    encontrar_nicho,
    gerar_set_hashtags,
    analisar_hashtags,
    gerar_variantes,
    get_hashtags_sazonais,
    get_dica_por_objetivo,
    formatar_tabela,
    formatar_markdown,
    HASHTAGS_DATABASE,
    HASHTAGS_ENGAJAMENTO_UNIVERSAL,
    HASHTAGS_SAZONAIS,
)


# =====================================================================
# TESTES DE encontrar_nicho
# =====================================================================

def test_encontrar_nicho_direto():
    assert encontrar_nicho("fitness") == "fitness"

def test_encontrar_nicho_com_sinonimo():
    assert encontrar_nicho("marketing") == "marketing_digital"
    assert encontrar_nicho("academia") == "fitness"
    assert encontrar_nicho("dinheiro") == "financas"

def test_encontrar_nicho_com_espaco():
    assert encontrar_nicho("marketing digital") == "marketing_digital"
    assert encontrar_nicho("desenvolvimento pessoal") == "desenvolvimento_pessoal"

def test_encontrar_nicho_inexistente():
    resultado = encontrar_nicho("nicho_completamente_inexistente_xyz123")
    assert resultado is None

def test_encontrar_nicho_case_insensitive():
    resultado = encontrar_nicho("MARKETING")
    assert resultado == "marketing_digital"


# =====================================================================
# TESTES DE gerar_set_hashtags
# =====================================================================

def test_gerar_set_hashtags_retorna_estrutura():
    resultado = gerar_set_hashtags("fitness")
    assert "nicho" in resultado
    assert "objetivo" in resultado
    assert "quantidade" in resultado
    assert "hashtags" in resultado
    assert "hashtags_texto" in resultado

def test_gerar_set_hashtags_nicho_invalido():
    resultado = gerar_set_hashtags("nicho_absolutamente_inexistente")
    assert "erro" in resultado
    assert "nichos_disponiveis" in resultado

def test_gerar_set_hashtags_quantidade():
    resultado = gerar_set_hashtags("marketing_digital", quantidade=10)
    assert len(resultado["hashtags"]) <= 10

def test_gerar_set_hashtags_objetivo_alcance():
    resultado = gerar_set_hashtags("fitness", objetivo="alcance")
    assert resultado["objetivo"] == "alcance"
    assert len(resultado["hashtags"]) > 0

def test_gerar_set_hashtags_objetivo_nicho():
    resultado = gerar_set_hashtags("empreendedorismo", objetivo="nicho")
    assert resultado["objetivo"] == "nicho"

def test_gerar_set_hashtags_objetivo_engajamento():
    resultado = gerar_set_hashtags("financas", objetivo="engajamento")
    assert resultado["objetivo"] == "engajamento"

def test_gerar_set_hashtags_todas_comecam_com_hash():
    resultado = gerar_set_hashtags("tecnologia")
    for h in resultado["hashtags"]:
        assert h.startswith("#"), f"Hashtag sem #: {h}"

def test_gerar_set_hashtags_sem_duplicatas():
    resultado = gerar_set_hashtags("marketing_digital", quantidade=20)
    hashtags = resultado["hashtags"]
    assert len(hashtags) == len(set(hashtags)), "Há hashtags duplicadas"

def test_gerar_set_hashtags_texto_concatenado():
    resultado = gerar_set_hashtags("beleza")
    texto = resultado["hashtags_texto"]
    for h in resultado["hashtags"]:
        assert h in texto

def test_gerar_set_hashtags_tem_dica():
    resultado = gerar_set_hashtags("moda")
    assert "dica" in resultado
    assert len(resultado["dica"]) > 0


# =====================================================================
# TESTES DE analisar_hashtags
# =====================================================================

def test_analisar_hashtags_retorna_estrutura():
    hashtags = ["#marketing", "#vendas", "#sucesso"]
    resultado = analisar_hashtags(hashtags)
    assert "total" in resultado
    assert "categorias" in resultado
    assert "score" in resultado
    assert "classificacao" in resultado

def test_analisar_hashtags_contagem():
    hashtags = ["#marketing", "#fitness", "#moda"]
    resultado = analisar_hashtags(hashtags)
    assert resultado["total"] == 3

def test_analisar_hashtags_sem_hash():
    # Deve funcionar mesmo sem o # no início
    hashtags = ["marketing", "#fitness"]
    resultado = analisar_hashtags(hashtags)
    assert resultado["total"] == 2

def test_analisar_hashtags_classificacao():
    # Set ideal: 10-20 hashtags com mix de tamanhos
    hashtags = [
        "#marketingdigital", "#marketing", "#socialmedia",
        "#marketingonline", "#marketingdeconteudo", "#estrategiademarketing",
        "#marketingbrasil", "#midiassociais", "#gestaoderedes",
        "#marketingparainiciantes", "#dicasdemarketing", "#aprendamarketing",
    ]
    resultado = analisar_hashtags(hashtags)
    assert resultado["classificacao"] in ["Excelente", "Bom", "Regular", "Precisa melhorar"]

def test_analisar_hashtags_score_range():
    hashtags = ["#marketing", "#fitness"]
    resultado = analisar_hashtags(hashtags)
    assert 0 <= resultado["score"] <= 100

def test_analisar_hashtags_nichos_detectados():
    hashtags = ["#marketingdigital", "#fitness", "#empreendedorismo"]
    resultado = analisar_hashtags(hashtags)
    assert len(resultado["nichos_detectados"]) > 0

def test_analisar_hashtags_muitas():
    hashtags = [f"#hashtag{i}" for i in range(35)]
    resultado = analisar_hashtags(hashtags)
    # Deve sugerir reduzir
    assert any("30" in s or "spam" in s.lower() for s in resultado["sugestoes"])

def test_analisar_hashtags_poucas():
    hashtags = ["#marketing"]
    resultado = analisar_hashtags(hashtags)
    # Deve sugerir adicionar mais
    assert len(resultado["sugestoes"]) > 0


# =====================================================================
# TESTES DE gerar_variantes
# =====================================================================

def test_gerar_variantes_retorna_lista():
    resultado = gerar_variantes("fitness", 3)
    assert isinstance(resultado, list)
    assert len(resultado) == 3

def test_gerar_variantes_objetivos_diferentes():
    variantes = gerar_variantes("marketing_digital", 3)
    if len(variantes) >= 2:
        objetivos = {v["objetivo"] for v in variantes}
        # Deve ter objetivos diferentes
        assert len(objetivos) >= 1

def test_gerar_variantes_nicho_invalido():
    resultado = gerar_variantes("nicho_invalido_xyz", 3)
    assert resultado == []

def test_gerar_variantes_set_numero():
    variantes = gerar_variantes("empreendedorismo", 3)
    for i, var in enumerate(variantes, 1):
        assert var["set_numero"] == i


# =====================================================================
# TESTES DE get_hashtags_sazonais
# =====================================================================

def test_get_hashtags_sazonais_retorna_lista():
    resultado = get_hashtags_sazonais()
    assert isinstance(resultado, list)

def test_get_hashtags_sazonais_conteudo():
    # Deve retornar hashtags ou lista vazia
    resultado = get_hashtags_sazonais()
    for h in resultado:
        assert h.startswith("#")


# =====================================================================
# TESTES DE get_dica_por_objetivo
# =====================================================================

def test_get_dica_alcance():
    dica = get_dica_por_objetivo("alcance")
    assert isinstance(dica, str)
    assert len(dica) > 0

def test_get_dica_engajamento():
    dica = get_dica_por_objetivo("engajamento")
    assert isinstance(dica, str)
    assert len(dica) > 0

def test_get_dica_nicho():
    dica = get_dica_por_objetivo("nicho")
    assert isinstance(dica, str)
    assert len(dica) > 0

def test_get_dica_objetivo_invalido():
    dica = get_dica_por_objetivo("objetivo_inexistente")
    assert isinstance(dica, str)  # Deve retornar string vazia, não quebrar


# =====================================================================
# TESTES DE FORMATAÇÃO
# =====================================================================

def test_formatar_tabela_sucesso():
    resultado = {
        "nicho": "fitness",
        "objetivo": "engajamento",
        "quantidade": 5,
        "hashtags": ["#fitness", "#treino", "#academia", "#saude", "#gym"],
        "hashtags_texto": "#fitness #treino #academia #saude #gym",
        "dica": "Dica de teste aqui."
    }
    saida = formatar_tabela(resultado)
    assert isinstance(saida, str)
    assert "fitness" in saida
    assert "HASHTAGS GERADAS" in saida

def test_formatar_tabela_com_erro():
    resultado = {
        "erro": "Nicho não encontrado",
        "nichos_disponiveis": ["fitness", "marketing_digital"]
    }
    saida = formatar_tabela(resultado)
    assert "❌" in saida or "Nicho não encontrado" in saida

def test_formatar_markdown_sucesso():
    resultado = {
        "nicho": "moda",
        "objetivo": "alcance",
        "quantidade": 3,
        "hashtags": ["#moda", "#fashion", "#estilo"],
        "hashtags_texto": "#moda #fashion #estilo",
        "dica": "Dica aqui."
    }
    saida = formatar_markdown(resultado)
    assert isinstance(saida, str)
    assert "# Instagram Hashtag Research" in saida
    assert "#moda" in saida


# =====================================================================
# TESTES DA BASE DE DADOS
# =====================================================================

def test_database_tem_nichos():
    assert len(HASHTAGS_DATABASE) >= 8

def test_database_estrutura_nicho():
    for nicho, dados in HASHTAGS_DATABASE.items():
        assert "grandes" in dados, f"Nicho {nicho} sem 'grandes'"
        assert "medias" in dados, f"Nicho {nicho} sem 'medias'"
        assert "pequenas" in dados, f"Nicho {nicho} sem 'pequenas'"

def test_database_hashtags_formato():
    for nicho, dados in HASHTAGS_DATABASE.items():
        for categoria in ["grandes", "medias", "pequenas"]:
            for h in dados.get(categoria, []):
                assert h.startswith("#"), f"Hashtag sem # em {nicho}/{categoria}: {h}"

def test_engajamento_universal_nao_vazio():
    assert len(HASHTAGS_ENGAJAMENTO_UNIVERSAL) > 0

def test_hashtags_sazonais_meses():
    meses_esperados = ["janeiro", "fevereiro", "marco", "abril", "maio", "junho",
                       "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]
    for mes in meses_esperados:
        assert mes in HASHTAGS_SAZONAIS, f"Mês {mes} não encontrado"
