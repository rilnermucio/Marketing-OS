# /auditoria-pro: Auditoria Premium Agency-Grade

Comando que produz PDF de 25-30 páginas pronto pra entregar pra cliente final brasileiro. Versão upgrade de `/auditoria` v6.7.0 standard.

## Diferenças vs /auditoria standard

| Item | /auditoria | /auditoria-pro |
|---|---|---|
| Páginas no PDF | 5-8 | 25-30 |
| Prosa por dimensão | 1 frase | 3-5 parágrafos |
| Screenshots | nenhum | homepage + 2-3 internas |
| Radar chart | não | sim, com ghost outline de potencial |
| Roadmap | não | 30/90/180 dias com esforço/impacto/owner |
| Antes/Depois de copy | não | lado-a-lado |
| Tabela competitiva | não | sim, com 3 concorrentes |
| Apêndice raw outputs | não | sim, completo dos 7 agents |
| Glossário | não | filtrado por termos usados |
| Tempo de geração | ~3-5 min | ~6-9 min |

## Setup

Mesmas dependências do /auditoria standard, mais:

```bash
pip install matplotlib playwright
playwright install chromium
```

Custo: $0 (Playwright local, sem Apify mandatory).

## Uso

```
/auditoria-pro https://example.com
```

Output em `workspace/auditorias/<timestamp>-landing-<slug>-pro/`:

```
RELATORIO.html              # HTML renderizado (debug)
RELATORIO.pdf               # PDF agency-grade
scores.json                 # synthesis raw
scoring_output.json         # scoring CLI output
roadmap.json                # roadmap estruturado
screenshots/
  homepage.png
  pricing.png  (se detectada)
  signup.png   (se detectada)
charts/
  radar_scorecard.png
anexos/
  anexo_research.md         # output completo de cada agent
  ...
```

## White-label

Use o mesmo `.auditoria-config.json` do /auditoria standard. A paleta default (deep ink blue + warm orange) é sobrescrita pelas cores do config se presente.

```json
{
  "brand_name": "Sua Agência",
  "primary_color": "#1a1a1a",
  "accent_color": "#0066cc",
  "footer_text": "© 2026 Sua Agência"
}
```

## Limitações na v6.8.0

- **Apenas landing pages.** Para Instagram, Meta Ads ou YouTube, use `/auditoria` standard.
- **Sem bounding boxes nos screenshots.** Anotações são textuais por enquanto. Será adicionado em v6.8.1+.
- **Sem screenshots dos competitors.** Apenas tabela comparativa textual. Apify para visuals em v6.8.1+.
- **Apenas viewport desktop.** Mobile shots em v6.8.1+.

## macOS: Playwright + dylib path

Mesma anotação do `/auditoria` standard: weasyprint precisa de `DYLD_FALLBACK_LIBRARY_PATH=/opt/homebrew/lib` no macOS. O `pdf_generator.py` configura automaticamente.
