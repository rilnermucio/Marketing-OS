# Auditoria multi-modal com PDF white-label (Design)

**Date:** 2026-05-09
**Status:** Draft (awaiting user review)
**Author:** Claude Opus 4.7 via brainstorming skill, with rilner
**Target version:** marketing-os v6.7.0

---

## Context

A análise competitiva (turnos anteriores desta sessão) identificou que o marketing-os tem 70k linhas de conteúdo, 18 agents two-tier, 35 voice clones e 32 commands, mas **não tem comando de auditoria orquestrada com PDF cliente-ready**. O concorrente direto `ai-marketing-claude` (zubair-trabzada/GitHub) construiu sua identidade inteira ao redor desse comando: `/market audit <url>` despacha 5 subagents em paralelo, gera scoring 0-100 ponderado e produz PDF profissional pra cliente. Isso é o killer feature que falta.

Marketing-os já tem todos os agents e infraestrutura necessários: o que falta é a camada de orquestração + scoring + PDF. Esta spec define essa camada.

### Constraints declarados pelo usuário (turnos anteriores)

| Constraint | Decisão |
|---|---|
| Scope | Multi-modal auto-detect (4 tipos: landing, Instagram, Meta Ads, YouTube) |
| Branding do PDF | White-label configurável (`.auditoria-config.json` no projeto do usuário) |
| Idioma | PT-BR (consistente com naming de commands existentes: `/criar-post`, `/criar-anuncio`, `/campanha-launch`) |
| Esforço alvo | 4-5 dias |
| Approach escolhido | Pragmatic v1 (Approach A das 3 propostas) |

### Não-objetivos (out of scope)

- Histórico/comparativo entre auditorias (v1.1+)
- Integração Notion MCP pra publicar relatório direto (v1.1+)
- Modificação dos 18 agents pra retornar JSON estruturado (decisão arquitetural: synthesis fica no command, não nos agents)
- Auditoria de funil completo multi-step (TOFU/MOFU/BOFU). Aceito apenas como single-input por run
- Internacionalização (EN, ES). Permanece PT-BR only

---

## Architecture

Mantém o padrão two-tier existente do plugin. Três camadas:

### Layer 1: Command orchestrator
Arquivo: `commands/auditoria.md`. Markdown com YAML frontmatter declarando `allowed-tools: Bash, WebFetch, Read, Write, Agent`. System prompt PT-BR (~150 linhas) com lógica de:
1. Parsing de input (`$ARGUMENTS`)
2. Invocação do detector
3. Switch por tipo
4. Dispatch matrix (Agent calls em paralelo, single message)
5. Synthesis step (atribui scores 0-100 por dimensão baseado em outputs dos agents)
6. Invocação do scoring script
7. Geração do RELATORIO.md (template por tipo)
8. Invocação do PDF generator

### Layer 2: Scripts determinísticos
Quatro scripts novos em `scripts/`:
- `audit_detector.py`: detect type from input
- `audit_scoring.py`: rubric weights, math ponderada, sort top wins/fixes, formatação
- `pdf_generator.py`: genérico e reutilizável (não exclusivo da auditoria)
- `audit_config.py`: loader/validator do `.auditoria-config.json`

### Layer 3: Output
Diretório `workspace/auditorias/<YYYY-MM-DD-HHMMSS>-<tipo>-<slug>/` (gitignored, consistente com separação workspace/plugin do projeto). Conteúdo:
- `RELATORIO.md`: relatório completo
- `RELATORIO.pdf`: versão PDF white-label
- `.audit-meta.json`: telemetria local (timestamps, agents que rodaram, falhas)

### Decisões arquiteturais não-óbvias

**Por que synthesis no command, não nos agents.** Modificar 18 system prompts pra emitir JSON estruturado em modo "auditoria" seria mudança de superfície gigante e quebra ortogonalidade (cada agent ficaria com 2 modos). Manter outputs free-form e fazer synthesis no command preserva os agents existentes intactos. Custo: ~50 linhas extras no command pra explicar a rubric ao Claude que faz synthesis.

**Por que `pdf_generator.py` é genérico, não específico de auditoria.** O usuário identificou na análise competitiva que PDF generator reutilizável dobra utilidade do investimento. Outros commands (`/criar-calendario`, `/criar-funil`, `/campanha-*`, `/criar-infoproduto`) podem chamar o mesmo script depois sem refactor. Custo desta decisão: o PDF generator não pode assumir estrutura específica de auditoria, precisa aceitar markdown arbitrário.

**Por que weasyprint, não reportlab.** Weasyprint usa CSS moderno (HTML/CSS to PDF). ReportLab requer 200+ linhas de layout primitivo pra cada novo template. Pra design decente em white-label, weasyprint é ordem de magnitude mais simples. Custo: dependência maior (cairo, pango), mas é well-supported e roda em macOS/Linux.

---

## Components

### 4.1 `audit_detector.py`

**Assinatura:**
```python
def detect(input_str: str) -> dict:
    """Returns {type, normalized, slug} or raises ValueError."""
```

**Logic:**
- Strip whitespace
- Se começa com `@` ou matches `^[a-z0-9_.]+$`: type=`instagram`, normalized=remove `@`, slug=lowercase username
- Se contém `facebook.com/ads/library`: type=`meta_ads`, normalized=URL canônica, slug=hash dos query params
- Se contém `youtube.com` ou `youtu.be`: type=`youtube`, normalized=URL canônica, slug=video_id
- Se URL válida (regex http/https): type=`landing`, normalized=URL com trailing slash removido, slug=domínio sem TLD
- Senão: raise ValueError com 4 exemplos PT-BR

**CLI mode:** `python audit_detector.py "<input>"` imprime JSON em stdout. Exit 0 se válido, exit 1 + erro em stderr se inválido.

### 4.2 `audit_scoring.py`

**Rubrics por tipo (constantes Python):**

```python
RUBRICS = {
    "landing": {
        "Conversão (CTA, friction, funil)": 25,
        "Copy (headline, value prop)": 20,
        "SEO (technical + content)": 15,
        "Trust signals": 10,
        "Design (hierarquia visual)": 10,
        "Brand (consistência, voice)": 10,
        "Diferenciação competitiva": 10,
    },
    "instagram": {
        "Bio + posicionamento": 20,
        "Consistência visual": 20,
        "Hooks últimos posts": 20,
        "Strategy/CTA": 15,
        "Engagement ratio": 15,
        "Cadência/frequência": 10,
    },
    "meta_ads": {
        "Hook do criativo (3s)": 25,
        "Copy (clarity + benefit)": 25,
        "Visual (composição)": 20,
        "CTA + landing match": 15,
        "Diferenciação vs concorrente": 15,
    },
    "youtube": {
        "Hook (30s)": 25,
        "Retention/pacing": 25,
        "Thumbnail + título": 20,
        "Estrutura narrativa": 15,
        "CTA/conversão": 15,
    },
}
```

**Assinatura:**
```python
def compute(audit_type: str, dimension_scores: dict, evidences: dict, fixes: dict) -> dict:
    """
    dimension_scores: {nome_dim: int 0-100 ou None se "N/D"}
    evidences: {nome_dim: str}
    fixes: {nome_dim: {"text": str, "priority": "alta"|"media"|"baixa"}}
    Returns: {overall, dimensions, top_wins, top_fixes, partial}
    """
```

**Logic:**
- Validate: rubric do tipo soma 100, todas as dimensões da rubric presentes em `dimension_scores` (ou explicitamente None)
- Overall: média ponderada das dimensões pontuadas. Se algumas são None, recalcula peso normalizado das restantes e marca `partial=True`
- Top wins: 3 dimensões com maior score
- Top fixes: 3 dimensões com menor score, ordenadas por (priority, score asc)
- Output: dict serializável pra JSON

**Format helpers:**
- `format_scorecard_md(result) -> str`: tabela markdown
- `format_priorities_md(result) -> str`: lista priorizada de fixes

**CLI mode:** lê JSON de stdin, escreve JSON em stdout.

### 4.3 `pdf_generator.py` (genérico, reutilizável)

**Assinatura:**
```python
def generate(markdown_path: Path, output_path: Path, config_path: Path | None = None) -> Path:
    """Renders markdown to PDF via weasyprint. Returns output_path."""
```

**Engine:** weasyprint 60+

**Pipeline:**
1. Read markdown
2. Convert to HTML via markdown-it-py (fenced code blocks, tables, GFM)
3. Wrap em template HTML embedded (constante no script)
4. Inject config (se houver) como CSS variables
5. Render via weasyprint

**Default theme (sem config):**
- Background: `#ffffff`
- Text: `#1a1a1a`
- Accent: `#1a73e8`
- Font: system sans-serif via `font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;`
- Footer fixo: `Auditoria gerada com marketing-os v6.7.0` (apenas quando sem config)
- A4 portrait, margens 2cm

**Com config (white-label):**
- Logo no topo (se `logo_path` apontar pra arquivo válido)
- `brand_name` no header
- Cores customizadas via CSS variables
- Footer: `footer_text` do config (ou ausente se vazio)

**Erro modes:**
- weasyprint não importa: ImportError com mensagem `Instale weasyprint: pip install weasyprint`
- Markdown malformado: tenta render mesmo assim (markdown-it-py é tolerante)
- Config inválido: ignora config, usa defaults, log warning em stderr

**CLI mode:** `python pdf_generator.py input.md output.pdf [config.json]`

### 4.4 `audit_config.py`

**Schema (`.auditoria-config.json`):**
```json
{
  "$schema": "https://json-schema.org/draft-07/schema#",
  "type": "object",
  "required": ["brand_name"],
  "properties": {
    "brand_name": {"type": "string", "minLength": 1},
    "logo_path": {"type": "string"},
    "primary_color": {"type": "string", "pattern": "^#[0-9a-fA-F]{6}$"},
    "accent_color": {"type": "string", "pattern": "^#[0-9a-fA-F]{6}$"},
    "footer_text": {"type": "string"}
  },
  "additionalProperties": false
}
```

**Assinatura:**
```python
def load(config_path: Path | None) -> dict | None:
    """Loads and validates. Returns None if no config or invalid."""
```

**Behavior:**
- Sem path ou path não existe: return None silenciosamente
- Path existe mas JSON inválido: log warning, return None
- JSON válido mas schema inválido: log warning com erros do jsonschema, return None
- Logo path inexistente: warning, mas mantém config (PDF generator lida)
- Cor inválida: warning, sobrescreve com default

### 4.5 `commands/auditoria.md`

**Frontmatter:**
```yaml
---
description: Auditoria multi-modal de landing page, Instagram, Meta Ad ou YouTube com scorecard ponderado e PDF white-label.
argument-hint: <url-ou-perfil>
allowed-tools: Bash, WebFetch, Read, Write, Agent
---
```

**System prompt structure:**
1. Recebe `$ARGUMENTS`. Se vazio: retorna usage com 4 exemplos PT-BR e aborta.
2. Bash: `python ${CLAUDE_PLUGIN_ROOT}/scripts/audit_detector.py "$ARGUMENTS"` → captura JSON. Se erro: aborta.
3. Switch por type. Pra cada type, dispatch matrix em single message com Agent calls em paralelo (4-7 conforme tipo). Cada Agent recebe prompt customizado mencionando o normalized input e a área de foco.
4. Coleta outputs dos N agents.
5. **Synthesis prompt embedded no command (~50 linhas):** "Para cada dimensão da rubric do tipo `{type}`, leia os outputs dos agents relevantes e atribua score 0-100, evidência (1 frase, citando o que viu), e fix priorizado (texto + priority)." Output esperado: JSON.
6. Bash: `python ${CLAUDE_PLUGIN_ROOT}/scripts/audit_scoring.py < scores.json` → recebe overall + tabelas formatadas.
7. Write: monta `RELATORIO.md` em `workspace/auditorias/<run>/` com header (overall + tipo + input + timestamp), exec summary, scorecard, dimension breakdown, anexo raw outputs.
8. Bash: `python ${CLAUDE_PLUGIN_ROOT}/scripts/pdf_generator.py RELATORIO.md RELATORIO.pdf [.auditoria-config.json]`.
9. Output inline no chat: paths dos 2 arquivos + 3 linhas de exec summary.

**Hook command:** `${CLAUDE_PLUGIN_ROOT}/scripts/hooks/quality_gate_hook.py` no PreToolUse `Write|Edit` (consistente com outros commands).

---

## Data flow

```
[1] User: /auditoria <input>
       ↓
[2] Bash: audit_detector.py "<input>"
       ↓ {"type":"landing","slug":"calendly-com","normalized":"https://calendly.com"}
[3] Switch por type → dispatch matrix
       Ex landing: 7 Agent() em paralelo (research, seo, copy, funnel, ads, design, brand)
       ↓
[4] Cada agent retorna markdown free-form (output schema livre)
       ↓
[5] Synthesis (Claude no command): aplica rubric do tipo, atribui scores 0-100
       ↓ JSON com dimensions/evidences/fixes
[6] Bash: audit_scoring.py < scores.json → overall ponderado + top wins/fixes
       ↓ JSON com result completo
[7] Write: RELATORIO.md em workspace/auditorias/<run>/ via template por tipo
       ↓
[8] Bash: pdf_generator.py RELATORIO.md RELATORIO.pdf [.auditoria-config.json]
       ↓
[9] Output: paths + exec summary 3 linhas
```

**Decisão crítica:** o scoring é "human-in-the-loop" (Claude no passo 5) com rubric determinística (passo 6). Não é puramente determinístico (não há NLP-from-text-to-score) e não é puramente subjetivo (a rubric e a math são fixas).

---

## Error handling

### Hard errors (aborta com mensagem clara)

| Falha | Resposta |
|---|---|
| Input vazio | Usage + 4 exemplos PT-BR, aborta |
| URL malformada | `Não consegui interpretar "<input>". Formatos válidos: <exemplos>` |
| `workspace/` não gravável | `Diretório workspace/ não existe ou sem permissão de escrita` |
| weasyprint não instalado | `Instale: pip install weasyprint`. Aborta no momento do Bash invocation |

### Soft degradation (continua, sinaliza no relatório)

| Falha | Comportamento |
|---|---|
| 1 agent falha | Continua com N-1. Dimensões dependentes desse agent ficam None. Overall recalcula com peso normalizado. Header marca "auditoria parcial" |
| >50% dos agents falham | Aborta: `Auditoria abortada: X de Y agents falharam` |
| `APIFY_TOKEN` ausente em IG/MetaAds/YouTube | Modo limitado: WebFetch fallback. Header destaca aviso e link pra `docs/APIFY-INTEGRATION.md` |
| Apify retorna vazio/timeout | Mesmo fallback + flag específica |
| PDF generation falha | Entrega só `RELATORIO.md`. Chat sinaliza erro + path |
| Config `.auditoria-config.json` inválido | Warning no chat, PDF neutro, log em `.config-error.log` |
| Logo path inexistente | Warning, PDF sem logo, resto do branding aplicado |

### User confirmation (interrompe e pergunta)

| Caso | Ação |
|---|---|
| Type detection ambígua (raro: URL Instagram embedada) | Pergunta inline |
| Auditoria duplicada do mesmo input em <24h | Aviso + confirmação `[s/N]` |

### Telemetria local
`workspace/auditorias/<run>/.audit-meta.json` com:
- Timestamp start/end
- Type detected
- Agents dispatched, agents que falharam
- APIFY_TOKEN presente (boolean, não vaza valor)
- Config aplicado ou não
- Erros não-fatais

Sem coleta remota (consistente com resto do plugin).

---

## Testing

### Unit tests (rápidos, fora de `@pytest.mark.smoke`)

| Test file | Cobertura | Coverage alvo |
|---|---|---|
| `test_audit_detector.py` | URL patterns, edge cases (trailing slash, query params, unicode), `@perfil` variants, input inválido | 100% |
| `test_audit_scoring.py` | Rubrics somam 100, math ponderada correta, partial inputs, ordenação top wins/fixes, score out of range | 100% |
| `test_audit_config.py` | Schema válido, schema inválido, config ausente, logo inexistente, cor inválida | 100% |
| `test_pdf_generator.py` | Markdown vira PDF não-vazio, config aplicado (mocked weasyprint), config malformado fallback | ~80% |

### Integration test

| Test file | Cobertura |
|---|---|
| `test_auditoria_smoke.py` (`@pytest.mark.smoke`) | Pipeline completo com agent outputs MOCKADOS. Detector → synthesis fake → scoring → markdown → PDF |

### Tests existentes (cobrem automaticamente)
- `test_commands_dispatch.py`: pega `/auditoria` automaticamente, valida que despacha
- `test_workspace_separation.py`: valida que outputs vão pra `workspace/`
- `test_plugin_manifest.py`: pega o command novo no count

### Manual validation antes de release v6.7.0

1. `/auditoria https://stripe.com` (landing, 7 agents)
2. `/auditoria @ericorocha` SEM APIFY_TOKEN (modo limitado)
3. `/auditoria @ericorocha` COM APIFY_TOKEN (estruturado)
4. Idem #1 com `.auditoria-config.json` no cwd

Critério de pass: cada um gera `RELATORIO.md` + `RELATORIO.pdf` em `workspace/auditorias/<run>/`, exec summary no chat, sem stack traces.

### CI
Sem mudança. `pytest -m "not smoke"` no CI atual pega os 4 unit tests novos automaticamente.

---

## File manifest

### Novos arquivos
- `commands/auditoria.md` (~150 linhas)
- `scripts/audit_detector.py` (~80 linhas)
- `scripts/audit_scoring.py` (~200 linhas, inclui rubrics + helpers)
- `scripts/pdf_generator.py` (~250 linhas, inclui template HTML)
- `scripts/audit_config.py` (~100 linhas)
- `scripts/tests/test_audit_detector.py` (~80 linhas)
- `scripts/tests/test_audit_scoring.py` (~150 linhas)
- `scripts/tests/test_audit_config.py` (~60 linhas)
- `scripts/tests/test_pdf_generator.py` (~80 linhas)
- `scripts/tests/test_auditoria_smoke.py` (~120 linhas)
- `docs/AUDIT-CONFIG.md` (documentação do `.auditoria-config.json`, ~80 linhas)

### Arquivos modificados
- `requirements.txt`: + `weasyprint>=60.0`, `markdown-it-py>=3.0`, `jsonschema>=4.0`
- `scripts/mos.py`: subcommand `mos audit ...` (alias do command pra invocação CLI direta)
- `AGENTS.md`: menção de `/auditoria` na seção de commands
- `CHANGELOG.md`: entrada v6.7.0
- `plugin.json`: bump para 6.7.0
- `.claude-plugin/marketplace.json`: bump version

**Total estimado:** ~1.350 linhas novas + ~50 linhas modificadas.

---

## Open questions / V1.1+

### Confirmações pendentes (não-bloqueantes)
- Default accent color (`#1a73e8`) é OK ou tem cor brand do marketing-os preferida?
- `mos audit` no `scripts/mos.py` é desejado ou só `/auditoria` no Claude Code basta?

### V1.1 candidatos (fora do scope desta release)
1. Histórico de auditorias: `workspace/auditorias/_index.json` + comando `/auditoria-comparar <run1> <run2>`
2. Notion MCP integration: publica RELATORIO.md direto em workspace Notion via tool existente
3. Auditoria de funil completo multi-step (TOFU/MOFU/BOFU)
4. Templates de RELATORIO.md customizáveis (além do default por tipo)
5. Localização EN/ES (depende de demanda)

---

## Implementation order (preview pra writing-plans skill)

1. Spec + dependências em `requirements.txt`
2. `audit_detector.py` + tests (mais isolado, valida regex/parsing)
3. `audit_scoring.py` + tests (rubrics + math, isolado)
4. `audit_config.py` + tests (schema validation, isolado)
5. `pdf_generator.py` + tests (depende de markdown_it + weasyprint, valida theming)
6. `commands/auditoria.md` (depende dos 4 scripts; aqui o command bate com agents)
7. Smoke test integration
8. `docs/AUDIT-CONFIG.md`
9. Manual validation dos 4 cenários
10. CHANGELOG + bump versão + commit + tag

Ordem garante: dependências resolvidas, cada step testável isoladamente, command só entra quando scripts já passam tests.
