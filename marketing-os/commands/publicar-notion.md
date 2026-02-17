---
description: Publish editorial calendars, content plans, or generated content directly to your Notion workspace.
argument-hint: "<what to publish, e.g., 'editorial calendar for March' or 'content plan for product launch'>"
---

# Publish to Notion

> Requires: Notion MCP integration active. See [CONNECTORS.md](../CONNECTORS.md) for setup.

Publish marketing content, editorial calendars, and project plans directly to your Notion workspace using the Notion MCP integration.

## Trigger

This command is invoked when the user says `/publicar-notion` followed by what they want to publish, or when they ask to send content to Notion, create a Notion page, or sync with Notion.

## Inputs

Gather the following information. If any required field is missing, ask the user before proceeding:

1. **Content Type** (required) — Editorial Calendar, Content Plan, Campaign Brief, Single Post, Project Documentation
2. **Content Source** (required) — Generated content from a previous command, or new content to create
3. **Notion Destination** (optional) — Specific page, database, or workspace area
4. **Format** (optional) — Page, Database Row, Database with Template

## Publication Types

### Editorial Calendar → Notion Database

Create a Notion database with columns:
- **Date** (date) — Publication date
- **Platform** (select) — Instagram, LinkedIn, TikTok, etc.
- **Content Type** (select) — Post, Carousel, Reels, Article, etc.
- **Status** (select) — Draft, Review, Approved, Published
- **Topic** (text) — Content topic
- **Copy** (rich text) — Full post copy
- **Hashtags** (text) — Hashtags list
- **Notes** (text) — Additional notes

**MCP tools used:**
- `notion-search` — Find existing calendar database
- `notion-create-database` — Create new calendar if needed
- `notion-create-pages` — Add entries to the calendar

### Content Plan → Notion Page

Create a structured page with:
- Campaign overview
- Content pillars
- Channel strategy
- Timeline
- KPIs and targets

**MCP tools used:**
- `notion-create-pages` — Create the content plan page

### Campaign Brief → Notion Page

Create a campaign brief page with:
- Objectives
- Target audience
- Messaging framework
- Channel breakdown
- Budget allocation
- Timeline

### Single Post → Notion Database Row

Add a single content piece to an existing content database:
- All post details (copy, hashtags, visual direction)
- Status tracking
- Platform assignment

## Output Structure

```
## NOTION PUBLICATION

📱 TYPE: [Publication type]
📍 DESTINATION: [Notion workspace/page/database]
📊 STATUS: [Published / Error]

---

### CONTENT PUBLISHED

[Summary of what was published to Notion]

---

### NOTION LINKS

🔗 [Direct link to created page/database]

---

### NEXT STEPS

1. Review the content in Notion
2. Assign team members to tasks
3. Update statuses as content progresses
```

## Final Ask

After publishing to Notion, ask:

"Would you like me to:
1. Add more content entries to the same database?
2. Create a related content plan page?
3. Set up a different Notion view (calendar, board, timeline)?
4. Generate additional content to populate the calendar?"
