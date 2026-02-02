---
description: Create a complete SEO-optimized article with keyword strategy, meta tags, structured headings, and internal linking suggestions.
argument-hint: "<topic and keyword, e.g., 'article about content marketing targeting 'content marketing strategy''>"
---

# Create SEO Article

> See [CONNECTORS.md](../CONNECTORS.md) for connected services that can provide keyword data and existing content for internal linking.

Create a complete, SEO-optimized article designed to rank on Google and drive organic traffic.

## Trigger

This command is invoked when the user says `/criar-artigo` followed by a topic, or when they ask to create a blog post, article, or SEO content.

## Inputs

Gather the following information. If any required field is missing, ask the user before proceeding:

1. **Topic** (required) — Main subject of the article
2. **Primary keyword** (required) — Main term to rank for
3. **Search intent** (required) — Informational, commercial, or transactional
4. **Target word count** (optional) — Default 1,500-2,500 for informational
5. **Audience** (optional) — Who is searching for this
6. **Secondary keywords** (optional) — Related terms to include
7. **Competitor URLs** (optional) — Top-ranking articles to outperform

## Keyword Strategy

### Keyword Mapping

Create a complete keyword map:

| Type | Keywords | Placement |
|------|----------|-----------|
| Primary | [Main keyword] | Title, H1, URL, first 100 words, meta |
| Secondary | [2-3 related terms] | H2 headings, body copy |
| Long-tail | [3-5 specific phrases] | H3 headings, FAQ section |
| LSI | [Semantically related] | Natural inclusion throughout |

### Search Intent Analysis

Determine content approach based on intent:

**Informational** (how-to, what is, guide):
- Comprehensive coverage
- Step-by-step instructions
- Examples and visuals
- 1,500-3,000 words

**Commercial** (best, top, comparison, review):
- Comparison tables
- Pros/cons lists
- Clear recommendations
- 2,000-4,000 words

**Transactional** (buy, pricing, discount):
- Clear value proposition
- Pricing information
- Strong CTAs
- 500-1,500 words

## Article Structure

### Title Tag Formula

```
[Primary Keyword]: [Benefit/Modifier] | [Brand]
```

**Requirements:**
- 50-60 characters
- Primary keyword near beginning
- Compelling enough to earn clicks
- Unique from other pages

**Generate 3-5 options:**
1. How-to format: "How to [Achieve X]: Complete Guide for [Year]"
2. Number format: "[X] [Topic] Strategies That Work in [Year]"
3. Question format: "What is [Topic]? Everything You Need to Know"
4. Benefit format: "[Topic]: [Specific Benefit] in [Timeframe]"

### Meta Description Formula

```
[Hook/Problem] + [Solution/Value] + [CTA or Benefit]
```

**Requirements:**
- 150-160 characters
- Include primary keyword
- Compelling value proposition
- Implicit or explicit CTA

### URL Structure

```
/[primary-keyword]
or
/[category]/[primary-keyword]
```

**Requirements:**
- Short and descriptive
- Primary keyword included
- Hyphens between words
- Lowercase only
- No parameters or dates

### Heading Structure

```
H1: [Primary Keyword] + [Benefit/Context]

H2: What is [Topic]?
    H3: [Definition aspect 1]
    H3: [Definition aspect 2]

H2: Why [Topic] Matters / Benefits of [Topic]
    H3: [Benefit 1]
    H3: [Benefit 2]
    H3: [Benefit 3]

H2: How to [Main Process/Strategy]
    H3: Step 1: [Action]
    H3: Step 2: [Action]
    H3: Step 3: [Action]

H2: [Secondary Keyword Topic]
    H3: [Subtopic]
    H3: [Subtopic]

H2: Common [Topic] Mistakes to Avoid
    H3: [Mistake 1]
    H3: [Mistake 2]

H2: [Topic] Tools/Resources/Examples
    H3: [Tool/Resource 1]
    H3: [Tool/Resource 2]

H2: Frequently Asked Questions
    H3: [Question 1]?
    H3: [Question 2]?
    H3: [Question 3]?

H2: Conclusion / Key Takeaways
```

## Content Guidelines

### Introduction (150-200 words)

```
[Hook — question, stat, or bold statement]

[Problem/context — why this matters to the reader]

[Promise — what they'll learn by reading]

[Credibility — why you/this content is trustworthy]

[Roadmap — brief overview of what's covered]
```

**Requirements:**
- Primary keyword in first 100 words
- Clear value proposition
- Engage the reader immediately

### Body Sections

For each H2 section:
- Start with context (why this matters)
- Provide actionable information
- Include examples or data
- Use bullet points and numbered lists
- Add visual descriptions or image suggestions
- Link to relevant internal/external resources

**Content density:**
- 200-400 words per H2 section
- Break long paragraphs (max 3-4 sentences)
- Use transition sentences between sections

### E-E-A-T Integration

Demonstrate expertise, experience, authoritativeness, and trust:

| Factor | How to Demonstrate |
|--------|-------------------|
| Experience | First-hand examples, case studies, "I did X" |
| Expertise | Technical accuracy, depth of knowledge |
| Authoritativeness | Citations, data, expert quotes |
| Trust | Sources cited, accurate info, clear policies |

### Featured Snippet Optimization

Structure content to win featured snippets:

**For paragraph snippets:**
```
H2: What is [Topic]?

[Topic] is [40-60 word definition that directly answers the question].
[Additional context follows...]
```

**For list snippets:**
```
H2: How to [Do Something]

Follow these steps to [achieve result]:

1. **[Step one]** — Brief description
2. **[Step two]** — Brief description
3. **[Step three]** — Brief description
```

**For table snippets:**
```
H2: [Comparison Topic]

| [Column 1] | [Column 2] | [Column 3] |
|------------|------------|------------|
| [Data] | [Data] | [Data] |
```

### Conclusion (150-200 words)

```
[Summary — key points revisited]

[Main takeaway — the one thing to remember]

[CTA — next step for the reader]

[Question — spark engagement/comments]
```

## Output Structure

Deliver the article in this format:

```
## SEO ARTICLE

📝 TOPIC: [Topic]
🔑 PRIMARY KEYWORD: [Keyword]
🎯 SEARCH INTENT: [Intent type]
📊 TARGET LENGTH: [Word count]

---

### KEYWORD MAP

| Type | Keyword | Monthly Volume | Difficulty |
|------|---------|----------------|------------|
| Primary | [keyword] | [est. volume] | [est. difficulty] |
| Secondary | [keyword] | [est. volume] | [est. difficulty] |
| Long-tail | [keyword] | [est. volume] | [est. difficulty] |

---

### META TAGS

**Title Tag (X characters):**
[Title]

**Meta Description (X characters):**
[Description]

**URL Slug:**
/[slug]

---

### ARTICLE OUTLINE

[Complete heading structure with H1, H2, H3]

---

### FULL ARTICLE

[Complete article with all sections]

---

### SEO CHECKLIST

- [ ] Primary keyword in title (near beginning)
- [ ] Primary keyword in H1
- [ ] Primary keyword in URL
- [ ] Primary keyword in first 100 words
- [ ] Meta description written (150-160 chars)
- [ ] Secondary keywords in H2s
- [ ] Images have alt text (suggest descriptions)
- [ ] Internal links added (suggest 2-5)
- [ ] External links to authoritative sources (1-3)
- [ ] Content length appropriate
- [ ] Headings follow logical hierarchy
- [ ] Mobile-friendly formatting

---

### INTERNAL LINKING SUGGESTIONS

| Anchor Text | Target Page Topic |
|-------------|-------------------|
| [anchor] | [page topic/URL if known] |
| [anchor] | [page topic/URL if known] |

---

### IMAGE SUGGESTIONS

| Placement | Description | Alt Text |
|-----------|-------------|----------|
| [After H2 X] | [Image description] | [Alt text with keyword] |
| [After H2 Y] | [Image description] | [Alt text] |

---

### FAQ SCHEMA

[Formatted FAQ section ready for schema markup]
```

## Final Ask

After delivering the article, ask:

"Would you like me to:
1. Expand any section with more detail or examples?
2. Generate additional title/meta variations for A/B testing?
3. Create a content brief for images or graphics?
4. Suggest a content cluster strategy around this topic?"
