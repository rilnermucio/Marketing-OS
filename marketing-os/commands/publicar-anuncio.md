---
description: Create and publish ad campaigns directly to Meta Ads platform with copy, targeting, and budget configuration.
argument-hint: "<campaign type and goal, e.g., 'lead generation campaign for course launch' or 'conversion campaign for product'>"
---

# Publish Ad Campaign

> Requires: Meta Ads MCP integration active (Especializei). See [CONNECTORS.md](../CONNECTORS.md) for setup.

Create and publish ad campaigns directly to Meta Ads (Facebook/Instagram) using the Meta Ads MCP integration. Works in coordination with `/criar-anuncio` (which generates copy) to then publish directly.

## Trigger

This command is invoked when the user says `/publicar-anuncio` followed by a campaign goal, or when they ask to publish, launch, or create a live ad campaign on Meta/Facebook/Instagram.

## Inputs

Gather the following information. If any required field is missing, ask the user before proceeding:

1. **Campaign Objective** (required) — Awareness, Traffic, Engagement, Leads, Conversions, Sales
2. **Ad Copy** (required) — Generated from `/criar-anuncio` or provided directly
3. **Target Audience** (required) — Demographics, interests, behaviors, custom audiences
4. **Budget** (required) — Daily or lifetime budget in BRL
5. **Duration** (required) — Start and end dates
6. **Placement** (optional) — Instagram Feed, Instagram Stories, Facebook Feed, Audience Network, All (default: All)
7. **Creative Assets** (optional) — Image/video URLs or descriptions for AI generation
8. **Landing Page URL** (optional) — Destination URL for clicks

## Campaign Structure

### Campaign Level (Objetivo)

| Objective | When to Use | Optimization |
|-----------|------------|-------------|
| Awareness | Brand visibility, reach | Impressions |
| Traffic | Drive to website/LP | Link clicks |
| Engagement | Likes, comments, shares | Post engagement |
| Leads | Lead form fills | Cost per lead |
| Conversions | Sales, signups | Cost per conversion |
| Sales | E-commerce purchases | ROAS |

### Ad Set Level (Segmentação)

**Targeting configuration:**
- Location (país, estado, cidade, raio)
- Age range
- Gender
- Interests (detailed targeting)
- Behaviors
- Custom audiences (if available)
- Lookalike audiences (if available)

**Budget and schedule:**
- Daily vs. lifetime budget
- Start/end dates
- Ad scheduling (specific hours)
- Bid strategy

### Ad Level (Criativo)

**Required elements:**
- Primary text (copy principal)
- Headline
- Description
- CTA button (Learn More, Sign Up, Shop Now, etc.)
- Creative (image or video)
- Destination URL

## Workflow

### Step 1: Generate Ad Copy
If not already created, use `/criar-anuncio` first to generate:
- Primary text variations (3+)
- Headline variations (3+)
- Description variations
- CTA options

### Step 2: Configure Campaign
Using Meta Ads MCP tools:

```
1. get_ad_accounts      → Select the ad account
2. create_campaign      → Set objective and name
3. create_adset         → Define targeting, budget, schedule
4. create_ad_creative   → Upload creative and copy
5. create_ad            → Link creative to ad set
```

### Step 3: Review and Launch
- Verify all settings
- Confirm budget
- Launch or schedule

## MCP Tools Used

| Tool | Purpose |
|------|---------|
| `get_ad_accounts` | List available ad accounts |
| `get_account_pages` | Get Facebook pages for ads |
| `create_campaign` | Create campaign with objective |
| `create_adset` | Set targeting, budget, schedule |
| `create_ad_creative` | Create ad with copy and visuals |
| `create_ad` | Finalize and launch ad |
| `get_insights` | Track performance after launch |
| `estimate_audience_size` | Estimate reach before launch |

## Output Structure

```
## AD CAMPAIGN PUBLISHED

🎯 OBJECTIVE: [Campaign objective]
💰 BUDGET: R$ [budget]/day
📅 DURATION: [Start] → [End]
📍 PLACEMENTS: [Placements]

---

### CAMPAIGN DETAILS

**Campaign ID:** [ID]
**Campaign Name:** [Name]
**Status:** [Active / Scheduled / In Review]

---

### AD SET

**Targeting:**
- Location: [Location]
- Age: [Range]
- Interests: [Interests]
- Estimated reach: [X] people

**Budget:** R$ [amount]/day
**Schedule:** [Start] to [End]

---

### AD CREATIVE

**Primary text:** "[Copy]"
**Headline:** "[Headline]"
**Description:** "[Description]"
**CTA:** [Button text]
**Destination:** [URL]

---

### PERFORMANCE TRACKING

After 24-48 hours, check metrics with:
- Impressions and reach
- CTR (click-through rate)
- CPC (cost per click)
- Conversions (if tracked)
- ROAS (if e-commerce)

---

### A/B TEST PLAN

| Variant | Element Changed | Hypothesis |
|---------|----------------|------------|
| A (Control) | Original copy | Baseline |
| B | Different headline | Test hook |
| C | Different CTA | Test action |
```

## Final Ask

After publishing the campaign, ask:

"Would you like me to:
1. Create additional ad variations for A/B testing?
2. Set up a retargeting audience for non-converters?
3. Generate a reporting dashboard setup?
4. Create the landing page for this campaign?
5. Monitor performance and suggest optimizations?"
