---
description: Create a complete expert clone with AI-powered research and content generation for all 4 clone files (profile, voice, frameworks, examples).
argument-hint: "<expert-name> [specialty]"
---

# Create Expert Clone (AI-Powered)

> Reference: See existing clones in `squads/marketing-os/data/clones/` for structure examples (e.g., `hormozi/`).

Create a complete, production-ready expert clone with rich content generated through web research and AI analysis. This command produces all 4 clone files matching the depth and quality of existing rich clones (~700 lines total).

## Trigger

This command is invoked when the user says `/criar-clone` followed by an expert name and optional specialty, or when they ask to create a new expert clone with AI-generated content.

## Inputs

Gather the following information. If any required field is missing, ask the user before proceeding:

1. **Expert Name** (required) — Full name of the expert (e.g., "Gary Vaynerchuk", "Seth Godin")
2. **Slug** (required) — Short identifier for the clone directory (e.g., "gary-vee", "seth-godin"). If not provided, derive from the expert name.
3. **Specialty** (optional) — Primary area of expertise. If not provided, research and determine automatically.
4. **Niches** (optional) — Comma-separated niches (e.g., "marketing-digital, empreendedorismo"). If not provided, determine from research.
5. **Content Types** (optional) — Best content types for this expert (e.g., "copy_vendas, roteiro_video"). If not provided, determine from research.
6. **Tone** (optional) — Voice tone description. If not provided, determine from research.

## Pre-Flight Check

Before starting, verify:

1. The clone directory does NOT already exist at `squads/marketing-os/data/clones/{slug}/`
2. The `clone-manifest.yaml` exists at `squads/marketing-os/data/clones/clone-manifest.yaml`
3. If the clone already exists, ask the user if they want to overwrite or abort

## Phase 1: Research

Use **WebSearch** to gather comprehensive information about the expert. Perform multiple searches to cover:

### Search Queries (adapt to the specific expert)

1. `"{expert name}" marketing philosophy frameworks methodology`
2. `"{expert name}" writing style voice communication patterns`
3. `"{expert name}" books career achievements biography`
4. `"{expert name}" content examples posts emails copy`
5. `"{expert name}" business strategy frameworks`
6. `"{expert name}" quotes famous phrases`

### Information to Collect

| Category | Details to Gather |
|----------|-------------------|
| **Identidade** | Nome completo, empresa(s), papel atual, livros, reconhecimento público |
| **Filosofia** | Filosofia central, princípios fundamentais (3-5), crenças sobre o mercado |
| **Trajetória** | Marcos importantes da carreira, datas, conquistas mensuráveis |
| **Audiência** | Público típico, faixa etária, nível de experiência, setores |
| **Voz** | Padrões de linguagem, vocabulário típico, o que evita, tom por contexto |
| **Frameworks** | Metodologias próprias (4-6), modelos de trabalho, fórmulas |
| **Exemplos** | Estilo de copy, estruturas de post, padrões de email, anúncios |

**IMPORTANT:** Only use verified, factual information. Do NOT invent frameworks, quotes, or achievements. If information is uncertain, note it and ask the user to confirm.

## Phase 2: Generate profile.md

Write `squads/marketing-os/data/clones/{slug}/profile.md` following this EXACT structure:

```markdown
# {Expert Name} - Perfil do Clone

## Identidade

- **Nome completo:** {full name}
- **Empresa:** {company/companies}
- **Papel:** {current role}
- **Reconhecimento:** {key achievement with numbers if possible}
- **Livros:** {published books, if any}

---

## Filosofia Central

{1-2 paragraphs describing the expert's core philosophy and approach. Be specific, reference their actual beliefs and frameworks.}

### Princípios Fundamentais

1. **{Principle Name}** - {Description with specific examples or numbers}

2. **{Principle Name}** - {Description with specific examples or numbers}

3. **{Principle Name}** - {Description with specific examples or numbers}

4. **{Principle Name}** - {Description with specific examples or numbers}

5. **{Principle Name}** - {Description with specific examples or numbers}

---

## Trajetória

{1-2 paragraphs with the expert's career narrative, including specific details and turning points.}

### Marcos importantes

- **{Year range}:** {Achievement with specific details}
- **{Year range}:** {Achievement with specific details}
- **{Year range}:** {Achievement with specific details}
- **{Year range}:** {Achievement with specific details}
- **{Year range}:** {Achievement with specific details}
- **{Current}:** {Current status/role}

---

## Audiência Típica

- {Audience segment 1}
- {Audience segment 2}
- {Audience segment 3}
- {Audience segment 4}
- {Audience segment 5}

---

## Estilo de Comunicação

| Aspecto | Descrição |
|---------|-----------|
| Tom | {tone description} |
| Linguagem | {language patterns} |
| Estrutura | {typical content structure} |
| Humor | {humor style if any} |
| Energia | {energy level and type} |
| Credibilidade | {how they build credibility} |

---

## Diferenciação

O que separa {expert name} de outros experts:

1. **{Differentiator}** - {Description}
2. **{Differentiator}** - {Description}
3. **{Differentiator}** - {Description}
4. **{Differentiator}** - {Description}
5. **{Differentiator}** - {Description}

---

## Quando Usar Este Clone

| Situação | Adequação |
|----------|-----------|
| {Use case 1} | Excelente |
| {Use case 2} | Excelente |
| {Use case 3} | Muito bom |
| {Use case 4} | Muito bom |
| {Anti-use case 1} | Não recomendado |
| {Anti-use case 2} | Não recomendado |
| {Edge case} | Usar com cautela |

---

## Tópicos de Domínio

- {Domain topic 1}
- {Domain topic 2}
- {Domain topic 3}
- {Domain topic 4}
- {Domain topic 5}
- {Domain topic 6}
- {Domain topic 7}
- {Domain topic 8}
```

**Target:** ~100 lines. All content in Portuguese with full acentuação.

## Phase 3: Generate voice.md

Write `squads/marketing-os/data/clones/{slug}/voice.md` following this EXACT structure:

```markdown
# {Expert Name} - Guia de Voz e Tom

## Visão Geral

{1 paragraph describing the overall voice: key characteristics, how they communicate, what makes their voice unique.}

---

## Características Fundamentais da Voz

### 1. {Characteristic Name}

{Description of this voice trait.}

**Não faça:**
> "{Example of what NOT to do}"

**Faça:**
> "{Example of what TO do in this expert's voice}"

### 2. {Characteristic Name}

{Description of this voice trait.}

**Não faça:**
> "{Example of what NOT to do}"

**Faça:**
> "{Example of what TO do in this expert's voice}"

### 3. {Characteristic Name}

{Description of this voice trait.}

**Exemplos típicos:**
- "{Example phrase 1}"
- "{Example phrase 2}"
- "{Example phrase 3}"

### 4. {Characteristic Name}

{Description of this voice trait.}

**Padrão rítmico:**
> "{Example showing the rhythm and style}"

### 5. {Characteristic Name}

{Description of this voice trait.}

**Padrões de abertura:**
- "{Opening pattern 1}"
- "{Opening pattern 2}"
- "{Opening pattern 3}"
- "{Opening pattern 4}"
- "{Opening pattern 5}"

---

## Estrutura Narrativa

### Padrão Principal: {Pattern Name}

```
1. {STEP}: {Description}
   "{Example}"

2. {STEP}: {Description}
   "{Example}"

3. {STEP}: {Description}
   "{Example}"

4. {STEP}: {Description}
   "{Example}"
```

### Padrão Secundário: {Pattern Name}

```
1. {STEP}: "{Example}"
2. {STEP}: "{Example}"
3. {STEP}: "{Example}"
```

---

## Vocabulário Típico

### Palavras e Expressões Frequentes

| Categoria | Expressões |
|-----------|------------|
| **{Category 1}** | "{expressions}" |
| **{Category 2}** | "{expressions}" |
| **{Category 3}** | "{expressions}" |
| **{Category 4}** | "{expressions}" |
| **{Category 5}** | "{expressions}" |
| **{Category 6}** | "{expressions}" |

### Palavras que {Expert Name} NUNCA usa

| Evitar | Por quê |
|--------|---------|
| "{word/phrase}" | {reason} |
| "{word/phrase}" | {reason} |
| "{word/phrase}" | {reason} |
| "{word/phrase}" | {reason} |
| "{word/phrase}" | {reason} |
| "{word/phrase}" | {reason} |

---

## Tom por Tipo de Conteúdo

### Copy de Vendas
- {characteristic 1}
- {characteristic 2}
- {characteristic 3}
- {characteristic 4}
- {characteristic 5}

### Landing Page
- {characteristic 1}
- {characteristic 2}
- {characteristic 3}
- {characteristic 4}
- {characteristic 5}

### Anúncio (Ad)
- {characteristic 1}
- {characteristic 2}
- {characteristic 3}
- {characteristic 4}
- {characteristic 5}

### Roteiro de Vídeo
- {characteristic 1}
- {characteristic 2}
- {characteristic 3}
- {characteristic 4}

### Post para Redes Sociais
- {characteristic 1}
- {characteristic 2}
- {characteristic 3}
- {characteristic 4}

---

## Regras de Formatação

1. **{Rule 1}** - {Description}
2. **{Rule 2}** - {Description}
3. **{Rule 3}** - {Description}
4. **{Rule 4}** - {Description}
5. **{Rule 5}** - {Description}
6. **{Rule 6}** - {Description}

---

## Exemplos de Adaptação de Tom

### Tom Formal (evitar ao clonar {Expert Name})
> "{Example of formal tone to avoid}"

### Tom {Expert Name} (usar)
> "{Example of the correct tone}"

### Tom Motivacional Vazio (evitar)
> "{Example of empty motivational tone to avoid}"

### Tom {Expert Name} (usar)
> "{Example of the correct tone as contrast}"

---

## Checklist de Voz

Antes de finalizar qualquer conteúdo no estilo {Expert Name}, verifique:

- [ ] {Check 1 - key voice characteristic}
- [ ] {Check 2 - opening/hook quality}
- [ ] {Check 3 - evidence/support}
- [ ] {Check 4 - avoiding anti-patterns}
- [ ] {Check 5 - CTA clarity}
- [ ] {Check 6 - formatting rules}
- [ ] {Check 7 - reader next steps}
- [ ] {Check 8 - tone consistency}
```

**Target:** ~190 lines. All content in Portuguese with full acentuação. Each characteristic MUST have "Não faça / Faça" or concrete examples.

## Phase 4: Generate frameworks.md

Write `squads/marketing-os/data/clones/{slug}/frameworks.md` following this EXACT structure:

```markdown
# {Expert Name} - Frameworks

## 1. {Framework Name} ({Portuguese Translation if applicable})

{1-2 sentences describing the framework and its purpose.}

{Optional: ASCII formula or visual representation if the framework has one}

### Componentes

| Componente | Descrição | Como aplicar |
|------------|-----------|--------------|
| **{Component 1}** | {Description} | {Application in copy/content} |
| **{Component 2}** | {Description} | {Application in copy/content} |
| **{Component 3}** | {Description} | {Application in copy/content} |
| **{Component 4}** | {Description} | {Application in copy/content} |

### Aplicação na Copy

{Specific guidance on how to use this framework when creating content.}

1. **{Step 1}** - {Description with examples}
2. **{Step 2}** - {Description with examples}
3. **{Step 3}** - {Description with examples}
4. **{Step 4}** - {Description with examples}

---

## 2. {Framework Name}

{Similar structure - adapt sections based on the framework's nature.}
{Include: description, components/structure (table), step-by-step, examples.}

---

## 3. {Framework Name}

{Similar structure.}

---

## 4. {Framework Name}

{Similar structure.}

---

## 5. {Framework Name} (if applicable)

{Similar structure.}

---

## 6. {Framework Name} (if applicable)

{Similar structure.}

---

## Resumo para Aplicação na Copy

| Framework | Use quando... |
|-----------|---------------|
| {Framework 1} | {When to use} |
| {Framework 2} | {When to use} |
| {Framework 3} | {When to use} |
| {Framework 4} | {When to use} |
| {Framework 5} | {When to use} |
| {Framework 6} | {When to use} |
```

**Target:** ~200 lines. Include 4-6 frameworks depending on the expert. Each framework must have:
- Description
- Components (table format)
- Step-by-step application
- Copy/content examples
- The summary table at the end

**CRITICAL:** Only include REAL frameworks the expert actually uses/teaches. Do NOT invent frameworks.

## Phase 5: Generate examples.md

Write `squads/marketing-os/data/clones/{slug}/examples.md` following this EXACT structure:

```markdown
# {Expert Name} - Exemplos Anotados

## Exemplo 1: Copy de Vendas - {Specific scenario}

### Copy

---

{Full sales copy example written in the expert's voice and style. 15-25 lines.
Use the expert's frameworks, vocabulary, and patterns.
Include specific numbers, proof points, and CTAs consistent with their approach.}

---

### Análise

| Elemento | Técnica Aplicada |
|----------|-----------------|
| **Headline** | {What technique was used and why} |
| **{Element}** | {Technique applied} |
| **{Element}** | {Technique applied} |
| **{Element}** | {Technique applied} |
| **{Element}** | {Technique applied} |
| **{Element}** | {Technique applied} |
| **{Element}** | {Technique applied} |
| **CTA** | {Technique applied} |

---

## Exemplo 2: Anúncio para Redes Sociais

### Copy

---

{Full ad copy in the expert's voice. 10-20 lines.}

---

### Análise

| Elemento | Técnica Aplicada |
|----------|-----------------|
| **{Element}** | {Technique applied} |
| **{Element}** | {Technique applied} |
| **{Element}** | {Technique applied} |
| **{Element}** | {Technique applied} |
| **{Element}** | {Technique applied} |
| **{Element}** | {Technique applied} |
| **{Element}** | {Technique applied} |

---

## Exemplo 3: Email de Vendas

### Copy

---

{Full email copy in the expert's voice. Include subject line, greeting, body, CTA, signature, and P.S. 15-25 lines.}

---

### Análise

| Elemento | Técnica Aplicada |
|----------|-----------------|
| **Assunto** | {Technique applied} |
| **{Element}** | {Technique applied} |
| **{Element}** | {Technique applied} |
| **{Element}** | {Technique applied} |
| **{Element}** | {Technique applied} |
| **{Element}** | {Technique applied} |
| **{Element}** | {Technique applied} |
| **P.S.** | {Technique applied} |

---

## Exemplo 4: Post LinkedIn

### Copy

---

{Full LinkedIn post in the expert's voice. 15-25 lines.}

---

### Análise

| Elemento | Técnica Aplicada |
|----------|-----------------|
| **{Element}** | {Technique applied} |
| **{Element}** | {Technique applied} |
| **{Element}** | {Technique applied} |
| **{Element}** | {Technique applied} |
| **{Element}** | {Technique applied} |
| **{Element}** | {Technique applied} |
| **{Element}** | {Technique applied} |
```

**Target:** ~200 lines. Each example must:
- Be a COMPLETE piece of copy (not a snippet)
- Authentically reflect the expert's voice and frameworks
- Include an analysis table mapping each element to the technique used
- Cover 4 formats: copy de vendas, anúncio, email, post LinkedIn

**CRITICAL:** Examples must feel like the expert actually wrote them. Use their vocabulary, frameworks, patterns, and tone from the voice.md and frameworks.md you generated.

## Phase 6: Update clone-manifest.yaml

Append a new entry to `squads/marketing-os/data/clones/clone-manifest.yaml` in the `clones:` section (BEFORE `matching_rules:`).

Follow the exact format of existing entries:

```yaml
  {slug}:
    name: "{Full Name}"
    specialty: "{Specialty description}"
    best_for: ["{type1}", "{type2}", "{type3}", "{type4}"]
    niches: ["{niche1}", "{niche2}", "{niche3}"]
    tone: "{tone description in Portuguese}"
    path: "{slug}/"
```

## Phase 7: Validation

After generating all files, verify:

- [ ] `profile.md` exists with all 8 sections (Identidade, Filosofia, Trajetória, Audiência, Estilo, Diferenciação, Quando Usar, Tópicos)
- [ ] `voice.md` exists with all 8 sections (Visão Geral, Características, Estrutura Narrativa, Vocabulário, Tom por Tipo, Regras, Exemplos Adaptação, Checklist)
- [ ] `frameworks.md` exists with 4-6 frameworks + resumo table
- [ ] `examples.md` exists with 4 examples + análise tables
- [ ] `clone-manifest.yaml` updated with new entry
- [ ] All files are in Portuguese with correct acentuação
- [ ] No invented or unverified information (all based on research)
- [ ] Total line count across 4 files is ~700 lines

Report the validation results to the user.

## Final Output

After completion, display:

```
Clone criado com sucesso: {Expert Name}

Arquivos gerados:
  squads/marketing-os/data/clones/{slug}/
  ├── profile.md    ({line count} linhas)
  ├── voice.md      ({line count} linhas)
  ├── frameworks.md ({line count} linhas)
  └── examples.md   ({line count} linhas)

Total: {total lines} linhas

Manifesto atualizado: clone-manifest.yaml

Para usar: aios clone use {slug} --agent copy-agent
```

Then ask:

"Deseja que eu:
1. Revise e ajuste algum arquivo específico?
2. Adicione mais frameworks ou exemplos?
3. Crie um clone de outro expert?
4. Teste o clone com um conteúdo de exemplo?"
