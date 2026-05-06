---
description: Create a complete sales funnel strategy with TOFU/MOFU/BOFU stages, content plan, email sequences, and conversion optimization.
argument-hint: "<funnel type and goal, e.g., 'lead generation funnel for SaaS' or 'course launch funnel'>"
---

# Create Sales Funnel

> See [CONNECTORS.md](../CONNECTORS.md) for connected services that can provide analytics data and automation tools.

Create a complete sales funnel with stage-by-stage content, email sequences, ad strategy, and conversion optimization.

## Trigger

This command is invoked when the user says `/criar-funil` followed by a funnel type and goal, or when they ask to create a sales funnel, conversion funnel, or customer journey.

## Inputs

Gather the following information. If any required field is missing, ask the user before proceeding:

1. **Funnel Type** (required) — Lead Generation, Product Launch, Webinar, Tripwire, Evergreen, High-Ticket
2. **Product/Service** (required) — What is being sold at the end of the funnel
3. **Price Point** (required) — Product price or price range
4. **Audience** (required) — Target audience (demographics, awareness level, sophistication level)
5. **Lead Magnet** (optional) — Free offer to capture leads (if not defined, suggest one)
6. **Timeline** (optional) — Implementation timeline in weeks
7. **Budget** (optional) — Monthly budget for paid traffic
8. **Existing Assets** (optional) — Current content, email list size, social following

## Funnel Type Specifications

### Lead Generation Funnel

```
TRAFFIC → LEAD MAGNET → EMAIL SEQUENCE → OFFER
```

**Stages:**
- **TOFU (Awareness):** Social posts, blog SEO, paid ads → land on lead capture page
- **MOFU (Consideration):** Email nurture sequence (7-10 emails), educational content
- **BOFU (Decision):** Sales emails, case studies, offer presentation, urgency

**Timeline:** 4-6 weeks to build, evergreen operation

### Product Launch Funnel (Jeff Walker PLF)

```
PRE-LAUNCH → LAUNCH → CART OPEN → CART CLOSE → POST-LAUNCH
```

**Stages:**
- **Pre-Launch (2-4 weeks):** Build anticipation, free content series (PLC 1-3)
- **Launch (3-7 days):** Cart open, daily emails, social proof surge
- **Post-Launch (1-2 weeks):** Buyer onboarding, non-buyer nurture, downsell

**Timeline:** 6-8 weeks total cycle

### Webinar Funnel

```
ADS/CONTENT → REGISTRATION → ATTENDANCE → OFFER → FOLLOW-UP
```

**Stages:**
- **Registration:** Drive signups through ads and organic content
- **Pre-webinar:** Confirmation + reminder sequence (3-4 emails)
- **Live event:** Value delivery + pitch (60-90 min)
- **Post-webinar:** Replay + urgency sequence (5-7 emails)

**Timeline:** 2-3 weeks per cycle, repeatable

### Tripwire Funnel

```
AD → LOW-TICKET OFFER ($7-47) → UPSELL → CORE OFFER
```

**Stages:**
- **Entry:** Irresistible low-ticket offer (self-liquidating)
- **Order Bump:** Complementary add-on (+30-50% of tripwire)
- **Upsell 1:** Next logical product (3-5x tripwire price)
- **Upsell 2:** Premium offer or bundle
- **Follow-up:** Email sequence for non-converters

**Timeline:** 2-3 weeks to build

### Evergreen Funnel

```
CONTENT/ADS → OPT-IN → AUTOMATED SEQUENCE → PERPETUAL SALES
```

**Stages:**
- **Entry:** Automated webinar or video series (always available)
- **Nurture:** Pre-built email sequence simulating live launch
- **Cart:** Automated urgency (deadline timer per subscriber)
- **Follow-up:** Non-buyer sequence, re-engagement after 30-60 days

**Timeline:** 4-6 weeks to build, runs indefinitely

### High-Ticket Funnel

```
CONTENT → APPLICATION → CALL BOOKING → SALES CALL → ONBOARDING
```

**Stages:**
- **TOFU:** High-value content establishing authority
- **Application:** Qualification form (filters serious prospects)
- **Call:** Strategy/discovery call (45-60 min)
- **Proposal:** Custom solution presentation
- **Close:** Follow-up sequence for pending decisions

**Timeline:** 2-4 weeks to set up

## Content Generation Per Stage

### TOFU — Awareness Content

| Format | Quantity | Purpose |
|--------|----------|---------|
| Blog posts | 3-5 | SEO traffic + authority |
| Social posts | 10-15 | Organic reach + engagement |
| Short videos | 3-5 | Awareness + virality |
| Paid ads | 3-5 creatives | Targeted traffic |

### MOFU — Nurture Content

| Format | Quantity | Purpose |
|--------|----------|---------|
| Lead magnet | 1 | Email capture |
| Email sequence | 7-12 emails | Trust building |
| Case studies | 2-3 | Social proof |
| Educational content | 3-5 pieces | Value delivery |

### BOFU — Conversion Content

| Format | Quantity | Purpose |
|--------|----------|---------|
| Sales page | 1 | Primary conversion |
| Sales emails | 5-7 | Direct selling |
| Testimonial content | 3-5 | Objection handling |
| Urgency/scarcity | 2-3 | Final push |

## Email Sequence Framework

### Nurture Sequence (Post Opt-in)

| Day | Email | Purpose |
|-----|-------|---------|
| D+0 | Boas-vindas + entrega do lead magnet | Valor imediato |
| D+1 | Story pessoal + conexão | Rapport |
| D+3 | Conteúdo educativo #1 | Autoridade |
| D+5 | Estudo de caso | Prova social |
| D+7 | Conteúdo educativo #2 | Expertise |
| D+9 | Mitos e verdades | Reframing |
| D+11 | Transição para oferta | Bridge |
| D+13 | Apresentação da oferta | Venda suave |
| D+15 | Objeções e FAQ | Eliminação de barreiras |
| D+17 | Urgência + última chamada | Fechamento |

### Sales Sequence (Cart Open)

| Day | Email | Purpose |
|-----|-------|---------|
| D+0 | Carrinho aberto — apresentação completa | Oferta |
| D+1 | Benefícios detalhados + stack de valor | Valor |
| D+2 | Depoimentos e resultados | Prova |
| D+3 | FAQ — objeções respondidas | Objeções |
| D+4 | Bônus exclusivo (tempo limitado) | Incentivo |
| D+5 | Último dia — manhã | Urgência |
| D+5 | Último dia — noite | Fechamento |

## Metrics Framework

### KPIs por Estágio

| Estágio | Métrica | Meta |
|---------|---------|------|
| TOFU | CPM / CPC / CTR | CTR > 2% |
| TOFU | Custo por Lead (CPL) | < 20% do ticket |
| MOFU | Taxa de abertura de email | > 25% |
| MOFU | Taxa de clique em email | > 3% |
| BOFU | Taxa de conversão da página | > 2-5% |
| BOFU | Custo por aquisição (CPA) | < 30% do ticket |
| Global | ROAS | > 3:1 |
| Global | LTV/CAC ratio | > 3:1 |

## Output Structure

Deliver the funnel in this format:

```
## SALES FUNNEL

🎯 TYPE: [Funnel type]
💰 PRODUCT: [Product/service]
💵 PRICE: R$ [price]
👤 AUDIENCE: [Target audience]
📅 TIMELINE: [Implementation timeline]

---

### FUNNEL MAP

[ASCII diagram of the complete funnel flow with stages]

TRAFFIC SOURCES
    ↓
[Stage 1] → [Conversion point]
    ↓
[Stage 2] → [Conversion point]
    ↓
[Stage 3] → [SALE]
    ↓
[POST-SALE] → [Upsell/Retention]

---

### STAGE 1: TOFU — AWARENESS

🎯 **Objective:** [Stage objective]
📊 **KPI:** [Key metric and target]

**Content plan:**
[Detailed content list with formats, topics, and platforms]

**Ad strategy:**
[Ad types, targeting, budget allocation]

---

### STAGE 2: MOFU — NURTURE

🎯 **Objective:** [Stage objective]
📊 **KPI:** [Key metric and target]

**Lead magnet:**
[Lead magnet concept, format, and value proposition]

**Email sequence:**
[Complete email sequence with day, subject, purpose]

---

### STAGE 3: BOFU — CONVERSION

🎯 **Objective:** [Stage objective]
📊 **KPI:** [Key metric and target]

**Sales page structure:**
[Key sections and copy direction]

**Sales email sequence:**
[Complete sales email sequence]

**Urgency/scarcity elements:**
[Specific urgency tactics]

---

### POST-SALE

**Buyer experience:**
[Onboarding sequence, upsells, retention]

**Non-buyer follow-up:**
[Re-engagement strategy, downsell, long-term nurture]

---

### IMPLEMENTATION CHECKLIST

**Week 1-2: Foundation**
- [ ] Define personas and awareness levels
- [ ] Create lead magnet
- [ ] Build landing pages
- [ ] Set up email automation

**Week 3-4: Content**
- [ ] Create TOFU content
- [ ] Write email sequences
- [ ] Prepare ad creatives
- [ ] Set up tracking/analytics

**Week 5-6: Launch & Optimize**
- [ ] Launch paid traffic
- [ ] Monitor metrics daily
- [ ] A/B test key elements
- [ ] Optimize conversion points

---

### BUDGET ALLOCATION

| Channel | % of Budget | Purpose |
|---------|-------------|---------|
| [Channel 1] | [X]% | [Purpose] |
| [Channel 2] | [X]% | [Purpose] |
| [Channel 3] | [X]% | [Purpose] |

---

### TOOLS RECOMMENDED

| Category | Tool | Purpose |
|----------|------|---------|
| Email | [Tool] | Automation |
| Landing Page | [Tool] | Page building |
| Analytics | [Tool] | Tracking |
| Ads | [Tool] | Traffic |
```

## Final Ask

After delivering the funnel, ask:

"Would you like me to:
1. Write the complete email sequences with full copy?
2. Create the landing page copy for the key conversion points?
3. Generate ad creatives copy for the traffic stage?
4. Create a detailed day-by-day implementation calendar?
5. Design a lead magnet concept and outline?"
