---
description: Generate multiple pieces of content at once for a specific theme or campaign, across multiple formats and platforms.
argument-hint: "<quantity> <type> <theme>, e.g., '10 posts about AI tools' or '5 emails for product launch'>"
---

# Batch Content Production

> See [CONNECTORS.md](../CONNECTORS.md) for connected services that can schedule and publish content.

Generate multiple pieces of content at once with variation in hooks, angles, and formats — all maintaining a unified theme and messaging.

## Trigger

This command is invoked when the user says `/batch` followed by a quantity, content type, and theme, or when they ask to create multiple pieces of content, produce content in bulk, or batch-create content.

## Inputs

Gather the following information. If any required field is missing, ask the user before proceeding:

1. **Quantity** (required) — How many pieces to generate (3, 5, 10, 15, 20, 30)
2. **Content Type** (required) — Posts, carousels, reels scripts, emails, articles, ads, mixed
3. **Theme/Topic** (required) — Central theme for all pieces
4. **Platforms** (optional) — Instagram, LinkedIn, TikTok, Twitter/X, email, blog (default: Instagram)
5. **Audience** (optional) — Target audience
6. **Tone** (optional) — Professional, casual, educational, entertaining
7. **Clone Voice** (optional) — Expert clone to apply (Hormozi, Ogilvy, etc.)
8. **Campaign Context** (optional) — Part of a larger campaign? Funnel stage?

## Batch Type Specifications

### Posts Batch (Social Media)

**Per piece:** Hook + body copy + CTA + hashtags
**Variation engine:** Each post uses a different hook type and angle

| Post # | Hook Type | Angle | Framework |
|--------|-----------|-------|-----------|
| 1 | Curiosity | Problem-aware | PAS |
| 2 | Promise | Solution-aware | AIDA |
| 3 | Question | Unaware | Education |
| 4 | Story | Most-aware | Testimonial |
| 5 | Controversy | Problem-aware | Myth-busting |
| 6 | List | Solution-aware | Tips |
| 7 | Statistic | Unaware | Data-driven |
| 8 | Challenge | Problem-aware | Transformation |
| 9 | Behind-scenes | Most-aware | Authenticity |
| 10 | Prediction | Solution-aware | Authority |

### Carousel Batch

**Per piece:** Cover slide + 7-9 content slides + CTA slide
**Variation:** Different structures (how-to, myths, checklist, before/after, tips)

### Reels/TikTok Script Batch

**Per piece:** Hook (3s) + content (15-55s) + CTA
**Variation:** Different hooks, formats (talking head, text-on-screen, tutorial, story)

### Email Batch

**Per piece:** Subject line + preview text + body + CTA
**Variation:** Different subject line formulas, email structures, CTA placements

### Article/Blog Batch

**Per piece:** Title + meta description + outline + key sections
**Variation:** Different SEO angles, content formats (listicle, how-to, guide, case study)

### Ad Copy Batch

**Per piece:** Headline + primary text + description + CTA
**Variation:** Different hooks, benefit angles, audience segments

### Mixed Batch

**Combination of multiple types for a unified campaign:**

| Quantity | Type | Platform | Purpose |
|----------|------|----------|---------|
| 5 | Posts | Instagram | Awareness |
| 3 | Carousels | Instagram | Education |
| 3 | Reels scripts | Instagram/TikTok | Engagement |
| 5 | Emails | Email | Nurture |
| 2 | Articles | Blog | SEO |
| 2 | Ad copy | Meta Ads | Traffic |

## Variation Engine

### Hook Rotation

Each piece must use a DIFFERENT hook type. Available hooks:

1. **Curiosity:** "Isso mudou tudo sobre como eu [tema]..."
2. **Controversy:** "Opinião impopular: [afirmação ousada]"
3. **Promise:** "Aqui está exatamente como [resultado]..."
4. **Question:** "Por que ninguém fala sobre [tema]?"
5. **Story:** "[Tempo] atrás, eu estava [ponto de dor]..."
6. **List:** "[Número] coisas que eu gostaria de saber sobre [tema]"
7. **Statistic:** "[Dado impactante] — e aqui está o porquê..."
8. **Challenge:** "Eu tentei [ação] por [tempo] e isso aconteceu..."
9. **Behind-scenes:** "O que eu não mostro sobre [tema]..."
10. **Prediction:** "Em [ano/tempo], [previsão ousada]..."

### Angle Rotation

Each piece approaches the theme from a different angle:

| Angle | Focus | Best For |
|-------|-------|----------|
| Educational | Como fazer, tutorial, guia | Autoridade |
| Inspiracional | Resultados, transformação | Engajamento |
| Contrário | Desmistificação, mitos | Viralidade |
| Pessoal | História própria, vulnerabilidade | Conexão |
| Dados | Estatísticas, pesquisa | Credibilidade |
| Prático | Dicas rápidas, checklist | Salvamentos |
| Tendência | Novidade, trend, atualidade | Alcance |
| Comparativo | Antes/depois, X vs Y | Clareza |

### Framework Rotation

Alternate copy frameworks to avoid repetition:

- PAS (Problema → Agitar → Solução)
- AIDA (Atenção → Interesse → Desejo → Ação)
- BAB (Antes → Depois → Ponte)
- Education (Contexto → Pontos → Aplicação)
- Story (Situação → Conflito → Resolução)

## Output Structure

Deliver the batch in this format:

```
## BATCH CONTENT PRODUCTION

🎯 THEME: [Central theme]
📊 QUANTITY: [X] pieces
📱 PLATFORMS: [Platforms]
🎨 TYPE: [Content type(s)]
🗣️ CLONE: [Clone voice, if applicable]

---

### SUMMARY TABLE

| # | Type | Hook | Angle | Platform | Status |
|---|------|------|-------|----------|--------|
| 1 | [Type] | [Hook type] | [Angle] | [Platform] | ✓ |
| 2 | [Type] | [Hook type] | [Angle] | [Platform] | ✓ |
| ... | ... | ... | ... | ... | ✓ |

---

### PIECE #1

📱 Platform: [Platform]
🎯 Angle: [Angle]
📝 Framework: [Framework used]

**HOOK:**
"[Hook text]"

**CONTENT:**
[Full content/copy]

**CTA:**
[Call to action]

**HASHTAGS:**
[Hashtags if applicable]

---

### PIECE #2
[Same structure, different hook/angle/framework]

---

[Continue for all pieces...]

---

### CALENDAR PLACEMENT SUGGESTIONS

| Week | Mon | Tue | Wed | Thu | Fri | Sat | Sun |
|------|-----|-----|-----|-----|-----|-----|-----|
| 1 | #1 | #2 | — | #3 | #4 | — | #5 |
| 2 | #6 | #7 | — | #8 | #9 | — | #10 |

**Best posting times:**
- Instagram: [Times]
- LinkedIn: [Times]
- TikTok: [Times]

---

### BATCH STATISTICS

| Metric | Value |
|--------|-------|
| Total pieces | [X] |
| Unique hooks used | [X] |
| Unique angles used | [X] |
| Frameworks applied | [X] |
| Estimated content days | [X] days |
```

## Final Ask

After delivering the batch, ask:

"Would you like me to:
1. Generate more pieces with new angles and hooks?
2. Create visual direction for each piece?
3. Adapt the batch for additional platforms?
4. Create A/B variations of the top 3 pieces?
5. Schedule these into a complete editorial calendar?"
