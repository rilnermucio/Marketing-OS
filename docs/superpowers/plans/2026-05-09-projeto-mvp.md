# /projeto MVP — Workflow com Handoffs e Approval Gates

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Implementar `/projeto` — sistema de gestão de projetos de marketing com pipeline declarativo, dispatch sequencial de subagents `mos-*`, approval gates entre stages e iteração via feedback. Substitui o `project_manager.py` existente (CRUD básico não usado).

**Architecture:** Markdown com YAML frontmatter como fonte de verdade do estado do projeto. `runs.jsonl` append-only como log de execução. `decisions.md` como histórico de aprovações. Slash command `/projeto` orquestra; Python `project_manager.py` gerencia file ops. Pipeline puramente sequencial no MVP, sem paralelismo nem DAG (Fase 2 evolui).

**Tech Stack:** Python 3 (stdlib + PyYAML), Markdown frontmatter, JSONL append, Claude Code slash command com Agent dispatch.

**Spec consensual (Claude + Codex, gpt-5.5/high):** ver `/tmp/debate-claude-codex/turn-{01,02,03}-*.md`.

---

## File Structure

**Files this plan creates or modifies:**

- **Create:** `commands/projeto.md` — slash command orchestrator (subcommands: novo, list, status, avancar, aprovar, rejeitar)
- **Create:** `scripts/templates/projeto/` — 4 template files (lancamento.md, perpetuo.md, consultoria.md, mentoria.md)
- **Replace:** `scripts/project_manager.py` — reescreve com novo design (state machine + runs.jsonl + dispatch helpers)
- **Replace:** `scripts/tests/test_project_manager.py` — reescreve testes pro novo comportamento
- **Modify:** `scripts/mos.py:89-95,110-115,179-181` — atualiza mapeamento de subcomandos
- **Modify:** `agents/mos-infoproduct.md:59` — atualiza dispatch reference
- **Modify:** `docs/ARCHITECTURE.md:596` — atualiza descrição do project_manager
- **Modify:** `docs/stories/active/STORY-001-atualizar-readme-scripts.md` — atualiza menção
- **Modify:** `scripts/tests/test_integration_mcp.py:257` — verificar se passa após refactor

User data fica em `workspace/projects/<slug>/` (gitignored). Plugin code em `commands/`, `scripts/`, `scripts/templates/`.

---

## Task 1: Tear down old project_manager.py + tests

**Files:**
- Delete: `scripts/project_manager.py` (vai ser reescrito do zero na Task 3)
- Delete: `scripts/tests/test_project_manager.py` (vai ser reescrito do zero na Task 4)

- [ ] **Step 1: Confirm old test currently passes (baseline)**

Run: `python -m pytest scripts/tests/test_project_manager.py -v`
Expected: PASS (baseline). Record count of passing tests.

- [ ] **Step 2: Delete old files**

```bash
rm scripts/project_manager.py
rm scripts/tests/test_project_manager.py
```

- [ ] **Step 3: Confirm test suite still discoverable**

Run: `python -m pytest scripts/tests/ -v -m "not smoke" --collect-only 2>&1 | tail -5`
Expected: collection succeeds, project_manager tests no longer listed.

- [ ] **Step 4: No commit yet** — Tasks 1-4 commit together as "feat: rewrite /projeto with workflow MVP".

---

## Task 2: Create directory for templates

**Files:**
- Create: `scripts/templates/projeto/.gitkeep`

- [ ] **Step 1: Create directory**

```bash
mkdir -p scripts/templates/projeto
touch scripts/templates/projeto/.gitkeep
```

- [ ] **Step 2: Verify**

Run: `ls scripts/templates/projeto/`
Expected: `.gitkeep`

---

## Task 3: Write project.md templates (4 types)

**Files:**
- Create: `scripts/templates/projeto/lancamento.md`
- Create: `scripts/templates/projeto/perpetuo.md`
- Create: `scripts/templates/projeto/consultoria.md`
- Create: `scripts/templates/projeto/mentoria.md`

Each template uses `{name}` and `{slug}` placeholders that the script substitutes via `str.format`.

- [ ] **Step 1: Create lancamento.md template**

Content of `scripts/templates/projeto/lancamento.md`:

```markdown
---
name: {name}
slug: {slug}
type: lancamento
status: active
current_stage: research
default_approval: required
created_at: {created_at}
pipeline:
  - id: research
    agent: mos-research
    approval: skip
  - id: estrategia
    agent: mos-launch
    approval: required
  - id: funil
    agent: mos-funnel
    approval: required
  - id: copy
    agent: mos-copy
    approval: required
  - id: design
    agent: mos-design
    approval: required
  - id: ads
    agent: mos-ads
    approval: required
---

# Briefing: {name}

## Produto/Oferta
[Descrever o produto]

## Avatar
[Quem é o cliente ideal]

## Ticket
[Preço]

## Cronograma
- Início: {created_at}
- Carrinho abre: [data]
- Carrinho fecha: [data]

## Notas adicionais
[Detalhes relevantes]
```

- [ ] **Step 2: Create perpetuo.md template**

Content of `scripts/templates/projeto/perpetuo.md`:

```markdown
---
name: {name}
slug: {slug}
type: perpetuo
status: active
current_stage: research
default_approval: required
created_at: {created_at}
pipeline:
  - id: research
    agent: mos-research
    approval: skip
  - id: funil
    agent: mos-funnel
    approval: required
  - id: copy
    agent: mos-copy
    approval: required
  - id: ads
    agent: mos-ads
    approval: required
  - id: analytics
    agent: mos-analytics
    approval: skip
---

# Briefing: {name}

## Produto/Oferta perpétua
[Descrever a oferta evergreen]

## Avatar
[Cliente ideal]

## Ticket
[Preço]

## Canais de tráfego
[Meta Ads / Google Ads / Orgânico]

## Notas adicionais
[Detalhes relevantes]
```

- [ ] **Step 3: Create consultoria.md template**

Content of `scripts/templates/projeto/consultoria.md`:

```markdown
---
name: {name}
slug: {slug}
type: consultoria
status: active
current_stage: discovery
default_approval: required
created_at: {created_at}
pipeline:
  - id: discovery
    agent: mos-research
    approval: required
  - id: diagnostico
    agent: mos-analytics
    approval: required
  - id: estrategia
    agent: mos-growth
    approval: required
  - id: deliverable
    agent: mos-copy
    approval: required
---

# Briefing: {name}

## Cliente
[Nome / setor]

## Problema apresentado
[Dor que o cliente trouxe]

## Escopo da consultoria
[O que está incluído]

## Prazo
- Início: {created_at}
- Entrega: [data]

## Notas adicionais
[Detalhes relevantes]
```

- [ ] **Step 4: Create mentoria.md template**

Content of `scripts/templates/projeto/mentoria.md`:

```markdown
---
name: {name}
slug: {slug}
type: mentoria
status: active
current_stage: planejamento
default_approval: required
created_at: {created_at}
pipeline:
  - id: planejamento
    agent: mos-infoproduct
    approval: required
  - id: conteudo
    agent: mos-copy
    approval: required
  - id: comunidade
    agent: mos-social
    approval: required
  - id: feedback
    agent: mos-analytics
    approval: skip
---

# Briefing: {name}

## Cohort/Turma
[Nome da turma, número de alunos]

## Tema central
[Sobre o que é a mentoria]

## Duração
- Início: {created_at}
- Fim: [data]
- Frequência: [semanal / quinzenal]

## Promessa de transformação
[O que o aluno sai sabendo/conseguindo]

## Notas adicionais
[Detalhes relevantes]
```

---

## Task 4: Write project_manager.py — core file ops + frontmatter parsing

**Files:**
- Create: `scripts/project_manager.py`
- Test: `scripts/tests/test_project_manager.py`

This is the largest task. Decomposed into TDD steps below.

- [ ] **Step 1: Write failing tests for slugify, frontmatter parse, template loading**

Content of `scripts/tests/test_project_manager.py`:

```python
"""Testes para project_manager.py — workflow com handoffs e approval gates."""
from __future__ import annotations

import json
import os
import sys
import tempfile
from pathlib import Path

import pytest

# Adicionar diretório de scripts ao path
SCRIPTS_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(SCRIPTS_DIR))

from project_manager import (
    slugify,
    load_template,
    parse_frontmatter,
    serialize_frontmatter,
    create_project,
    list_projects,
    project_status,
    advance_stage,
    approve_stage,
    reject_stage,
    append_run,
    PROJECT_TYPES,
)


@pytest.fixture
def tmp_workspace(monkeypatch):
    """Workspace isolado em tmpdir."""
    tmpdir = tempfile.mkdtemp()
    workspace = Path(tmpdir) / "workspace" / "projects"
    workspace.mkdir(parents=True, exist_ok=True)
    monkeypatch.setattr("project_manager.PROJECTS_ROOT", workspace)
    yield workspace


def test_slugify_basic():
    assert slugify("Lançamento Curso IA") == "lancamento-curso-ia"


def test_slugify_strips_special_chars():
    assert slugify("Cliente: ACME Inc.") == "cliente-acme-inc"


def test_slugify_collapses_whitespace():
    assert slugify("  varios   espacos  ") == "varios-espacos"


def test_load_template_valid_type():
    tpl = load_template("lancamento")
    assert "{name}" in tpl
    assert "{slug}" in tpl
    assert "type: lancamento" in tpl


def test_load_template_invalid_type_raises():
    with pytest.raises(ValueError, match="invalid"):
        load_template("invalid")


def test_parse_frontmatter_extracts_dict_and_body():
    content = """---
name: test
type: lancamento
current_stage: research
---

# Body content here
"""
    fm, body = parse_frontmatter(content)
    assert fm["name"] == "test"
    assert fm["type"] == "lancamento"
    assert fm["current_stage"] == "research"
    assert "Body content here" in body


def test_serialize_frontmatter_roundtrip():
    fm = {"name": "x", "type": "lancamento", "pipeline": [{"id": "a", "agent": "mos-x"}]}
    body = "# Hi"
    serialized = serialize_frontmatter(fm, body)
    fm2, body2 = parse_frontmatter(serialized)
    assert fm2 == fm
    assert body2.strip() == body.strip()
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `python -m pytest scripts/tests/test_project_manager.py -v`
Expected: FAIL with "ModuleNotFoundError: No module named 'project_manager'" or "cannot import name X".

- [ ] **Step 3: Create skeleton project_manager.py with imports + constants + slugify + template loader + frontmatter parser**

Content of `scripts/project_manager.py`:

```python
#!/usr/bin/env python3
"""
project_manager.py — Workflow de projetos de marketing com handoffs e approval gates.

Substitui o CRUD anterior. Agora gerencia state machine declarativa por projeto:
- project.md (frontmatter YAML + body)
- runs.jsonl (append-only log de execucoes)
- decisions.md (historico de aprovacoes/rejeicoes)
- pastas <NN>-<stage>/ (artifacts por estagio)

Uso:
    python project_manager.py novo "Lançamento Curso IA" --tipo lancamento
    python project_manager.py list
    python project_manager.py status lancamento-curso-ia
    python project_manager.py avancar lancamento-curso-ia
    python project_manager.py aprovar lancamento-curso-ia
    python project_manager.py rejeitar lancamento-curso-ia "feedback"
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
from datetime import datetime
from pathlib import Path
from typing import Optional

import yaml

# Localiza o repositorio root via __file__ (scripts/project_manager.py)
REPO_ROOT = Path(__file__).resolve().parent.parent
PROJECTS_ROOT = REPO_ROOT / "workspace" / "projects"
TEMPLATES_DIR = REPO_ROOT / "scripts" / "templates" / "projeto"

PROJECT_TYPES = ("lancamento", "perpetuo", "consultoria", "mentoria")


# ---------- helpers ----------

def slugify(text: str) -> str:
    """Converte texto livre em slug URL-safe."""
    text = text.lower().strip()
    accent_map = {
        "[àáâãä]": "a", "[èéêë]": "e", "[ìíîï]": "i",
        "[òóôõö]": "o", "[ùúûü]": "u", "[ç]": "c",
    }
    for pattern, repl in accent_map.items():
        text = re.sub(pattern, repl, text)
    text = re.sub(r"[^a-z0-9]+", "-", text)
    return text.strip("-")


def load_template(project_type: str) -> str:
    """Carrega template de um tipo de projeto."""
    if project_type not in PROJECT_TYPES:
        raise ValueError(
            f"invalid type '{project_type}'. Valid: {', '.join(PROJECT_TYPES)}"
        )
    template_path = TEMPLATES_DIR / f"{project_type}.md"
    return template_path.read_text(encoding="utf-8")


FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---\n?(.*)$", re.DOTALL)


def parse_frontmatter(content: str) -> tuple[dict, str]:
    """Extrai frontmatter YAML + body de um arquivo Markdown."""
    match = FRONTMATTER_RE.match(content)
    if not match:
        return {}, content
    fm = yaml.safe_load(match.group(1)) or {}
    body = match.group(2)
    return fm, body


def serialize_frontmatter(fm: dict, body: str) -> str:
    """Serializa frontmatter + body de volta pra Markdown."""
    yaml_str = yaml.safe_dump(fm, sort_keys=False, allow_unicode=True).strip()
    return f"---\n{yaml_str}\n---\n\n{body.strip()}\n"
```

- [ ] **Step 4: Run tests — should now pass for slugify, load_template, parse_frontmatter, serialize_frontmatter**

Run: `python -m pytest scripts/tests/test_project_manager.py -v`
Expected: 6 tests pass (slugify x3, load_template x2, frontmatter x2). Other imports still fail.

- [ ] **Step 5: Add tests for create_project**

Append to `scripts/tests/test_project_manager.py`:

```python
def test_create_project_creates_structure(tmp_workspace):
    create_project("Lançamento Curso IA", "lancamento")
    project_dir = tmp_workspace / "lancamento-curso-ia"
    assert project_dir.is_dir()
    assert (project_dir / "project.md").is_file()
    assert (project_dir / "runs.jsonl").is_file()
    assert (project_dir / "decisions.md").is_file()


def test_create_project_writes_frontmatter_correctly(tmp_workspace):
    create_project("Curso X", "lancamento")
    content = (tmp_workspace / "curso-x" / "project.md").read_text(encoding="utf-8")
    fm, body = parse_frontmatter(content)
    assert fm["name"] == "Curso X"
    assert fm["slug"] == "curso-x"
    assert fm["type"] == "lancamento"
    assert fm["current_stage"] == "research"
    assert fm["status"] == "active"
    assert "Briefing" in body


def test_create_project_rejects_invalid_type(tmp_workspace):
    with pytest.raises(ValueError):
        create_project("X", "invalid")


def test_create_project_rejects_duplicate(tmp_workspace):
    create_project("Curso Y", "perpetuo")
    with pytest.raises(FileExistsError):
        create_project("Curso Y", "perpetuo")
```

- [ ] **Step 6: Run new tests, watch them fail**

Run: `python -m pytest scripts/tests/test_project_manager.py -v -k "create_project"`
Expected: FAIL with "ImportError: cannot import name 'create_project'".

- [ ] **Step 7: Implement create_project**

Append to `scripts/project_manager.py`:

```python
# ---------- create ----------

def create_project(name: str, project_type: str) -> Path:
    """Cria estrutura nova do projeto."""
    if project_type not in PROJECT_TYPES:
        raise ValueError(f"invalid type '{project_type}'")

    slug = slugify(name)
    project_dir = PROJECTS_ROOT / slug

    if project_dir.exists():
        raise FileExistsError(f"projeto ja existe: {slug}")

    project_dir.mkdir(parents=True, exist_ok=True)

    template = load_template(project_type)
    created_at = datetime.now().isoformat(timespec="seconds")
    rendered = template.format(name=name, slug=slug, created_at=created_at)
    (project_dir / "project.md").write_text(rendered, encoding="utf-8")

    (project_dir / "runs.jsonl").touch()
    (project_dir / "decisions.md").write_text(
        f"# Decisoes: {name}\n\n", encoding="utf-8"
    )

    return project_dir
```

- [ ] **Step 8: Run create_project tests, watch them pass**

Run: `python -m pytest scripts/tests/test_project_manager.py -v -k "create_project"`
Expected: 4 tests pass.

- [ ] **Step 9: Add tests for list_projects**

Append to `scripts/tests/test_project_manager.py`:

```python
def test_list_projects_empty(tmp_workspace):
    assert list_projects() == []


def test_list_projects_returns_active_first(tmp_workspace):
    create_project("Projeto A", "lancamento")
    create_project("Projeto B", "perpetuo")
    projects = list_projects()
    assert len(projects) == 2
    slugs = {p["slug"] for p in projects}
    assert slugs == {"projeto-a", "projeto-b"}
    assert all(p["status"] == "active" for p in projects)
```

- [ ] **Step 10: Run, watch fail, then implement**

Run: `python -m pytest scripts/tests/test_project_manager.py -v -k "list_projects"`
Expected: FAIL.

Append to `scripts/project_manager.py`:

```python
# ---------- list ----------

def list_projects() -> list[dict]:
    """Lista todos os projetos com snapshot de estado."""
    if not PROJECTS_ROOT.exists():
        return []
    out = []
    for entry in sorted(PROJECTS_ROOT.iterdir()):
        if not entry.is_dir():
            continue
        project_md = entry / "project.md"
        if not project_md.is_file():
            continue
        fm, _ = parse_frontmatter(project_md.read_text(encoding="utf-8"))
        out.append({
            "slug": fm.get("slug", entry.name),
            "name": fm.get("name", entry.name),
            "type": fm.get("type", "?"),
            "status": fm.get("status", "?"),
            "current_stage": fm.get("current_stage", "?"),
        })
    return out
```

Re-run: tests pass.

- [ ] **Step 11: Add tests for project_status**

Append:

```python
def test_project_status_returns_state(tmp_workspace):
    create_project("Status Test", "lancamento")
    state = project_status("status-test")
    assert state["slug"] == "status-test"
    assert state["current_stage"] == "research"
    assert state["status"] == "active"
    assert state["pipeline"][0]["id"] == "research"
    assert state["last_run"] is None  # ainda nenhuma execucao


def test_project_status_unknown_slug_raises(tmp_workspace):
    with pytest.raises(FileNotFoundError):
        project_status("nao-existe")
```

- [ ] **Step 12: Run, watch fail, then implement**

Run: `python -m pytest scripts/tests/test_project_manager.py -v -k "project_status"`
Expected: FAIL.

Append:

```python
# ---------- status ----------

def _read_jsonl(path: Path) -> list[dict]:
    if not path.exists():
        return []
    lines = []
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if line:
            lines.append(json.loads(line))
    return lines


def project_status(slug: str) -> dict:
    """Snapshot completo do estado de um projeto."""
    project_dir = PROJECTS_ROOT / slug
    project_md = project_dir / "project.md"
    if not project_md.is_file():
        raise FileNotFoundError(f"projeto nao encontrado: {slug}")

    fm, body = parse_frontmatter(project_md.read_text(encoding="utf-8"))
    runs = _read_jsonl(project_dir / "runs.jsonl")

    return {
        "slug": slug,
        "name": fm.get("name", slug),
        "type": fm.get("type"),
        "status": fm.get("status"),
        "current_stage": fm.get("current_stage"),
        "pipeline": fm.get("pipeline", []),
        "default_approval": fm.get("default_approval", "required"),
        "last_run": runs[-1] if runs else None,
        "total_runs": len(runs),
    }
```

Re-run: pass.

- [ ] **Step 13: Add tests for append_run + advance_stage + approve_stage + reject_stage**

Append:

```python
def test_append_run_writes_jsonl_line(tmp_workspace):
    create_project("Run Test", "lancamento")
    append_run("run-test", {
        "stage_id": "research",
        "agent": "mos-research",
        "iteration": 1,
        "status": "running",
    })
    runs = _read_jsonl(tmp_workspace / "run-test" / "runs.jsonl")
    assert len(runs) == 1
    assert runs[0]["stage_id"] == "research"
    assert runs[0]["status"] == "running"
    assert "run_id" in runs[0]
    assert "started_at" in runs[0]


def test_advance_stage_creates_pending_run(tmp_workspace):
    create_project("Advance Test", "lancamento")
    run = advance_stage("advance-test")
    assert run["stage_id"] == "research"
    assert run["agent"] == "mos-research"
    assert run["status"] == "pending"
    assert run["iteration"] == 1


def test_approve_stage_advances_current_stage(tmp_workspace):
    create_project("Approve Test", "perpetuo")
    advance_stage("approve-test")  # research em pending
    # marca o run como pending_approval (simula que o agente terminou)
    runs_path = tmp_workspace / "approve-test" / "runs.jsonl"
    runs = _read_jsonl(runs_path)
    runs[-1]["status"] = "pending_approval"
    runs_path.write_text(
        "\n".join(json.dumps(r) for r in runs) + "\n", encoding="utf-8"
    )
    state = approve_stage("approve-test")
    # current_stage deve ter avancado pra "funil"
    assert state["current_stage"] == "funil"
    last_run = state["last_run"]
    assert last_run["status"] == "approved"


def test_reject_stage_keeps_current_and_logs_feedback(tmp_workspace):
    create_project("Reject Test", "lancamento")
    advance_stage("reject-test")
    runs_path = tmp_workspace / "reject-test" / "runs.jsonl"
    runs = _read_jsonl(runs_path)
    runs[-1]["status"] = "pending_approval"
    runs_path.write_text(
        "\n".join(json.dumps(r) for r in runs) + "\n", encoding="utf-8"
    )
    state = reject_stage("reject-test", "muito formal")
    assert state["current_stage"] == "research"  # fica no mesmo
    assert state["last_run"]["status"] == "rejected"
    assert state["last_run"]["feedback"] == "muito formal"
    decisions = (tmp_workspace / "reject-test" / "decisions.md").read_text(
        encoding="utf-8"
    )
    assert "muito formal" in decisions
```

- [ ] **Step 14: Run, watch fail, then implement append_run + advance_stage + approve_stage + reject_stage**

Run: `python -m pytest scripts/tests/test_project_manager.py -v`
Expected: 4 new tests fail.

Append to `scripts/project_manager.py`:

```python
# ---------- run log ----------

def append_run(slug: str, run: dict) -> dict:
    """Appenda uma linha no runs.jsonl. Preenche run_id e started_at se faltarem."""
    project_dir = PROJECTS_ROOT / slug
    runs_path = project_dir / "runs.jsonl"
    existing = _read_jsonl(runs_path)
    next_id = f"run_{len(existing) + 1:03d}"

    run = dict(run)  # copia defensiva
    run.setdefault("run_id", next_id)
    run.setdefault("started_at", datetime.now().isoformat(timespec="seconds"))

    with runs_path.open("a", encoding="utf-8") as f:
        f.write(json.dumps(run, ensure_ascii=False) + "\n")
    return run


# ---------- state machine ----------

def _update_frontmatter(slug: str, updates: dict) -> dict:
    """Mescla updates no frontmatter do project.md e regrava."""
    project_md = PROJECTS_ROOT / slug / "project.md"
    fm, body = parse_frontmatter(project_md.read_text(encoding="utf-8"))
    fm.update(updates)
    project_md.write_text(serialize_frontmatter(fm, body), encoding="utf-8")
    return fm


def _next_stage(pipeline: list[dict], current_id: str) -> Optional[dict]:
    """Retorna o proximo stage na pipeline, ou None se acabou."""
    for i, stage in enumerate(pipeline):
        if stage["id"] == current_id and i + 1 < len(pipeline):
            return pipeline[i + 1]
    return None


def _current_stage_def(pipeline: list[dict], current_id: str) -> Optional[dict]:
    for stage in pipeline:
        if stage["id"] == current_id:
            return stage
    return None


def _stage_iteration(slug: str, stage_id: str) -> int:
    """Quantas vezes esse stage rodou ate agora? (proxima iteracao = N+1)"""
    runs = _read_jsonl(PROJECTS_ROOT / slug / "runs.jsonl")
    return sum(1 for r in runs if r.get("stage_id") == stage_id) + 1


def advance_stage(slug: str) -> dict:
    """Cria um run pendente pro stage atual e retorna ele.

    Nao executa o agente — quem executa eh o slash command /projeto.
    Esse helper soh registra "vai rodar isso agora".
    """
    state = project_status(slug)
    stage_def = _current_stage_def(state["pipeline"], state["current_stage"])
    if stage_def is None:
        raise ValueError(f"stage atual '{state['current_stage']}' nao esta na pipeline")
    iteration = _stage_iteration(slug, stage_def["id"])
    run = append_run(slug, {
        "stage_id": stage_def["id"],
        "agent": stage_def["agent"],
        "iteration": iteration,
        "status": "pending",
        "source": "pipeline",
    })
    return run


def approve_stage(slug: str) -> dict:
    """Aprova o ultimo run pendente e avanca o current_stage.

    Se ja for o ultimo stage da pipeline, marca status: completed.
    """
    project_dir = PROJECTS_ROOT / slug
    runs_path = project_dir / "runs.jsonl"
    runs = _read_jsonl(runs_path)
    if not runs:
        raise ValueError("nenhum run para aprovar")

    last = runs[-1]
    if last.get("status") not in ("pending", "running", "pending_approval"):
        raise ValueError(f"ultimo run nao esta aguardando aprovacao: {last.get('status')}")

    last["status"] = "approved"
    last["approved_at"] = datetime.now().isoformat(timespec="seconds")
    runs_path.write_text(
        "\n".join(json.dumps(r, ensure_ascii=False) for r in runs) + "\n",
        encoding="utf-8",
    )

    # Append na decisions.md
    _append_decision(
        slug, last["stage_id"], last["run_id"], "aprovado", feedback=None
    )

    # Avanca current_stage
    state = project_status(slug)
    next_stage = _next_stage(state["pipeline"], last["stage_id"])
    if next_stage is None:
        _update_frontmatter(slug, {"status": "completed"})
    else:
        _update_frontmatter(slug, {"current_stage": next_stage["id"]})

    return project_status(slug)


def reject_stage(slug: str, feedback: str) -> dict:
    """Rejeita o ultimo run e mantem current_stage (proxima execucao re-roda com feedback)."""
    project_dir = PROJECTS_ROOT / slug
    runs_path = project_dir / "runs.jsonl"
    runs = _read_jsonl(runs_path)
    if not runs:
        raise ValueError("nenhum run para rejeitar")

    last = runs[-1]
    last["status"] = "rejected"
    last["rejected_at"] = datetime.now().isoformat(timespec="seconds")
    last["feedback"] = feedback
    runs_path.write_text(
        "\n".join(json.dumps(r, ensure_ascii=False) for r in runs) + "\n",
        encoding="utf-8",
    )

    _append_decision(
        slug, last["stage_id"], last["run_id"], "rejeitado", feedback=feedback
    )
    return project_status(slug)


def _append_decision(slug: str, stage_id: str, run_id: str, decision: str, feedback: Optional[str]):
    """Append entry humanizada em decisions.md."""
    when = datetime.now().strftime("%Y-%m-%d %H:%M")
    block = [f"\n## {when} — {stage_id} ({run_id})", f"- **Decisao:** {decision}"]
    if feedback:
        block.append(f"- **Feedback:** {feedback}")
    block.append("")
    decisions_md = PROJECTS_ROOT / slug / "decisions.md"
    with decisions_md.open("a", encoding="utf-8") as f:
        f.write("\n".join(block) + "\n")
```

- [ ] **Step 15: Run all tests, watch them pass**

Run: `python -m pytest scripts/tests/test_project_manager.py -v`
Expected: ~14-18 tests pass (slugify, template, frontmatter, create, list, status, append_run, advance, approve, reject).

---

## Task 5: Add CLI argparse main()

**Files:**
- Modify: `scripts/project_manager.py` — append `main()` and `if __name__ == "__main__"` block

- [ ] **Step 1: Append CLI**

Append to `scripts/project_manager.py`:

```python
# ---------- CLI ----------

def _print_status(state: dict) -> None:
    print(f"\nProjeto: {state['name']} ({state['slug']})")
    print(f"Tipo: {state['type']}  Status: {state['status']}")
    print(f"Stage atual: {state['current_stage']}")
    print(f"Total de runs: {state['total_runs']}")
    if state.get("last_run"):
        lr = state["last_run"]
        print(
            f"Ultimo run: {lr.get('run_id')} stage={lr.get('stage_id')} "
            f"status={lr.get('status')} iter={lr.get('iteration')}"
        )
    print("\nPipeline:")
    for s in state["pipeline"]:
        marker = ">" if s["id"] == state["current_stage"] else " "
        approval = s.get("approval", state["default_approval"])
        print(f"  {marker} {s['id']:<14} agent={s['agent']:<18} approval={approval}")


def _print_list(projects: list[dict]) -> None:
    if not projects:
        print("Nenhum projeto encontrado em workspace/projects/.")
        return
    print(f"\n{len(projects)} projeto(s):\n")
    for p in projects:
        print(
            f"  [{p['status']:<10}] {p['slug']:<28} tipo={p['type']:<12} "
            f"stage={p['current_stage']}"
        )


def main():
    parser = argparse.ArgumentParser(
        description="Workflow de projetos do Marketing OS (handoffs + approvals)."
    )
    sub = parser.add_subparsers(dest="cmd")

    p_novo = sub.add_parser("novo", help="Criar novo projeto")
    p_novo.add_argument("name")
    p_novo.add_argument(
        "--tipo", required=True, choices=PROJECT_TYPES, help="Tipo do projeto"
    )

    sub.add_parser("list", help="Listar projetos")

    p_status = sub.add_parser("status", help="Mostrar estado de um projeto")
    p_status.add_argument("slug")

    p_avancar = sub.add_parser("avancar", help="Cria run pendente pro stage atual")
    p_avancar.add_argument("slug")

    p_aprovar = sub.add_parser("aprovar", help="Aprova ultimo run e avanca stage")
    p_aprovar.add_argument("slug")

    p_rejeitar = sub.add_parser("rejeitar", help="Rejeita ultimo run com feedback")
    p_rejeitar.add_argument("slug")
    p_rejeitar.add_argument("feedback")

    args = parser.parse_args()
    if not args.cmd:
        parser.print_help()
        sys.exit(1)

    try:
        if args.cmd == "novo":
            project_dir = create_project(args.name, args.tipo)
            print(f"Projeto criado em {project_dir}")
            _print_status(project_status(slugify(args.name)))
        elif args.cmd == "list":
            _print_list(list_projects())
        elif args.cmd == "status":
            _print_status(project_status(args.slug))
        elif args.cmd == "avancar":
            run = advance_stage(args.slug)
            print(f"Run pendente criado: {run['run_id']} stage={run['stage_id']} agent={run['agent']}")
            print("Agora /projeto despacha o agente. Quando terminar, use /projeto aprovar ou rejeitar.")
        elif args.cmd == "aprovar":
            state = approve_stage(args.slug)
            print(f"Stage aprovado. Novo stage atual: {state['current_stage']} (status={state['status']})")
        elif args.cmd == "rejeitar":
            state = reject_stage(args.slug, args.feedback)
            print(f"Stage rejeitado. Stage atual continua: {state['current_stage']}")
            print(f"Feedback registrado em decisions.md.")
    except (ValueError, FileNotFoundError, FileExistsError) as e:
        print(f"ERRO: {e}", file=sys.stderr)
        sys.exit(2)


if __name__ == "__main__":
    main()
```

- [ ] **Step 2: Test CLI smoke (sem tests automatizados — manual smoke)**

Run:
```bash
python scripts/project_manager.py --help
python scripts/project_manager.py novo --help
```
Expected: argparse help mostra subcommands + flags.

- [ ] **Step 3: Run full test suite**

Run: `python -m pytest scripts/tests/test_project_manager.py -v`
Expected: all pass.

---

## Task 6: Update mos.py CLI registry

**Files:**
- Modify: `scripts/mos.py:89-95` (subcommand mappings) and lines 110-115 (command_args), 179-181 (help text)

- [ ] **Step 1: Read current mos.py registry**

Run: `grep -n "project" scripts/mos.py`
Note the line numbers for project entries.

- [ ] **Step 2: Replace project subcommands block**

Use Edit on `scripts/mos.py`:

Replace the `"project": { ... }` dict (around line 89-95) with:

```python
    "project": {
        "novo": ("project_manager.py", "Cria novo projeto"),
        "list": ("project_manager.py", "Lista projetos"),
        "status": ("project_manager.py", "Status de um projeto"),
        "avancar": ("project_manager.py", "Despacha proximo stage do pipeline"),
        "aprovar": ("project_manager.py", "Aprova stage e avanca"),
        "rejeitar": ("project_manager.py", "Rejeita stage com feedback"),
    },
```

Replace the `("project", ...)` lambdas (around line 110-115) with:

```python
    ("project", "novo"): lambda args: ["novo"] + args,
    ("project", "list"): lambda args: ["list"] + args,
    ("project", "status"): lambda args: ["status"] + args,
    ("project", "avancar"): lambda args: ["avancar"] + args,
    ("project", "aprovar"): lambda args: ["aprovar"] + args,
    ("project", "rejeitar"): lambda args: ["rejeitar"] + args,
```

Replace help text (around line 179-181):

```python
    mos project novo "Lançamento Curso" --tipo lancamento
    mos project list
    mos project status lancamento-curso
    mos project avancar lancamento-curso
    mos project aprovar lancamento-curso
    mos project rejeitar lancamento-curso "feedback"
```

Remove the docstring lines `python mos.py project create/list/status` from the top of mos.py and replace with new commands.

- [ ] **Step 3: Smoke test mos.py CLI**

Run:
```bash
python scripts/mos.py project novo --help 2>&1 || python scripts/mos.py project novo "Teste" --tipo lancamento --help
python scripts/mos.py project list
```

Expected: help works; list returns "Nenhum projeto" (workspace ainda vazio).

---

## Task 7: Create /projeto slash command

**Files:**
- Create: `commands/projeto.md`

- [ ] **Step 1: Write the slash command file**

Content of `commands/projeto.md`:

````markdown
---
description: Workflow de projetos com pipeline declarativo, dispatch sequencial dos mos-* e approval gates entre stages. Subcomandos novo|list|status|avancar|aprovar|rejeitar.
argument-hint: "<subcomando> [args] (ex: novo \"Lançamento X\" --tipo lancamento)"
---

# /projeto: Gestao de projetos com workflow estruturado

Substitui o gerenciamento ad-hoc de projetos por um pipeline declarativo, com handoffs entre subagents `mos-*` e approval gates entre stages. Cada projeto vive em `workspace/projects/<slug>/`.

## Subcomandos

- `/projeto novo "<nome>" --tipo {lancamento|perpetuo|consultoria|mentoria}` — cria projeto novo a partir do template do tipo
- `/projeto list` — lista todos os projetos com status atual
- `/projeto status <slug>` — mostra detalhe (pipeline, stage atual, ultimo run)
- `/projeto avancar <slug>` — despacha o agente do stage atual e marca run como pending_approval
- `/projeto aprovar <slug>` — aprova ultimo run e avanca pra proximo stage
- `/projeto rejeitar <slug> "<feedback>"` — rejeita ultimo run; proxima execucao roda novamente com o feedback

## Como cada subcomando se comporta

### novo / list / status / aprovar / rejeitar

Tarefas determinísticas. Roda direto via Bash:

```
Bash("python scripts/project_manager.py <subcomando> [args]")
```

Mostra a saída pro usuario sem reformatar — o script ja imprime estado human-readable.

### avancar (orquestrador real)

Esse subcomando NAO eh determinístico — ele despacha um subagent. Fluxo:

1. **Lê estado:** `Bash("python scripts/project_manager.py status <slug>")` retorna pipeline, stage atual, agente daquele stage.
2. **Cria run pendente:** `Bash("python scripts/project_manager.py avancar <slug>")` registra `run_NNN` em `runs.jsonl` com status=pending.
3. **Monta contexto:** lê `workspace/projects/<slug>/project.md` (briefing) + outputs anteriores das pastas `<NN>-<stage>/` se existirem.
4. **Despacha agente:** `Agent(subagent_type: "mos-<x>", prompt: "<briefing + outputs anteriores + feedback se houver iteracao>2>")`.
5. **Salva output:** o resultado vai pra `workspace/projects/<slug>/<NN>-<stage_id>/draft-vN.md` (N = numero da iteracao).
6. **Atualiza run:** marca o run no `runs.jsonl` como `status=pending_approval` e adiciona campo `output: <path>`.
7. **Mostra ao usuario:** preview do output + instrucao "use /projeto aprovar <slug> ou /projeto rejeitar <slug> \"motivo\"".

Importante:
- Se o stage anterior teve iteracao com feedback, incluir o feedback no prompt do novo run.
- Se `approval: skip` no stage atual, ja chama `aprovar` automaticamente sem pausar.
- Se ja for o ultimo stage da pipeline, ao aprovar marca o projeto como `status: completed`.

## Exemplo de uso completo

```
> /projeto novo "Lançamento Curso IA" --tipo lancamento
Projeto criado. Stage atual: research. Agente: mos-research.

> /projeto avancar lancamento-curso-ia
[mos-research roda automaticamente, despacha pesquisa de mercado]
Output salvo em 01-research/draft-v1.md.
Use /projeto aprovar ou /projeto rejeitar.

> /projeto aprovar lancamento-curso-ia
Stage aprovado. Avancou pra: estrategia. Agente: mos-launch.

> /projeto avancar lancamento-curso-ia
[mos-launch roda]
Output em 02-estrategia/draft-v1.md.

> /projeto rejeitar lancamento-curso-ia "muito agressivo, suaviza tom"
Rejeitado. Feedback registrado em decisions.md.

> /projeto avancar lancamento-curso-ia
[mos-launch roda novamente, prompt agora inclui o feedback]
Output em 02-estrategia/draft-v2.md.
```

## Quando NAO usar /projeto

- Tarefa one-shot rapida (1 post, 1 email): use `/criar-*` direto, nao precisa pipeline.
- Pergunta conceitual: responda inline sem criar projeto.
- Campanha completa em paralelo sem necessidade de approval: use `/campanha-*` direto.

`/projeto` eh pra quando voce quer rastreabilidade entre stages, controle de aprovacao e capacidade de retomar dias depois.
````

- [ ] **Step 2: Verify command shows up in test_commands_dispatch**

Run: `python -m pytest scripts/tests/test_commands_dispatch.py -v`
Expected: PASS (projeto.md tem `Agent(subagent_type:` no body, então não precisa estar em UTILITY_COMMANDS).

Se falhar com "no dispatch found" no `/projeto`: o comando faz dispatch dinâmico (não literalmente `Agent(subagent_type: "mos-...")`)  então pode precisar adicionar `projeto.md` ao set `UTILITY_COMMANDS` em `scripts/tests/test_commands_dispatch.py`.

- [ ] **Step 3: Add projeto.md to UTILITY_COMMANDS if test fails**

Edit `scripts/tests/test_commands_dispatch.py`:

```python
UTILITY_COMMANDS = {
    "publicar-notion.md",
    "campanha.md",
    "projeto.md",  # orquestrador dinamico, dispatch determinado em runtime pelo pipeline
}
```

Re-run test, expect pass.

---

## Task 8: Update mos-infoproduct.md reference

**Files:**
- Modify: `agents/mos-infoproduct.md:59`

- [ ] **Step 1: Read current line**

Run: `sed -n '55,65p' agents/mos-infoproduct.md`
Expected: ver bloco que cita `python3 scripts/project_manager.py create "infoproduto-X"`.

- [ ] **Step 2: Replace with new command**

Use Edit:

```
old_string: python3 scripts/project_manager.py create "infoproduto-X"
new_string: python3 scripts/project_manager.py novo "infoproduto-X" --tipo mentoria
```

Se o contexto da linha sugerir tipo diferente (lancamento), usar `--tipo lancamento`.

---

## Task 9: Update docs (ARCHITECTURE.md + STORY-001)

**Files:**
- Modify: `docs/ARCHITECTURE.md:596`
- Modify: `docs/stories/active/STORY-001-atualizar-readme-scripts.md` (linhas 32, 65)

- [ ] **Step 1: Update ARCHITECTURE.md**

Read context line 590-600:

Run: `sed -n '590,600p' docs/ARCHITECTURE.md`

Edit the description of `project_manager.py`:

```
old: PM["project_manager.py\nGerenciamento de projetos"]
new: PM["project_manager.py\nWorkflow + handoffs + approval gates"]
```

- [ ] **Step 2: Update STORY-001 mentions**

Read context:

Run: `grep -n "project_manager" docs/stories/active/STORY-001-atualizar-readme-scripts.md`

Mantém menção (story está concluída, é histórico). Apenas adiciona uma nota no final da story se relevante; senão deixa quieto.

---

## Task 10: Verify end-to-end with manual smoke test

**Files:**
- None — manual integration test

- [ ] **Step 1: Run full test suite**

Run: `python -m pytest scripts/tests/ -v -m "not smoke"`
Expected: all pass (incluindo o novo test_project_manager.py + test_commands_dispatch.py + test_workspace_separation.py).

- [ ] **Step 2: Manual smoke — criar projeto, avancar, aprovar**

Run:
```bash
python scripts/project_manager.py novo "Smoke Test Lançamento" --tipo lancamento
python scripts/project_manager.py status smoke-test-lancamento
python scripts/project_manager.py avancar smoke-test-lancamento
python scripts/project_manager.py aprovar smoke-test-lancamento
python scripts/project_manager.py status smoke-test-lancamento
```

Expected:
- novo: cria pasta `workspace/projects/smoke-test-lancamento/` com 3 arquivos
- status: mostra pipeline, stage research, 0 runs
- avancar: cria run_001 pendente pra mos-research
- aprovar: avanca pra estrategia, run_001 marcado como approved
- status final: stage atual = estrategia, total_runs = 1, last_run.status = approved

- [ ] **Step 3: Cleanup smoke test**

Run: `rm -rf workspace/projects/smoke-test-lancamento`

- [ ] **Step 4: Validate workspace separation test ainda passa**

Run: `python -m pytest scripts/tests/test_workspace_separation.py -v`
Expected: PASS (workspace/projects/ é gitignored, não vaza).

---

## Task 11: Commit + CHANGELOG

**Files:**
- Modify: `CHANGELOG.md` (adicionar entrada na proxima versao)

- [ ] **Step 1: Check current version + last entry**

Run: `head -30 CHANGELOG.md`

- [ ] **Step 2: Add entry**

Adicionar no topo do CHANGELOG sob nova versao (incrementar minor, ex: 6.7.0):

```markdown
## [6.7.0] - 2026-05-09

### Added
- `/projeto` slash command: workflow de projetos com pipeline declarativo, dispatch sequencial dos `mos-*` e approval gates. Subcomandos: novo, list, status, avancar, aprovar, rejeitar.
- 4 templates de projeto em `scripts/templates/projeto/`: lancamento, perpetuo, consultoria, mentoria. Cada um com pipeline default + stages.
- `runs.jsonl` append-only por projeto pra rastrear execucoes (run_id, stage_id, agent, iteration, status, timestamps).
- `decisions.md` por projeto pra historico human-readable de aprovacoes/rejeicoes.

### Changed
- `scripts/project_manager.py` reescrito do zero. CRUD anterior (project.json + content/ + notes) substituido por state machine declarativa em `project.md` com YAML frontmatter.
- `scripts/mos.py`: subcomandos `mos project` agora sao `novo|list|status|avancar|aprovar|rejeitar` (antes: create|list|status|add-content|complete|note).

### Migration notes
Quem usava `mos project create` deve migrar pra `mos project novo`. Pasta `output/projects/` antiga nao eh mais lida — projetos novos vivem em `workspace/projects/`.
```

Bump version em `.claude-plugin/plugin.json` e `.claude-plugin/marketplace.json` pra `6.7.0`.

- [ ] **Step 3: Run full test suite once more**

Run: `python -m pytest scripts/tests/ -v -m "not smoke" && python scripts/validate_agents.py --strict`
Expected: tudo verde.

- [ ] **Step 4: Commit**

```bash
git add commands/projeto.md scripts/project_manager.py scripts/templates/projeto/ scripts/tests/test_project_manager.py scripts/mos.py scripts/tests/test_commands_dispatch.py agents/mos-infoproduct.md docs/ARCHITECTURE.md docs/stories/active/STORY-001-atualizar-readme-scripts.md CHANGELOG.md .claude-plugin/plugin.json .claude-plugin/marketplace.json
git commit -m "$(cat <<'EOF'
feat(projeto): workflow MVP com handoffs e approval gates

- /projeto slash command com novo|list|status|avancar|aprovar|rejeitar
- 4 templates por tipo (lancamento, perpetuo, consultoria, mentoria)
- project_manager.py reescrito: state machine YAML + runs.jsonl + decisions.md
- Substitui CRUD anterior; consenso de design Claude+Codex (gpt-5.5/high)

Co-Authored-By: Claude Opus 4.7 <noreply@anthropic.com>
EOF
)"
```

---

## Self-Review Checklist

- [x] **Spec coverage:** Cada item do spec consolidado tem task correspondente?
  - Markdown+frontmatter: Task 3 + Task 4
  - runs.jsonl: Task 4 (append_run + tests)
  - decisions.md: Task 4 (_append_decision)
  - Pipeline declarativa: Task 3 (templates) + Task 4 (parsing)
  - approval per type + override per stage: Templates já têm `default_approval` + per-stage `approval`. Lógica em `_print_status` mostra herança.
  - 4 templates por tipo: Task 3
  - Comandos novo|list|status|avancar|aprovar|rejeitar: Task 5 (CLI) + Task 7 (slash)
  - Iteração com feedback: Task 4 (`_stage_iteration` + reject_stage salva feedback)
  - Atualizar referências: Task 6 (mos.py), Task 8 (mos-infoproduct), Task 9 (docs)

- [x] **No placeholders:** Cada step contém código exato. Nenhum "TODO" ou "implement later".

- [x] **Type consistency:** Funções referenciadas em testes (`create_project`, `list_projects`, `project_status`, `advance_stage`, `approve_stage`, `reject_stage`, `append_run`, `slugify`, `load_template`, `parse_frontmatter`, `serialize_frontmatter`, `PROJECT_TYPES`) batem com as implementações nas tasks 4 e 5.

- [x] **Convenções do repo:** segue padrão de comandos em `commands/*.md`, scripts em `scripts/*.py`, tests em `scripts/tests/test_*.py`, documentação em `docs/`. Workspace gitignored. Frontmatter em comandos. Assinatura `Co-Authored-By: Claude Opus 4.7` no commit.

- [x] **Faseamento respeitado:** MVP entrega flat sequential. Sem paralelismo (parallel/join), sem auto_approve, sem artifacts/ separados, sem published_at. Esses ficam pra Fase 2 condicional ao uso real.

---

## Execução

Plano salvo em `docs/superpowers/plans/2026-05-09-projeto-mvp.md`. Duas opções:

1. **Subagent-Driven (recomendado)** — dispatcho fresh subagent por task, revisão entre tasks, iteração rápida
2. **Inline Execution** — executo tasks nesta sessão com checkpoints pra revisão em batches

Qual?
