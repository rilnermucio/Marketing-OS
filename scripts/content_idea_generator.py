#!/usr/bin/env python3
"""
Content Idea Generator - Gera ideias de conteúdo baseado em pilares
Combina pilares de conteúdo + formatos + ângulos para criar ideias únicas.

Uso:
    python content_idea_generator.py [nicho] [quantidade]
    python content_idea_generator.py tecnologia 20
    python content_idea_generator.py marketing_digital 15
"""

import sys
import json
import random
from typing import List, Dict
from datetime import datetime

# Pilares de conteúdo por nicho
PILARES = {
    "tecnologia": {
        "pilares": ["IA e Automação", "Produtividade", "Ferramentas", "Carreira Tech", "Tendências"],
        "temas": [
            "ChatGPT", "Automação", "No-code", "Programação", "Apps",
            "Gadgets", "Cloud", "Segurança digital", "Trabalho remoto", "Startups"
        ],
        "problemas": [
            "perder tempo com tarefas repetitivas",
            "não saber usar ferramentas de IA",
            "ficar para trás na tecnologia",
            "não conseguir automatizar processos",
            "gastar muito com ferramentas"
        ]
    },
    "marketing_digital": {
        "pilares": ["Tráfego", "Conversão", "Conteúdo", "Branding", "Analytics"],
        "temas": [
            "Instagram", "Anúncios", "Copy", "SEO", "Email marketing",
            "Funil de vendas", "Landing pages", "Métricas", "Growth", "Leads"
        ],
        "problemas": [
            "não conseguir vender online",
            "ter baixo engajamento",
            "não saber criar conteúdo",
            "gastar muito em ads sem retorno",
            "não entender métricas"
        ]
    },
    "empreendedorismo": {
        "pilares": ["Vendas", "Gestão", "Mindset", "Finanças", "Escala"],
        "temas": [
            "Precificação", "Negociação", "Liderança", "Processos", "Fluxo de caixa",
            "Contratação", "Produtividade", "Networking", "Pitch", "Investimento"
        ],
        "problemas": [
            "não conseguir clientes",
            "não ter tempo para tudo",
            "dificuldade em precificar",
            "medo de empreender",
            "não saber delegar"
        ]
    },
    "desenvolvimento_pessoal": {
        "pilares": ["Mindset", "Hábitos", "Produtividade", "Relacionamentos", "Propósito"],
        "temas": [
            "Rotina matinal", "Foco", "Procrastinação", "Autoconhecimento", "Metas",
            "Meditação", "Leitura", "Comunicação", "Inteligência emocional", "Resiliência"
        ],
        "problemas": [
            "procrastinar demais",
            "não ter disciplina",
            "ansiedade e estresse",
            "falta de motivação",
            "não conseguir criar hábitos"
        ]
    },
    "financas": {
        "pilares": ["Organização", "Investimentos", "Renda Extra", "Mindset", "Planejamento"],
        "temas": [
            "Reserva de emergência", "Renda fixa", "Ações", "FIIs", "Criptomoedas",
            "Orçamento", "Dívidas", "Aposentadoria", "Renda passiva", "Educação financeira"
        ],
        "problemas": [
            "não sobrar dinheiro no fim do mês",
            "não saber investir",
            "ter muitas dívidas",
            "medo de investir",
            "não ter controle financeiro"
        ]
    },
}

# Formatos de conteúdo
FORMATOS = {
    "educativo": [
        "Tutorial passo a passo",
        "Guia completo de {tema}",
        "O que é {tema} e como funciona",
        "{numero} dicas de {tema}",
        "Como começar em {tema}",
        "Os fundamentos de {tema}",
    ],
    "lista": [
        "{numero} ferramentas de {tema}",
        "{numero} erros de {tema} para evitar",
        "{numero} hacks de {tema}",
        "Top {numero} {tema} para {ano}",
        "{numero} lições de {tema}",
        "{numero} mitos sobre {tema}",
    ],
    "comparativo": [
        "{tema} vs {tema2}: qual escolher?",
        "Antes e depois de usar {tema}",
        "{tema} em {ano} vs {ano2}",
        "Iniciante vs Expert em {tema}",
        "O que mudou em {tema}",
    ],
    "case": [
        "Como {resultado} com {tema}",
        "De {antes} para {depois} usando {tema}",
        "Minha jornada com {tema}",
        "O que aprendi em {tempo} de {tema}",
        "Case: {resultado} em {tempo}",
    ],
    "problema_solucao": [
        "Por que você não consegue {problema}",
        "O erro fatal em {tema}",
        "Como resolver {problema}",
        "Pare de fazer isso em {tema}",
        "A verdade sobre {problema}",
    ],
    "opiniao": [
        "Minha opinião sincera sobre {tema}",
        "Por que eu discordo sobre {tema}",
        "O que ninguém fala sobre {tema}",
        "Unpopular opinion: {tema}",
        "A verdade inconveniente sobre {tema}",
    ],
    "trending": [
        "Reagindo a {tema}",
        "Testando {tema} viral",
        "A trend de {tema} funciona?",
        "O que todo mundo está errando sobre {tema}",
        "Isso mudou tudo em {tema}",
    ],
}

# Ângulos/gatilhos
ANGULOS = [
    "para iniciantes",
    "em {tempo}",
    "sem gastar nada",
    "que ninguém ensina",
    "comprovado",
    "atualizado {ano}",
    "do zero ao avançado",
    "na prática",
    "com exemplos reais",
    "passo a passo",
]


def generate_ideas(nicho: str, quantidade: int = 20) -> Dict:
    """Gera ideias de conteúdo combinando pilares, formatos e ângulos."""

    if nicho not in PILARES:
        nicho = "tecnologia"

    nicho_data = PILARES[nicho]
    ideas = []
    ano = datetime.now().year

    for i in range(quantidade):
        # Selecionar elementos aleatórios
        pilar = random.choice(nicho_data["pilares"])
        tema = random.choice(nicho_data["temas"])
        tema2 = random.choice([t for t in nicho_data["temas"] if t != tema])
        problema = random.choice(nicho_data["problemas"])
        formato_tipo = random.choice(list(FORMATOS.keys()))
        formato_template = random.choice(FORMATOS[formato_tipo])
        angulo = random.choice(ANGULOS)

        # Substituir variáveis no template
        idea = formato_template.format(
            tema=tema,
            tema2=tema2,
            problema=problema,
            numero=random.choice([3, 5, 7, 10]),
            ano=ano,
            ano2=ano - 1,
            resultado="resultados incríveis",
            antes="iniciante",
            depois="expert",
            tempo=random.choice(["30 dias", "1 semana", "6 meses", "1 ano"]),
        )

        # Adicionar ângulo (50% das vezes)
        if random.random() > 0.5:
            angulo_formatado = angulo.format(
                tempo=random.choice(["7 dias", "30 dias", "24 horas"]),
                ano=ano
            )
            idea = f"{idea} ({angulo_formatado})"

        ideas.append({
            "idea": idea,
            "pilar": pilar,
            "tema_principal": tema,
            "formato": formato_tipo,
            "prioridade": random.choice(["alta", "média", "baixa"]),
        })

    # Organizar por pilar
    ideas_por_pilar = {}
    for idea in ideas:
        pilar = idea["pilar"]
        if pilar not in ideas_por_pilar:
            ideas_por_pilar[pilar] = []
        ideas_por_pilar[pilar].append(idea)

    return {
        "nicho": nicho,
        "pilares": nicho_data["pilares"],
        "total_ideias": len(ideas),
        "ideias": ideas,
        "ideias_por_pilar": ideas_por_pilar,
        "formatos_usados": list(set(i["formato"] for i in ideas)),
    }


def print_results(results: Dict):
    """Imprime os resultados formatados."""

    print("=" * 70)
    print(f"💡 CONTENT IDEA GENERATOR: {results['nicho'].upper()}")
    print("=" * 70)
    print()
    print(f"📊 Total de ideias: {results['total_ideias']}")
    print(f"📁 Pilares: {', '.join(results['pilares'])}")
    print()

    print("-" * 70)
    print("🎯 IDEIAS POR PILAR:")
    print("-" * 70)
    print()

    for pilar, ideias in results['ideias_por_pilar'].items():
        print(f"📌 {pilar.upper()}")
        for i, idea in enumerate(ideias, 1):
            prioridade_emoji = {"alta": "🔴", "média": "🟡", "baixa": "🟢"}[idea["prioridade"]]
            print(f"   {prioridade_emoji} {idea['idea']}")
            print(f"      └─ Formato: {idea['formato']} | Tema: {idea['tema_principal']}")
        print()

    print("-" * 70)
    print("📋 RESUMO:")
    print("-" * 70)
    print()

    # Contar por formato
    formato_count = {}
    for idea in results['ideias']:
        fmt = idea['formato']
        formato_count[fmt] = formato_count.get(fmt, 0) + 1

    print("Distribuição por formato:")
    for fmt, count in sorted(formato_count.items(), key=lambda x: -x[1]):
        bar = "█" * count
        print(f"   {fmt:20} {bar} ({count})")

    print()
    print("💡 PRÓXIMOS PASSOS:")
    print("   1. Selecione as ideias de alta prioridade")
    print("   2. Adapte para seu tom de voz")
    print("   3. Defina formatos (carrossel, reels, artigo)")
    print("   4. Adicione ao calendário editorial")
    print()
    print("=" * 70)


def main():
    if len(sys.argv) < 2:
        print("Uso: python content_idea_generator.py [nicho] [quantidade]")
        print()
        print("Nichos disponíveis:")
        for n in PILARES.keys():
            print(f"   • {n}")
        print()
        print("Exemplo: python content_idea_generator.py tecnologia 20")
        sys.exit(1)

    nicho = sys.argv[1]
    quantidade = int(sys.argv[2]) if len(sys.argv) > 2 else 20

    if nicho not in PILARES:
        print(f"⚠️  Nicho '{nicho}' não encontrado.")
        print(f"Nichos disponíveis: {', '.join(PILARES.keys())}")
        sys.exit(1)

    results = generate_ideas(nicho, quantidade)
    print_results(results)

    # Output JSON
    print()
    print("📄 JSON Output:")
    print(json.dumps(results, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
