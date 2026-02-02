---
name: analytics-agent
description: Analyze content performance, track KPIs, create reports, and optimize based on data. Use when analyzing metrics, building dashboards, setting up A/B tests, interpreting analytics data, or creating performance reports.
---

# Analytics Agent Skill

Expert analytics skill focused on measuring content performance, interpreting data, and providing actionable optimization recommendations based on metrics across all platforms.

## When to Use This Skill

- Analyzing content performance across platforms
- Creating performance reports and dashboards
- Setting up and interpreting A/B tests
- Defining KPIs and success metrics
- Benchmarking against industry standards
- Making data-driven content decisions
- Optimizing based on analytics insights

## Metrics Framework by Platform

### Instagram Metrics

| Metric | Definition | Benchmark | Priority |
|--------|------------|-----------|----------|
| **Reach** | Unique accounts that saw content | Varies by size | High |
| **Impressions** | Total views (including repeats) | 1.5-2x reach | Medium |
| **Engagement Rate** | (Likes+Comments+Saves+Shares)/Reach | 3-6% | Critical |
| **Save Rate** | Saves/Reach | 2-5% | Critical |
| **Share Rate** | Shares/Reach | 0.5-2% | High |
| **Profile Visits** | Clicks to profile from content | 1-3% of reach | Medium |
| **Follower Growth** | New followers from content | Varies | High |

**Engagement Rate Formula:**
```
Engagement Rate = (Likes + Comments + Saves + Shares) / Reach × 100
```

### YouTube Metrics

| Metric | Definition | Benchmark | Priority |
|--------|------------|-----------|----------|
| **CTR (Click-Through Rate)** | Clicks/Impressions | 4-10% | Critical |
| **AVD (Average View Duration)** | Mean watch time | 50%+ of video | Critical |
| **Retention Rate** | % watched at each point | 50%+ average | Critical |
| **Subscriber Conversion** | Subs gained/Views | 1-4% | High |
| **RPM (Revenue per Mille)** | Revenue per 1000 views | $2-10 | Medium |
| **Watch Time** | Total minutes watched | Platform metric | High |

**Key YouTube Signals:**
```
High CTR + High AVD = Algorithm boost
High CTR + Low AVD = Clickbait penalty
Low CTR + High AVD = Thumbnail/title issue
Low CTR + Low AVD = Content issue
```

### LinkedIn Metrics

| Metric | Definition | Benchmark | Priority |
|--------|------------|-----------|----------|
| **Impressions** | Total views | Varies by network | Medium |
| **Engagement Rate** | Interactions/Impressions | 2-5% | High |
| **Dwell Time** | Time spent reading | N/A (internal) | Critical |
| **Click-Through Rate** | Clicks/Impressions | 1-3% | High |
| **Comment Quality** | Meaningful comments vs. emoji | Qualitative | High |
| **Profile Views** | Post-content profile visits | Track trend | Medium |

### TikTok Metrics

| Metric | Definition | Benchmark | Priority |
|--------|------------|-----------|----------|
| **Views** | Total video plays | Varies | Medium |
| **Completion Rate** | % who watched to end | 60%+ | Critical |
| **Rewatch Rate** | Loops / Total views | 10%+ | Critical |
| **Share Rate** | Shares/Views | 1-5% | High |
| **Comment Rate** | Comments/Views | 0.5-3% | High |
| **Follower Conversion** | New follows/Views | 0.5-2% | Medium |

### Email Metrics

| Metric | Definition | Benchmark | Priority |
|--------|------------|-----------|----------|
| **Open Rate** | Opens/Delivered | 20-25% | High |
| **Click Rate (CTR)** | Clicks/Delivered | 2-5% | Critical |
| **Click-to-Open (CTOR)** | Clicks/Opens | 10-15% | High |
| **Unsubscribe Rate** | Unsubs/Delivered | <0.5% | Monitor |
| **Bounce Rate** | Bounces/Sent | <2% | Monitor |
| **Conversion Rate** | Conversions/Clicks | 1-5% | Critical |

### Website/Blog Metrics

| Metric | Definition | Benchmark | Priority |
|--------|------------|-----------|----------|
| **Organic Traffic** | Visits from search | Track growth | High |
| **Bounce Rate** | Single-page visits | 40-60% | Medium |
| **Time on Page** | Average reading time | 2-4 min | High |
| **Pages per Session** | Content explored | 1.5-3 | Medium |
| **Conversion Rate** | Goal completions/Visits | 1-3% | Critical |
| **Scroll Depth** | How far users scroll | 50%+ | Medium |

## Performance Analysis Framework

### The COAL Framework

```
C — COLLECT
├── Gather data from all sources
├── Ensure tracking is accurate
└── Define time period

O — ORGANIZE
├── Segment by content type
├── Compare periods
└── Identify patterns

A — ANALYZE
├── What performed well?
├── What underperformed?
├── Why? (hypothesis)

L — LEVERAGE
├── Double down on winners
├── Fix or abandon losers
└── Test hypotheses
```

### Content Performance Matrix

```
                    HIGH ENGAGEMENT
                          │
         HIDDEN GEMS      │      TOP PERFORMERS
         (Promote more)   │      (Repeat formula)
                          │
LOW REACH ────────────────┼──────────────────── HIGH REACH
                          │
         LOW PRIORITY     │      HIGH REACH, LOW ENGAGE
         (Deprioritize)   │      (Fix content quality)
                          │
                    LOW ENGAGEMENT
```

### Diagnostic Questions

| Symptom | Possible Causes | Analysis Steps |
|---------|-----------------|----------------|
| Low reach | Algorithm, timing, hashtags | Check posting time, hashtag performance |
| Low engagement | Content quality, audience mismatch | Analyze content type, compare to winners |
| High reach, low saves | Not valuable enough | Add actionable takeaways |
| High reach, low comments | Not conversation-worthy | Add questions, controversial takes |
| Low CTR (YouTube) | Weak thumbnail/title | A/B test thumbnails |
| Low retention (video) | Weak hook, pacing issues | Check retention graph drop-offs |

## A/B Testing Framework

### What to Test

| Element | Platform | Test Type |
|---------|----------|-----------|
| Headlines | All | Copy variations |
| Thumbnails | YouTube | Visual variations |
| Posting time | All | Time slots |
| CTA | All | Action copy |
| Hook | Video | Opening variations |
| Format | Social | Carousel vs. single |
| Length | All | Short vs. long |

### A/B Test Structure

```
HYPOTHESIS:
"If we [change], then [metric] will [improve/decrease] because [reason]"

VARIANTS:
Control (A): Current version
Test (B): Changed version
[Test (C): Optional third variant]

SUCCESS METRIC:
Primary: [Main metric to measure]
Secondary: [Supporting metrics]

SAMPLE SIZE:
Minimum per variant: [Calculate based on baseline]
Duration: [Time needed for significance]

STATISTICAL SIGNIFICANCE:
Target confidence level: 95%
Minimum detectable effect: [% change you care about]
```

### Sample Size Calculator

```
For 95% confidence, 80% power:
- 5% baseline conversion, 20% lift → ~3,900 per variant
- 10% baseline conversion, 10% lift → ~14,300 per variant
- 2% baseline conversion, 50% lift → ~1,500 per variant

Rule of thumb: Run test until you have at least:
- 100 conversions per variant (ideal)
- 1,000 impressions per variant (minimum)
```

## Reporting Framework

### Weekly Report Structure

```
## WEEKLY PERFORMANCE REPORT
Period: [Date] - [Date]

### EXECUTIVE SUMMARY
- [Key win]
- [Key challenge]
- [Key opportunity]

### KEY METRICS

| Metric | This Week | Last Week | Change | Target |
|--------|-----------|-----------|--------|--------|
| [Metric 1] | [Value] | [Value] | [+/-]% | [Target] |
| [Metric 2] | [Value] | [Value] | [+/-]% | [Target] |

### TOP PERFORMING CONTENT

1. [Content 1]
   - Reach: [X] | Engagement: [X]%
   - Why it worked: [Analysis]

2. [Content 2]
   - Reach: [X] | Engagement: [X]%
   - Why it worked: [Analysis]

### UNDERPERFORMING CONTENT

1. [Content 1]
   - Expected: [X] | Actual: [X]
   - Hypothesis: [Why it didn't work]

### INSIGHTS & LEARNINGS
- [Insight 1]
- [Insight 2]

### NEXT WEEK ACTIONS
- [ ] [Action 1]
- [ ] [Action 2]
```

### Monthly Report Structure

```
## MONTHLY PERFORMANCE REPORT
Period: [Month Year]

### MONTH OVERVIEW
[2-3 sentence summary of the month]

### GOALS VS. ACTUALS

| Goal | Target | Actual | Status |
|------|--------|--------|--------|
| [Goal 1] | [Target] | [Actual] | ✅/⚠️/❌ |
| [Goal 2] | [Target] | [Actual] | ✅/⚠️/❌ |

### PLATFORM BREAKDOWN

**Instagram:**
- Followers: [X] ([+/-X] from last month)
- Avg. Engagement Rate: [X]%
- Top post: [Description]

**YouTube:**
- Subscribers: [X] ([+/-X])
- Avg. CTR: [X]%
- Watch time: [X] hours
- Top video: [Description]

[Repeat for each platform]

### CONTENT PERFORMANCE BY TYPE

| Content Type | Volume | Avg. Reach | Avg. Engagement |
|--------------|--------|------------|-----------------|
| Carousel | [X] | [X] | [X]% |
| Reels | [X] | [X] | [X]% |
| Static | [X] | [X] | [X]% |

### KEY LEARNINGS
1. [Learning with data support]
2. [Learning with data support]

### NEXT MONTH STRATEGY
- [Strategic focus 1]
- [Strategic focus 2]
- [Content experiments to run]
```

## Benchmarking

### Industry Benchmarks by Platform

**Instagram (by follower count):**
| Follower Range | Engagement Rate Benchmark |
|----------------|---------------------------|
| <1K (Nano) | 5-10% |
| 1K-10K (Micro) | 4-6% |
| 10K-100K (Mid) | 2-4% |
| 100K-1M (Macro) | 1.5-2.5% |
| 1M+ (Mega) | 1-2% |

**YouTube (by channel size):**
| Subscriber Range | CTR Benchmark | AVD Benchmark |
|------------------|---------------|---------------|
| <1K | 2-5% | 40-50% |
| 1K-10K | 4-8% | 45-55% |
| 10K-100K | 5-10% | 50-60% |
| 100K+ | 6-12% | 50-65% |

**Email (by industry):**
| Industry | Open Rate | Click Rate |
|----------|-----------|------------|
| Marketing/Advertising | 17% | 2% |
| E-commerce | 15% | 2.5% |
| Education | 25% | 3% |
| Health/Fitness | 21% | 2.5% |
| Technology | 20% | 2% |
| Finance | 20% | 2.5% |

## KPI Setting Framework

### SMART Goals for Content

```
S — SPECIFIC
"Increase Instagram engagement rate"
→ "Increase Instagram carousel engagement rate"

M — MEASURABLE
"Improve YouTube performance"
→ "Increase YouTube CTR from 4% to 6%"

A — ACHIEVABLE
"Get 1M followers"
→ "Grow from 10K to 15K followers (50% growth)"

R — RELEVANT
"Increase vanity metrics"
→ "Increase email signups from content"

T — TIME-BOUND
"Eventually improve conversion"
→ "Increase conversion rate by Q2 2026"
```

### Content KPI Tiers

| Tier | Metrics | Purpose |
|------|---------|---------|
| **North Star** | 1-2 key business metrics | Ultimate success measure |
| **Primary** | 3-5 platform metrics | Direct content performance |
| **Secondary** | 5-10 supporting metrics | Context and diagnosis |
| **Vanity** | Followers, likes (raw) | Awareness, not success |

## Output Format

### Standard Analytics Deliverables

For every analytics request, provide:

1. **Executive summary** — Key insights in 3 bullets
2. **Metrics table** — With benchmarks and trends
3. **Performance analysis** — What worked/didn't and why
4. **Recommendations** — Specific, actionable next steps
5. **Test ideas** — A/B tests to run

### Example Output Structure

```
## PERFORMANCE ANALYSIS

📊 PERIOD: [Date range]
📈 PLATFORM: [Platform name]
🎯 FOCUS: [What we're analyzing]

---

### EXECUTIVE SUMMARY

✅ **Win:** [Key positive finding]
⚠️ **Challenge:** [Key area for improvement]
💡 **Opportunity:** [Actionable insight]

---

### KEY METRICS

| Metric | Value | vs. Last Period | vs. Benchmark | Status |
|--------|-------|-----------------|---------------|--------|
| [Metric 1] | [Value] | [+/-X]% | [Above/Below] | [✅/⚠️/❌] |
| [Metric 2] | [Value] | [+/-X]% | [Above/Below] | [✅/⚠️/❌] |
| [Metric 3] | [Value] | [+/-X]% | [Above/Below] | [✅/⚠️/❌] |

---

### TOP PERFORMERS

**#1: [Content Title/Description]**
- Reach: [X] | Engagement: [X]%
- What made it work: [Analysis]
- Replication opportunity: [How to repeat]

**#2: [Content Title/Description]**
- Reach: [X] | Engagement: [X]%
- What made it work: [Analysis]

---

### UNDERPERFORMERS

**[Content Title/Description]**
- Expected: [X] | Actual: [X]
- Gap analysis: [Why it missed]
- Fix: [What to do differently]

---

### INSIGHTS

1. **[Pattern observed]**
   Data: [Supporting metrics]
   Implication: [What this means]

2. **[Pattern observed]**
   Data: [Supporting metrics]
   Implication: [What this means]

---

### RECOMMENDATIONS

| Priority | Action | Expected Impact | Effort |
|----------|--------|-----------------|--------|
| 🔴 High | [Action 1] | [Impact] | [Low/Med/High] |
| 🟡 Medium | [Action 2] | [Impact] | [Low/Med/High] |
| 🟢 Low | [Action 3] | [Impact] | [Low/Med/High] |

---

### A/B TESTS TO RUN

**Test 1: [Test name]**
- Hypothesis: If we [change], then [metric] will improve by [%]
- Variants: A) [Control] | B) [Test]
- Duration: [Time needed]
- Success metric: [Primary metric]
```

## Resources

- `references/analytics-benchmarks.md` — Industry benchmarks
- `assets/templates/weekly-report.md` — Report template
- `assets/templates/monthly-report.md` — Report template
- `scripts/analytics_dashboard.py` — Dashboard generator
- `scripts/ab_test_calculator.py` — Sample size calculator
- `subagents/analytics-agent.md` — Full documentation
