---
description: Cria roteiro completo de vídeo com hook, estrutura, direções visuais e conceito de thumbnail para YouTube, Reels, TikTok, Shorts ou VSL. Ativa o Video Agent completo com ciência de retenção, clones de voz e regras de qualidade do Marketing OS.
argument-hint: "<formato e tema, ex: 'Reels 90s viral sobre produtividade' ou 'YouTube tutorial email marketing'>"
---

# Criar Vídeo — Video Agent Completo

> Este comando ativa o **Video Agent** completo do Marketing OS (`../subagents/video-agent.md`) com todos os seus frameworks de retenção, clones de voz e regras de qualidade. NÃO execute por conta própria — siga o protocolo abaixo.

## Delegação ao Video Agent

Ao receber este comando, você DEVE:

1. Carregar e seguir `../subagents/video-agent.md` como seu guia principal
2. Aplicar as **Regras de Qualidade do Marketing OS** (seção abaixo)
3. Selecionar o **clone de voz** conforme a intenção do vídeo
4. Entregar o roteiro no **Formato de Output Padrão** (seção abaixo)

## Trigger

Este comando é invocado quando o usuário diz `/criar-video`, ou pede para criar roteiro de vídeo, YouTube, Reels, TikTok, Shorts ou VSL.

## Inputs

Se algum campo obrigatório estiver faltando, pergunte antes de prosseguir:

1. **Formato** (obrigatório) — YouTube long-form, YouTube Shorts, Instagram Reels, TikTok, ou VSL
2. **Tema** (obrigatório) — Assunto do vídeo
3. **Objetivo** (obrigatório) — Viral/entretenimento, educar, inspirar, ou converter/vender
4. **Duração** (obrigatório para Reels) — 15s, 30s, 60s, 90s, ou outro
5. **Nicho** (obrigatório) — Marketing Digital, IA, Dev Pessoal, Empreendedorismo, Saúde, etc.
6. **Público-alvo** (opcional) — Para quem é o vídeo
7. **Clone de voz** (opcional) — Se não informado, aplicar regra de seleção automática abaixo
8. **CTA** (opcional) — Ação desejada do espectador

## Seleção Automática de Clone de Voz

Se o usuário não especificar um clone, aplicar esta regra:

| Objetivo do vídeo | Clone ativado | Por quê |
|---|---|---|
| Viral / entretenimento / crescimento de audiência | **MrBeast** | Retenção extrema, energia épica, challenge-driven |
| Venda / funil / conversão | **Brunson** | Hook-story-offer, escassez, CTA de conversão |
| Educativo / lifestyle / produtividade | **Abdaal** | Evidence-based, acessível, calmo |
| VSL / oferta de alto valor | **Hormozi** | Números concretos, lógica matemática, urgência |
| YouTube long-form / brand | **Abdaal** ou **Ogilvy** | Research-driven, storytelling elegante |

Após selecionar o clone, carregar o perfil em `squads/marketing-os/data/clones/{nome-clone}/` para aplicar voz, tom e frameworks específicos.

## Estruturas por Formato

Usar as estruturas completas definidas em `../subagents/video-agent.md`. Resumo de referência rápida:

### Reels / TikTok / Shorts

| Duração | Estrutura |
|---------|-----------|
| 15s | Hook (0-3s) → Ponto único (3-12s) → CTA (12-15s) |
| 30s | Hook (0-3s) → Contexto (3-8s) → Conteúdo (8-25s) → CTA (25-30s) |
| 60s | Hook (0-3s) → Promessa (3-8s) → Ponto 1+2+3 (8-50s) → CTA (50-60s) |
| 90s | Hook (0-3s) → Promessa (3-8s) → Ponto 1 (8-28s) → Re-hook (28-32s) → Ponto 2 (32-52s) → Ponto 3 (52-72s) → CTA + Loop (72-90s) |

**Regra dos 90s:** inserir re-hook entre 25-30s para recuperar atenção. Estrutura completa em `../subagents/video-agent.md` seção "Formatos de Vídeo".

### YouTube Long-Form (8-20 min)

Ver estrutura detalhada em `../subagents/video-agent.md`.

### VSL (5-45 min)

Ver estrutura detalhada em `../subagents/video-agent.md`.

## Regras de Qualidade Obrigatórias (Marketing OS)

**NUNCA usar em nenhum roteiro ou conteúdo gerado:**

| Proibido | Alternativa |
|----------|-------------|
| `—` (travessão longo) | Use `.` `,` `:` ou quebre a frase |
| `brutal` | intenso, forte, impactante, poderoso |
| PALAVRAS EM MAIÚSCULA | Escreva em minúscula normalmente |
| Aspas para delimitar falas no roteiro | Escreva o texto direto, sem aspas |
| Emojis em excesso | Máximo 1-2 por conteúdo |
| Texto sem acentos | SEMPRE usar acentuação correta em português |

**Verificação de fatos:** Ao citar pessoas famosas, estatísticas ou dados, usar WebSearch para verificar antes de incluir. Nunca inventar dados.

**Verificar sempre antes de entregar:** acentuação, aspas, caps, emojis, fatos.

## Formato de Output Padrão

Entregar o roteiro neste formato:

```
## ROTEIRO DE VÍDEO

Dados do Vídeo:
- Formato: [YouTube / Reels / TikTok / Shorts / VSL]
- Plataforma: [Instagram / YouTube / TikTok / etc.]
- Duração: [XX segundos / XX minutos]
- Objetivo: [Viral / Educar / Converter / Inspirar]
- Nicho: [nicho]
- Clone de Voz: [nome do clone ativado]
- Público-alvo: [descrição]

---

Variações A/B do Hook (escolha uma para gravar):

Opção A (Recomendada):
[hook sem aspas, direto]
Por que funciona: [explicação breve]

Opção B:
[hook alternativo]

Opção C:
[hook alternativo]

---

Roteiro Completo:

[TIMECODE] VISUAL: [descrição da cena]
TEXTO NA TELA: [texto se aplicável]
FALA: texto direto sem aspas aqui

[continuar para todas as seções com timecodes...]

---

Especificações Técnicas:
- Proporção: [9:16 para Reels/TikTok | 16:9 para YouTube]
- Resolução: [1080x1920 | 1920x1080]
- Ritmo de corte: [descrição]
- Música: [gênero/mood sugerido]

---

Caption / Legenda:
[legenda completa com CTA e hashtags]

Hashtags: [6-10 hashtags relevantes]

---

Métricas-alvo:
- Watch time: [%]
- Saves/Compartilhamentos: [meta]
- Comentários: [tipo de engajamento esperado]

---

Enquete para Stories (obrigatório para Reels):
Pergunta: [pergunta relacionada ao conteúdo]
Opção A: [resposta]
Opção B: [resposta]

---

Próximos passos:
1. [ação de produção]
2. [ação de produção]
3. [ação de publicação]
```

## Após Entregar

Perguntar:

Quer que eu:
1. Expanda alguma seção com mais detalhes ou exemplos?
2. Crie variações adicionais do hook para testes A/B?
3. Adapte este roteiro para outra plataforma ou duração?
4. Gere um brief de design para a thumbnail?
