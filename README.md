# :dart: Agente Criador de Conteudo

Agente de IA especializado em criacao de conteudo estrategico para multiplos nichos e plataformas. Projetado para funcionar como skill do Claude Code.

[![GitHub](https://img.shields.io/badge/GitHub-rilnermucio%2FAgents-blue?logo=github)](https://github.com/rilnermucio/Agents.git)
[![Python](https://img.shields.io/badge/Python-3.8%2B-yellow?logo=python)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

## :clipboard: Visao Geral

O **Agente Criador de Conteudo** e um sistema de IA composto por 11 subagentes especializados que trabalham em conjunto para criar conteudo estrategico de alta qualidade. Ele cobre:

- **Redes sociais**: Instagram (feed, carrossel, reels, stories), LinkedIn, Twitter/X, TikTok, YouTube, Pinterest, Facebook
- **Marketing**: Email marketing, newsletters, sequencias de automacao
- **SEO**: Artigos otimizados, blog posts, meta tags, featured snippets
- **Video**: Scripts YouTube, Reels/TikTok/Shorts, VSL (Video Sales Letter)
- **Audio**: Roteiros de podcast, spots publicitarios
- **Anuncios**: Copy para Meta Ads, Google Ads, TikTok Ads, LinkedIn Ads
- **Landing pages**: Paginas de vendas, captura de leads
- **IA generativa**: Prompts para geracao de imagens e videos com IA

Suporta **10+ nichos** com personas, pilares de conteudo, hooks e hashtags especificos para cada um.

## :building_construction: Arquitetura

```
CONTENT CREATOR (Agente Principal)
|
+-- :mag: RESEARCH AGENT        - Pesquisa de tendencias, concorrencia, keywords
+-- :pencil2: COPY AGENT            - Headlines, CTAs, copy persuasivo, variacoes A/B
+-- :mag_right: SEO AGENT             - Otimizacao on-page, estruturacao, E-E-A-T
+-- :iphone: SOCIAL AGENT          - Posts por plataforma, hashtags, timing
+-- :clapper: VIDEO AGENT           - Scripts YouTube, Reels, TikTok, VSL
+-- :robot: AI TOOLS AGENT        - Prompts para imagem e video com IA
+-- :bar_chart: ANALYTICS AGENT      - Metricas, relatorios, testes A/B
+-- :studio_microphone: AUDIO AGENT          - Podcasts, roteiros de audio, spots
+-- :envelope: EMAIL AGENT           - Sequencias de email, newsletters
+-- :loudspeaker: ADS AGENT            - Copy de anuncios Meta/Google/TikTok/LinkedIn
+-- :art: DESIGN AGENT          - Design visual, paletas de cores, identidade
```

## :open_file_folder: Estrutura do Projeto

```
Agente Criador de Conteudo/
|
+-- Skill.md                          # Arquivo principal da skill (Claude Code)
+-- README.md                         # Este arquivo
+-- GUIA-DE-USO.md                    # Guia completo de uso do agente
+-- INSTALACAO-SKILL.md               # Instrucoes de instalacao da skill
+-- requirements.txt                  # Dependencias Python
+-- content-creator.skill             # Skill empacotada v1
+-- content-creator-v2.skill          # Skill empacotada v2
+-- .gitignore
|
+-- subagents/                        # 11 subagentes especializados
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
|   +-- design-agent.md               # NOVO: Design visual e identidade
|
+-- scripts/                          # 20 scripts Python de automacao
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
|
+-- assets/
|   +-- templates/                    # 27 templates de conteudo
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
|   +-- swipe-files/                  # Banco de referencias e exemplos
|   |   +-- headlines-virais.md
|   |   +-- hooks-reels.md
|   |   +-- ctas-conversao.md
|   |   +-- emails-conversao.md
|   |   +-- copy-carrossel.md
|   |   +-- bios-instagram.md
|   |   +-- transicoes-reels.md       # NOVO
|   |   +-- trends-adaptaveis.md      # NOVO
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
|       +-- prompts-imagem-ia.md      # NOVO: Prompts para geracao de imagens
|       +-- prompts-post-pronto.md    # NOVO: Prompts para posts prontos
|
+-- references/                       # Guias de referencia por tipo
|   +-- niches.md
|   +-- strategy.md
|   +-- social-media.md
|   +-- blog-seo.md
|   +-- email-marketing.md
|   +-- landing-pages.md
|   +-- ads-copy.md
|   +-- design-specs.md               # NOVO: Especificacoes de design
|
+-- workflows/                        # 7 workflows de campanha
|   +-- lancamento-produto.md
|   +-- calendario-mensal.md
|   +-- campanha-conversao.md
|   +-- funil-vendas.md
|   +-- parceria-influencer.md
|   +-- batch-production-workflow.md  # NOVO: Producao em lote
|   +-- tiktok-trends-chrome.md       # NOVO: Monitoramento TikTok
|
+-- output/                           # Pasta para conteudo gerado
+-- outputs/                          # Exemplos de conteudo gerado
|
+-- skill-package/                    # Skill empacotada para distribuicao
    +-- content-creator/
```

## :robot: Subagentes

| Subagente | Arquivo | Descricao |
|-----------|---------|-----------|
| Research Agent | `subagents/research-agent.md` | Pesquisa de tendencias, analise de concorrencia, keyword research, mapeamento de audiencia |
| Copy Agent | `subagents/copy-agent.md` | Headlines, hooks, CTAs otimizados, copy de vendas, variacoes A/B, neuromarketing |
| SEO Agent | `subagents/seo-agent.md` | Otimizacao on-page, estruturacao de conteudo, meta tags, E-E-A-T |
| Social Agent | `subagents/social-agent.md` | Posts por plataforma, adaptacao cross-platform, hashtags, timing, algoritmos |
| Video Agent | `subagents/video-agent.md` | Scripts YouTube (long-form), Reels/TikTok/Shorts, VSL, hooks de retencao |
| AI Tools Agent | `subagents/ai-tools-agent.md` | Prompts para imagem (Midjourney, DALL-E, Flux) e video (Veo 3.1, Sora 2, Kling) |
| Analytics Agent | `subagents/analytics-agent.md` | Metricas por plataforma, relatorios, analise de performance, testes A/B |
| Audio Agent | `subagents/audio-agent.md` | Roteiros de podcast (solo, entrevista, co-host), spots, audiobooks |
| Email Agent | `subagents/email-agent.md` | Sequencias de email, newsletters, automacoes de marketing |
| Ads Agent | `subagents/ads-agent.md` | Copy de anuncios Meta/Google/TikTok/LinkedIn, estrategia de ads |
| Design Agent | `subagents/design-agent.md` | Design visual, paletas de cores, identidade de marca, layouts |

## :page_facing_up: Templates Disponiveis (27 templates)

### Redes Sociais

| Template | Arquivo | Descricao |
|----------|---------|-----------|
| Post Instagram Carrossel | `assets/templates/post-instagram-carrossel.md` | Template de carrossel Instagram |
| Instagram Feed Post | `assets/templates/instagram-feed-post.md` | Posts para feed do Instagram |
| Instagram Stories | `assets/templates/instagram-stories.md` | Templates de stories interativos |
| Carrossel Thumbnail Mastery | `assets/templates/carrossel-thumbnail-mastery.md` | Capas de carrossel de alto impacto |
| Card Unico por Nicho | `assets/templates/card-unico-niche-templates.md` | Templates de card unico por nicho |
| Post LinkedIn | `assets/templates/post-linkedin.md` | Estrutura de post para LinkedIn |
| Twitter Thread | `assets/templates/twitter-thread.md` | Threads virais para Twitter/X |
| Pinterest Pins | `assets/templates/pinterest-pins.md` | Pins e Idea Pins otimizados |

### Video

| Template | Arquivo | Descricao |
|----------|---------|-----------|
| YouTube Script | `assets/templates/youtube-script.md` | Roteiros completos para videos longos |
| YouTube Shorts | `assets/templates/youtube-shorts.md` | Scripts para Shorts otimizados |
| Reels/TikTok Script | `assets/templates/reels-tiktok-script.md` | Scripts para videos curtos (15s, 30s, 60s) |
| Reels Audio Strategy | `assets/templates/reels-audio-strategy.md` | Estrategia de audio para Reels virais |
| VSL Script | `assets/templates/vsl-script.md` | Video Sales Letter completo |
| Pesquisa TikTok Trends | `assets/templates/pesquisa-tiktok-trends.md` | Metodologia de pesquisa de trends |

### Audio e Podcast

| Template | Arquivo | Descricao |
|----------|---------|-----------|
| Podcast Episode | `assets/templates/podcast-episode.md` | Estrutura de episodio de podcast |
| Podcast Ad Reads | `assets/templates/podcast-ad-reads.md` | Scripts de anuncios para podcasts |

### Conteudo Escrito

| Template | Arquivo | Descricao |
|----------|---------|-----------|
| Artigo SEO | `assets/templates/artigo-seo.md` | Estrutura completa para artigos otimizados |
| Email Newsletter | `assets/templates/email-newsletter.md` | Template de newsletter por email |
| Press Release | `assets/templates/press-release.md` | Comunicados de imprensa |
| Case Study | `assets/templates/case-study.md` | Estudos de caso |
| Whitepaper | `assets/templates/whitepaper.md` | Conteudo B2B aprofundado |

### Vendas e Conversao

| Template | Arquivo | Descricao |
|----------|---------|-----------|
| Webinar Script | `assets/templates/webinar-script.md` | Roteiro completo de webinar/live de vendas |
| Sales Page | `assets/templates/sales-page.md` | Estrutura de pagina de vendas |
| Lead Magnet | `assets/templates/lead-magnet.md` | Templates de iscas digitais |
| UGC Brief | `assets/templates/ugc-brief.md` | Briefing para criadores UGC |

### Personalizados

| Template | Arquivo | Descricao |
|----------|---------|-----------|
| Meus Templates | `assets/templates/meus-templates.md` | Templates personalizados do usuario |

## :wrench: Scripts de Automacao (20 scripts)

### Analise e Otimizacao

| Script | Descricao | Comando |
|--------|-----------|---------|
| `seo_analyzer.py` | Analisa e otimiza conteudo para SEO com score 0-100 | `python scripts/seo_analyzer.py arquivo.md "keyword"` |
| `readability_checker.py` | Analisa legibilidade com Flesch adaptado para portugues | `python scripts/readability_checker.py --file artigo.txt` |
| `headline_scorer.py` | Pontua headlines por poder emocional e clareza (0-100) | `python scripts/headline_scorer.py "Sua headline aqui"` |
| `content_audit.py` | Audita conteudo existente e sugere melhorias | `python scripts/content_audit.py arquivo.md --tipo blog` |
| `competitor_analyzer.py` | Analisa perfis de concorrentes e extrai insights | `python scripts/competitor_analyzer.py "@perfil1" "@perfil2"` |

### Geracao de Conteudo

| Script | Descricao | Comando |
|--------|-----------|---------|
| `hook_generator.py` | Gera hooks virais para videos e posts | `python scripts/hook_generator.py "tema" reels 10` |
| `hook_variant_generator.py` | Gera multiplas variacoes de hooks por formato | `python scripts/hook_variant_generator.py "tema" --formato reels` |
| `content_idea_generator.py` | Gera ideias de conteudo por nicho e pilares | `python scripts/content_idea_generator.py tecnologia 20` |
| `ab_generator.py` | Gera variacoes de copy para testes A/B | `python scripts/ab_generator.py headline "texto original"` |
| `caption_generator.py` | Gera legendas otimizadas para Instagram por objetivo | `python scripts/caption_generator.py "tema" engajamento` |

### Instagram e Redes Sociais

| Script | Descricao | Comando |
|--------|-----------|---------|
| `hashtag_generator.py` | Gera hashtags relevantes por nicho e plataforma | `python scripts/hashtag_generator.py nicho plataforma` |
| `instagram_hashtag_research.py` | Pesquisa avancada de hashtags com estrategias | `python scripts/instagram_hashtag_research.py "nicho" --gerar-set` |
| `carousel_structure_generator.py` | Gera estruturas completas de carrossel | `python scripts/carousel_structure_generator.py "tema" educativo 10` |
| `reels_script_generator.py` | Gera roteiros para Reels com timestamps | `python scripts/reels_script_generator.py "tema" 30 tutorial` |

### Planejamento e Calendario

| Script | Descricao | Comando |
|--------|-----------|---------|
| `content_calendar.py` | Cria calendario editorial para multiplas plataformas | `python scripts/content_calendar.py 2026-02-01 4 instagram linkedin` |
| `content_repurposer.py` | Adapta conteudo entre plataformas automaticamente | `python scripts/content_repurposer.py --file artigo.txt --output todos` |

### Tendencias e Trends

| Script | Descricao | Comando |
|--------|-----------|---------|
| `trend_tracker.py` | Monitora tendencias via Google Trends, Reddit, YouTube | `python scripts/trend_tracker.py "termo" google,reddit --periodo 7` |
| `trend_adapter.py` | Adapta trends virais para diferentes nichos | `python scripts/trend_adapter.py "get ready with me" marketing` |
| `tiktok_trends_scraper.py` | Busca videos virais do TikTok por hashtag | `python scripts/tiktok_trends_scraper.py --hashtag "marketing" --min-views 1000000` |

## :iphone: Plataformas Suportadas

- **Instagram** - Feed, Carrossel, Reels, Stories
- **LinkedIn** - Posts, Artigos, Newsletter
- **Twitter/X** - Tweets, Threads
- **TikTok** - Videos curtos, Lives
- **YouTube** - Videos long-form, Shorts
- **Pinterest** - Pins, Idea Pins
- **Facebook** - Posts, Stories, Grupos
- **Email** - Newsletters, Sequencias, Automacoes
- **Blog/SEO** - Artigos otimizados, Landing pages
- **Podcast** - Episodios, Show notes
- **Anuncios** - Meta Ads, Google Ads, TikTok Ads, LinkedIn Ads

## :dart: Nichos Suportados

| Nicho | Foco Principal | Tom Sugerido |
|-------|----------------|--------------|
| Inteligencia Artificial | Ferramentas, tutoriais, tendencias | Educativo, acessivel |
| Desenvolvimento Pessoal | Mindset, habitos, proposito | Inspiracional, empatico |
| Desenvolvimento Profissional | Carreira, skills, lideranca | Profissional, pratico |
| Tecnologia/Programacao | Codigo, tutoriais, carreira tech | Tecnico, didatico |
| Empreendedorismo | Negocios, vendas, escala | Motivador, estrategico |
| Financas Pessoais | Investimentos, renda, organizacao | Educativo, confiavel |
| Saude e Bem-Estar | Exercicio, nutricao, saude mental | Acolhedor, motivador |
| Educacao | Estudos, aprendizado, concursos | Didatico, encorajador |
| Produtividade | Tempo, foco, ferramentas | Pratico, direto |
| Marketing Digital | Estrategias, ferramentas, metricas | Autoridade, data-driven |

## :rocket: Como Usar

### Como Skill do Claude Code

1. **Configure como skill** no Claude Code apontando para o arquivo `Skill.md`
2. **O agente sera acionado automaticamente** quando detectar triggers como: conteudo, marketing, post, blog, SEO, newsletter, copy, landing page, campanha, anuncio, Instagram, LinkedIn, TikTok, video, YouTube, Reels, podcast, VSL
3. **Exemplo de uso**:

```
Voce: "Crie um carrossel para Instagram sobre produtividade com IA"

O agente automaticamente:
1. Consulta o nicho (IA + Produtividade)
2. Aciona o Social Agent para formato Instagram
3. Aciona o Copy Agent para headlines e CTAs
4. Usa templates de carrossel
5. Gera hashtags relevantes
6. Entrega conteudo pronto com variacoes A/B
```

### Scripts Python

Todos os scripts podem ser executados independentemente via terminal:

```bash
# Analisar SEO de um artigo
python scripts/seo_analyzer.py artigo.md "marketing digital"

# Gerar hashtags para um nicho
python scripts/hashtag_generator.py marketing_digital instagram

# Criar calendario editorial de 4 semanas
python scripts/content_calendar.py 2026-02-01 4 instagram linkedin tiktok

# Gerar variacoes A/B de uma headline
python scripts/ab_generator.py headline "Aprenda marketing digital"

# Pontuar uma headline
python scripts/headline_scorer.py "7 segredos de marketing digital que ninguem conta"

# Comparar headlines
python scripts/headline_scorer.py --compare "Headline A" "Headline B"

# Analisar legibilidade de um texto
python scripts/readability_checker.py --file artigo.txt

# Adaptar conteudo para todas as plataformas
python scripts/content_repurposer.py --file artigo.txt --output todos

# Gerar hooks virais
python scripts/hook_generator.py "produtividade com IA" reels 10

# Gerar ideias de conteudo
python scripts/content_idea_generator.py tecnologia 20
```

## :bar_chart: Workflows (7 workflows)

| Workflow | Arquivo | Descricao |
|----------|---------|-----------|
| Lancamento de Produto | `workflows/lancamento-produto.md` | Campanha completa de lancamento com timeline de 30 dias |
| Calendario Mensal | `workflows/calendario-mensal.md` | Planejamento editorial mensal completo |
| Campanha de Conversao | `workflows/campanha-conversao.md` | Flash sale, promocoes, geracao de leads |
| Funil de Vendas | `workflows/funil-vendas.md` | Processo completo TOFU -> MOFU -> BOFU |
| Parceria com Influencer | `workflows/parceria-influencer.md` | Prospeccao, briefing e gestao de influenciadores |
| Batch Production | `workflows/batch-production-workflow.md` | Producao em lote para escalar conteudo |
| TikTok Trends Chrome | `workflows/tiktok-trends-chrome.md` | Monitoramento de trends do TikTok via Chrome |

## :card_file_box: Swipe Files (9 arquivos)

Banco de referencias e exemplos prontos para uso:

| Arquivo | Descricao |
|---------|-----------|
| `assets/swipe-files/headlines-virais.md` | Colecao de headlines de alto impacto |
| `assets/swipe-files/hooks-reels.md` | Hooks testados para Reels e TikTok |
| `assets/swipe-files/ctas-conversao.md` | CTAs otimizados para conversao |
| `assets/swipe-files/emails-conversao.md` | Modelos de emails que convertem |
| `assets/swipe-files/copy-carrossel.md` | Copys para carrosseis de Instagram |
| `assets/swipe-files/bios-instagram.md` | Modelos de bio para Instagram |
| `assets/swipe-files/transicoes-reels.md` | Transicoes criativas para Reels |
| `assets/swipe-files/trends-adaptaveis.md` | Trends adaptaveis para diferentes nichos |
| `assets/swipe-files/paletas-cores.md` | Paletas de cores por nicho e emocao |

## :sparkles: Prompts para IA (3 arquivos)

| Arquivo | Descricao |
|---------|-----------|
| `assets/prompts/prompt-biblioteca.md` | Biblioteca completa de prompts |
| `assets/prompts/prompts-imagem-ia.md` | Prompts para geracao de imagens com IA |
| `assets/prompts/prompts-post-pronto.md` | Prompts para criar posts completos |

## :clipboard: Frameworks de Copywriting

O agente utiliza os seguintes frameworks conforme o contexto:

- **AIDA** - Atencao -> Interesse -> Desejo -> Acao
- **PAS** - Problema -> Agitar -> Solucao
- **BAB** - Antes -> Depois -> Ponte
- **4Ps** - Promessa -> Imagem -> Prova -> Empurrao
- **QUEST** - Qualificar -> Entender -> Educar -> Estimular -> Transicionar

## :books: Documentacao

| Arquivo | Descricao |
|---------|-----------|
| `GUIA-DE-USO.md` | Guia completo de uso do agente com exemplos praticos |
| `INSTALACAO-SKILL.md` | Instrucoes detalhadas para instalar a skill no Claude Code |
| `CONTRIBUTING.md` | Guia para contribuicao no projeto |
| `CHANGELOG.md` | Historico de alteracoes e versoes |
| `references/design-specs.md` | Especificacoes de design e dimensoes por plataforma |

## :package: Instalacao Rapida

### Opcao 1: Skill Empacotada

1. Baixe o arquivo `content-creator-v2.skill`
2. Importe no Claude Code como skill
3. Comece a usar!

### Opcao 2: Via Repositorio

```bash
git clone https://github.com/rilnermucio/Agents.git
cd "Agente Criador de Conteudo"
pip install -r requirements.txt
```

Para instrucoes detalhadas, consulte `INSTALACAO-SKILL.md`.

## :handshake: Contribuicao

Contribuicoes sao bem-vindas! Para contribuir:

1. Faca um fork do repositorio
2. Crie uma branch para sua feature (`git checkout -b feature/nova-feature`)
3. Commit suas alteracoes (`git commit -m 'Adiciona nova feature'`)
4. Push para a branch (`git push origin feature/nova-feature`)
5. Abra um Pull Request

Para mais detalhes, consulte `CONTRIBUTING.md`.

### Areas para contribuicao

- Novos templates de conteudo
- Novos nichos e personas
- Melhorias nos scripts Python
- Novos workflows de campanha
- Traducoes e localizacoes

## :memo: Licenca

Este projeto esta licenciado sob a licenca MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---

Desenvolvido com :purple_heart: por [rilnermucio](https://github.com/rilnermucio)
