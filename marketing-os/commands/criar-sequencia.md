---
description: Create a coordinated multi-channel content sequence across email, social media, and ads with unified messaging and timeline.
argument-hint: "<campaign goal and channels, e.g., 'product launch across email + Instagram + Meta Ads' or '30-day nurture sequence'>"
---

# Create Multi-Channel Sequence

> See [CONNECTORS.md](../CONNECTORS.md) for connected services that can publish to platforms and automate workflows.

Create a coordinated multi-channel content sequence with unified messaging, timeline, and content for each touchpoint across email, social media, and ads.

## Trigger

This command is invoked when the user says `/criar-sequencia` followed by a campaign goal and channels, or when they ask to create a multi-channel campaign, content sequence, or coordinated marketing campaign.

## Inputs

Gather the following information. If any required field is missing, ask the user before proceeding:

1. **Campaign Goal** (required) — Launch, promotion, nurture, re-engagement, awareness, conversion
2. **Channels** (required) — Email, Instagram, LinkedIn, TikTok, Twitter/X, YouTube, Meta Ads, Google Ads, WhatsApp
3. **Duration** (required) — 7 days, 14 days, 30 days, or custom
4. **Product/Offer** (required) — What is being promoted
5. **Audience** (required) — Target audience and their awareness level
6. **Budget** (optional) — Paid media budget
7. **Existing Assets** (optional) — Email list size, social following, content library
8. **Tone** (optional) — Professional, casual, urgent, storytelling, educational

## Sequence Type Specifications

### Launch Sequence (7-14 days)

**Phases:**
```
PRE-LAUNCH (Days 1-5)    → Build anticipation
LAUNCH (Days 6-8)        → Cart open, maximum exposure
CLOSING (Days 9-11)      → Urgency, last chance
POST-LAUNCH (Days 12-14) → Results, onboarding
```

**Channel orchestration:**

| Phase | Email | Social | Ads |
|-------|-------|--------|-----|
| Pre-launch | Teaser series (3 emails) | Behind-the-scenes, countdown | Awareness campaign |
| Launch | Announcement + benefits | Launch post + stories | Conversion campaign |
| Closing | Urgency + testimonials | Social proof + countdown | Retargeting |
| Post | Buyer welcome / non-buyer nurture | Results + celebration | Lookalike |

### Nurture Sequence (30 days)

**Phases:**
```
WEEK 1: Introduction & Value     → Who you are, why follow
WEEK 2: Education & Authority    → Teach, demonstrate expertise
WEEK 3: Social Proof & Trust     → Case studies, testimonials
WEEK 4: Conversion & Offer       → Present solution, CTA
```

### Promotion Sequence (5-7 days)

**Phases:**
```
DAY 1: Announcement              → The offer is live
DAY 2: Benefits deep dive        → Why this matters
DAY 3: Social proof              → Others love it
DAY 4: Objection handling        → FAQ, concerns addressed
DAY 5: Bonus/incentive           → Extra value for action
DAY 6: Last day warning          → Urgency
DAY 7: Final hours               → Now or never
```

### Re-engagement Sequence (14 days)

**Phases:**
```
DAYS 1-3: "We miss you"          → Reconnect emotionally
DAYS 4-7: Fresh value            → New content, updated offer
DAYS 8-11: Social proof          → What others are doing
DAYS 12-14: Final offer          → Special comeback incentive
```

## Unified Messaging Framework

### Core Message Architecture

Before creating channel-specific content, define:

```
CORE MESSAGE:
"[One sentence that captures the entire campaign message]"

KEY PROMISE:
"[The primary transformation/benefit]"

SUPPORTING POINTS:
1. [Proof point / benefit #1]
2. [Proof point / benefit #2]
3. [Proof point / benefit #3]

EMOTIONAL HOOK:
"[The feeling you want to evoke]"

PRIMARY CTA:
"[The one action you want across all channels]"
```

### Channel Adaptation Rules

| Channel | Tone Adjustment | Format | CTA Style |
|---------|----------------|--------|-----------|
| Email | Personal, direct | Long-form, storytelling | Button + link |
| Instagram Feed | Visual, aspirational | Carousel or single image | "Link na bio" |
| Instagram Stories | Casual, behind-scenes | Polls, questions, swipe-up | Sticker link |
| Instagram Reels | Entertaining, fast-paced | 15-30s video | Caption CTA |
| LinkedIn | Professional, insightful | Text post or article | "Comment below" |
| Twitter/X | Concise, provocative | Thread or single tweet | Link in thread |
| TikTok | Authentic, trend-driven | Native video, 15-60s | Bio link |
| Meta Ads | Direct, benefit-focused | Image/video + copy | Button CTA |
| Google Ads | Search-intent focused | Headlines + descriptions | Site link |
| WhatsApp | Intimate, conversational | Message + media | Reply CTA |

## Timeline Generation

### Daily Touchpoint Map

For each day of the sequence, define:

```
DAY [N] — [Phase name]

THEME: [Daily theme/message angle]

📧 EMAIL:
  Subject: "[Subject line]"
  Preview: "[Preview text]"
  Key message: [1-2 sentences]
  CTA: [Action]
  Send time: [HH:MM]

📱 INSTAGRAM:
  Format: [Feed / Stories / Reels]
  Content: [Description]
  Caption: [First 2 lines]
  Hashtags: [5-10 relevant]
  Post time: [HH:MM]

💼 LINKEDIN:
  Format: [Post / Article]
  Hook: [First line]
  Content: [Key points]
  Post time: [HH:MM]

📢 ADS:
  Platform: [Meta / Google]
  Objective: [Awareness / Traffic / Conversion]
  Creative: [Description]
  Copy: [Primary text]
  Budget: R$ [daily budget]

💬 WHATSAPP (if applicable):
  Message: [Short message]
  Media: [Image/video if any]
  Send time: [HH:MM]
```

## Output Structure

Deliver the sequence in this format:

```
## MULTI-CHANNEL SEQUENCE

🎯 CAMPAIGN: [Campaign name]
📅 DURATION: [X] days
📢 CHANNELS: [List of channels]
💰 PRODUCT: [Product/offer]
👤 AUDIENCE: [Target audience]

---

### UNIFIED MESSAGE FRAMEWORK

**Core message:** "[One sentence]"
**Key promise:** "[Transformation]"
**Emotional hook:** "[Feeling]"
**Primary CTA:** "[Action]"

---

### SEQUENCE OVERVIEW

[Visual timeline showing all touchpoints across all channels]

| Day | Email | Social | Ads | Theme |
|-----|-------|--------|-----|-------|
| 1 | [Brief] | [Brief] | [Brief] | [Theme] |
| 2 | [Brief] | [Brief] | [Brief] | [Theme] |
| ... | ... | ... | ... | ... |

---

### DETAILED DAY-BY-DAY CONTENT

**DAY 1 — [Theme]**

📧 **Email:**
Subject: "[Subject]"
[Full email copy]

📱 **Instagram:**
Format: [Type]
[Full caption + hashtags]

💼 **LinkedIn:**
[Full post copy]

📢 **Ads:**
[Ad copy + creative direction]

[Repeat for all days...]

---

### EMAIL SEQUENCE COMPLETE

[All emails with subject lines, preview text, and full body copy]

---

### SOCIAL MEDIA CONTENT CALENDAR

[Grid view of all social posts with dates, platforms, and content type]

---

### AD CREATIVES BRIEF

[All ad copy variations with targeting suggestions]

---

### CROSS-CHANNEL COORDINATION NOTES

[How channels reinforce each other, timing considerations, frequency caps]

---

### METRICS DASHBOARD

| Channel | KPI | Target | Tracking |
|---------|-----|--------|----------|
| Email | Open rate | > 25% | [Tool] |
| Email | Click rate | > 3% | [Tool] |
| Instagram | Engagement rate | > 4% | Insights |
| LinkedIn | Impressions | [Target] | Analytics |
| Ads | ROAS | > 3:1 | Ads Manager |
| Overall | Conversions | [Target] | UTM tracking |
```

## Final Ask

After delivering the sequence, ask:

"Would you like me to:
1. Expand the full copy for a specific channel's sequence?
2. Create additional ad creative variations?
3. Add another channel to the sequence?
4. Generate the visual direction for social posts?
5. Create a detailed budget allocation plan?"
