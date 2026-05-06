---
description: Create a complete landing page with hero section, benefits, social proof, offer, and CTA optimized for conversion.
argument-hint: "<type and purpose, e.g., 'lead capture for webinar' or 'sales page for online course'>"
---

# Create Landing Page

> See [CONNECTORS.md](../CONNECTORS.md) for connected services that can provide brand guidelines, design assets, and analytics data.

Create a complete, conversion-optimized landing page with all essential sections, copy frameworks, and visual direction.

## Trigger

This command is invoked when the user says `/criar-landing-page` followed by a page type and purpose, or when they ask to create a landing page, sales page, or lead capture page.

## Inputs

Gather the following information. If any required field is missing, ask the user before proceeding:

1. **Page Type** (required) — Lead Capture, Sales Page, Webinar Registration, Waitlist/Coming Soon, Product Launch, Thank You Page
2. **Product/Service** (required) — What is being offered
3. **Audience** (required) — Who this page is for (demographics, psychographics, awareness level)
4. **Goal** (required) — Capture leads, sell product, register for event, build waitlist
5. **Price Point** (optional) — If sales page, the price or price range
6. **Tone** (optional) — Professional, casual, urgent, premium, friendly
7. **Key Differentiator** (optional) — What makes this offer unique
8. **Deadline/Urgency** (optional) — Launch date, limited spots, time-sensitive offer

## Brand Voice Integration

If brand guidelines are available through connected services or have been previously established:
- Apply the documented tone and voice
- Use approved vocabulary and phrases
- Follow visual identity guidelines for color suggestions
- Maintain consistency with existing marketing materials

If no brand guidelines exist, ask the user to describe their brand in 3-5 adjectives.

## Page Type Specifications

### Lead Capture Page

**Structure (1-2 scrolls):**
- Hero: Headline + lead magnet promise
- Benefits: 3-5 bullet points of what they will get
- Social proof: Quick stat or testimonial
- Form: Name + email (minimal friction)
- Lead magnet preview image

**Key rules:**
- One single CTA
- Minimal text — every word must earn its place
- Lead magnet value must be immediately clear
- No navigation links (zero distractions)

### Sales Page (Long Form)

**Structure (5-15 scrolls):**
- Hero: Headline + subheadline + CTA + social proof
- Problem/Pain: Identify and agitate the problem
- Solution: Present the product as the answer
- Benefits: Detailed with specific results
- How it works: 3-5 simple steps
- Social proof: Testimonials, case studies, logos
- Offer: Price anchoring + value stack + bonuses
- Guarantee: Risk reversal
- FAQ: Handle 5-7 top objections
- Final CTA: Urgency + last push

**Key rules:**
- Multiple CTAs throughout (minimum 3)
- Specific numbers and results over vague promises
- Address objections before they arise
- Value stack must make price feel like a bargain

### Webinar Registration Page

**Structure (1-2 scrolls):**
- Hero: Webinar title + key benefit + date/time
- What you will learn: 3-5 bullet points
- Speaker bio: Credibility and authority
- Registration form: Name + email
- Urgency: Limited spots, countdown timer

**Key rules:**
- Date and time prominently displayed
- Speaker authority established clearly
- Promise specific takeaways, not vague topics
- Countdown timer for urgency

### Waitlist/Coming Soon Page

**Structure (1 scroll):**
- Hero: Product teaser + launch date
- Value proposition: Why this matters
- Early access benefits: What waitlisters get
- Form: Email only (lowest friction)
- Social proof: Interest indicators

### Product Launch Page

**Structure (3-8 scrolls):**
- Hero: Product name + bold promise + launch date
- Teaser: What the product does (without revealing everything)
- Problem it solves: Pain points addressed
- Key features/benefits: Top 3-5 highlights
- Social proof: Beta results, endorsements, pre-orders count
- Offer: Early bird pricing, launch bonuses
- FAQ: Common questions
- CTA: Pre-order / Join waitlist

## Content Generation

### Headline Formulas

Generate at least 3 headline options using these frameworks:

**Result + Time:**
```
[Desired Result] em [Specific Time]
Example: "Domine Marketing Digital em 30 Dias"
```

**Without + Pain:**
```
[Result] Sem [Main Pain/Obstacle]
Example: "Venda Online Sem Aparecer"
```

**For Who:**
```
Para [Persona] Que Quer [Result]
Example: "Para Empreendedores Que Querem Escalar"
```

**Number + Specific:**
```
[Number] [Method/Steps] Para [Specific Result]
Example: "O Método de 5 Passos Para Criar Anúncios Que Vendem"
```

**Challenge Question:**
```
E Se Você Pudesse [Desired Result]?
Example: "E Se Você Pudesse Viver do Seu Hobby?"
```

### Subheadline Formulas

```
O [método/sistema] para [persona] que quer [resultado] sem [dor]
Descubra como [resultado] usando [método] mesmo que [objeção comum]
A forma mais [adjetivo] de [resultado] em [ano]
```

### CTA Copy Rules

| Type | Weak | Strong |
|------|------|--------|
| Generic | "Clique aqui" | "Quero Começar Agora" |
| E-commerce | "Comprar" | "Garantir o Meu" |
| Lead | "Enviar" | "Receber Meu Guia Grátis" |
| Trial | "Experimentar" | "Testar Grátis por 7 Dias" |
| Course | "Inscrever" | "Quero Acesso Imediato" |
| Webinar | "Registrar" | "Reservar Minha Vaga" |

### Power Words

| Urgência | Exclusividade | Confiança | Valor |
|----------|---------------|-----------|-------|
| Agora | Exclusivo | Garantido | Grátis |
| Hoje | Limitado | Comprovado | Bônus |
| Imediato | Único | Testado | Incluso |
| Última chance | Especial | Seguro | Extra |
| Restam X | VIP | Certificado | Presente |

### Copy Principles

1. **Benefícios > Features** — "Domine a habilidade que vai dobrar seu salário" > "Curso com 40 horas"
2. **Específico > Genérico** — "Gere R$5.000 extras por mês" > "Ganhe mais dinheiro"
3. **Você > Nós** — "Você tem suporte sempre que precisar" > "Nós oferecemos suporte 24h"
4. **Ativo > Passivo** — "Você vai alcançar resultados" > "Os resultados serão alcançados"

## Output Structure

Deliver the landing page in this format:

```
## LANDING PAGE

🎯 TYPE: [Page type]
👤 AUDIENCE: [Target audience]
🏷️ PRODUCT: [Product/service name]
📈 GOAL: [Conversion goal]

---

### HEADLINE OPTIONS

**Option A (Recommended):**
"[Headline text]"

**Subheadline:**
"[Subheadline text]"

**Option B (Benefit angle):**
"[Headline text]"

**Option C (Curiosity angle):**
"[Headline text]"

---

### HERO SECTION (Above the Fold)

[Complete hero section copy: headline, subheadline, CTA button text, social proof line, hero image/video direction]

---

### PROBLEM/PAIN SECTION

[Empathy headline]
[4-5 specific pain points the audience faces]
[Validation statement]

---

### SOLUTION SECTION

[Product presentation headline]
[1 paragraph product description]
[3 core benefits with specific results]

---

### BENEFITS SECTION (Expanded)

[Benefits headline]
[5-6 detailed benefits with icons/checkmarks]

[Before/After comparison if applicable:]
ANTES                    →  DEPOIS
• Pain point 1               • Desired state 1
• Pain point 2               • Desired state 2

---

### SOCIAL PROOF SECTION

[Social proof headline]

**Testimonial 1:**
"[Quote with specific result]"
— [Name], [Role/Company or Result]

**Testimonial 2:**
"[Quote with specific result]"
— [Name], [Role/Company or Result]

[Key numbers:]
• [X]+ satisfied clients
• [X]% satisfaction rate
• [X]+ results achieved

---

### HOW IT WORKS

[Headline: "Como Funciona em X Passos"]

1️⃣ [Step 1 - User action]
[Brief explanation]

2️⃣ [Step 2 - What happens]
[Brief explanation]

3️⃣ [Step 3 - Result obtained]
[Brief explanation]

---

### OFFER SECTION

[Offer headline]

[Value stack:]
✓ [Item 1] — valor R$XX
✓ [Item 2] — valor R$XX
✓ [Bonus 1] — valor R$XX
✓ [Bonus 2] — valor R$XX

Total value: R$ [sum]
You pay only: R$ [final price]
or [X]x of R$ [installment]

[CTA Button: "[Action-oriented text]"]

🛡️ [Guarantee: X-day money-back guarantee]

---

### FAQ SECTION

❓ [Objection question 1]
[Direct answer that eliminates the objection]

❓ [Objection question 2]
[Direct answer]

❓ [Objection question 3]
[Direct answer]

❓ [Objection question 4]
[Direct answer]

❓ [Objection question 5]
[Direct answer]

---

### FINAL CTA SECTION

[Urgency headline]
[Value summary in 1 line]

[CTA Button: "[Final action text]"]

⏰ [Urgency element: deadline, limited spots]
🔒 [Security badges: secure payment, guarantee]

---

### VISUAL DIRECTION

🎨 **Color palette:** [Primary, secondary, accent colors]
🔤 **Typography:** [Heading and body font suggestions]
📐 **Layout:** [Layout recommendations]
📷 **Images:** [Image style and suggestions]

---

### SEO METADATA

🏷️ **Title tag:** [60 characters max]
📝 **Meta description:** [155 characters max]
🔑 **Focus keyword:** [Primary keyword]

---

### CONVERSION CHECKLIST

- [ ] Headline clara com benefício
- [ ] Proposta de valor única evidente
- [ ] CTAs visíveis com copy de ação
- [ ] Prova social presente
- [ ] Garantia/redução de risco
- [ ] FAQ com objeções principais
- [ ] Mobile responsive considerado
- [ ] Formulários simples (mínimos campos)
```

## Final Ask

After delivering the landing page, ask:

"Would you like me to:
1. Create A/B variations with different headlines and angles?
2. Generate the email sequence for post-registration/purchase?
3. Create ad copy to drive traffic to this landing page?
4. Generate AI image prompts for the visual elements?
5. Adapt this into a different page type (e.g., lead capture → sales page)?"
