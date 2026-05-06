---
description: Create complete podcast episode scripts including intros, segments, interview questions, show notes, and promotional content.
argument-hint: "<format and topic, e.g., 'interview about productivity' or 'solo episode on marketing trends'>"
---

# Create Podcast Script

> See [CONNECTORS.md](../CONNECTORS.md) for connected services that can provide guest research and audio platform integrations.

Create comprehensive podcast scripts optimized for listener retention, engagement, and professional production.

## Trigger

This command is invoked when the user says `/criar-podcast` followed by a format and topic, or when they ask to create a podcast script, episode outline, or show notes.

## Inputs

Gather the following information. If any required field is missing, ask the user before proceeding:

1. **Format** (required) — Solo, interview, co-hosted, storytelling, or panel
2. **Topic** (required) — Main subject of the episode
3. **Duration** (optional) — Target length (15, 30, 45, or 60+ minutes)
4. **Guest Info** (optional) — For interviews, information about the guest
5. **Audience** (optional) — Who listens to this podcast
6. **Show Name** (optional) — For personalized intros/outros
7. **Tone** (optional) — Educational, conversational, entertaining, or professional

## Episode Format Structures

### Solo Episode Structure

```
INTRO (1-3 min)
├── Hook (30s) — Compelling opening that teases value
├── Show intro (30s) — Podcast name, brief description
├── Episode intro (1-2min) — What you'll cover and why it matters
└── Credibility (30s) — Why you're qualified to speak on this

CONTENT (80% of episode)
├── Segment 1 (8-15 min)
│   ├── Main point introduction
│   ├── Supporting details/examples
│   ├── Actionable takeaway
│   └── Transition to next segment
├── [Ad break if applicable]
├── Segment 2 (8-15 min)
│   ├── Main point introduction
│   ├── Supporting details/examples
│   ├── Actionable takeaway
│   └── Transition
├── Segment 3 (8-15 min)
│   └── [Same structure]
└── [Additional segments as needed]

OUTRO (2-5 min)
├── Key takeaways summary
├── Call to action (subscribe, review, etc.)
├── Tease next episode
└── Sign-off
```

### Interview Episode Structure

```
PRE-INTERVIEW (1-2 min)
├── Hook about guest/topic
├── Show intro
├── Guest introduction and credentials
└── What listeners will learn

INTERVIEW (80% of episode)
├── Opening questions (5-10 min)
│   ├── Background/journey question
│   ├── Current work question
│   └── Hook into main topic
├── [Ad break if applicable]
├── Core questions (20-40 min)
│   ├── Deep-dive questions (3-5)
│   ├── Follow-up probes
│   ├── Story/example prompts
│   └── Contrarian/challenging questions
├── [Mid-roll ad if applicable]
├── Rapid-fire or fun segment (5-10 min)
│   └── Lighter questions, quick answers
└── Closing questions (5 min)
    ├── Best advice question
    ├── Resource recommendations
    └── Where to find guest

OUTRO (2-3 min)
├── Thank guest
├── Summarize key insights
├── Call to action
└── Sign-off
```

### Co-Hosted Episode Structure

```
INTRO (2-4 min)
├── Banter/hook opening
├── Show intro
├── Episode topic introduction
└── Quick agenda preview

CONTENT (80% of episode)
├── Discussion segments
│   ├── Host 1 introduces topic/point
│   ├── Host 2 adds perspective/reaction
│   ├── Back-and-forth exploration
│   ├── Audience example/story
│   └── Key takeaway agreed upon
├── [Ad breaks distributed naturally]
└── Wrap-up discussion

OUTRO (2-4 min)
├── Each host's final thought
├── Listener call to action
├── Next episode tease
└── Dual sign-off
```

### Storytelling Episode Structure

```
HOOK (1-2 min)
├── Dramatic opening (in medias res)
├── Question or mystery to solve
└── Promise of payoff

ACT 1: SETUP (15-20% of episode)
├── Introduce protagonist/situation
├── Establish stakes
├── Present the challenge
└── First turning point

ACT 2: CONFLICT (50-60% of episode)
├── Rising action
├── Complications and obstacles
├── Midpoint revelation
├── Darkest moment/all seems lost
└── Key insight or discovery

ACT 3: RESOLUTION (20-25% of episode)
├── Climax
├── Resolution
├── Transformation/lesson
└── Reflection and takeaway

OUTRO (2-3 min)
├── Connect to listener's life
├── Call to action
└── Sign-off
```

## Script Writing Elements

### Hook Formulas

| Type | Example Opening |
|------|-----------------|
| Question | "What if I told you that everything you know about [topic] is wrong?" |
| Stat/Fact | "73% of [audience] fail at [goal]. Here's why, and how to be in the other 27%." |
| Story | "Three years ago, I was [relatable situation]. Then something changed..." |
| Contrarian | "Everyone says [common advice]. I'm going to tell you why that's terrible advice." |
| Preview | "By the end of this episode, you'll know exactly how to [valuable outcome]." |
| Curiosity | "There's one thing [successful people] do that nobody talks about..." |

### Transition Phrases

| From → To | Phrase Examples |
|-----------|-----------------|
| Intro → Content | "So let's dive in..." / "Here's where it gets interesting..." |
| Point → Point | "Now that we've covered X, let's talk about Y..." |
| Story → Lesson | "Here's what that taught me..." / "The takeaway here is..." |
| Content → Ad | "Quick break, and then we'll get into..." |
| Ad → Content | "Alright, we're back. Now, where were we..." |
| Content → Outro | "Before we wrap up..." / "To bring it all together..." |

### Interview Questions Framework

| Question Type | Purpose | Example |
|---------------|---------|---------|
| Origin | Understand journey | "Take us back to when you first started..." |
| Process | Learn methodology | "Walk us through your approach to..." |
| Challenge | Show struggle | "What was the biggest obstacle you faced?" |
| Lesson | Extract wisdom | "What's something you wish you knew earlier?" |
| Contrarian | Create tension | "Some people would argue [opposite]. How do you respond?" |
| Tactical | Provide value | "Can you give us a specific example of...?" |
| Rapid-fire | Entertainment | "Quick answers: [series of short questions]" |
| Closing | Future-focused | "What's next for you? Where can people find you?" |

### Ad Read Templates

**Host-Read Ad (60 seconds):**
```
You know what's been helping me lately with [relevant problem]?
[Sponsor name]. Here's the thing about [Sponsor] — [key benefit].

I've been using it for [time period] and [personal experience].

What I love most is [specific feature]. It's perfect for [audience fit].

Right now, they're offering [offer] when you go to [URL]
or use code [CODE] at checkout.

That's [URL spelled out] — link in the show notes.
```

**Pre-Produced Ad (30 seconds):**
```
This episode is brought to you by [Sponsor].
[One-sentence value proposition].
[Key differentiator or feature].
Get [offer] at [URL]. That's [URL spelled out].
```

## Show Notes Template

```
EPISODE TITLE: [Title]
EPISODE NUMBER: [#]
PUBLISH DATE: [Date]
DURATION: [Time]

---

DESCRIPTION (150-300 words):
[Compelling description with keywords for SEO]

---

KEY TAKEAWAYS:
• [Takeaway 1]
• [Takeaway 2]
• [Takeaway 3]
• [Takeaway 4]
• [Takeaway 5]

---

TIMESTAMPS:
[00:00] - Introduction
[02:30] - [Topic 1]
[12:45] - [Topic 2]
[25:00] - [Topic 3]
[38:15] - Key takeaways
[42:00] - Where to find [guest]
[44:30] - Closing

---

RESOURCES MENTIONED:
• [Resource 1] - [URL]
• [Resource 2] - [URL]
• [Book/Article] by [Author]

---

CONNECT WITH [GUEST]:
• Website: [URL]
• Instagram: [@handle]
• LinkedIn: [URL]
• Twitter: [@handle]

---

CONNECT WITH US:
• Subscribe: [Link]
• Review: [Link]
• Instagram: [@handle]
• Website: [URL]

---

SPONSORS:
• [Sponsor 1] - [URL] (Code: [CODE])
• [Sponsor 2] - [URL]
```

## Output Structure

Deliver the script in this format:

```
## PODCAST SCRIPT

🎙️ SHOW: [Show Name]
📍 EPISODE: [Number/Title]
⏱️ TARGET DURATION: [Time]
🎯 FORMAT: [Solo / Interview / Co-hosted / Storytelling]

---

### EPISODE OVERVIEW

**Topic:** [Main subject]
**Goal:** [What listeners should learn/feel/do]
**Target Audience:** [Who this is for]

---

### PRE-PRODUCTION NOTES

**Equipment needed:** [Any special requirements]
**Guest prep:** [If applicable, what to send guest]
**Research needed:** [Any facts/stats to verify]

---

### SCRIPT

#### INTRO [0:00 - 2:00]

**[HOOK — 0:00]**

[Word-for-word hook script]

**[SHOW INTRO — 0:30]**

"Welcome to [Show Name], the podcast where [value proposition].
I'm your host, [Name], and today [episode intro]."

**[EPISODE SETUP — 1:00]**

[What you'll cover and why it matters]

---

#### SEGMENT 1: [TITLE] [2:00 - 12:00]

**[Main Point]**

[Full script or detailed talking points]

**[Supporting Detail]**

[Script or talking points]

**[Example/Story]**

[Specific example to illustrate]

**[Actionable Takeaway]**

[What listener can do with this information]

**[Transition]**

"Now that we've covered [X], let's move on to [Y]..."

---

#### [AD BREAK — if applicable] [12:00 - 13:00]

[Ad read script]

---

#### SEGMENT 2: [TITLE] [13:00 - 23:00]

[Same structure as Segment 1]

---

#### SEGMENT 3: [TITLE] [23:00 - 33:00]

[Same structure as Segment 1]

---

#### OUTRO [33:00 - 36:00]

**[SUMMARY]**

"Let's quickly recap what we covered today:
First, [takeaway 1].
Second, [takeaway 2].
And finally, [takeaway 3]."

**[CALL TO ACTION]**

"If you found this valuable, [specific ask — subscribe, review, share].
[Why it matters to you as the host]."

**[NEXT EPISODE TEASE]**

"Next week, we're going to [preview]. You won't want to miss it."

**[SIGN-OFF]**

"Thanks for listening. I'm [Name], and I'll see you in the next one."

---

### SHOW NOTES

[Complete show notes following template above]

---

### EPISODE TITLE OPTIONS

1. "[Title option 1]"
2. "[Title option 2]"
3. "[Title option 3]"

---

### SOCIAL MEDIA CLIPS

**Clip 1 (30-60s):**
Timestamp: [X:XX - X:XX]
Hook: "[Quote or topic for clip]"

**Clip 2 (30-60s):**
Timestamp: [X:XX - X:XX]
Hook: "[Quote or topic for clip]"

**Clip 3 (30-60s):**
Timestamp: [X:XX - X:XX]
Hook: "[Quote or topic for clip]"

---

### PROMOTIONAL COPY

**Instagram/Social Post:**
[Caption for promoting the episode]

**Email Newsletter:**
[Short teaser for email list]

**Twitter Thread:**
[3-5 tweet thread about episode insights]
```

## Final Ask

After delivering the script, ask:

"Would you like me to:
1. Create interview questions for a specific guest?
2. Write ad read scripts for your sponsors?
3. Generate social media content to promote this episode?
4. Develop a series outline for multiple episodes on this topic?"
