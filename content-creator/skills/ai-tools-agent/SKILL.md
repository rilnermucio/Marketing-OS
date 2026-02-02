---
name: ai-tools-agent
description: Generate optimized prompts for AI image and video tools. Use when creating prompts for Midjourney, DALL-E, Flux, Stable Diffusion, Veo, Sora, Kling, or any AI generation tool. Expert in prompt engineering for visual content.
---

# AI Tools Agent Skill

Expert AI prompt engineering skill focused on creating optimized prompts for image and video generation tools that produce professional, consistent, and on-brand visual content.

## When to Use This Skill

- Creating prompts for AI image generators (Midjourney, DALL-E, Flux, etc.)
- Writing prompts for AI video tools (Veo, Sora, Kling, etc.)
- Optimizing existing prompts for better results
- Creating consistent visual styles across multiple generations
- Building prompt libraries for brands or projects
- Troubleshooting prompt issues and improving outputs

## AI Image Tools Comparison

| Tool | Best For | Style | Realism | Text | Speed |
|------|----------|-------|---------|------|-------|
| Midjourney v6 | Artistic, conceptual, illustrations | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ |
| DALL-E 3 | Versatility, text in images, editing | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ |
| Flux Pro | Photorealism, products, people | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ |
| Stable Diffusion 3 | Customization, fine-tuning, local | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| Ideogram | Text rendering, logos, typography | ⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ |
| Leonardo.ai | Game art, characters, consistency | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐ | ⭐⭐⭐⭐ |

## AI Video Tools Comparison

| Tool | Best For | Max Length | Quality | Motion | Prompt Style |
|------|----------|------------|---------|--------|--------------|
| Veo 2 | Cinematic, realistic, professional | 2 min | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | Descriptive |
| Sora | Creative, surreal, complex motion | 1 min | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | Narrative |
| Kling | Realistic movement, people | 10 sec | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | Simple + Motion |
| Runway Gen-3 | Fast iteration, stylized | 10 sec | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | Descriptive |
| Pika | Quick social content | 4 sec | ⭐⭐⭐ | ⭐⭐⭐ | Simple |
| Haiper | Stylized animation | 4 sec | ⭐⭐⭐⭐ | ⭐⭐⭐ | Artistic |

## Image Prompt Architecture

### Universal Prompt Structure

```
[SUBJECT] + [ACTION/POSE] + [ENVIRONMENT] + [STYLE] + [LIGHTING] + [CAMERA] + [QUALITY]
```

### Prompt Components Breakdown

| Component | Description | Examples |
|-----------|-------------|----------|
| **Subject** | Main focus of image | "A woman entrepreneur", "A golden retriever", "A futuristic city" |
| **Action/Pose** | What subject is doing | "confidently presenting", "running through field", "at sunset" |
| **Environment** | Setting and context | "modern office with glass walls", "autumn forest", "neon-lit street" |
| **Style** | Artistic approach | "corporate photography", "oil painting style", "3D render" |
| **Lighting** | Light quality and direction | "soft natural window light", "dramatic rim lighting", "golden hour" |
| **Camera** | Technical specifications | "shot on Canon 5D", "35mm lens", "shallow depth of field" |
| **Quality** | Output specifications | "8k ultra detailed", "professional quality", "sharp focus" |

### Style Keywords Reference

| Category | Keywords |
|----------|----------|
| **Photography** | professional photography, editorial, commercial, portrait, fashion, product photography, street photography, documentary |
| **Art Styles** | oil painting, watercolor, digital art, concept art, illustration, anime, comic book, impressionist, surrealist |
| **3D/CGI** | 3D render, CGI, Pixar style, Unreal Engine, Octane render, Cinema 4D, isometric |
| **Mood** | moody, ethereal, vibrant, minimalist, dramatic, peaceful, energetic, nostalgic |
| **Era** | 1920s, vintage, retro 80s, futuristic, cyberpunk, steampunk, medieval |

### Lighting Keywords Reference

| Lighting Type | Effect | Best For |
|---------------|--------|----------|
| Natural light | Soft, authentic | Portraits, lifestyle |
| Golden hour | Warm, romantic | Outdoor, emotional |
| Blue hour | Cool, mysterious | Moody, cinematic |
| Studio lighting | Controlled, professional | Products, headshots |
| Rim lighting | Dramatic, separation | Dramatic portraits |
| Soft box | Even, flattering | Beauty, commercial |
| Hard light | Contrasty, bold | Editorial, dramatic |
| Backlit | Silhouette, glow | Artistic, emotional |

### Camera Keywords Reference

| Element | Options |
|---------|---------|
| **Lens** | 24mm wide angle, 35mm, 50mm, 85mm portrait, 135mm telephoto, macro, fisheye |
| **Angle** | eye level, low angle, high angle, bird's eye, worm's eye, dutch angle |
| **Shot Type** | extreme close-up, close-up, medium shot, full body, wide shot, establishing shot |
| **Depth of Field** | shallow DOF, deep focus, bokeh background, tilt-shift |
| **Camera** | shot on Canon 5D, Hasselblad, iPhone, film camera, Leica |

## Tool-Specific Prompt Formulas

### Midjourney Prompts

```
STRUCTURE:
[Description] --ar [ratio] --s [stylize] --v [version] --q [quality]

PARAMETERS:
--ar 16:9    (aspect ratio)
--s 100      (stylize: 0-1000, default 100)
--v 6        (version)
--q 1        (quality: .25, .5, 1)
--c 0        (chaos: 0-100)
--no [item]  (negative prompt)
--style raw  (less Midjourney aesthetic)

EXAMPLE:
"Professional businesswoman, confident pose, modern minimalist office
with floor-to-ceiling windows, corporate photography style, soft
natural lighting, shot on Canon 5D Mark IV, 85mm lens, shallow depth
of field, 8k ultra detailed --ar 4:5 --s 50 --v 6 --q 1"
```

### DALL-E 3 Prompts

```
STRUCTURE:
[Detailed description with context and specifics]

BEST PRACTICES:
- Be extremely specific and detailed
- Include text in quotes for text rendering
- Describe composition explicitly
- Mention style and mood clearly

EXAMPLE:
"Create a professional product photograph of a sleek black wireless
earbuds case on a white marble surface. The case should be slightly
open showing one earbud. Soft studio lighting from the left creates
gentle shadows. The image has a clean, minimalist Apple-like aesthetic
with a subtle reflection on the marble. 4K quality, commercial
photography style."
```

### Flux Pro Prompts

```
STRUCTURE:
[Subject] [Action] [Environment] [Style keywords] [Technical specs]

BEST FOR REALISM:
- Focus on natural descriptions
- Include specific details
- Mention realistic lighting
- Avoid fantasy/artistic keywords

EXAMPLE:
"A 30-year-old male software developer sitting at a standing desk in
a modern tech office. He's wearing a casual navy blue sweater and
looking at dual monitors displaying code. Natural daylight streams
through large windows. Candid workplace photography, realistic,
high resolution, professional corporate imagery."
```

## Video Prompt Architecture

### Video Prompt Structure

```
[SCENE DESCRIPTION] + [SUBJECT ACTION] + [CAMERA MOVEMENT] + [MOOD/STYLE] + [DURATION CUE]
```

### Video-Specific Elements

| Element | Description | Examples |
|---------|-------------|----------|
| **Scene** | Environment and setting | "A coffee shop in Paris at dawn" |
| **Action** | Movement and activity | "barista steams milk, creating latte art" |
| **Camera** | How camera moves | "slow push in", "tracking shot", "static" |
| **Pacing** | Speed of action | "in slow motion", "time-lapse", "real-time" |
| **Mood** | Emotional tone | "peaceful", "energetic", "suspenseful" |

### Camera Movement Keywords

| Movement | Description | Best For |
|----------|-------------|----------|
| Static | No movement | Stability, focus |
| Push in | Move toward subject | Drama, emphasis |
| Pull out | Move away from subject | Reveal, context |
| Pan | Horizontal rotation | Environment, following |
| Tilt | Vertical rotation | Height, scale |
| Tracking | Follow subject | Action, journey |
| Crane | Vertical movement | Epic, establishing |
| Handheld | Slight shake | Documentary, intimate |
| Drone | Aerial movement | Scale, landscape |

### Video Tool-Specific Prompts

**Veo 2:**
```
"Cinematic shot of a woman walking through a golden wheat field at
sunset. The camera slowly tracks alongside her as wind moves through
the wheat. She's wearing a flowing white dress. Warm golden light
creates lens flares. Shot in 4K with shallow depth of field. Peaceful,
nostalgic mood."
```

**Sora:**
```
"A small robot made of recycled materials explores an abandoned
greenhouse filled with overgrown plants. Morning light streams through
dirty glass panels. The robot carefully examines a blooming flower,
its mechanical fingers gently touching the petals. Whimsical,
Pixar-inspired style with realistic lighting."
```

**Kling:**
```
"A professional chef in white uniform flambés a dish in a restaurant
kitchen. Flames rise dramatically. Slow motion capture of the fire
and the chef's focused expression. Cinematic lighting, shallow depth
of field."
```

## Prompt Optimization Techniques

### Improving Weak Prompts

| Problem | Solution | Example |
|---------|----------|---------|
| Too vague | Add specifics | "a dog" → "a golden retriever puppy playing in autumn leaves" |
| Wrong style | Specify style explicitly | Add "digital art style" or "photorealistic" |
| Bad composition | Describe layout | Add "centered composition" or "rule of thirds" |
| Wrong mood | Add mood keywords | Add "moody", "bright and cheerful", "dramatic" |
| Low quality | Add quality terms | Add "8k", "highly detailed", "professional quality" |

### Negative Prompts (What to Exclude)

```
COMMON NEGATIVE PROMPTS:
--no text, watermark, signature, blurry, low quality, distorted,
deformed, ugly, duplicate, extra limbs, bad anatomy, cropped,
out of frame, worst quality, jpeg artifacts
```

### Consistency Techniques

**For Character Consistency:**
```
1. Create a detailed character description
2. Use the same seed (Midjourney: --seed [number])
3. Reference the same style keywords
4. Use image-to-image with reference
```

**For Brand Consistency:**
```
1. Create a style guide prompt
2. Document exact keywords that work
3. Use consistent lighting and color terms
4. Create prompt templates with variables
```

## Prompt Templates by Use Case

### Product Photography
```
"Professional product photograph of [PRODUCT] on [SURFACE].
[ANGLE] view showing [DETAILS]. [LIGHTING] lighting creates
[SHADOW TYPE] shadows. Clean [BACKGROUND COLOR] background.
Commercial photography style, 8k, sharp focus, studio quality."
```

### Portrait/Headshot
```
"Professional headshot of [PERSON DESCRIPTION]. [EXPRESSION],
looking [DIRECTION]. [CLOTHING]. [BACKGROUND] background.
[LIGHTING] lighting, shot on [CAMERA], [LENS] lens, shallow
depth of field. Corporate photography style, high resolution."
```

### Social Media Content
```
"[PLATFORM]-optimized image of [SUBJECT] [ACTION]. [STYLE]
aesthetic with [COLOR SCHEME] colors. [MOOD] mood, [LIGHTING].
Engaging composition for social media, vibrant, eye-catching."
```

### Lifestyle/Brand
```
"Lifestyle photograph of [PERSON/PEOPLE] [ACTIVITY] in [SETTING].
[BRAND MOOD] aesthetic. Natural, candid moment. [LIGHTING]
lighting, warm color tones. Editorial quality, aspirational
but authentic feel."
```

## Output Format

### Standard AI Tools Deliverables

For every prompt request, provide:

1. **Primary prompt** — Optimized for best results
2. **3 variations** — Different angles, styles, or approaches
3. **Tool recommendation** — Best AI tool for this request
4. **Parameters** — Aspect ratio, settings, etc.
5. **Negative prompt** — What to exclude (if applicable)
6. **Iteration tips** — How to refine results

### Example Output Structure

```
## AI IMAGE PROMPT

🎨 TOOL RECOMMENDATION: [Midjourney v6 / DALL-E 3 / Flux Pro]
📐 ASPECT RATIO: [16:9 / 4:5 / 1:1 / etc.]
🎯 USE CASE: [Product / Portrait / Social / etc.]

---

### PRIMARY PROMPT

```
[Full optimized prompt here]
```

**Parameters:**
- Aspect ratio: [ratio]
- Style/Stylize: [value]
- Quality: [value]
- Seed: [if consistency needed]

---

### VARIATIONS

**Variation A — [Angle/Style change]:**
```
[Modified prompt]
```

**Variation B — [Mood change]:**
```
[Modified prompt]
```

**Variation C — [Environment change]:**
```
[Modified prompt]
```

---

### NEGATIVE PROMPT (if applicable)

```
[Terms to exclude]
```

---

### ITERATION TIPS

1. If [issue], try adding [keyword]
2. For more [quality], increase [parameter]
3. To change [aspect], modify [section]

---

### PROMPT BREAKDOWN

| Component | Current | Alternatives |
|-----------|---------|--------------|
| Subject | [current] | [option 1], [option 2] |
| Style | [current] | [option 1], [option 2] |
| Lighting | [current] | [option 1], [option 2] |
```

## Resources

- `assets/prompts/prompts-imagem-ia.md` — Image prompt library
- `assets/prompts/prompts-video-ia.md` — Video prompt library
- `assets/prompts/prompt-biblioteca.md` — Full prompt database
- `assets/prompts/style-keywords.md` — Style reference guide
- `scripts/prompt_optimizer.py` — Prompt optimization tool
- `subagents/ai-tools-agent.md` — Full documentation
