---
description: Capture screenshots of landing pages, social profiles, or competitor websites for analysis and reference.
argument-hint: "<URL to capture, e.g., 'https://competitor.com' or 'Instagram profile @username'>"
---

# Capture Screenshot

> Requires: Playwright MCP integration active. See [CONNECTORS.md](../CONNECTORS.md) for setup.

Capture screenshots of websites, landing pages, social profiles, and competitor content for analysis, reference, and comparison.

## Trigger

This command is invoked when the user says `/capturar-tela` followed by a URL, or when they ask to screenshot, capture, or save a visual reference of a webpage.

## Inputs

Gather the following information. If any required field is missing, ask the user before proceeding:

1. **URL** (required) — The webpage URL to capture
2. **Capture Type** (optional) — Full page, above the fold, specific section, mobile view
3. **Device** (optional) — Desktop (1920x1080), Tablet (768x1024), Mobile (375x812)
4. **Purpose** (optional) — Analysis, reference, competitive audit, design inspiration

## Capture Types

### Full Page
Captures the entire page from top to bottom, scrolling as needed.

### Above the Fold
Captures only what's visible without scrolling — the most critical section.

### Mobile View
Captures the page as it appears on a mobile device (iPhone 14 size).

### Multiple Viewports
Captures the same page across desktop, tablet, and mobile for responsive analysis.

## MCP Tools Used

| Tool | Purpose |
|------|---------|
| `browser_navigate` | Load the target URL |
| `browser_take_screenshot` | Capture the visual |
| `browser_snapshot` | Get accessibility tree for analysis |
| `browser_resize` | Set viewport for different devices |
| `browser_evaluate` | Extract specific data from the page |

## Workflow

```
1. Navigate to URL (browser_navigate)
2. Set viewport size (browser_resize) — if specific device requested
3. Wait for page load (3 seconds or specific element)
4. Take screenshot (browser_take_screenshot)
5. Optionally: Get page snapshot for text analysis (browser_snapshot)
6. Analyze the captured content
```

## Output Structure

```
## SCREENSHOT CAPTURED

🌐 URL: [URL captured]
📐 VIEWPORT: [Dimensions]
📱 DEVICE: [Desktop / Tablet / Mobile]
📅 CAPTURED: [Date and time]

---

### SCREENSHOT

[Screenshot image displayed]

---

### PAGE ANALYSIS

**Title:** [Page title]
**Type:** [Landing page / Blog / Social profile / E-commerce]

**Above the fold elements:**
- [ ] Headline visible
- [ ] CTA visible
- [ ] Value proposition clear
- [ ] Visual hierarchy effective

**Key observations:**
1. [Observation about design/layout]
2. [Observation about copy/messaging]
3. [Observation about CTA placement]

---

### COMPETITIVE INSIGHTS (if competitor)

| Element | Their Approach | Opportunity |
|---------|---------------|-------------|
| Headline | [What they do] | [What you could do better] |
| CTA | [Their CTA] | [Your improved version] |
| Social Proof | [How they use it] | [How to adapt] |
| Design | [Style notes] | [Differentiation ideas] |
```

## Final Ask

After capturing the screenshot, ask:

"Would you like me to:
1. Analyze this page's conversion elements in detail?
2. Capture the same page on mobile view?
3. Compare with another competitor's page?
4. Create a landing page inspired by this design?"
