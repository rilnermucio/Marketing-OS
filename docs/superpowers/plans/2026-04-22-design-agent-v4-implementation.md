# Design Agent v4.0 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Replace `subagents/design-agent.md` (v3.1, 3.546 lines, marketing-only) with v4.0 full-stack design intelligence (marketing + product + design system + brand), hybrid builder+orchestrator model, supported by 10 modular companions and 8 executable templates.

**Architecture:** Refactor + extract from v3.1. One agent (~2k lines, strategic brain) + 10 deep companions in `references/design/` + 8 skeleton templates in `assets/templates/design/`. Archive v3.1 as fallback. Sync canonical → skill-package copy.

**Tech Stack:** Markdown (prose), JSON (tokens), CSS, TypeScript/JavaScript (configs), shell scripts for validation.

**Spec:** `docs/superpowers/specs/2026-04-22-design-agent-v4-design.md`

---

## Pre-flight context for implementers

**Repository layout essentials:**
- Canonical subagents: `subagents/*.md` (edit here)
- Mirror 1: `marketing-os/subagents/` — symlink to `../subagents/` (auto-follows)
- Mirror 2: `skills/marketing-os/subagents/` — symlink to `../../subagents/` (auto-follows)
- Mirror 3: `skill-package/marketing-os/subagents/` — **real directory, needs manual copy**
- Canonical references: `references/*.md`
- Mirror 1: `marketing-os/references/` — symlink to `../references/`
- Mirror 2: `skills/marketing-os/references/` — symlink to `../../references/`
- Mirror 3: `skill-package/marketing-os/references/` — real copy, needs manual sync
- Canonical templates: `assets/templates/*` (root of `assets/templates/` has flat files; subfolder OK)
- Mirror 1: `marketing-os/assets/` (via `marketing-os/assets` symlink → `../assets/`)
- Mirror 2: `skills/marketing-os/assets/` — symlink to `../../assets/`
- Mirror 3: `skill-package/marketing-os/assets/` — real copy

**Content rules (non-negotiable, from `.claude/CLAUDE.md` + Marketing OS memory):**
- Portuguese. Maintain accents (ção, ã, õ, á, é, í, ó, ú).
- Zero em-dash `—` where a comma or period works (allowed in prose only where syntactically needed).
- Zero "brutal", gratuitous ALL CAPS, quotes in scripts.
- Zero self-proclaimed superlatives without evidence ("most advanced on the planet").
- WebSearch before citing people/stats; mark illustrative examples as such.

**Source file to extract from:**
- `subagents/design-agent.md` (v3.1, 3.546 lines) — see spec §7 for the extraction map.

---

## Phase 0 — Foundation and Safety

### Task 1: Archive v3.1 and scaffold directories

**Files:**
- Rename: `subagents/design-agent.md` → `subagents/design-agent-v3.1-archive.md`
- Create: `references/design/` (new subfolder)
- Create: `assets/templates/design/` (new subfolder)
- Sync: `skill-package/marketing-os/subagents/design-agent.md` → `skill-package/marketing-os/subagents/design-agent-v3.1-archive.md`

- [ ] **Step 1: Create archive copy (keep canonical intact during build)**

Run:
```bash
cd "/Users/rilner/Marketing OS"
cp subagents/design-agent.md subagents/design-agent-v3.1-archive.md
```

Expected: `subagents/design-agent-v3.1-archive.md` created, `subagents/design-agent.md` still exists.

- [ ] **Step 2: Create directory structure**

Run:
```bash
cd "/Users/rilner/Marketing OS"
mkdir -p references/design assets/templates/design
ls -d references/design assets/templates/design
```

Expected: both directories listed without errors.

- [ ] **Step 3: Sync archive to skill-package copy**

Run:
```bash
cd "/Users/rilner/Marketing OS"
cp subagents/design-agent-v3.1-archive.md skill-package/marketing-os/subagents/design-agent-v3.1-archive.md
```

Expected: skill-package copy matches canonical archive. Verify:
```bash
diff subagents/design-agent-v3.1-archive.md skill-package/marketing-os/subagents/design-agent-v3.1-archive.md
```
Expected: no output (files identical).

- [ ] **Step 4: Commit**

```bash
cd "/Users/rilner/Marketing OS"
git add subagents/design-agent-v3.1-archive.md skill-package/marketing-os/subagents/design-agent-v3.1-archive.md
git commit -m "$(cat <<'EOF'
chore(design): archive v3.1 design agent before v4 rebuild

Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>
EOF
)"
```

Note: empty directories (`references/design/`, `assets/templates/design/`) are not tracked by git. They appear naturally when populated.

---

## Phase 1 — Templates (8 tasks)

Templates are small skeletons the agent fills in Builder Mode. Done first to lock contracts that companions reference.

### Task 2: tokens.json.template

**Files:**
- Create: `assets/templates/design/tokens.json.template`

**Size target:** ~200 lines.

- [ ] **Step 1: Write file with W3C Design Tokens structure (core → semantic → component layers)**

Content outline:
```json
{
  "$schema": "https://design-tokens.github.io/community-group/format/",
  "_meta": {
    "name": "{{PROJECT_NAME}} Design Tokens",
    "version": "0.1.0",
    "description": "W3C Design Tokens — three-layer architecture"
  },
  "core": {
    "color": {
      "neutral": {
        "0":   {"$value": "#FFFFFF", "$type": "color"},
        "50":  {"$value": "#F9FAFB", "$type": "color"},
        "100": {"$value": "#F3F4F6", "$type": "color"},
        "200": {"$value": "#E5E7EB", "$type": "color"},
        "300": {"$value": "#D1D5DB", "$type": "color"},
        "400": {"$value": "#9CA3AF", "$type": "color"},
        "500": {"$value": "#6B7280", "$type": "color"},
        "600": {"$value": "#4B5563", "$type": "color"},
        "700": {"$value": "#374151", "$type": "color"},
        "800": {"$value": "#1F2937", "$type": "color"},
        "900": {"$value": "#111827", "$type": "color"},
        "1000": {"$value": "#000000", "$type": "color"}
      },
      "brand": {
        "primary": {"$value": "{{BRAND_PRIMARY}}", "$type": "color", "$description": "Replace with hex value"},
        "secondary": {"$value": "{{BRAND_SECONDARY}}", "$type": "color"},
        "accent": {"$value": "{{BRAND_ACCENT}}", "$type": "color"}
      }
    },
    "dimension": {
      "spacing": {
        "0":   {"$value": "0px",    "$type": "dimension"},
        "1":   {"$value": "4px",    "$type": "dimension"},
        "2":   {"$value": "8px",    "$type": "dimension"},
        "3":   {"$value": "12px",   "$type": "dimension"},
        "4":   {"$value": "16px",   "$type": "dimension"},
        "6":   {"$value": "24px",   "$type": "dimension"},
        "8":   {"$value": "32px",   "$type": "dimension"},
        "12":  {"$value": "48px",   "$type": "dimension"},
        "16":  {"$value": "64px",   "$type": "dimension"},
        "24":  {"$value": "96px",   "$type": "dimension"}
      },
      "radius": {
        "none":  {"$value": "0px",     "$type": "dimension"},
        "sm":    {"$value": "4px",     "$type": "dimension"},
        "md":    {"$value": "8px",     "$type": "dimension"},
        "lg":    {"$value": "12px",    "$type": "dimension"},
        "xl":    {"$value": "16px",    "$type": "dimension"},
        "full":  {"$value": "9999px",  "$type": "dimension"}
      }
    },
    "typography": {
      "fontFamily": {
        "sans":  {"$value": "Inter, system-ui, sans-serif", "$type": "fontFamily"},
        "serif": {"$value": "Merriweather, Georgia, serif", "$type": "fontFamily"},
        "mono":  {"$value": "JetBrains Mono, monospace",    "$type": "fontFamily"}
      },
      "fontWeight": {
        "regular":  {"$value": 400, "$type": "fontWeight"},
        "medium":   {"$value": 500, "$type": "fontWeight"},
        "semibold": {"$value": 600, "$type": "fontWeight"},
        "bold":     {"$value": 700, "$type": "fontWeight"}
      },
      "fontSize": {
        "xs":   {"$value": "12px", "$type": "dimension"},
        "sm":   {"$value": "14px", "$type": "dimension"},
        "base": {"$value": "16px", "$type": "dimension"},
        "lg":   {"$value": "18px", "$type": "dimension"},
        "xl":   {"$value": "20px", "$type": "dimension"},
        "2xl":  {"$value": "24px", "$type": "dimension"},
        "3xl":  {"$value": "30px", "$type": "dimension"},
        "4xl":  {"$value": "36px", "$type": "dimension"},
        "5xl":  {"$value": "48px", "$type": "dimension"}
      },
      "lineHeight": {
        "tight":  {"$value": 1.2,  "$type": "number"},
        "normal": {"$value": 1.5,  "$type": "number"},
        "loose":  {"$value": 1.75, "$type": "number"}
      }
    },
    "duration": {
      "instant": {"$value": "100ms", "$type": "duration"},
      "fast":    {"$value": "150ms", "$type": "duration"},
      "normal":  {"$value": "250ms", "$type": "duration"},
      "slow":    {"$value": "400ms", "$type": "duration"},
      "slower":  {"$value": "700ms", "$type": "duration"}
    },
    "easing": {
      "linear":    {"$value": [0, 0, 1, 1],       "$type": "cubicBezier"},
      "easeIn":    {"$value": [0.4, 0, 1, 1],     "$type": "cubicBezier"},
      "easeOut":   {"$value": [0, 0, 0.2, 1],     "$type": "cubicBezier"},
      "easeInOut": {"$value": [0.4, 0, 0.2, 1],   "$type": "cubicBezier"}
    }
  },
  "semantic": {
    "color": {
      "background": {
        "primary":   {"$value": "{core.color.neutral.0}",   "$type": "color"},
        "secondary": {"$value": "{core.color.neutral.50}",  "$type": "color"},
        "elevated":  {"$value": "{core.color.neutral.0}",   "$type": "color"},
        "overlay":   {"$value": "{core.color.neutral.900}", "$type": "color"}
      },
      "text": {
        "primary":   {"$value": "{core.color.neutral.900}", "$type": "color"},
        "secondary": {"$value": "{core.color.neutral.600}", "$type": "color"},
        "muted":     {"$value": "{core.color.neutral.400}", "$type": "color"},
        "inverse":   {"$value": "{core.color.neutral.0}",   "$type": "color"}
      },
      "border": {
        "default": {"$value": "{core.color.neutral.200}", "$type": "color"},
        "strong":  {"$value": "{core.color.neutral.400}", "$type": "color"},
        "focus":   {"$value": "{core.color.brand.primary}", "$type": "color"}
      },
      "feedback": {
        "success": {"$value": "#10B981", "$type": "color"},
        "warning": {"$value": "#F59E0B", "$type": "color"},
        "danger":  {"$value": "#EF4444", "$type": "color"},
        "info":    {"$value": "#3B82F6", "$type": "color"}
      }
    }
  },
  "component": {
    "button": {
      "padding": {
        "sm": {"$value": "{core.dimension.spacing.2} {core.dimension.spacing.3}", "$type": "dimension"},
        "md": {"$value": "{core.dimension.spacing.3} {core.dimension.spacing.4}", "$type": "dimension"},
        "lg": {"$value": "{core.dimension.spacing.4} {core.dimension.spacing.6}", "$type": "dimension"}
      },
      "radius": {"$value": "{core.dimension.radius.md}", "$type": "dimension"},
      "fontWeight": {"$value": "{core.typography.fontWeight.medium}", "$type": "fontWeight"}
    },
    "card": {
      "padding":    {"$value": "{core.dimension.spacing.6}",  "$type": "dimension"},
      "radius":     {"$value": "{core.dimension.radius.lg}",  "$type": "dimension"},
      "background": {"$value": "{semantic.color.background.elevated}", "$type": "color"}
    }
  }
}
```

Use Write tool to create the file with the JSON above (copy literally, keeping all `{{PLACEHOLDER}}` tokens where the agent will substitute values).

- [ ] **Step 2: Verify JSON validity**

Run:
```bash
cd "/Users/rilner/Marketing OS"
python3 -c "import json; json.load(open('assets/templates/design/tokens.json.template'))" && echo "OK: valid JSON"
```

Expected: `OK: valid JSON` (note: `{{PLACEHOLDER}}` is inside strings, so JSON is still valid).

- [ ] **Step 3: Commit**

```bash
cd "/Users/rilner/Marketing OS"
git add assets/templates/design/tokens.json.template
git commit -m "$(cat <<'EOF'
feat(design/templates): add W3C tokens.json template

Three-layer architecture (core/semantic/component) with placeholders
for brand values.

Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>
EOF
)"
```

---

### Task 3: theme.css.template

**Files:**
- Create: `assets/templates/design/theme.css.template`

**Size target:** ~150 lines.

- [ ] **Step 1: Write CSS layer structure with tokens**

Content to write (full file — use Write tool):

```css
/* =============================================================================
   {{PROJECT_NAME}} Theme
   Generated from tokens.json via Style Dictionary (or copy manually).
   ========================================================================== */

@layer base, theme, components, utilities;

/* ----- Light theme (default) ------------------------------------------------ */
@layer theme {
  :root {
    /* Brand */
    --color-brand-primary: {{BRAND_PRIMARY}};
    --color-brand-secondary: {{BRAND_SECONDARY}};
    --color-brand-accent: {{BRAND_ACCENT}};

    /* Neutrals */
    --color-neutral-0:    #FFFFFF;
    --color-neutral-50:   #F9FAFB;
    --color-neutral-100:  #F3F4F6;
    --color-neutral-200:  #E5E7EB;
    --color-neutral-300:  #D1D5DB;
    --color-neutral-400:  #9CA3AF;
    --color-neutral-500:  #6B7280;
    --color-neutral-600:  #4B5563;
    --color-neutral-700:  #374151;
    --color-neutral-800:  #1F2937;
    --color-neutral-900:  #111827;
    --color-neutral-1000: #000000;

    /* Semantic */
    --color-bg-primary:    var(--color-neutral-0);
    --color-bg-secondary:  var(--color-neutral-50);
    --color-bg-elevated:   var(--color-neutral-0);
    --color-text-primary:  var(--color-neutral-900);
    --color-text-secondary: var(--color-neutral-600);
    --color-text-muted:    var(--color-neutral-400);
    --color-border-default: var(--color-neutral-200);
    --color-border-strong: var(--color-neutral-400);
    --color-focus:         var(--color-brand-primary);

    /* Feedback */
    --color-success: #10B981;
    --color-warning: #F59E0B;
    --color-danger:  #EF4444;
    --color-info:    #3B82F6;

    /* Spacing (4px base) */
    --space-0:  0;
    --space-1:  4px;
    --space-2:  8px;
    --space-3:  12px;
    --space-4:  16px;
    --space-6:  24px;
    --space-8:  32px;
    --space-12: 48px;
    --space-16: 64px;
    --space-24: 96px;

    /* Radius */
    --radius-none: 0;
    --radius-sm:   4px;
    --radius-md:   8px;
    --radius-lg:   12px;
    --radius-xl:   16px;
    --radius-full: 9999px;

    /* Typography */
    --font-sans:  Inter, system-ui, sans-serif;
    --font-serif: Merriweather, Georgia, serif;
    --font-mono:  "JetBrains Mono", monospace;

    --font-size-xs:   12px;
    --font-size-sm:   14px;
    --font-size-base: 16px;
    --font-size-lg:   18px;
    --font-size-xl:   20px;
    --font-size-2xl:  24px;
    --font-size-3xl:  30px;
    --font-size-4xl:  36px;
    --font-size-5xl:  48px;

    --line-height-tight:  1.2;
    --line-height-normal: 1.5;
    --line-height-loose:  1.75;

    --font-weight-regular:  400;
    --font-weight-medium:   500;
    --font-weight-semibold: 600;
    --font-weight-bold:     700;

    /* Motion */
    --duration-instant: 100ms;
    --duration-fast:    150ms;
    --duration-normal:  250ms;
    --duration-slow:    400ms;
    --duration-slower:  700ms;

    --easing-linear:      cubic-bezier(0, 0, 1, 1);
    --easing-ease-in:     cubic-bezier(0.4, 0, 1, 1);
    --easing-ease-out:    cubic-bezier(0, 0, 0.2, 1);
    --easing-ease-in-out: cubic-bezier(0.4, 0, 0.2, 1);
  }

  /* ----- Dark theme --------------------------------------------------------- */
  [data-theme="dark"] {
    --color-bg-primary:    var(--color-neutral-900);
    --color-bg-secondary:  var(--color-neutral-800);
    --color-bg-elevated:   var(--color-neutral-800);
    --color-text-primary:  var(--color-neutral-50);
    --color-text-secondary: var(--color-neutral-300);
    --color-text-muted:    var(--color-neutral-500);
    --color-border-default: var(--color-neutral-700);
    --color-border-strong: var(--color-neutral-500);
  }
}

/* ----- Reduced motion ------------------------------------------------------- */
@media (prefers-reduced-motion: reduce) {
  :root {
    --duration-instant: 0ms;
    --duration-fast:    0ms;
    --duration-normal:  0ms;
    --duration-slow:    0ms;
    --duration-slower:  0ms;
  }
}
```

- [ ] **Step 2: Commit**

```bash
cd "/Users/rilner/Marketing OS"
git add assets/templates/design/theme.css.template
git commit -m "$(cat <<'EOF'
feat(design/templates): add theme.css template

CSS layers + custom properties; light/dark themes; prefers-reduced-motion.

Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>
EOF
)"
```

---

### Task 4: component-spec.md.template

**Files:**
- Create: `assets/templates/design/component-spec.md.template`

**Size target:** ~300 lines.

- [ ] **Step 1: Write component spec skeleton**

Write to the file a template structured in 12 sections, each with placeholders and inline guidance:

```markdown
# Componente: {{COMPONENT_NAME}}

> **Status:** {{STATUS}} (Draft / Ready / Deprecated)
> **Versão:** {{VERSION}} (semver: major.minor.patch)
> **Última revisão:** {{DATE}}
> **Owner:** {{OWNER}}

---

## 1. Propósito

{{ONE_LINE_PURPOSE}}

**Quando usar:**
- {{USE_CASE_1}}
- {{USE_CASE_2}}

**Quando NÃO usar:**
- {{ANTI_USE_CASE_1}} — use `{{ALTERNATIVE_COMPONENT}}` em vez disso
- {{ANTI_USE_CASE_2}}

---

## 2. Anatomia

```
┌─────────────────────────────────────┐
│  [ícone]  Label principal    [seta] │  ← descrição dos slots
└─────────────────────────────────────┘
```

| Parte | Nome técnico | Opcional? |
|-------|--------------|-----------|
| {{PART_1}} | `{{part-1-slot}}` | Sim/Não |
| {{PART_2}} | `{{part-2-slot}}` | Sim/Não |

---

## 3. Props API

| Prop | Tipo | Default | Descrição |
|------|------|---------|-----------|
| `variant` | `"primary" \| "secondary" \| "ghost"` | `"primary"` | Intent visual |
| `size` | `"sm" \| "md" \| "lg"` | `"md"` | Tamanho |
| `disabled` | `boolean` | `false` | Desativa interação |
| `loading` | `boolean` | `false` | Estado de loading |
| `aria-label` | `string` | — | Label para screen readers (obrigatório se só ícone) |
| `onClick` | `(e: MouseEvent) => void` | — | Handler de clique |
| `children` | `ReactNode` | — | Conteúdo |

---

## 4. Variantes Visuais

### `primary`
- Background: `var(--color-brand-primary)`
- Text: `var(--color-text-inverse)`
- Contraste: {{X.X}}:1 (WCAG {{AA/AAA}})

### `secondary`
- Background: `transparent`
- Border: `var(--color-border-strong)`
- Text: `var(--color-text-primary)`

### `ghost`
- Background: `transparent`
- Border: `none`
- Text: `var(--color-text-primary)`

---

## 5. Estados

| Estado | Quando ativa | Visual |
|--------|--------------|--------|
| `default` | Padrão | Base |
| `hover` | Ponteiro por cima | Background ligeiramente mais escuro (8% shade) |
| `active` | Pressionado | Background mais escuro (12% shade) |
| `focus-visible` | Foco via teclado | Ring 2px `var(--color-focus)` offset 2px |
| `disabled` | `disabled=true` | Opacidade 50%, cursor `not-allowed`, sem hover |
| `loading` | `loading=true` | Spinner visível, `aria-busy="true"` |

---

## 6. Acessibilidade (WCAG 2.2)

**Requisitos obrigatórios:**
- [ ] Contraste texto/background ≥ 4.5:1 (AA) ou 7:1 (AAA)
- [ ] Target size ≥ 24×24 CSS pixels (WCAG 2.5.8)
- [ ] Focus indicator visível (WCAG 2.4.11, contrast ≥ 3:1)
- [ ] Keyboard: Enter e Space ativam
- [ ] Screen reader: anuncia label + variant + state
- [ ] `aria-label` obrigatório quando só ícone (sem texto visível)
- [ ] `aria-busy="true"` durante loading
- [ ] `aria-disabled="true"` quando disabled (em vez de `disabled` se precisa ser focável)

**Testing:**
- Axe-core: 0 violations
- NVDA/JAWS: anunciamento correto do role + label + state

---

## 7. Exemplos de Código

### React
```tsx
import { {{ComponentName}} } from '@/components/{{component-name}}';

<{{ComponentName}} variant="primary" size="md" onClick={handleClick}>
  Salvar
</{{ComponentName}}>
```

### Uso com ícone
```tsx
<{{ComponentName}} variant="ghost" aria-label="Fechar modal">
  <XIcon />
</{{ComponentName}}>
```

---

## 8. Do / Don't

### ✓ DO
- Use `primary` para ação principal da tela (máximo 1 por view)
- Use `secondary` para ações alternativas
- Mantenha labels curtos (1-3 palavras idealmente)

### ✗ DON'T
- Não use mais de 1 `primary` por view (cria competição de atenção)
- Não use só ícone sem `aria-label`
- Não embed em texto corrido; use link em vez disso

---

## 9. Figma

- **Library:** {{FIGMA_LIBRARY_LINK}}
- **Component key:** {{COMPONENT_KEY}}
- **Variants mapeadas:** variant, size, state

### Code Connect
Mapping em `{{component-name}}.figma.tsx`:
```tsx
import figma from '@figma/code-connect';
import { {{ComponentName}} } from './{{component-name}}';

figma.connect({{ComponentName}}, 'FIGMA_NODE_URL', {
  props: {
    variant: figma.enum('Variant', { Primary: 'primary', Secondary: 'secondary', Ghost: 'ghost' }),
    size:    figma.enum('Size',    { Small: 'sm', Medium: 'md', Large: 'lg' }),
    label:   figma.string('Label'),
  },
  example: (props) => <{{ComponentName}} {...props} />,
});
```

---

## 10. Tokens Usados

| Token | Uso |
|-------|-----|
| `semantic.color.bg.primary` | Background primary variant |
| `semantic.color.text.inverse` | Text primary variant |
| `component.button.radius` | Border radius |
| `component.button.padding.md` | Padding medium size |

---

## 11. Dependências

- Nenhuma / `{{DependencyComponent}}` / etc.

---

## 12. Changelog

| Versão | Data | Mudança | Breaking? |
|--------|------|---------|-----------|
| 1.0.0 | {{DATE}} | Versão inicial | — |
```

- [ ] **Step 2: Commit**

```bash
cd "/Users/rilner/Marketing OS"
git add assets/templates/design/component-spec.md.template
git commit -m "$(cat <<'EOF'
feat(design/templates): add component-spec template

12-section skeleton: purpose, anatomy, props API, variants, states,
WCAG 2.2 a11y requirements, examples, do/don't, Figma mapping, tokens,
changelog.

Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>
EOF
)"
```

---

### Task 5: ds-readme.md.template

**Files:**
- Create: `assets/templates/design/ds-readme.md.template`

**Size target:** ~200 lines.

- [ ] **Step 1: Write DS README skeleton**

Write to file (in Portuguese, following Marketing OS convention):

```markdown
# {{DS_NAME}}

> {{ONE_LINE_TAGLINE}}

![version](https://img.shields.io/badge/version-{{VERSION}}-blue)
![a11y](https://img.shields.io/badge/WCAG-2.2_AA-green)
![coverage](https://img.shields.io/badge/coverage-{{PCT}}%25-brightgreen)

**Status:** {{STATUS}} | **Última release:** {{DATE}}

---

## O que é

{{DS_NAME}} é o design system de {{COMPANY}} — biblioteca unificada de componentes, tokens e padrões para construir produtos consistentes, acessíveis e rápidos.

### Princípios

1. **{{PRINCIPLE_1}}** — {{DESCRIPTION}}
2. **{{PRINCIPLE_2}}** — {{DESCRIPTION}}
3. **{{PRINCIPLE_3}}** — {{DESCRIPTION}}

---

## Instalação

### NPM
```bash
npm install @{{ORG}}/{{DS_PACKAGE}}
```

### Yarn / PNPM
```bash
yarn add @{{ORG}}/{{DS_PACKAGE}}
# ou
pnpm add @{{ORG}}/{{DS_PACKAGE}}
```

---

## Uso Rápido

### 1. Importar o tema
```tsx
import '@{{ORG}}/{{DS_PACKAGE}}/theme.css';
```

### 2. Usar componentes
```tsx
import { Button, Card, Input } from '@{{ORG}}/{{DS_PACKAGE}}';

function App() {
  return (
    <Card>
      <Input placeholder="Seu email" />
      <Button variant="primary">Inscrever</Button>
    </Card>
  );
}
```

### 3. Trocar para dark mode
```tsx
<html data-theme="dark">...</html>
```

---

## Estrutura

```
{{DS_PACKAGE}}/
├── tokens/           # W3C design tokens (JSON)
├── theme/            # CSS compilado (light + dark)
├── components/       # Componentes React (ou framework alvo)
├── icons/            # Biblioteca de ícones
└── docs/             # Documentação (Storybook)
```

---

## Componentes

| Componente | Status | Versão | Docs |
|------------|--------|--------|------|
| Button | Stable | 1.2.0 | [link] |
| Card | Stable | 1.0.0 | [link] |
| Input | Stable | 1.1.0 | [link] |
| Modal | Beta | 0.3.0 | [link] |
| ... | ... | ... | ... |

---

## Design Tokens

3 camadas:
1. **Core** — valores base (cores neutras, espaçamento, tipografia)
2. **Semantic** — significado (background primary, text secondary)
3. **Component** — contexto específico (button padding, card radius)

Formato: W3C Design Tokens spec 2025.10. Consumir via CSS variables ou JS import.

---

## Acessibilidade

- WCAG 2.2 AA em todos componentes (target AAA)
- Tested com axe-core + NVDA + VoiceOver + Voice Control
- Keyboard-first navigation
- `prefers-reduced-motion` respeitado

---

## Contribuir

1. Leia o [CONTRIBUTING.md]
2. Abra issue para discussão antes de PR grande
3. Siga o RFC process para novos componentes
4. Todos PRs precisam: testes, docs, a11y audit, review de 2 maintainers

---

## Links

- [Storybook]({{STORYBOOK_URL}})
- [Figma Library]({{FIGMA_URL}})
- [Changelog](./CHANGELOG.md)
- [Roadmap]({{ROADMAP_URL}})

---

## Licença

{{LICENSE}} © {{YEAR}} {{COMPANY}}
```

- [ ] **Step 2: Commit**

```bash
cd "/Users/rilner/Marketing OS"
git add assets/templates/design/ds-readme.md.template
git commit -m "$(cat <<'EOF'
feat(design/templates): add DS README template

Install, usage, components table, tokens overview, a11y, contribution.

Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>
EOF
)"
```

---

### Task 6: style-dictionary.config.js.template

**Files:**
- Create: `assets/templates/design/style-dictionary.config.js.template`

**Size target:** ~150 lines.

- [ ] **Step 1: Write Style Dictionary config for multi-platform output**

Write to file:

```javascript
/**
 * Style Dictionary config — {{PROJECT_NAME}}
 * Generates multi-platform output from tokens.json (W3C Design Tokens format).
 *
 * Usage:
 *   npx style-dictionary build
 *
 * Outputs:
 *   build/web/theme.css          (CSS custom properties)
 *   build/web/tokens.js          (JS module with nested object)
 *   build/ios/tokens.swift       (Swift constants)
 *   build/android/tokens.xml     (Android resources)
 *   build/flutter/tokens.dart    (Dart constants)
 */

const StyleDictionary = require('style-dictionary');

// --- Custom transform: px -> dp for Android -------------------------------
StyleDictionary.registerTransform({
  name: 'size/pxToDp',
  type: 'value',
  matcher: (token) => token.$type === 'dimension' && token.$value.endsWith('px'),
  transformer: (token) => token.$value.replace('px', 'dp'),
});

// --- Custom transform: px -> pt for iOS -----------------------------------
StyleDictionary.registerTransform({
  name: 'size/pxToPt',
  type: 'value',
  matcher: (token) => token.$type === 'dimension' && token.$value.endsWith('px'),
  transformer: (token) => parseFloat(token.$value),
});

// --- Custom format: CSS layer ---------------------------------------------
StyleDictionary.registerFormat({
  name: 'css/theme-layer',
  formatter: ({ dictionary }) => {
    const vars = dictionary.allTokens
      .map((t) => `  --${t.name}: ${t.$value};`)
      .join('\n');
    return `@layer theme {\n  :root {\n${vars}\n  }\n}\n`;
  },
});

// --- Build config ---------------------------------------------------------
module.exports = {
  source: ['tokens.json'],

  platforms: {
    web: {
      transformGroup: 'web',
      buildPath: 'build/web/',
      files: [
        {
          destination: 'theme.css',
          format: 'css/theme-layer',
        },
        {
          destination: 'tokens.js',
          format: 'javascript/es6',
        },
        {
          destination: 'tokens.d.ts',
          format: 'typescript/es6-declarations',
        },
      ],
    },

    ios: {
      transformGroup: 'ios-swift',
      transforms: ['size/pxToPt'],
      buildPath: 'build/ios/',
      files: [
        {
          destination: 'Tokens.swift',
          format: 'ios-swift/class.swift',
          className: '{{PROJECT_CLASS_NAME}}Tokens',
        },
      ],
    },

    android: {
      transformGroup: 'android',
      transforms: ['size/pxToDp'],
      buildPath: 'build/android/',
      files: [
        {
          destination: 'colors.xml',
          format: 'android/colors',
          filter: { type: 'color' },
        },
        {
          destination: 'dimens.xml',
          format: 'android/dimens',
          filter: { type: 'dimension' },
        },
      ],
    },

    flutter: {
      transformGroup: 'flutter',
      buildPath: 'build/flutter/',
      files: [
        {
          destination: 'tokens.dart',
          format: 'flutter/class.dart',
          className: '{{PROJECT_CLASS_NAME}}Tokens',
        },
      ],
    },
  },
};
```

- [ ] **Step 2: Commit**

```bash
cd "/Users/rilner/Marketing OS"
git add assets/templates/design/style-dictionary.config.js.template
git commit -m "$(cat <<'EOF'
feat(design/templates): add Style Dictionary config template

Web/iOS/Android/Flutter output with custom transforms and CSS layer
format.

Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>
EOF
)"
```

---

### Task 7: storybook-main.ts.template

**Files:**
- Create: `assets/templates/design/storybook-main.ts.template`

**Size target:** ~100 lines.

- [ ] **Step 1: Write Storybook 8+ config with essential addons**

Write to file:

```typescript
/**
 * Storybook 8+ config — {{PROJECT_NAME}}
 * Place at `.storybook/main.ts` in your repo.
 */

import type { StorybookConfig } from '@storybook/react-vite';

const config: StorybookConfig = {
  stories: [
    '../src/**/*.mdx',
    '../src/**/*.stories.@(js|jsx|mjs|ts|tsx)',
  ],

  addons: [
    '@storybook/addon-essentials',         // controls, docs, viewport, backgrounds, actions
    '@storybook/addon-a11y',               // axe-core integration
    '@storybook/addon-interactions',       // play functions
    '@storybook/addon-links',              // cross-story links
    '@storybook/addon-themes',             // light/dark toggle
    'storybook-addon-designs',             // Figma embeds in docs
    'storybook-dark-mode',                 // theme switcher
  ],

  framework: {
    name: '@storybook/react-vite',
    options: {},
  },

  docs: {
    autodocs: 'tag',    // autodocs only for components tagged 'autodocs'
    defaultName: 'Docs',
  },

  typescript: {
    reactDocgen: 'react-docgen-typescript',
    reactDocgenTypescriptOptions: {
      shouldExtractLiteralValuesFromEnum: true,
      propFilter: (prop) => {
        if (prop.parent) return !/node_modules/.test(prop.parent.fileName);
        return true;
      },
    },
  },

  staticDirs: ['../public'],

  viteFinal: async (config) => {
    // Ensure theme.css loads first
    return config;
  },
};

export default config;
```

- [ ] **Step 2: Commit**

```bash
cd "/Users/rilner/Marketing OS"
git add assets/templates/design/storybook-main.ts.template
git commit -m "$(cat <<'EOF'
feat(design/templates): add Storybook 8+ main config template

Addons: essentials, a11y, interactions, themes, Figma designs.

Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>
EOF
)"
```

---

### Task 8: brand-guidelines.md.template

**Files:**
- Create: `assets/templates/design/brand-guidelines.md.template`

**Size target:** ~500 lines.

- [ ] **Step 1: Write 30-section brand book skeleton**

Sections to include (with placeholders for each):

1. Apresentação / Manifesto (tone, raison d'être)
2. Missão, Visão, Valores
3. Personas (3-5 personas principais)
4. Voz & Tom (matriz contexto → tom)
5. Vocabulário (on-brand / off-brand words, banned list)
6. Elevator pitches (15s, 30s, 60s)
7. Logo system (primary, secondary, lockups)
8. Logo — clear space (mínimo X de padding)
9. Logo — minimum size (px digital, mm print)
10. Logo — don'ts (8-12 casos visuais)
11. Paleta primária (cores + hex + RGB + HSL + CMYK + Pantone)
12. Paleta secundária / accent
13. Paleta funcional (success, warning, danger, info)
14. Contraste & a11y (matriz pares de cores + ratios WCAG)
15. Tipografia — famílias (display + body + UI + mono)
16. Tipografia — hierarquia (H1-H6 + body + caption + specs)
17. Tipografia — pairings e regras
18. Grid & layout (5 canvases: web / mobile / print / social / merch)
19. Direção de fotografia (style, mood, composition, color grading)
20. Sistema de ilustração (style, color, construction rules)
21. Sistema de ícones (metaphor, grid, weight, anatomy)
22. Motion principles (easing brand, timing, personality in motion)
23. Sonic brand (se aplicável — jingle, UI sounds)
24. Aplicações — digital (site, app, email, social)
25. Aplicações — print (cartão, papel timbrado, folder, outdoor)
26. Aplicações — merch (camiseta, caneca, adesivo, brindes)
27. Aplicações — ambiente (sinalização, fachada, escritório)
28. Aplicações — embalagem (produto físico)
29. Co-branding (quando usar, regras, exemplos)
30. Contato / Revisão / Changelog

For each section, write:
- Heading (##)
- 1-2 sentence purpose
- Placeholders for values (`{{BRAND_PRIMARY_HEX}}`, etc.)
- 1-2 example filled-in lines as guidance
- "Guidance:" callout on what the agent should populate when filling

Template size: ~500 lines total (each section ~15-18 lines avg).

- [ ] **Step 2: Commit**

```bash
cd "/Users/rilner/Marketing OS"
git add assets/templates/design/brand-guidelines.md.template
git commit -m "$(cat <<'EOF'
feat(design/templates): add brand guidelines 30-section template

Full brand book skeleton with placeholders and inline guidance.

Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>
EOF
)"
```

---

### Task 9: design-review.md.template

**Files:**
- Create: `assets/templates/design/design-review.md.template`

**Size target:** ~150 lines.

- [ ] **Step 1: Write design review checklist**

Write to file:

```markdown
# Design Review — {{ARTIFACT_NAME}}

> **Reviewer:** {{REVIEWER}}
> **Data:** {{DATE}}
> **Artefato:** {{ARTIFACT_TYPE}} ({{COMPONENT/SCREEN/BRAND/CAMPAIGN}})
> **Veredito:** {{PASS / CONCERNS / FAIL}}

---

## Contexto

{{BRIEF_SUMMARY}}

**Links:**
- Figma: {{FIGMA_LINK}}
- Spec: {{SPEC_LINK}}
- Brief: {{BRIEF_LINK}}

---

## Checklist (15 pontos)

### Estratégia & Propósito
- [ ] **1. Alinhado com brief** — entrega o que foi pedido
- [ ] **2. Audience clara** — sabe pra quem está falando
- [ ] **3. Mensagem/hierarquia** — ponto principal identificável em ≤ 3s

### Hierarquia Visual
- [ ] **4. Hierarquia tipográfica** — H1 > H2 > H3 > body é visualmente clara
- [ ] **5. Focal point** — um ponto principal de atenção (não competindo)
- [ ] **6. White space** — respira, não é denso demais

### Cor & Contraste
- [ ] **7. Paleta coerente** — usa tokens da marca, sem cores ad-hoc
- [ ] **8. Contraste WCAG 2.2 AA** — todos pares texto/bg ≥ 4.5:1 (normal) / 3:1 (large)
- [ ] **9. Dark mode funcional** — não é só inversão; testado

### Tipografia
- [ ] **10. Famílias corretas** — usa fontes do DS, sem extras
- [ ] **11. Scale consistente** — usa tokens de font-size; não arbitrário
- [ ] **12. Line-height adequado** — 1.5 para body, 1.2 para display

### Layout & Grid
- [ ] **13. Grid respeitado** — alinhamento em colunas definidas
- [ ] **14. Responsive** — testado em mobile / tablet / desktop
- [ ] **15. Densidade consistente** — spacing uniforme, não ad-hoc

---

## Severity Matrix

| Severidade | Descrição | Ação |
|------------|-----------|------|
| **Critical** | Bloqueia release. Quebra a11y, marca, ou funcionalidade. | Bloquear merge; corrigir antes |
| **High** | Afeta experiência significativamente. Deve corrigir antes do release. | Corrigir nesse ciclo |
| **Medium** | Melhoria notável mas não bloqueante. | Criar tech debt ticket |
| **Low** | Nitpick, polimento. | Opcional; documentar |

---

## Issues Encontrados

### Critical
{{#each critical}}
- **{{title}}** — {{description}}
  - *Localização:* {{where}}
  - *Fix sugerido:* {{fix}}
{{/each}}

### High
...

### Medium
...

### Low
...

---

## Veredito Final

**{{PASS / CONCERNS / FAIL}}**

**Rubrica:**
- **PASS:** Zero Critical, ≤ 2 High
- **CONCERNS:** Zero Critical, 3-5 High (aprovado com fixes documentados)
- **FAIL:** ≥ 1 Critical OU ≥ 6 High (retorna para revisão)

**Próximos passos:**
- {{ACTION_1}}
- {{ACTION_2}}

---

## Aprovação

- [ ] Reviewer: {{REVIEWER}} — {{DATE}}
- [ ] Design Lead: {{DESIGN_LEAD}} — {{DATE}}
- [ ] Produto/Owner: {{PRODUCT_OWNER}} — {{DATE}}
```

- [ ] **Step 2: Commit**

```bash
cd "/Users/rilner/Marketing OS"
git add assets/templates/design/design-review.md.template
git commit -m "$(cat <<'EOF'
feat(design/templates): add design review template

15-point checklist + severity matrix + PASS/CONCERNS/FAIL rubric.

Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>
EOF
)"
```

---

## Phase 2 — Companions (10 tasks)

Deep knowledge documents. Each companion is a self-contained playbook.

**Author-time instructions that apply to all companion tasks:**
- Write in Portuguese (system language).
- Zero em-dash `—` except where syntactically necessary.
- Each companion starts with: title (h1), 1-line description, index/TOC, then sections.
- Reference other companions by relative path: `../design/XX-filename.md`.
- Reference agent by: `../../subagents/design-agent.md`.
- WebSearch before citing any statistic, study, or named person — confirm exists and the claim is accurate. Mark illustrative examples explicitly.
- No self-proclaimed superlatives.
- Use tables, lists, and code blocks liberally — these are reference docs.

### Task 10: `references/design/01-tokens-w3c-spec.md`

**Files:**
- Create: `references/design/01-tokens-w3c-spec.md`

**Size target:** 1.000-1.300 linhas.

**Source material:** W3C Design Tokens Community Group spec 2025.10 (verify current version via WebSearch before authoring).

- [ ] **Step 1: Write file outline and introduction**

Sections (each will be filled with detailed content):
1. O que é W3C Design Tokens (spec status, goals, adoption)
2. Anatomia de um token ($value, $type, $description, $extensions)
3. Os 13 tipos oficiais (color, dimension, fontFamily, fontWeight, duration, cubicBezier, shadow, border, gradient, transition, typography, number, composite)
4. Referências e alias (`{core.color.brand.primary}`)
5. Hierarquia de grupos (nesting + naming conventions)
6. Arquitetura 3-camadas (core → semantic → component)
7. Exemplo completo: tokens.json de projeto real
8. Theming (light/dark/multi-brand)
9. Responsive tokens (breakpoint-specific values)
10. Style Dictionary pipeline (como transformar para CSS/iOS/Android/Flutter)
11. Tokens Studio plugin (Figma workflow)
12. Validation & linting (JSON schema, tipagem TS)
13. Versionamento de tokens (semver, deprecation)
14. Integrações (Tailwind, shadcn/ui, Material, Fluent)
15. Anti-patterns (tokens arbitrários, nomeação inconsistente, vazamento de valores)
16. FAQ

- [ ] **Step 2: Write each section with concrete examples**

Mandatory inclusions:
- Full working tokens.json example (~50 tokens minimum)
- Style Dictionary config snippet producing CSS + iOS + Android output
- Comparison table: tokens W3C vs Tailwind config vs shadcn variables
- Naming convention rules (kebab-case for JSON keys? camelCase? — reference official)

- [ ] **Step 3: Validate no broken references and size target**

Run:
```bash
cd "/Users/rilner/Marketing OS"
wc -l references/design/01-tokens-w3c-spec.md
```
Expected: between 1000 and 1300.

- [ ] **Step 4: Commit**

```bash
cd "/Users/rilner/Marketing OS"
git add references/design/01-tokens-w3c-spec.md
git commit -m "$(cat <<'EOF'
feat(design/references): add W3C tokens spec companion (01)

Full W3C Design Tokens spec coverage: 13 types, 3-layer architecture,
Style Dictionary pipeline, Tokens Studio workflow, validation, theming,
anti-patterns, integrations.

Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>
EOF
)"
```

---

### Task 11: `references/design/02-atomic-design-playbook.md`

**Files:**
- Create: `references/design/02-atomic-design-playbook.md`

**Size target:** 800-1.000 linhas.

- [ ] **Step 1: Write outline**

Sections:
1. Atomic Design — contexto histórico (Brad Frost, 2013, evolução até 2026)
2. Os 6 níveis (Tokens + Atoms + Molecules + Organisms + Templates + Pages)
3. Como decidir o nível de um componente (decision tree)
4. Atoms — princípios + 12 exemplos concretos
5. Molecules — princípios + 10 exemplos
6. Organisms — princípios + 8 exemplos
7. Templates — layouts sem conteúdo
8. Pages — instâncias concretas
9. Naming conventions por nível
10. Variant systems (Figma variants + code variants)
11. Composition patterns (slot, children, render props, compound components)
12. Anti-patterns (over-abstraction, premature composition, level confusion)
13. Atomic design + tokens = combinação poderosa
14. Migração: quando promover ou rebaixar um componente
15. 12 exemplos end-to-end (Button, Card, Form, Modal, Table, Nav, Hero, etc.)

- [ ] **Step 2: Write sections with Figma + code examples for each**

For each of the 12 end-to-end examples, show:
- Figma structure (variants)
- Code API (props)
- Where tokens plug in
- Do/Don't

- [ ] **Step 3: Validate**

```bash
cd "/Users/rilner/Marketing OS"
wc -l references/design/02-atomic-design-playbook.md
```
Expected: 800-1000.

- [ ] **Step 4: Commit**

```bash
cd "/Users/rilner/Marketing OS"
git add references/design/02-atomic-design-playbook.md
git commit -m "$(cat <<'EOF'
feat(design/references): add atomic design playbook (02)

Brad Frost 6 levels applied, decision criteria per level, naming
conventions, variant systems, composition patterns, anti-patterns,
12 end-to-end examples.

Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>
EOF
)"
```

---

### Task 12: `references/design/03-ds-governance.md`

**Files:**
- Create: `references/design/03-ds-governance.md`

**Size target:** 600-800 linhas.

- [ ] **Step 1: Write outline**

Sections:
1. Por que governance importa (exemplos de DS que falharam por falta)
2. Semver aplicado a DS (major / minor / patch para componentes e tokens)
3. RFC process (template, fluxo, sign-offs)
4. Modelo de contribuição (core team + community, roles)
5. Design review rituals (cadence, checklist, owners)
6. Deprecation policy (sunset timeline, migration guides, comms)
7. Breaking changes (detecção, comunicação, rollback)
8. Release cadence (weekly / monthly / on-demand)
9. Metrics (adoption rate, consistency score, token compliance, debt tracker)
10. Contribution checklist (tests, docs, a11y audit, approvals)
11. Roadmap template + backlog prioritization
12. Governance comms (changelog, release notes, Slack, email digest)
13. External contributions (fork model, CLA)
14. 3 real-world case studies (Carbon IBM, Polaris Shopify, Lightning Salesforce)

- [ ] **Step 2: Write sections + include RFC template inline**

RFC template should cover: problem, proposed solution, alternatives considered, impact, migration path, success metrics.

- [ ] **Step 3: Validate**

```bash
cd "/Users/rilner/Marketing OS"
wc -l references/design/03-ds-governance.md
```
Expected: 600-800.

- [ ] **Step 4: Commit**

```bash
cd "/Users/rilner/Marketing OS"
git add references/design/03-ds-governance.md
git commit -m "$(cat <<'EOF'
feat(design/references): add DS governance companion (03)

Semver, RFC process, contribution model, deprecation, metrics,
release cadence, case studies (Carbon/Polaris/Lightning).

Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>
EOF
)"
```

---

### Task 13: `references/design/04-accessibility-wcag22.md`

**Files:**
- Create: `references/design/04-accessibility-wcag22.md`

**Size target:** 900-1.100 linhas.

- [ ] **Step 1: Write outline**

Sections:
1. WCAG 2.2 — o que mudou vs 2.1 (9 novos success criteria)
2. Princípios POUR (Perceivable, Operable, Understandable, Robust)
3. Níveis A, AA, AAA (o que entregar)
4. Contraste — tabela completa (texto normal 4.5:1, large 3:1, UI components 3:1, non-text 3:1)
5. Focus indicators (2.4.11, 2.4.12, 2.4.13 novos)
6. Target size (2.5.8 — 24×24 CSS pixels mínimo)
7. Dragging movements (2.5.7 — sempre oferecer alternativa)
8. Consistent help (3.2.6 — help em mesma localização)
9. Redundant entry (3.3.7 — não pedir mesma info 2x)
10. Accessible authentication (3.3.8 — não exigir cognitive test)
11. Checklist por componente — Button
12. Checklist — Input/Form
13. Checklist — Modal/Dialog
14. Checklist — Table/DataGrid
15. Checklist — Navigation/Menu
16. Checklist — Toast/Notification
17. Patterns ARIA essenciais (live regions, aria-describedby, aria-expanded, roles)
18. Keyboard navigation patterns (Tab order, Esc dismisses, arrow keys in composites)
19. Screen reader behavior (NVDA, JAWS, VoiceOver, TalkBack)
20. Cognitive a11y (plain language, predictability, consistency)
21. Motor a11y (click targets, drag alternatives, debounced inputs)
22. Testing toolkit (axe-core, Lighthouse, pa11y, WAVE, manual screen reader)
23. Automated testing in CI (GitHub Actions example)
24. Common failures + quick fixes (top 20)
25. Role-based checklists (designer, dev, QA, content)

- [ ] **Step 2: Write with code examples (HTML + ARIA + CSS) for each pattern**

Each component checklist shows:
- Minimum ARIA roles/attrs
- Keyboard contract
- Focus management code
- Screen reader expectations

- [ ] **Step 3: Validate**

```bash
cd "/Users/rilner/Marketing OS"
wc -l references/design/04-accessibility-wcag22.md
```
Expected: 900-1100.

- [ ] **Step 4: Commit**

```bash
cd "/Users/rilner/Marketing OS"
git add references/design/04-accessibility-wcag22.md
git commit -m "$(cat <<'EOF'
feat(design/references): add WCAG 2.2 accessibility companion (04)

9 new 2.2 criteria, POUR principles, per-component checklists (Button/
Input/Modal/Table/Nav/Toast), ARIA patterns, keyboard contracts, SR
expectations, testing toolkit, common failures + fixes.

Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>
EOF
)"
```

---

### Task 14: `references/design/05-motion-spec.md`

**Files:**
- Create: `references/design/05-motion-spec.md`

**Size target:** 500-700 linhas.

- [ ] **Step 1: Write outline**

Sections:
1. Por que motion importa (comunicação, orientação, feedback, continuidade)
2. Motion tokens (duration: 100/150/250/400/700ms; easing library)
3. Easing curves explicadas (ease-out para enter, ease-in para exit, standard cubic-bezier)
4. Choreography (stagger, parallel, sequential, orchestrated)
5. 12 princípios de animação (Disney) aplicados a UI (squash/stretch, anticipation, follow-through, etc.)
6. Reduced motion (prefers-reduced-motion, como respeitar)
7. Motion grammar (entry, exit, emphasis, state change, loading, error)
8. Component-level recipes (modal enter, toast pop, button press, page transition, skeleton pulse)
9. Micro-interactions (hover, focus, active, success confirmation)
10. Performance (GPU-accelerated props, will-change, transform/opacity only)
11. Tools comparison (CSS transitions, Framer Motion, Lottie, Rive, GSAP, Web Animations API)
12. Quando usar qual tool (decision tree)
13. Motion in brand (personality expression)
14. Anti-patterns (bouncy everything, distracting loops, 1s+ durations, auto-play videos)
15. Testing motion (screen recording, stutter detection, reduced-motion QA)

- [ ] **Step 2: Write with CSS + Framer Motion code examples**

Each recipe shows CSS implementation + Framer Motion equivalent + when each is preferable.

- [ ] **Step 3: Validate**

```bash
cd "/Users/rilner/Marketing OS"
wc -l references/design/05-motion-spec.md
```
Expected: 500-700.

- [ ] **Step 4: Commit**

```bash
cd "/Users/rilner/Marketing OS"
git add references/design/05-motion-spec.md
git commit -m "$(cat <<'EOF'
feat(design/references): add motion spec companion (05)

Motion tokens, easing library, choreography, Disney 12 principles for
UI, reduced-motion, component recipes, tool comparison, performance,
anti-patterns.

Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>
EOF
)"
```

---

### Task 15: `references/design/06-brand-system-blueprint.md`

**Files:**
- Create: `references/design/06-brand-system-blueprint.md`

**Size target:** 1.300-1.600 linhas.

- [ ] **Step 1: Write outline matching brand-guidelines template**

30 sections corresponding to brand-guidelines.md.template (from Task 8), but this time with DEEP guidance, examples, frameworks, anti-patterns instead of placeholders.

Each section covers:
- O que é e por que importa
- Framework decisório
- 3-5 exemplos reais de marcas conhecidas
- Common pitfalls
- Template de documentação

Extract and expand from v3.1 sections 16 (Sistema de Marca), 14 (Design Cultural), 22 (Fotografia), 23 (Print).

- [ ] **Step 2: Write with brand case studies**

Reference case studies: Airbnb, Stripe, Linear, Notion, Duolingo, Mailchimp (verify brand references/evolutions are current via WebSearch).

- [ ] **Step 3: Validate**

```bash
cd "/Users/rilner/Marketing OS"
wc -l references/design/06-brand-system-blueprint.md
```
Expected: 1300-1600.

- [ ] **Step 4: Commit**

```bash
cd "/Users/rilner/Marketing OS"
git add references/design/06-brand-system-blueprint.md
git commit -m "$(cat <<'EOF'
feat(design/references): add brand system blueprint (06)

30-section brand book depth: logo, palette, typography, voice/tone,
vocabulary, photography, illustration, icon system, motion, sonic,
applications (digital/print/merch/env), architecture, co-branding.

Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>
EOF
)"
```

---

### Task 16: `references/design/07-figma-mcp-playbook.md`

**Files:**
- Create: `references/design/07-figma-mcp-playbook.md`

**Size target:** 450-550 linhas.

- [ ] **Step 1: Write outline**

Sections:
1. O ecossistema Figma MCP do user (skills: figma-generate-library, figma-use, figma-generate-design, figma-implement-design, figma-code-connect, figma-create-design-system-rules)
2. Quando invocar cada skill (decision tree)
3. Ordem correta de build: variables → styles → components → variants → libraries
4. Prompt patterns que funcionam vs falham
5. Setup: Figma Dev Mode + Code Connect
6. Workflow: code codebase → Figma library (figma-generate-library)
7. Workflow: Figma design → production code (figma-implement-design)
8. Workflow: page from code → Figma screen (figma-generate-design)
9. Workflow: design system rules (figma-create-design-system-rules)
10. Common gotchas (missing variables, unit mismatches, variant explosion)
11. Handoff patterns designer → dev
12. Files organization (published library vs consumer files)
13. Version control of Figma files
14. Troubleshooting (when MCP fails, fallbacks)

- [ ] **Step 2: Write with concrete skill-invocation examples**

Each skill gets 1-2 full example invocations showing: user request → agent reasoning → skill call → expected outcome.

- [ ] **Step 3: Validate**

```bash
cd "/Users/rilner/Marketing OS"
wc -l references/design/07-figma-mcp-playbook.md
```
Expected: 450-550.

- [ ] **Step 4: Commit**

```bash
cd "/Users/rilner/Marketing OS"
git add references/design/07-figma-mcp-playbook.md
git commit -m "$(cat <<'EOF'
feat(design/references): add Figma MCP playbook (07)

When/how to invoke figma-generate-library, figma-use, figma-generate-design,
figma-implement-design, figma-code-connect, figma-create-design-system-rules.
Prompt patterns, workflows, gotchas, handoff.

Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>
EOF
)"
```

---

### Task 17: `references/design/08-shadcn-integration.md`

**Files:**
- Create: `references/design/08-shadcn-integration.md`

**Size target:** 350-500 linhas.

- [ ] **Step 1: Write outline**

Sections:
1. O que é shadcn/ui (copy-paste component library, não npm package)
2. Quando usar `vercel:shadcn` skill
3. Instalação + init (`npx shadcn init`)
4. Componentes disponíveis e quando adicionar cada
5. Custom registries — criar DS privado em cima do shadcn
6. Theming via CSS variables (alinhar com tokens W3C)
7. Composition patterns (wrappers, variants, extensions)
8. Coexistência com DS próprio (shadcn como base, DS como camada)
9. Migração de outros DS → shadcn
10. Anti-patterns (re-abstract componentes, duplicar lógica, fighting shadcn conventions)
11. 5 exemplos concretos (Button customizado, Form completo, Dashboard, Landing page)

- [ ] **Step 2: Write with shadcn CLI commands + code**

Show real `npx shadcn add` commands and how to customize after.

- [ ] **Step 3: Validate**

```bash
cd "/Users/rilner/Marketing OS"
wc -l references/design/08-shadcn-integration.md
```
Expected: 350-500.

- [ ] **Step 4: Commit**

```bash
cd "/Users/rilner/Marketing OS"
git add references/design/08-shadcn-integration.md
git commit -m "$(cat <<'EOF'
feat(design/references): add shadcn integration companion (08)

When to use vercel:shadcn, custom registries, theming with W3C tokens,
composition patterns, DS coexistence, migration paths, anti-patterns.

Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>
EOF
)"
```

---

### Task 18: `references/design/09-handoff-to-code.md`

**Files:**
- Create: `references/design/09-handoff-to-code.md`

**Size target:** 600-800 linhas.

- [ ] **Step 1: Write outline**

Sections:
1. Por que handoff quebra (causas comuns)
2. Princípio: tokens são a única fonte de verdade
3. Pipeline: tokens.json → Style Dictionary → [web / iOS / Android / Flutter]
4. Figma Code Connect setup (passo-a-passo)
5. Component documentation: Storybook + MDX
6. Design-to-code review rituals (checkpoint gates)
7. Change propagation: token change → auto PR → preview deploy
8. Tooling (Figma Dev Mode, Zeplin, Abstract, Avocode — comparação)
9. Checklists: designer entrega / dev recebe
10. Handoff de motion (how to spec animations for devs)
11. Handoff de estados interativos (hover, focus, loading, error)
12. Handoff de responsive (mobile/tablet/desktop specs)
13. Handoff de a11y (quem garante o quê)
14. CI/CD para DS (build + publish + consume)
15. Monorepo vs multi-repo trade-offs
16. Tipagem forte (TypeScript definitions geradas de tokens)

- [ ] **Step 2: Write with CI config examples (GitHub Actions)**

Include actual `.github/workflows/ds-release.yml` example showing build → test → publish → notify.

- [ ] **Step 3: Validate**

```bash
cd "/Users/rilner/Marketing OS"
wc -l references/design/09-handoff-to-code.md
```
Expected: 600-800.

- [ ] **Step 4: Commit**

```bash
cd "/Users/rilner/Marketing OS"
git add references/design/09-handoff-to-code.md
git commit -m "$(cat <<'EOF'
feat(design/references): add design-to-code handoff companion (09)

Tokens pipeline, Code Connect setup, Storybook+MDX, review rituals,
CI/CD, monorepo trade-offs, responsive/motion/a11y handoff.

Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>
EOF
)"
```

---

### Task 19: `references/design/10-orchestration-routes.md`

**Files:**
- Create: `references/design/10-orchestration-routes.md`

**Size target:** 700-900 linhas.

**Note:** This is the CENTRAL orchestration document. Write it carefully — it's the core of the hybrid model.

- [ ] **Step 1: Write outline**

Sections:
1. Modelo híbrido explicado (Builder + Orchestrator)
2. Princípio de decisão: build simples, delegate complexo
3. Mapa de skills disponíveis (nome + propósito + quando)
4. DECISION TREE MESTRE (flowchart: request → branch → action)
5. Rotas para DESIGN SYSTEM (15 cenários)
6. Rotas para FIGMA work (10 cenários)
7. Rotas para CODE IMPLEMENTATION (8 cenários)
8. Rotas para BRAND work (8 cenários)
9. Rotas para MARKETING CONTENT (12 cenários — social, ads, email, landing)
10. Rotas para AI IMAGE/VIDEO generation (6 cenários)
11. Rotas para A11Y AUDIT (4 cenários)
12. Rotas para DESIGN REVIEW (3 cenários)
13. Fallbacks quando skill indisponível
14. Integration com outros subagentes Marketing OS (@copy, @ads, @social, @video, @email)
15. Exemplos de orquestração complexa (5 end-to-end: "crie um DS", "lance uma marca", "campanha integrada")

- [ ] **Step 2: Write each route as a concrete rule**

Format for each route:
```
ROUTE: [name]
TRIGGER: [what user asks]
DECISION: [what agent decides internally]
ACTION: [Build directly | Invoke skill X | Delegate to subagent Y | Ask user for Z]
OUTPUT: [what the user gets]
EXAMPLE: [real user request + agent response]
```

Total: 60-70 routes catalogued.

- [ ] **Step 3: Validate all referenced skills exist in user's environment**

Run:
```bash
cd "/Users/rilner/Marketing OS"
grep -oE "figma:[a-z-]+|vercel:[a-z-]+|frontend-design:[a-z-]+|document-skills:[a-z-]+" references/design/10-orchestration-routes.md | sort -u
```

Cross-check the output list against the skills available in the user's environment (verified at session start: `figma:figma-generate-library`, `figma:figma-use`, `figma:figma-generate-design`, `figma:figma-implement-design`, `figma:figma-code-connect`, `figma:figma-create-design-system-rules`, `vercel:shadcn`, `frontend-design:frontend-design`, `document-skills:frontend-design`, `document-skills:brand-guidelines`, `document-skills:canvas-design`, `document-skills:algorithmic-art`, `document-skills:webapp-testing`).

Every skill mentioned must exist. If any don't, remove the route or flag it.

- [ ] **Step 4: Validate size**

```bash
cd "/Users/rilner/Marketing OS"
wc -l references/design/10-orchestration-routes.md
```
Expected: 700-900.

- [ ] **Step 5: Commit**

```bash
cd "/Users/rilner/Marketing OS"
git add references/design/10-orchestration-routes.md
git commit -m "$(cat <<'EOF'
feat(design/references): add orchestration routes companion (10)

Core hybrid model: 60+ decision routes mapping user requests to
actions (build directly / invoke skill / delegate subagent). Covers
DS, Figma, code, brand, marketing, AI gen, a11y, reviews.

Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>
EOF
)"
```

---

## Phase 3 — Agent v4.0 (5 tasks)

Now write the new agent. Extract from `design-agent-v3.1-archive.md` per spec §7 and integrate orchestration.

**Strategy:** Build sections progressively, committing each chunk. Assemble into final file at the end.

### Task 20: Agent skeleton + sections §1-4

**Files:**
- Create: `subagents/design-agent.md` (new file; the canonical will reappear via this write)

**Size after this task:** ~400 lines (partial agent).

- [ ] **Step 1: Write frontmatter and sections §1-4**

Write to `subagents/design-agent.md`:

Content outline:
```markdown
# Design Agent v4.0 — Full-Stack Design Intelligence
> Marketing + Produto + Design System + Brand | Abril 2026

Subagente de design full-stack do Marketing OS. Combina direção
criativa, design visual, UX, acessibilidade, motion, geração de IA e
engenharia de design system. Opera em modelo híbrido: constrói
artefatos leves direto (tokens, specs, brand books, briefings,
prompts) e orquestra skills especializadas para trabalho pesado
(Figma libraries, componentes React, DS completo em código).

---

## Índice

1. Quando Acionar
2. Mental Model
3. Orchestration Routes
4. Builder Mode
5. Design Principles (condensado)
6. Percepção Visual
7. Cor + Tipografia + Composição (essentials)
8. Geração de Imagens com IA
9. Design System — Build Flow
10. Brand System — Build Flow
11. Marketing Content Playbooks
12. Motion + Video
13. Acessibilidade
14. Quality Gate
15. Integration com Marketing OS

---

## 1. Quando Acionar

- Criar identidade visual de marca (pessoal, produto, empresa)
- Desenhar componente UI ou tela de produto
- Iniciar ou evoluir design system (tokens, components, governance)
- Gerar prompts para imagem/vídeo com IA
- Produzir direção visual para marketing (post, thumbnail, carrossel, VSL)
- Brand book completo ou audit de marca
- A11y audit (WCAG 2.2)
- Design review de artefato
- Handoff design → código
- Coordenar work entre design, copy, ads, video (via outros subagentes)
- Quando quiser começar do zero vs iterar existente

---

## 2. Mental Model: Como Este Agente Pensa

Triagem em 3 passos:

### Passo 1 — Qual domínio?
- Marketing content? → §11
- Product UI? → §9 (DS) + companion 02 (atomic)
- Brand identity? → §10 + companion 06
- Design system? → §9 + companions 01, 02, 03, 07, 08, 09
- A11y audit? → §13 + companion 04
- Motion? → §12 + companion 05

### Passo 2 — Construir direto ou delegar?
- Lightweight artifact (tokens.json, spec.md, brand book md, prompt IA, social direction) → Builder Mode (§4)
- Heavy work (Figma library, React components production, shadcn integration) → Orchestrate (§3)

### Passo 3 — Qual skill/subagente?
Seguir decision tree em §3 e companion 10.

---

## 3. Orchestration Routes

[Compact version — full 60+ routes in `references/design/10-orchestration-routes.md`]

### Top 15 rotas mais comuns

| Request | Action |
|---------|--------|
| "Criar DS pro meu app" | Asks 5 qs → tokens.json (build) → `figma:figma-generate-library` (Figma lib) → `vercel:shadcn` ou `frontend-design` (code) |
| "Gere tokens W3C pra X" | Builder (fills tokens.json.template) |
| "Crie component Button" | `figma:figma-generate-library` OU `vercel:shadcn` OU `frontend-design` depending on target |
| "Brand book pra minha marca" | Builder (fills brand-guidelines.md.template) + companion 06 |
| "Audit a11y desse componente" | Builder (fills design-review template) + companion 04 checklist |
| "Post Instagram carrossel sobre X" | Builder (visual direction + AI prompt) + delegate @copywriter-agent if copy needed |
| "Thumbnail YouTube sobre Y" | Builder (direction + AI prompt via GPT Image 1.5 / Midjourney V7) |
| "Handoff desse design pro dev" | Companion 09 + `figma:figma-code-connect` |
| "Implement esse Figma em React" | `figma:figma-implement-design` |
| "Landing page de produto" | `frontend-design:frontend-design` |
| "Custom poster/art" | `document-skills:canvas-design` ou `document-skills:algorithmic-art` |
| "Teste meu app no browser" | `document-skills:webapp-testing` (acessibilidade via axe) |
| "Escrever regras de DS pro codebase" | `figma:figma-create-design-system-rules` |
| "Desenhar screen a partir de código" | `figma:figma-generate-design` |
| "Aplicar brand da Anthropic em X" | `document-skills:brand-guidelines` |

Deep routes em companion `references/design/10-orchestration-routes.md`.

---

## 4. Builder Mode: Artefatos Que Este Agente Gera Direto

O agente preenche estes templates (em `assets/templates/design/`):

| Template | O que gera | Quando |
|----------|------------|--------|
| `tokens.json.template` | Tokens W3C 3 camadas | Request DS do zero ou upgrade token system |
| `theme.css.template` | CSS variables | Após tokens definidos |
| `component-spec.md.template` | Spec de componente (12 seções) | Para documentar cada componente |
| `ds-readme.md.template` | README inicial do DS | Bootstrap de DS |
| `style-dictionary.config.js.template` | Pipeline multi-platform | Setup de build de tokens |
| `storybook-main.ts.template` | Config Storybook 8+ | Setup de docs |
| `brand-guidelines.md.template` | Brand book 30 seções | Request de brand book |
| `design-review.md.template` | Review checklist | Request de review/audit |

Além disso, gera direto (sem template):
- Briefings visuais para designers humanos
- Prompts de IA (GPT Image 1.5, Midjourney V7, FLUX.2, Ideogram 3.0, Recraft V3)
- Direção visual para social posts (specs + prompt + copy brief)
- Mood boards (descritivos)
- Design decisions log
- Token diff reports
```

Write the full content for sections 1-4 (~400 lines).

- [ ] **Step 2: Commit partial**

```bash
cd "/Users/rilner/Marketing OS"
git add subagents/design-agent.md
git commit -m "$(cat <<'EOF'
feat(design-agent): v4.0 skeleton + sections §1-4 (triggers, mental
model, orchestration routes, builder mode)

WIP — remaining sections in follow-up commits.

Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>
EOF
)"
```

---

### Task 21: Agent sections §5-8 (principles, perception, essentials, AI images)

**Files:**
- Modify: `subagents/design-agent.md` (append sections §5-8)

**Size after this task:** ~1.000 lines (cumulative).

- [ ] **Step 1: Extract content from v3.1 archive**

Read source from `subagents/design-agent-v3.1-archive.md`:
- Section 3 "Os 10 Mandamentos do Design (Dieter Rams)" → condense for §5
- Section 2 "A Ciência da Percepção Visual" → condense for §6
- Sections 5 (cores), 6 (tipografia), 7 (composição) → extract essentials for §7 (deep → companions 02, 06)
- Section 17 "Geração de Imagens com IA" → preserve integral for §8

- [ ] **Step 2: Append sections §5-8 to agent**

§5 Design Principles — condensed (~150 lines):
- Rams 10 Mandamentos (list + one-line each)
- Vignelli canon (5-6 principles)
- Paul Rand key insights (brand simplicity)
- Paula Scher (scale + personality)
- Quando aplicar qual framework
- → Deep dive em companions 02, 06

§6 Percepção Visual — condensed (~150 lines):
- 13ms imagem vs 250ms texto
- Hierarquia de atenção (movimento, rostos, cores, contraste, padrões)
- Leis Gestalt (proximidade, similaridade, continuidade, fechamento, figura/fundo)
- Lei Hick-Hyman
- Lei Miller (7±2)
- Lei Fitts
- → Deep em companion 02

§7 Cor + Tipografia + Composição — essentials (~200 lines):
- Cor: roda cromática, harmonias (complementar, triádica, análoga), temperatura, psicologia
- Tipografia: display vs body vs UI, escala modular (1.2, 1.25, 1.333), pareamento serif+sans
- Composição: grid (12-col, 8pt), regra dos terços, golden ratio, white space
- → Deep em companions 02, 06

§8 Geração de Imagens com IA 2026 (~500 lines):
- **Preserve 95% do conteúdo do v3.1 §17** (é excelente)
- Update: verify model names and capabilities via WebSearch (GPT Image 1.5, Midjourney V7, FLUX.2, Ideogram 3.0, Recraft V3 — ensure these are current April 2026)
- Prompt engineering patterns por plataforma
- Tabela comparativa (strengths / weaknesses / best for / pricing)
- Prompts para: portrait, product photo, illustration, infographic, thumbnail, social ad
- Negative prompting
- Seeding + reproducibility
- Upscaling + post-processing

- [ ] **Step 3: Validate cumulative size**

```bash
cd "/Users/rilner/Marketing OS"
wc -l subagents/design-agent.md
```
Expected: ~900-1100.

- [ ] **Step 4: Commit**

```bash
cd "/Users/rilner/Marketing OS"
git add subagents/design-agent.md
git commit -m "$(cat <<'EOF'
feat(design-agent): v4.0 §5-8 (principles, perception, color+type+
composition, AI images)

Condensed from v3.1 archive. AI images section preserved integral
with current April 2026 model specs.

Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>
EOF
)"
```

---

### Task 22: Agent sections §9-11 (DS overview, brand overview, marketing playbooks)

**Files:**
- Modify: `subagents/design-agent.md` (append §9-11)

**Size after this task:** ~1.600 lines (cumulative).

- [ ] **Step 1: Write §9 Design System — Build Flow (~200 lines)**

- Quando criar DS (sinais: 3+ produtos, 5+ devs, inconsistência visível)
- Atomic design 6 níveis (Tokens → Atoms → Molecules → Organisms → Templates → Pages)
- Build flow: briefing → tokens → atoms → molecules → organisms → library
- Ordem de decisão (mobile-first, dark-ready, a11y-first)
- Deep → companions 01, 02, 03, 07, 08, 09

- [ ] **Step 2: Write §10 Brand System — Build Flow (~150 lines)**

- Quando criar brand (nova marca, rebrand, extensão)
- Brand elements: logo + cor + tipo + voz + tom + vocabulário
- Build flow: discovery → strategy → identity → application → guidelines
- Deep → companion 06

- [ ] **Step 3: Write §11 Marketing Content Playbooks (~350 lines)**

Extract from v3.1: §§ 8 (Design para Conversão), 9 (Visual Storytelling), 15 (Specs por Plataforma), 19 (Viz Dados), 20 (E-Commerce), 21 (Apresentações), 25 (Video Design), 26 (Posts Prontos Híbrido), 27 (Templates Nicho).

Subsections:
- Social feed posts (Instagram/LinkedIn/TikTok/Twitter): specs + composition + conversion levers
- Stories/Reels/Shorts: 9:16 specs, safe zones, motion
- Thumbnails (YouTube): formula + 12 examples
- Carrosséis: storytelling visual + swipe mechanics
- VSL/Sales video: visual pacing
- Landing pages: hero + social proof + CTA visual hierarchy
- E-commerce: product cards, PDP, checkout
- Apresentações: slide design principles
- Data viz: minimal chart junk, sanewatches
- Ads (Meta/Google/TikTok): specs + conversion principles
- Email: layout, CTA, dark mode compat
- Posts Prontos Híbrido (preserve do v3.1): sistema de templates ativáveis

- [ ] **Step 4: Validate**

```bash
cd "/Users/rilner/Marketing OS"
wc -l subagents/design-agent.md
```
Expected: ~1500-1700.

- [ ] **Step 5: Commit**

```bash
cd "/Users/rilner/Marketing OS"
git add subagents/design-agent.md
git commit -m "$(cat <<'EOF'
feat(design-agent): v4.0 §9-11 (DS build flow, brand build flow,
marketing playbooks)

Marketing playbooks extracted + consolidated from v3.1 sections 8, 9,
15, 19-21, 25-27. Posts Prontos Híbrido preserved integral.

Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>
EOF
)"
```

---

### Task 23: Agent sections §12-15 (motion, a11y, quality gate, integration)

**Files:**
- Modify: `subagents/design-agent.md` (append §12-15)

**Size after this task:** ~2.000 lines (cumulative).

- [ ] **Step 1: Write §12 Motion + Video Design — Essentials (~150 lines)**

- Motion tokens (100/150/250/400/700ms)
- Easing essentials (ease-out enter, ease-in exit)
- When to animate (feedback, continuity, personality)
- prefers-reduced-motion
- Video design essentials (Reels/TikTok/YouTube)
- Deep → companion 05

- [ ] **Step 2: Write §13 Acessibilidade — Essentials (~150 lines)**

- WCAG 2.2 AA como minimum, AAA target
- 5 quick wins (contraste, focus visible, semantic HTML, alt text, keyboard nav)
- Per-project a11y budget
- 9 novos criteria do 2.2 (resumo)
- Deep → companion 04

- [ ] **Step 3: Write §14 Quality Gate — Design Review Checklist (~100 lines)**

- 15-point checklist (de design-review.md.template)
- Severity matrix (Critical/High/Medium/Low)
- Quando fazer review
- Como documentar (template `assets/templates/design/design-review.md.template`)

- [ ] **Step 4: Write §15 Integration com Marketing OS (~100 lines)**

- Outros subagentes do Marketing OS relevantes: @copywriter-agent, @ads-agent, @social-agent, @video-agent, @email-agent, @seo-agent
- Padrões de colaboração (quem invoca quem)
- Artefatos compartilhados (briefing, paleta, tokens, brand book)
- Fluxo end-to-end de campanha integrada (exemplo: lançamento de produto com DS + brand + campaign)
- Não duplicar trabalho de outros agentes (design-agent NÃO escreve copy — delega)

- [ ] **Step 5: Validate cumulative size in target range**

```bash
cd "/Users/rilner/Marketing OS"
wc -l subagents/design-agent.md
```
Expected: 1800-2500.

- [ ] **Step 6: Commit**

```bash
cd "/Users/rilner/Marketing OS"
git add subagents/design-agent.md
git commit -m "$(cat <<'EOF'
feat(design-agent): v4.0 §12-15 (motion, a11y, quality gate,
integration) — agent draft complete

Full v4.0 draft assembled. Ready for cross-ref validation and sync.

Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>
EOF
)"
```

---

### Task 24: Agent cross-references and polish

**Files:**
- Modify: `subagents/design-agent.md` (fix cross-refs, polish)

- [ ] **Step 1: Verify all companion references use correct relative path**

Run:
```bash
cd "/Users/rilner/Marketing OS"
grep -nE "references/design/[0-9]+" subagents/design-agent.md
```

Expected: every reference uses the pattern `references/design/XX-name.md` (no broken paths).

- [ ] **Step 2: Verify all template references use correct path**

```bash
cd "/Users/rilner/Marketing OS"
grep -nE "assets/templates/design/" subagents/design-agent.md
```

Expected: every template reference is `assets/templates/design/NAME.template`.

- [ ] **Step 3: Verify all skill references exist**

```bash
cd "/Users/rilner/Marketing OS"
grep -oE "figma:[a-z-]+|vercel:[a-z-]+|frontend-design:[a-z-]+|document-skills:[a-z-]+" subagents/design-agent.md | sort -u
```

Cross-check against available skills (listed at session start). Every skill mentioned must exist.

- [ ] **Step 4: Check for forbidden words + accent consistency**

```bash
cd "/Users/rilner/Marketing OS"
grep -nE "\bbrutal\b|\bmais avançado do planeta\b|\bmelhor do planeta\b|\bbest on the planet\b|\brevolucionário\b" subagents/design-agent.md
```
Expected: no matches.

```bash
# Spot-check accents on common words
grep -cE "cao\b|coes\b" subagents/design-agent.md
```
Expected: 0 (should be `ção`/`ções`, not `cao`/`coes`).

- [ ] **Step 5: Fix any issues found in steps 1-4**

If broken refs exist, fix them. If forbidden words appear, rewrite. If accents missing, add them.

- [ ] **Step 6: Final TOC/index audit**

Ensure §1-15 in the Índice section match the actual headings in the file.

- [ ] **Step 7: Commit if changes made**

```bash
cd "/Users/rilner/Marketing OS"
git diff subagents/design-agent.md | head -100
# If changes exist:
git add subagents/design-agent.md
git commit -m "$(cat <<'EOF'
fix(design-agent): v4.0 cross-reference and accent polish

Resolve broken refs, remove forbidden words, ensure accent
consistency, reconcile TOC with headings.

Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>
EOF
)"
```

If no changes needed, skip commit.

---

## Phase 4 — Sync, Validation, Release (4 tasks)

### Task 25: Sync canonical to skill-package mirror

**Files:**
- Sync: canonical → `skill-package/marketing-os/subagents/`
- Sync: canonical → `skill-package/marketing-os/references/design/`
- Sync: canonical → `skill-package/marketing-os/assets/templates/design/`

- [ ] **Step 1: Verify symlink mirrors auto-propagated**

```bash
cd "/Users/rilner/Marketing OS"
# marketing-os/subagents is symlink → auto-follows
diff subagents/design-agent.md marketing-os/subagents/design-agent.md
# skills/marketing-os/subagents is symlink → auto-follows
diff subagents/design-agent.md skills/marketing-os/subagents/design-agent.md
```

Both diffs should output nothing (identical via symlink).

- [ ] **Step 2: Sync agent file to skill-package**

```bash
cd "/Users/rilner/Marketing OS"
cp subagents/design-agent.md skill-package/marketing-os/subagents/design-agent.md
diff subagents/design-agent.md skill-package/marketing-os/subagents/design-agent.md
```
Expected: no output (identical).

- [ ] **Step 3: Sync references/design/ to skill-package**

```bash
cd "/Users/rilner/Marketing OS"
mkdir -p skill-package/marketing-os/references/design
cp references/design/*.md skill-package/marketing-os/references/design/
ls skill-package/marketing-os/references/design/
```
Expected: 10 files matching `references/design/`.

Verify:
```bash
cd "/Users/rilner/Marketing OS"
diff -r references/design skill-package/marketing-os/references/design
```
Expected: no output.

- [ ] **Step 4: Sync assets/templates/design/ to skill-package**

```bash
cd "/Users/rilner/Marketing OS"
mkdir -p skill-package/marketing-os/assets/templates/design
cp assets/templates/design/*.template skill-package/marketing-os/assets/templates/design/
ls skill-package/marketing-os/assets/templates/design/
```
Expected: 8 files matching `assets/templates/design/`.

Verify:
```bash
cd "/Users/rilner/Marketing OS"
diff -r assets/templates/design skill-package/marketing-os/assets/templates/design
```
Expected: no output.

- [ ] **Step 5: Commit sync**

```bash
cd "/Users/rilner/Marketing OS"
git add skill-package/marketing-os/
git commit -m "$(cat <<'EOF'
chore(skill-package): sync design-agent v4.0 + companions + templates

Mirror canonical subagent, references/design/, and
assets/templates/design/ into skill-package for distribution.

Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>
EOF
)"
```

---

### Task 26: Structural + content validation (F.1 and F.2 gates)

**Files:**
- Validation only; no file writes except the validation script itself (if created).

- [ ] **Step 1: Run structural validation (F.1)**

Run these checks in sequence:

```bash
cd "/Users/rilner/Marketing OS"

# Gate 1.1: All 19 files exist
test -f subagents/design-agent.md && echo "OK: agent" || echo "FAIL: agent"
test -f subagents/design-agent-v3.1-archive.md && echo "OK: archive" || echo "FAIL: archive"
for i in 01-tokens-w3c-spec 02-atomic-design-playbook 03-ds-governance 04-accessibility-wcag22 05-motion-spec 06-brand-system-blueprint 07-figma-mcp-playbook 08-shadcn-integration 09-handoff-to-code 10-orchestration-routes; do
  test -f "references/design/$i.md" && echo "OK: $i" || echo "FAIL: $i"
done
for t in tokens.json theme.css component-spec.md ds-readme.md style-dictionary.config.js storybook-main.ts brand-guidelines.md design-review.md; do
  test -f "assets/templates/design/$t.template" && echo "OK: template $t" || echo "FAIL: template $t"
done

# Gate 1.2: Agent size in range
SIZE=$(wc -l < subagents/design-agent.md)
if [ "$SIZE" -ge 1800 ] && [ "$SIZE" -le 2500 ]; then
  echo "OK: agent size $SIZE in range"
else
  echo "FAIL: agent size $SIZE out of range (1800-2500)"
fi

# Gate 1.3: Agent title v4.0
head -1 subagents/design-agent.md | grep -q "v4.0" && echo "OK: v4.0 title" || echo "FAIL: v4.0 title"
```

Expected: all `OK:` lines, zero `FAIL:`.

- [ ] **Step 2: Run content quality check (F.2)**

```bash
cd "/Users/rilner/Marketing OS"

# Check 1: No TODO/TBD/placeholders in agent or companions (templates allowed to have {{PLACEHOLDER}})
for f in subagents/design-agent.md references/design/*.md; do
  if grep -qE "TODO|TBD|\\bXXX\\b|FIXME|\\{\\{[A-Z_]+\\}\\}" "$f"; then
    echo "FAIL: placeholders in $f"
    grep -nE "TODO|TBD|\\bXXX\\b|FIXME|\\{\\{[A-Z_]+\\}\\}" "$f" | head -5
  fi
done

# Check 2: No forbidden words
for f in subagents/design-agent.md references/design/*.md; do
  if grep -qiE "\\bbrutal\\b|\\bmais avançado do planeta\\b|\\bmelhor do planeta\\b|\\brevolucionário\\b" "$f"; then
    echo "FAIL: forbidden word in $f"
    grep -niE "\\bbrutal\\b|\\bmais avançado do planeta\\b|\\bmelhor do planeta\\b|\\brevolucionário\\b" "$f" | head -3
  fi
done

# Check 3: Internal reference integrity (agent → companions)
grep -oE "references/design/[0-9]+-[a-z0-9-]+\\.md" subagents/design-agent.md | sort -u | while read ref; do
  test -f "$ref" && echo "OK: $ref exists" || echo "FAIL: $ref MISSING"
done

# Check 4: Internal reference integrity (agent → templates)
grep -oE "assets/templates/design/[a-z0-9-]+\\.[a-z]+\\.template" subagents/design-agent.md | sort -u | while read ref; do
  test -f "$ref" && echo "OK: $ref exists" || echo "FAIL: $ref MISSING"
done
```

Expected: zero FAIL lines. If any appear, fix the underlying issue (typo, rename, missing file) and re-run.

- [ ] **Step 3: If validation creates a script, commit it**

If a reusable validation script was extracted to `scripts/validate_design_agent.sh`:

```bash
cd "/Users/rilner/Marketing OS"
git add scripts/validate_design_agent.sh
git commit -m "$(cat <<'EOF'
chore(design): add validation script for design agent v4.0

Checks: file existence, size range, placeholder/forbidden-word scan,
internal reference integrity.

Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>
EOF
)"
```

If no script was created (validation run inline), skip commit.

---

### Task 27: Integration smoke tests (F.3)

**Files:**
- No file writes; log-only for this task.

Run 5 end-to-end scenarios to validate the agent behavior. Each scenario is a simulated user request; walk through the agent's expected reasoning and check if the agent file + companions support it correctly.

- [ ] **Step 1: Scenario 1 — "Crie um DS pro meu SaaS B2B"**

Expected agent flow (verify each piece exists in the agent file):
1. Agent reads §2 (mental model) → identifies "DS" domain → §9 + companions 01, 02, 03, 07, 08, 09
2. Agent checks §3 orchestration → asks 5 qs (audience, stack, brand exists?, theming?, deadline?)
3. Agent builds tokens.json from template (Builder Mode §4)
4. Agent delegates Figma library to `figma:figma-generate-library` (route in §3)
5. Agent delegates code to `vercel:shadcn` or `frontend-design` (route in §3)

Manually walk: open `subagents/design-agent.md`, confirm sections §2, §3, §4, §9 contain this flow. If any step is missing, go back and fix the agent.

Log result: PASS / FAIL with reason.

- [ ] **Step 2: Scenario 2 — "Brand book pra minha marca pessoal"**

Expected:
1. §2 → Brand domain → §10 + companion 06
2. §4 Builder Mode → fills `brand-guidelines.md.template`
3. Output: brand book completo

Verify agent file mentions template + companion 06. Log PASS/FAIL.

- [ ] **Step 3: Scenario 3 — "Post Instagram carrossel sobre IA"**

Expected:
1. §2 → Marketing content → §11
2. §11 Carrosséis playbook → composition + storytelling
3. §8 AI images → prompt for thumbnail + slide covers
4. Output: spec visual + AI prompt + (delegate copy para @copywriter-agent via §15)

Verify §8, §11, §15 support this. Log PASS/FAIL.

- [ ] **Step 4: Scenario 4 — "Crie componente Button no Figma"**

Expected:
1. §2 → Product UI (Figma) → §3 orchestration
2. §3 route → `figma:figma-generate-library`
3. Agent invokes the skill (conceptually — here we just verify the route exists)

Verify §3 contains the Figma button route. Log PASS/FAIL.

- [ ] **Step 5: Scenario 5 — "Audit a11y deste componente"**

Expected:
1. §2 → A11y audit → §13 + companion 04
2. §4 Builder Mode → fills `design-review.md.template`
3. Output: WCAG 2.2 report (PASS/CONCERNS/FAIL verdict)

Verify §4, §13, companion 04 exist and template is referenced. Log PASS/FAIL.

- [ ] **Step 6: Tally and commit log**

If all 5 PASS:
```bash
cd "/Users/rilner/Marketing OS"
cat > docs/superpowers/plans/2026-04-22-design-agent-v4-validation-log.md <<'EOF'
# Design Agent v4.0 — Validation Log

## Smoke Test Results (2026-04-22)

| # | Scenario | Result |
|---|----------|--------|
| 1 | Crie um DS pro meu SaaS B2B | PASS |
| 2 | Brand book pra minha marca pessoal | PASS |
| 3 | Post Instagram carrossel sobre IA | PASS |
| 4 | Crie componente Button no Figma | PASS |
| 5 | Audit a11y deste componente | PASS |

**Total:** 5/5 PASS. Agent validated.
EOF
git add docs/superpowers/plans/2026-04-22-design-agent-v4-validation-log.md
git commit -m "$(cat <<'EOF'
test(design-agent): v4.0 smoke tests — 5/5 PASS

Validated scenarios: DS build, brand book, Instagram carousel, Figma
component, a11y audit.

Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>
EOF
)"
```

If any FAIL: go back to the agent/companion source of the failure, fix it, re-sync (Task 25), re-run validation (Task 26), re-run smoke tests (Task 27).

---

### Task 28: Final release tag + summary commit

**Files:**
- Tag only; optional summary to docs/.

- [ ] **Step 1: Verify clean working tree**

```bash
cd "/Users/rilner/Marketing OS"
git status
```
Expected: "nothing to commit, working tree clean" (everything committed).

- [ ] **Step 2: Tag the release**

```bash
cd "/Users/rilner/Marketing OS"
git tag -a design-agent-v4.0 -m "Design Agent v4.0 — Full-Stack Design Intelligence

Marketing + Produto + Design System + Brand.
Hybrid builder+orchestrator model.
1 agent + 10 companions + 8 templates = 19 files.

Spec: docs/superpowers/specs/2026-04-22-design-agent-v4-design.md
Plan: docs/superpowers/plans/2026-04-22-design-agent-v4-implementation.md
"
git tag | grep design-agent-v4.0
```
Expected: `design-agent-v4.0`.

- [ ] **Step 3: Update MEMORY.md with v4.0 architecture notes**

This is auto-memory. Append to `/Users/rilner/.claude/projects/-Users-rilner-Marketing-OS/memory/MEMORY.md`:

```markdown
## Design Agent v4.0 Architecture (2026-04-22)
- Canonical: `subagents/design-agent.md` (~2k lines, strategic brain)
- Archive: `subagents/design-agent-v3.1-archive.md` (fallback)
- Companions: `references/design/01-tokens-w3c-spec.md` through `10-orchestration-routes.md` (10 files)
- Templates: `assets/templates/design/*.template` (8 files)
- Total new files: 19
- Model: Hybrid builder (tokens/specs/brand books/prompts) + orchestrator (delegates to figma:*, vercel:shadcn, frontend-design)
- Skill-package copies required (references/design and assets/templates/design — real dirs, not symlinks)
```

Done by writing memory (via auto-memory system), not directly edited by plan executor.

- [ ] **Step 4: Final sign-off message**

Print summary:
```
Design Agent v4.0 — DELIVERED

Files created/modified:
  - 1 agent (subagents/design-agent.md)
  - 1 archive (subagents/design-agent-v3.1-archive.md)
  - 10 companions (references/design/)
  - 8 templates (assets/templates/design/)
  - 1 validation log (docs/superpowers/plans/)
  - skill-package mirrors synced

Tag: design-agent-v4.0
Spec: docs/superpowers/specs/2026-04-22-design-agent-v4-design.md
```

No commit needed for this step (summary only).

---

## Self-review of this plan

**Spec coverage:**
- §1 Purpose → covered across all 28 tasks
- §2 Context → Preflight section
- §3 Architecture → Tasks 1, 20-25
- §4 Agent structure → Tasks 20-24
- §5 Companions → Tasks 10-19
- §6 Templates → Tasks 2-9
- §7 Extraction plan → Tasks 21-22 (v3.1 archive reads)
- §8 Definition of Done → Tasks 26-28
- §9 Rollback plan → implicit via archive (Task 1)
- §10 Out of scope → respected (no Python scripts, no Sketch, no MCP server)

**Placeholder scan:** None in the plan itself. Templates intentionally contain `{{PLACEHOLDER}}` (they are skeletons; Task 26 excludes them from the placeholder check correctly — only `.md` files in `subagents/` and `references/design/` are scanned, not `.template` files).

**Type consistency:**
- File paths consistent throughout (`references/design/XX-name.md`, `assets/templates/design/NAME.template`).
- Skill names consistent (`figma:figma-generate-library`, `vercel:shadcn`, etc.) — match system-reported available skills.
- Agent sections numbered consistently (§1-15 in both spec and plan).
- Sizing targets consistent: agent 1800-2500, total file count 19.

No issues to fix.

---

## Execution Handoff

Plan complete and saved to `docs/superpowers/plans/2026-04-22-design-agent-v4-implementation.md`. Two execution options:

1. **Subagent-Driven (recommended)** — dispatch a fresh subagent per task, review between tasks, fast iteration.

2. **Inline Execution** — execute tasks in this session using executing-plans, batch execution with checkpoints.

Which approach?
