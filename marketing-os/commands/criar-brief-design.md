---
description: Create a design brief with specs, color palettes, typography, and component requirements for Figma or any design tool.
argument-hint: "<project type, e.g., 'Instagram carousel template' or 'landing page design for SaaS'>"
---

# Create Design Brief

> See [CONNECTORS.md](../CONNECTORS.md) for Figma MCP integration and design asset connections.

Create a comprehensive design brief with visual direction, specifications, color palettes, typography, and component requirements that can be used directly in Figma or any design tool.

## Trigger

This command is invoked when the user says `/criar-brief-design` followed by a project type, or when they ask to create a design brief, visual direction, or design specifications.

## Inputs

Gather the following information. If any required field is missing, ask the user before proceeding:

1. **Project Type** (required) — Social media template, landing page, carousel, ad creative, brand identity, presentation, email template
2. **Brand Context** (required) — Brand name, industry, existing colors/fonts, mood
3. **Purpose** (required) — What the design needs to achieve
4. **Audience** (optional) — Who will see this design
5. **Platforms** (optional) — Where the design will be used (Instagram, web, print, etc.)
6. **Style Preference** (optional) — Minimalist, bold, corporate, playful, premium, tech, organic
7. **References** (optional) — Design inspiration, competitor examples, mood references

## Design Specifications by Platform

### Instagram

| Format | Dimensions | Safe Zone | Key Rules |
|--------|-----------|-----------|-----------|
| Feed Post | 1080x1080 | Full | Text > 20% contrasta com fundo |
| Carousel | 1080x1080 per slide | Full | Consistência entre slides |
| Stories | 1080x1920 | Centro 1080x1420 | Evitar extremidades top/bottom |
| Reels Cover | 1080x1920 | Centro 1080x1350 | Thumbnail legível |

### LinkedIn

| Format | Dimensions | Key Rules |
|--------|-----------|-----------|
| Post | 1200x627 | Profissional, clean |
| Article Cover | 1200x644 | Título legível no overlay |
| Banner | 1584x396 | Branding sutil |

### YouTube

| Format | Dimensions | Key Rules |
|--------|-----------|-----------|
| Thumbnail | 1280x720 | Face + texto grande + cores fortes |
| Banner | 2560x1440 | Safe area: 1546x423 centro |

### Web/Landing Page

| Element | Specs | Key Rules |
|---------|-------|-----------|
| Hero | Full width, 600-800px height | CTA acima do fold |
| Sections | Max 1200px content width | Espaçamento generoso |
| Mobile | 375px min width | Touch targets 44x44px |

## Content Generation

### Color Palette Framework

Generate a complete palette:

```
PRIMARY:    #[hex] — Cor principal da marca (botões, CTAs, destaques)
SECONDARY:  #[hex] — Cor complementar (backgrounds, seções alternadas)
ACCENT:     #[hex] — Cor de destaque (badges, alertas, links)
NEUTRAL:    #[hex] — Texto e elementos neutros
BACKGROUND: #[hex] — Fundo principal
SURFACE:    #[hex] — Cards, modais, elementos elevados
```

**Paleta por emoção/nicho:**

| Emoção/Nicho | Cores Sugeridas | Exemplo |
|-------------|----------------|---------|
| Confiança/Tech | Azul, cinza, branco | #2563EB, #64748B |
| Energia/Fitness | Laranja, vermelho, preto | #F97316, #DC2626 |
| Premium/Luxo | Preto, dourado, marfim | #1A1A1A, #D4AF37 |
| Saúde/Bem-estar | Verde, bege, terra | #16A34A, #D4C5A9 |
| Educação | Roxo, azul, branco | #7C3AED, #3B82F6 |
| Criativo/Design | Rosa, gradientes | #EC4899, #8B5CF6 |

### Typography Framework

```
HEADING FONT:  [Font name] — [Weight: Bold/Black]
  - H1: [size]px / [line-height]
  - H2: [size]px / [line-height]
  - H3: [size]px / [line-height]

BODY FONT:     [Font name] — [Weight: Regular/Medium]
  - Body: [size]px / [line-height]
  - Small: [size]px / [line-height]
  - Caption: [size]px / [line-height]

ACCENT FONT:   [Font name] — [Weight: Light/Italic] (optional)
  - Quotes, highlights, special elements
```

**Combinações seguras:**

| Heading | Body | Style |
|---------|------|-------|
| Inter | Inter | Clean, moderno |
| Montserrat | Open Sans | Profissional |
| Playfair Display | Lato | Elegante |
| Poppins | Roboto | Amigável |
| DM Sans | DM Sans | Minimalista |

### Layout Principles

```
GRID:          [12 columns / 8 columns / Free]
SPACING:       Base unit: [8px] — Multiples: 8, 16, 24, 32, 48, 64
BORDER RADIUS: [0px sharp / 4px subtle / 8px rounded / 16px soft / Full pill]
SHADOWS:       [None flat / Subtle / Medium / Strong]
```

## Output Structure

Deliver the design brief in this format:

```
## DESIGN BRIEF

🎨 PROJECT: [Project type]
🏷️ BRAND: [Brand name]
📱 PLATFORMS: [Target platforms]
🎯 PURPOSE: [Design goal]

---

### VISUAL DIRECTION

**Style:** [Minimalist / Bold / Corporate / Playful / Premium]
**Mood:** [3-5 adjectives describing the visual feel]
**References:** [Inspiration notes or links]

---

### COLOR PALETTE

| Role | Color | Hex | Usage |
|------|-------|-----|-------|
| Primary | [Swatch] | #[hex] | [Usage] |
| Secondary | [Swatch] | #[hex] | [Usage] |
| Accent | [Swatch] | #[hex] | [Usage] |
| Neutral | [Swatch] | #[hex] | [Usage] |
| Background | [Swatch] | #[hex] | [Usage] |
| Surface | [Swatch] | #[hex] | [Usage] |

---

### TYPOGRAPHY

**Heading:** [Font] — [Weight]
**Body:** [Font] — [Weight]
**Sizes:** [Scale defined]

---

### LAYOUT & SPACING

**Grid:** [Grid system]
**Spacing unit:** [Base unit]
**Border radius:** [Radius]
**Shadows:** [Shadow style]

---

### COMPONENT SPECS

[Detailed specs for each component/section needed]

**Component 1: [Name]**
- Dimensions: [WxH]
- Layout: [Description]
- Elements: [What goes inside]
- States: [Default, hover, active, disabled]

---

### DIMENSIONS TABLE

| Asset | Width | Height | Format | DPI |
|-------|-------|--------|--------|-----|
| [Asset 1] | [W] | [H] | [PNG/JPG/SVG] | [72/300] |
| [Asset 2] | [W] | [H] | [PNG/JPG/SVG] | [72/300] |

---

### AI IMAGE PROMPTS (if applicable)

**Prompt 1 — [Usage]:**
"[Detailed prompt for Midjourney/DALL-E/Flux]"

**Prompt 2 — [Usage]:**
"[Detailed prompt]"

---

### DESIGN CHECKLIST

- [ ] Cores aplicadas conforme palette
- [ ] Tipografia consistente
- [ ] Espaçamento seguindo grid
- [ ] Mobile responsive verificado
- [ ] Contrastes acessíveis (WCAG AA)
- [ ] Assets exportados nos formatos corretos
- [ ] Marca/logo posicionados corretamente
```

## Final Ask

After delivering the design brief, ask:

"Would you like me to:
1. Generate specific AI image prompts for the visuals?
2. Create the copy that goes with this design?
3. Adapt this brief for additional platforms?
4. Create a detailed component library specification?
5. Connect this brief to your Figma project (via MCP)?"
