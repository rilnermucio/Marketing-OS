---
description: Create a complete social media post optimized for the specified platform with hooks, copy, hashtags, and posting recommendations.
argument-hint: "<platform and topic, e.g., 'Instagram post about productivity tips'>"
---

# Create Social Media Post

> See [CONNECTORS.md](../CONNECTORS.md) for connected services that can provide brand guidelines and audience data.

Create a complete, platform-optimized social media post that drives engagement and achieves the specified goal.

## Trigger

This command is invoked when the user says `/criar-post` followed by a platform and topic, or when they ask to create a social media post.

## Inputs

Gather the following information. If any required field is missing, ask the user before proceeding:

1. **Platform** (required) — Instagram, LinkedIn, Twitter/X, TikTok, Facebook, or Pinterest
2. **Topic/Theme** (required) — What the post is about
3. **Goal** (required) — Engagement, reach, traffic, conversion, or brand awareness
4. **Audience** (optional) — Target demographic and psychographic details
5. **Tone** (optional) — Professional, casual, inspirational, educational, or entertaining
6. **Format** (optional) — Feed post, carousel, story, reel, thread, etc.
7. **CTA** (optional) — Desired action from the audience

## Brand Voice Integration

If brand guidelines are available through connected services or have been previously established:
- Apply the documented tone and voice
- Use approved vocabulary and phrases
- Follow visual identity guidelines for any creative direction
- Maintain consistency with previous content

If no brand guidelines exist, ask the user to describe their brand voice in 3-5 adjectives.

## Platform-Specific Requirements

### Instagram

**Feed Post:**
- Caption: Hook in first 125 characters (visible before "more")
- Total caption: Up to 2,200 characters
- Hashtags: 10-15 (mix of high, medium, and niche)
- Format: Conversational, use line breaks for readability

**Carousel:**
- Slide 1: Hook that stops the scroll
- Slides 2-9: One idea per slide, clear and scannable
- Final slide: CTA (follow, save, share, comment)
- Caption: Summarize value + CTA

**Reels:**
- Hook: First 3 seconds must capture attention
- Caption: Short, punchy, under 150 characters
- Hashtags: 3-5 relevant tags
- Include trending audio suggestion if applicable

### LinkedIn

- Hook: Strong first line (210 characters visible)
- Format: Short paragraphs, 1-3 sentences each
- Length: 1,200-1,500 characters optimal
- Hashtags: 3-5 relevant professional tags
- Tone: Professional but personable

### Twitter/X

**Single Tweet:**
- Length: Under 280 characters
- Hook: Lead with value or curiosity
- CTA: Clear action or question

**Thread:**
- Tweet 1: Strong hook + "🧵" indicator
- Body tweets: One point per tweet
- Final tweet: Summary + CTA

### TikTok

- Caption: Under 100 characters
- Hook: First word must grab attention
- Hashtags: 3-5 including trending when relevant
- Sound suggestion: Recommend trending audio if applicable

## Content Generation

### Hook Formulas

Generate at least 3 hook options using these frameworks:

1. **Curiosity**: "This changed everything about how I [topic]..."
2. **Controversy**: "Unpopular opinion: [bold statement]"
3. **Promise**: "Here's exactly how to [achieve result]..."
4. **Question**: "Why does nobody talk about [topic]?"
5. **Story**: "[Timeframe] ago, I was [pain point]..."
6. **List**: "[Number] things I wish I knew about [topic]"

### Body Copy Structure

Apply the appropriate framework based on goal:

**For engagement (PAS):**
- Problem: Identify the pain point
- Agitate: Expand on consequences
- Solution: Present the answer with value

**For conversions (AIDA):**
- Attention: Hook that stops the scroll
- Interest: Engage with relevant details
- Desire: Paint the transformation
- Action: Clear CTA

**For education:**
- Hook: Why this matters
- Context: Background information
- Points: 3-5 key takeaways
- CTA: How to apply this

### Hashtag Strategy

Generate platform-appropriate hashtags:

| Category | Volume | Quantity | Purpose |
|----------|--------|----------|---------|
| High | 1M+ posts | 2-3 | Broad reach |
| Medium | 100K-1M | 3-4 | Balanced |
| Niche | 10K-100K | 4-5 | Targeted |
| Branded | Any | 1-2 | Recognition |

## Output Structure

Deliver the post in this format:

```
## SOCIAL MEDIA POST

📱 PLATFORM: [Platform name]
🎯 GOAL: [Engagement / Reach / Traffic / Conversion]
📍 FORMAT: [Post type]

---

### HOOK OPTIONS

**Option A (Recommended):**
"[Hook text]"

**Option B (Curiosity angle):**
"[Hook text]"

**Option C (Benefit angle):**
"[Hook text]"

---

### POST CONTENT

[Full formatted post copy]

---

### CTA

[Call to action text]

---

### HASHTAGS

[Platform-appropriate hashtag list]

---

### A/B VARIATIONS

**Variation 1 — [Angle name]:**
[Alternative version]

**Variation 2 — [Angle name]:**
[Alternative version]

---

### POSTING RECOMMENDATIONS

⏰ **Best time to post:** [Day and time based on platform]
📊 **Expected engagement:** [Benchmark for this content type]
🔄 **Repurposing:** [How to adapt for other platforms]

---

### AI IMAGE PROMPT (if applicable)

[Optimized prompt for visual creation]
```

## Final Ask

After delivering the post, ask:

"Would you like me to:
1. Create variations with different hooks or angles?
2. Adapt this for other platforms?
3. Generate an AI image prompt for the visual?
4. Create a carousel version with multiple slides?"
