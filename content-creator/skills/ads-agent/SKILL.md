# 🎯 Ads Agent - Subagente de Anúncios Pagos

Subagente especializado em criação de copy e estratégia para anúncios pagos (Meta Ads, Google Ads, TikTok Ads).

---

## 🎯 Quando Usar

- Criar copy de anúncios
- Desenvolver estratégia de campanha
- Otimizar headlines e CTAs
- Criar variações para testes A/B
- Definir públicos e segmentações
- Estruturar funis de tráfego pago

---

## 📊 Plataformas Suportadas

| Plataforma | Formatos Principais | Objetivo Principal |
|------------|---------------------|-------------------|
| **Meta Ads** | Imagem, Vídeo, Carrossel, Stories | Awareness, Conversão, Leads |
| **Google Ads** | Search, Display, YouTube | Intenção, Remarketing |
| **TikTok Ads** | Vídeo nativo, Spark Ads | Awareness, Engajamento |
| **LinkedIn Ads** | Sponsored Content, InMail | B2B, Leads qualificados |

---

## 🎨 Meta Ads (Facebook/Instagram)

### Especificações Técnicas

| Formato | Dimensão | Texto Primário | Headline | Descrição |
|---------|----------|----------------|----------|-----------|
| **Feed Imagem** | 1080x1080 | 125 chars | 40 chars | 30 chars |
| **Feed Vídeo** | 1080x1080 | 125 chars | 40 chars | 30 chars |
| **Stories** | 1080x1920 | 125 chars | 40 chars | - |
| **Carrossel** | 1080x1080 | 125 chars | 40 chars | 20 chars |
| **Reels** | 1080x1920 | 72 chars | 40 chars | - |

### Estrutura de Copy - Meta Ads

```
┌─────────────────────────────────────────┐
│ TEXTO PRIMÁRIO (acima da imagem)        │
│ ├── Hook: Primeira linha impactante     │
│ ├── Problema/Oportunidade               │
│ ├── Solução/Benefício                   │
│ └── CTA textual                         │
├─────────────────────────────────────────┤
│ [CRIATIVO: Imagem/Vídeo]                │
├─────────────────────────────────────────┤
│ HEADLINE: Promessa clara                │
│ DESCRIÇÃO: Complemento + urgência       │
│ [BOTÃO CTA]                             │
└─────────────────────────────────────────┘
```

### Templates de Copy - Meta Ads

#### Template TOFU (Awareness)
```
TEXTO PRIMÁRIO:
{Hook de identificação}

Se você é {persona} e quer {desejo}, precisa ver isso.

{Breve explicação do valor}

👉 {CTA}

HEADLINE: {Benefício principal}
DESCRIÇÃO: {Complemento + diferencial}
CTA: Saiba Mais
```

#### Template MOFU (Consideração)
```
TEXTO PRIMÁRIO:
{Hook de problema}

Você já tentou {solução comum} e não funcionou?

O problema é: {insight}

Descobri um método que {resultado} sem {objeção}.

{Prova social ou dado}

HEADLINE: {Método/Solução}
DESCRIÇÃO: Veja como funciona
CTA: Saiba Mais
```

#### Template BOFU (Conversão)
```
TEXTO PRIMÁRIO:
🔥 {Oferta/Promoção}

{Benefício 1}
{Benefício 2}
{Benefício 3}

{Urgência/Escassez}

👉 {CTA direto}

HEADLINE: {Oferta + Desconto/Bônus}
DESCRIÇÃO: {Urgência}
CTA: Comprar Agora / Inscrever-se
```

---

## 🔍 Google Ads

### Especificações - Search Ads

| Elemento | Limite | Quantidade |
|----------|--------|------------|
| **Headline** | 30 chars | Até 15 |
| **Description** | 90 chars | Até 4 |
| **Display Path** | 15 chars | 2 |

### Estrutura RSA (Responsive Search Ads)

```
HEADLINES (criar 10-15):
├── Com keyword exata
├── Com benefício principal
├── Com número/estatística
├── Com pergunta
├── Com CTA
├── Com marca
├── Com diferencial
├── Com urgência
└── Com prova social

DESCRIPTIONS (criar 4):
├── Benefícios expandidos
├── Features + diferenciais
├── Prova social + credibilidade
└── CTA + urgência
```

### Templates Google Search

#### Template Informacional
```
HEADLINES:
• Como {Ação} em {Tempo}
• Guia Completo de {Tema}
• {Tema}: Tudo que Você Precisa Saber
• Aprenda {Tema} do Zero
• {Número} Dicas de {Tema}

DESCRIPTIONS:
• Descubra como {benefício} de forma simples e prática. Guia completo com passo a passo.
• Aprenda {tema} com especialistas. Método testado por +{número} alunos. Comece hoje!
```

#### Template Transacional
```
HEADLINES:
• {Produto} com {Desconto}% OFF
• Compre {Produto} Online
• {Produto} - Frete Grátis
• Oferta: {Produto} por R${Preço}
• {Produto} Original - Site Oficial

DESCRIPTIONS:
• {Produto} com até {X}% de desconto. Parcelamos em até 12x. Entrega rápida para todo Brasil.
• Compre {produto} no site oficial. Garantia de {X} anos. Troca grátis em {X} dias.
```

---

## 🎬 TikTok Ads

### Especificações

| Elemento | Limite |
|----------|--------|
| **Nome do Anúncio** | 512 chars |
| **Texto do Anúncio** | 100 chars |
| **Vídeo** | 5-60s (9:16) |
| **CTA** | Pré-definidos |

### Estrutura de Vídeo TikTok Ads

```
0-3s: HOOK FORTE
├── Texto na tela impactante
├── Movimento/ação visual
└── Áudio que prende

3-15s: PROBLEMA/CONTEXTO
├── Identificação com persona
├── Dor ou desejo
└── Setup para solução

15-40s: SOLUÇÃO/DEMONSTRAÇÃO
├── Mostrar produto/serviço
├── Benefícios visuais
├── Prova de funcionamento
└── Depoimentos curtos

40-50s: PROVA SOCIAL
├── Resultados
├── Reviews
└── Números

50-60s: CTA
├── Oferta clara
├── Urgência
└── Instrução específica
```

### Hooks para TikTok Ads

```
CURIOSIDADE:
"POV: você descobriu {benefício}"
"O que ninguém te conta sobre {tema}"
"Eu testei {produto} e olha isso..."

IDENTIFICAÇÃO:
"Se você é {persona}, isso é pra você"
"Todo mundo que {situação} precisa ver isso"
"Você também passa por isso?"

CHOQUE:
"Isso deveria ser ilegal"
"Não acredito que funcionou"
"Eu estava fazendo tudo errado"

TENDÊNCIA:
"Essa trend de {tema}..."
"Todo mundo está falando de {produto}"
"Finalmente testei {viral}"
```

---

## 📊 Estrutura de Campanha

### Funil de Tráfego Pago

```
┌─────────────────────────────────────────────────────────┐
│                    TOFU (AWARENESS)                      │
│  Objetivo: Alcance, Vídeo Views, Engajamento            │
│  Público: Amplo, Interesses, Lookalike                  │
│  Copy: Educativo, Valor, Sem venda                      │
│  CTA: Saiba Mais, Assista                               │
├─────────────────────────────────────────────────────────┤
│                 MOFU (CONSIDERAÇÃO)                      │
│  Objetivo: Tráfego, Leads, Mensagens                    │
│  Público: Engajou TOFU, Site visitors                   │
│  Copy: Problema-Solução, Autoridade                     │
│  CTA: Baixar, Inscrever, Ver mais                       │
├─────────────────────────────────────────────────────────┤
│                  BOFU (CONVERSÃO)                        │
│  Objetivo: Conversões, Compras, Leads                   │
│  Público: Remarketing quente, Leads, Carrinho           │
│  Copy: Oferta, Urgência, Prova social                   │
│  CTA: Comprar, Garantir, Inscrever-se                   │
└─────────────────────────────────────────────────────────┘
```

### Orçamento Sugerido por Fase

| Fase | % do Budget | Objetivo |
|------|-------------|----------|
| **TOFU** | 20-30% | Aquecer público frio |
| **MOFU** | 30-40% | Educar e qualificar |
| **BOFU** | 40-50% | Converter |

---

## 🎯 Segmentação e Públicos

### Tipos de Público

```
PÚBLICOS FRIOS:
├── Interesses relacionados
├── Comportamentos de compra
├── Dados demográficos
└── Lookalike 1-3%

PÚBLICOS MORNOS:
├── Engajou com conteúdo (30-90 dias)
├── Visitou site (30-90 dias)
├── Lookalike de compradores
└── Lista de leads

PÚBLICOS QUENTES:
├── Visitou página de produto (7-14 dias)
├── Adicionou ao carrinho (7 dias)
├── Iniciou checkout (3 dias)
└── Compradores para upsell
```

---

## ✅ Checklist de Anúncio

### Antes de Publicar

- [ ] Copy dentro dos limites de caracteres
- [ ] Hook nos primeiros 3 segundos (vídeo)
- [ ] CTA claro e específico
- [ ] Criativo de alta qualidade
- [ ] Texto legível no mobile
- [ ] Sem muito texto na imagem (<20%)
- [ ] Landing page consistente com anúncio
- [ ] UTMs configurados
- [ ] Pixel/conversões configurados
- [ ] Público correto selecionado
- [ ] Orçamento adequado
- [ ] Variações para teste A/B

---

## 📈 Métricas de Performance

### KPIs por Objetivo

| Objetivo | Métrica Principal | Benchmark |
|----------|-------------------|-----------|
| **Awareness** | CPM, Alcance | CPM < R$20 |
| **Tráfego** | CPC, CTR | CTR > 1%, CPC < R$2 |
| **Leads** | CPL, Taxa Conversão | CPL < R$15 |
| **Vendas** | ROAS, CPA | ROAS > 3x |

### Diagnóstico de Problemas

```
CTR BAIXO (<1%):
├── Criativo fraco
├── Hook não prende
├── Público errado
└── Copy genérica

CPC ALTO:
├── Concorrência alta
├── Relevância baixa
├── Segmentação ampla demais
└── Criativo saturado

CPL/CPA ALTO:
├── Landing page não converte
├── Promessa diferente do anúncio
├── Formulário muito longo
└── Público frio demais
```

---

## 🔄 Testes A/B

### O que Testar

```
PRIORIDADE ALTA:
├── Hook/primeira linha
├── Criativo (imagem vs vídeo)
├── CTA button
└── Público

PRIORIDADE MÉDIA:
├── Headline
├── Descrição
├── Formato (carrossel vs single)
└── Posicionamento

PRIORIDADE BAIXA:
├── Cores do criativo
├── Horário de veiculação
├── Ordem do carrossel
└── Extensões
```

### Regras de Teste

```
• Testar 1 variável por vez
• Mínimo 1.000 impressões por variação
• Significância estatística > 95%
• Documentar hipótese antes do teste
• Implementar vencedor e testar próxima variável
```

---

## 🔄 Sequências de Retargeting

### Estrutura de Sequência de 7 Dias

```
DIA 1 - LEMBRETE
├── Objetivo: Relembrar o interesse
├── Tom: Amigável e leve
├── Foco: Produto/serviço que foi visualizado
└── CTA: Volte e veja mais

DIA 3 - PROVA SOCIAL
├── Objetivo: Gerar confiança
├── Tom: Inspirador e confiável
├── Foco: Depoimentos, avaliações, casos de sucesso
└── CTA: Veja o que estão dizendo

DIA 5 - TRATAMENTO DE OBJEÇÕES
├── Objetivo: Eliminar barreiras
├── Tom: Empático e esclarecedor
├── Foco: FAQ, garantias, comparações
└── CTA: Tire suas dúvidas / Sem risco

DIA 7 - URGÊNCIA / ÚLTIMA CHANCE
├── Objetivo: Gerar ação imediata
├── Tom: Urgente e direto
├── Foco: Oferta limitada, bônus expirando
└── CTA: Garanta agora / Última chance
```

### Templates por Touchpoint

**Dia 1 - Lembrete:**
```
TEXTO PRIMÁRIO:
Ei, notamos que você deu uma olhada em {produto/serviço}! 👀

Ainda está pensando? A gente entende — decisões importantes merecem tempo.

Mas enquanto decide, que tal dar mais uma olhada?

HEADLINE: {Produto} está te esperando
CTA: Voltar ao Site
```

**Dia 3 - Prova Social:**
```
TEXTO PRIMÁRIO:
Mais de {número} pessoas já escolheram {produto/serviço}.

"{Depoimento real de cliente}" — {Nome do cliente}

Descubra por que tantas pessoas confiam em {marca}.

HEADLINE: +{número} clientes satisfeitos
CTA: Ver Depoimentos
```

**Dia 5 - Tratamento de Objeções:**
```
TEXTO PRIMÁRIO:
Talvez você esteja se perguntando:

❓ "E se não funcionar para mim?"
→ {Resposta com garantia}

❓ "É caro demais?"
→ {Resposta com valor/parcelamento}

❓ "Não tenho tempo"
→ {Resposta com praticidade}

HEADLINE: Sem risco. Garantia de {X} dias.
CTA: Saiba Mais
```

**Dia 7 - Urgência / Última Chance:**
```
TEXTO PRIMÁRIO:
⏰ Última chance!

{Oferta/desconto/bônus} expira HOJE.

Depois disso, o preço volta ao normal.

Não deixe pra depois o que pode mudar sua {resultado} agora.

HEADLINE: Oferta encerra hoje — {desconto}% OFF
CTA: Garantir Agora
```

### Boas Práticas de Frequency Capping

| Fase do Funil | Frequência Máxima | Período |
|---------------|-------------------|---------|
| TOFU (Awareness) | 2-3 impressões | Por semana |
| MOFU (Consideração) | 3-5 impressões | Por semana |
| BOFU (Conversão) | 5-7 impressões | Por semana |
| Retargeting intensivo | 1-2 impressões | Por dia |

**Sinais de excesso de frequência:**
- CTR caindo consistentemente
- Aumento de comentários negativos
- CPC subindo sem motivo aparente
- Taxa de ocultação do anúncio aumentando

### Públicos de Exclusão

- Pessoas que já compraram (últimos 30-180 dias)
- Leads já convertidos na campanha atual
- Funcionários e parceiros (lista de emails)
- Pessoas que ocultaram o anúncio
- Público de frequência acima do limite (quando possível)

---

## 🧪 Creative Testing Framework

### Hierarquia de Testes

```
1. CONCEITO (maior impacto)
│  Qual a ideia central do anúncio?
│  Ex: Educativo vs Testemunho vs Demo
│
2. FORMATO
│  Qual formato funciona melhor?
│  Ex: Vídeo vs Imagem vs Carrossel
│
3. HOOK
│  Qual abertura prende mais atenção?
│  Ex: Pergunta vs Afirmação vs Estatística
│
4. COPY
│  Qual texto converte mais?
│  Ex: Longa vs Curta, Formal vs Informal
│
5. CTA (menor impacto individual)
   Qual chamada gera mais ação?
   Ex: "Comprar" vs "Garantir" vs "Testar grátis"
```

### Como Estruturar Testes de Criativos

1. **Definir hipótese clara** - "Acredito que {variação B} terá melhor {métrica} porque {razão}"
2. **Isolar uma variável** - Mudar apenas um elemento por teste
3. **Usar mesmo público** - Para comparação justa
4. **Definir métrica de sucesso** - CTR, CPA, ROAS ou outra
5. **Definir prazo** - Mínimo de 3-5 dias de veiculação

### Orçamento Mínimo por Teste

| Plataforma | Budget Mínimo por Variação | Duração Mínima |
|------------|---------------------------|----------------|
| Meta Ads | R$ 50-100/dia | 3-5 dias |
| Google Ads (Search) | R$ 30-50/dia | 5-7 dias |
| TikTok Ads | R$ 50-80/dia | 3-5 dias |
| LinkedIn Ads | R$ 80-150/dia | 5-7 dias |

**Regra geral:** cada variação precisa de pelo menos 1.000 impressões ou 50 conversões para ter significância mínima.

### Quando Pausar um Anúncio vs Deixar Rodando

**Pausar quando:**
- CPA está 2x acima da meta após 1.000 impressões
- CTR abaixo de 0,5% após 2.000 impressões (Meta)
- Zero conversões após gastar 3x o CPA meta
- Feedback negativo acima de 5%

**Deixar rodando quando:**
- Ainda não atingiu volume mínimo de dados
- CPA está dentro de 1,5x da meta e melhorando
- Anúncio tem menos de 3 dias de veiculação
- Está em fase de aprendizado da plataforma

### Sinais de Fadiga Criativa

| Sinal | O que Observar | Ação |
|-------|----------------|------|
| CTR caindo | Queda de >20% em 7 dias | Atualizar criativo |
| Frequência alta | Acima de 3-4 na semana | Expandir público ou pausar |
| CPA subindo | Aumento de >30% sem mudança externa | Testar novo conceito |
| Engajamento negativo | Comentários de "já vi isso" | Rotacionar criativos |
| CPM subindo | Aumento sem sazonalidade | Renovar criativos ou públicos |

### Processo de Iteração

1. Rodar 3-5 variações de conceito
2. Identificar conceito vencedor
3. Criar 3-5 variações de formato com o conceito vencedor
4. Identificar formato vencedor
5. Testar 3-5 hooks diferentes no formato e conceito vencedores
6. Repetir para copy e CTA
7. Combinar todos os elementos vencedores no "anúncio campeão"
8. Usar o campeão como controle para novos testes

### Template: Log de Testes de Criativos

```markdown
# LOG DE TESTES - [CAMPANHA]

## Teste #[Número]
- **Data:** [DD/MM/AAAA]
- **Variável testada:** [Conceito/Formato/Hook/Copy/CTA]
- **Hipótese:** [Se X, então Y, porque Z]

| Variação | Descrição | Spend | Impressões | CTR | CPA | ROAS |
|----------|-----------|-------|------------|-----|-----|------|
| A (Controle) | [Desc] | R$[X] | [Y] | [Z%] | R$[W] | [V]x |
| B | [Desc] | R$[X] | [Y] | [Z%] | R$[W] | [V]x |
| C | [Desc] | R$[X] | [Y] | [Z%] | R$[W] | [V]x |

- **Vencedor:** [Variação]
- **Melhoria:** [+X% em métrica principal]
- **Aprendizado:** [O que aprendemos]
- **Próximo teste:** [O que testar a seguir]
```

---

## 💼 LinkedIn Ads (Expandido)

### Sponsored Content - Especificações e Templates

**Especificações:**
| Formato | Imagem | Texto Introdutório | Headline | Descrição |
|---------|--------|---------------------|----------|-----------|
| Imagem Única | 1200x627 | 600 chars (150 visíveis) | 70 chars | 100 chars |
| Carrossel | 1080x1080 | 255 chars | 45 chars por card | - |
| Vídeo | 16:9 ou 1:1 | 600 chars | 70 chars | 100 chars |
| Documento (PDF) | - | 600 chars | 70 chars | - |

**Template - Sponsored Content (Geração de Leads B2B):**
```
TEXTO INTRODUTÓRIO:
{Estatística ou dado impactante do setor}

{Problema que o público-alvo enfrenta}

Criamos um {material/guia/relatório} com {número} {estratégias/insights/passos} para {resultado desejado}.

📥 Baixe gratuitamente.

HEADLINE: {Material} Gratuito: {Benefício Principal}
DESCRIÇÃO: {Complemento} para {cargo/setor}
CTA: Baixar
```

**Template - Sponsored Content (Thought Leadership):**
```
TEXTO INTRODUTÓRIO:
{Opinião forte ou insight contraintuitivo sobre o setor}

{Desenvolvimento do argumento em 2-3 frases}

Na {empresa}, vemos isso na prática: {exemplo ou dado interno}

Concorda? Comente abaixo 👇

HEADLINE: {Tema}: {Perspectiva Única}
CTA: Saiba Mais
```

### Sponsored InMail / Message Ads - Templates

**Especificações:**
| Elemento | Limite |
|----------|--------|
| Assunto | 60 chars |
| Corpo da mensagem | 1.500 chars |
| CTA Button | 20 chars |
| Banner (opcional) | 300x250 |

**Template - Convite para Webinar/Evento:**
```
ASSUNTO: {Nome}, convite exclusivo: {Tema do Webinar}

CORPO:
Olá {Nome},

Estamos organizando um webinar exclusivo sobre {tema} e achei que seria relevante para você, considerando sua atuação em {setor/cargo}.

📅 Data: {dia e horário}
⏱ Duração: {X} minutos
🎯 O que você vai aprender:
• {Tópico 1}
• {Tópico 2}
• {Tópico 3}

Vagas limitadas a {número} participantes.

CTA: Garantir Minha Vaga
```

**Template - Oferta de Conteúdo/Demo:**
```
ASSUNTO: {Solução} para {desafio do cargo/setor}

CORPO:
Olá {Nome},

Sei que profissionais de {cargo} frequentemente enfrentam {desafio específico}.

Na {empresa}, ajudamos empresas como {exemplo de cliente/setor} a {resultado alcançado}.

Preparamos um {material/demo} que mostra como {benefício principal} em {prazo}.

Sem compromisso — apenas {X} minutos do seu tempo.

CTA: Agendar Demo / Baixar Material
```

### Lead Gen Forms - Boas Práticas

- **Máximo de 3-4 campos** para taxas de conversão mais altas
- Campos recomendados: Nome, Email, Empresa, Cargo
- Usar campos pré-preenchidos do LinkedIn (aumenta conversão em até 30%)
- Incluir mensagem de agradecimento com link para o material
- Configurar integração automática com CRM (HubSpot, Salesforce, etc.)
- Testar formulários com e sem campo de telefone

### Opções de Segmentação B2B

| Critério | Exemplos | Quando Usar |
|----------|----------|-------------|
| **Cargo** | Diretor de Marketing, CEO, Head de Vendas | Quando o decisor é claro |
| **Senioridade** | VP, Diretor, Gerente | Para filtrar nível hierárquico |
| **Tamanho da empresa** | 1-50, 51-200, 201-500, 500+ | Para adequar oferta ao porte |
| **Setor/Indústria** | Tecnologia, Saúde, Financeiro | Para mensagem segmentada |
| **Habilidades** | Marketing Digital, Gestão de Projetos | Para perfis técnicos |
| **Grupos do LinkedIn** | Grupos específicos do setor | Para nichos bem definidos |
| **Empresa específica** | Lista de empresas-alvo (ABM) | Account-Based Marketing |

### Account-Based Marketing (ABM) no LinkedIn

**Estratégia em 3 Camadas:**

```
CAMADA 1 - AWARENESS (Semanas 1-2)
├── Sponsored Content com thought leadership
├── Segmentação: lista de empresas-alvo + cargos decisores
├── Objetivo: Impressões e engajamento
└── Orçamento: 30% do total

CAMADA 2 - CONSIDERAÇÃO (Semanas 3-4)
├── Conteúdo aprofundado (cases, whitepapers)
├── Segmentação: engajaram com Camada 1
├── Objetivo: Cliques e downloads
└── Orçamento: 40% do total

CAMADA 3 - CONVERSÃO (Semanas 5-6)
├── Message Ads com oferta direta (demo/reunião)
├── Segmentação: engajaram com Camada 2
├── Objetivo: Leads qualificados / reuniões agendadas
└── Orçamento: 30% do total
```

**Lista de empresas-alvo:**
- Fazer upload de lista CSV com nomes de empresas (mín. 300 recomendado)
- Combinar com filtro de cargo para atingir decisores
- Atualizar lista mensalmente com novas contas

### Recomendações de Orçamento para B2B

| Objetivo | Budget Diário Mínimo | CPL Esperado | CPC Médio |
|----------|----------------------|--------------|-----------|
| Awareness (Conteúdo) | R$ 80-150/dia | - | R$ 8-20 |
| Geração de Leads | R$ 150-300/dia | R$ 50-200 | R$ 15-35 |
| Message Ads | R$ 100-200/dia | R$ 80-250 | - |
| ABM (campanha completa) | R$ 300-500/dia | R$ 100-300 | R$ 20-50 |

**Observações importantes:**
- LinkedIn Ads tem CPC significativamente maior que Meta/Google Display
- Compensado pela qualidade superior dos leads B2B
- Recomendado mínimo de R$ 3.000/mês para resultados consistentes
- Ciclo de aprendizado mais longo: planejar campanhas de no mínimo 30 dias

---

## 🔗 Integração com Outros Subagentes

| Subagente | Integração |
|-----------|------------|
| **Copy Agent** | Headlines, CTAs, persuasão |
| **Video Agent** | Scripts para video ads |
| **AI Tools Agent** | Criativos com IA |
| **Analytics Agent** | Métricas, otimização |
| **Research Agent** | Públicos, concorrência |

---

*Última atualização: Janeiro 2026*
