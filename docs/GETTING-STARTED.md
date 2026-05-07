# Getting Started com Marketing OS

Guia prático: como instalar, primeiro briefing, e os 5 cenários mais comuns.

## Instalação rápida

No Claude Code (CLI ou Desktop):

```
/plugin marketplace add rilnermucio/Marketing-OS
/plugin install marketing-os@mos-marketplace
```

Pronto. O orquestrador é a skill `/marketing-os`, e os 18 subagents `mos-*` ficam disponíveis automaticamente.

## Conceito-chave: project-scoped memory

O Marketing OS aprende **por projeto**. Crie uma pasta dedicada pra cada cliente:

```bash
mkdir ~/Code/clientes/wellness-science
cd ~/Code/clientes/wellness-science
claude  # ou abre Claude Desktop nessa pasta
```

A primeira vez que você usar `mos-copy` (ou qualquer agent com memory) nessa pasta, ele salva briefing/feedback em `.claude/agent-memory/marketing-os-mos-copy/`. Próximas sessões na mesma pasta carregam esse contexto automaticamente.

**Regra prática:** uma pasta = um cliente / um projeto. Não misture trabalhos diferentes na mesma pasta.

## 5 cenários comuns

### Cenário 1 — Headlines pra produto novo (dispatch simples)

```
Você: /marketing-os escreve 5 headlines pra meu curso de Python pra devs juniores
```

**O que o orquestrador faz:**
- Reconhece "headlines" → trigger pro `mos-copy` (workflow #1, dispatch simples)
- Roda quality gates globais (sem travessão, sem "brutal", PT-BR correto)
- Entrega 5 headlines + 2-3 variações A/B + sugestões de teste

### Cenário 2 — Carrossel completo (dispatch composto)

```
Você: /marketing-os cria um carrossel sobre 7 erros de copy pra LinkedIn
```

**O que o orquestrador faz:**
- Reconhece "carrossel" → trigger pro **workflow #8** (composto)
- Dispara em paralelo: `mos-social` (estrutura) + `mos-copy` (texto dos slides) + `mos-design` (paleta + tipografia)
- Consolida outputs num pacote: estrutura + 7 slides com texto + design spec + caption + hashtags + sugestão de enquete obrigatória

### Cenário 3 — Página de aplicação BOFU (workflow estratégico)

```
Você: /marketing-os cria página de aplicação pra mentoria do Dr. Victor
       [anexa copy.pdf]
```

**O que o orquestrador faz:**
- Reconhece "página de aplicação" → trigger pro **workflow #5** (BOFU page)
- Carrega memory do cliente se existir (briefing, brand voice, regras)
- Dispara em paralelo:
  - `mos-funnel` analisa estrutura BOFU (CTA placement, escassez, anti-avatar, FAQ)
  - `mos-copy` revisa copy do PDF + aplica quality gates + gera variações
  - `mos-design` define direção visual (paleta médica premium, hierarquia)
- Consolida em brief único
- Se você pediu HTML/CSS de fato, **delega à skill `frontend-design`** com o brief completo
- Se pediu só specs, entrega o brief

### Cenário 4 — Lançamento de infoproduto (workflow longo)

```
Você: /marketing-os vou lançar um curso de IA pra empreendedores BR, ticket R$ 1.997
```

**O que o orquestrador faz:**
- Reconhece "lançar curso" → trigger pro **workflow #7** (lançamento de infoproduto)
- 4 fases:
  1. **Research:** `mos-research` valida mercado, concorrentes, ticket praticado
  2. **Estrutura + estratégia:** `mos-infoproduct` define módulos/pricing + `mos-launch` escolhe modelo (PLF/perpétuo/etc.) + `mos-funnel` desenha jornada
  3. **Execução:** `mos-copy` (sales page) + `mos-email` (sequência completa) + `mos-ads` (campanhas TOFU/MOFU/BOFU)
  4. **Quality gates** + sugestões de teste A/B

### Cenário 5 — Briefing vago (protocolo de pergunta)

```
Você: /marketing-os cria copy
```

**O que o orquestrador faz:**
- Detecta briefing vago → **NÃO chuta**
- Pergunta as 5 chaves de uma vez:
  1. Nicho? (saúde, finanças, tech, etc.)
  2. Avatar? (cargo, faixa de renda, dor)
  3. Ticket? (low/mid/high)
  4. Plataforma? (Instagram, LinkedIn, email, web)
  5. Urgência? (hoje, semana, futuro)
- Pula perguntas que já têm resposta no memory do projeto

## Compliance regulatório (importante)

Se você trabalha com nichos de **saúde / finanças / suplementos**, o plugin adiciona disclaimers obrigatórios automaticamente em qualquer peça final:

| Nicho | Órgão | Disclaimer aplicado |
|---|---|---|
| Médico / dental / nutrição | CFM/CRM, CONAR | "Resultados variam"; CRM visível; sem "cura" |
| Suplementos | ANVISA | "Auxilia/contribui" (não cura/trata) |
| Finanças / investimentos | CVM | "Rentabilidade passada não garante futura" |
| Cosméticos | ANVISA | Sem prometer tratar doença de pele |

Detecta automaticamente via memory do cliente, pasta atual, ou pergunta-chave #1 (nicho).

## Slash commands rápidos

Quando você sabe exatamente o que quer, use o command direto:

```
/criar-post Instagram sobre produtividade
/criar-carrossel 10 erros de copy
/criar-email sequência de boas-vindas
/criar-anuncio Meta Ads pra curso de Python
/criar-webinar lançamento do meu curso
```

Quando você prefere descrever em linguagem natural, use `/marketing-os` que ele orquestra:

```
/marketing-os tenho um curso novo de IA, preciso de pesquisa + tom de marca + headlines iniciais
```

Resultado é o mesmo — depende do quanto você quer ditar a invocação.

## Voice clones de copywriters lendários

Quando o briefing pede estilo específico:

```
/marketing-os escreve sales letter no estilo do Gary Halbert pra produto de finanças
```

O `mos-copy` carrega `assets/clones/halbert/` (profile, frameworks, voice, examples) e gera no estilo. 35 perfis disponíveis (Halbert, Hopkins, Kennedy, Ogilvy, Schwartz, Sugarman, Hormozi, GaryVee, MrBeast, Brunson, Cialdini, Codie Sanchez, Abdaal, Conrado, Joel Jota, etc.).

Pra clonar a SUA voz a partir de amostras locais (posts, emails, artigos seus):

```bash
# Coloca samples em workspace/voice-samples/
mkdir -p workspace/voice-samples
# Cola seus textos (cada arquivo = 1 amostra)

# Gera seu clone
/criar-meu-clone
```

## Próximos passos

- **Customizar pra seu nicho:** edite `references/niches.md` se trabalha com nicho fora dos 10 padrão
- **Criar workflows próprios:** `workflows/` tem 9 workflows end-to-end documentados como base
- **Avaliar performance:** `mos-analytics` ajuda a fechar o loop com métricas
- **Iterar:** memory automática melhora cada agent ao longo do tempo dentro de cada projeto

## Quando algo dá errado

Ver [TROUBLESHOOTING.md](./TROUBLESHOOTING.md) — cobre os bugs mais comuns de install/sync/dispatch que aprendemos no debug das v6.1.x.
