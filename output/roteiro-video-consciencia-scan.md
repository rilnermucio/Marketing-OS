# Roteiro de Produção - Vídeo "Escaneamento de Consciência" (PT-BR)

Documento refeito com fluxo de agentes do **Marketing OS**.

## Agentes usados (Marketing OS)
- `Video Agent`: estrutura de retenção, timing e roteiro por cena.
- `AI Tools Agent`: prompts de geração para vídeo e áudio.
- `Design Agent`: padronização visual (CRT/glitch) e consistência técnica.
- `Copy Agent`: adaptação da copy para PT-BR mantendo o impacto do original.

## Especificação travada (igual ao original)
- Formato: `1080x1920` (9:16)
- FPS: `30`
- Duração total: `25.4s`
- Estética: CRT/VHS, scanlines, RGB split, black background, texto branco glow
- Ritmo: cortes rápidos + glitches + micro pausas de impacto

## Prompt mestre (usar em todas as cenas)
```text
Vertical 9:16 retro CRT monitor in complete darkness, deep black background,
white bold condensed sans-serif text, subtle glow bloom, horizontal scanlines,
chromatic aberration RGB split, analog VHS noise, fisheye tube distortion,
intermittent glitch artifacts, high contrast, ominous cyberpunk mood,
cinematic grain, rapid hard cuts, no people, no UI, no watermark.
```

## Prompt negativo (usar em todas)
```text
no modern clean UI, no colorful gradients, no realistic faces, no extra objects,
no logo watermark, no subtitles bar, no pastel palette, no cartoon style.
```

## Timeline final (texto em português)

| Tempo | Texto on-screen (ALL CAPS) | Narração (opcional) |
|---|---|---|
| 0.00-1.10 | AGUARDE | Aguarde. |
| 1.10-2.40 | ISSO VAI LEVAR APENAS | Isso vai levar apenas |
| 2.40-3.80 | 1.28 SEGUNDOS | um vírgula vinte e oito segundos. |
| 3.80-5.20 | SUA CONSCIÊNCIA FOI ESCANEADA. | Sua consciência foi escaneada. |
| 5.20-6.40 | PROCESSANDO... | Processando... |
| 6.40-7.40 | OS RESULTADOS SÃO... | Os resultados são... |
| 7.40-8.60 | PREOCUPANTES. | preocupantes. |
| 8.60-10.20 | POR QUE VOCÊ CONTINUA | Por que você continua |
| 10.20-12.20 | RESTRINGINDO SEU PRÓPRIO POTENCIAL | restringindo seu próprio potencial |
| 12.20-14.20 | PELO CONFORTO DOS OUTROS? | pelo conforto dos outros? |
| 14.20-15.80 | POR QUE VOCÊ INSISTE | Por que você insiste |
| 15.80-17.40 | QUE SEU TEMPO VALE SER GASTO | que seu tempo vale ser gasto |
| 17.40-21.30 | CONSUMINDO MÍDIA QUE CORROMPE E APODRECE SUA CAPACIDADE DE FOCO? | consumindo mídia que corrompe e apodrece sua capacidade de foco? |
| 21.30-23.30 | MAS ISSO NÃO É NOVIDADE PRA VOCÊ. | Mas isso não é novidade pra você. |
| 23.30-24.70 | VOCÊ JÁ SABE DISSO. | Você já sabe disso. |
| 24.70-25.40 | SÍMBOLO FINAL (OLHO/LOGO) | (sem fala, apenas impacto sonoro) |

## Cenas e prompts prontos

### Cena 1 - Hook de carregamento (0.00-3.80)
**Prompt de vídeo**
```text
[MASTER PROMPT]
Sequence of text appearing in hard glitch cuts:
"AGUARDE" -> "ISSO VAI LEVAR APENAS" -> "1.28 SEGUNDOS".
Counter feeling and escalating tension. Bright scanline flash before next scene.
```
**SFX**: buzz CRT + beeps curtos crescendo + flash hit.

### Cena 2 - Diagnóstico (3.80-8.60)
**Prompt de vídeo**
```text
[MASTER PROMPT]
Diagnostic terminal pacing with short text bursts:
"SUA CONSCIÊNCIA FOI ESCANEADA." -> "PROCESSANDO..." ->
"OS RESULTADOS SÃO..." -> "PREOCUPANTES.".
Include micro screen shake on "PREOCUPANTES.".
```
**SFX**: hum grave + glitches secos + bass impact em "PREOCUPANTES.".

### Cena 3 - Confronto 1 (8.60-14.20)
**Prompt de vídeo**
```text
[MASTER PROMPT]
Confrontational typography sequence with rapid cuts:
"POR QUE VOCÊ CONTINUA" ->
"RESTRINGINDO SEU PRÓPRIO POTENCIAL" ->
"PELO CONFORTO DOS OUTROS?".
Hold each phrase briefly, add subtle jitter and RGB channel drift.
```
**SFX**: drone tenso + hits eletrônicos por frase.

### Cena 4 - Confronto 2 (14.20-21.30)
**Prompt de vídeo**
```text
[MASTER PROMPT]
Aggressive escalation with denser text and stronger distortion:
"POR QUE VOCÊ INSISTE" ->
"QUE SEU TEMPO VALE SER GASTO" ->
"CONSUMINDO MÍDIA QUE CORROMPE E APODRECE SUA CAPACIDADE DE FOCO?".
Increase scanline distortion and static toward the end.
```
**SFX**: bass pulsante + estática crescente + corte seco no final.

### Cena 5 - Fechamento psicológico (21.30-24.70)
**Prompt de vídeo**
```text
[MASTER PROMPT]
Slow, controlled delivery with slight flicker:
"MAS ISSO NÃO É NOVIDADE PRA VOCÊ." ->
"VOCÊ JÁ SABE DISSO.".
Lower motion, higher tension, lingering glow.
```
**SFX**: quase silêncio + low rumble + um hit suave antes da cena final.

### Cena 6 - Assinatura final (24.70-25.40)
**Prompt de vídeo**
```text
[MASTER PROMPT]
Black screen with minimalist white eye symbol centered.
Quick glitch-in, hold, abrupt cut to black.
```
**SFX**: pulse único/heartbeat + tail curto de estática.

## Workflow recomendado (produção)
1. Gerar 6 clipes (um por cena) com durações travadas.
2. Se a IA errar tipografia, gerar sem texto e aplicar texto na edição.
3. Montar no CapCut/Resolve com cortes secos exatamente nos tempos da tabela.
4. Aplicar bus de áudio único (hum + glitches + hits) para continuidade.

## Preset de texto para pós (caso necessário)
- Fonte: sans-serif condensada bold (caixa alta)
- Cor: `#FFFFFF`
- Glow: leve (5-10%)
- Aberração cromática: 1-2 px RGB split
- Tracking: levemente fechado
- Posição: centro ou centro-inferior

## QA final antes de publicar
- Texto legível em tela pequena (mobile).
- Nenhum frame colorido fora da estética preto/branco.
- Picos de áudio sem clipar (`-1 dBTP` máx).
- Duração final entre `25.3s` e `25.5s`.
- CTA na legenda (não no vídeo): `Comente ALTERD para desbloquear.`

