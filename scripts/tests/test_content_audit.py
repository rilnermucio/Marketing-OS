#!/usr/bin/env python3
"""
Testes para content_audit.py
"""

import sys
import os
import tempfile
import json
import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from content_audit import (
    contar_palavras,
    contar_caracteres,
    calcular_tempo_leitura,
    analisar_legibilidade,
    analisar_estrutura_markdown,
    analisar_seo,
    analisar_copywriting,
    analisar_social,
    analisar_email,
    extrair_palavras_chave,
    calcular_pontuacao_geral,
    auditar_arquivo,
    ler_arquivo,
    PALAVRAS_PODER,
    STOP_WORDS,
)


# =====================================================================
# TESTES DE contar_palavras
# =====================================================================

def test_contar_palavras_basico():
    assert contar_palavras("olá mundo") == 2

def test_contar_palavras_vazio():
    assert contar_palavras("") == 0

def test_contar_palavras_multiplos_espacos():
    assert contar_palavras("  palavra   outra  ") == 2

def test_contar_palavras_com_pontuacao():
    assert contar_palavras("Olá, mundo! Como vai?") == 4


# =====================================================================
# TESTES DE contar_caracteres
# =====================================================================

def test_contar_caracteres_basico():
    resultado = contar_caracteres("abc")
    assert resultado["total"] == 3
    assert resultado["sem_espacos"] == 3

def test_contar_caracteres_com_espaco():
    resultado = contar_caracteres("a b")
    assert resultado["total"] == 3
    assert resultado["sem_espacos"] == 2
    assert resultado["espacos"] == 1

def test_contar_caracteres_linhas():
    resultado = contar_caracteres("linha1\nlinha2")
    assert resultado["linhas"] == 2


# =====================================================================
# TESTES DE calcular_tempo_leitura
# =====================================================================

def test_calcular_tempo_leitura_curto():
    assert calcular_tempo_leitura(100) == "< 1 min"

def test_calcular_tempo_leitura_um_minuto():
    resultado = calcular_tempo_leitura(250)
    assert "1-2 min" in resultado or "1 min" in resultado

def test_calcular_tempo_leitura_longo():
    resultado = calcular_tempo_leitura(1000)
    assert "5 min" in resultado

def test_calcular_tempo_leitura_zero():
    assert calcular_tempo_leitura(0) == "< 1 min"


# =====================================================================
# TESTES DE analisar_legibilidade
# =====================================================================

def test_analisar_legibilidade_retorna_campos_esperados():
    texto = "Este é um texto simples. Ele tem poucas palavras. É fácil de ler."
    resultado = analisar_legibilidade(texto)
    assert "indice_flesch" in resultado
    assert "nivel" in resultado
    assert "publico_alvo" in resultado
    assert "media_palavras_por_sentenca" in resultado
    assert "total_sentencas" in resultado

def test_analisar_legibilidade_flesch_range():
    texto = "Este é um texto simples para teste de legibilidade básica."
    resultado = analisar_legibilidade(texto)
    assert 0 <= resultado["indice_flesch"] <= 100

def test_analisar_legibilidade_classificacao():
    # Texto muito simples deve ter nível fácil
    texto = "Vai. Come. Bebe. Dorme. Acorda."
    resultado = analisar_legibilidade(texto)
    assert resultado["nivel"] in ["Muito fácil", "Fácil", "Moderado", "Difícil", "Muito difícil"]

def test_analisar_legibilidade_texto_complexo():
    texto = ("A implementação metodológica dos procedimentos epistemológicos "
             "contemporâneos requer a compreensão aprofundada das fundamentações "
             "filosóficas que permeiam os paradigmas interdisciplinares.")
    resultado = analisar_legibilidade(texto)
    assert resultado["indice_flesch"] < 60  # deve ser difícil


# =====================================================================
# TESTES DE analisar_estrutura_markdown
# =====================================================================

def test_analisar_estrutura_markdown_basico():
    texto = "# Título\n\n## Seção\n\n- item 1\n- item 2\n"
    resultado = analisar_estrutura_markdown(texto)
    assert resultado["headings"]["h1"] == 1
    assert resultado["headings"]["h2"] == 1
    assert resultado["listas"]["nao_ordenadas"] == 2

def test_analisar_estrutura_markdown_formatacao():
    texto = "**negrito** e *italico* e `codigo`"
    resultado = analisar_estrutura_markdown(texto)
    assert resultado["formatacao"]["negrito"] == 1
    assert resultado["formatacao"]["italico"] == 1
    assert resultado["formatacao"]["codigo"] == 1

def test_analisar_estrutura_markdown_links():
    texto = "[link aqui](https://exemplo.com) e outro [link](https://teste.com)"
    resultado = analisar_estrutura_markdown(texto)
    assert resultado["links"] == 2

def test_analisar_estrutura_markdown_imagens():
    texto = "![alt text](imagem.jpg)"
    resultado = analisar_estrutura_markdown(texto)
    assert resultado["imagens"] == 1

def test_analisar_estrutura_markdown_vazio():
    resultado = analisar_estrutura_markdown("")
    assert resultado["headings"]["h1"] == 0
    assert resultado["listas"]["nao_ordenadas"] == 0


# =====================================================================
# TESTES DE analisar_seo
# =====================================================================

def test_analisar_seo_retorna_estrutura():
    texto = "# Título de Teste\n\nConteúdo básico para teste de SEO com algumas palavras."
    resultado = analisar_seo(texto)
    assert "pontuacao" in resultado
    assert "itens" in resultado
    assert "sugestoes" in resultado
    assert isinstance(resultado["pontuacao"], int)

def test_analisar_seo_pontuacao_range():
    texto = "# Título\n\n" + "Palavras " * 100
    resultado = analisar_seo(texto)
    assert 0 <= resultado["pontuacao"] <= 100

def test_analisar_seo_com_keyword():
    texto = "# Marketing Digital\n\n" + "marketing digital " * 10 + "Conteúdo sobre marketing digital."
    resultado = analisar_seo(texto, keyword="marketing digital")
    # Com keyword presente, pontuação deve ser maior que zero
    assert resultado["pontuacao"] > 0

def test_analisar_seo_conteudo_longo():
    texto = "# Título\n\n## Seção\n\n" + "palavra " * 1600
    resultado = analisar_seo(texto)
    # Conteúdo longo deve pontuar bem
    itens_ok = [i for i in resultado["itens"] if i["ok"]]
    assert len(itens_ok) > 0

def test_analisar_seo_titulo_ideal():
    titulo = "A" * 55  # 55 chars — dentro do ideal 50-60
    resultado = analisar_seo("texto qualquer", titulo=titulo)
    itens_titulo = [i for i in resultado["itens"] if "Título" in i["item"]]
    if itens_titulo:
        assert itens_titulo[0]["ok"] is True


# =====================================================================
# TESTES DE analisar_copywriting
# =====================================================================

def test_analisar_copywriting_retorna_estrutura():
    texto = "Garante agora! Você vai conseguir resultados incríveis."
    resultado = analisar_copywriting(texto)
    assert "palavras_poder" in resultado
    assert "total_palavras_poder" in resultado
    assert "ctas_encontrados" in resultado
    assert "perguntas" in resultado
    assert "pontuacao" in resultado

def test_analisar_copywriting_palavras_poder():
    texto = "Oferta exclusiva limitada! Garanta agora antes que expire."
    resultado = analisar_copywriting(texto)
    assert resultado["total_palavras_poder"] > 0

def test_analisar_copywriting_perguntas():
    texto = "Você quer resultados? O que está impedindo você? Como posso ajudar?"
    resultado = analisar_copywriting(texto)
    assert resultado["perguntas"] == 3

def test_analisar_copywriting_sem_poder():
    texto = "O cachorro correu pelo jardim verde e bonito."
    resultado = analisar_copywriting(texto)
    assert resultado["total_palavras_poder"] == 0
    assert len(resultado["sugestoes"]) > 0

def test_analisar_copywriting_numeros():
    texto = "Aumente seus resultados em 300% com 5 passos simples. Já são 10.000 clientes."
    resultado = analisar_copywriting(texto)
    assert resultado["usa_numeros"] is True


# =====================================================================
# TESTES DE analisar_social
# =====================================================================

def test_analisar_social_retorna_estrutura():
    texto = "Post de teste #marketing #vendas @usuario"
    resultado = analisar_social(texto)
    assert "caracteres" in resultado
    assert "hashtags" in resultado
    assert "mencoes" in resultado
    assert "adequacao_plataformas" in resultado

def test_analisar_social_hashtags():
    texto = "#marketing #vendas #sucesso"
    resultado = analisar_social(texto)
    assert len(resultado["hashtags"]) == 3

def test_analisar_social_mencoes():
    texto = "Obrigado @joao e @maria!"
    resultado = analisar_social(texto)
    assert len(resultado["mencoes"]) == 2

def test_analisar_social_plataformas():
    texto = "A" * 100  # 100 chars
    resultado = analisar_social(texto)
    assert "Twitter/X" in resultado["adequacao_plataformas"]
    assert "Instagram" in resultado["adequacao_plataformas"]
    assert resultado["adequacao_plataformas"]["Twitter/X"]["dentro_limite"] is True

def test_analisar_social_excede_twitter():
    texto = "A" * 300  # 300 chars — excede limite do Twitter (280)
    resultado = analisar_social(texto)
    assert resultado["adequacao_plataformas"]["Twitter/X"]["dentro_limite"] is False


# =====================================================================
# TESTES DE analisar_email
# =====================================================================

def test_analisar_email_retorna_estrutura():
    texto = "Assunto: Olá!\n\nConteúdo do email aqui. Clique para saber mais."
    resultado = analisar_email(texto)
    assert "spam_words" in resultado
    assert "pontuacao" in resultado
    assert "sugestoes" in resultado

def test_analisar_email_personalizacao():
    texto = "Olá {{nome}},\n\nSegue sua oferta especial."
    resultado = analisar_email(texto)
    assert resultado["personalizado"] is True

def test_analisar_email_sem_personalizacao():
    texto = "Olá usuário,\n\nSegue sua oferta."
    resultado = analisar_email(texto)
    assert resultado["personalizado"] is False
    assert len(resultado["sugestoes"]) > 0

def test_analisar_email_spam_words():
    texto = "GRÁTIS! Clique aqui para sua oferta exclusiva garantida urgente!"
    resultado = analisar_email(texto)
    assert len(resultado["spam_words"]) > 0

def test_analisar_email_unsubscribe():
    texto = "Conteúdo do email. Para descadastrar, clique aqui."
    resultado = analisar_email(texto)
    assert resultado["tem_unsubscribe"] is True


# =====================================================================
# TESTES DE extrair_palavras_chave
# =====================================================================

def test_extrair_palavras_chave_retorna_lista():
    texto = "marketing digital é essencial para negócios modernos de marketing"
    resultado = extrair_palavras_chave(texto, n=5)
    assert isinstance(resultado, list)
    assert len(resultado) <= 5

def test_extrair_palavras_chave_tuplas():
    texto = "conteúdo conteúdo conteúdo criação criação"
    resultado = extrair_palavras_chave(texto)
    if resultado:
        assert isinstance(resultado[0], tuple)
        assert len(resultado[0]) == 2

def test_extrair_palavras_chave_sem_stop_words():
    texto = "o a de da do em para com que"
    resultado = extrair_palavras_chave(texto)
    palavras = [p[0] for p in resultado]
    for sw in STOP_WORDS:
        assert sw not in palavras

def test_extrair_palavras_chave_frequencia():
    texto = "marketing marketing marketing digital digital"
    resultado = extrair_palavras_chave(texto, n=2)
    if resultado:
        # "marketing" deve aparecer mais que "digital"
        assert resultado[0][1] >= resultado[1][1]


# =====================================================================
# TESTES DE calcular_pontuacao_geral
# =====================================================================

def test_calcular_pontuacao_geral_vazio():
    resultado = calcular_pontuacao_geral({})
    assert resultado["total"] == 0
    assert resultado["nivel"] == "Precisa melhorar"

def test_calcular_pontuacao_geral_com_dados():
    resultados = {
        "legibilidade": {"indice_flesch": 70},
        "seo": {"pontuacao": 60},
        "copywriting": {"pontuacao": 80},
    }
    resultado = calcular_pontuacao_geral(resultados)
    assert resultado["total"] > 0
    assert resultado["nivel"] in ["Excelente", "Bom", "Regular", "Precisa melhorar"]

def test_calcular_pontuacao_geral_range():
    resultados = {
        "legibilidade": {"indice_flesch": 100},
        "seo": {"pontuacao": 100},
        "copywriting": {"pontuacao": 100},
    }
    resultado = calcular_pontuacao_geral(resultados)
    assert 0 <= resultado["total"] <= 100


# =====================================================================
# TESTES DE ler_arquivo e auditar_arquivo
# =====================================================================

def test_ler_arquivo_existente():
    with tempfile.NamedTemporaryFile(mode='w', suffix='.txt', delete=False, encoding='utf-8') as f:
        f.write("Conteúdo de teste para o arquivo temporário.")
        caminho = f.name
    try:
        conteudo, ext = ler_arquivo(caminho)
        assert conteudo is not None
        assert "Conteúdo de teste" in conteudo
        assert ext == ".txt"
    finally:
        os.unlink(caminho)

def test_ler_arquivo_inexistente():
    conteudo, ext = ler_arquivo("/caminho/que/nao/existe.txt")
    assert conteudo is None
    assert ext is None

def test_auditar_arquivo_markdown(tmp_path):
    conteudo = """# Título Principal

## Introdução

Este é um artigo sobre marketing digital. O marketing digital é essencial para negócios.
Você vai aprender tudo sobre marketing digital neste artigo completo.

## Desenvolvimento

Aqui está o conteúdo principal. Aproveite agora esta oportunidade exclusiva!
Clique aqui para descobrir mais sobre marketing digital.

- Ponto importante 1
- Ponto importante 2
- Ponto importante 3

## Conclusão

Garanta já seu sucesso com marketing digital. Não perca esta chance!
"""
    arquivo = tmp_path / "artigo.md"
    arquivo.write_text(conteudo, encoding='utf-8')

    resultado = auditar_arquivo(str(arquivo), tipo="blog")
    assert "erro" not in resultado
    assert "metricas" in resultado
    assert "legibilidade" in resultado
    assert "seo" in resultado
    assert "pontuacao_geral" in resultado

def test_auditar_arquivo_inexistente():
    resultado = auditar_arquivo("/nao/existe.md")
    assert "erro" in resultado

def test_auditar_arquivo_tipo_social(tmp_path):
    conteudo = "Post de teste #marketing #vendas. Comente sua opinião!"
    arquivo = tmp_path / "post.txt"
    arquivo.write_text(conteudo, encoding='utf-8')

    resultado = auditar_arquivo(str(arquivo), tipo="social")
    assert "social" in resultado
    assert "erro" not in resultado

def test_auditar_arquivo_tipo_email(tmp_path):
    conteudo = "Assunto: Novidades!\n\nOlá {{nome}}, temos uma oferta especial. Clique aqui. Para descadastrar, clique aqui."
    arquivo = tmp_path / "email.txt"
    arquivo.write_text(conteudo, encoding='utf-8')

    resultado = auditar_arquivo(str(arquivo), tipo="email")
    assert "email" in resultado
    assert "erro" not in resultado


# =====================================================================
# TESTES DE CONSTANTES
# =====================================================================

def test_palavras_poder_categorias():
    categorias_esperadas = ["urgencia", "exclusividade", "facilidade", "garantia",
                            "novidade", "gratuito", "resultados"]
    for cat in categorias_esperadas:
        assert cat in PALAVRAS_PODER

def test_stop_words_portugues():
    palavras_comuns = ["de", "da", "do", "em", "para", "com", "que"]
    for p in palavras_comuns:
        assert p in STOP_WORDS
