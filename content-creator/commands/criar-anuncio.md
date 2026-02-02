---
description: Create high-converting ad copy for Meta Ads, Google Ads, TikTok Ads, LinkedIn Ads, and other paid platforms with multiple variations for testing.
argument-hint: "<platform and product, e.g., 'Meta Ads for SaaS product' or 'Google Search for e-commerce'>"
---

# Create Ad Copy

> See [CONNECTORS.md](../CONNECTORS.md) for connected services that can provide product data and ad platform integrations.

Create complete ad copy optimized for conversions, ROAS, and platform-specific best practices.

## Trigger

This command is invoked when the user says `/criar-anuncio` followed by a platform and product/offer, or when they ask to create ads, ad copy, or campaign content.

## Inputs

Gather the following information. If any required field is missing, ask the user before proceeding:

1. **Platform** (required) — Meta Ads, Google Ads, TikTok Ads, LinkedIn Ads, or Pinterest Ads
2. **Product/Offer** (required) — What is being advertised
3. **Objective** (optional) — Awareness, traffic, leads, conversions, or sales
4. **Target Audience** (optional) — Who the ad is targeting
5. **Key Benefit** (optional) — Primary value proposition
6. **Tone** (optional) — Professional, casual, urgent, playful, or authoritative
7. **Budget Range** (optional) — For optimization recommendations

## Platform Specifications

### Meta Ads (Facebook/Instagram)

| Placement | Primary Text | Headline | Description | Image/Video |
|-----------|--------------|----------|-------------|-------------|
| Feed | 125 chars visible (2,200 max) | 40 chars | 30 chars | 1:1 or 4:5 |
| Stories | 125 chars | 40 chars | — | 9:16 |
| Reels | 72 chars visible | 40 chars | — | 9:16 |
| Right Column | 125 chars | 40 chars | 20 chars | 1.91:1 |
| Marketplace | 125 chars | 40 chars | 30 chars | 1:1 |

**Best Practices:**
- Lead with benefit, not feature
- Use emojis sparingly (1-2 max)
- Hook in first line (before "See more")
- Test video vs. static
- Use social proof when possible

### Google Ads

**Search Ads:**

| Element | Limit | Quantity |
|---------|-------|----------|
| Headlines | 30 chars each | Up to 15 |
| Descriptions | 90 chars each | Up to 4 |
| Display URL paths | 15 chars each | 2 |

**Responsive Search Ad Structure:**
```
Headlines (mix of types):
- Keyword-focused (include search term)
- Benefit-focused (value proposition)
- CTA-focused (action to take)
- Social proof (numbers, awards)
- USP-focused (unique differentiator)

Descriptions:
- Expand on benefits
- Include CTA
- Address objections
- Add urgency when relevant
```

**Display Ads:**

| Element | Limit |
|---------|-------|
| Short headline | 25 chars |
| Long headline | 90 chars |
| Description | 90 chars |
| Business name | 25 chars |

### TikTok Ads

| Element | Limit | Notes |
|---------|-------|-------|
| Ad text | 100 chars recommended | 150 max |
| Video | 9:16 | 5-60 sec (15-30 optimal) |
| CTA button | Pre-set options | "Shop Now", "Learn More", etc. |

**Best Practices:**
- First 3 seconds critical
- Native look (not polished ads)
- Trending sounds when possible
- Text overlays on video
- Creator/UGC style outperforms branded

### LinkedIn Ads

| Ad Type | Intro Text | Headline | Description |
|---------|------------|----------|-------------|
| Single Image | 150 chars visible (600 max) | 70 chars | 100 chars |
| Video | 150 chars visible (600 max) | 70 chars | — |
| Carousel | 150 chars visible | 45 chars per card | — |
| Message Ad | 500 chars | — | — |

**Best Practices:**
- Professional tone (but not boring)
- Lead with business outcome
- Use specific data and numbers
- Mention job titles/industries
- Test different value propositions

## Ad Copy Framework

### The PADS Framework

```
P — PROBLEM
Start with the pain point or challenge.
Make the audience feel understood.

A — AGITATE
Expand on the consequences.
What happens if they don't solve it?

D — DESIRE
Paint the picture of life after.
The transformation, the outcome.

S — SOLUTION
Present your product/service.
Clear CTA to take action.
```

### Angle Development

| Angle Type | Focus | Example Hook |
|------------|-------|--------------|
| **Problem-aware** | Pain point | "Tired of [problem]?" |
| **Solution-aware** | Your solution | "Discover how [solution] works" |
| **Result-focused** | Outcome | "Get [specific result] in [time]" |
| **Social proof** | Others' success | "Join 10,000+ [audience] who..." |
| **Comparison** | vs. alternatives | "Finally, a [product] that actually..." |
| **Curiosity** | Unknown info | "The #1 mistake [audience] make..." |
| **Urgency** | Time-sensitive | "Limited time: [offer] ends soon" |
| **Authority** | Credibility | "Featured in Forbes, used by Nike..." |

## Output Structure

Deliver the ad copy in this format:

```
## AD COPY

📢 PLATFORM: [Meta / Google / TikTok / LinkedIn]
🎯 OBJECTIVE: [Awareness / Traffic / Conversions / Leads]
👥 TARGET AUDIENCE: [Description]
📍 PLACEMENT: [Feed / Stories / Search / etc.]

---

### VERSION 1: [Angle Name — e.g., "Problem-Aware"]

**Primary Text:**
[Full ad copy within character limits]

**Headline:**
[Headline within character limit]

**Description:**
[Description within character limit]

**CTA Button:**
[Shop Now / Learn More / Sign Up / etc.]

---

### VERSION 2: [Different Angle — e.g., "Social Proof"]

**Primary Text:**
[Full ad copy with different hook/angle]

**Headline:**
[Alternative headline]

**Description:**
[Alternative description]

---

### VERSION 3: [Another Angle — e.g., "Result-Focused"]

**Primary Text:**
[Continue pattern...]

**Headline:**
[Headline]

**Description:**
[Description]

---

### VERSION 4: Short-form (Stories/Reels)

**Primary Text:**
[Condensed version for placements with less space]

**Headline:**
[Shorter headline variation]

---

### VERSION 5: Urgency/Scarcity

**Primary Text:**
[Version with time-limited offer or scarcity]

**Headline:**
[Urgency-focused headline]

---

## CREATIVE DIRECTION

**Visual recommendation:**
[Description of image/video to pair with copy]

**Hook for video ads (first 3 seconds):**
[Opening script that stops the scroll]

**UGC-style script:**
[If applicable, a native-feeling video script]

---

## A/B TEST SUGGESTIONS

| Test | Variant A | Variant B | Hypothesis |
|------|-----------|-----------|------------|
| Hook | [Current] | [Test] | [Expected result] |
| CTA | [Current] | [Test] | [Expected result] |
| Angle | [Current] | [Test] | [Expected result] |
| Format | [Image] | [Video] | [Expected result] |

---

## CAMPAIGN STRUCTURE SUGGESTION

**Ad Set Organization:**
- Ad Set 1: [Audience type + targeting]
- Ad Set 2: [Audience type + targeting]
- Ad Set 3: [Audience type + targeting]

**Budget Allocation:**
[Recommendation based on objective]

---

## NOTES

- **Primary value proposition:** [Key message]
- **Objection addressed:** [Common concern handled]
- **Next iteration idea:** [Future test]
```

## Final Ask

After delivering the ad copy, ask:

"Would you like me to:
1. Create more variations with different angles?
2. Adapt this copy for another platform?
3. Write a full video script for the ad?
4. Generate A/B test variations for specific elements?"
