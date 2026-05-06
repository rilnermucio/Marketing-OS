---
description: Create comprehensive editorial calendars for social media with content pillars, posting schedules, format distribution, and strategic planning.
argument-hint: "<period and niche, e.g., 'monthly for fitness brand' or 'Q1 for SaaS startup'>"
---

# Create Editorial Calendar

> See [CONNECTORS.md](../CONNECTORS.md) for connected services that can provide scheduling integrations and platform data.

Create strategic editorial calendars that balance content pillars, optimize posting times, and maintain consistent brand presence.

## Trigger

This command is invoked when the user says `/criar-calendario` followed by a period and/or niche, or when they ask to create a content calendar, editorial plan, or posting schedule.

## Inputs

Gather the following information. If any required field is missing, ask the user before proceeding:

1. **Period** (required) — Week, month, quarter, or custom range
2. **Platforms** (required) — Instagram, LinkedIn, TikTok, Twitter, YouTube, or multi-platform
3. **Niche/Industry** (optional) — Business sector or content focus
4. **Content Pillars** (optional) — Main themes (will define if not provided)
5. **Posting Frequency** (optional) — How often per platform
6. **Goals** (optional) — Growth, engagement, sales, authority, or mixed
7. **Important Dates** (optional) — Launches, holidays, events to include

## Content Pillar Framework

### Defining Content Pillars (3-5 recommended)

| Pillar Type | Purpose | Content Examples |
|-------------|---------|------------------|
| **Educational** | Establish expertise | How-to, tips, tutorials, guides |
| **Inspirational** | Motivate and connect | Quotes, success stories, transformations |
| **Entertaining** | Increase reach | Trends, humor, relatable content |
| **Promotional** | Drive conversions | Products, offers, launches, CTAs |
| **Community** | Build relationships | Q&A, polls, UGC, behind-scenes |

### Pillar Distribution (Weekly)

| Business Type | Educational | Inspirational | Entertaining | Promotional | Community |
|---------------|-------------|---------------|--------------|-------------|-----------|
| B2B/SaaS | 40% | 15% | 10% | 20% | 15% |
| E-commerce | 25% | 20% | 20% | 25% | 10% |
| Personal Brand | 35% | 25% | 15% | 10% | 15% |
| Service Business | 30% | 20% | 15% | 20% | 15% |
| Creator/Influencer | 25% | 20% | 30% | 10% | 15% |

## Format Distribution by Platform

### Instagram

| Format | Frequency | Best For | Algorithm Priority |
|--------|-----------|----------|-------------------|
| Reels | 4-7x/week | Reach, discovery | Highest |
| Carousel | 3-5x/week | Saves, education | High |
| Feed Post | 2-3x/week | Brand, announcements | Medium |
| Stories | Daily | Engagement, connection | Medium |

### LinkedIn

| Format | Frequency | Best For | Algorithm Priority |
|--------|-----------|----------|-------------------|
| Text Post | 3-5x/week | Thought leadership | High |
| Document/PDF | 2-3x/week | Saves, education | Highest |
| Image + Text | 2-3x/week | Engagement | Medium |
| Video | 1-2x/week | Authority | Medium |

### TikTok

| Format | Frequency | Best For | Algorithm Priority |
|--------|-----------|----------|-------------------|
| Trending | 3-5x/week | Reach, discovery | Highest |
| Educational | 2-4x/week | Authority, saves | High |
| Storytelling | 2-3x/week | Connection | High |
| BTS/Native | 2-3x/week | Authenticity | Medium |

## Optimal Posting Times (Brazil - BRT)

| Platform | Best Times | Best Days | Avoid |
|----------|------------|-----------|-------|
| Instagram | 7-9h, 12-14h, 19-21h | Tue, Wed, Thu | Late night |
| LinkedIn | 7-8h, 12h, 17-18h | Tue, Wed, Thu | Weekends |
| TikTok | 19-22h | Tue, Thu, Fri | Early morning |
| Twitter | 8-10h, 12-13h, 17-18h | Weekdays | Late night |
| YouTube | 14-16h (publish) | Thu, Fri | Monday |

## Weekly Structure Templates

### Template A: Balanced Growth

| Day | Content Type | Pillar | Format |
|-----|--------------|--------|--------|
| Monday | Educational | Value | Carousel/Thread |
| Tuesday | Storytelling | Connection | Reel/Video |
| Wednesday | Tips/Listicle | Value | Carousel |
| Thursday | Behind-scenes | Community | Stories/Post |
| Friday | Promotional | Conversion | Post + Stories |
| Saturday | Entertainment | Reach | Reel/Trend |
| Sunday | Inspirational | Connection | Quote/Post |

### Template B: Authority Building

| Day | Content Type | Pillar | Format |
|-----|--------------|--------|--------|
| Monday | Industry insight | Educational | Text/Thread |
| Tuesday | Case study | Social proof | Carousel/PDF |
| Wednesday | How-to | Educational | Video/Reel |
| Thursday | Opinion/Take | Thought leadership | Text post |
| Friday | Q&A/FAQ | Community | Stories/Live |
| Saturday | Curated content | Value | Carousel |
| Sunday | Week preview | Planning | Stories |

### Template C: Sales-Focused

| Day | Content Type | Pillar | Format |
|-----|--------------|--------|--------|
| Monday | Problem awareness | Educational | Carousel |
| Tuesday | Solution education | Value | Video/Reel |
| Wednesday | Social proof | Trust | Testimonial post |
| Thursday | Objection handling | Educational | Carousel/Stories |
| Friday | Offer/CTA | Promotional | Post + Stories |
| Saturday | UGC/Results | Social proof | Reel/Post |
| Sunday | Teaser/Preview | Curiosity | Stories |

## Important Dates to Consider

### Monthly Recurring

| Type | Examples | Content Opportunity |
|------|----------|---------------------|
| Beginning of month | Goals, planning | Motivational, planning tips |
| Mid-month | Check-ins | Progress, adjustments |
| End of month | Recaps, reflections | Results, learnings |
| Payday (5th, 20th) | Higher purchase intent | Promotional content |

### Brazilian Calendar Highlights

| Month | Key Dates | Content Ideas |
|-------|-----------|---------------|
| January | New Year, back to work | Goals, fresh starts, planning |
| February | Carnival | Behind-scenes, light content |
| March | Women's Day, Consumer Day | Celebrations, promotions |
| April | Easter | Family, renewal themes |
| May | Mother's Day, Labor Day | Tributes, work-life balance |
| June | Festa Junina, Valentine's (BR) | Cultural, relationship content |
| July | Winter vacation | Lighter content, reflection |
| August | Father's Day | Tributes, family content |
| September | Independence Day | National pride, business |
| October | Children's Day | Family, playful content |
| November | Black Friday, Consciousness Day | Major promotions, awareness |
| December | Christmas, New Year | Gratitude, celebration, planning |

## Output Structure

Deliver the calendar in this format:

```
## EDITORIAL CALENDAR

📅 PERIOD: [Week/Month/Quarter — Dates]
📱 PLATFORMS: [Instagram, LinkedIn, TikTok, etc.]
🎯 PRIMARY GOAL: [Growth / Engagement / Sales / Authority]
📊 POSTING FREQUENCY: [X posts per week per platform]

---

### CONTENT PILLARS

| Pillar | Description | Percentage | Hashtag |
|--------|-------------|------------|---------|
| [Pillar 1] | [What it covers] | [X%] | #[tag] |
| [Pillar 2] | [What it covers] | [X%] | #[tag] |
| [Pillar 3] | [What it covers] | [X%] | #[tag] |
| [Pillar 4] | [What it covers] | [X%] | #[tag] |

---

### IMPORTANT DATES THIS PERIOD

| Date | Event | Content Opportunity | Priority |
|------|-------|---------------------|----------|
| [Date] | [Event] | [Content idea] | High/Medium |
| [Date] | [Event] | [Content idea] | High/Medium |

---

### WEEKLY OVERVIEW

#### Week 1: [Theme/Focus]

| Day | Date | Platform | Format | Topic/Theme | Pillar | Time |
|-----|------|----------|--------|-------------|--------|------|
| Mon | [Date] | IG | Carousel | [Topic] | Educational | 19:00 |
| Tue | [Date] | IG | Reel | [Topic] | Entertainment | 20:00 |
| Wed | [Date] | IG/LI | Post | [Topic] | Inspirational | 12:00 |
| Thu | [Date] | IG | Stories | [Topic] | Community | 10:00 |
| Fri | [Date] | IG | Carousel | [Topic] | Promotional | 19:00 |
| Sat | [Date] | IG | Reel | [Topic] | Entertainment | 11:00 |
| Sun | [Date] | IG | Post | [Topic] | Inspirational | 10:00 |

#### Week 2: [Theme/Focus]
[Same structure...]

#### Week 3: [Theme/Focus]
[Same structure...]

#### Week 4: [Theme/Focus]
[Same structure...]

---

### CONTENT IDEAS BY PILLAR

**[Pillar 1 — Educational]:**
1. [Specific content idea]
2. [Specific content idea]
3. [Specific content idea]

**[Pillar 2 — Inspirational]:**
1. [Specific content idea]
2. [Specific content idea]
3. [Specific content idea]

**[Continue for each pillar...]**

---

### FORMAT DISTRIBUTION

| Format | Quantity/Week | Percentage | Primary Platform |
|--------|---------------|------------|------------------|
| Reels/TikTok | [X] | [X%] | Instagram, TikTok |
| Carousel | [X] | [X%] | Instagram, LinkedIn |
| Single Post | [X] | [X%] | All platforms |
| Stories | [X] | [X%] | Instagram |
| Video | [X] | [X%] | YouTube, TikTok |

---

### KPIs TO TRACK

| Metric | Current | Target | How to Improve |
|--------|---------|--------|----------------|
| Reach | [X] | [Target] | [Strategy] |
| Engagement Rate | [X%] | [Target%] | [Strategy] |
| Followers | [X] | [Target] | [Strategy] |
| Saves | [X] | [Target] | [Strategy] |
| Website Clicks | [X] | [Target] | [Strategy] |

---

### PRODUCTION CHECKLIST

**Weekly Prep (Sunday):**
- [ ] Review upcoming week's content
- [ ] Prepare visuals/graphics
- [ ] Write and schedule captions
- [ ] Prepare Stories content
- [ ] Check important dates

**Daily Tasks:**
- [ ] Post scheduled content
- [ ] Engage with comments (first hour)
- [ ] Stories check-in
- [ ] Community engagement (15-30 min)
```

## Final Ask

After delivering the calendar, ask:

"Would you like me to:
1. Write the complete copy for each post in the calendar?
2. Create detailed content briefs for specific pieces?
3. Adjust the calendar for a different posting frequency?
4. Add a specific campaign or launch to the calendar?"
