# Marketing OS — Plugin-First Refactor (Design)

**Date:** 2026-05-06
**Status:** Draft (awaiting user review)
**Author:** Claude Opus 4.7 (1M) via brainstorming skill, with rilner

---

## Context

O Marketing OS hoje é um projeto que cresceu por sedimentação: começou (presumivelmente) como um plugin Claude Code com 18 subagentes de marketing, mas absorveu por cima um meta-framework de desenvolvimento de software (Synkra AIOS) com workflows formais de Story-Driven Development, IDS gates, agent authority matrix, integração CodeRabbit, conceito de "squads", e configurações para Codex CLI e Antigravity IDE — nenhum dos quais o autor usa de fato no dia-a-dia.

O resultado é um repo com:

- **4 cópias** de "marketing-os" em subpastas distintas (`marketing-os/`, `skill-package/marketing-os/`, `skills/marketing-os/`, `squads/marketing-os/`)
- **2 SKILL.md** divergentes (`skills/` 10489 bytes, `skill-package/` 11270 bytes)
- **Root poluído** com 5+ arquivos de conteúdo pessoal (`carrossel-instagram-*.md`, `Roteiro_Reels_*.md`, `vertice-logo.svg`, etc) misturados com manifesto do plugin
- **AIOS framework dormante** (`.aios/`, `.aios-core/`, `squads/`, `.codex/`, `.antigravity/`, regras AIOS em `.claude/rules/`)
- **Versões dessincronizadas** (`plugin.json` v5.1.0 vs `package.json` v5.0.0)
- **Mistura Python+Node** sem critério (Python pra `validate_agents.py` e tests; Node só pra `ajv` JSON schema validator)
- **AGENTS.md AIOS-flavored** apontando pra Codex CLI (não usado)

### Perfil de uso (constraints declarados)

| Constraint | Valor |
|---|---|
| Quem usa hoje | Só o autor, localmente |
| Pode quebrar tudo | Sim |
| Sistemas em uso real | Apenas Marketing (18 subagentes); AIOS é dead code |
| Prioridades | (1) eliminar duplicação + root limpo; (2) desacoplar pra evoluir sem quebrar |
| Subscription disponível | Claude Max (permite usar `claude -p` em testes sem custo extra) |

---

## Goals

1. **Plugin-first identity:** o repo passa a ser inequivocamente um Claude Code plugin distribuível (`marketing-os` v5.1.0), não um híbrido plugin+framework.
2. **Single source of truth:** uma cópia só de cada recurso (assets, references, scripts, subagents, workflows). Zero duplicação.
3. **Plugin↔Workspace boundary:** separação clara entre o que é o plugin (versionado, distribuível) e o que é o workspace pessoal (gitignored).
4. **Decapitação do AIOS:** remoção do framework dormante e seus rastros (configs, regras, AGENTS.md, Codex/Antigravity).
5. **Verificabilidade:** testes automatizados (estáticos + smoke) confirmam que o plugin permanece funcional após cada fase.
6. **Reduzir surface cognitiva:** `tree -L 1` cabe em uma tela; `du -sh .` reduz pelo menos 30%.

## Non-goals

- Reescrever a lógica/qualidade dos 18 subagentes de marketing
- Adicionar novos agentes ou workflows
- Migrar Python → TypeScript (ou vice-versa)
- Otimizar performance dos agentes
- Criar suite de testes funcionais que avaliem qualidade subjetiva do output dos agentes
- Publicar o plugin no marketplace público (preparação só, não execução)

---

## Section 1 — Target Architecture

### Layout final

```
Marketing OS/
├── .claude-plugin/              # manifesto Claude (mantém)
├── plugin.json                  # v5.1.0 (mantém, sincronizado com package.json se mantido)
├── README.md                    # reescrito, focado no plugin
├── CHANGELOG.md                 # mantém
├── LICENSE
├── CONTRIBUTING.md              # mantém
├── .gitignore                   # atualizado (workspace/, caches, secrets)
├── .mcp.json                    # config MCP do plugin
├── .env.example                 # exemplo público de .env
│
├── skills/marketing-os/         # ÚNICA skill (canônica)
│   ├── SKILL.md                 # entrypoint
│   ├── assets -> ../../assets   # symlinks internos (resolução de path, não dup)
│   ├── references -> ../../references
│   ├── scripts -> ../../scripts
│   ├── subagents -> ../../subagents
│   └── workflows -> ../../workflows
│
├── subagents/                   # 18 agentes de marketing (single source no root)
├── commands/                    # slash commands
├── workflows/                   # workflows de criação de conteúdo
├── assets/                      # checklists, frameworks, personas, prompts, swipe-files, templates
├── references/                  # ads-copy.md, blog-seo.md, social-media.md, etc + design/
├── scripts/                     # tooling (validate_agents.py, etc)
│   └── tests/                   # pytest tests
├── docs/                        # documentação do plugin (sem AIOS)
│   ├── architecture/
│   ├── guides/
│   └── superpowers/specs/       # specs deste e futuros refactors
├── .claude/                     # config Claude Code do projeto
│   ├── CLAUDE.md                # reescrito enxuto (~40 linhas)
│   └── rules/                   # zero ou um só arquivo com bits salváveis do mcp-usage.md
│
└── workspace/                   # 🆕 ESPAÇO LOCAL (gitignored)
    ├── outputs/
    ├── drafts/
    ├── brand/
    ├── research/
    ├── landing-pages/
    └── media/
```

### Princípio de fronteira

> "Se outra pessoa clonar esse repo e instalar como plugin Claude Code, isso deve estar lá? Sim → plugin. Não, é meu trabalho/conteúdo → workspace (gitignored)."

---

## Section 2 — Migration Plan (Phased)

5 fases sequenciais. Cada fase termina com: commit + verificação Tier 1 (e Tier 2 nas fases 2 e 3 + 5). Rollback: `git reset --hard HEAD~1`.

### Phase 0 — Safety Net (~5 min)

- [ ] Criar branch `refactor/plugin-first` a partir de `main`
- [ ] Commit das modificações não-commitadas atuais (2 modificados, 8 untracked) numa baseline isolada
- [ ] Capturar baseline: `tree -L 2 > /tmp/before-tree.txt`, `du -sh */ > /tmp/before-du.txt`
- [ ] Ler `scripts/validate_agents.py` (untracked) e entender o que valida
- [ ] **Tier 2 baseline:** rodar smoke tests via `claude -p` em 5 agentes representativos, salvar outputs em `tests/snapshots/baseline/`

**Checkpoint:** branch criada, baseline capturada.

### Phase 1 — Extract Personal Workspace (low-risk, reversible)

- [ ] Criar `workspace/{outputs,drafts,brand,research,landing-pages,media}/.gitkeep`
- [ ] `git mv` dos artefatos:
  - `carrossel-instagram-*.md`, `Roteiro_Reels_*.md`, `Roteiro_Video_*.md` → `workspace/drafts/`
  - `vertice-logo.svg`, `vertice-symbol.png` → `workspace/brand/`
  - `outputs/`, `output/` (se existir singular) → `workspace/outputs/`
  - `research/` (root) → `workspace/research/`
  - `landing-pages/` (root) → `workspace/landing-pages/`
  - `media/` (root) → `workspace/media/`
- [ ] Atualizar `.gitignore`: adicionar `workspace/` com exceção de `.gitkeep`
- [ ] Verificar `grep -r "carrossel-instagram\|Roteiro_Reels\|vertice-logo\|landing-pages/copy" subagents/ workflows/ skills/ commands/` retorna **vazio**
- [ ] Rodar Tier 1: `pytest scripts/tests/ -v`
- [ ] Commit: `chore: extract personal content to workspace/`

**Checkpoint:** root limpo de artefatos pessoais, plugin intacto.

### Phase 2 — Consolidate marketing-os (deduplication)

- [ ] Diff `skills/marketing-os/SKILL.md` vs `skill-package/marketing-os/SKILL.md` — identificar conteúdo único de cada
- [ ] Fundir conteúdo útil em `skills/marketing-os/SKILL.md` (canônico, referenciado em `plugin.json`)
- [ ] **Symlinks em `skills/marketing-os/`:** mantidos. Não são duplicação — são resolução de path do plugin. Single source of truth = root. `skills/marketing-os/{assets,references,scripts,subagents,workflows}` permanecem como symlinks pra `../../{...}/`. Os symlinks dangling (que apontavam pra `marketing-os/` deletado, ou outros paths quebrados) são removidos. **Verificar na Phase 0** o que outros plugins Claude Code oficiais fazem (symlinks vs conteúdo direto vs paths relativos em SKILL.md) e ajustar se padrão da plataforma for outro
- [ ] Deletar `marketing-os/` (root, redundante com symlinks)
- [ ] Deletar `skill-package/`
- [ ] Deletar `skills/marketing-os/SKILL.md.pre-migration.backup`
- [ ] Verificar `find . -xtype l 2>/dev/null` retorna **vazio** (zero symlinks dangling — symlinks válidos pra root continuam existindo)
- [ ] Rodar Tier 1: `pytest scripts/tests/ -v`
- [ ] Rodar Tier 2: smoke tests, comparar com baseline
- [ ] Commit: `refactor: consolidate marketing-os into single canonical skill`

**Checkpoint:** uma cópia só de cada recurso, plugin funcional.

### Phase 3 — Decapitate AIOS (largest demolition)

- [ ] Remover diretórios:
  - `.aios/`
  - `.aios-core/`
  - `.antigravity/`
  - `.codex/`
  - `squads/`
- [ ] Remover arquivos:
  - `.aios-installation-config.yaml`
  - `.aios-pm-config.yaml`
  - `AGENTS.md` (AIOS-framed)
- [ ] Remover regras AIOS de `.claude/rules/`:
  - `workflow-execution.md`
  - `story-lifecycle.md`
  - `ids-principles.md`
  - `agent-authority.md`
  - `coderabbit-integration.md`
- [ ] Reescrever `.claude/CLAUDE.md` enxuto (~40 linhas): identidade do plugin, convenções, "não fazer push sem confirmar", referência a docs/
- [ ] Avaliar `.claude/rules/mcp-usage.md`: extrair bits úteis sobre Playwright/MCP pra um arquivo final (`.claude/rules/mcp-conventions.md`) ou fundir em `CLAUDE.md`; deletar original
- [ ] Verificar `grep -ri "aios\|@aios-master\|@architect\|story-driven\|IDS gate" --include="*.md" --include="*.yaml" --include="*.json" .` (excluindo CHANGELOG.md) retorna **vazio**
- [ ] Rodar Tier 1: `pytest scripts/tests/ -v`
- [ ] Rodar Tier 2: smoke tests, comparar com baseline
- [ ] Commit: `refactor: remove dormant AIOS framework`

**Checkpoint:** AIOS extirpado, plugin permanece funcional.

### Phase 4 — Polish

- [ ] Reescrever `README.md` (de 29 KB AIOS-flavored → ~5 KB focado): o que é, como instalar, lista 1-line dos 18 agentes, link pra docs/
- [ ] Decidir destino de `package.json` + `node_modules/`:
  - `grep -r "ajv" scripts/ subagents/` antes
  - Se `ajv` é usado: sincronizar `package.json` v5.0.0 → v5.1.0; manter
  - Se não usado: deletar `package.json` e `node_modules/`
- [ ] Decidir destino de `requirements.txt`/`pytest.ini`/`.pytest_cache/`:
  - Se Python só pra `scripts/validate_agents.py` e nossos testes novos → manter
  - Senão limpar
- [ ] Avaliar `GUIA-DE-USO.md` e `INSTALACAO-SKILL.md`:
  - Comparar com `README.md` reescrito
  - Se >80% redundantes → deletar, migrar bits únicos
  - Senão mover pra `docs/guides/`
- [ ] Limpar arquivos órfãos: `.DS_Store` (todos), `.env.backup.*`
- [ ] Atualizar `.gitignore` final (workspace/, caches, secrets, backups)
- [ ] Verificar `du -sh .` reduziu pelo menos 30% comparado ao baseline
- [ ] Verificar `tree -L 1 .` cabe em ~20 linhas
- [ ] Commit: `chore: polish plugin metadata and docs`

**Checkpoint:** plugin enxuto e auto-explicativo.

### Phase 5 — Functional Verification

- [ ] Rodar Tier 1 completo: `pytest scripts/tests/ -v`
- [ ] Rodar Tier 2 completo: smoke tests em todos os 5-6 agentes representativos via `claude -p`, comparar com baseline (Phase 0)
- [ ] Verificação manual: instalar plugin no Claude Code local, ativar 2-3 agentes diferentes, pedir tarefa simples, validar resposta sensata
- [ ] Documentar resultado no `CHANGELOG.md`
- [ ] Verificar critérios "pronto" (ver Section 5)
- [ ] Commit final: `chore: verify plugin functional after refactor`
- [ ] Merge `refactor/plugin-first` → `main` (squash ou rebase, decisão do autor)

**Checkpoint:** plugin verificadamente funcional, refactor concluído.

---

## Section 3 — Plugin↔Workspace Boundary

### Plugin (versionado, distribuído)

| Pasta/arquivo | Razão |
|---|---|
| `skills/marketing-os/` | A skill em si |
| `subagents/` | Definição dos 18 agentes |
| `commands/` | Slash commands |
| `workflows/` | Workflows reutilizáveis |
| `assets/` | Checklists, frameworks, personas, prompts, swipe-files, templates — material que os agentes carregam |
| `references/` | Guias técnicos (ads-copy, blog-seo, social-media, strategy, design, ux-writing) |
| `scripts/` | Tooling (validate_agents.py, tests) |
| `docs/` | Documentação do plugin |
| `.claude/` | Config Claude Code do projeto (rules + CLAUDE.md) |
| `plugin.json`, `.claude-plugin/`, `.mcp.json` | Manifesto e config do plugin |
| `README.md`, `LICENSE`, `CHANGELOG.md`, `CONTRIBUTING.md`, `.gitignore`, `.env.example` | Raiz padrão |

### Workspace (`workspace/`, gitignored)

| Pasta destino | Origem | Razão |
|---|---|---|
| `workspace/drafts/` | `carrossel-instagram-*.md`, `Roteiro_Reels_*.md`, `Roteiro_Video_*.md` | Rascunhos pessoais, não exemplos genéricos |
| `workspace/brand/` | `vertice-logo.svg`, `vertice-symbol.png` | Marca pessoal (Vertice) |
| `workspace/outputs/` | `outputs/`, `output/` | Conteúdo gerado em uso real |
| `workspace/research/` | `research/` (root) | Pesquisas internas |
| `workspace/landing-pages/` | `landing-pages/` | LPs reais (especializei-lab-*, imersao-expert) |
| `workspace/media/` | `media/images/` | Mídia pessoal |

### Casos especiais

- **`.env`, `.env.backup.*`** → ficam no root, gitignored. `.env.example` versionado.
- **`.playwright-mcp/`, `.pytest_cache/`, `node_modules/`, `__pycache__/`, `.DS_Store`** → caches/lixo, sempre gitignored.
- **`AGENTS.md` (root)** → AIOS-framed. **Deletar** na Phase 3.
- **`GUIA-DE-USO.md`, `INSTALACAO-SKILL.md` (root)** → avaliar na Phase 4: redundante com novo README.md → deletar; senão mover pra `docs/guides/`.
- **`CONTRIBUTING.md`** → mantém no root.

### `.gitignore` (refatorado)

```gitignore
# Workspace pessoal (não distribuído)
workspace/
!workspace/.gitkeep
!workspace/*/.gitkeep

# Secrets
.env
.env.backup.*
.env.local

# Caches
.playwright-mcp/
.pytest_cache/
node_modules/
__pycache__/
*.pyc
.DS_Store

# Backups de migração
*.pre-migration.backup
*.bak
```

---

## Section 4 — Deletion Criteria

### 🗑️ Hard-delete (AIOS e órfãos)

| Item | Motivo |
|---|---|
| `.aios/`, `.aios-core/` | Framework AIOS dormante |
| `.aios-installation-config.yaml`, `.aios-pm-config.yaml` | Config AIOS |
| `.antigravity/` | Config Google Antigravity IDE; não usado |
| `.codex/` | Config OpenAI Codex CLI; não usado |
| `squads/` | Conceito AIOS, redundante |
| `AGENTS.md` | AIOS-framed, instruções pra Codex |
| `.claude/CLAUDE.md` (atual ~150 linhas) | Reescrito do zero |
| `.claude/rules/{workflow-execution, story-lifecycle, ids-principles, agent-authority, coderabbit-integration}.md` | Regras AIOS |
| `skill-package/` | Cópia frozen, stale |
| `marketing-os/` (root, com symlinks) | Redundante após Phase 2 |
| `*.pre-migration.backup`, `.env.backup.*`, `.DS_Store` (todos) | Lixo |

### 🤔 Avaliar antes de matar

| Item | Plano |
|---|---|
| `.claude/rules/mcp-usage.md` | Extrair bits úteis sobre Playwright/MCP, fundir em `CLAUDE.md` ou `mcp-conventions.md`; descartar resto |
| `package.json` v5.0.0 + `node_modules/` (`ajv`) | `grep -r ajv scripts/` — se usado: sincronizar versão; senão deletar |
| `requirements.txt`, `pytest.ini`, `.pytest_cache/` | Manter (será usado pelos testes Tier 1) |
| `GUIA-DE-USO.md`, `INSTALACAO-SKILL.md` | Comparar com novo README; redundante → deletar; senão `docs/guides/` |
| `assets/swipe-files/` | Verificar se tem material proprietário/seu vs público; mover proprietário pra workspace |

### ✨ Substituições mínimas

| Antigo | Novo |
|---|---|
| `.claude/CLAUDE.md` AIOS (~150 linhas) | `.claude/CLAUDE.md` enxuto (~40 linhas) |
| `.claude/rules/*.md` AIOS (5 arquivos) | Zero ou um arquivo (`mcp-conventions.md`) |
| `AGENTS.md` AIOS | (deletado, sem substituto) |
| `README.md` atual (29 KB) | `README.md` reescrito (~5 KB) |

---

## Section 5 — Verification & Testing

### Tier 1 — Static validation (mandatório, sem custo)

Pytest suite em `scripts/tests/`:

| Teste | O que valida |
|---|---|
| `test_plugin_manifest.py` | `plugin.json` schema, versão consistente com `package.json` (se mantido), campos obrigatórios |
| `test_skill_md.py` | Frontmatter de `skills/marketing-os/SKILL.md` (name, description, allowed-tools) |
| `test_subagents.py` | Para cada subagent em `subagents/`: frontmatter válido (name, description, model, tools), parseia sem erro |
| `test_commands.py` | Para cada command em `commands/`: estrutura válida |
| `test_no_dangling_refs.py` | Varre `.md` em busca de links/refs internos quebrados |
| `test_no_aios_residue.py` | Falha se encontrar "aios", "@aios-master", `.aios-core` etc fora de `CHANGELOG.md` |
| `test_workspace_separation.py` | Falha se algum arquivo do plugin referenciar path do `workspace/` |
| `test_no_dangling_symlinks.py` | `find . -xtype l` retorna vazio (symlinks válidos OK; só falha se algum apontar pra path inexistente) |

**Pré-requisito:** ler `scripts/validate_agents.py` (untracked) e absorver/expandir, não duplicar.

**Comando:** `pytest scripts/tests/ -v`

### Tier 2 — Smoke tests via `claude -p` (recomendado, sem custo extra)

Usa subscription Claude Max do autor via subprocess pra `claude -p`. Em `scripts/tests/test_agents_smoke.py`:

```python
import subprocess

def invoke_agent(agent: str, prompt: str) -> str:
    result = subprocess.run(
        ["claude", "-p", f"@{agent} {prompt}"],
        capture_output=True, text=True, timeout=120
    )
    return result.stdout

def test_copy_agent_responds():
    output = invoke_agent("copy", "escreva uma headline pra produto X")
    assert len(output) > 100
    assert "headline" in output.lower() or "título" in output.lower()
```

**Agentes representativos** (5-6, não os 18 todos):
- `@copy` — output esperado: headline + sub-headline
- `@seo` — output esperado: keywords + meta description
- `@social` — output esperado: post + hashtags
- `@email` — output esperado: subject + body + CTA
- `@design` — output esperado: design rationale + spec
- `@ads` — output esperado: copy + targeting

**Validações** (estruturais, não subjetivas):
- Resposta não-vazia, >100 chars
- Contém marcadores estruturais esperados
- Não retorna erro de "agent not found" ou similar

**Pré-requisito:** Claude Code logado em conta Max do autor; agentes carregados como plugin local.

**Comando:** `pytest scripts/tests/test_agents_smoke.py -v` (~30-60s, ~5-6 invocações)

### Plano de execução de testes por fase

| Momento | Tier 1 | Tier 2 |
|---|---|---|
| Phase 0 (baseline) | ✅ rodar e snapshot | ✅ rodar e salvar como golden em `tests/snapshots/baseline/` |
| Phase 1 (workspace) | ✅ deve passar 100% | ⚪ não necessário (só moveu artefatos) |
| Phase 2 (dedup) | ✅ deve passar 100% | ✅ rodar e comparar com baseline |
| Phase 3 (matar AIOS) | ✅ deve passar 100% | ✅ rodar e comparar com baseline |
| Phase 4 (polish) | ✅ deve passar 100% | ⚪ não necessário (só metadata) |
| Phase 5 (final) | ✅ rodar 100% | ✅ rodar 100% e comparar com baseline |

### Critérios de "pronto"

- ✅ Todos os testes Tier 1 passam
- ✅ Smoke Tier 2: respostas estruturalmente equivalentes ao baseline
- ✅ `du -sh .` reduziu ≥30% comparado ao baseline
- ✅ `tree -L 1 .` cabe em ~20 linhas
- ✅ `grep -ri "aios" --include="*.md" .` só em `CHANGELOG.md`
- ✅ Plugin carrega em Claude Code sem erro
- ✅ 2-3 agentes respondem manualmente em sessão real
- ✅ `git log --oneline` mostra histórico limpo (~5-6 commits, um por fase)

### Rollback strategy

- Cada fase termina com commit. Se algo quebrar:
  - Volta uma fase: `git reset --hard HEAD~1`
  - Volta tudo: `git reset --hard <baseline-sha>` (capturada na Phase 0)
- Branch `refactor/plugin-first` isolada — `main` permanece intocada até merge final.
- **Nunca** usar `--no-verify` ou pular hooks. Se hook quebrar, investigar.

### Limitações aceitas (não testadas)

- Qualidade subjetiva do output dos agentes ("esse copy ficou bom?")
- Performance (latência, throughput)
- Compatibilidade com versões antigas do Claude Code
- Comportamento sob rate limit do Max (assumido tolerável dado volume baixo de smoke tests)

---

## Out of scope

- Reescrever lógica de qualquer subagente
- Adicionar novos agentes/workflows/commands
- Migrar Python ↔ TypeScript
- Otimizar performance
- Publicar no marketplace público
- Criar suite de testes funcionais que avaliem qualidade do output
- Versionamento semântico ou release engineering automático
- Integração com CI externo

---

## Open questions / Risks

| Item | Mitigação |
|---|---|
| `scripts/validate_agents.py` é untracked — se for half-baked, Tier 1 base é frágil | Phase 0 inclui leitura crítica e expansão se necessário |
| Symlinks vs conteúdo direto: qual padrão Claude Code prefere pra plugins? | Verificar plugins oficiais do marketplace na Phase 0; default: **manter symlinks** (resolução de path, não dup); reavaliar se padrão for diferente |
| `claude -p` em pytest pode ter overhead de inicialização alto (>5s/invocação) | Aceitar; smoke é só em 5-6 agentes; rodar em paralelo se ficar inviável |
| Rate limit do Max durante smoke tests | Volume baixo (5-6 invocações por execução); rodar smoke só em fases críticas (2, 3, 5) |
| `package.json` divergente do `plugin.json` (5.0.0 vs 5.1.0) | Decisão na Phase 4 baseada em uso real de deps Node |
| Conteúdo único em `skill-package/SKILL.md` vs `skills/marketing-os/SKILL.md` (divergiram) | Phase 2: diff explícito antes de deletar, fundir conteúdo único |
| AIOS pode ter referências cruzadas inesperadas em scripts/ ou subagents/ | Phase 3: grep extensivo antes de commitar |

---

## Next step

Após aprovação deste design, próximo skill a invocar: `superpowers:writing-plans` para criar plano de implementação detalhado e executável.
