---
description: Activate a campaign preset (lancamento, prospeccao, retencao, autoridade, growth, black-friday). Each preset dispatches a tailored sequence of mos-* agents in parallel/sequential phases with the recommended clone voice.
argument-hint: "<preset> [--produto=...] [--clone=...] [--canal=...] [--budget=...] [--nicho=...]"
---

# /campanha: Presets de Campanha por Objetivo

Meta-roteador. Cada preset traduz "quero rodar uma campanha do tipo X" em **fases de dispatch explícitas** dos mos-* agents adequados, com clone primário sugerido, checklist e KPIs.

## Required inputs (ask if missing)

1. **Tipo do preset** (obrigatório): `lancamento` | `prospeccao` | `retencao` | `autoridade` | `growth` | `black-friday`
2. **Produto/oferta** (obrigatório na maioria dos presets)
3. **Audiência/avatar** (obrigatório)
4. **Customizações opcionais**: `--produto=<nome>`, `--clone=<override>`, `--canal=<canal>`, `--budget=<valor>`, `--nicho=<nicho>`, `--preco=<valor>`, `--segmento=<segmento>`, `--desconto=<%>`

## Customização

Cada preset tem clone primário recomendado, mas o usuário pode sobrescrever:

```
/campanha lancamento --produto="Curso de Copy" --preco=997 --clone=hormozi
/campanha prospeccao --canal=instagram --budget=500 --nicho=empreendedorismo
/campanha retencao --segmento=inativos-90dias --desconto=20%
/campanha autoridade --clone=garyvee
/campanha black-friday --produto="Mentoria 1:1" --desconto=40%
```

---

## Preset 1: /campanha lancamento

**Objetivo:** Lançar produto/serviço/curso/oferta com máximo impacto.
**Clone primário:** `brunson` · **Clone alternativo:** `suby`

### Dispatch

**Fase 1 (paralelo, single message):**

```
- Agent(subagent_type: "mos-research", prompt: "Validação pré-lançamento de [produto] pra [avatar/nicho]: tamanho do nicho, concorrência ativa, ticket médio praticado, dores não atendidas, ângulos de oferta com tração. Considere memory existente.")

- Agent(subagent_type: "mos-launch", prompt: "Estratégia de lançamento pra [produto], ticket [preço]: escolher modelo (PLF / semente / relâmpago / perpétuo) baseado em nicho [nicho] e tamanho da lista. Definir cronograma -2sem → +5dias, pitch timing, gatilhos de escassez.")

- Agent(subagent_type: "mos-funnel", prompt: "Funil de lançamento pra [produto]: TOFU (aquecimento orgânico + ads) → MOFU (lead magnet/CPL/webinar) → BOFU (carta de vendas + carrinho). Pontos de queda esperados e contramedidas.")
```

**Fase 2 (paralelo, depende da estratégia da Fase 1):**

```
- Agent(subagent_type: "mos-copy", prompt: "Copy de lançamento clone=brunson: headline da página, big idea, mecanismo único, anti-avatar, stack value, garantia, FAQ. Usando posicionamento da Fase 1: [colar].")

- Agent(subagent_type: "mos-storytelling", prompt: "Narrativa da jornada do produto: arco do criador → problema dor → descoberta → solução. Hero's journey aplicado ao pitch de lançamento.")

- Agent(subagent_type: "mos-social", prompt: "Sequência de posts de aquecimento (5-7 posts): semana -2 problema, semana -1 solução parcial, dia 0 abertura. Plataforma [Instagram/LinkedIn/etc]. Aplicar quality gates + enquete.")

- Agent(subagent_type: "mos-email", prompt: "Sequência completa de lançamento: 5 emails de pré-aquecimento + email abertura carrinho + 3 emails de urgência/prova/fechamento + email pós-fechamento. Considere memory do cliente.")
```

**Fase 3 (sequencial, depende da copy/criativo da Fase 2):**

```
- Agent(subagent_type: "mos-ads", prompt: "Campanhas de tráfego pra cada fase do lançamento: pré (lista quente), durante (conversão), retargeting pós. Budget [valor]. Audiências quentes/frias/lookalikes.")

- Agent(subagent_type: "mos-design", prompt: "Assets visuais da campanha: identidade do lançamento, paleta, capa do produto, mockups, criativos de ads, banners de página. Coerência com brand existente.")

- Agent(subagent_type: "mos-analytics", prompt: "Setup de tracking: pixels, UTMs, eventos de conversão (lead, view-content, add-to-cart, purchase), KPIs do lançamento, dashboard de monitoramento.")
```

### Cronograma default
- **Semana -2:** Aquecimento (problema)
- **Semana -1:** Conteúdo de valor (solução parcial)
- **Dia -3:** Abertura do carrinho / anúncio do produto
- **Dia -1:** Urgência e prova social
- **Dia 0:** Lançamento oficial
- **Dia +2:** Depoimentos e follow-up
- **Dia +5:** Fechamento / última chance

### Frameworks aplicados
- PLF (Product Launch Formula) — Jeff Walker
- Seed-and-Launch — Russell Brunson
- Value Stack — Alex Hormozi

### Checklist de Lançamento

```
PRÉ-LANÇAMENTO (2 semanas antes):
[ ] Pesquisa de mercado e validação de oferta (Fase 1: mos-research)
[ ] Definição de avatar e posicionamento (Fase 1)
[ ] Produto/oferta core completa
[ ] Landing page de captura de leads / lista de espera
[ ] Sequência de email de aquecimento (Fase 2: mos-email)
[ ] Conteúdo de aquecimento social (Fase 2: mos-social)
[ ] Assets visuais e identidade (Fase 3: mos-design)
[ ] Setup de tracking — pixel, UTMs, conversões (Fase 3: mos-analytics)

LANÇAMENTO (dia D):
[ ] Email de abertura
[ ] Posts em todas as plataformas ativas
[ ] Anúncios pagos ativados
[ ] Stories com contagem regressiva
[ ] Monitoramento em tempo real (mos-analytics)

PÓS-LANÇAMENTO:
[ ] Sequência de follow-up
[ ] Retargeting para não-convertidos
[ ] Email de fechamento
[ ] Análise de performance (mos-analytics)
[ ] Documentação de aprendizados
```

### KPIs

| KPI | Benchmark | Como Medir |
|-----|-----------|------------|
| Conversão da lista | 3-7% | Compras / leads na lista |
| ROAS de ads | > 3x | Receita / Gasto em ads |
| Open rate emails | > 35% | Abertos / enviados |
| CTR emails | > 5% | Cliques / abertos |

---

## Preset 2: /campanha prospeccao

**Objetivo:** Gerar leads qualificados e novos clientes de forma consistente.
**Clone primário:** `suby` · **Clone alternativo:** `kennedy`

### Dispatch

**Fase 1 (sequencial, research informa o resto):**

```
- Agent(subagent_type: "mos-research", prompt: "Mapeamento de avatar e canais para prospecção em [nicho]: dores reais, linguagem usada, plataformas onde está, concorrentes ativos, lead magnets que funcionam. Considere memory.")
```

**Fase 2 (paralelo, depende do research):**

```
- Agent(subagent_type: "mos-funnel", prompt: "Funil HDIC (Horde-Direct-Convert) de Sabri Suby: TOFU (audiência fria + interesse + lookalike) → MOFU (lead magnet + nutrição) → BOFU (oferta direta + retargeting). Pontos de qualificação.")

- Agent(subagent_type: "mos-copy", prompt: "Copy clone=suby: lead magnet de alto valor (PDF/mini-curso/webinar), landing page de captura, headline + CTA. Usando avatar da Fase 1.")

- Agent(subagent_type: "mos-ads", prompt: "Campanhas de tráfego pago pra prospecção: audiência fria + interest + lookalike. Budget [valor]. CPL alvo [< R$15-50 dependendo de nicho]. Variantes A/B de criativo.")
```

**Fase 3 (paralelo):**

```
- Agent(subagent_type: "mos-email", prompt: "Sequência de nutrição 7-10 emails pós opt-in: educação → história → caso de prova → soft pitch → hard pitch → urgência → última chance. Considere memory.")

- Agent(subagent_type: "mos-social", prompt: "Conteúdo de topo de funil: 3-5 posts/semana sobre dores do avatar, sem pitch direto. Quality gates + enquete.")

- Agent(subagent_type: "mos-analytics", prompt: "Tracking de CAC, CPL por canal, conversão da landing, performance da nutrição. Dashboard mensal de revisão.")
```

### Frameworks
- Método HDIC (Horde-Direct-Convert) — Sabri Suby
- Pirâmide de Consciência (3% → 97%)
- Os 3 Pilares — Jay Abraham

### Estrutura do Funil

```
TOPO (Awareness): conteúdo orgânico de dores + ads frios → tráfego pra LM
MEIO (Interesse): lead magnet + nutrição email + retargeting → qualificação
FUNDO (Decisão): oferta direta + testemunhos + garantia → conversão
```

### Checklist

```
SETUP INICIAL:
[ ] Avatar detalhado (Fase 1: mos-research)
[ ] Lead magnet criado (Fase 2: mos-copy)
[ ] Landing page de captura (Fase 2: mos-copy)
[ ] Sequência de nutrição (Fase 3: mos-email)
[ ] Budget e canais definidos (Fase 2: mos-ads)

OPERAÇÃO SEMANAL:
[ ] 3-5 posts de topo (Fase 3: mos-social)
[ ] CPL monitorado e criativos otimizados
[ ] Métricas da nutrição revisadas
[ ] Próxima variante A/B da landing testada

ANÁLISE MENSAL:
[ ] CAC vs LTV sustentável?
[ ] Canal com menor CPL?
[ ] Email da nutrição com mais conversão?
[ ] Próximo teste A/B prioritário
```

### KPIs

| KPI | Meta | Canal |
|-----|------|-------|
| CPL | < R$15-50 (varia por nicho) | Ads |
| Opt-in | > 35% | Landing page |
| Open nutrição | > 30% | Email |
| CAC | < LTV/3 | Todos |

---

## Preset 3: /campanha retencao

**Objetivo:** Aumentar LTV, reativar clientes inativos, reduzir churn.
**Clone primário:** `abraham` · **Clone alternativo:** `leila-hormozi`

### Dispatch

**Fase 1 (paralelo — entender LTV/churn antes de agir):**

```
- Agent(subagent_type: "mos-research", prompt: "Análise da base atual: segmentação por recência/valor, identificação de clientes inativos (>90d), perfil de churn (motivos), ticket médio histórico. Considere memory do cliente.")

- Agent(subagent_type: "mos-analytics", prompt: "Métricas de retenção: LTV médio, taxa de churn mensal, segmento VIP (top 20%), padrões de queda de engajamento. Setup de alertas de risco.")
```

**Fase 2 (paralelo, depende dos segmentos da Fase 1):**

```
- Agent(subagent_type: "mos-email", prompt: "Sequências por segmento clone=abraham:
  - Inativos 90+d: 5 emails em 14d (reconexão genuína + oferta de retorno)
  - Ativos < 90d: upsell/cross-sell (estilo Hormozi confiante)
  - VIP top 20%: programa de fidelidade + indicação personalizada
  - Em risco de churn: 3 emails rápidos perguntando o problema + suporte personalizado
  Considere memory.")

- Agent(subagent_type: "mos-copy", prompt: "Copy de reativação e upsell clone=abraham: headlines que evocam reconexão (não desconto barato), CTAs de retorno, emails de programa de indicação.")

- Agent(subagent_type: "mos-social", prompt: "Conteúdo pra clientes existentes: bastidores, novidades, casos de uso avançados. Reforça valor pra quem já comprou. Quality gates + enquete.")
```

### Segmentação

```
SEGMENTO 1 — INATIVOS (>90d): Reativação com oferta exclusiva. Tom Abraham. 5 emails / 14d.
SEGMENTO 2 — ATIVOS (<90d): Upsell/cross-sell. Tom Hormozi. Email + social.
SEGMENTO 3 — VIP (top 20%): Programa de fidelidade. Tom exclusivo. Email + ligação se high-ticket.
SEGMENTO 4 — RISCO DE CHURN: Engajamento de emergência. 3 emails rápidos + suporte personalizado.
```

### Frameworks
- Os 3 Pilares — Abraham (Pilar 2 e 3)
- LTV Maximization
- Reactivation Sequence — Dan Kennedy

### Checklist

```
SETUP (uma vez):
[ ] Segmentar base por recência e valor (Fase 1)
[ ] Sequência de onboarding (novos clientes)
[ ] Sequência de reativação (inativos) (Fase 2: mos-email)
[ ] Sequência de upsell (ativos) (Fase 2: mos-email)
[ ] Critérios de "cliente em risco" definidos (Fase 1: mos-analytics)

OPERAÇÃO MENSAL:
[ ] Lista de inativos do mês exportada
[ ] Campanha de reativação rodada
[ ] Oportunidades de upsell identificadas
[ ] Taxa de churn analisada

KPIs:
[ ] LTV médio aumentando?
[ ] Reativação > 10%?
[ ] Upsell > 15%?
[ ] Churn abaixo da meta?
```

---

## Preset 4: /campanha autoridade

**Objetivo:** Construir autoridade, credibilidade e presença de marca no nicho.
**Clone primário:** `ogilvy` · **Clone alternativo:** `abdaal`

### Dispatch

**Fase 1 (paralelo):**

```
- Agent(subagent_type: "mos-research", prompt: "Mapeamento de temas de autoridade no nicho [nicho]: o que os top players publicam, gaps de conteúdo, perguntas não respondidas, dados/estudos atuais. Considere memory.")

- Agent(subagent_type: "mos-brand", prompt: "Definir/refinar identidade de autoridade: arquétipo (sage / hero / mentor), voz/tom estilo Ogilvy (sofisticado, evidence-based), pilares de posicionamento. Brand spec replicável.")
```

**Fase 2 (paralelo, depende do positioning):**

```
- Agent(subagent_type: "mos-copy", prompt: "Posts e artigos de posicionamento clone=ogilvy: thought leadership, opinião baseada em evidência, sem clickbait. Aplicar quality gates rigorosos (sem hype).")

- Agent(subagent_type: "mos-seo", prompt: "Estratégia SEO de autoridade: 1 artigo longo quinzenal (pillar pages) + cluster de artigos satélites. Keyword research focado em intent informacional. Internal linking pra hub de autoridade.")

- Agent(subagent_type: "mos-social", prompt: "Calendário editorial de autoridade nos pilares: 40% Educação + 30% Perspectiva + 20% Prova + 10% Humanização. 2-3 posts/semana de valor profundo. Quality gates + enquete.")

- Agent(subagent_type: "mos-storytelling", prompt: "Narrativas de credibilidade: casos de estudo do próprio trabalho, jornada do criador, decisões controversas com lições. Hero's journey aplicado em formato editorial.")
```

**Fase 3 (opcional — se nicho/audiência justificar áudio):**

```
- Agent(subagent_type: "mos-audio", prompt: "Roteiro de podcast ou conteúdo em áudio: 1 episódio mensal de aprofundamento, formato entrevista ou solo. Show notes + clipes pra repurposing.")
```

### Pilares de Conteúdo

```
PILAR 1 — EDUCAÇÃO (40%): ensina algo específico/útil. Carrossel, artigo, vídeo tutorial.
PILAR 2 — PERSPECTIVA (30%): opinião baseada em dados. Post de texto, LinkedIn, thread.
PILAR 3 — PROVA (20%): casos de sucesso, resultados, bastidores. Depoimento, estudo de caso.
PILAR 4 — HUMANIZAÇÃO (10%): falhas, jornada, curiosidades pessoais. Stories, vídeo informal.
```

### Frameworks
- Content Marketing — David Ogilvy
- Evidence-Based Content — Ali Abdaal
- Preeminência — Jay Abraham

---

## Preset 5: /campanha growth

**Objetivo:** Experimentação acelerada para crescimento não-linear.
**Clone primário:** `ellis` · **Clone alternativo:** `chen`

### Dispatch

**Fase 1 (paralelo):**

```
- Agent(subagent_type: "mos-research", prompt: "Análise de oportunidades de growth: pontos de fricção do funil atual, north star metric, alavancas com maior potencial de impacto. Considere memory de experimentos anteriores.")

- Agent(subagent_type: "mos-analytics", prompt: "Setup AARRR (Acquisition / Activation / Retention / Referral / Revenue): tracking de cada estágio, identificação de leaks, baseline pra comparação de experimentos.")
```

**Fase 2 (paralelo, depende das oportunidades identificadas):**

```
- Agent(subagent_type: "mos-ab-testing", prompt: "Design de batch de experimentos: 4-6 hipóteses ranqueadas por ICE Score (Impacto × Confiança × Facilidade). Pra cada uma: variante A/B, tamanho mínimo de amostra, critério de parada, métrica primária.")

- Agent(subagent_type: "mos-growth", prompt: "Estratégias de growth hacking aplicáveis ao funil [TOFU/MOFU/BOFU]: viral loops, referral, retention hooks, ativação. Priorizar por viral coefficient esperado.")

- Agent(subagent_type: "mos-copy", prompt: "Variantes de copy pros experimentos da Fase 2: headlines, CTAs, value props alternativas. Pra cada variante, hipótese explicitada.")
```

### Ciclo Semanal de Experimentos

```
SEG (Hipótese): "Se [mudança], então [métrica] vai [melhorar] porque [razão]". ICE Score.
TER (Design): variante A/B + amostra mínima + tracking + critério de parada.
QUA-SEX (Execução): launcha + não analisa antes do tempo definido + documenta variáveis externas.
SEG seguinte (Análise): significância estatística + segmentos + decisão (implementar / iterar / descartar).
SEMPRE (Documentação): log de experimentos + aprendizados (mesmo em casos negativos) + próxima hipótese.
```

### Frameworks
- ICE Score — Sean Ellis
- Growth Loop
- Viral Coefficient
- AARRR Metrics (Pirate Metrics)

---

## Preset 6: /campanha black-friday

**Objetivo:** Maximizar receita em datas especiais (Black Friday, Cyber Monday, datas comemorativas).
**Clone primário:** `hormozi` · **Clone alternativo:** `suby`

### Dispatch

**Fase 1 (sequencial — estratégia precisa vir primeiro):**

```
- Agent(subagent_type: "mos-launch", prompt: "Estratégia Black Friday pra [produto]: composição da oferta (desconto + bônus + urgência real), value stack que justifica o preço, cronograma D-7 → D+2, lista VIP pra warm-up. Frameworks: Hormozi value stack + scarcity real (não artificial).")
```

**Fase 2 (paralelo, depende da estratégia):**

```
- Agent(subagent_type: "mos-copy", prompt: "Copy clone=hormozi de alta urgência pra Black Friday: headlines de oferta, página de vendas atualizada com timer, CTAs agressivos mas honestos, FAQ de objeções de fim de ano. Quality gates + compliance.")

- Agent(subagent_type: "mos-email", prompt: "Sequência intensiva 7 dias:
  - Dia -7: teaser + abertura da lista VIP
  - Dia -3: anúncio oficial da promoção
  - Dia -1: último aviso
  - Dia 0: abertura — Black Friday (manhã + tarde + noite)
  - Dia +1: Cyber Monday (se aplicável)
  - Dia +2: última chance (manhã + 6h antes do fim)
  Considere memory de campanhas BF anteriores.")

- Agent(subagent_type: "mos-ads", prompt: "Campanhas agressivas de conversão pra BF: budget escalonado D-7 → D+2, bid strategy ROAS, criativos com timer + desconto destacado, retargeting de carrinho abandonado. ROAS alvo > 4x.")

- Agent(subagent_type: "mos-social", prompt: "Posts e stories de contagem regressiva + promoção: D-7 teaser, D-3 oficial, D-1 urgência, D0 abertura, D+1 social proof de quem comprou, D+2 última chance. Quality gates + enquete.")
```

**Fase 3 (paralelo durante a campanha):**

```
- Agent(subagent_type: "mos-analytics", prompt: "Monitoramento em tempo real durante BF: receita/hora vs meta, ROAS por canal, conversão do checkout, alertas de queda. Dashboard de plantão.")
```

### Cronograma

| Dia | Ação |
|-----|------|
| D-7 | Teaser + lista VIP |
| D-3 | Anúncio oficial da promoção |
| D-1 | Último aviso |
| D 0 | Abertura — Black Friday |
| D+1 | Cyber Monday (se aplicável) |
| D+2 | Última chance |

### Frameworks
- Value Stack — Alex Hormozi
- Urgência Real (não artificial)
- Scarcity Marketing

### Checklist Black Friday

```
3 SEMANAS ANTES:
[ ] Oferta definida (produto + bônus + desconto) (Fase 1: mos-launch)
[ ] Value stack calculado pra justificar preço (Fase 1)
[ ] Lista VIP de espera criada
[ ] Copy completa preparada (Fase 2: mos-copy)
[ ] Design dos assets (mos-design opcional)

1 SEMANA ANTES:
[ ] Anúncios configurados (Fase 2: mos-ads) — não ativar ainda
[ ] Página de vendas e checkout testados
[ ] Posts e emails agendados
[ ] Briefing da equipe

NO DIA:
[ ] Anúncios ativados às 00h01
[ ] Email de abertura enviado
[ ] Posts em todas as plataformas
[ ] Monitoramento por hora (Fase 3: mos-analytics)

KPIs:
[ ] Receita vs meta
[ ] ROAS > 4x (BF tem melhor ROAS)
[ ] Conversão vs campanha normal
```

---

## Quality Gates Globais (aplicar em todas as fases de todos os presets)

Ver `skills/marketing-os/SKILL.md`:
- Sem `—` (travessão longo)
- Sem "brutal"
- Sem CAPS gratuito
- Sem aspas em roteiros/falas
- Máximo 1-2 emojis (preferir 0)
- Acentuação PT-BR correta
- Fact-check via WebSearch em pessoas/estatísticas/cases (CONFIRMADO / PROVÁVEL / NÃO USAR)
- Compliance regulatório se nicho saúde/finanças/suplementos
- Enquete obrigatória em conteúdo social
- Disclaimer "Resultados não garantidos" em promessa quantitativa

## Memory note (vale para todos os presets)

Vários dos agents dispatchados (`mos-copy`, `mos-email`, `mos-ads`, `mos-social`, `mos-funnel`, `mos-launch`) têm memory project em `.claude/agent-memory/marketing-os-<agent>/`. **Sempre mencione no prompt** que considere memory existente do cliente — evita repetir hooks usados, mantém consistência com campanhas passadas, e respeita restrições de compliance previamente registradas.

## Recursos relacionados

- `workflows/end-to-end-campaign-workflow.md` — workflow completo de referência
- `workflows/content-pipeline.md` — pipeline de produção
- `assets/clones/clone-manifest.yaml` — sistema de clones (35 perfis)
- `subagents/ab-testing-agent.md` — testes A/B aprofundados
- `scripts/ab_generator.py` — geração automática de variantes

## Por que essa estrutura de fases

Campanhas falham quando se pula a estratégia (Fase 1) e vai direto pra execução de copy. Cada preset força a sequência: research/strategy primeiro, depois assets em paralelo, depois execução técnica (ads/tracking). O dispatch explícito torna a coordenação dos agents reproduzível e o output rastreável fase a fase.
