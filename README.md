# :dart: Marketing OS

Marketing OS — sistema operacional completo de marketing digital. Projetado para funcionar como skill do Claude Code.

[![GitHub](https://img.shields.io/badge/GitHub-rilnermucio%2FAgents-blue?logo=github)](https://github.com/rilnermucio/Agents.git)
[![Python](https://img.shields.io/badge/Python-3.8%2B-yellow?logo=python)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

## :clipboard: Visão Geral

O **Marketing OS** é um sistema operacional de marketing digital composto por **17 subagentes especializados**, **23 comandos**, **15 clones de voz**, **8 workflows** e **23 scripts** que trabalham em conjunto para criar conteúdo estratégico de alta qualidade. Ele cobre:

- **Redes sociais**: Instagram (feed, carrossel, reels, stories), LinkedIn, Twitter/X, TikTok, YouTube, Pinterest, Facebook
- **Messaging**: WhatsApp Business, Telegram, DM automation
- **Marketing**: Email marketing, newsletters, sequências de automação multi-canal
- **SEO**: Artigos otimizados, blog posts, meta tags, featured snippets
- **Vídeo**: Scripts YouTube, Reels/TikTok/Shorts, VSL, webinars
- **Áudio**: Roteiros de podcast, spots publicitários
- **Anúncios**: Copy para Meta Ads, Google Ads, TikTok Ads, LinkedIn Ads + publicação direta via MCP
- **Landing pages**: Páginas de vendas, captura de leads, webinar registration
- **Funis**: Lead gen, product launch, webinar, tripwire, evergreen
- **Infoprodutos**: Ebooks, cursos, memberships, workshops, mentorias
- **IA generativa**: Prompts para geração de imagens e vídeos com IA
- **Integrações MCP**: Notion, Meta Ads, Playwright (screenshots), Figma (design briefs)

Suporta **10+ nichos** com personas, pilares de conteúdo, hooks e hashtags específicos para cada um.

## :building_construction: Arquitetura

```
MARKETING OS (Agente Principal)
|
+-- :mag: RESEARCH AGENT        - Pesquisa de tendências, concorrência, keywords
+-- :pencil2: COPY AGENT            - Headlines, CTAs, copy persuasivo, variações A/B
+-- :mag_right: SEO AGENT             - Otimização on-page, estruturação, E-E-A-T
+-- :iphone: SOCIAL AGENT          - Posts por plataforma, hashtags, timing
+-- :clapper: VIDEO AGENT           - Scripts YouTube, Reels, TikTok, VSL
+-- :robot: AI TOOLS AGENT        - Prompts para imagem e vídeo com IA
+-- :bar_chart: ANALYTICS AGENT      - Métricas, relatórios, testes A/B
+-- :studio_microphone: AUDIO AGENT          - Podcasts, roteiros de áudio, spots
+-- :envelope: EMAIL AGENT           - Sequências de email, newsletters
+-- :loudspeaker: ADS AGENT            - Copy de anúncios Meta/Google/TikTok/LinkedIn
+-- :art: DESIGN AGENT          - Design visual, paletas de cores, identidade
+-- :crown: BRAND AGENT           - Identidade de marca, posicionamento, tom de voz
+-- :book: STORYTELLING AGENT    - Narrativas, storytelling, arcos de história
+-- :funnel_web: FUNNEL AGENT          - Funis de vendas, jornada do cliente
+-- :chart_with_upwards_trend: GROWTH AGENT          - Crescimento, growth hacking, aquisição
+-- :rocket: LAUNCH AGENT          - Lançamentos de produtos e campanhas
+-- :package: INFOPRODUCT BUILDER  - Infoprodutos, cursos, ebooks, memberships
```

## :open_file_folder: Estrutura do Projeto

```
Marketing OS/
|
+-- Skill.md                          # Arquivo principal da skill (Claude Code)
+-- plugin.json                       # Metadados do plugin para marketplace
+-- README.md                         # Este arquivo
+-- GUIA-DE-USO.md                    # Guia completo de uso do agente
+-- INSTALACAO-SKILL.md               # Instruções de instalação da skill
+-- requirements.txt                  # Dependências Python
+-- .gitignore
|
+-- skills/                           # Skills para Claude Cowork marketplace
|   +-- marketing-os/              # Skill principal
|       +-- SKILL.md                  # Definição da skill
|       +-- (symlinks para pastas)
|
+-- subagents/                        # 17 subagentes especializados
|   +-- research-agent.md
|   +-- copy-agent.md
|   +-- seo-agent.md
|   +-- social-agent.md
|   +-- video-agent.md
|   +-- ai-tools-agent.md
|   +-- analytics-agent.md
|   +-- audio-agent.md
|   +-- email-agent.md
|   +-- ads-agent.md
|   +-- design-agent.md
|   +-- brand-agent.md
|   +-- storytelling-agent.md
|   +-- funnel-agent.md
|   +-- growth-agent.md
|   +-- launch-agent.md
|   +-- infoproduct-builder-agent.md
|
+-- scripts/                          # 23 scripts de automação
|   +-- seo_analyzer.py
|   +-- hashtag_generator.py
|   +-- content_calendar.py
|   +-- ab_generator.py
|   +-- headline_scorer.py
|   +-- readability_checker.py
|   +-- content_repurposer.py
|   +-- hook_generator.py
|   +-- hook_variant_generator.py
|   +-- content_idea_generator.py
|   +-- caption_generator.py
|   +-- carousel_structure_generator.py
|   +-- reels_script_generator.py
|   +-- instagram_hashtag_research.py
|   +-- competitor_analyzer.py
|   +-- content_audit.py
|   +-- trend_tracker.py
|   +-- trend_adapter.py
|   +-- tiktok_trends_scraper.py
|   +-- project_manager.py               # NOVO: Gerenciador de projetos
|   +-- quality_gate.py                   # NOVO: Quality gate para outputs
|   +-- mos.py                            # NOVO: CLI unificado
|
+-- assets/
|   +-- templates/                    # 26 templates de conteúdo
|   |   +-- artigo-seo.md
|   |   +-- email-newsletter.md
|   |   +-- post-linkedin.md
|   |   +-- post-instagram-carrossel.md
|   |   +-- instagram-feed-post.md    # NOVO
|   |   +-- instagram-stories.md      # NOVO
|   |   +-- youtube-script.md
|   |   +-- youtube-shorts.md         # NOVO
|   |   +-- reels-tiktok-script.md
|   |   +-- reels-audio-strategy.md   # NOVO
|   |   +-- vsl-script.md
|   |   +-- podcast-episode.md
|   |   +-- podcast-ad-reads.md       # NOVO
|   |   +-- twitter-thread.md
|   |   +-- pinterest-pins.md         # NOVO
|   |   +-- press-release.md
|   |   +-- case-study.md
|   |   +-- whitepaper.md
|   |   +-- webinar-script.md
|   |   +-- sales-page.md
|   |   +-- lead-magnet.md
|   |   +-- ugc-brief.md
|   |   +-- carrossel-thumbnail-mastery.md  # NOVO
|   |   +-- card-unico-niche-templates.md   # NOVO
|   |   +-- pesquisa-tiktok-trends.md       # NOVO
|   |   +-- meus-templates.md               # NOVO: Templates personalizados
|   |
|   +-- swipe-files/                  # Banco de referências e exemplos
|   |   +-- headlines-virais.md
|   |   +-- hooks-reels.md
|   |   +-- ctas-conversão.md
|   |   +-- emails-conversão.md
|   |   +-- copy-carrossel.md
|   |   +-- bios-instagram.md
|   |   +-- transicoes-reels.md       # NOVO
|   |   +-- trends-adaptáveis.md      # NOVO
|   |   +-- paletas-cores.md          # NOVO
|   |
|   +-- personas/                     # Templates e personas por nicho
|   |   +-- persona-template.md
|   |   +-- personas-por-nicho.md
|   |
|   +-- checklists/
|   |   +-- pre-publicacao.md
|   |
|   +-- prompts/
|       +-- prompt-biblioteca.md
|       +-- prompts-imagem-ia.md      # NOVO: Prompts para geração de imagens
|       +-- prompts-post-pronto.md    # NOVO: Prompts para posts prontos
|
+-- references/                       # Guias de referência por tipo
|   +-- niches.md
|   +-- strategy.md
|   +-- social-media.md
|   +-- blog-seo.md
|   +-- email-marketing.md
|   +-- landing-pages.md
|   +-- ads-copy.md
|   +-- design-specs.md               # NOVO: Especificações de design
|
+-- workflows/                        # 8 workflows de campanha
|   +-- lancamento-produto.md
|   +-- calendario-mensal.md
|   +-- campanha-conversao.md
|   +-- funil-vendas.md
|   +-- parceria-influencer.md
|   +-- batch-production-workflow.md
|   +-- tiktok-trends-chrome.md
|   +-- content-pipeline.md             # NOVO: Pipeline de conteúdo
|
+-- outputs/                          # Conteúdo gerado
|
+-- skill-package/                    # Skill empacotada para distribuição
    +-- marketing-os/
```

## :robot: Subagentes

| Subagente | Arquivo | Descrição |
|-----------|---------|-----------|
| Research Agent | `subagents/research-agent.md` | Pesquisa de tendências, análise de concorrência, keyword research, mapeamento de audiência |
| Copy Agent | `subagents/copy-agent.md` | Headlines, hooks, CTAs otimizados, copy de vendas, variações A/B, neuromarketing |
| SEO Agent | `subagents/seo-agent.md` | Otimização on-page, estruturação de conteúdo, meta tags, E-E-A-T |
| Social Agent | `subagents/social-agent.md` | Posts por plataforma, adaptação cross-platform, hashtags, timing, algoritmos |
| Video Agent | `subagents/video-agent.md` | Scripts YouTube (long-form), Reels/TikTok/Shorts, VSL, hooks de retenção |
| AI Tools Agent | `subagents/ai-tools-agent.md` | Prompts para imagem (Midjourney, DALL-E, Flux) e vídeo (Veo 3.1, Sora 2, Kling) |
| Analytics Agent | `subagents/analytics-agent.md` | Métricas por plataforma, relatórios, análise de performance, testes A/B |
| Audio Agent | `subagents/audio-agent.md` | Roteiros de podcast (solo, entrevista, co-host), spots, audiobooks |
| Email Agent | `subagents/email-agent.md` | Sequências de email, newsletters, automações de marketing |
| Ads Agent | `subagents/ads-agent.md` | Copy de anúncios Meta/Google/TikTok/LinkedIn, estratégia de ads |
| Design Agent | `subagents/design-agent.md` | Design visual, paletas de cores, identidade de marca, layouts |
| Brand Agent | `subagents/brand-agent.md` | Identidade de marca, posicionamento, tom de voz |
| Storytelling Agent | `subagents/storytelling-agent.md` | Narrativas, storytelling, arcos de história |
| Funnel Agent | `subagents/funnel-agent.md` | Funis de vendas, jornada do cliente |
| Growth Agent | `subagents/growth-agent.md` | Crescimento, growth hacking, aquisição |
| Launch Agent | `subagents/launch-agent.md` | Lançamentos de produtos e campanhas |
| Infoproduct Builder Agent | `subagents/infoproduct-builder-agent.md` | Infoprodutos, cursos, ebooks, memberships, workshops |

## :speech_balloon: Comandos (23 comandos)

Comandos invocáveis via `/comando` ou linguagem natural:

### Criação de Conteúdo

| Comando | Descrição |
|---------|-----------|
| `/criar-post` | Posts para Instagram, LinkedIn, Twitter/X, TikTok |
| `/criar-carrossel` | Carrosséis de Instagram com estrutura completa |
| `/criar-artigo` | Artigos SEO otimizados para blog |
| `/criar-email` | Sequências de email marketing e newsletters |
| `/criar-video` | Scripts de vídeo para YouTube, Reels, TikTok, VSL |
| `/criar-podcast` | Roteiros de podcast (solo, entrevista, co-host) |
| `/criar-anuncio` | Copy para anúncios Meta/Google/TikTok/LinkedIn |
| `/criar-calendario` | Calendários editoriais multi-plataforma |
| `/gerar-imagem` | Prompts para geração de imagens com IA |
| `/criar-landing-page` | Landing pages (vendas, captura, webinar, waitlist) |
| `/criar-webinar` | Scripts de webinar + emails + slides outline |
| `/criar-sequencia` | Sequências multi-canal coordenadas |

### Estratégia e Análise

| Comando | Descrição |
|---------|-----------|
| `/criar-funil` | Funis de vendas completos (lead gen, launch, evergreen) |
| `/criar-infoproduto` | Infoprodutos (ebook, curso, membership, workshop) |
| `/analisar-video` | Análise de vídeos (hooks, retenção, CTAs, engagement) |
| `/analisar-concorrencia` | Análise competitiva e benchmarking |
| `/clonar-estrategia` | Reverse-engineering de estratégias de marketing |
| `/batch` | Produção em lote de conteúdo |

### Clones e Marca

| Comando | Descrição |
|---------|-----------|
| `/criar-clone` | Criar clone de voz de um expert |
| `/criar-brief-design` | Briefs de design para Figma (cores, tipografia, specs) |

### Integrações e Publicação

| Comando | Descrição |
|---------|-----------|
| `/publicar-notion` | Publicar calendários e conteúdo no Notion via MCP |
| `/publicar-anuncio` | Criar e publicar campanhas no Meta Ads via MCP |
| `/capturar-tela` | Capturar screenshots de sites via Playwright MCP |

## :speaking_head: Sistema de Clones de Voz (15 clones)

Clones de voz que adaptam tom, hooks e CTAs para diferentes estilos:

### Copywriters Clássicos

| Clone | Especialidade |
|-------|--------------|
| Alex Hormozi | Business offers, lead generation, scaling |
| David Ogilvy | Brand advertising, headlines, research-driven copy |
| Gary Halbert | Direct response, sales letters, emotional copy |
| Eugene Schwartz | Market awareness, sophistication levels |
| Russell Brunson | Funnels, webinars, storytelling frameworks |

### Storytellers

| Clone | Especialidade |
|-------|--------------|
| Donald Miller | StoryBrand framework, narrativa centrada no cliente |
| Park Howell | ABT framework, business storytelling |

### Criadores de Conteúdo

| Clone | Especialidade |
|-------|--------------|
| MrBeast | Conteúdo viral, retenção extrema, thumbnails |
| Ali Abdaal | Conteúdo educativo, produtividade, lifestyle |
| Gary Vaynerchuk | Social media, personal branding, attention economy |
| Iman Gadzhi | Agency building, high-ticket, education business |

### Growth e Marketing

| Clone | Especialidade |
|-------|--------------|
| Sean Ellis | Growth hacking, experimentação, product-market fit |
| Andrew Chen | Network effects, viral loops, marketplace growth |
| Neil Patel | SEO, digital marketing, content marketing, analytics |
| Leila Hormozi | Operations, team building, scaling, leadership |

## :page_facing_up: Templates Disponíveis (26 templates)

### Redes Sociais

| Template | Arquivo | Descrição |
|----------|---------|-----------|
| Post Instagram Carrossel | `assets/templates/post-instagram-carrossel.md` | Template de carrossel Instagram |
| Instagram Feed Post | `assets/templates/instagram-feed-post.md` | Posts para feed do Instagram |
| Instagram Stories | `assets/templates/instagram-stories.md` | Templates de stories interativos |
| Carrossel Thumbnail Mastery | `assets/templates/carrossel-thumbnail-mastery.md` | Capas de carrossel de alto impacto |
| Card Único por Nicho | `assets/templates/card-unico-niche-templates.md` | Templates de card único por nicho |
| Post LinkedIn | `assets/templates/post-linkedin.md` | Estrutura de post para LinkedIn |
| Twitter Thread | `assets/templates/twitter-thread.md` | Threads virais para Twitter/X |
| Pinterest Pins | `assets/templates/pinterest-pins.md` | Pins e Idea Pins otimizados |

### Vídeo

| Template | Arquivo | Descrição |
|----------|---------|-----------|
| YouTube Script | `assets/templates/youtube-script.md` | Roteiros completos para vídeos longos |
| YouTube Shorts | `assets/templates/youtube-shorts.md` | Scripts para Shorts otimizados |
| Reels/TikTok Script | `assets/templates/reels-tiktok-script.md` | Scripts para vídeos curtos (15s, 30s, 60s) |
| Reels Audio Strategy | `assets/templates/reels-audio-strategy.md` | Estratégia de áudio para Reels virais |
| VSL Script | `assets/templates/vsl-script.md` | Vídeo Sales Letter completo |
| Pesquisa TikTok Trends | `assets/templates/pesquisa-tiktok-trends.md` | Metodologia de pesquisa de trends |

### Áudio e Podcast

| Template | Arquivo | Descrição |
|----------|---------|-----------|
| Podcast Episode | `assets/templates/podcast-episode.md` | Estrutura de episódio de podcast |
| Podcast Ad Reads | `assets/templates/podcast-ad-reads.md` | Scripts de anúncios para podcasts |

### Conteúdo Escrito

| Template | Arquivo | Descrição |
|----------|---------|-----------|
| Artigo SEO | `assets/templates/artigo-seo.md` | Estrutura completa para artigos otimizados |
| Email Newsletter | `assets/templates/email-newsletter.md` | Template de newsletter por email |
| Press Release | `assets/templates/press-release.md` | Comunicados de imprensa |
| Case Study | `assets/templates/case-study.md` | Estudos de caso |
| Whitepaper | `assets/templates/whitepaper.md` | Conteúdo B2B aprofundado |

### Vendas e Conversão

| Template | Arquivo | Descrição |
|----------|---------|-----------|
| Webinar Script | `assets/templates/webinar-script.md` | Roteiro completo de webinar/live de vendas |
| Sales Page | `assets/templates/sales-page.md` | Estrutura de página de vendas |
| Lead Magnet | `assets/templates/lead-magnet.md` | Templates de iscas digitais |
| UGC Brief | `assets/templates/ugc-brief.md` | Briefing para criadores UGC |

### Personalizados

| Template | Arquivo | Descrição |
|----------|---------|-----------|
| Meus Templates | `assets/templates/meus-templates.md` | Templates personalizados do usuário |

## :wrench: Scripts de Automação (23 scripts)

### Análise e Otimização

| Script | Descrição | Comando |
|--------|-----------|---------|
| `seo_analyzer.py` | Analisa e otimiza conteúdo para SEO com score 0-100 | `python scripts/seo_analyzer.py arquivo.md "keyword"` |
| `readability_checker.py` | Analisa legibilidade com Flesch adaptado para português | `python scripts/readability_checker.py --file artigo.txt` |
| `headline_scorer.py` | Pontua headlines por poder emocional e clareza (0-100) | `python scripts/headline_scorer.py "Sua headline aqui"` |
| `content_audit.py` | Audita conteúdo existente e sugere melhorias | `python scripts/content_audit.py arquivo.md --tipo blog` |
| `competitor_analyzer.py` | Analisa perfis de concorrentes e extrai insights | `python scripts/competitor_analyzer.py "@perfil1" "@perfil2"` |

### Geração de Conteúdo

| Script | Descrição | Comando |
|--------|-----------|---------|
| `hook_generator.py` | Gera hooks virais para vídeos e posts | `python scripts/hook_generator.py "tema" reels 10` |
| `hook_variant_generator.py` | Gera múltiplas variações de hooks por formato | `python scripts/hook_variant_generator.py "tema" --formato reels` |
| `content_idea_generator.py` | Gera ideias de conteúdo por nicho e pilares | `python scripts/content_idea_generator.py tecnologia 20` |
| `ab_generator.py` | Gera variações de copy para testes A/B | `python scripts/ab_generator.py headline "texto original"` |
| `caption_generator.py` | Gera legendas otimizadas para Instagram por objetivo | `python scripts/caption_generator.py "tema" engajamento` |

### Instagram e Redes Sociais

| Script | Descrição | Comando |
|--------|-----------|---------|
| `hashtag_generator.py` | Gera hashtags relevantes por nicho e plataforma | `python scripts/hashtag_generator.py nicho plataforma` |
| `instagram_hashtag_research.py` | Pesquisa avançada de hashtags com estratégias | `python scripts/instagram_hashtag_research.py "nicho" --gerar-set` |
| `carousel_structure_generator.py` | Gera estruturas completas de carrossel | `python scripts/carousel_structure_generator.py "tema" educativo 10` |
| `reels_script_generator.py` | Gera roteiros para Reels com timestamps | `python scripts/reels_script_generator.py "tema" 30 tutorial` |

### Planejamento e Calendário

| Script | Descrição | Comando |
|--------|-----------|---------|
| `content_calendar.py` | Cria calendário editorial para múltiplas plataformas | `python scripts/content_calendar.py 2026-02-01 4 instagram linkedin` |
| `content_repurposer.py` | Adapta conteúdo entre plataformas automaticamente | `python scripts/content_repurposer.py --file artigo.txt --output todos` |

### Tendências e Trends

| Script | Descrição | Comando |
|--------|-----------|---------|
| `trend_tracker.py` | Monitora tendências via Google Trends, Reddit, YouTube | `python scripts/trend_tracker.py "termo" google,reddit --periodo 7` |
| `trend_adapter.py` | Adapta trends virais para diferentes nichos | `python scripts/trend_adapter.py "get ready with me" marketing` |
| `tiktok_trends_scraper.py` | Busca videos virais do TikTok por hashtag | `python scripts/tiktok_trends_scraper.py --hashtag "marketing" --min-views 1000000` |

### Projetos e Qualidade

| Script | Descrição | Comando |
|--------|-----------|---------|
| `project_manager.py` | Gerencia projetos e campanhas com estado persistente | `python scripts/project_manager.py create "Nome" --type launch` |
| `quality_gate.py` | Verifica qualidade de outputs (hook, CTA, SEO, readability) | `python scripts/quality_gate.py output.md --type post` |

### CLI Unificado

| Script | Descrição | Comando |
|--------|-----------|---------|
| `mos.py` | CLI unificado para todos os scripts do Marketing OS | `python scripts/mos.py seo analyze artigo.md "keyword"` |

**Comandos do CLI `mos`:**
```bash
python scripts/mos.py seo analyze artigo.md "keyword"     # Análise SEO
python scripts/mos.py headlines score "Sua headline"       # Pontuar headline
python scripts/mos.py hooks generate "tema" reels 10       # Gerar hooks
python scripts/mos.py hashtags generate nicho instagram    # Gerar hashtags
python scripts/mos.py calendar create 2026-03-01 4         # Calendário editorial
python scripts/mos.py quality check output.md --type post  # Quality gate
python scripts/mos.py project create "Nome" --type launch  # Criar projeto
python scripts/mos.py project list                         # Listar projetos
```

## :iphone: Plataformas Suportadas

- **Instagram** - Feed, Carrossel, Reels, Stories
- **LinkedIn** - Posts, Artigos, Newsletter
- **Twitter/X** - Tweets, Threads
- **TikTok** - Vídeos curtos, Lives
- **YouTube** - Vídeos long-form, Shorts
- **Pinterest** - Pins, Idea Pins
- **Facebook** - Posts, Stories, Grupos
- **WhatsApp Business** - Listas de transmissão, automação, templates
- **Telegram** - Canais e grupos
- **Email** - Newsletters, Sequências, Automações
- **Blog/SEO** - Artigos otimizados, Landing pages
- **Podcast** - Episódios, Show notes
- **Anúncios** - Meta Ads, Google Ads, TikTok Ads, LinkedIn Ads

## :dart: Nichos Suportados

| Nicho | Foco Principal | Tom Sugerido |
|-------|----------------|--------------|
| Inteligência Artificial | Ferramentas, tutoriais, tendências | Educativo, acessível |
| Desenvolvimento Pessoal | Mindset, hábitos, propósito | Inspiracional, empático |
| Desenvolvimento Profissional | Carreira, skills, liderança | Profissional, prático |
| Tecnologia/Programação | Código, tutoriais, carreira tech | Técnico, didático |
| Empreendedorismo | Negócios, vendas, escala | Motivador, estratégico |
| Finanças Pessoais | Investimentos, renda, organização | Educativo, confiável |
| Saúde e Bem-Estar | Exercício, nutrição, saúde mental | Acolhedor, motivador |
| Educação | Estudos, aprendizado, concursos | Didático, encorajador |
| Produtividade | Tempo, foco, ferramentas | Prático, direto |
| Marketing Digital | Estratégias, ferramentas, métricas | Autoridade, data-driven |

## :rocket: Como Usar

### Como Skill do Claude Code

1. **Configure como skill** no Claude Code apontando para o arquivo `Skill.md`
2. **O agente será acionado automaticamente** quando detectar triggers como: conteúdo, marketing, post, blog, SEO, newsletter, copy, landing page, campanha, anúncio, Instagram, LinkedIn, TikTok, vídeo, YouTube, Reels, podcast, VSL
3. **Exemplo de uso**:

```
Você: "Crie um carrossel para Instagram sobre produtividade com IA"

O agente automaticamente:
1. Consulta o nicho (IA + Produtividade)
2. Aciona o Social Agent para formato Instagram
3. Aciona o Copy Agent para headlines e CTAs
4. Usa templates de carrossel
5. Gera hashtags relevantes
6. Entrega conteúdo pronto com variações A/B
```

### Scripts Python

Todos os scripts podem ser executados independentemente via terminal:

```bash
# Analisar SEO de um artigo
python scripts/seo_analyzer.py artigo.md "marketing digital"

# Gerar hashtags para um nicho
python scripts/hashtag_generator.py marketing_digital instagram

# Criar calendário editorial de 4 semanas
python scripts/content_calendar.py 2026-02-01 4 instagram linkedin tiktok

# Gerar variações A/B de uma headline
python scripts/ab_generator.py headline "Aprenda marketing digital"

# Pontuar uma headline
python scripts/headline_scorer.py "7 segredos de marketing digital que ninguém conta"

# Comparar headlines
python scripts/headline_scorer.py --compare "Headline A" "Headline B"

# Analisar legibilidade de um texto
python scripts/readability_checker.py --file artigo.txt

# Adaptar conteúdo para todas as plataformas
python scripts/content_repurposer.py --file artigo.txt --output todos

# Gerar hooks virais
python scripts/hook_generator.py "produtividade com IA" reels 10

# Gerar ideias de conteúdo
python scripts/content_idea_generator.py tecnologia 20
```

## :bar_chart: Workflows (8 workflows)

| Workflow | Arquivo | Descrição |
|----------|---------|-----------|
| Lançamento de Produto | `workflows/lancamento-produto.md` | Campanha completa de lançamento com timeline de 30 dias |
| Calendário Mensal | `workflows/calendario-mensal.md` | Planejamento editorial mensal completo |
| Campanha de Conversão | `workflows/campanha-conversao.md` | Flash sale, promoções, geração de leads |
| Funil de Vendas | `workflows/funil-vendas.md` | Processo completo TOFU -> MOFU -> BOFU |
| Parceria com Influencer | `workflows/parceria-influencer.md` | Prospecção, briefing e gestão de influenciadores |
| Batch Production | `workflows/batch-production-workflow.md` | Produção em lote para escalar conteúdo |
| TikTok Trends Chrome | `workflows/tiktok-trends-chrome.md` | Monitoramento de trends do TikTok via Chrome |
| Content Pipeline | `workflows/content-pipeline.md` | Pipeline de conteúdo: Research → Copy → Design → Review |

## :card_file_box: Swipe Files (9 arquivos)

Banco de referências e exemplos prontos para uso:

| Arquivo | Descrição |
|---------|-----------|
| `assets/swipe-files/headlines-virais.md` | Coleção de headlines de alto impacto |
| `assets/swipe-files/hooks-reels.md` | Hooks testados para Reels e TikTok |
| `assets/swipe-files/ctas-conversão.md` | CTAs otimizados para conversão |
| `assets/swipe-files/emails-conversão.md` | Modelos de emails que convertem |
| `assets/swipe-files/copy-carrossel.md` | Copys para carrosséis de Instagram |
| `assets/swipe-files/bios-instagram.md` | Modelos de bio para Instagram |
| `assets/swipe-files/transicoes-reels.md` | Transições criativas para Reels |
| `assets/swipe-files/trends-adaptáveis.md` | Trends adaptáveis para diferentes nichos |
| `assets/swipe-files/paletas-cores.md` | Paletas de cores por nicho e emoção |

## :sparkles: Prompts para IA (3 arquivos)

| Arquivo | Descrição |
|---------|-----------|
| `assets/prompts/prompt-biblioteca.md` | Biblioteca completa de prompts |
| `assets/prompts/prompts-imagem-ia.md` | Prompts para geração de imagens com IA |
| `assets/prompts/prompts-post-pronto.md` | Prompts para criar posts completos |

## :clipboard: Frameworks de Copywriting

O agente utiliza os seguintes frameworks conforme o contexto:

- **AIDA** - Atenção -> Interesse -> Desejo -> Ação
- **PAS** - Problema -> Agitar -> Solução
- **BAB** - Antes -> Depois -> Ponte
- **4Ps** - Promessa -> Imagem -> Prova -> Empurrão
- **QUEST** - Qualificar -> Entender -> Educar -> Estimular -> Transicionar

## :books: Documentação

| Arquivo | Descrição |
|---------|-----------|
| `GUIA-DE-USO.md` | Guia completo de uso do agente com exemplos práticos |
| `INSTALACAO-SKILL.md` | Instruções detalhadas para instalar a skill no Claude Code |
| `CONTRIBUTING.md` | Guia para contribuição no projeto |
| `CHANGELOG.md` | Histórico de alterações e versões |
| `references/design-specs.md` | Especificações de design e dimensões por plataforma |

## :package: Instalação Rápida

### Opção 1: Via Claude Cowork (Recomendado)

Instale diretamente do GitHub como marketplace de plugins:

1. Abra o **Claude Cowork**
2. Vá em **Plugins** > **Adicionar marketplace do GitHub**
3. Cole a URL do repositório:
   ```
   https://github.com/rilnermucio/Agents
   ```
4. Clique em **Adicionar**
5. A skill `marketing-os` estará disponível automaticamente!

**Vantagem:** Sempre atualizado! Quando o repositório for atualizado, sua skill também será.

### Opção 2: Instalação Local

```bash
# Clone o repositório
git clone https://github.com/rilnermucio/Agents.git
cd "Marketing OS"

# Instale dependências Python (opcional, para scripts)
pip install -r requirements.txt
```

### Opção 3: Copiar Skill Manualmente

1. Copie a pasta `skills/marketing-os/` para:
   - **macOS:** `~/.claude/skills/`
   - **Windows:** `%APPDATA%\Claude\skills\`
   - **Linux:** `~/.config/claude/skills/`

Para instruções detalhadas, consulte `INSTALACAO-SKILL.md`.

## :handshake: Contribuição

Contribuições são bem-vindas! Para contribuir:

1. Faça um fork do repositório
2. Crie uma branch para sua feature (`git checkout -b feature/nova-feature`)
3. Commit suas alterações (`git commit -m 'Adiciona nova feature'`)
4. Push para a branch (`git push origin feature/nova-feature`)
5. Abra um Pull Request

Para mais detalhes, consulte `CONTRIBUTING.md`.

### Áreas para contribuição

- Novos templates de conteúdo
- Novos nichos e personas
- Melhorias nos scripts Python
- Novos workflows de campanha
- Traduções e localizações

## :memo: Licença

Este projeto está licenciado sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---

Desenvolvido com :purple_heart: por [rilnermucio](https://github.com/rilnermucio)
