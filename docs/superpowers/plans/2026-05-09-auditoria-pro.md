# Auditoria Pro Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Ship `/auditoria-pro <url>` command that produces 25-30 page agency-grade PDF for landing page audits, with radar chart, screenshots, expanded prose synthesis (3-5 paragraphs per dimension), competitive comparison, 30/90/180 day roadmap, and technical appendix.

**Architecture:** Builds on top of v6.7.0 `/auditoria` infrastructure. Adds 5 new Python scripts (audit_screenshot, audit_radar_chart, audit_premium_template, audit_roadmap_generator, audit_glossary) and 1 new command. Reuses audit_detector, audit_scoring, audit_config, pdf_generator (with `--from-html` extension). Synthesis stays in command (no agent modifications). New visual identity: deep ink blue `#0a2540` + warm orange `#ff6b35`.

**Tech Stack:** Python 3.11+, pytest, weasyprint, markdown-it-py, jsonschema (existing). New: matplotlib (radar chart), playwright (screenshots). Reference spec: `docs/superpowers/specs/2026-05-09-auditoria-pro-design.md`.

---

## File Structure

### New files
- `commands/auditoria-pro.md` — premium orchestrator command
- `scripts/audit_screenshot.py` — Playwright screenshot capture
- `scripts/audit_radar_chart.py` — matplotlib radar chart generator
- `scripts/audit_premium_template.py` — premium HTML/CSS template renderer
- `scripts/audit_roadmap_generator.py` — 30/90/180 day roadmap generator
- `scripts/audit_glossary.py` — technical terms glossary (50+ entries)
- `scripts/tests/test_audit_screenshot.py`
- `scripts/tests/test_audit_radar_chart.py`
- `scripts/tests/test_audit_premium_template.py`
- `scripts/tests/test_audit_roadmap_generator.py`
- `scripts/tests/test_audit_glossary.py`
- `scripts/tests/test_auditoria_pro_smoke.py` (`@pytest.mark.smoke`)
- `docs/AUDITORIA-PRO.md` — user-facing doc

### Modified files
- `scripts/pdf_generator.py` — add `--from-html` support
- `scripts/tests/test_pdf_generator.py` — tests for `--from-html`
- `requirements.txt` — add matplotlib, playwright
- `scripts/tests/test_integration_mcp.py` — SCRIPTS_EXCLUIDOS extension
- `scripts/tests/test_workspace_separation.py` — allowlist auditoria-pro.md
- `AGENTS.md` — count 33 → 34, mention /auditoria-pro
- `CHANGELOG.md` — v6.8.0 entry
- `.claude-plugin/plugin.json` — bump 6.7.0 → 6.8.0
- `.claude-plugin/marketplace.json` — bump version

### File responsibilities

| File | Single responsibility |
|---|---|
| `audit_screenshot.py` | URL → PNG screenshots of homepage + internal pages. Pure I/O wrapper around Playwright |
| `audit_radar_chart.py` | Score dict → radar PNG. Pure matplotlib rendering |
| `audit_premium_template.py` | Report data dict → HTML string ready for weasyprint. CSS embedded |
| `audit_roadmap_generator.py` | Fixes list → categorized roadmap dict (30/90/180 buckets) |
| `audit_glossary.py` | Static dict + filter function for technical terms |
| `commands/auditoria-pro.md` | Orchestrate: parse, dispatch agents+screenshots, synthesize, render, generate PDF |

---

## Task 1: Add dependencies and verify environment

**Files:**
- Modify: `requirements.txt`

- [ ] **Step 1: Read current requirements.txt**

Run: `cat /Users/rilner/Code/especializei/esp-marketing-os/requirements.txt`

- [ ] **Step 2: Append new dependencies**

Add at the end of `requirements.txt`:

```
# Dependencias para /auditoria-pro v6.8.0
matplotlib>=3.7
playwright>=1.40
```

- [ ] **Step 3: Install Python deps**

Run: `pip install -r requirements.txt`
Expected: matplotlib + playwright install successfully.

- [ ] **Step 4: Install Playwright Chromium browser**

Run: `playwright install chromium`
Expected: chromium downloaded (~150MB).

- [ ] **Step 5: Verify imports**

Run: `python -c "import matplotlib, playwright; print('ok')"`
Expected output: `ok`

Run: `python -c "from playwright.sync_api import sync_playwright; print('playwright ok')"`
Expected output: `playwright ok`

- [ ] **Step 6: Commit**

```bash
git add requirements.txt
git commit -m "chore(deps): add matplotlib and playwright for /auditoria-pro"
```

---

## Task 2: audit_glossary.py — technical terms dictionary

**Files:**
- Create: `scripts/audit_glossary.py`
- Create: `scripts/tests/test_audit_glossary.py`

- [ ] **Step 1: Write failing tests**

Create `scripts/tests/test_audit_glossary.py`:

```python
"""Tests for audit_glossary.py."""
from __future__ import annotations

import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pytest

from audit_glossary import GLOSSARY, render_glossary_md


class TestGlossaryDict:
    def test_has_at_least_50_terms(self):
        assert len(GLOSSARY) >= 50

    def test_all_entries_have_strings(self):
        for term, definition in GLOSSARY.items():
            assert isinstance(term, str)
            assert isinstance(definition, str)
            assert len(definition) > 20  # meaningful definition

    def test_includes_core_terms(self):
        # Core terms used in audit reports
        for term in ["CWV", "schema markup", "CTA", "value proposition", "SEO"]:
            assert any(term.lower() in k.lower() for k in GLOSSARY.keys()), f"Missing: {term}"


class TestRenderGlossary:
    def test_render_all_when_no_filter(self):
        md = render_glossary_md()
        for term in GLOSSARY:
            assert term in md or term.lower() in md.lower()

    def test_filter_by_used_terms(self):
        used = {"CWV", "schema markup"}
        md = render_glossary_md(used_terms=used)
        # Verify only filtered terms appear
        for term in used:
            assert term in md or term.lower() in md.lower()
        # Verify a non-used term does not appear (pick one not in used set)
        unused_term = next(k for k in GLOSSARY if k not in used)
        # Only check if unused_term has unique enough name
        if len(unused_term) > 5 and unused_term.lower() not in " ".join(used).lower():
            assert unused_term not in md

    def test_render_returns_markdown(self):
        md = render_glossary_md()
        assert "## Glossário" in md
        assert "**" in md  # bold formatting
```

- [ ] **Step 2: Run, verify failures**

Run: `cd /Users/rilner/Code/especializei/esp-marketing-os && python -m pytest scripts/tests/test_audit_glossary.py -v`
Expected: ImportError.

- [ ] **Step 3: Create audit_glossary.py with 50+ terms**

Create `scripts/audit_glossary.py`:

```python
"""Glossário técnico curado pra relatórios /auditoria-pro.

50+ termos técnicos com definições em PT-BR, voltados pra cliente final
não-técnico mas educado. Cada definição: 1-2 frases, sem jargão circular.

Uso: render_glossary_md(used_terms) filtra apenas os termos efetivamente
mencionados no relatório, mantendo a seção de glossário enxuta.
"""
from __future__ import annotations


GLOSSARY: dict[str, str] = {
    "CWV": "Core Web Vitals. Métricas do Google que medem performance percebida pelo usuário: LCP (Largest Contentful Paint), INP (Interaction to Next Paint) e CLS (Cumulative Layout Shift).",
    "LCP": "Largest Contentful Paint. Tempo até o maior elemento da página renderizar. Bom: até 2.5s.",
    "INP": "Interaction to Next Paint. Latência de resposta a interações do usuário. Bom: até 200ms.",
    "CLS": "Cumulative Layout Shift. Quanto a página se reorganiza durante o carregamento. Bom: até 0.1.",
    "schema markup": "Marcação estruturada (geralmente JSON-LD) que ajuda buscadores a entender o conteúdo da página, habilitando rich snippets nos resultados de busca.",
    "JSON-LD": "Formato leve de dados linkados, padrão recomendado pelo Google para schema markup.",
    "rich snippets": "Resultados de busca enriquecidos com informações estruturadas (preço, rating, FAQ), gerados a partir de schema markup.",
    "hreflang": "Atributo HTML que sinaliza variantes de idioma e região de uma página, evitando que o Google penalize conteúdo duplicado entre versões.",
    "CTA": "Call-to-Action. Elemento (botão, link, frase) que pede uma ação específica do usuário. Exemplos: 'Comece agora', 'Falar com vendas'.",
    "value proposition": "Promessa central de valor. O motivo principal pelo qual um usuário deveria escolher um produto vs alternativas. Geralmente comunicada no headline da homepage.",
    "headline": "Título principal de uma página, geralmente acima do fold. Carrega o peso da promessa de valor.",
    "subheadline": "Texto de apoio ao headline, expande ou esclarece a promessa.",
    "above the fold": "Conteúdo visível sem rolar a página. Tradicionalmente o espaço mais valioso da landing.",
    "fold": "Linha horizontal imaginária onde a página é cortada pela parte inferior da viewport.",
    "social proof": "Prova social. Evidências de que outras pessoas/empresas usam o produto: depoimentos, logos, números, reviews.",
    "trust signals": "Sinais de confiança. Elementos que reduzem a percepção de risco do usuário: certificações, garantias, badges de segurança, números de uso.",
    "friction": "Atrito no funil. Qualquer obstáculo que reduz conversão: formulários longos, exigência de cartão, etapas desnecessárias.",
    "funnel": "Funil de conversão. Sequência de etapas que um visitante percorre até virar cliente.",
    "TOFU": "Top of Funnel. Topo do funil. Estágio de descoberta, audiência fria, sem intenção de compra clara.",
    "MOFU": "Middle of Funnel. Meio do funil. Estágio de avaliação, audiência considerando alternativas.",
    "BOFU": "Bottom of Funnel. Fundo do funil. Estágio de decisão, audiência pronta pra comprar ou trocar.",
    "lead magnet": "Conteúdo gratuito (ebook, checklist, webinar) oferecido em troca do email do visitante. Captura de lead no TOFU.",
    "lead": "Pessoa que demonstrou interesse fornecendo dados de contato. Ainda não é cliente.",
    "tripwire": "Oferta de baixo ticket no início do funil pra converter lead em comprador (mesmo de baixo valor) e quebrar a barreira psicológica de pagar.",
    "upsell": "Oferta de produto/plano superior após uma compra inicial.",
    "downsell": "Oferta alternativa de menor valor quando o usuário rejeita o upsell.",
    "PLG": "Product-Led Growth. Modelo de aquisição onde o produto é o motor principal de crescimento (free trial, freemium, viralidade).",
    "AARRR": "Pirate Metrics. Framework de funil: Aquisição, Ativação, Retenção, Receita, Referência (Acquisition, Activation, Retention, Revenue, Referral).",
    "ICP": "Ideal Customer Profile. Perfil ideal de cliente. Características da empresa/persona que melhor encaixa no produto.",
    "persona": "Representação semi-ficcional do cliente ideal, baseada em pesquisa. Inclui demografia, dor, motivação, objeções.",
    "engagement rate": "Taxa de engajamento. Razão entre interações (likes, comments, saves) e seguidores ou impressões.",
    "viewport": "Área visível de uma página em um dispositivo. 'viewport mobile' = 375x812, 'viewport desktop' = 1440x900 ou similar.",
    "responsive design": "Design responsivo. Layout que se adapta automaticamente a diferentes viewports (mobile, tablet, desktop).",
    "mobile-first": "Abordagem de design onde o layout é construído primeiro pra mobile e expande pra telas maiores.",
    "viewport meta tag": "Tag HTML que controla como o navegador mobile renderiza a página. Sem ela, mobile renderiza como desktop e o usuário precisa dar zoom.",
    "WCAG": "Web Content Accessibility Guidelines. Diretrizes do W3C para acessibilidade web. Níveis A, AA, AAA.",
    "contrast ratio": "Razão de contraste entre texto e fundo. WCAG AA exige 4.5:1 para texto normal e 3:1 para texto grande.",
    "alt text": "Texto alternativo de uma imagem. Descrição lida por leitores de tela e usada por buscadores. Imagens decorativas usam alt vazio.",
    "skip link": "Link no topo da página que permite usuários de teclado pular direto pro conteúdo principal, ignorando navegação repetitiva.",
    "ARIA": "Accessible Rich Internet Applications. Conjunto de atributos HTML que ajudam tecnologias assistivas a interpretar componentes complexos.",
    "lazy loading": "Carregamento preguiçoso. Imagens fora do viewport só carregam quando o usuário rola até elas, reduzindo o peso inicial da página.",
    "preload": "Tag HTML que diz ao navegador para baixar um recurso crítico (fonte, imagem hero) antes do parser HTML chegar nele.",
    "preconnect": "Tag HTML que diz ao navegador para abrir conexão antecipada com um domínio externo (CDN, fonts, analytics).",
    "CDN": "Content Delivery Network. Rede de servidores distribuídos geograficamente que serve conteúdo estático (imagens, CSS, JS) com baixa latência.",
    "SSR": "Server-Side Rendering. Renderização da página no servidor antes de enviar pro navegador, melhorando tempo de primeira pintura e SEO.",
    "CSR": "Client-Side Rendering. Renderização no navegador via JavaScript após receber HTML mínimo do servidor. Pior pra SEO se mal configurado.",
    "hydration": "Processo onde o JavaScript do cliente 'reidrata' o HTML estático do SSR, anexando event handlers e tornando a página interativa.",
    "title tag": "Tag HTML <title>. Aparece como título da aba do navegador e como título do resultado nos buscadores. Recomendado: até 60 caracteres.",
    "meta description": "Atributo HTML que descreve a página em ~155 caracteres. Aparece abaixo do title nos resultados de busca. Influencia CTR.",
    "CTR": "Click-Through Rate. Taxa de cliques. Razão entre cliques e impressões. CTR de SERP, de email, de ad creative, etc.",
    "SERP": "Search Engine Results Page. Página de resultados de um buscador.",
    "anchor text": "Texto clicável de um link. Importante pra SEO: descreve o destino do link.",
    "internal linking": "Links entre páginas do mesmo site. Distribui autoridade SEO e melhora navegação.",
    "backlink": "Link de outro site apontando pro seu. Sinal forte de autoridade pro Google.",
    "canonical": "Tag HTML rel=canonical. Aponta a versão 'oficial' de uma página quando há duplicatas, evitando penalidade SEO.",
    "robots.txt": "Arquivo na raiz do site que diz a buscadores quais páginas podem ou não ser rastreadas.",
    "sitemap.xml": "Arquivo XML que lista todas as páginas do site, ajudando buscadores a descobrir conteúdo novo.",
    "ad creative": "Criativo de anúncio. Imagem, vídeo ou texto usado em campanhas pagas.",
    "hook": "Primeiro elemento de um conteúdo (frase, imagem, primeiros 3 segundos) que captura atenção e faz o usuário continuar.",
    "retention": "Retenção. (1) % de usuários que continuam usando o produto ao longo do tempo. (2) % de viewers que assistem além de um certo ponto de um vídeo.",
    "churn": "Cancelamento. Taxa de clientes que deixam o produto em um período.",
    "MRR": "Monthly Recurring Revenue. Receita recorrente mensal. Métrica fundamental de SaaS.",
    "ARR": "Annual Recurring Revenue. MRR x 12.",
    "LTV": "Lifetime Value. Receita total esperada por cliente ao longo do relacionamento.",
    "CAC": "Customer Acquisition Cost. Custo de aquisição por cliente. LTV/CAC > 3 é referência saudável.",
    "ROAS": "Return on Ad Spend. Receita gerada por real investido em ads.",
    "CPA": "Cost Per Acquisition. Custo por aquisição (de lead ou cliente, conforme contexto).",
    "CPM": "Cost Per Mille. Custo por mil impressões. Métrica padrão de exposição em ads.",
}


def render_glossary_md(used_terms: set[str] | None = None) -> str:
    """Render glossary as markdown. Filter by used_terms when provided."""
    if used_terms is None:
        terms_to_render = GLOSSARY
    else:
        terms_to_render = {
            k: v for k, v in GLOSSARY.items()
            if any(t.lower() in k.lower() or k.lower() in t.lower() for t in used_terms)
        }

    if not terms_to_render:
        return ""

    lines = ["## Glossário", "", "Termos técnicos mencionados neste relatório:", ""]
    for term in sorted(terms_to_render):
        lines.append(f"**{term}.** {terms_to_render[term]}")
        lines.append("")
    return "\n".join(lines)
```

- [ ] **Step 4: Run tests, verify pass**

Run: `python -m pytest scripts/tests/test_audit_glossary.py -v`
Expected: 6 passed.

- [ ] **Step 5: Commit**

```bash
git add scripts/audit_glossary.py scripts/tests/test_audit_glossary.py
git commit -m "feat(audit-pro): glossario tecnico curado com 67 termos PT-BR"
```

---

## Task 3: audit_radar_chart.py — radar chart with ghost outline

**Files:**
- Create: `scripts/audit_radar_chart.py`
- Create: `scripts/tests/test_audit_radar_chart.py`

- [ ] **Step 1: Write failing tests**

Create `scripts/tests/test_audit_radar_chart.py`:

```python
"""Tests for audit_radar_chart.py."""
from __future__ import annotations

import os
import sys
from pathlib import Path

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pytest

from audit_radar_chart import generate, _compute_potential_scores


SAMPLE_SCORES = {
    "Conversão (CTA, friction, funil)": 71,
    "Copy (headline, value prop)": 77,
    "SEO (technical + content)": 66,
    "Trust signals": 82,
    "Design (hierarquia visual)": 87,
    "Brand (consistência, voice)": 87,
    "Diferenciação competitiva": 78,
}

SAMPLE_FIXES = {
    "Conversão (CTA, friction, funil)": {"priority": "alta"},
    "Copy (headline, value prop)": {"priority": "alta"},
    "SEO (technical + content)": {"priority": "alta"},
    "Trust signals": {"priority": "media"},
    "Design (hierarquia visual)": {"priority": "media"},
    "Brand (consistência, voice)": {"priority": "media"},
    "Diferenciação competitiva": {"priority": "alta"},
}


class TestGenerate:
    def test_generates_non_empty_png(self, tmp_path: Path):
        out = tmp_path / "radar.png"
        result = generate(SAMPLE_SCORES, SAMPLE_FIXES, out)
        assert result == out
        assert out.exists()
        assert out.stat().st_size > 1000  # PNG with content

    def test_custom_colors_applied(self, tmp_path: Path):
        out = tmp_path / "radar.png"
        generate(SAMPLE_SCORES, SAMPLE_FIXES, out,
                 primary_color="#0a2540", accent_color="#ff6b35")
        assert out.exists()

    def test_handles_partial_scores(self, tmp_path: Path):
        partial = dict(SAMPLE_SCORES)
        partial["SEO (technical + content)"] = None
        out = tmp_path / "radar.png"
        generate(partial, SAMPLE_FIXES, out)
        assert out.exists()


class TestPotentialScores:
    def test_alta_priority_adds_15_points(self):
        scores = {"A": 50}
        fixes = {"A": {"priority": "alta"}}
        potential = _compute_potential_scores(scores, fixes)
        assert potential["A"] == 65  # 50 + 15

    def test_media_priority_adds_5_points(self):
        scores = {"A": 50}
        fixes = {"A": {"priority": "media"}}
        potential = _compute_potential_scores(scores, fixes)
        assert potential["A"] == 55  # 50 + 5

    def test_baixa_priority_adds_2_points(self):
        scores = {"A": 50}
        fixes = {"A": {"priority": "baixa"}}
        potential = _compute_potential_scores(scores, fixes)
        assert potential["A"] == 52

    def test_caps_at_100(self):
        scores = {"A": 95}
        fixes = {"A": {"priority": "alta"}}
        potential = _compute_potential_scores(scores, fixes)
        assert potential["A"] == 100

    def test_none_scores_remain_none(self):
        scores = {"A": None}
        fixes = {"A": {"priority": "alta"}}
        potential = _compute_potential_scores(scores, fixes)
        assert potential["A"] is None
```

- [ ] **Step 2: Run, verify failures**

Run: `python -m pytest scripts/tests/test_audit_radar_chart.py -v`
Expected: ImportError.

- [ ] **Step 3: Implement audit_radar_chart.py**

Create `scripts/audit_radar_chart.py`:

```python
"""Generate radar chart PNG for /auditoria-pro reports.

Two layers:
- Solid colored polygon: current scores (filled with accent_color alpha 0.3)
- Dashed outline: potential scores after priority-alta fixes (estimated)

Uses matplotlib (Agg backend, no display required).
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


_PRIORITY_BOOST = {"alta": 15, "media": 5, "baixa": 2}


def _compute_potential_scores(
    scores: dict[str, int | None],
    fixes: dict[str, dict],
) -> dict[str, int | None]:
    """Estimate scores after applying priority-weighted fixes. Capped at 100."""
    potential = {}
    for dim, score in scores.items():
        if score is None:
            potential[dim] = None
            continue
        fix = fixes.get(dim, {})
        boost = _PRIORITY_BOOST.get(fix.get("priority", "baixa"), 2)
        potential[dim] = min(100, score + boost)
    return potential


def _truncate(label: str, max_len: int = 22) -> str:
    if len(label) <= max_len:
        return label
    return label[: max_len - 1].rstrip() + "…"


def generate(
    scores: dict[str, int | None],
    fixes: dict[str, dict],
    output_path: Path | str,
    primary_color: str = "#0a2540",
    accent_color: str = "#ff6b35",
) -> Path:
    """Render radar chart PNG. Returns output_path."""
    out_path = Path(output_path)
    dimensions = list(scores.keys())
    n = len(dimensions)

    # Replace None with 0 for plotting (visual only)
    current = [scores[d] if scores[d] is not None else 0 for d in dimensions]
    potential_scores = _compute_potential_scores(scores, fixes)
    potential = [potential_scores[d] if potential_scores[d] is not None else 0 for d in dimensions]

    angles = np.linspace(0, 2 * np.pi, n, endpoint=False).tolist()
    angles += angles[:1]
    current += current[:1]
    potential += potential[:1]

    fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True), dpi=200)

    # Potential outline (dashed, behind)
    ax.plot(angles, potential, color=accent_color, linewidth=1.5,
            linestyle="--", alpha=0.6, label="Potencial após fixes priorizados")

    # Current scores (solid filled)
    ax.fill(angles, current, color=accent_color, alpha=0.25)
    ax.plot(angles, current, color=primary_color, linewidth=2.5, label="Score atual")

    # Axis labels
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels([_truncate(d) for d in dimensions], fontsize=9, color=primary_color)

    # Radial gridlines
    ax.set_ylim(0, 100)
    ax.set_yticks([20, 40, 60, 80, 100])
    ax.set_yticklabels(["20", "40", "60", "80", "100"], fontsize=8, color="#6b7280")
    ax.grid(color="#e5e7eb", linewidth=0.8)

    # Style
    ax.spines["polar"].set_color("#e5e7eb")
    ax.set_facecolor("#ffffff")

    # Legend
    ax.legend(loc="upper right", bbox_to_anchor=(1.3, 1.1), fontsize=9, frameon=False)

    plt.tight_layout()
    plt.savefig(out_path, dpi=200, bbox_inches="tight",
                facecolor="white", edgecolor="none", transparent=False)
    plt.close(fig)

    return out_path


def _cli() -> int:
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--scores-json", required=True, help="Path to scoring_output.json")
    parser.add_argument("--output", required=True, help="Output PNG path")
    parser.add_argument("--primary-color", default="#0a2540")
    parser.add_argument("--accent-color", default="#ff6b35")
    args = parser.parse_args()

    data = json.loads(Path(args.scores_json).read_text(encoding="utf-8"))
    scores = {d: info["score"] for d, info in data["dimensions"].items()}
    fixes = {d: info["fix"] for d, info in data["dimensions"].items()}

    generate(scores, fixes, Path(args.output),
             primary_color=args.primary_color, accent_color=args.accent_color)
    print(args.output)
    return 0


if __name__ == "__main__":
    sys.exit(_cli())
```

- [ ] **Step 4: Run tests, verify pass**

Run: `python -m pytest scripts/tests/test_audit_radar_chart.py -v`
Expected: 8 passed.

- [ ] **Step 5: Commit**

```bash
git add scripts/audit_radar_chart.py scripts/tests/test_audit_radar_chart.py
git commit -m "feat(audit-pro): radar chart with ghost outline for potential scores"
```

---

## Task 4: audit_screenshot.py — Playwright capture

**Files:**
- Create: `scripts/audit_screenshot.py`
- Create: `scripts/tests/test_audit_screenshot.py`

- [ ] **Step 1: Write failing tests**

Create `scripts/tests/test_audit_screenshot.py`:

```python
"""Tests for audit_screenshot.py.

Real Playwright runs are marked @pytest.mark.smoke (slow, network).
Unit tests use mocking.
"""
from __future__ import annotations

import os
import sys
from pathlib import Path
from unittest.mock import MagicMock, patch

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pytest

from audit_screenshot import _detect_internal_pages, capture


class TestDetectInternalPages:
    def test_finds_pricing_link(self):
        html = '<html><body><a href="/pricing">Pricing</a></body></html>'
        result = _detect_internal_pages(html, "https://example.com")
        assert "https://example.com/pricing" in result

    def test_finds_signup_link(self):
        html = '<a href="/signup">Sign up</a>'
        result = _detect_internal_pages(html, "https://example.com")
        assert "https://example.com/signup" in result

    def test_ignores_external_links(self):
        html = '<a href="https://other.com/pricing">Other</a>'
        result = _detect_internal_pages(html, "https://example.com")
        assert all("other.com" not in u for u in result)

    def test_max_3_pages(self):
        html = ('<a href="/pricing">P</a><a href="/signup">S</a>'
                '<a href="/contact">C</a><a href="/features">F</a>'
                '<a href="/about">A</a>')
        result = _detect_internal_pages(html, "https://example.com")
        assert len(result) <= 3

    def test_dedupes_urls(self):
        html = '<a href="/pricing">P1</a><a href="/pricing">P2</a>'
        result = _detect_internal_pages(html, "https://example.com")
        assert len([u for u in result if "pricing" in u]) == 1


class TestCaptureMocked:
    @patch("audit_screenshot.sync_playwright")
    def test_capture_returns_dict(self, mock_pw, tmp_path: Path):
        # Mock Playwright context
        mock_browser = MagicMock()
        mock_page = MagicMock()
        mock_page.content.return_value = "<html><body></body></html>"
        mock_browser.new_page.return_value = mock_page
        mock_pw.return_value.__enter__.return_value.chromium.launch.return_value = mock_browser

        result = capture("https://example.com", tmp_path)
        assert "homepage" in result
        assert "internals" in result
        assert "errors" in result

    def test_invalid_url_raises(self, tmp_path: Path):
        with pytest.raises(ValueError, match="URL inválida"):
            capture("not-a-url", tmp_path)


class TestCaptureRealSmoke:
    """Smoke tests with real Playwright. Slow; excluded from default CI."""

    @pytest.mark.smoke
    def test_real_capture_example_com(self, tmp_path: Path):
        result = capture("https://example.com", tmp_path, timeout_ms=15000)
        assert result["homepage"].exists()
        assert result["homepage"].stat().st_size > 1000  # PNG with content
```

- [ ] **Step 2: Run, verify failures**

Run: `python -m pytest scripts/tests/test_audit_screenshot.py -v -m "not smoke"`
Expected: ImportError.

- [ ] **Step 3: Implement audit_screenshot.py**

Create `scripts/audit_screenshot.py`:

```python
"""Capture screenshots of landing page + internal pages via Playwright.

Pure I/O wrapper. Returns paths to PNG files. Errors degrade gracefully
(logged, not raised). Headless Chromium with desktop viewport by default.

CLI: python audit_screenshot.py --url <url> --output-dir <dir>
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from urllib.parse import urljoin, urlparse


_INTERNAL_KEYWORDS = ["pricing", "signup", "sign-up", "register", "contact", "features", "demo", "about"]
_MAX_INTERNAL_PAGES = 3


def _detect_internal_pages(html: str, base_url: str) -> list[str]:
    """Extract up to MAX_INTERNAL_PAGES URLs matching internal keywords. Same-host only."""
    base_host = urlparse(base_url).netloc
    found = []
    seen = set()

    # Match all <a href="..."> links
    href_pattern = re.compile(r'href=["\']([^"\']+)["\']', re.IGNORECASE)
    for match in href_pattern.finditer(html):
        href = match.group(1)
        if href.startswith("#") or href.startswith("mailto:") or href.startswith("tel:"):
            continue

        absolute = urljoin(base_url, href)
        parsed = urlparse(absolute)
        if parsed.netloc != base_host:
            continue

        # Match against keywords
        path_lower = parsed.path.lower()
        if not any(kw in path_lower for kw in _INTERNAL_KEYWORDS):
            continue

        # Dedupe
        normalized = absolute.rstrip("/")
        if normalized in seen:
            continue
        seen.add(normalized)
        found.append(absolute)

        if len(found) >= _MAX_INTERNAL_PAGES:
            break

    return found


def capture(
    url: str,
    output_dir: Path | str,
    viewport: tuple[int, int] = (1440, 900),
    timeout_ms: int = 30000,
) -> dict:
    """Capture screenshots. Returns {homepage: Path, internals: list[Path], errors: list}."""
    if not re.match(r"^https?://", url):
        raise ValueError(f"URL inválida: {url!r}")

    out_dir = Path(output_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    from playwright.sync_api import sync_playwright

    result = {"homepage": None, "internals": [], "errors": []}

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        try:
            context = browser.new_context(
                viewport={"width": viewport[0], "height": viewport[1]},
                user_agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) auditoria-pro",
            )
            page = context.new_page()

            # Capture homepage
            try:
                page.goto(url, wait_until="networkidle", timeout=timeout_ms)
                homepage_path = out_dir / "homepage.png"
                page.screenshot(path=str(homepage_path), full_page=True)
                result["homepage"] = homepage_path

                # Detect internal pages from rendered HTML
                html = page.content()
                internal_urls = _detect_internal_pages(html, url)

                for internal_url in internal_urls:
                    try:
                        page.goto(internal_url, wait_until="networkidle", timeout=timeout_ms)
                        slug = re.sub(r"\W+", "-", urlparse(internal_url).path.strip("/"))[:40] or "page"
                        internal_path = out_dir / f"{slug}.png"
                        page.screenshot(path=str(internal_path), full_page=True)
                        result["internals"].append(internal_path)
                    except Exception as e:
                        result["errors"].append(f"internal {internal_url}: {e}")

            except Exception as e:
                result["errors"].append(f"homepage: {e}")

        finally:
            browser.close()

    return result


def _cli() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", required=True)
    parser.add_argument("--output-dir", required=True)
    parser.add_argument("--viewport", default="1440x900")
    parser.add_argument("--timeout-ms", type=int, default=30000)
    args = parser.parse_args()

    w, h = args.viewport.split("x")
    result = capture(args.url, args.output_dir, viewport=(int(w), int(h)), timeout_ms=args.timeout_ms)

    out = {
        "homepage": str(result["homepage"]) if result["homepage"] else None,
        "internals": [str(p) for p in result["internals"]],
        "errors": result["errors"],
    }
    print(json.dumps(out, ensure_ascii=False))
    return 0 if result["homepage"] else 1


if __name__ == "__main__":
    sys.exit(_cli())
```

- [ ] **Step 4: Run unit tests, verify pass**

Run: `python -m pytest scripts/tests/test_audit_screenshot.py -v -m "not smoke"`
Expected: 7 passed (5 internal pages tests + 2 capture mocked).

- [ ] **Step 5: Run smoke test (optional, real Playwright)**

Run: `python -m pytest scripts/tests/test_audit_screenshot.py -v -m smoke`
Expected: 1 passed (real example.com screenshot, ~10-15s).

- [ ] **Step 6: Commit**

```bash
git add scripts/audit_screenshot.py scripts/tests/test_audit_screenshot.py
git commit -m "feat(audit-pro): Playwright screenshot capture with internal page detection"
```

---

## Task 5: audit_roadmap_generator.py — 30/90/180 buckets

**Files:**
- Create: `scripts/audit_roadmap_generator.py`
- Create: `scripts/tests/test_audit_roadmap_generator.py`

- [ ] **Step 1: Write failing tests**

Create `scripts/tests/test_audit_roadmap_generator.py`:

```python
"""Tests for audit_roadmap_generator.py."""
from __future__ import annotations

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pytest

from audit_roadmap_generator import (
    generate,
    _estimate_effort,
    _suggest_owner,
)


class TestGenerate:
    def test_alta_priority_low_score_high_weight_to_30_days(self):
        fixes = [{
            "dimension": "Conversão (CTA, friction, funil)",
            "score": 50,
            "fix": {"text": "Adicionar CTA secundário", "priority": "alta"},
        }]
        rubric_weights = {"Conversão (CTA, friction, funil)": 25}
        result = generate(fixes, rubric_weights)
        assert any(item["dimension"].startswith("Conversão")
                   for item in result["30_days"])

    def test_media_priority_to_90_days(self):
        fixes = [{
            "dimension": "Trust signals",
            "score": 70,
            "fix": {"text": "Adicionar depoimentos", "priority": "media"},
        }]
        rubric_weights = {"Trust signals": 10}
        result = generate(fixes, rubric_weights)
        assert any(item["dimension"] == "Trust signals" for item in result["90_days"])

    def test_baixa_priority_to_180_days(self):
        fixes = [{
            "dimension": "Brand (consistência, voice)",
            "score": 85,
            "fix": {"text": "Refinar voz em FAQ", "priority": "baixa"},
        }]
        rubric_weights = {"Brand (consistência, voice)": 10}
        result = generate(fixes, rubric_weights)
        assert any(item["dimension"].startswith("Brand")
                   for item in result["180_days"])

    def test_each_item_has_required_fields(self):
        fixes = [{
            "dimension": "Conversão",
            "score": 60,
            "fix": {"text": "X", "priority": "alta"},
        }]
        rubric_weights = {"Conversão": 25}
        result = generate(fixes, rubric_weights)
        for bucket in ("30_days", "90_days", "180_days"):
            for item in result[bucket]:
                assert "action" in item
                assert "dimension" in item
                assert "effort" in item
                assert item["effort"] in ("S", "M", "L")
                assert "impact" in item
                assert item["impact"] in ("alto", "medio", "baixo")
                assert "owner" in item


class TestEstimateEffort:
    def test_redesign_keyword_returns_L(self):
        assert _estimate_effort("Redesign do hero section") == "L"

    def test_reescrever_keyword_returns_M(self):
        assert _estimate_effort("Reescrever title tag") == "M"

    def test_simple_returns_S(self):
        assert _estimate_effort("Adicionar 1 selo de segurança") == "S"

    def test_create_keyword_returns_M(self):
        assert _estimate_effort("Criar lead magnet") == "M"


class TestSuggestOwner:
    def test_conversao_to_growth(self):
        assert _suggest_owner("Conversão (CTA, friction, funil)") == "Growth Lead"

    def test_copy_to_copywriter(self):
        assert _suggest_owner("Copy (headline, value prop)") == "Copywriter"

    def test_seo_to_seo_specialist(self):
        assert _suggest_owner("SEO (technical + content)") == "SEO Specialist"

    def test_design_to_design(self):
        assert _suggest_owner("Design (hierarquia visual)") == "Designer"

    def test_unknown_to_marketing_lead(self):
        assert _suggest_owner("Unknown Dimension") == "Marketing Lead"
```

- [ ] **Step 2: Run, verify failures**

Run: `python -m pytest scripts/tests/test_audit_roadmap_generator.py -v`
Expected: ImportError.

- [ ] **Step 3: Implement audit_roadmap_generator.py**

Create `scripts/audit_roadmap_generator.py`:

```python
"""Generate 30/90/180 day roadmap from audit fixes.

Heuristic bucketing:
- 30 days: priority alta + score < 70 + weight >= 15 (high impact, urgent)
- 90 days: priority alta + medium weight, OR priority media + low score
- 180 days: priority baixa, OR priority media + high score, OR remaining

Each item has: action, dimension, effort (S/M/L), impact (alto/medio/baixo), owner.
"""
from __future__ import annotations

import json
import sys


_OWNER_MAP = {
    "Conversão": "Growth Lead",
    "Copy": "Copywriter",
    "SEO": "SEO Specialist",
    "Trust": "Growth Lead",
    "Design": "Designer",
    "Brand": "Brand Manager",
    "Diferenciação": "Marketing Lead",
    "Bio": "Social Media Manager",
    "Hooks": "Content Lead",
    "Strategy": "Content Lead",
    "Engagement": "Social Media Manager",
    "Cadência": "Content Lead",
    "Visual": "Designer",
}


_EFFORT_KEYWORDS_L = ["redesign", "refazer", "reestruturar", "criar do zero", "rebuild"]
_EFFORT_KEYWORDS_M = ["reescrever", "criar", "implementar", "adicionar lead magnet",
                      "construir", "desenvolver", "configurar"]


def _estimate_effort(fix_text: str) -> str:
    """S = small (<1 day), M = medium (1-5 days), L = large (>1 week)."""
    text_lower = fix_text.lower()
    for kw in _EFFORT_KEYWORDS_L:
        if kw in text_lower:
            return "L"
    for kw in _EFFORT_KEYWORDS_M:
        if kw in text_lower:
            return "M"
    return "S"


def _suggest_owner(dimension: str) -> str:
    """Map dimension name to suggested owner role."""
    for prefix, owner in _OWNER_MAP.items():
        if prefix.lower() in dimension.lower():
            return owner
    return "Marketing Lead"


def _impact_from_priority_and_weight(priority: str, weight: int) -> str:
    if priority == "alta" and weight >= 15:
        return "alto"
    if priority == "alta" or weight >= 20:
        return "alto"
    if priority == "media":
        return "medio"
    return "baixo"


def _bucket_for(priority: str, score: int, weight: int) -> str:
    """Decide which bucket a fix belongs to."""
    if priority == "alta" and score < 70 and weight >= 15:
        return "30_days"
    if priority == "alta":
        return "30_days" if score < 80 else "90_days"
    if priority == "media":
        return "90_days" if score < 75 else "180_days"
    return "180_days"


def generate(fixes: list[dict], rubric_weights: dict[str, int]) -> dict:
    """Generate roadmap dict with 3 buckets."""
    result = {"30_days": [], "90_days": [], "180_days": []}

    for fix_entry in fixes:
        dim = fix_entry["dimension"]
        score = fix_entry.get("score", 50)
        fix_data = fix_entry.get("fix", {})
        text = fix_data.get("text", "")
        priority = fix_data.get("priority", "baixa")
        weight = rubric_weights.get(dim, 10)

        bucket = _bucket_for(priority, score, weight)
        item = {
            "action": text,
            "dimension": dim,
            "effort": _estimate_effort(text),
            "impact": _impact_from_priority_and_weight(priority, weight),
            "owner": _suggest_owner(dim),
            "priority": priority,
        }
        result[bucket].append(item)

    return result


def _cli() -> int:
    payload = json.loads(sys.stdin.read())

    # Accept either scoring_output.json structure or simpler {fixes, weights}
    if "dimensions" in payload:
        # scoring_output.json format
        fixes = []
        weights = {}
        for dim, info in payload["dimensions"].items():
            fixes.append({
                "dimension": dim,
                "score": info["score"] if info["score"] is not None else 50,
                "fix": info["fix"],
            })
            weights[dim] = info["weight"]
    else:
        fixes = payload["fixes"]
        weights = payload.get("rubric_weights", {})

    result = generate(fixes, weights)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(_cli())
```

- [ ] **Step 4: Run tests, verify pass**

Run: `python -m pytest scripts/tests/test_audit_roadmap_generator.py -v`
Expected: 12 passed.

- [ ] **Step 5: Commit**

```bash
git add scripts/audit_roadmap_generator.py scripts/tests/test_audit_roadmap_generator.py
git commit -m "feat(audit-pro): roadmap generator with 30/90/180 day buckets"
```

---

## Task 6: audit_premium_template.py — HTML/CSS premium template

**Files:**
- Create: `scripts/audit_premium_template.py`
- Create: `scripts/tests/test_audit_premium_template.py`

This is the largest task. The template renders 10 sections with embedded CSS. Total ~600 lines split across structure + CSS + render functions.

- [ ] **Step 1: Write failing tests**

Create `scripts/tests/test_audit_premium_template.py`:

```python
"""Tests for audit_premium_template.py."""
from __future__ import annotations

import os
import sys
from pathlib import Path

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pytest

from audit_premium_template import render, _render_cover, _render_dimension_section


SAMPLE_DATA = {
    "client_url": "https://stripe.com",
    "client_name": "stripe.com",
    "audit_type": "landing",
    "timestamp": "2026-05-09 10:25:07",
    "overall_score": 76,
    "partial": False,
    "exec_summary": "Stripe entrega execução de classe mundial...",
    "dimensions": {
        "Conversão (CTA, friction, funil)": {
            "score": 71,
            "weight": 25,
            "evidences": [
                "Pricing com fees ocultos",
                "Sem lead magnet ativo",
                "CTA único pra audiências heterogêneas",
            ],
            "fixes": [
                {"text": "Adicionar CTA secundário", "priority": "alta"},
            ],
            "prose": "Esta é a maior alavanca de melhoria identificada na auditoria...",
            "before_after": [
                {"before": "Start now", "after": "Start building free (devs)"},
            ],
            "agent_citation": "Conforme análise mos-funnel: 'O caminho é linear...'",
        },
    },
    "competitive": {
        "competitors": [
            {"name": "Adyen", "differentiation": "..."},
            {"name": "PayPal", "differentiation": "..."},
        ],
        "table_md": "| Dimensão | Cliente | Adyen | PayPal |\n|---|---|---|---|\n| ... |",
    },
    "roadmap": {
        "30_days": [{"action": "X", "dimension": "Y", "effort": "S", "impact": "alto", "owner": "Z"}],
        "90_days": [],
        "180_days": [],
    },
    "appendix": {
        "research": "raw output...",
        "seo": "raw output...",
    },
}

SAMPLE_SCREENSHOTS = {
    "homepage": "/tmp/homepage.png",
    "internals": ["/tmp/pricing.png"],
}

SAMPLE_CHARTS = {
    "radar": "/tmp/radar.png",
}


class TestRender:
    def test_render_returns_valid_html(self):
        html = render(SAMPLE_DATA, SAMPLE_SCREENSHOTS, SAMPLE_CHARTS, config=None)
        assert html.startswith("<!DOCTYPE html>")
        assert "</html>" in html

    def test_html_contains_all_sections(self):
        html = render(SAMPLE_DATA, SAMPLE_SCREENSHOTS, SAMPLE_CHARTS, config=None)
        # Cover
        assert "stripe.com" in html
        # Exec summary
        assert "Stripe entrega" in html
        # Scorecard with score
        assert "76" in html
        # Dimension prose
        assert "Esta é a maior alavanca" in html
        # Roadmap
        assert "30 dias" in html or "30_days" in html
        # Appendix
        assert "raw output" in html

    def test_html_includes_premium_palette(self):
        html = render(SAMPLE_DATA, SAMPLE_SCREENSHOTS, SAMPLE_CHARTS, config=None)
        assert "#0a2540" in html  # primary
        assert "#ff6b35" in html  # accent

    def test_white_label_overrides_palette(self):
        config = {"brand_name": "Acme", "primary_color": "#000000", "accent_color": "#ff0000"}
        html = render(SAMPLE_DATA, SAMPLE_SCREENSHOTS, SAMPLE_CHARTS, config=config)
        assert "#000000" in html
        assert "#ff0000" in html
        assert "Acme" in html


class TestCover:
    def test_cover_includes_client_name(self):
        html = _render_cover(SAMPLE_DATA, config=None)
        assert "stripe.com" in html

    def test_cover_full_bleed(self):
        html = _render_cover(SAMPLE_DATA, config=None)
        assert "cover" in html.lower()


class TestDimensionSection:
    def test_dimension_section_renders_prose(self):
        dim_data = SAMPLE_DATA["dimensions"]["Conversão (CTA, friction, funil)"]
        html = _render_dimension_section("Conversão (CTA, friction, funil)", dim_data, screenshot=None)
        assert "Esta é a maior alavanca" in html
        assert "71" in html
        assert "25" in html  # weight

    def test_dimension_section_renders_before_after(self):
        dim_data = SAMPLE_DATA["dimensions"]["Conversão (CTA, friction, funil)"]
        html = _render_dimension_section("Conversão (CTA, friction, funil)", dim_data, screenshot=None)
        assert "Start now" in html
        assert "Start building free" in html

    def test_priority_class_applied(self):
        dim_data = SAMPLE_DATA["dimensions"]["Conversão (CTA, friction, funil)"]
        html = _render_dimension_section("Conversão (CTA, friction, funil)", dim_data, screenshot=None)
        assert "priority-alta" in html
```

- [ ] **Step 2: Run, verify failures**

Run: `python -m pytest scripts/tests/test_audit_premium_template.py -v`
Expected: ImportError.

- [ ] **Step 3: Implement audit_premium_template.py**

Create `scripts/audit_premium_template.py`. This file is ~600 lines; structure below. Implement in this order:

```python
"""Premium HTML/CSS template renderer for /auditoria-pro PDF reports.

Renders 10 sections: cover, executive summary, methodology, visual scorecard,
per-dimension analysis (7), competitive comparison, roadmap, appendix, glossary,
next steps. CSS embedded for weasyprint compatibility.

Visual identity: deep ink blue #0a2540 + warm orange #ff6b35.
"""
from __future__ import annotations

from html import escape
from pathlib import Path


_DEFAULT_CONFIG = {
    "brand_name": "marketing-os",
    "primary_color": "#0a2540",
    "accent_color": "#ff6b35",
    "footer_text": "Auditoria Pro · marketing-os",
    "logo_path": None,
}


_CSS = """
:root {
  --primary: {primary};
  --accent: {accent};
  --text: #1a1a1a;
  --muted: #6b7280;
  --bg-soft: #f9fafb;
  --border: #e5e7eb;
  --success: #16a34a;
  --warning: #f59e0b;
  --danger: #dc2626;
}
@page { size: A4; margin: 2.5cm 2cm; @bottom-right { content: "Página " counter(page) " de " counter(pages); font-size: 9pt; color: var(--muted); } }
@page :first { margin: 0; @bottom-right { content: ""; } }
* { box-sizing: border-box; }
body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", system-ui, sans-serif; color: var(--text); line-height: 1.55; font-size: 11pt; margin: 0; }
.page { page-break-before: always; padding: 0; }
.page:first-of-type { page-break-before: auto; }
.cover { width: 100%; height: 297mm; background: linear-gradient(135deg, var(--primary) 0%, #1a3a5c 100%); color: white; padding: 60mm 30mm; display: flex; flex-direction: column; justify-content: space-between; }
.cover-brand { font-size: 14pt; font-weight: 600; letter-spacing: 1px; text-transform: uppercase; opacity: 0.85; }
.cover-title { font-size: 48pt; font-weight: 700; line-height: 1.1; margin-top: 40pt; }
.cover-client { font-size: 24pt; font-weight: 400; margin-top: 12pt; opacity: 0.9; }
.cover-meta { display: flex; flex-direction: column; gap: 6pt; font-size: 11pt; opacity: 0.8; margin-top: 60pt; }
.cover-confidential { display: inline-block; background: var(--accent); color: white; padding: 4pt 12pt; border-radius: 4pt; font-size: 10pt; font-weight: 600; letter-spacing: 1px; text-transform: uppercase; align-self: flex-end; }
h1 { font-size: 28pt; color: var(--primary); font-weight: 700; margin: 0 0 16pt 0; line-height: 1.2; }
h2 { font-size: 20pt; color: var(--accent); font-weight: 600; border-bottom: 2px solid var(--accent); padding-bottom: 8pt; margin: 28pt 0 12pt 0; }
h3 { font-size: 14pt; color: var(--primary); font-weight: 600; margin: 18pt 0 8pt 0; }
h4 { font-size: 11pt; color: var(--primary); font-weight: 600; margin: 12pt 0 4pt 0; text-transform: uppercase; letter-spacing: 0.5px; }
p { margin: 0 0 10pt 0; text-align: justify; }
.score-big { font-size: 96pt; color: var(--primary); font-weight: 700; line-height: 1; text-align: center; margin: 20pt 0; }
.score-label { text-align: center; font-size: 13pt; color: var(--muted); text-transform: uppercase; letter-spacing: 2px; margin-top: -10pt; }
.exec-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 24pt; margin-top: 24pt; }
.exec-card { background: var(--bg-soft); border-left: 4px solid var(--accent); padding: 16pt; border-radius: 4pt; }
.exec-card.strength { border-left-color: var(--success); }
table { width: 100%; border-collapse: collapse; margin: 12pt 0; font-size: 10pt; }
table thead { background: var(--primary); color: white; }
table th, table td { padding: 8pt 10pt; text-align: left; border-bottom: 1px solid var(--border); }
table tbody tr:nth-child(even) { background: var(--bg-soft); }
.scorecard-status { padding: 2pt 8pt; border-radius: 3pt; font-size: 9pt; font-weight: 600; }
.status-forte { background: #dcfce7; color: #166534; }
.status-ok { background: #fef3c7; color: #92400e; }
.status-atencao { background: #fee2e2; color: #991b1b; }
.priority-alta { background: #fee2e2; color: #991b1b; padding: 2pt 8pt; border-radius: 3pt; font-size: 9pt; font-weight: 600; }
.priority-media { background: #fef3c7; color: #92400e; padding: 2pt 8pt; border-radius: 3pt; font-size: 9pt; font-weight: 600; }
.priority-baixa { background: #dbeafe; color: #1e40af; padding: 2pt 8pt; border-radius: 3pt; font-size: 9pt; font-weight: 600; }
.dimension-section { page-break-inside: avoid; margin-bottom: 24pt; }
.dimension-header { display: flex; justify-content: space-between; align-items: baseline; border-bottom: 1px solid var(--border); padding-bottom: 8pt; }
.dimension-score-pill { font-size: 24pt; color: var(--primary); font-weight: 700; }
.dimension-prose { margin: 12pt 0; }
.evidences-list { background: var(--bg-soft); padding: 12pt 16pt; border-radius: 4pt; margin: 12pt 0; }
.evidences-list ul { margin: 6pt 0; padding-left: 20pt; }
.before-after { display: grid; grid-template-columns: 1fr 1fr; gap: 16pt; margin: 12pt 0; }
.before-after-card { padding: 12pt; border-radius: 4pt; }
.before-card { background: #fee2e2; border-left: 3pt solid var(--danger); }
.after-card { background: #dcfce7; border-left: 3pt solid var(--success); }
.before-after-label { font-size: 9pt; text-transform: uppercase; letter-spacing: 1px; font-weight: 700; margin-bottom: 4pt; }
blockquote.agent-citation { border-left: 3pt solid var(--accent); padding: 8pt 16pt; margin: 12pt 0; color: var(--muted); font-style: italic; background: var(--bg-soft); }
img.screenshot { max-width: 100%; border: 1px solid var(--border); border-radius: 4pt; margin: 12pt 0; }
img.radar-chart { max-width: 600px; display: block; margin: 16pt auto; }
.competitive-grid { display: grid; grid-template-columns: repeat(2, 1fr); gap: 16pt; margin: 16pt 0; }
.competitor-card { background: var(--bg-soft); padding: 16pt; border-radius: 4pt; }
.roadmap-bucket { margin: 16pt 0; }
.roadmap-bucket-header { display: flex; align-items: center; gap: 12pt; margin-bottom: 8pt; }
.roadmap-bucket-title { font-size: 13pt; color: var(--primary); font-weight: 700; }
.roadmap-bucket-pill { padding: 2pt 12pt; background: var(--accent); color: white; border-radius: 99pt; font-size: 9pt; font-weight: 600; }
.appendix-agent { page-break-inside: avoid; margin: 20pt 0; padding: 16pt; background: var(--bg-soft); border-radius: 4pt; }
.appendix-agent-header { font-size: 13pt; font-weight: 700; color: var(--primary); margin-bottom: 12pt; }
.glossary dt { font-weight: 700; color: var(--primary); margin-top: 8pt; }
.glossary dd { margin: 0 0 12pt 0; padding-left: 0; color: var(--text); }
.next-steps-box { background: var(--primary); color: white; padding: 24pt; border-radius: 4pt; margin: 16pt 0; }
.next-steps-box h2 { color: white; border-bottom-color: rgba(255,255,255,0.3); }
.muted { color: var(--muted); font-size: 10pt; }
.divider { height: 1px; background: var(--border); margin: 20pt 0; }
"""


def _render_cover(data: dict, config: dict | None) -> str:
    cfg = {**_DEFAULT_CONFIG, **(config or {})}
    brand = escape(cfg["brand_name"])
    client = escape(data["client_name"])
    url = escape(data["client_url"])
    audit_type = escape(data["audit_type"])
    ts = escape(data["timestamp"])
    return f"""
    <section class="cover">
      <div>
        <div class="cover-brand">{brand}</div>
        <h1 class="cover-title" style="color: white;">Auditoria Pro</h1>
        <div class="cover-client">{client}</div>
        <div class="cover-meta">
          <div>URL: {url}</div>
          <div>Tipo: {audit_type}</div>
          <div>Data: {ts}</div>
        </div>
      </div>
      <div class="cover-confidential">Confidencial</div>
    </section>
    """


def _render_executive_summary(data: dict) -> str:
    score = data["overall_score"]
    summary = escape(data["exec_summary"])
    partial_label = " (parcial)" if data.get("partial") else ""
    return f"""
    <section class="page">
      <h1>Sumário Executivo</h1>
      <div class="score-big">{score}</div>
      <div class="score-label">Score Geral{escape(partial_label)} · 0 a 100</div>
      <div class="divider"></div>
      <p>{summary}</p>
    </section>
    """


def _render_methodology() -> str:
    return """
    <section class="page">
      <h1>Metodologia</h1>
      <p>Esta auditoria foi conduzida via dispatch paralelo de 7 agents especializados (research, SEO, copy, funnel, ads, design, brand) que analisaram a landing page usando WebFetch e conhecimento público setorizado. As respostas foram sintetizadas via rubric ponderada de 7 dimensões.</p>
      <h2>Dimensões avaliadas</h2>
      <table>
        <thead><tr><th>Dimensão</th><th>Peso</th><th>Foco</th></tr></thead>
        <tbody>
          <tr><td>Conversão (CTA, friction, funil)</td><td>25%</td><td>Caminho até a ação principal, atrito, lead magnets</td></tr>
          <tr><td>Copy (headline, value prop)</td><td>20%</td><td>Clareza, persuasão, especificidade</td></tr>
          <tr><td>SEO (technical + content)</td><td>15%</td><td>Title, meta, schema, performance, mobile</td></tr>
          <tr><td>Trust signals</td><td>10%</td><td>Prova social, garantias, autoridade</td></tr>
          <tr><td>Design (hierarquia visual)</td><td>10%</td><td>Hierarquia, tipografia, acessibilidade</td></tr>
          <tr><td>Brand (consistência, voice)</td><td>10%</td><td>Voice, identidade, persona</td></tr>
          <tr><td>Diferenciação competitiva</td><td>10%</td><td>Posicionamento vs alternativas</td></tr>
        </tbody>
      </table>
      <h2>Frameworks aplicados</h2>
      <p>Análise de copy via 4Us (Útil, Urgente, Único, Específico), princípios de Cialdini para trust signals, hierarquia visual via Gestalt, scoring de fricção segundo Sugarman.</p>
      <h2>Limitações declaradas</h2>
      <p>A análise considerou exclusivamente conteúdo público acessível via WebFetch e WebSearch. Dados internos (analytics, funil real, ROI de campanhas) não estão refletidos.</p>
    </section>
    """


def _render_visual_scorecard(data: dict, charts: dict) -> str:
    radar_path = charts.get("radar")
    radar_html = f'<img class="radar-chart" src="file://{radar_path}" alt="Radar de scores" />' if radar_path else ""

    rows = []
    for dim, info in data["dimensions"].items():
        score = info["score"]
        weight = info["weight"]
        if score is None:
            status = "N/D"
            cls = "scorecard-status"
            score_str = "N/D"
        elif score >= 80:
            status = "Forte"
            cls = "scorecard-status status-forte"
            score_str = str(score)
        elif score >= 60:
            status = "OK"
            cls = "scorecard-status status-ok"
            score_str = str(score)
        else:
            status = "Atenção"
            cls = "scorecard-status status-atencao"
            score_str = str(score)
        rows.append(f"<tr><td>{escape(dim)}</td><td>{weight}%</td><td>{score_str}</td><td><span class='{cls}'>{status}</span></td></tr>")

    return f"""
    <section class="page">
      <h1>Diagnóstico Visual</h1>
      {radar_html}
      <h2>Scorecard</h2>
      <table>
        <thead><tr><th>Dimensão</th><th>Peso</th><th>Score</th><th>Status</th></tr></thead>
        <tbody>{''.join(rows)}</tbody>
      </table>
    </section>
    """


def _render_dimension_section(name: str, data: dict, screenshot: str | None) -> str:
    score = data.get("score", "N/D")
    weight = data.get("weight", 0)
    prose = escape(data.get("prose", ""))
    evidences = data.get("evidences", [])
    fixes = data.get("fixes", [])
    before_after = data.get("before_after", [])
    citation = data.get("agent_citation", "")

    evid_html = "<ul>" + "".join(f"<li>{escape(e)}</li>" for e in evidences) + "</ul>" if evidences else ""
    fixes_html = ""
    for fix in fixes:
        prio = fix.get("priority", "baixa")
        fixes_html += f'<p><span class="priority-{prio}">{prio.upper()}</span> {escape(fix["text"])}</p>'

    ba_html = ""
    if before_after:
        ba_html = "<h4>Antes vs Depois (Copy sugerido)</h4><div class='before-after'>"
        for ba in before_after:
            ba_html += f"""
            <div class="before-after-card before-card">
              <div class="before-after-label">Antes</div>
              <div>{escape(ba['before'])}</div>
            </div>
            <div class="before-after-card after-card">
              <div class="before-after-label">Depois</div>
              <div>{escape(ba['after'])}</div>
            </div>
            """
        ba_html += "</div>"

    citation_html = f'<blockquote class="agent-citation">{escape(citation)}</blockquote>' if citation else ""
    screenshot_html = f'<img class="screenshot" src="file://{screenshot}" alt="Screenshot" />' if screenshot else ""

    return f"""
    <section class="dimension-section">
      <div class="dimension-header">
        <h2 style="border:none; margin:0;">{escape(name)}</h2>
        <div class="dimension-score-pill">{score}<span style="font-size:14pt; color:var(--muted);"> / 100 · peso {weight}%</span></div>
      </div>
      <div class="dimension-prose"><p>{prose}</p></div>
      {screenshot_html}
      <h4>Evidências observadas</h4>
      <div class="evidences-list">{evid_html}</div>
      {ba_html}
      <h4>Fix priorizado</h4>
      {fixes_html}
      {citation_html}
    </section>
    """


def _render_competitive(data: dict) -> str:
    competitive = data.get("competitive", {})
    competitors = competitive.get("competitors", [])
    table = competitive.get("table_md", "")
    cards = "".join(
        f'<div class="competitor-card"><h3>{escape(c["name"])}</h3><p>{escape(c.get("differentiation", ""))}</p></div>'
        for c in competitors
    )
    return f"""
    <section class="page">
      <h1>Análise Competitiva</h1>
      <p>Posicionamento da auditoria em relação aos principais concorrentes diretos identificados durante o research.</p>
      <div class="competitive-grid">{cards}</div>
      <h2>Tabela comparativa</h2>
      <div>{table}</div>
    </section>
    """


def _render_roadmap(roadmap: dict) -> str:
    def render_bucket(title: str, pill: str, items: list) -> str:
        if not items:
            return f"<div class='roadmap-bucket'><div class='roadmap-bucket-header'><div class='roadmap-bucket-title'>{title}</div><div class='roadmap-bucket-pill'>{pill}</div></div><p class='muted'>Sem itens críticos.</p></div>"
        rows = "".join(
            f"<tr><td>{escape(item['action'])}</td><td>{escape(item['dimension'])}</td><td>{item['effort']}</td><td>{item['impact']}</td><td>{escape(item['owner'])}</td></tr>"
            for item in items
        )
        return f"""
        <div class="roadmap-bucket">
          <div class="roadmap-bucket-header">
            <div class="roadmap-bucket-title">{title}</div>
            <div class="roadmap-bucket-pill">{pill}</div>
          </div>
          <table>
            <thead><tr><th>Ação</th><th>Dimensão</th><th>Esforço</th><th>Impacto</th><th>Owner sugerido</th></tr></thead>
            <tbody>{rows}</tbody>
          </table>
        </div>
        """

    return f"""
    <section class="page">
      <h1>Roadmap de Implementação</h1>
      <p>Sequenciamento dos fixes identificados, organizados por horizonte de execução. Esforço S/M/L (small/medium/large) e impacto estimado.</p>
      {render_bucket("Quick wins", "30 dias", roadmap.get("30_days", []))}
      {render_bucket("Impacto estruturante", "90 dias", roadmap.get("90_days", []))}
      {render_bucket("Transformações de fundo", "180 dias", roadmap.get("180_days", []))}
    </section>
    """


def _render_appendix(data: dict) -> str:
    appendix = data.get("appendix", {})
    sections = []
    for agent, raw in appendix.items():
        sections.append(f"""
        <details class="appendix-agent">
          <summary class="appendix-agent-header">Output completo: mos-{escape(agent)}</summary>
          <pre style="white-space: pre-wrap; font-size: 9pt;">{escape(raw)}</pre>
        </details>
        """)
    return f"""
    <section class="page">
      <h1>Apêndice Técnico</h1>
      <p>Outputs completos dos 7 agents. Use como referência pra desenvolvedores e especialistas.</p>
      {''.join(sections)}
    </section>
    """


def _render_glossary(used_terms: set | None = None) -> str:
    from audit_glossary import render_glossary_md

    md = render_glossary_md(used_terms)
    if not md:
        return ""

    # Convert simple markdown to HTML manually (preserving structure)
    lines = md.split("\n")
    html_parts = ["<section class='page'>", "<h1>Glossário</h1>"]
    in_dl = False
    for line in lines:
        if line.startswith("##"):
            continue  # already have h1
        if line.startswith("**") and "." in line:
            term, _, definition = line.partition(".** ")
            term = term.lstrip("*").rstrip("*")
            if not in_dl:
                html_parts.append("<dl class='glossary'>")
                in_dl = True
            html_parts.append(f"<dt>{escape(term)}</dt><dd>{escape(definition)}</dd>")
    if in_dl:
        html_parts.append("</dl>")
    html_parts.append("</section>")
    return "\n".join(html_parts)


def _render_next_steps(config: dict | None) -> str:
    cfg = {**_DEFAULT_CONFIG, **(config or {})}
    return f"""
    <section class="page">
      <h1>Próximos Passos</h1>
      <div class="next-steps-box">
        <h2 style="margin-top:0;">Como avançar</h2>
        <p>Esta auditoria identifica oportunidades específicas. A implementação dos fixes priorizados costuma gerar lift mensurável em 30-90 dias quando executada com disciplina.</p>
        <h3 style="color:white; margin-top:20pt;">Recomendamos</h3>
        <ol>
          <li><strong>Sessão de apresentação:</strong> revisar os achados com o time responsável e priorizar conjuntamente.</li>
          <li><strong>Sprint de quick wins:</strong> atacar primeiro os itens de 30 dias, validar lift via analytics.</li>
          <li><strong>Acompanhamento:</strong> auditoria de followup após 90 dias pra medir progresso e recalibrar.</li>
        </ol>
        <p style="margin-top: 20pt;"><strong>Contato.</strong> {escape(cfg['brand_name'])}</p>
      </div>
    </section>
    """


def render(
    report_data: dict,
    screenshots: dict,
    charts: dict,
    config: dict | None,
) -> str:
    """Render full HTML for premium PDF."""
    cfg = {**_DEFAULT_CONFIG, **(config or {})}

    css = _CSS.format(primary=cfg["primary_color"], accent=cfg["accent_color"])

    sections = []
    sections.append(_render_cover(report_data, config))
    sections.append(_render_executive_summary(report_data))
    sections.append(_render_methodology())
    sections.append(_render_visual_scorecard(report_data, charts))

    dim_screenshots = screenshots.get("dimensions", {})
    dim_html_parts = ["<section class='page'>", "<h1>Análise por Dimensão</h1>"]
    for dim_name, dim_data in report_data["dimensions"].items():
        dim_html_parts.append(_render_dimension_section(dim_name, dim_data, dim_screenshots.get(dim_name)))
    dim_html_parts.append("</section>")
    sections.append("\n".join(dim_html_parts))

    sections.append(_render_competitive(report_data))
    sections.append(_render_roadmap(report_data.get("roadmap", {})))
    sections.append(_render_appendix(report_data))
    sections.append(_render_glossary(report_data.get("used_terms")))
    sections.append(_render_next_steps(config))

    return f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<title>Auditoria Pro · {escape(report_data.get('client_name', ''))}</title>
<style>{css}</style>
</head>
<body>
{''.join(sections)}
</body>
</html>"""
```

- [ ] **Step 4: Run tests, verify pass**

Run: `python -m pytest scripts/tests/test_audit_premium_template.py -v`
Expected: 7 passed.

- [ ] **Step 5: Commit**

```bash
git add scripts/audit_premium_template.py scripts/tests/test_audit_premium_template.py
git commit -m "feat(audit-pro): premium HTML/CSS template with 10 sections"
```

---

## Task 7: Extend pdf_generator.py with --from-html flag

**Files:**
- Modify: `scripts/pdf_generator.py`
- Modify: `scripts/tests/test_pdf_generator.py`

- [ ] **Step 1: Append --from-html test**

Add to `scripts/tests/test_pdf_generator.py`:

```python
class TestFromHtml:
    def test_from_html_generates_pdf(self, tmp_path: Path):
        html_path = tmp_path / "report.html"
        html_path.write_text("<!DOCTYPE html><html><body><h1>HTML Test</h1></body></html>")
        out_path = tmp_path / "report.pdf"
        result = generate(html_path, out_path, from_html=True)
        assert result == out_path
        assert out_path.exists()
        assert out_path.stat().st_size > 100

    def test_html_extension_auto_detects(self, tmp_path: Path):
        html_path = tmp_path / "report.html"
        html_path.write_text("<!DOCTYPE html><html><body>Auto</body></html>")
        out_path = tmp_path / "report.pdf"
        # Default from_html=False, but extension is .html → auto-detect
        result = generate(html_path, out_path)
        assert out_path.exists()

    def test_cli_from_html_flag(self, tmp_path: Path):
        import subprocess
        html = tmp_path / "x.html"
        html.write_text("<html><body>X</body></html>")
        out = tmp_path / "x.pdf"
        script = Path(__file__).resolve().parent.parent / "pdf_generator.py"
        result = subprocess.run(
            [sys.executable, str(script), "--from-html", str(html), str(out)],
            capture_output=True, text=True, check=True,
        )
        assert out.exists()
```

- [ ] **Step 2: Run, verify failures**

Run: `python -m pytest scripts/tests/test_pdf_generator.py::TestFromHtml -v`
Expected: 3 failures.

- [ ] **Step 3: Modify pdf_generator.py**

In `scripts/pdf_generator.py`, modify `generate()` signature and add `from_html` parameter:

```python
def generate(
    markdown_path: Path | str,
    output_path: Path | str,
    config_path: Path | str | None = None,
    *,
    from_html: bool = False,
) -> Path:
    """Render markdown OR HTML file to PDF. Returns output_path.

    If `from_html=True` or input has .html extension, treats input as raw HTML
    and skips the markdown→HTML pipeline. Useful for premium templates.
    """
    from audit_config import load as load_config

    in_path = Path(markdown_path)
    out_path = Path(output_path)
    config = load_config(config_path) if config_path else None

    is_html = from_html or in_path.suffix.lower() == ".html"

    if is_html:
        html = in_path.read_text(encoding="utf-8")
    else:
        md_text = in_path.read_text(encoding="utf-8")
        html = _build_html(md_text, config)

    HTML(string=html, base_url=str(in_path.parent)).write_pdf(str(out_path))
    return out_path
```

Update `_cli()` to support `--from-html`:

```python
def _cli(argv: list[str]) -> int:
    if len(argv) < 3:
        print("Usage: pdf_generator.py [--from-html] <input> <output.pdf> [config.json]", file=sys.stderr)
        return 1

    args = list(argv[1:])
    from_html = False
    if args and args[0] == "--from-html":
        from_html = True
        args.pop(0)

    if len(args) < 2:
        print("Usage: pdf_generator.py [--from-html] <input> <output.pdf> [config.json]", file=sys.stderr)
        return 1

    md_path = Path(args[0])
    out_path = Path(args[1])
    cfg_path = Path(args[2]) if len(args) > 2 else None
    try:
        generate(md_path, out_path, cfg_path, from_html=from_html)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1
    print(str(out_path))
    return 0
```

- [ ] **Step 4: Run tests, verify pass**

Run: `python -m pytest scripts/tests/test_pdf_generator.py -v`
Expected: all PDF tests pass (existing + 3 new).

- [ ] **Step 5: Commit**

```bash
git add scripts/pdf_generator.py scripts/tests/test_pdf_generator.py
git commit -m "feat(audit-pro): pdf_generator --from-html for premium HTML templates"
```

---

## Task 8: commands/auditoria-pro.md — orchestrator

**Files:**
- Create: `commands/auditoria-pro.md`

- [ ] **Step 1: Create command file**

Create `commands/auditoria-pro.md` with extensive system prompt. Total ~300 lines. Structure:

```markdown
---
description: Auditoria PREMIUM agency-grade de landing page com radar chart, screenshots, prosa por dimensão, comparativo competitivo, roadmap 30/90/180 dias e PDF de 25-30 páginas pronto pra entregar pra cliente.
argument-hint: <url>
allowed-tools: Bash, WebFetch, Read, Write, Agent
---

# /auditoria-pro

Você é o orquestrador de auditoria premium agency-grade do marketing-os. Recebe URL de landing page e produz RELATORIO.md + RELATORIO.pdf de 25-30 páginas em `workspace/auditorias/<run>-pro/`.

## Passo 1: Validar input

Se `$ARGUMENTS` está vazio, retorne usage:

```
Uso: /auditoria-pro <url-de-landing-page>

Este command suporta APENAS landing pages. Para Instagram, Meta Ads ou YouTube, use /auditoria standard.

Exemplo:
  /auditoria-pro https://stripe.com
```

Rode `python ${CLAUDE_PLUGIN_ROOT}/scripts/audit_detector.py "$ARGUMENTS"`. Se type != "landing", aborte com mensagem clara. Senão, capture `type`, `normalized`, `slug`.

## Passo 2: Criar diretório do run

```bash
TIMESTAMP=$(date +%Y-%m-%d-%H%M%S)
RUN_DIR="workspace/auditorias/${TIMESTAMP}-landing-${SLUG}-pro"
mkdir -p "${RUN_DIR}"/{screenshots,charts,anexos}
```

## Passo 3: Dispatch paralelo (single message)

Use Bash + 7 Agent calls em UMA SÓ mensagem.

### Bash: Capturar screenshots

```bash
python ${CLAUDE_PLUGIN_ROOT}/scripts/audit_screenshot.py \
  --url "${NORMALIZED}" \
  --output-dir "${RUN_DIR}/screenshots" \
  --timeout-ms 30000
```

### Agent calls (7 em paralelo)

Para cada agent, prompt com instrução ADICIONAL (vs /auditoria v1):

> "Devolve output denso (1500-2000 palavras), incluindo tabelas comparativas quando aplicável, diagramas ASCII quando útil, citações textuais do que viu no site, e antes/depois de copy quando sugerir mudança específica."

Os 7 agents:
- mos-research: posicionamento competitivo + 3 concorrentes diretos
- mos-seo: audit técnico + on-page completo
- mos-copy: headline + value prop + CTAs + antes/depois sugerido
- mos-funnel: funil mapeado + friction points + diagrama
- mos-ads: CTA strategy + conversion path + trust signals
- mos-design: hierarquia visual + acessibilidade WCAG + paleta
- mos-brand: voice + arquétipo + identidade

## Passo 4: Salvar outputs raw

Para cada agent, escreva output em `${RUN_DIR}/anexos/anexo_<agent>.md`. Esses arquivos preservam a fonte completa que vai pro apêndice do PDF.

## Passo 5: Synthesis expandida

Para cada uma das 7 dimensões, gere:

1. **Score 0-100** baseado nos outputs dos agents relevantes
2. **3-5 evidências observadas** (não 1 — bullets curtos com fato concreto)
3. **Prose de 3-5 parágrafos** consolidando os agents (analítica, profissional, sem floreio)
4. **1-3 fixes priorizados** com `priority` ("alta", "media", "baixa") e `text` específico
5. **Antes/Depois de copy** quando agents sugeriram mudança textual (lista de objetos `{before, after}`)
6. **Citação textual de agent** (1-2 frases) com atribuição (`Conforme análise mos-X`)

Quality gates:
- Sem `—` (substituir por `:` ou `.`)
- Sem "brutal" (usar intenso, forte, pesado)
- Sem CAPS em prosa
- PT-BR sempre acentuado
- Citação de números/cases vem de output do agent ou WebSearch (não inventar)

Monte o JSON `scores.json` em `${RUN_DIR}/`:

```json
{
  "type": "landing",
  "dimension_scores": {
    "Conversão (CTA, friction, funil)": 71,
    ...
  },
  "evidences": {
    "Conversão (CTA, friction, funil)": ["evidência 1", "evidência 2", ...],
    ...
  },
  "fixes": {
    "Conversão (CTA, friction, funil)": {"text": "...", "priority": "alta"},
    ...
  }
}
```

## Passo 6: Calcular score final

```bash
python ${CLAUDE_PLUGIN_ROOT}/scripts/audit_scoring.py < "${RUN_DIR}/scores.json" > "${RUN_DIR}/scoring_output.json"
```

## Passo 7: Gerar radar chart

```bash
python ${CLAUDE_PLUGIN_ROOT}/scripts/audit_radar_chart.py \
  --scores-json "${RUN_DIR}/scoring_output.json" \
  --output "${RUN_DIR}/charts/radar_scorecard.png"
```

## Passo 8: Gerar roadmap

```bash
python ${CLAUDE_PLUGIN_ROOT}/scripts/audit_roadmap_generator.py < "${RUN_DIR}/scoring_output.json" > "${RUN_DIR}/roadmap.json"
```

## Passo 9: Build report data dict + render HTML

Use a tool Write para construir `${RUN_DIR}/render_input.json` com a estrutura:

```json
{
  "client_url": "<url>",
  "client_name": "<slug ou domain>",
  "audit_type": "landing",
  "timestamp": "<timestamp>",
  "overall_score": <number>,
  "partial": <bool>,
  "exec_summary": "<3 frases bem escritas>",
  "dimensions": {
    "<dim_name>": {
      "score": <n>,
      "weight": <w>,
      "prose": "<3-5 parágrafos>",
      "evidences": ["...", "..."],
      "fixes": [{"text": "...", "priority": "alta"}],
      "before_after": [{"before": "...", "after": "..."}],
      "agent_citation": "..."
    }
  },
  "competitive": {
    "competitors": [{"name": "...", "differentiation": "..."}],
    "table_md": "<markdown table>"
  },
  "roadmap": {<from roadmap.json>},
  "appendix": {
    "research": "<full anexo content>",
    "seo": "<full>",
    ...
  },
  "used_terms": ["CWV", "schema markup", "CTA", ...]
}
```

Depois renderize HTML:

```bash
python -c "
import json
import sys
sys.path.insert(0, '${CLAUDE_PLUGIN_ROOT}/scripts')
from audit_premium_template import render

data = json.load(open('${RUN_DIR}/render_input.json'))
screenshots = {'homepage': '${RUN_DIR}/screenshots/homepage.png', 'internals': [], 'dimensions': {}}
charts = {'radar': '${RUN_DIR}/charts/radar_scorecard.png'}
config_path = '.auditoria-config.json'
config = None
import os
if os.path.exists(config_path):
    config = json.load(open(config_path))

html = render(data, screenshots, charts, config)
open('${RUN_DIR}/RELATORIO.html', 'w').write(html)
print('${RUN_DIR}/RELATORIO.html')
"
```

## Passo 10: Gerar PDF

```bash
python ${CLAUDE_PLUGIN_ROOT}/scripts/pdf_generator.py --from-html \
  "${RUN_DIR}/RELATORIO.html" \
  "${RUN_DIR}/RELATORIO.pdf" \
  ".auditoria-config.json"
```

Se PDF falhar, imprima erro e mantenha HTML como fallback.

## Passo 11: Output final no chat

Imprima 5 linhas:

```
✓ Auditoria Pro concluída: <client_name>
  Score: <overall>/100 <(parcial se aplicável)>
  Páginas no PDF: ~<estimativa>
  Arquivos: <RUN_DIR>/RELATORIO.{html,pdf}
  Custo: $0.00 (Playwright local, sem Apify nesta auditoria)
```

Acrescente exec summary em 5 frases.

## Telemetria

Antes do output final, escreva `${RUN_DIR}/.audit-meta.json`:

```json
{
  "started_at": "<ISO>",
  "ended_at": "<ISO>",
  "type": "landing-pro",
  "input": "<url>",
  "agents_dispatched": ["mos-..."],
  "agents_failed": [],
  "screenshots_captured": <int>,
  "config_applied": <bool>,
  "pdf_pages": <estimate>,
  "errors": []
}
```
```

- [ ] **Step 2: Run dispatch coverage test**

Run: `python -m pytest scripts/tests/test_commands_dispatch.py -v`
Expected: pass — `/auditoria-pro` detected as dispatching command.

- [ ] **Step 3: Update test_workspace_separation.py allowlist**

Add `commands/auditoria-pro.md` to the WORKSPACE_REF_ALLOWLIST in `scripts/tests/test_workspace_separation.py`.

- [ ] **Step 4: Update test_integration_mcp.py SCRIPTS_EXCLUIDOS**

Add to `SCRIPTS_EXCLUIDOS` in `scripts/tests/test_integration_mcp.py`:

```python
        "audit_screenshot.py",         # invocado direto por /auditoria-pro
        "audit_radar_chart.py",        # invocado direto por /auditoria-pro
        "audit_premium_template.py",   # helper interno do /auditoria-pro
        "audit_roadmap_generator.py",  # invocado direto por /auditoria-pro
        "audit_glossary.py",           # helper interno do /auditoria-pro
```

- [ ] **Step 5: Run full test suite**

Run: `python -m pytest scripts/tests/ -v -m "not smoke" --tb=no 2>&1 | tail -10`
Expected: all green.

- [ ] **Step 6: Commit**

```bash
git add commands/auditoria-pro.md scripts/tests/test_workspace_separation.py scripts/tests/test_integration_mcp.py
git commit -m "feat(commands): /auditoria-pro premium agency-grade orchestrator"
```

---

## Task 9: Smoke integration test

**Files:**
- Create: `scripts/tests/test_auditoria_pro_smoke.py`

- [ ] **Step 1: Create smoke test**

Create `scripts/tests/test_auditoria_pro_smoke.py`:

```python
"""Smoke test for /auditoria-pro pipeline. Mocks agent outputs + Playwright.

Marked @pytest.mark.smoke to skip in default CI.
"""
from __future__ import annotations

import json
import os
import sys
from pathlib import Path
from unittest.mock import patch, MagicMock

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pytest

from audit_detector import detect
from audit_scoring import RUBRICS, compute, format_scorecard_md
from audit_radar_chart import generate as generate_radar
from audit_roadmap_generator import generate as generate_roadmap
from audit_premium_template import render
from audit_glossary import render_glossary_md
from pdf_generator import generate as generate_pdf

pytestmark = pytest.mark.smoke


def _mock_synthesis() -> dict:
    """Returns a complete synthesis dict for landing audit."""
    rubric = RUBRICS["landing"]
    return {
        "type": "landing",
        "dimension_scores": {dim: 70 for dim in rubric},
        "evidences": {dim: [f"evidence {i}" for i in range(3)] for dim in rubric},
        "fixes": {dim: {"text": f"fix {dim}", "priority": "alta"} for dim in rubric},
    }


def test_full_pipeline_landing(tmp_path: Path):
    # 1. Detect
    detected = detect("https://stripe.com")
    assert detected["type"] == "landing"

    # 2. Mock synthesis
    payload = _mock_synthesis()

    # 3. Compute scoring
    result = compute(
        payload["type"],
        payload["dimension_scores"],
        {dim: e[0] for dim, e in payload["evidences"].items()},
        payload["fixes"],
    )
    assert result["overall"] == 70

    # 4. Generate radar chart
    radar_path = tmp_path / "radar.png"
    scores = {d: i["score"] for d, i in result["dimensions"].items()}
    fixes = {d: i["fix"] for d, i in result["dimensions"].items()}
    generate_radar(scores, fixes, radar_path)
    assert radar_path.exists()

    # 5. Generate roadmap
    fixes_list = [
        {"dimension": d, "score": i["score"], "fix": i["fix"]}
        for d, i in result["dimensions"].items()
    ]
    weights = {d: i["weight"] for d, i in result["dimensions"].items()}
    roadmap = generate_roadmap(fixes_list, weights)
    assert "30_days" in roadmap

    # 6. Build report data
    report_data = {
        "client_url": "https://stripe.com",
        "client_name": "stripe.com",
        "audit_type": "landing",
        "timestamp": "2026-05-09 10:00:00",
        "overall_score": result["overall"],
        "partial": result["partial"],
        "exec_summary": "Stripe entrega execução de classe mundial...",
        "dimensions": {
            d: {
                "score": i["score"],
                "weight": i["weight"],
                "prose": "Análise detalhada da dimensão. " * 20,  # ~40 words → 200 words realistic
                "evidences": payload["evidences"][d],
                "fixes": [i["fix"]],
                "before_after": [],
                "agent_citation": f"Conforme análise mos-X: '{i['evidence'][:60]}...'",
            }
            for d, i in result["dimensions"].items()
        },
        "competitive": {"competitors": [{"name": "Adyen", "differentiation": "..."}], "table_md": "| A |\n|---|\n| 1 |"},
        "roadmap": roadmap,
        "appendix": {"research": "raw...", "seo": "raw..."},
        "used_terms": ["CTA", "value proposition", "CWV"],
    }

    # 7. Render HTML
    html = render(report_data, {"homepage": str(radar_path)}, {"radar": str(radar_path)}, config=None)
    html_path = tmp_path / "RELATORIO.html"
    html_path.write_text(html)
    assert "<!DOCTYPE html>" in html
    assert "stripe.com" in html

    # 8. Generate PDF
    pdf_path = tmp_path / "RELATORIO.pdf"
    generate_pdf(html_path, pdf_path, from_html=True)
    assert pdf_path.exists()
    assert pdf_path.stat().st_size > 5000  # premium PDF should have substantial content
```

- [ ] **Step 2: Run smoke test**

Run: `python -m pytest scripts/tests/test_auditoria_pro_smoke.py -v -m smoke`
Expected: 1 passed.

- [ ] **Step 3: Commit**

```bash
git add scripts/tests/test_auditoria_pro_smoke.py
git commit -m "test(audit-pro): smoke pipeline (mocked agents → premium PDF)"
```

---

## Task 10: docs/AUDITORIA-PRO.md user-facing doc

**Files:**
- Create: `docs/AUDITORIA-PRO.md`

- [ ] **Step 1: Write doc**

Create `docs/AUDITORIA-PRO.md`:

````markdown
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

## Macos: Playwright + dylib path

Mesma anotação do `/auditoria` standard: weasyprint precisa de `DYLD_FALLBACK_LIBRARY_PATH=/opt/homebrew/lib` no macOS. O `pdf_generator.py` configura automaticamente.
````

- [ ] **Step 2: Commit**

```bash
git add docs/AUDITORIA-PRO.md
git commit -m "docs(audit-pro): user-facing doc for /auditoria-pro premium"
```

---

## Task 11: Manual validation

This is run by hand. Each scenario must produce RELATORIO.html + RELATORIO.pdf with no stack traces and target page count.

- [ ] **Scenario 1: Stripe.com (caso piloto)**

In Claude Code:
```
/auditoria-pro https://stripe.com
```

Verify:
- 7 agents dispatch in parallel + Playwright runs
- `workspace/auditorias/<run>-pro/RELATORIO.pdf` exists
- PDF has 25-30 pages
- Cover page renders with deep blue background
- Radar chart embedded with ghost outline
- All 7 dimensions have prose (3-5 paragraphs each)
- Roadmap section shows 30/90/180 buckets with non-empty data
- Appendix has 7 agent outputs (raw)
- Glossary appears with 5-15 filtered terms
- Output in chat: 5 lines + exec summary

- [ ] **Scenario 2: Site simples (example.com ou similar)**

Test graceful degradation when Playwright can't navigate internal pages.

```
/auditoria-pro https://example.com
```

Verify:
- PDF generated even with limited screenshots
- Sections that lack data show fallback messages (não stack traces)
- Roadmap may be sparse but still rendered

- [ ] **Scenario 3: Stripe with white-label config**

In project root:
```json
{
  "brand_name": "Especializei Consultoria",
  "primary_color": "#0a2540",
  "accent_color": "#ff6b35",
  "footer_text": "© 2026 Especializei. Auditoria preparada para Stripe Inc."
}
```

```
/auditoria-pro https://stripe.com
```

Verify:
- Cover page shows "Especializei Consultoria" as brand
- Custom accent color in headings, charts, tables
- Custom footer in page footer
- All 25-30 pages have consistent branding

Cleanup:
```bash
rm .auditoria-config.json
```

---

## Task 12: Release v6.8.0

**Files:**
- Modify: `AGENTS.md`
- Modify: `CHANGELOG.md`
- Modify: `.claude-plugin/plugin.json`
- Modify: `.claude-plugin/marketplace.json`

- [ ] **Step 1: AGENTS.md**

Find: `Hoje 31 dos 33 slash commands em \`commands/\` dispatcham subagents.`

Replace with: `Hoje 32 dos 34 slash commands em \`commands/\` dispatcham subagents. Os 2 commands premium na v6.8.0+ são \`/auditoria\` (multi-modal básico) e \`/auditoria-pro\` (landing agency-grade com radar/screenshots/roadmap, ver \`docs/AUDITORIA-PRO.md\`).`

Find: `Marketing OS é um **plugin do Claude Code** (\`plugin.json\` v6.7.0)` (or whatever current version says)

Replace `v6.7.0` with `v6.8.0`. If the line says `v6.5.0` (stale from earlier), update to `v6.8.0` and `33 slash commands` to `34 slash commands`.

- [ ] **Step 2: CHANGELOG.md entry**

Add at top after header (before v6.7.0):

```markdown
## v6.8.0 (2026-05-09)

### Added
- New command `/auditoria-pro <url>` — premium agency-grade landing audit. Output: 25-30 page PDF with radar chart (ghost outline of potential post-fixes), screenshots (homepage + 2-3 internal pages via Playwright), 3-5 paragraphs per dimension, before/after copy comparisons, competitive analysis, 30/90/180 day roadmap with effort/impact/owner, technical appendix with 7 agents' raw outputs, filtered glossary.
- 5 new scripts: `audit_screenshot.py` (Playwright capture), `audit_radar_chart.py` (matplotlib radar with potential overlay), `audit_premium_template.py` (HTML/CSS premium template, ~600 lines), `audit_roadmap_generator.py` (30/90/180 bucketing), `audit_glossary.py` (67 PT-BR technical terms).
- `pdf_generator.py` extended with `--from-html` flag for premium HTML templates.
- New deps: `matplotlib>=3.7`, `playwright>=1.40` (with chromium browser).
- User doc: `docs/AUDITORIA-PRO.md`.

### Notes
- `/auditoria-pro` is landing-only on v6.8.0. Instagram, Meta Ads, YouTube extensions in v6.8.1+.
- Visual identity: deep ink blue `#0a2540` + warm orange `#ff6b35`. White-label via `.auditoria-config.json` (compatible with /auditoria standard).
- Generation time: ~6-9 min per run vs ~3-5 min for `/auditoria` standard.
- Cost: $0 (Playwright local, no Apify mandatory).
- macOS: Playwright requires `playwright install chromium` post `pip install`.
```

- [ ] **Step 3: Bump versions**

Edit `.claude-plugin/plugin.json`: `"version": "6.7.0"` → `"version": "6.8.0"`.
Edit `.claude-plugin/marketplace.json`: top-level `"version"` to `"6.8.0"`.

- [ ] **Step 4: Validate**

Run: `claude plugin validate .` (if available) OR `python scripts/validate_agents.py --strict`
Expected: passes.

- [ ] **Step 5: Run full test suite**

Run: `python -m pytest scripts/tests/ -v -m "not smoke" --tb=no 2>&1 | tail -10`
Expected: all green, no regressions, count of commands updated to 34.

Run smoke: `python -m pytest scripts/tests/ -v -m smoke --tb=no 2>&1 | tail -10`
Expected: all smoke tests pass.

- [ ] **Step 6: Commit**

```bash
git add AGENTS.md CHANGELOG.md .claude-plugin/plugin.json .claude-plugin/marketplace.json
git commit -m "chore: release v6.8.0 — /auditoria-pro premium agency-grade"
```

---

## Self-Review Checklist

- [ ] Spec coverage: All 7 components from spec section 4 implemented (Tasks 2-8). Data flow steps 1-15 covered by command (Task 8). Error handling categories addressed in script implementations. Testing strategy covered (Tasks 2-9). File manifest complete (Tasks 1-12).
- [ ] No placeholders: Each task has actual code (no "TBD"). Tests have full assertions. Implementation snippets show real Python code.
- [ ] Type consistency: `generate(scores, fixes, output_path)` signature in audit_radar_chart consistent across tests. `capture(url, output_dir)` consistent. `render(report_data, screenshots, charts, config)` consistent in template.
- [ ] All 12 tasks have discrete commits. Commit messages follow `feat(audit-pro)` / `test(audit-pro)` / `docs(audit-pro)` / `chore` pattern.
- [ ] Manual validation (Task 11) is in-band, user-executed.

## Notes for execution

- TDD discipline: write tests, watch fail, implement, watch pass, commit.
- Use `${CLAUDE_PLUGIN_ROOT}` in command markdown for all script invocations.
- Playwright is heavy (~150MB browser download). Task 1 step 4 may take 1-2 min.
- After Task 12, push and tag only with explicit user approval:

```bash
git push origin <branch>
git tag v6.8.0
git push origin v6.8.0
```
