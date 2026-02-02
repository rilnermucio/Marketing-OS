---
description: Create a complete Instagram carousel with hook slide, content slides, CTA, caption, and visual direction.
argument-hint: "<topic and type, e.g., '10 productivity tips' or 'storytelling carousel about my journey'>"
---

# Create Instagram Carousel

> See [CONNECTORS.md](../CONNECTORS.md) for connected services that can provide brand guidelines and design assets.

Create a complete Instagram carousel optimized for saves, shares, and engagement with strategic slide structure.

## Trigger

This command is invoked when the user says `/criar-carrossel` followed by a topic, or when they ask to create a carousel for Instagram or LinkedIn.

## Inputs

Gather the following information. If any required field is missing, ask the user before proceeding:

1. **Topic** (required) — Main subject of the carousel
2. **Type** (required) — Educational, list, storytelling, comparison, how-to, or myth-busting
3. **Slide count** (optional) — 5-10 slides recommended, default to 8
4. **Audience** (optional) — Who this is for
5. **Goal** (optional) — Saves, shares, follows, or traffic
6. **Tone** (optional) — Professional, casual, bold, or inspirational
7. **Visual style** (optional) — Minimalist, colorful, branded, or photo-based

## Carousel Types

Adapt the structure based on the selected type:

### Educational

```
Slide 1: Hook — Bold statement or question
Slide 2: Problem/context — Why this matters
Slides 3-8: Teaching points — One concept per slide
Slide 9: Summary — Key takeaways
Slide 10: CTA — Follow for more
```

### List/Tips

```
Slide 1: Hook — "[Number] [topic] you need to know"
Slides 2-9: One tip per slide with brief explanation
Slide 10: CTA — Save this + follow
```

### Storytelling

```
Slide 1: Hook — Intriguing statement or question
Slide 2: Setting — Context and situation
Slides 3-7: Journey — Challenges and turning points
Slide 8: Transformation — The change
Slide 9: Lesson — What you learned
Slide 10: CTA — Comment your experience
```

### Comparison

```
Slide 1: Hook — "[A] vs [B]: Which is better?"
Slides 2-4: Option A — Pros and context
Slides 5-7: Option B — Pros and context
Slide 8: Analysis — Key differences
Slide 9: Verdict — Recommendation
Slide 10: CTA — What's your choice?
```

### How-To

```
Slide 1: Hook — "How to [achieve result]"
Slide 2: Overview — What you'll learn
Slides 3-8: Steps — One step per slide with visual
Slide 9: Result — What success looks like
Slide 10: CTA — Try it and DM results
```

### Myth-Busting

```
Slide 1: Hook — "Stop believing these [topic] myths"
Slides 2-8: Myth + Truth pairs
Slide 9: Reality check — What actually works
Slide 10: CTA — Share to help others
```

## Slide Copy Guidelines

### Slide 1 (Hook)

The most critical slide. Must stop the scroll in under 2 seconds.

**Hook formulas:**
- "[Number] [things] that will [change/transform/help] your [area]"
- "Stop [common mistake]. Do this instead."
- "The truth about [topic] nobody tells you"
- "I [achieved result] in [timeframe]. Here's how:"
- "[Bold controversial statement]"

**Design requirements:**
- Maximum 8-12 words
- Font size: Large and readable
- High contrast between text and background
- Face or eye-catching visual element

### Slides 2-9 (Content)

**Copy rules:**
- One idea per slide (never more)
- Maximum 3-4 short sentences OR 3-5 bullet points
- Use numbers or icons to break up text
- Include visual metaphors when possible
- Build momentum — each slide should make them want the next

**Visual hierarchy:**
- Headline: Main point (bold, larger)
- Body: Supporting detail (regular, smaller)
- Optional: Icon or illustration

### Slide 10 (CTA)

**Effective CTAs:**
- "Save this for later 🔖"
- "Follow @[handle] for more [topic]"
- "Share with someone who needs this"
- "Comment [emoji] if you agree"
- "Link in bio to learn more"

**Design requirements:**
- Clear, single action
- Username visible
- Contrasting CTA button or element

## Caption Structure

Generate a caption that complements the carousel:

```
[Hook — first 125 characters must grab attention]

[Brief context — why this matters]

[Key takeaway summary — what they'll learn]

[Engagement question — spark comments]

[CTA — what you want them to do]

.
.
.

[Hashtags — 10-15 relevant tags]
```

## Output Structure

Deliver the carousel in this format:

```
## INSTAGRAM CAROUSEL

📱 FORMAT: Carousel ([X] slides)
🎯 TYPE: [Educational / List / Story / etc.]
🎨 STYLE: [Visual direction]

---

### SLIDE-BY-SLIDE CONTENT

**SLIDE 1 — HOOK**
📝 Text: "[Hook copy]"
🎨 Visual: [Design direction]
💡 Why it works: [Brief explanation]

---

**SLIDE 2 — [PURPOSE]**
📝 Text: "[Slide copy]"
🎨 Visual: [Design direction]

---

**SLIDE 3 — [PURPOSE]**
📝 Text: "[Slide copy]"
🎨 Visual: [Design direction]

[Continue for all slides...]

---

**SLIDE [X] — CTA**
📝 Text: "[CTA copy]"
🎨 Visual: [Design direction]

---

### CAPTION

[Full formatted caption with hashtags]

---

### ALTERNATIVE HOOKS

**Option A:** "[Alternative hook]"
**Option B:** "[Alternative hook]"

---

### VISUAL DIRECTION

**Color palette:** [Suggested colors]
**Typography:** [Font recommendations]
**Style:** [Minimalist / Bold / Photo-based / etc.]
**Consistency:** [How to maintain visual thread]

---

### AI IMAGE PROMPTS

**Cover slide prompt:**
"[Optimized prompt for slide 1]"

**Content slide template prompt:**
"[Optimized prompt for consistent content slides]"

---

### POSTING RECOMMENDATIONS

⏰ **Best time:** [Day and time]
📊 **Target metrics:** Saves > Shares > Comments > Likes
🔄 **Repurpose as:** [LinkedIn doc, Twitter thread, blog post]
```

## Final Ask

After delivering the carousel, ask:

"Would you like me to:
1. Adjust the slide count or restructure the flow?
2. Create alternative hooks for A/B testing?
3. Generate more detailed AI image prompts for Canva or Figma?
4. Adapt this carousel for LinkedIn document format?"
