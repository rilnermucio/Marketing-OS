# :dart: Agente Criador de Conteudo

Agente de IA especializado em criacao de conteudo estrategico para multiplos nichos e plataformas. Projetado para funcionar como skill do Claude Code.

[![GitHub](https://img.shields.io/badge/GitHub-rilnermucio%2FAgents-blue?logo=github)](https://github.com/rilnermucio/Agents.git)
[![Python](https://img.shields.io/badge/Python-3.8%2B-yellow?logo=python)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

## :clipboard: Visao Geral

O **Agente Criador de Conteudo** e um sistema de IA composto por 10 subagentes especializados que trabalham em conjunto para criar conteudo estrategico de alta qualidade. Ele cobre:

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
```

## :open_file_folder: Estrutura do Projeto

```
Agente Criador de Conteudo/
|
+-- Skill.md                          # Arquivo principal da skill (Claude Code)
+-- README.md                         # Este arquivo
+-- requirements.txt                  # Dependencias Python
+-- .gitignore
|
+-- subagents/                        # 10 subagentes especializados
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
|
+-- scripts/                          # Scripts Python de automacao
|   +-- seo_analyzer.py
|   +-- hashtag_generator.py
|   +-- content_calendar.py
|   +-- ab_generator.py
|   +-- headline_scorer.py
|   +-- readability_checker.py
|   +-- content_repurposer.py
|   +-- hook_generator.py
|   +-- content_idea_generator.py
|
+-- assets/
|   +-- templates/                    # 16 templates de conteudo
|   |   +-- artigo-seo.md
|   |   +-- email-newsletter.md
|   |   +-- post-linkedin.md
|   |   +-- post-instagram-carrossel.md
|   |   +-- youtube-script.md
|   |   +-- reels-tiktok-script.md
|   |   +-- vsl-script.md
|   |   +-- podcast-episode.md
|   |   +-- twitter-thread.md
|   |   +-- press-release.md
|   |   +-- case-study.md
|   |   +-- whitepaper.md
|   |   +-- webinar-script.md
|   |   +-- sales-page.md
|   |   +-- lead-magnet.md
|   |   +-- ugc-brief.md
|   |
|   +-- swipe-files/                  # Banco de referencias e exemplos
|   |   +-- headlines-virais.md
|   |   +-- hooks-reels.md
|   |   +-- ctas-conversao.md
|   |   +-- emails-conversao.md
|   |   +-- copy-carrossel.md
|   |   +-- bios-instagram.md
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
|
+-- references/                       # Guias de referencia por tipo
|   +-- niches.md
|   +-- strategy.md
|   +-- social-media.md
|   +-- blog-seo.md
|   +-- email-marketing.md
|   +-- landing-pages.md
|   +-- ads-copy.md
|
+-- workflows/                        # Workflows de campanha
|   +-- lancamento-produto.md
|   +-- calendario-mensal.md
|   +-- campanha-conversao.md
|   +-- funil-vendas.md
|   +-- parceria-influencer.md
|
+-- output/                           # Pasta para conteudo gerado
```

## :robot: Subagentes

| Subagente | Arquivo | Descricao |
|-----------|---------|-----------|
| Research Agent | `subagents/research-agent.md` | Pesquisa de tendencias, analise de concorrencia, keyword research, mapeamento de audiencia |
| Copy Agent | `subagents/copy-agent.md` | Headlines, hooks, CTAs otimizados, copy de vendas, variacoes A/B |
| SEO Agent | `subagents/seo-agent.md` | Otimizacao on-page, estruturacao de conteudo, meta tags, E-E-A-T |
| Social Agent | `subagents/social-agent.md` | Posts por plataforma, adaptacao cross-platform, hashtags, timing |
| Video Agent | `subagents/video-agent.md` | Scripts YouTube (long-form), Reels/TikTok/Shorts, VSL, hooks de retencao |
| AI Tools Agent | `subagents/ai-tools-agent.md` | Prompts para imagem (Midjourney, DALL-E) e video (Veo 3.1, Sora 2, Kling) |
| Analytics Agent | `subagents/analytics-agent.md` | Metricas por plataforma, relatorios, analise de performance, testes A/B |
| Audio Agent | `subagents/audio-agent.md` | Roteiros de podcast (solo, entrevista, co-host), spots, audiobooks |
| Email Agent | `subagents/email-agent.md` | Sequencias de email, newsletters, automacoes de marketing |
| Ads Agent | `subagents/ads-agent.md` | Copy de anuncios Meta/Google/TikTok/LinkedIn, estrategia de ads |

## :page_facing_up: Templates Disponiveis

| Template | Arquivo | Descricao |
|----------|---------|-----------|
| Artigo SEO | `assets/templates/artigo-seo.md` | Estrutura completa para artigos otimizados |
| Email Newsletter | `assets/templates/email-newsletter.md` | Template de newsletter por email |
| Post LinkedIn | `assets/templates/post-linkedin.md` | Estrutura de post para LinkedIn |
| Post Instagram Carrossel | `assets/templates/post-instagram-carrossel.md` | Template de carrossel Instagram |
| YouTube Script | `assets/templates/youtube-script.md` | Roteiros completos para videos longos |
| Reels/TikTok Script | `assets/templates/reels-tiktok-script.md` | Scripts para videos curtos (15s, 30s, 60s) |
| VSL Script | `assets/templates/vsl-script.md` | Video Sales Letter completo |
| Podcast Episode | `assets/templates/podcast-episode.md` | Estrutura de episodio de podcast |
| Twitter Thread | `assets/templates/twitter-thread.md` | Threads virais para Twitter/X |
| Press Release | `assets/templates/press-release.md` | Comunicados de imprensa |
| Case Study | `assets/templates/case-study.md` | Estudos de caso |
| Whitepaper | `assets/templates/whitepaper.md` | Conteudo B2B aprofundado |
| Webinar Script | `assets/templates/webinar-script.md` | Roteiro completo de webinar/live de vendas |
| Sales Page | `assets/templates/sales-page.md` | Estrutura de pagina de vendas |
| Lead Magnet | `assets/templates/lead-magnet.md` | Templates de iscas digitais |
| UGC Brief | `assets/templates/ugc-brief.md` | Briefing para criadores UGC |

## :wrench: Scripts de Automacao

| Script | Descricao | Comando |
|--------|-----------|---------|
| `seo_analyzer.py` | Analisa e otimiza conteudo para SEO com score 0-100 | `python scripts/seo_analyzer.py arquivo.md "keyword"` |
| `hashtag_generator.py` | Gera hashtags relevantes por nicho e plataforma | `python scripts/hashtag_generator.py nicho plataforma` |
| `content_calendar.py` | Cria calendario editorial para multiplas plataformas | `python scripts/content_calendar.py 2026-02-01 4 instagram linkedin` |
| `ab_generator.py` | Gera variacoes de copy para testes A/B | `python scripts/ab_generator.py headline "texto original"` |
| `headline_scorer.py` | Pontua headlines por poder emocional e clareza (0-100) | `python scripts/headline_scorer.py "Sua headline aqui"` |
| `readability_checker.py` | Analisa legibilidade com Flesch adaptado para portugues | `python scripts/readability_checker.py --file artigo.txt` |
| `content_repurposer.py` | Adapta conteudo entre plataformas automaticamente | `python scripts/content_repurposer.py --file artigo.txt --output todos` |
| `hook_generator.py` | Gera hooks virais para videos e posts | `python scripts/hook_generator.py "tema" reels 10` |
| `content_idea_generator.py` | Gera ideias de conteudo por nicho e pilares | `python scripts/content_idea_generator.py tecnologia 20` |

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

## :bar_chart: Workflows

| Workflow | Arquivo | Descricao |
|----------|---------|-----------|
| Lancamento de Produto | `workflows/lancamento-produto.md` | Campanha completa de lancamento com timeline de 30 dias |
| Calendario Mensal | `workflows/calendario-mensal.md` | Planejamento editorial mensal completo |
| Campanha de Conversao | `workflows/campanha-conversao.md` | Flash sale, promocoes, geracao de leads |
| Funil de Vendas | `workflows/funil-vendas.md` | Processo completo TOFU -> MOFU -> BOFU |
| Parceria com Influencer | `workflows/parceria-influencer.md` | Prospeccao, briefing e gestao de influenciadores |

## :clipboard: Frameworks de Copywriting

O agente utiliza os seguintes frameworks conforme o contexto:

- **AIDA** - Atencao -> Interesse -> Desejo -> Acao
- **PAS** - Problema -> Agitar -> Solucao
- **BAB** - Antes -> Depois -> Ponte
- **4Ps** - Promessa -> Imagem -> Prova -> Empurrao
- **QUEST** - Qualificar -> Entender -> Educar -> Estimular -> Transicionar

## :handshake: Contribuicao

Contribuicoes sao bem-vindas! Para contribuir:

1. Faca um fork do repositorio
2. Crie uma branch para sua feature (`git checkout -b feature/nova-feature`)
3. Commit suas alteracoes (`git commit -m 'Adiciona nova feature'`)
4. Push para a branch (`git push origin feature/nova-feature`)
5. Abra um Pull Request

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
