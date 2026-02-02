---
description: Create a complete video script with hook, structure, visual directions, and thumbnail concept for YouTube, Reels, TikTok, Shorts, or VSL.
argument-hint: "<format and topic, e.g., 'YouTube tutorial on email marketing' or 'TikTok about morning routine'>"
---

# Create Video Script

> See [CONNECTORS.md](../CONNECTORS.md) for connected services that can provide brand voice and content guidelines.

Create a complete video script optimized for retention and engagement, tailored to the specific platform and format.

## Trigger

This command is invoked when the user says `/criar-video` followed by a format and topic, or when they ask to create a video script, YouTube video, Reels, TikTok, Shorts, or VSL.

## Inputs

Gather the following information. If any required field is missing, ask the user before proceeding:

1. **Format** (required) — YouTube long-form, YouTube Shorts, Instagram Reels, TikTok, or VSL
2. **Topic** (required) — What the video is about
3. **Goal** (required) — Educate, entertain, inspire, or convert
4. **Duration** (optional) — Target length in minutes/seconds
5. **Audience** (optional) — Who this is for
6. **Tone** (optional) — Professional, casual, energetic, or authoritative
7. **CTA** (optional) — Desired action from viewers

## Format Specifications

### YouTube Long-Form (8-20 minutes)

**Structure:**
```
HOOK (0-30s)
├── Pattern interrupt (0-3s)
├── Promise/hook statement (3-10s)
├── Credibility (10-20s)
└── Roadmap (20-30s)

CONTENT (80% of video)
├── Section 1 + retention bump
├── Section 2 + retention bump
├── Section 3 + retention bump
└── Continue as needed...

CONCLUSION (1-2 min)
├── Summary of key points
├── Main takeaway
├── CTA (subscribe, comment, link)
└── Tease next video
```

**Retention strategies:**
- Open loop every 2-3 minutes
- Pattern interrupt every 60-90 seconds
- B-roll at attention dips
- Direct address to camera

### YouTube Shorts / Instagram Reels / TikTok (15-60s)

**Structure:**
```
HOOK (0-3s)
├── Visual pattern interrupt
└── Curiosity/promise statement

CONTENT (3s-50s)
├── Point 1 (with text overlay)
├── Point 2 (with text overlay)
├── Point 3 (with text overlay)
└── Quick transitions between

CTA (last 5-10s)
├── Clear call to action
└── Loop opportunity (end connects to start)
```

**Platform nuances:**
- **TikTok**: Native feel, trending sounds, text on screen
- **Reels**: Polished but authentic, music-driven
- **Shorts**: Information-dense, fast-paced

### VSL (Video Sales Letter) (5-45 minutes)

**Structure:**
```
HOOK (0-2 min)
├── Pattern interrupt
├── Big promise
├── Identify audience and pain
└── Credibility hint

PROBLEM (2-8 min)
├── Describe pain in detail
├── Common solutions that fail
├── Why it's not their fault
└── Agitate consequences

SOLUTION (8-15 min)
├── Introduce your solution
├── Why it's different
├── The mechanism (how it works)
└── Proof and results

OFFER (15-25 min)
├── What they get
├── Bonuses (stack value)
├── Price reveal (anchor higher first)
├── Guarantee
└── Scarcity/urgency

CLOSE (25-30+ min)
├── Summary of transformation
├── Final objection handling
├── Clear CTA
└── Consequence of inaction
```

## Hook Framework

Generate 3-5 hook options based on the content:

### Hook Categories

**Curiosity hooks:**
- "This changed everything about how I [topic]..."
- "Nobody's talking about this, but..."
- "I just discovered why [common thing] doesn't work..."

**Controversy hooks:**
- "Unpopular opinion: [bold statement]..."
- "Everyone's doing [thing] wrong..."
- "Stop [common advice] immediately..."

**Result hooks:**
- "How I [achieved result] in [timeframe]..."
- "This [method] got me [specific result]..."
- "[Number] [result] with just [simple method]..."

**Tutorial hooks:**
- "Here's exactly how to [achieve thing]..."
- "3 steps to [result] (that actually work)..."
- "Watch me [do thing] in real time..."

**Story hooks:**
- "I was [relatable situation] when [unexpected thing happened]..."
- "Last week, something crazy happened..."
- "You won't believe what I found out..."

## Script Writing Guidelines

### For YouTube Long-Form

Use the three-column format:

```
TIMESTAMP | VISUAL | AUDIO/SCRIPT
----------|--------|-------------
0:00-0:03 | [B-roll description] | "[Word-for-word script]"
0:03-0:10 | [Face to camera] | "[Script continues]"
```

Include:
- Exact dialogue/narration
- Visual direction (b-roll, screen recording, graphics)
- On-screen text callouts
- Music/sound effect cues
- Retention notes (where to add pattern interrupts)

### For Short-Form (Reels/TikTok/Shorts)

```
[SECOND] VISUAL | TEXT ON SCREEN | VOICEOVER
--------|----------------|----------
[0-1s] Close-up face | | "POV:"
[1-3s] Reaction | "When you discover..." | "...you just discovered"
[3-8s] Tutorial | "Step 1: Do this" | "First, you need to..."
```

### For VSL

Full word-for-word script with:
- Slide/visual direction for each section
- Emphasis markers for key phrases
- Pause indicators [PAUSE]
- Emotional beat notes

## Output Structure

Deliver the script in this format:

```
## VIDEO SCRIPT

📹 FORMAT: [YouTube Long-form / Reels / TikTok / Shorts / VSL]
⏱️ ESTIMATED DURATION: [XX:XX]
🎯 GOAL: [Educate / Entertain / Inspire / Convert]
👥 AUDIENCE: [Target description]

---

### HOOK OPTIONS

**Option A (Recommended):**
"[Word-for-word hook]"
Why it works: [Brief explanation]

**Option B:**
"[Alternative hook]"

**Option C:**
"[Alternative hook]"

---

### FULL SCRIPT

#### SECTION 1: [TITLE] (0:00-X:XX)

[TIMESTAMP] VISUAL: [Description]
SCRIPT: "[Word-for-word dialogue]"

💡 RETENTION NOTE: [Tip for maintaining attention]

[Continue for all sections...]

---

### VISUAL DIRECTION

**B-roll needed:**
- [Scene 1 description]
- [Scene 2 description]
- [Scene 3 description]

**On-screen text:**
- [Text callout 1]
- [Text callout 2]

**Graphics/animations:**
- [Description]

---

### TITLE OPTIONS

1. "[Title 1]" — [Character count]
2. "[Title 2]" — [Character count]
3. "[Title 3]" — [Character count]

---

### THUMBNAIL CONCEPT

**Visual:** [Description of image composition]
**Text:** [2-3 words max]
**Emotion:** [Expression if face is shown]
**Colors:** [Suggested palette]

---

### CTA SCRIPT

"[Word-for-word closing CTA]"

---

### RETENTION STRATEGY

| Timestamp | Technique | Description |
|-----------|-----------|-------------|
| [X:XX] | [Technique] | [What to do] |
| [X:XX] | [Technique] | [What to do] |

---

### DESCRIPTION/CAPTION

[For YouTube: Full description with timestamps]
[For Short-form: Caption with hashtags]

---

### MUSIC/SOUND

**Suggested tracks:**
- [Genre/mood 1]
- [Genre/mood 2]

**Sound effects:**
- [SFX 1 at timestamp]
- [SFX 2 at timestamp]
```

## Final Ask

After delivering the script, ask:

"Would you like me to:
1. Expand any section with more detail or examples?
2. Create alternative hooks for A/B testing?
3. Generate additional thumbnail concepts?
4. Adapt this script for a different platform or duration?"
