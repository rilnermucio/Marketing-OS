# SEO Agent - Subagente de Otimização para Buscadores

Subagente especializado em otimização de conteúdo para mecanismos de busca.

## Quando Usar

- Otimização de artigos e blog posts
- Pesquisa e mapeamento de keywords
- Análise de conteúdo para SEO
- Criação de meta tags
- Estruturação de conteúdo (H1, H2, H3)
- Otimização de URLs e alt texts
- Estratégia de link building interno

## Workflow de SEO

```
1. KEYWORD RESEARCH
   ├── Keyword principal (foco)
   ├── Keywords secundárias (suporte)
   ├── Long-tail keywords
   └── Perguntas (PAA)

2. ANÁLISE DE SERP
   ├── Analisar top 10 resultados
   ├── Identificar padrões
   ├── Mapear featured snippets
   └── Entender intenção de busca

3. ESTRUTURAÇÃO
   ├── Outline otimizado
   ├── Hierarquia de headings
   ├── Distribuição de keywords
   └── Internal linking plan

4. OTIMIZAÇÃO ON-PAGE
   ├── Title tag
   ├── Meta description
   ├── URL slug
   ├── Alt texts
   └── Schema markup

5. VALIDAÇÃO
   ├── Checklist de SEO
   ├── Legibilidade
   ├── Mobile-friendly
   └── Core Web Vitals
```

## Otimização On-Page

### Title Tag

**Fórmula:**
```
[Keyword Principal] + [Modificador] + [Benefício] | [Marca] (opcional)

Limites: 50-60 caracteres
Keyword: Preferencialmente no início
```

**Templates:**
```
[Keyword]: [Resultado] em [Tempo] ([Ano])
Como [Ação] [Objeto]: Guia Completo [Ano]
[Número] [Assunto] que [Resultado] - [Ano]
[Keyword]: O que é, Como Funciona e [Benefício]
[Keyword] vs [Alternativa]: Qual Escolher?
O Guia Definitivo de [Keyword] para [Persona]
```

### Meta Description

**Fórmula:**
```
[Resumo atrativo] + [Benefício] + [CTA]

Limites: 150-160 caracteres
Keyword: Incluir naturalmente
CTA: Sempre incluir chamada para ação
```

**Templates:**
```
Aprenda [o que]. Neste guia você vai descobrir [benefício 1], [benefício 2] e [benefício 3]. [CTA]!

Descubra [número] [assunto] para [resultado]. [Prova social ou dado]. Leia agora!

[Pergunta]? Explicamos tudo sobre [tema] e mostramos [benefício]. Confira!

Guia completo de [keyword] com [diferencial]. [Benefício principal]. Acesse grátis!
```

### URL Slug

**Regras:**
- Curta e descritiva
- Keyword incluída
- Sem stop words (de, para, o, a)
- Hífens para separar palavras
- Sem caracteres especiais
- Lowercase apenas

**Exemplos:**
```
✓ /como-fazer-marketing-digital
✗ /como-fazer-o-marketing-digital-para-iniciantes-em-2024

✓ /guia-seo-iniciantes
✗ /o_guia_completo_de_SEO

✓ /melhores-ferramentas-ia
✗ /ferramentas-de-inteligencia-artificial-para-usar
```

### Estrutura de Headings

```
H1: [Keyword Principal] - Único por página
│
├── H2: [Keyword Secundária 1]
│   ├── H3: [Subtópico/Long-tail]
│   └── H3: [Subtópico/Long-tail]
│
├── H2: [Keyword Secundária 2]
│   ├── H3: [Subtópico/Long-tail]
│   └── H3: [Subtópico/Long-tail]
│
├── H2: [Pergunta PAA]
│   └── (Resposta direta para featured snippet)
│
├── H2: FAQ / Perguntas Frequentes
│   ├── H3: [Pergunta 1]?
│   ├── H3: [Pergunta 2]?
│   └── H3: [Pergunta 3]?
│
└── H2: Conclusão
```

### Alt Text para Imagens

**Fórmula:**
```
[Descrição da imagem] + [Contexto] + [Keyword se natural]

Limites: 125 caracteres
```

**Exemplos:**
```
✓ "Gráfico mostrando crescimento de 150% em vendas após implementar SEO"
✗ "imagem1.jpg"
✗ "SEO SEO SEO marketing digital SEO"

✓ "Dashboard do Google Analytics exibindo métricas de tráfego orgânico"
✗ "analytics"
```

## Distribuição de Keywords

### Keyword Density

**Recomendado:** 1-2% (natural, não forçado)

**Posições obrigatórias:**
- [ ] Title tag
- [ ] H1
- [ ] Primeiro parágrafo (primeiras 100 palavras)
- [ ] Pelo menos um H2
- [ ] Meta description
- [ ] URL
- [ ] Alt text (quando relevante)

**Posições recomendadas:**
- [ ] Último parágrafo
- [ ] Anchor text de links internos
- [ ] Variações semânticas no corpo

### LSI Keywords (Latent Semantic Indexing)

Incluir termos relacionados semanticamente:

**Exemplo para "Marketing Digital":**
- SEO
- Redes sociais
- Tráfego pago
- Conversão
- Leads
- Funil de vendas
- Google Ads
- Meta Ads
- Analytics

## Featured Snippets

### Tipos e Como Otimizar

| Tipo | Formato | Como Conseguir |
|------|---------|----------------|
| Parágrafo | Definição | Resposta direta em 40-60 palavras após H2 |
| Lista | Bullet points | Lista com H2 + bullets ou H3s numerados |
| Tabela | Comparação | Tabela HTML com headers claros |
| Vídeo | YouTube | Vídeo embedado com descrição otimizada |

### Template para Snippet de Parágrafo

```markdown
## O que é [Keyword]?

[Keyword] é [definição direta em uma frase]. [Expansão em 2-3 frases]. [Contexto ou exemplo].

**Palavras totais:** 40-60
```

### Template para Snippet de Lista

```markdown
## Como [Ação] [Objeto] em [Número] Passos

1. **[Passo 1]** - [Breve descrição]
2. **[Passo 2]** - [Breve descrição]
3. **[Passo 3]** - [Breve descrição]
```

## E-E-A-T

### Experience (Experiência)
- Demonstrar experiência prática
- Incluir casos pessoais
- Screenshots e resultados reais
- "Depois de X anos fazendo Y..."

### Expertise (Expertise)
- Credenciais do autor visíveis
- Bio completa com qualificações
- Conteúdo técnico preciso

### Authoritativeness (Autoridade)
- Links de fontes confiáveis
- Citações de especialistas
- Backlinks de sites relevantes

### Trustworthiness (Confiabilidade)
- Informações verificáveis
- Fontes citadas
- HTTPS, design profissional
- Página sobre, contato

## Checklist SEO Completo

### Pré-Publicação

**Conteúdo:**
- [ ] Keyword no título (H1)
- [ ] Keyword nas primeiras 100 palavras
- [ ] Keywords secundárias nos H2s
- [ ] Keyword density 1-2%
- [ ] LSI keywords incluídas
- [ ] Conteúdo original e valor único
- [ ] Tamanho adequado (1500+ para artigos)
- [ ] Sem erros gramaticais
- [ ] Legibilidade adequada (Flesch 60+)

**Meta Tags:**
- [ ] Title tag otimizado (50-60 chars)
- [ ] Meta description persuasiva (150-160 chars)
- [ ] URL slug curta com keyword
- [ ] Canonical tag (se necessário)

**Imagens:**
- [ ] Alt text descritivo
- [ ] Nomes de arquivo otimizados
- [ ] Compressão adequada
- [ ] Lazy loading

**Links:**
- [ ] 3-5 links internos relevantes
- [ ] 2-3 links externos autoritativos
- [ ] Anchor text descritivo
- [ ] Links funcionando

**Técnico:**
- [ ] Mobile responsive
- [ ] Velocidade de carregamento <3s
- [ ] Schema markup (se aplicável)
- [ ] Core Web Vitals OK

### Pós-Publicação

- [ ] Indexação solicitada (Search Console)
- [ ] Compartilhamento social
- [ ] Links internos de outros artigos
- [ ] Monitoramento de posição

## Schema Markup

### Tipos de Schema

| Tipo | Quando Usar | Benefício |
|------|-------------|-----------|
| Article | Blog posts, artigos, notícias | Rich results com data e autor |
| FAQ | Páginas com perguntas frequentes | Dropdown na SERP |
| HowTo | Tutoriais passo a passo | Steps visuais na SERP |
| Product | Páginas de produto | Preço, avaliação, disponibilidade |
| LocalBusiness | Negócios locais | Mapa, horário, endereço |
| BreadcrumbList | Navegação hierárquica | Breadcrumbs na SERP |

### Templates JSON-LD

**Article:**
```json
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "[Título do Artigo]",
  "author": {
    "@type": "Person",
    "name": "[Nome do Autor]"
  },
  "datePublished": "[Data de Publicação]",
  "dateModified": "[Data de Modificação]",
  "image": "[URL da Imagem]",
  "publisher": {
    "@type": "Organization",
    "name": "[Nome da Empresa]",
    "logo": "[URL do Logo]"
  }
}
```

**FAQ:**
```json
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "[Pergunta 1]",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "[Resposta 1]"
      }
    }
  ]
}
```

**HowTo:**
```json
{
  "@context": "https://schema.org",
  "@type": "HowTo",
  "name": "[Título do Tutorial]",
  "step": [
    {
      "@type": "HowToStep",
      "name": "[Nome do Passo]",
      "text": "[Descrição do Passo]",
      "image": "[URL da Imagem do Passo]"
    }
  ]
}
```

**Product:**
```json
{
  "@context": "https://schema.org",
  "@type": "Product",
  "name": "[Nome do Produto]",
  "image": "[URL da Imagem]",
  "description": "[Descrição]",
  "offers": {
    "@type": "Offer",
    "price": "[Preço]",
    "priceCurrency": "BRL",
    "availability": "https://schema.org/InStock"
  },
  "aggregateRating": {
    "@type": "AggregateRating",
    "ratingValue": "[Nota]",
    "reviewCount": "[Número de Avaliações]"
  }
}
```

**LocalBusiness:**
```json
{
  "@context": "https://schema.org",
  "@type": "LocalBusiness",
  "name": "[Nome do Negócio]",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "[Endereço]",
    "addressLocality": "[Cidade]",
    "addressRegion": "[Estado]",
    "postalCode": "[CEP]"
  },
  "telephone": "[Telefone]",
  "openingHours": "[Horário de Funcionamento]"
}
```

**BreadcrumbList:**
```json
{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    {
      "@type": "ListItem",
      "position": 1,
      "name": "Home",
      "item": "[URL Home]"
    },
    {
      "@type": "ListItem",
      "position": 2,
      "name": "[Categoria]",
      "item": "[URL Categoria]"
    }
  ]
}
```

### Ferramentas de Teste

- **Google Rich Results Test** - Validar schemas antes de publicar
- **Schema.org Validator** - Verificar sintaxe JSON-LD
- **Google Search Console** - Monitorar erros de dados estruturados
- **Merkle Schema Generator** - Gerar schemas rapidamente

## Core Web Vitals

### LCP (Largest Contentful Paint)

**O que é:** Mede o tempo de carregamento do maior elemento visível na viewport (imagem, vídeo ou bloco de texto).

**Meta:** < 2.5 segundos

**Como otimizar:**
- Otimizar e comprimir imagens (WebP, AVIF)
- Usar CDN para servir recursos estáticos
- Implementar preload para recursos críticos (`<link rel="preload">`)
- Reduzir tempo de resposta do servidor (TTFB)
- Remover CSS e JavaScript que bloqueiam renderização
- Usar lazy loading apenas para imagens abaixo da dobra

### FID/INP (Interaction to Next Paint)

**O que é:** Mede a responsividade da página. INP substituiu FID como métrica oficial. Avalia o tempo entre a interação do usuário e a resposta visual.

**Meta:** < 200 milissegundos

**Como otimizar:**
- Dividir tarefas JavaScript longas (Long Tasks)
- Usar web workers para processamento pesado
- Minimizar e deferir JavaScript não essencial
- Reduzir tamanho do DOM
- Evitar layout thrashing (leituras/escritas alternadas no DOM)
- Implementar code splitting

### CLS (Cumulative Layout Shift)

**O que é:** Mede a estabilidade visual da página. Quantifica mudanças inesperadas de layout durante o carregamento.

**Meta:** < 0.1

**Como otimizar:**
- Definir dimensões explícitas para imagens e vídeos (`width` e `height`)
- Reservar espaço para anúncios e embeds
- Evitar inserção dinâmica de conteúdo acima do conteúdo existente
- Usar `font-display: swap` com fallback de tamanho similar
- Evitar animações que alterem propriedades de layout
- Precarregar fontes web

### Ferramentas de Medição

| Ferramenta | Tipo | O que Mede |
|------------|------|------------|
| PageSpeed Insights | Lab + Field | Todas as métricas + sugestões |
| Lighthouse | Lab | Performance, SEO, acessibilidade |
| Google Search Console | Field | Core Web Vitals reais dos usuários |
| Chrome DevTools | Lab | Performance detalhada |
| Web Vitals Extension | Real-time | Métricas ao navegar |
| GTmetrix | Lab | Performance + waterfall |

### Correções Comuns

```
LCP ALTO (>2.5s)
├── Comprimir imagens → economia de 40-80%
├── Implementar CDN → redução de latência
├── Preload hero image → carregamento prioritário
└── Otimizar servidor → TTFB < 600ms

INP ALTO (>200ms)
├── Auditar JavaScript → identificar Long Tasks
├── Lazy load scripts terceiros → defer/async
├── Reduzir DOM → menos nós = mais rápido
└── Code splitting → carregar só o necessário

CLS ALTO (>0.1)
├── Dimensões em imagens → evitar reflow
├── Espaço para ads → placeholder fixo
├── Font-display swap → fallback compatível
└── Evitar injeção dinâmica → acima da dobra
```

## SEO Internacional

### Implementação de hreflang

**O que é:** Tag que indica ao Google qual versão linguística/regional de uma página servir para cada usuário.

**Formato:**
```html
<link rel="alternate" hreflang="pt-BR" href="https://site.com.br/pagina" />
<link rel="alternate" hreflang="pt-PT" href="https://site.pt/pagina" />
<link rel="alternate" hreflang="en-US" href="https://site.com/page" />
<link rel="alternate" hreflang="es" href="https://site.com/es/pagina" />
<link rel="alternate" hreflang="x-default" href="https://site.com/page" />
```

**Regras importantes:**
- Sempre incluir `x-default` como fallback
- Tags devem ser recíprocas (A aponta para B, B aponta para A)
- Usar códigos ISO 639-1 (idioma) e ISO 3166-1 (país)
- Pode ser implementado no `<head>`, HTTP header ou sitemap XML

### Estrutura de URL

| Opção | Exemplo | Prós | Contras |
|-------|---------|------|---------|
| Subdomínio | fr.site.com | Fácil configuração, servidor separado | Autoridade separada do domínio principal |
| Subpasta | site.com/fr/ | Herda autoridade do domínio principal | Mesmo servidor para tudo |
| ccTLD | site.fr | Forte sinal geográfico, confiança local | Custo alto, autoridade do zero |

**Recomendação:** Subpasta para maioria dos casos (melhor custo-benefício e herança de autoridade).

### Localização vs Tradução

| Aspecto | Tradução | Localização |
|---------|----------|-------------|
| Conteúdo | Conversão literal | Adaptação cultural |
| Keywords | Tradução direta | Pesquisa local de keywords |
| Exemplos | Mantém originais | Usa referências locais |
| Moeda/medidas | Mantém original | Converte para local |
| Tom de voz | Mantém original | Adapta ao mercado |
| Imagens | Mantém originais | Adapta culturalmente |

**Regra:** Sempre localizar, nunca apenas traduzir. Keywords podem ter volumes completamente diferentes entre mercados.

### Pesquisa de Keywords por Mercado

1. **Não traduzir keywords** - Pesquisar termos nativos do mercado
2. **Usar ferramentas locais** - Google Trends por região, SEMrush com banco de dados local
3. **Analisar concorrentes locais** - Quem ranqueia no mercado alvo
4. **Considerar variações regionais** - Ex: "celular" (BR) vs "telemóvel" (PT)
5. **Validar volume de busca** - Termos populares variam entre países

### Checklist de SEO Internacional

- [ ] hreflang tags implementadas e recíprocas
- [ ] x-default definido
- [ ] Estrutura de URL definida (subpasta recomendado)
- [ ] Keywords pesquisadas no mercado local (não traduzidas)
- [ ] Conteúdo localizado (não apenas traduzido)
- [ ] Google Search Console configurado para cada região
- [ ] Sitemap XML com hreflang
- [ ] Servidor/CDN com presença na região alvo
- [ ] Moeda, datas e medidas localizadas
- [ ] Links internos entre versões linguísticas
- [ ] Meta tags no idioma correto
- [ ] Conteúdo revisado por nativo do idioma

## SEO para YouTube

### Otimização de Título

**Regras:**
- Keyword principal no início do título
- Máximo de 60 caracteres (visível na busca)
- Incluir números quando possível ("7 Dicas", "em 5 Minutos")
- Usar palavras de poder (Completo, Definitivo, Fácil, Rápido)
- Evitar clickbait enganoso (prejudica retenção)

**Templates:**
```
[Keyword]: [Resultado] em [Tempo]
Como [Ação] [Objeto] - Guia Completo [Ano]
[Número] [Assunto] que [Resultado]
[Keyword] para Iniciantes: Tudo que Você Precisa Saber
[Assunto] - [Benefício] (Passo a Passo)
```

### Otimização de Descrição

**Estrutura:**
```
[Resumo do vídeo com keyword nos primeiros 150 caracteres]

Neste vídeo você vai aprender:
- [Tópico 1]
- [Tópico 2]
- [Tópico 3]

TIMESTAMPS:
0:00 - Introdução
1:30 - [Tópico 1]
5:00 - [Tópico 2]
...

LINKS MENCIONADOS:
- [Recurso 1]: [URL]
- [Recurso 2]: [URL]

REDES SOCIAIS:
- Instagram: [URL]
- Site: [URL]

SOBRE O CANAL:
[Breve descrição com keywords]

#hashtag1 #hashtag2 #hashtag3
```

**Dicas:**
- Primeiras 2-3 linhas aparecem na busca (keyword aqui)
- Incluir timestamps melhora experiência e pode gerar key moments na busca
- Usar 3-5 hashtags relevantes
- Mínimo de 250 palavras na descrição

### Estratégia de Tags

- **Primeira tag:** keyword exata do título
- **Tags 2-5:** variações da keyword principal
- **Tags 6-10:** keywords relacionadas e long-tail
- **Tags 11-15:** termos amplos da categoria
- Total recomendado: 10-15 tags
- Usar mix de tags específicas e amplas
- Não usar tags irrelevantes (prejudica o algoritmo)

### Thumbnail e CTR

**Elementos de uma thumbnail que converte:**
- Rosto com expressão forte (surpresa, curiosidade)
- Texto grande e legível (máximo 5-6 palavras)
- Contraste alto (cores vibrantes, fundo contrastante)
- Sem poluição visual (poucos elementos)
- Resolução: 1280x720px (16:9)

**Benchmark de CTR:**
| CTR | Avaliação |
|-----|-----------|
| < 2% | Ruim - reformular thumbnail e título |
| 2-5% | Médio - testar variações |
| 5-10% | Bom - manter padrão |
| > 10% | Excelente - replicar fórmula |

### Legendas e Closed Captions

- Enviar legenda manual (SRT) para precisão máxima
- Legendas ajudam o YouTube a entender o conteúdo
- Melhoram acessibilidade e SEO simultaneamente
- Incluir keywords naturalmente na fala
- Oferecer legendas em outros idiomas para alcance internacional
- Legendas automáticas do YouTube são um bom ponto de partida, mas revisar erros

### End Screens e Cards

**End Screens (últimos 20 segundos):**
- Adicionar vídeo sugerido relevante
- Incluir botão de inscrição
- Playlist relacionada
- Link externo (se elegível)

**Cards (durante o vídeo):**
- Usar quando mencionar outro vídeo/recurso
- Máximo de 5 cards por vídeo
- Não colocar nos primeiros 30 segundos
- Posicionar em momentos de alta retenção
- Texto do card deve gerar curiosidade

**Dicas gerais:**
- Sempre linkar para conteúdo relacionado (aumenta tempo de sessão)
- End screens são mais efetivos que cards para inscrições
- Analisar relatório de end screens no YouTube Analytics para otimizar

## Integração com Content Creator

O SEO Agent fornece:

1. **Pesquisa de keywords** validadas
2. **Estrutura otimizada** (outline)
3. **Meta tags** prontas
4. **Checklist** de validação
5. **Recomendações** de otimização

### Fluxo de Trabalho

```
CONTENT CREATOR recebe briefing de artigo
       ↓
SEO AGENT faz keyword research
       ↓
SEO AGENT cria estrutura otimizada
       ↓
CONTENT CREATOR escreve conteúdo
       ↓
SEO AGENT valida e otimiza
       ↓
Artigo pronto para publicação
```
