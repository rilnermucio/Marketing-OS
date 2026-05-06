---
description: Generate optimized prompts for AI image generation tools including Midjourney, DALL-E, Flux, Ideogram, and other platforms.
argument-hint: "<description and tool, e.g., 'product photo for Flux' or 'illustration for Midjourney'>"
---

# Generate AI Image Prompt

> See [CONNECTORS.md](../CONNECTORS.md) for connected AI image generation services and integrations.

Create optimized prompts for AI image generation that produce consistent, high-quality results across different tools.

## Trigger

This command is invoked when the user says `/gerar-imagem` followed by a description and/or tool, or when they ask to create an image prompt, AI image, or visual content generation.

## Inputs

Gather the following information. If any required field is missing, ask the user before proceeding:

1. **Subject** (required) — What the image should show
2. **Purpose** (optional) — Social media, website, product, marketing, art
3. **Tool** (optional) — Midjourney, DALL-E 3, Flux, Ideogram, Leonardo, or Stable Diffusion
4. **Style** (optional) — Photorealistic, illustration, 3D, minimalist, cinematic
5. **Aspect Ratio** (optional) — 1:1, 16:9, 9:16, 4:3, or custom
6. **Mood/Atmosphere** (optional) — Professional, playful, dramatic, warm, minimal

## Tool Capabilities

### Tool Comparison

| Tool | Best For | Strengths | Aspect Ratios |
|------|----------|-----------|---------------|
| **Midjourney** | Art, concepts, stylized | Aesthetic quality, consistency | 1:1, 16:9, 9:16, 4:3 |
| **DALL-E 3** | Versatility, text in images | Text rendering, editing | 1:1, 16:9, 9:16 |
| **Flux Pro** | Photorealism, products | Detail, realism | Custom |
| **Ideogram** | Text in images, logos | Typography, branding | 1:1, 16:9, 9:16 |
| **Leonardo** | Game art, characters | Consistency, models | Custom |
| **Stable Diffusion** | Control, customization | ControlNet, LoRAs | Custom |

### Style Strengths by Tool

| Style | Best Tool | Second Choice |
|-------|-----------|---------------|
| Photorealistic | Flux Pro | DALL-E 3 |
| Illustration | Midjourney | Leonardo |
| 3D Render | Leonardo | Midjourney |
| Text/Logo | Ideogram | DALL-E 3 |
| Artistic/Abstract | Midjourney | Stable Diffusion |
| Product Photos | Flux Pro | DALL-E 3 |

## Prompt Architecture

### Universal Prompt Structure

```
[SUBJECT] + [ACTION/POSE] + [ENVIRONMENT] + [STYLE] + [LIGHTING] + [CAMERA] + [QUALITY]
```

### Component Breakdown

| Component | Purpose | Examples |
|-----------|---------|----------|
| **Subject** | Main focus | "A woman in her 30s", "A modern laptop" |
| **Action/Pose** | What subject is doing | "Looking at camera", "floating in space" |
| **Environment** | Setting/background | "In a minimalist office", "against white background" |
| **Style** | Visual aesthetic | "Photorealistic", "watercolor illustration" |
| **Lighting** | Light quality | "Soft natural light", "dramatic side lighting" |
| **Camera** | Perspective/lens | "Shot on 85mm", "wide angle", "macro" |
| **Quality** | Technical specs | "8K", "high detail", "sharp focus" |

### Midjourney-Specific Parameters

| Parameter | Effect | Values |
|-----------|--------|--------|
| `--ar` | Aspect ratio | 1:1, 16:9, 9:16, 4:3, 3:2 |
| `--v` | Version | 5, 5.1, 5.2, 6, 6.1 |
| `--style` | Style preset | raw, cute, scenic |
| `--stylize` or `--s` | Stylization | 0-1000 (default 100) |
| `--chaos` or `--c` | Variation | 0-100 |
| `--quality` or `--q` | Quality | 0.25, 0.5, 1, 2 |
| `--no` | Negative prompt | --no text, watermark |

### DALL-E 3 Optimization

```
Best practices:
- Be specific and detailed
- Describe composition explicitly
- Mention text placement if needed
- Specify style clearly
- Use natural language (less technical)
```

### Flux Pro Optimization

```
Best practices:
- Focus on photorealistic descriptions
- Include technical camera details
- Specify lighting precisely
- Use professional photography terms
- Describe materials and textures
```

## Style Keywords Library

### Photography Styles

| Style | Keywords |
|-------|----------|
| Portrait | "portrait photography, shallow depth of field, 85mm lens, soft bokeh" |
| Product | "commercial product photography, clean background, studio lighting" |
| Editorial | "editorial photography, magazine style, high fashion" |
| Documentary | "documentary style, candid, natural light, authentic" |
| Lifestyle | "lifestyle photography, warm tones, natural environment" |

### Artistic Styles

| Style | Keywords |
|-------|----------|
| Minimalist | "minimalist, clean lines, negative space, simple composition" |
| Cinematic | "cinematic, dramatic lighting, film grain, anamorphic" |
| Surreal | "surrealism, dreamlike, impossible geometry, magical realism" |
| Vintage | "vintage aesthetic, retro, film photography, nostalgic" |
| Modern | "contemporary, sleek, sophisticated, clean design" |

### Lighting Keywords

| Type | Keywords |
|------|----------|
| Natural | "golden hour, soft daylight, overcast, dappled light" |
| Studio | "softbox lighting, rim light, key light, three-point lighting" |
| Dramatic | "chiaroscuro, high contrast, moody, low key" |
| Bright | "high key, bright, airy, luminous, well-lit" |
| Neon | "neon glow, cyberpunk lighting, colored light, RGB" |

## Output Structure

Deliver the prompt in this format:

```
## AI IMAGE PROMPT

🎨 TOOL: [Midjourney / DALL-E 3 / Flux / Ideogram]
📐 ASPECT RATIO: [1:1 / 16:9 / 9:16 / custom]
🎯 PURPOSE: [Social media / Website / Product / Marketing]
✨ STYLE: [Photorealistic / Illustration / 3D / etc.]

---

### PRIMARY PROMPT

**Full Prompt:**
[Complete, optimized prompt for the selected tool]

**With Parameters (if applicable):**
[Prompt with tool-specific parameters like --ar, --v, --s]

---

### PROMPT BREAKDOWN

| Component | Content |
|-----------|---------|
| Subject | [Main subject description] |
| Action/Pose | [What subject is doing] |
| Environment | [Setting/background] |
| Style | [Visual aesthetic] |
| Lighting | [Light description] |
| Camera | [Perspective/technical] |
| Quality | [Quality modifiers] |

---

### VARIATIONS

**Variation A (Different angle/perspective):**
[Alternative prompt focusing on different composition]

**Variation B (Different style):**
[Alternative prompt with different aesthetic]

**Variation C (Different mood):**
[Alternative prompt with different atmosphere]

---

### NEGATIVE PROMPT (if applicable)

**Exclude:**
[Elements to avoid: blurry, low quality, distorted, watermark, text, etc.]

---

### TOOL-SPECIFIC TIPS

**For [Selected Tool]:**
- [Tip 1 for best results]
- [Tip 2 for best results]
- [Tip 3 for best results]

---

### ITERATION SUGGESTIONS

**If results need adjustment:**
- To make more [X]: Add "[keyword]"
- To reduce [Y]: Remove "[keyword]" or add to negative
- To change style: Replace "[current]" with "[alternative]"

---

### RECOMMENDED SETTINGS

| Setting | Value | Reason |
|---------|-------|--------|
| [Parameter 1] | [Value] | [Why this works] |
| [Parameter 2] | [Value] | [Why this works] |
| [Parameter 3] | [Value] | [Why this works] |
```

## Final Ask

After delivering the prompt, ask:

"Would you like me to:
1. Create variations for different styles or moods?
2. Optimize this prompt for a different AI tool?
3. Generate prompts for a complete visual series?
4. Add specific elements or adjust the composition?"
