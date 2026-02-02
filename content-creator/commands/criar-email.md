---
description: Create email marketing content including single emails, complete sequences, newsletters, and automated flows with subject lines and preview text.
argument-hint: "<type and purpose, e.g., 'welcome sequence for SaaS' or 'launch email for course'>"
---

# Create Email Marketing

> See [CONNECTORS.md](../CONNECTORS.md) for connected services that can provide subscriber data and email platform integrations.

Create complete email marketing content optimized for opens, clicks, and conversions.

## Trigger

This command is invoked when the user says `/criar-email` followed by a type and purpose, or when they ask to create an email, newsletter, or email sequence.

## Inputs

Gather the following information. If any required field is missing, ask the user before proceeding:

1. **Type** (required) — Single email, welcome sequence, nurture sequence, launch sequence, abandoned cart, re-engagement, or newsletter
2. **Purpose/Goal** (required) — What the email should achieve
3. **Audience** (required) — Who is receiving this email
4. **Product/Offer** (optional) — What you're promoting (if applicable)
5. **Tone** (optional) — Friendly, professional, urgent, casual, or inspirational
6. **CTA** (optional) — Desired action from the reader
7. **Sequence length** (optional) — Number of emails if sequence

## Email Types and Structures

### Single Email

For one-off emails (announcements, promotions, updates):

```
SUBJECT LINE — Hook that earns the open
PREVIEW TEXT — Complements and extends the subject
OPENING — Hook that keeps them reading
BODY — Value delivery or story
CTA — Clear single action
PS — Secondary hook or urgency (optional)
```

### Welcome Sequence (3-5 emails)

**Email 1 (Immediate): The Welcome**
- Deliver promised lead magnet
- Set expectations for future emails
- Quick win or immediate value
- CTA: Reply or small engagement action

**Email 2 (Day 1-2): The Story**
- Share your/brand story
- Build connection and relatability
- Show the transformation journey
- CTA: Consume content

**Email 3 (Day 3-4): The Value**
- Best piece of content
- Actionable tip they can use today
- Demonstrate expertise
- CTA: Try the tip

**Email 4 (Day 5-6): Social Proof**
- Case study or testimonial
- Results others have achieved
- "You can do this too" message
- CTA: Learn about offer

**Email 5 (Day 7): The Offer**
- Introduce product/service
- Benefits over features
- Overcome main objection
- CTA: Purchase/sign up

### Launch Sequence (7-10 emails)

**Pre-Launch Phase:**
- Email 1: Tease announcement
- Email 2: Behind-the-scenes/story
- Email 3: Waitlist/early access

**Launch Phase:**
- Email 4: Doors open + main benefits
- Email 5: Full details + FAQ
- Email 6: Case study/testimonial
- Email 7: Overcome objection #1
- Email 8: Overcome objection #2
- Email 9: Bonus announcement
- Email 10: Final hours + doors closing

### Abandoned Cart (3 emails)

**Email 1 (1 hour): Gentle Reminder**
- "Did you forget something?"
- Show cart items
- Simple return CTA
- No discount

**Email 2 (24 hours): Address Objections**
- Social proof (reviews)
- Answer common questions
- Hint at urgency
- CTA: Complete purchase

**Email 3 (72 hours): Last Chance + Incentive**
- Discount or free shipping
- Final urgency
- Scarcity message
- Strong CTA

### Newsletter

```
HEADER — Branding, date
INTRO — Personal touch, brief update
MAIN CONTENT — Primary value (1-3 items)
SECONDARY — Additional resources or curated content
CTA — Primary action
FOOTER — Social links, unsubscribe
```

## Subject Line Framework

### Subject Line Formulas

| Formula | Template | Example |
|---------|----------|---------|
| Curiosity | "This changed everything..." | "This changed everything about my mornings..." |
| Benefit | "[Result] in [Timeframe]" | "Double your leads in 30 days" |
| Question | "Are you [pain point]?" | "Are you making this mistake?" |
| Urgency | "[Time limit]: [Offer]" | "24 hours left: 50% off" |
| Personal | "[Name], [personal hook]" | "[Name], quick question" |
| Number | "[X] ways to [result]" | "5 ways to write better emails" |
| FOMO | "Everyone's talking about..." | "Everyone's talking about this trick" |

### Subject Line Best Practices

- Length: 30-50 characters (mobile-friendly)
- Use personalization when available
- Max 1 emoji, only if brand-appropriate
- Test lowercase vs. title case
- Avoid spam trigger words
- Create urgency without being clickbait

### Preview Text Strategy

Preview text should:
- Complement, not repeat the subject
- Add curiosity or context
- Be under 90 characters
- Never be left empty (shows "View in browser")

**Formula:**
```
Subject: [Hook]
Preview: [Expansion or payoff of hook]

Example:
Subject: "You're leaving money on the table"
Preview: "Here's the 5-minute fix (no fancy tools needed)"
```

## Email Body Framework

### Opening Hooks

| Type | Example |
|------|---------|
| Question | "What would you do with 10 extra hours per week?" |
| Bold statement | "Everything you've been told about [topic] is wrong." |
| Personal | "I've been thinking about you and wanted to share..." |
| Story | "Last Tuesday, something unexpected happened..." |
| Data | "73% of [audience] struggle with this. Are you one?" |
| Direct | "I'm going to show you exactly how to [result]." |

### Body Structure (PAS)

```
PROBLEM
[Identify the pain point. Make them feel understood.]

AGITATE
[Expand on consequences. Build emotional urgency.]

SOLUTION
[Present your answer. Show the transformation.]

CTA
[Clear, single call to action.]
```

### Body Structure (AIDA)

```
ATTENTION
[Hook that stops them from deleting.]

INTEREST
[Relevant details that engage.]

DESIRE
[Paint the outcome. Benefits, proof.]

ACTION
[Clear CTA with reason to act now.]
```

### CTA Best Practices

| Weak | Strong |
|------|--------|
| Submit | Get My Free Guide |
| Click Here | Start My Free Trial |
| Learn More | Show Me How |
| Buy Now | Get Instant Access |
| Download | Send Me the Checklist |

**CTA guidelines:**
- One primary CTA per email
- Use action verbs
- Make it benefit-driven
- Place 2-3 times in longer emails
- Button + text link for accessibility

### PS Strategy

Use PS for:
- Repeat CTA differently
- Add urgency/scarcity
- Include bonus or incentive
- Personal note
- Address common objection

## Output Structure

Deliver the email in this format:

```
## EMAIL

📧 TYPE: [Welcome / Launch / Newsletter / etc.]
📍 SEQUENCE POSITION: [Email X of Y] (if applicable)
🎯 GOAL: [What this email should achieve]
⏰ SEND TIMING: [Recommended day/time]

---

### SUBJECT LINE OPTIONS

**Primary (Recommended):**
"[Subject line]"

**Variation A (Curiosity):**
"[Subject line]"

**Variation B (Benefit):**
"[Subject line]"

---

### PREVIEW TEXT

"[Preview text that complements subject]"

---

### EMAIL BODY

---

[Greeting]

**[Opening hook paragraph]**

[Body content following structure]

[Transition to CTA]

**[CTA Button/Link]**
[CTA text]

[Closing]

[Signature]

**P.S.** [Secondary hook or urgency]

---

---

### NOTES

- **Goal:** [What we want reader to do/feel]
- **Key objection addressed:** [If applicable]
- **Next email preview:** [For sequences]

---

### A/B TEST SUGGESTIONS

| Element | Version A | Version B |
|---------|-----------|-----------|
| Subject | [Option 1] | [Option 2] |
| CTA | [Option 1] | [Option 2] |

---

### SEQUENCE OVERVIEW (if applicable)

| Email | Timing | Subject | Goal |
|-------|--------|---------|------|
| 1 | Day 0 | [Subject] | [Goal] |
| 2 | Day 1 | [Subject] | [Goal] |
| 3 | Day 3 | [Subject] | [Goal] |
```

## Final Ask

After delivering the email, ask:

"Would you like me to:
1. Create the full sequence with all emails written out?
2. Generate more subject line variations for A/B testing?
3. Adapt the tone or length for a different audience?
4. Create a re-engagement sequence for non-openers?"
