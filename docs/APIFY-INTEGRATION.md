# Apify Integration (opcional)

Scraping estruturado de SERP do Google e perfis públicos do Instagram via [Apify Actors](https://apify.com/store), consumido pelos agents `mos-seo` e `mos-research`. **Totalmente opt-in** — sem token configurado, o plugin se comporta exatamente como antes.

## Por que existe

Casos onde `WebSearch`/`WebFetch` não bastam:

- **SERP estruturado pra SEO**: top 10 com snippets, People Also Ask e related searches em formato JSON, em uma chamada.
- **Concorrente externo no Instagram**: posts + métricas agregadas + top hashtags de um perfil sem precisar de login no IG.

Pra qualquer outra coisa (pesquisa rasa, fact-check, conteúdo público em página única), `WebSearch` continua sendo o caminho — mais rápido, sem custo e sem dependência externa.

## Setup (3 passos)

1. **Crie conta no Apify**: https://console.apify.com/sign-up (free tier dá ~$5 USD de crédito mensal — cobre semanas de teste do MVP).
2. **Pegue o token**: Settings → Integrations → API token → copiar.
3. **Exporte no shell** (ou no `~/.zshrc` / `.env` local):
   ```bash
   export APIFY_TOKEN="apify_api_xxx..."
   ```

Pronto. Rode um `--dry-run` pra confirmar que o custo estimado bate com o esperado:

```bash
python scripts/apify_serp.py --query "infoproduto bofu" --dry-run
python scripts/apify_instagram.py --handle @concorrente --dry-run
```

## Uso direto

```bash
# SERP (default 10 resultados, BR + pt-BR)
python scripts/apify_serp.py --query "infoproduto bofu"

# SERP com mais resultados e formato JSON
python scripts/apify_serp.py --query "x" --max-results 20 --format json

# Instagram (default 30 posts)
python scripts/apify_instagram.py --handle @concorrente

# Instagram via URL completa
python scripts/apify_instagram.py --handle "https://instagram.com/concorrente/"

# Via CLI unificado (mos.py)
python scripts/mos.py apify serp "x" --max-results 10
python scripts/mos.py apify instagram @concorrente --max-posts 30
```

Output:
- **stdout**: Markdown summary (consumível direto pelos agents)
- **arquivo**: JSON completo em `workspace/research/apify/<timestamp>-<slug>.json` (gitignored)
- **stderr**: caminho do arquivo salvo + mensagens de erro

## Custo estimado

Baseado em pricing público dos Actors em maio/2026. **Heurística** — preço real pode variar.

| Operação | Volume | Custo aproximado |
|---|---|---|
| 1 query SERP, 10 resultados | 10 results | $0.05 USD |
| 1 query SERP, 100 resultados (cap) | 100 results | $0.50 USD |
| 1 perfil IG, 30 posts | 30 posts | $0.07 USD |
| 1 perfil IG, 100 posts (cap) | 100 posts | $0.23 USD |

**Hard caps no MVP**: 100 results SERP, 100 posts Instagram. Evita engano de digitar 10000.

Sempre rode `--dry-run` antes de execuções caras.

## Como os agents usam

### `mos-seo`

Quando o briefing pede "rankear pra X", "análise de SERP", "intent matching", "keyword research aprofundada", o agent verifica `APIFY_TOKEN` e, se disponível, invoca `apify_serp.py` para pegar a SERP estruturada antes de propor headline e outline. Sem token, segue com `WebSearch` normal.

### `mos-research`

Quando o briefing envolve análise de concorrente específico, content gap analysis ou benchmark de engajamento, o agent invoca `apify_instagram.py` pra pegar top posts e hashtags. O resultado vai pro `Research Brief` final como evidência.

## Graceful degrade

Sem `APIFY_TOKEN`, os scripts saem com **exit 0** e mensagem em stderr. Os agents capturam isso e seguem com WebSearch. Não há erro, não há crash — só ausência da ferramenta opcional.

Erros reais (401 invalid token, 429 rate limit, timeout) saem com **exit 2** e mensagem clara em stderr. O agent decide retry, fallback ou alertar o usuário.

## FAQ

**O token Apify fica exposto no plugin?**
Não. Cada usuário define o seu `APIFY_TOKEN` localmente. O plugin nunca embute credencial. O scraping vai pra `workspace/` que é gitignored.

**Funciona offline / sem internet?**
Não. Os Actors rodam na nuvem do Apify. `WebSearch` também precisa de internet — sem rede, marketing-os funciona em "modo composição" (geração baseada em conhecimento embutido, sem fact-check).

**Posso adicionar outros Actors (TikTok, LinkedIn)?**
Por design, não no MVP. Se o uso provar valor depois de algumas semanas, é trivial adicionar — basta criar `scripts/apify_<plataforma>.py` seguindo o pattern de `apify_serp.py` e atualizar `_COST_RATES` em `apify_client.py`.

**Quero limitar custo máximo por execução**
Use `--max-results` (SERP) ou `--max-posts` (IG). Hard cap de 100 já está no script.

**Como vejo o que foi salvo até agora?**
```bash
ls -lah workspace/research/apify/
```

**Como deleto resultados antigos?**
```bash
# Remove tudo mais antigo que 30 dias
find workspace/research/apify/ -name "*.json" -mtime +30 -delete
```

## Opt-out completo

Se decidir desinstalar:

1. Remova `APIFY_TOKEN` do shell.
2. Opcional: delete `workspace/research/apify/` (são só JSONs locais, gitignored).
3. Os scripts Python ficam, mas inertes — `mos-seo` e `mos-research` voltam ao comportamento original (WebSearch).

Não há banco de dados, não há config persistente, não há lock-in.

## Arquitetura

```
scripts/
├── apify_client.py       # auth + run-sync + erro + custo (sem CLI próprio)
├── apify_serp.py         # google-search-scraper Actor + CLI
└── apify_instagram.py    # instagram-scraper Actor + CLI

scripts/tests/
├── test_apify_client.py    # 31 tests
├── test_apify_serp.py      # 23 tests
└── test_apify_instagram.py # 29 tests
```

`apify_client.py` usa `urllib.request` da stdlib — sem dependência nova no `requirements.txt`. Mock dos testes via `monkeypatch.setattr` (consistente com `test_notion_api.py`, `test_meta_ads_api.py`).
