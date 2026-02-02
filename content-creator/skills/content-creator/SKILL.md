---
name: content-creator
description: Orchestrate content creation across all channels and formats — social media, blogs, videos, podcasts, emails, and ads. Use when planning content strategy, coordinating multiple content types, or when the task spans multiple specialized areas like copy, SEO, design, and distribution.
---

# Content Creator Skill

Master orchestration skill that coordinates 11 specialized subagents to create comprehensive content strategies and deliverables across all marketing channels.

## When to Use This Skill

- Planning a complete content strategy across multiple channels
- Creating a content piece that requires multiple specialties (copy + design + SEO)
- Coordinating a campaign with various content formats
- When unsure which specialized skill to use — this skill will route to the right one

## Subagent Coordination

This skill orchestrates the following specialized agents:

| Subagent | Specialty | When to Invoke |
|----------|-----------|----------------|
| copy-agent | Persuasive writing | Headlines, CTAs, sales copy, A/B variations |
| seo-agent | Search optimization | Blog posts, articles, keyword strategy |
| social-agent | Social media | Platform-specific posts, hashtags, timing |
| video-agent | Video content | Scripts for YouTube, Reels, TikTok, VSL |
| audio-agent | Audio content | Podcast scripts, audio ads |
| ai-tools-agent | AI generation | Image and video prompts for AI tools |
| design-agent | Visual direction | Color palettes, typography, layouts |
| analytics-agent | Performance | Metrics, KPIs, reporting |
| email-agent | Email marketing | Sequences, newsletters, automation |
| ads-agent | Paid advertising | Ad copy for Meta, Google, TikTok |
| research-agent | Research | Trends, competitors, audience analysis |

## Content Creation Workflow

### Phase 1: Discovery
1. Identify the content objective (awareness, engagement, conversion)
2. Define target audience and their pain points
3. Determine platforms and formats needed
4. Establish brand voice and tone requirements

### Phase 2: Research
Invoke **research-agent** to:
- Analyze competitor content
- Identify trending topics
- Map audience preferences
- Gather relevant data and statistics

### Phase 3: Strategy
- Select content pillars aligned with objectives
- Plan content mix (educational, entertaining, promotional)
- Define distribution channels and timing
- Set success metrics

### Phase 4: Creation
Route to specialized agents based on content type:

| Content Type | Primary Agent | Supporting Agents |
|--------------|---------------|-------------------|
| Blog post | seo-agent | copy-agent, research-agent |
| Instagram post | social-agent | copy-agent, design-agent |
| YouTube video | video-agent | copy-agent, ai-tools-agent |
| Email sequence | email-agent | copy-agent |
| Ad campaign | ads-agent | copy-agent, design-agent |
| Podcast episode | audio-agent | research-agent |

### Phase 5: Optimization
Invoke **analytics-agent** to:
- Define KPIs for each content piece
- Set up tracking recommendations
- Plan A/B testing strategy

## Supported Niches

Each niche has specific tone, terminology, and content preferences:

| Niche | Tone | Key Themes | Content Focus |
|-------|------|------------|---------------|
| Marketing Digital | Authoritative, data-driven | ROI, growth, tools | Case studies, tutorials |
| Inteligência Artificial | Educational, accessible | Innovation, practical use | Demos, explainers |
| Desenvolvimento Pessoal | Inspirational, empathetic | Growth, habits, mindset | Stories, frameworks |
| Desenvolvimento Profissional | Professional, practical | Career, skills, leadership | Tips, guides |
| Tecnologia | Technical, didactic | Code, tools, trends | Tutorials, reviews |
| Empreendedorismo | Motivational, strategic | Business, sales, scale | Lessons, strategies |
| Finanças Pessoais | Educational, trustworthy | Investment, savings | Guides, calculators |
| Saúde e Bem-Estar | Warm, supportive | Exercise, nutrition, mental | Tips, routines |
| Educação | Didactic, encouraging | Learning, study tips | Methods, resources |
| Produtividade | Practical, direct | Time, focus, tools | Systems, hacks |

## Content Formats Reference

### Short-Form Content
| Format | Dimensions | Specs |
|--------|------------|-------|
| Instagram Feed | 1080x1080 or 1080x1350 | Caption up to 2200 chars |
| Instagram Stories | 1080x1920 | 15s video or static |
| Instagram Reels | 1080x1920 | 15-90s |
| TikTok | 1080x1920 | 15s-10min |
| Twitter/X | 280 chars | Images 1200x675 |
| LinkedIn Post | Up to 3000 chars | Images 1200x1200 |

### Long-Form Content
| Format | Length | Key Elements |
|--------|--------|--------------|
| Blog Post | 1500-3000 words | SEO-optimized, structured headings |
| YouTube Video | 8-20 minutes | Scripted, retention hooks |
| Podcast Episode | 20-60 minutes | Structured segments |
| Email Newsletter | 300-500 words | Scannable, single CTA |
| Landing Page | Varies | Headline, benefits, social proof, CTA |

## Copywriting Frameworks

### AIDA (Awareness → Interest → Desire → Action)
Best for: Landing pages, sales emails, ads
```
[ATTENTION] Hook that stops the scroll
[INTEREST] Present the problem or opportunity
[DESIRE] Show benefits and transformation
[ACTION] Clear, urgent CTA
```

**Example:**
```
[ATTENTION] "You're losing 3 hours every day to tasks AI could do for you."
[INTEREST] "Most professionals spend 40% of their time on repetitive work."
[DESIRE] "Imagine finishing your day at 3pm with everything done."
[ACTION] "Start your free trial — no credit card required."
```

### PAS (Problem → Agitate → Solution)
Best for: Email sequences, social posts, VSL
```
[PROBLEM] Identify the specific pain
[AGITATE] Intensify the consequences
[SOLUTION] Present relief through your offer
```

**Example:**
```
[PROBLEM] "Creating content takes you 10+ hours per week."
[AGITATE] "That's 500+ hours per year you could spend growing your business."
[SOLUTION] "Our templates cut content creation time by 80%."
```

### BAB (Before → After → Bridge)
Best for: Case studies, testimonials, storytelling
```
[BEFORE] Current painful situation
[AFTER] Desired transformed state
[BRIDGE] Your product/service as the path
```

**Example:**
```
[BEFORE] "Maria struggled to post consistently — 2-3 times per month at best."
[AFTER] "Now she posts daily and grew from 1K to 50K followers in 6 months."
[BRIDGE] "She used our content calendar system."
```

### 4Ps (Promise → Picture → Proof → Push)
Best for: Sales pages, webinars
```
[PROMISE] Main benefit
[PICTURE] Visualization of the result
[PROOF] Social proof, data, testimonials
[PUSH] CTA with urgency
```

## Hashtag Strategy

### Instagram Hashtag Mix
Use a balanced mix for optimal reach:
- **2-3 high volume** (1M+ posts): Broad reach, high competition
- **3-4 medium volume** (100K-1M posts): Good reach, moderate competition
- **3-4 low volume** (10K-100K posts): Niche, targeted, higher engagement
- **1-2 branded**: Your own branded hashtags

### LinkedIn
- Use 3-5 hashtags maximum
- Mix industry (#marketing) with topic (#contentcreation)
- Check hashtag follower counts

### TikTok
- Use trending sounds and hashtags
- Mix broad (#fyp) with niche (#marketingtips)
- Include challenge hashtags when relevant

## Quality Checklist

Before delivering any content, verify:

- [ ] Aligned with stated objective and target audience
- [ ] Consistent tone of voice throughout
- [ ] Clear, actionable CTA
- [ ] SEO optimized (when applicable)
- [ ] No grammatical errors
- [ ] Properly formatted for the platform
- [ ] A/B variations included (when requested)
- [ ] Success metrics defined
- [ ] Relevant hashtags (for social)
- [ ] Strong hook in first 3 seconds/lines
- [ ] Retention structure applied (for video)
- [ ] Visual direction included (when applicable)

## Standard Deliverables

For every content request, provide:

1. **Primary content** — formatted for the target platform
2. **2-3 variations** — for A/B testing
3. **Optimization notes** — platform-specific recommendations
4. **Suggested metrics** — how to measure success
5. **Next steps** — actionable follow-up items
6. **Hashtags/Keywords** — when applicable
7. **AI prompts** — for image/video generation when needed

## Resources

### Templates
- `assets/templates/youtube-script.md` — YouTube long-form scripts
- `assets/templates/reels-tiktok-script.md` — Short video scripts
- `assets/templates/instagram-feed-post.md` — Feed post templates
- `assets/templates/post-instagram-carrossel.md` — Carousel structures
- `assets/templates/email-newsletter.md` — Email templates
- `assets/templates/sales-page.md` — Landing page structure

### Swipe Files
- `assets/swipe-files/headlines-virais.md` — Proven headline formulas
- `assets/swipe-files/hooks-reels.md` — Video hooks
- `assets/swipe-files/ctas-conversao.md` — CTA examples
- `assets/swipe-files/copy-carrossel.md` — Carousel copy

### References
- `references/niches.md` — Niche-specific guidance
- `references/social-media.md` — Platform best practices
- `references/design-specs.md` — Dimensions and specs

### Scripts
- `scripts/seo_analyzer.py` — SEO analysis
- `scripts/hashtag_generator.py` — Hashtag generation
- `scripts/hook_generator.py` — Hook creation
- `scripts/content_calendar.py` — Calendar generation
