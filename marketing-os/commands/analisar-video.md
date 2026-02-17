---
description: Analyze YouTube or TikTok videos to extract hooks, CTAs, retention strategies, content structure, and actionable insights.
argument-hint: "<video URL or description, e.g., 'https://youtube.com/watch?v=...' or 'analyze MrBeast's latest video strategy'>"
---

# Analyze Video

> See [CONNECTORS.md](../CONNECTORS.md) for connected services that can capture screenshots and access video data.

Analyze any video (YouTube, TikTok, Instagram Reels) to reverse-engineer its hooks, structure, retention strategies, CTAs, and engagement techniques into actionable insights.

## Trigger

This command is invoked when the user says `/analisar-video` followed by a video URL or description, or when they ask to analyze, break down, or reverse-engineer a video's strategy.

## Inputs

Gather the following information. If any required field is missing, ask the user before proceeding:

1. **Video Source** (required) — URL, transcript, or description of the video to analyze
2. **Analysis Focus** (optional) — Hooks, retention, CTAs, storytelling, editing, all
3. **Content Type** (optional) — YouTube long-form, Shorts, Reels, TikTok, VSL
4. **Purpose** (optional) — Learn from it, replicate style, improve own content, competitive analysis
5. **Your Niche** (optional) — To contextualize insights for your specific market

## Analysis Framework

### 1. Hook Analysis (First 3-30 seconds)

Break down the opening into:

| Element | Analysis |
|---------|----------|
| **Hook type** | Curiosity, controversy, promise, story, question, shock |
| **First words** | Exact opening line and why it works |
| **Visual hook** | What appears on screen in first 3 seconds |
| **Pattern interrupt** | What stops the scroll |
| **Tension created** | What open loop keeps viewers watching |

**Hook effectiveness score:** Rate 1-10 based on scroll-stopping power

### 2. Content Structure Map

Map the complete video structure with timestamps:

```
[00:00-00:XX] HOOK — [Type and description]
[00:XX-XX:XX] SETUP — [Context and framing]
[XX:XX-XX:XX] CONTENT BLOCK 1 — [Topic and technique]
[XX:XX-XX:XX] RETENTION BUMP — [Re-engagement technique]
[XX:XX-XX:XX] CONTENT BLOCK 2 — [Topic and technique]
[XX:XX-XX:XX] CLIMAX — [Peak value moment]
[XX:XX-XX:XX] CTA — [Call to action]
[XX:XX-XX:XX] OUTRO — [Closing strategy]
```

### 3. Retention Strategy Analysis

| Technique | Timestamp | Effect |
|-----------|-----------|--------|
| Open loops | [Where used] | Keeps viewer watching to close the loop |
| Pattern interrupts | [Where used] | Resets attention when focus drops |
| Curiosity gaps | [Where used] | Creates "I need to know" moments |
| Visual changes | [Where used] | Scene cuts, B-roll, graphics |
| Pacing changes | [Where used] | Speed up/slow down energy |
| Preview/teases | [Where used] | Shows what's coming next |
| Emotional shifts | [Where used] | Moves between emotions |

**Retention curve estimate:** Predict where audience drops off and why

### 4. CTA Analysis

| CTA | Timestamp | Type | Placement |
|-----|-----------|------|-----------|
| [CTA 1] | [Time] | Subscribe/Follow | [In content or outro] |
| [CTA 2] | [Time] | Like/Save | [Contextual or explicit] |
| [CTA 3] | [Time] | Comment | [Question-driven or challenge] |
| [CTA 4] | [Time] | Link/Product | [Description, pinned, spoken] |

**CTA integration quality:** Seamless vs. disruptive (1-10 scale)

### 5. Storytelling/Narrative Analysis

| Element | Description |
|---------|-------------|
| **Narrative arc** | Hero's journey, problem-solution, before-after, list, tutorial |
| **Emotional journey** | What emotions are triggered and when |
| **Characters** | Who appears and their role in the narrative |
| **Conflict/tension** | What creates stakes and interest |
| **Resolution** | How the story/content resolves |
| **Transformation** | Before/after state of the viewer |

### 6. Technical/Editing Analysis

| Aspect | Observation |
|--------|-------------|
| **Cuts per minute** | Editing pace and rhythm |
| **B-roll usage** | Supporting visuals |
| **Text overlays** | On-screen text, captions, graphics |
| **Music/sound** | Audio layers and transitions |
| **Transitions** | Cut types (jump cuts, transitions, match cuts) |
| **Thumbnail** | Click-worthiness analysis |
| **Title** | SEO and curiosity optimization |

### 7. Engagement Triggers

Identify specific techniques used to drive engagement:

- **Comment bait:** Questions, polls, challenges
- **Share triggers:** Relatable moments, tag-a-friend, controversial takes
- **Save triggers:** Actionable tips, frameworks, step-by-step
- **Follow triggers:** Series teasers, consistent value promise

## Output Structure

Deliver the analysis in this format:

```
## VIDEO ANALYSIS

🎬 VIDEO: [Title or description]
📱 PLATFORM: [YouTube / TikTok / Instagram]
⏱️ DURATION: [Length]
👤 CREATOR: [Creator name]
🎯 PURPOSE: [Video's primary goal]

---

### EXECUTIVE SUMMARY

[2-3 sentences summarizing the video's strategy and why it works or doesn't]

**Overall score:** [X]/10
**Best element:** [What stands out most]
**Weakest element:** [What could be improved]

---

### HOOK BREAKDOWN

**Opening line:** "[Exact first words]"
**Hook type:** [Classification]
**Why it works:** [Analysis]
**Hook score:** [X]/10

**Alternative hooks (if you were making this video):**
1. "[Improved hook option A]"
2. "[Improved hook option B]"
3. "[Improved hook option C]"

---

### STRUCTURE MAP

[Complete timestamped structure with annotations]

---

### RETENTION TECHNIQUES

[Table of all retention techniques with timestamps]

**Estimated retention curve:**
[ASCII chart or description of where viewers likely drop]

---

### CTA CATALOG

[All CTAs with timestamps, types, and effectiveness]

---

### STORYTELLING ANALYSIS

[Narrative arc, emotional journey, transformation]

---

### TECHNICAL ANALYSIS

[Editing, visuals, audio, title, thumbnail]

---

### KEY TAKEAWAYS

📌 **Top 5 techniques to replicate:**
1. [Technique + how to apply]
2. [Technique + how to apply]
3. [Technique + how to apply]
4. [Technique + how to apply]
5. [Technique + how to apply]

---

### ADAPTATION BLUEPRINT

**How to apply this to your content:**

[Specific recommendations for the user's niche and format]

**Script template inspired by this analysis:**
[A reusable template based on the video's structure]
```

## Final Ask

After delivering the analysis, ask:

"Would you like me to:
1. Create a script using this video's structure for your topic?
2. Generate hook variations inspired by this analysis?
3. Analyze another video from the same creator for pattern detection?
4. Create a full content strategy based on these techniques?"
