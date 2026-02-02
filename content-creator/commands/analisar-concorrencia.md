---
description: Analyze competitor profiles, content strategies, and market positioning to extract actionable insights and identify opportunities.
argument-hint: "<competitors or niche, e.g., '@competitor1 @competitor2' or 'fitness coaching niche'>"
---

# Analyze Competition

> See [CONNECTORS.md](../CONNECTORS.md) for connected services that can provide social listening and competitive intelligence data.

Conduct comprehensive competitor analysis to identify patterns, gaps, and opportunities for differentiation.

## Trigger

This command is invoked when the user says `/analisar-concorrencia` followed by competitor names or niche, or when they ask to analyze competitors, do competitive research, or benchmark against others.

## Inputs

Gather the following information. If any required field is missing, ask the user before proceeding:

1. **Competitors** (required) — Specific accounts/brands to analyze (2-5 recommended) OR niche to research
2. **Platforms** (optional) — Which platforms to focus on (Instagram, LinkedIn, TikTok, YouTube)
3. **Analysis Depth** (optional) — Quick overview, standard, or comprehensive
4. **Focus Areas** (optional) — Content, engagement, positioning, audience, or all
5. **Your Brand Context** (optional) — Information about the user's brand for comparison

## Analysis Framework

### Competitor Profile Template

```
COMPETITOR: [Name/Handle]

OVERVIEW
├── Platform(s): [Where they're active]
├── Followers: [Count by platform]
├── Posting Frequency: [Posts per week]
├── Account Age: [When started]
└── Verified: [Yes/No]

POSITIONING
├── Unique Value Proposition: [What they promise]
├── Target Audience: [Who they serve]
├── Brand Voice: [How they communicate]
├── Visual Identity: [Look and feel]
└── Price Positioning: [Premium/Mid/Budget]

CONTENT STRATEGY
├── Content Pillars: [Main themes]
├── Formats Used: [Video, carousel, etc.]
├── Posting Schedule: [When they post]
├── Hashtag Strategy: [Types and quantity]
└── Call-to-Actions: [What they ask for]

ENGAGEMENT
├── Avg. Likes: [Per post]
├── Avg. Comments: [Per post]
├── Engagement Rate: [Percentage]
├── Response Rate: [How often they reply]
└── Community Size: [Active followers estimate]

TOP PERFORMING CONTENT
├── Post 1: [Description + metrics]
├── Post 2: [Description + metrics]
├── Post 3: [Description + metrics]
└── Common Patterns: [What works]

WEAKNESSES/GAPS
├── Content Gaps: [What they're missing]
├── Engagement Issues: [Problems observed]
├── Positioning Gaps: [Underserved angles]
└── Opportunities: [What you could do better]
```

## Metrics to Analyze

### Engagement Metrics

| Metric | Formula | Good Benchmark |
|--------|---------|----------------|
| Engagement Rate | (Likes + Comments) / Followers × 100 | >3% (IG), >2% (LI) |
| Comment Ratio | Comments / Likes × 100 | >2% |
| Save Rate | Saves / Reach × 100 | >2% (estimate) |
| Share Rate | Shares / Reach × 100 | >1% |
| Growth Rate | (New - Old) / Old × 100 | >2%/month |

### Content Performance Indicators

| Indicator | What It Shows | How to Identify |
|-----------|---------------|-----------------|
| Viral Posts | What breaks through | 3x+ avg engagement |
| Consistent Performers | Reliable content types | Above avg, low variance |
| Underperformers | What to avoid | Below avg, consistently |
| Engagement Spikes | Timing/topic wins | Sudden engagement jumps |
| Growth Correlations | What drives follows | Posts before follower spikes |

## Analysis Categories

### 1. Content Analysis

| Element | Questions to Answer |
|---------|---------------------|
| Themes | What topics do they cover? How often? |
| Formats | What content types perform best? |
| Frequency | How often do they post? When? |
| Quality | Production value? Professional or raw? |
| Copy Style | Long or short? Formal or casual? |
| Hooks | How do they start posts/videos? |
| CTAs | What actions do they request? |

### 2. Audience Analysis

| Element | Questions to Answer |
|---------|---------------------|
| Demographics | Who engages? (from comment analysis) |
| Pain Points | What problems are mentioned? |
| Questions | What do followers ask? |
| Sentiment | Positive, negative, or neutral? |
| Engagement Level | Passive viewers or active community? |
| Overlap | Do they share your target audience? |

### 3. Positioning Analysis

| Element | Questions to Answer |
|---------|---------------------|
| Value Prop | What unique value do they offer? |
| Differentiators | What makes them stand out? |
| Weaknesses | Where do they fall short? |
| Pricing | How do they position on price? |
| Credibility | What authority signals do they use? |
| Brand Voice | Professional, friendly, edgy, etc.? |

### 4. Strategy Patterns

| Pattern | What to Look For |
|---------|-----------------|
| Content Pillars | Recurring themes and categories |
| Launch Sequences | How they promote new offers |
| Engagement Tactics | How they encourage interaction |
| Community Building | How they create connection |
| Sales Approach | Hard sell vs. soft sell vs. value-first |

## SWOT Framework

```
STRENGTHS (Internal Positive)
├── What do they do well?
├── What are their advantages?
├── What unique resources do they have?
└── What do followers praise?

WEAKNESSES (Internal Negative)
├── Where do they underperform?
├── What complaints do followers have?
├── What content underperforms?
└── Where is there inconsistency?

OPPORTUNITIES (External Positive)
├── What gaps exist in the market?
├── What trends are they missing?
├── What audience needs are unmet?
└── Where can you differentiate?

THREATS (External Negative)
├── What are they doing better than you?
├── What trends might hurt them (and you)?
├── What market changes affect the niche?
└── Who else is competing for this audience?
```

## Output Structure

Deliver the analysis in this format:

```
## COMPETITIVE ANALYSIS

🎯 FOCUS: [Niche/Industry]
📊 COMPETITORS ANALYZED: [Number]
📱 PLATFORMS: [Instagram, LinkedIn, TikTok, etc.]
📅 ANALYSIS DATE: [Date]

---

### EXECUTIVE SUMMARY

**Key Findings:**
- [Most important insight 1]
- [Most important insight 2]
- [Most important insight 3]

**Top Opportunity:**
[The biggest gap or opportunity identified]

**Recommended Action:**
[Primary recommendation based on analysis]

---

### COMPETITOR 1: [Name/Handle]

**Overview:**
| Metric | Value |
|--------|-------|
| Followers | [X] |
| Posting Frequency | [X/week] |
| Engagement Rate | [X%] |
| Primary Content | [Type] |

**Positioning:**
[2-3 sentences describing their market position]

**Content Strategy:**
- Pillars: [List main themes]
- Top Formats: [What performs best]
- Posting Schedule: [When they post]

**What Works:**
- [Successful element 1]
- [Successful element 2]
- [Successful element 3]

**Gaps/Weaknesses:**
- [Weakness 1]
- [Weakness 2]
- [Weakness 3]

**Top Performing Posts:**
1. [Post description] — [X] engagement
2. [Post description] — [X] engagement
3. [Post description] — [X] engagement

---

### COMPETITOR 2: [Name/Handle]
[Same structure as Competitor 1]

---

### COMPETITOR 3: [Name/Handle]
[Same structure as Competitor 1]

---

### COMPARATIVE ANALYSIS

**Side-by-Side Comparison:**

| Metric | Comp 1 | Comp 2 | Comp 3 | Industry Avg |
|--------|--------|--------|--------|--------------|
| Followers | [X] | [X] | [X] | [X] |
| Engagement Rate | [X%] | [X%] | [X%] | [X%] |
| Post Frequency | [X/wk] | [X/wk] | [X/wk] | [X/wk] |
| Reels/Video | [X%] | [X%] | [X%] | [X%] |
| Carousel | [X%] | [X%] | [X%] | [X%] |

**Content Strategy Comparison:**

| Element | Comp 1 | Comp 2 | Comp 3 |
|---------|--------|--------|--------|
| Primary Pillar | [X] | [X] | [X] |
| Tone | [X] | [X] | [X] |
| CTA Style | [X] | [X] | [X] |
| Visual Style | [X] | [X] | [X] |

---

### MARKET GAPS & OPPORTUNITIES

**Content Gaps:**
| Gap | Competitors Covering | Opportunity Level |
|-----|---------------------|-------------------|
| [Gap 1] | None / Few | High |
| [Gap 2] | None / Few | Medium |
| [Gap 3] | Some | Medium |

**Positioning Opportunities:**
1. [Underserved angle or audience]
2. [Unique differentiator available]
3. [Format or platform opportunity]

**Audience Needs Not Being Met:**
- [Unmet need 1]
- [Unmet need 2]
- [Unmet need 3]

---

### CONTENT INSPIRATION

**Successful Patterns to Adapt:**
1. [Pattern from competitor] → [How to adapt]
2. [Pattern from competitor] → [How to adapt]
3. [Pattern from competitor] → [How to adapt]

**Hooks That Perform:**
- "[Hook example 1]"
- "[Hook example 2]"
- "[Hook example 3]"

**CTAs That Work:**
- "[CTA example 1]"
- "[CTA example 2]"
- "[CTA example 3]"

---

### STRATEGIC RECOMMENDATIONS

**Differentiation Strategy:**
[How to position differently from competitors]

**Content Priorities:**
1. [Priority 1 — What to create first]
2. [Priority 2 — What to create next]
3. [Priority 3 — What to test]

**Quick Wins:**
- [Easy implementation 1]
- [Easy implementation 2]
- [Easy implementation 3]

**Long-Term Plays:**
- [Strategic move 1]
- [Strategic move 2]

---

### ACTION ITEMS

| Priority | Action | Timeline | Expected Impact |
|----------|--------|----------|-----------------|
| High | [Action 1] | [Time] | [Impact] |
| High | [Action 2] | [Time] | [Impact] |
| Medium | [Action 3] | [Time] | [Impact] |
| Medium | [Action 4] | [Time] | [Impact] |
```

## Final Ask

After delivering the analysis, ask:

"Would you like me to:
1. Deep dive into a specific competitor's strategy?
2. Create a differentiation plan based on the gaps identified?
3. Generate content ideas to fill the market gaps?
4. Build a competitive content calendar?"
