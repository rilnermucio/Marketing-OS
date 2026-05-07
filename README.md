# Marketing OS

> Plugin Claude Code com **18 subagentes especializados** em marketing digital + 25 slash commands + 35 voice clones de copywriters lendários.

[![Version](https://img.shields.io/badge/version-6.3.0-blue.svg)](./CHANGELOG.md)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](./LICENSE)

## O que é

Marketing OS é um plugin para o [Claude Code](https://www.anthropic.com/claude-code) que orquestra 18 subagentes nativos especializados em domínios distintos do marketing digital. O plugin reivindica território explícito sobre briefings de marketing — quando você pede "cria página de aplicação" ou "monta um webinar", ele dispatcha os subagents corretos em paralelo, com camada estratégica antes de qualquer execução técnica.

**Conteúdo PT-BR otimizado para o mercado brasileiro.**

## Instalação

### Via marketplace (recomendado)

No Claude Code (CLI ou Desktop):

```
/plugin marketplace add rilnermucio/Marketing-OS
/plugin install marketing-os@mos-marketplace
```

Auto-update fica ligado por padrão — cada `git push` no repo vira atualização automática no startup da próxima sessão.

### Via clone local (desenvolvimento)

```bash
git clone https://github.com/rilnermucio/Marketing-OS.git "Marketing OS"
cd "Marketing OS"

# Deps Python pra rodar testes/validações
pip install -r requirements.txt

# Validar native agents
python scripts/validate_agents.py

# Tier 1 test suite
python -m pytest scripts/tests/ -v -m "not smoke"

# Carrega no Claude Code via --plugin-dir
claude --plugin-dir .
```

### Workspace pessoal (gitignored)

Crie sua área de trabalho local — não distribuída pelo plugin:

```bash
mkdir -p workspace/{drafts,outputs,brand,research,landing-pages,media}
```

## Os 18 subagentes nativos

Invocados pelo orquestrador (skill `/marketing-os`) ou diretamente via `@<agente>`:

| Agente | Domínio | Memory |
|---|---|---|
| `@mos-copy` | Copywriting persuasivo (headlines, CTAs, sales letters) | ✓ project |
| `@mos-seo` | Otimização de busca (keywords, on-page, E-E-A-T, AI-SEO) | — |
| `@mos-social` | Posts e estratégia em redes sociais (cross-platform) | ✓ project |
| `@mos-video` | Roteiros (YouTube, Reels, TikTok, VSL, Shorts) | — |
| `@mos-audio` | Podcasts, audiobooks, spots, sound design | — |
| `@mos-design` | Direção visual, paletas, tipografia, design specs | ✓ project |
| `@mos-ai-tools` | Prompts pra Midjourney, Flux, Runway, Sora, etc. | — |
| `@mos-analytics` | Métricas, KPIs, dashboards, GA4 | — |
| `@mos-email` | Email marketing (welcome, nurture, vendas, automação) | — |
| `@mos-ads` | Anúncios pagos (Meta, Google, TikTok, LinkedIn) | ✓ project |
| `@mos-research` | Trend spotting, audience research, validação | ✓ project |
| `@mos-brand` | Identidade de marca, arquétipos, manifesto | ✓ project |
| `@mos-storytelling` | Narrativa aplicada (hero's journey, StoryBrand) | — |
| `@mos-funnel` | Funis de conversão, jornada (TOFU/MOFU/BOFU) | ✓ project |
| `@mos-growth` | Growth hacking, AARRR, retention | — |
| `@mos-launch` | Lançamentos (PLF, semente, relâmpago, perpétuo) | ✓ project |
| `@mos-infoproduct` | Cursos, memberships, mentorias, ebooks | ✓ project |
| `@mos-ab-testing` | A/B/MVT, ICE prioritization, significância estatística |  — |

**Memory `project`:** 9 agents persistem contexto por projeto (briefing do cliente, feedback) em `.claude/agent-memory/marketing-os-<agent>/`. Recarregam automaticamente em sessões futuras na mesma pasta.

## Workflows orquestrados

10 padrões de orquestração documentados em [`skills/marketing-os/SKILL.md`](./skills/marketing-os/SKILL.md):

| # | Workflow | Agents disparados |
|---|---|---|
| 1 | Dispatch simples | 1 agent |
| 2 | Dispatch paralelo | múltiplos agents independentes |
| 3 | Dispatch sequencial | agents com dependência (ex: research → seo → copy) |
| 4 | Content pipeline | research+brand → seo/copy/social + design |
| 5 | **Página de aplicação / landing / vendas (BOFU)** | mos-funnel + mos-copy + mos-design → opt. handoff a `frontend-design` |
| 6 | **Webinar (live ou perpetual)** | launch + funnel + video → copy + email |
| 7 | **Lançamento de infoproduto** | research → infoproduct + launch + funnel → copy + email + ads |
| 8 | **Carrossel completo** | social + copy + design (+ ai-tools) |
| 9 | **VSL completa** | storytelling + copy + video |
| 10 | **Análise de concorrente + clone** | research + brand → copy (voice clone) |

Ver SKILL.md pra detalhes de cada workflow + "por que essa ordem importa".

## Slash commands rápidos

25 commands em `commands/` cobrindo workflows comuns. Quando você invoca direto (`/criar-carrossel`), segue lógica do command file. Quando pede em linguagem natural ("cria carrossel sobre X"), o orquestrador da skill dispatcha conforme tabela acima.

| Categoria | Commands |
|---|---|
| Conteúdo social | `/criar-post`, `/criar-carrossel`, `/criar-calendario` |
| Vídeo/áudio | `/criar-video`, `/criar-podcast` |
| Páginas/funis | `/criar-landing-page`, `/criar-funil`, `/criar-webinar` |
| Email | `/criar-email`, `/criar-sequencia` |
| Ads | `/criar-anuncio`, `/publicar-anuncio` |
| Infoproduto | `/criar-infoproduto` |
| Voice clones | `/criar-clone` (expert externo), `/criar-meu-clone` (suas amostras) |
| Análise | `/analisar-concorrencia`, `/analisar-video`, `/clonar-estrategia` |
| Visual | `/criar-brief-design`, `/gerar-imagem`, `/capturar-tela` |
| Operação | `/campanha`, `/batch`, `/criar-artigo`, `/publicar-notion` |

## Estrutura

```
Marketing OS/
├── .claude-plugin/         # plugin.json + marketplace.json
├── agents/                 # 18 native subagents (mos-*.md)
├── skills/marketing-os/    # Skill entrypoint (SKILL.md = orquestrador)
├── subagents/              # Tier 2 knowledge bases (~3500 linhas cada)
├── commands/               # 25 slash commands
├── workflows/              # 9 workflows end-to-end documentados
├── assets/                 # Frameworks, personas, prompts, swipe files,
│   ├── clones/             #   templates, 35 voice clones
│   ├── frameworks/
│   ├── personas/
│   ├── prompts/
│   ├── swipe-files/
│   └── templates/
├── references/             # Guias técnicos por domínio
├── scripts/                # 29 ferramentas Python + Tier 1 tests
│   ├── hooks/              # Quality gate hook (PreToolUse)
│   └── tests/              # Suite pytest
├── docs/                   # Documentação técnica
│   ├── GETTING-STARTED.md  # Começo rápido
│   ├── TROUBLESHOOTING.md  # Bugs comuns
│   └── ARCHITECTURE.md     # Arquitetura two-tier
└── workspace/              # Área pessoal (gitignored)
```

## Voice clones (35 perfis em `assets/clones/`)

Copywriters/marketers lendários referenciados pelo `mos-copy` quando o briefing pede estilo específico:

Halbert, Hopkins, Kennedy, Ogilvy, Schwartz, Sugarman, Caples, Cialdini, Brunson, Hormozi, Leila Hormozi, GaryVee, MrBeast, Codie Sanchez, Abdaal, Abraham, Joel Jota, Conrado, Mel Robbins, Patel, Provost, Rachitsky, Suby, Welsh, Cole, Collier, Ellis, Ezra Firestone, Flavio Augusto, Gadzhi, Godin, Howell, Chen, Miller.

Cada um com `profile.md`, `frameworks.md`, `voice.md`, `examples.md`.

## Desenvolvimento

Ver [`AGENTS.md`](./AGENTS.md) pra guia completo de desenvolvimento (arquitetura, dispatch protocol, plugin distribution gotchas, quality gates). `CLAUDE.md` é shim que importa AGENTS.md — Claude Code lê automaticamente.

```bash
# Tier 1 test suite (estática, rápida — sem Claude Code login)
python -m pytest scripts/tests/ -v -m "not smoke"

# Validar native agents (frontmatter, knowledge base refs)
python scripts/validate_agents.py

# Validar plugin manifest
claude plugin validate .

# CLI unificado das ferramentas
python scripts/mos.py --help
```

CI rodando em `.github/workflows/tests.yml` (922 testes Tier 1 + cobertura ≥70%).

## Documentação adicional

- **[docs/GETTING-STARTED.md](./docs/GETTING-STARTED.md)** — primeiros passos com 5 exemplos de briefings
- **[docs/TROUBLESHOOTING.md](./docs/TROUBLESHOOTING.md)** — problemas comuns de install/configuração e como resolver
- **[docs/ARCHITECTURE.md](./docs/ARCHITECTURE.md)** — arquitetura two-tier (system prompts enxutos + knowledge bases profundas)
- **[CHANGELOG.md](./CHANGELOG.md)** — histórico completo de releases
- **[AGENTS.md](./AGENTS.md)** — guia canônico pra contributors / agentes de IA

## Licença

MIT — ver [LICENSE](./LICENSE).
