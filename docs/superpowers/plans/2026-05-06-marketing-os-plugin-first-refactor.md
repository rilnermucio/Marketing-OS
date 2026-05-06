# Marketing OS Plugin-First Refactor — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Refatorar o repo Marketing OS para identidade plugin-first do Claude Code: consolidar 4 cópias de marketing-os em 1, separar plugin distribuível de workspace pessoal (gitignored), remover framework AIOS dormante, garantir verificabilidade via testes Tier 1 (estáticos) e Tier 2 (smoke via `claude -p`).

**Architecture:** Trabalho em 5 fases sequenciais sobre branch `refactor/plugin-first`. Cada fase termina com commit + testes verdes. TDD onde aplicável (testes phase-specific escritos antes da mudança). Rollback via `git reset --hard` por fase.

**Tech Stack:** Python 3.8+ (pytest, PyYAML opcional, stdlib), Bash, Git, Claude Code CLI (`claude -p` para smoke tests via subscription Max), Markdown.

**Spec:** `docs/superpowers/specs/2026-05-06-marketing-os-plugin-first-refactor-design.md`

---

## File Structure

### New files to create

| Path | Responsibility |
|---|---|
| `scripts/tests/__init__.py` | Marca pytest package |
| `scripts/tests/conftest.py` | Fixtures compartilhadas (project_root, etc) |
| `scripts/tests/test_plugin_manifest.py` | Valida `plugin.json` schema, versão, campos obrigatórios |
| `scripts/tests/test_skill_md.py` | Valida frontmatter de `skills/marketing-os/SKILL.md` |
| `scripts/tests/test_subagents.py` | Itera `subagents/*.md`, valida estrutura |
| `scripts/tests/test_native_agents.py` | Wrappa `validate_agents.py` em pytest, valida `.claude/agents/` |
| `scripts/tests/test_no_dangling_refs.py` | Detecta links/refs internos quebrados em `.md` |
| `scripts/tests/test_no_aios_residue.py` | Falha se encontrar AIOS strings (ativado após Phase 3) |
| `scripts/tests/test_workspace_separation.py` | Valida que arquivos do plugin não referenciam `workspace/` |
| `scripts/tests/test_no_dangling_symlinks.py` | `find . -xtype l` retorna vazio (broken symlinks) |
| `scripts/tests/test_agents_smoke.py` | Smoke tests via `claude -p` (Tier 2) |
| `tests/snapshots/baseline/.gitkeep` | Marca diretório de baselines |
| `tests/snapshots/baseline/<agent>.txt` | Output baseline de cada agente smoke-tested (5-6 arquivos) |
| `workspace/.gitkeep` | Marca workspace |
| `workspace/{drafts,brand,outputs,research,landing-pages,media}/.gitkeep` | Marca subdirs |

### Files to modify

| Path | Mudança |
|---|---|
| `.gitignore` | Adicionar workspace/, .pre-migration.backup, etc |
| `.claude/CLAUDE.md` | Reescrita completa (~40 linhas, sem AIOS) |
| `README.md` | Reescrita completa (~5 KB, focada em plugin) |
| `CHANGELOG.md` | Adicionar entrada da refatoração v6.0.0 |
| `plugin.json` | Possivelmente atualizar description |
| `package.json` | Sync versão para 5.1.0 ou deletar |
| `skills/marketing-os/SKILL.md` | Fundir conteúdo único de `skill-package/marketing-os/SKILL.md` |
| `pytest.ini` | Adicionar markers `@pytest.mark.aios_removed`, `@pytest.mark.smoke` |

### Files/dirs to delete

`.aios/`, `.aios-core/`, `.aios-installation-config.yaml`, `.aios-pm-config.yaml`, `.antigravity/`, `.codex/`, `squads/`, `AGENTS.md`, `skill-package/`, `marketing-os/` (root, com symlinks), `.claude/rules/{workflow-execution,story-lifecycle,ids-principles,agent-authority,coderabbit-integration}.md`, todos `*.pre-migration.backup`, `.env.backup.*`, `.DS_Store` (todos), opcionalmente `package.json`/`node_modules/`/`AGENTS.md`/`GUIA-DE-USO.md`/`INSTALACAO-SKILL.md` baseado em decisão da Phase 4.

### Files to move

| De | Para |
|---|---|
| `carrossel-instagram-*.md`, `Roteiro_*.md` (root) | `workspace/drafts/` |
| `vertice-logo.svg`, `vertice-symbol.png` (root) | `workspace/brand/` |
| `outputs/`, `output/` (se existir) | `workspace/outputs/` |
| `research/` (root) | `workspace/research/` |
| `landing-pages/` (root) | `workspace/landing-pages/` |
| `media/` (root) | `workspace/media/` |

---

## Phase 0 — Safety Net & Baseline

### Task 0.1: Create branch and capture baseline

**Files:**
- Modify: git state (branch, commits)

- [ ] **Step 1: Verify clean working tree (or stash modifications)**

```bash
cd "/Users/rilner/Marketing OS"
git status --short
```

If output shows modifications, decide: commit them on main first OR stash them.

- [ ] **Step 2: Create the refactor branch**

```bash
git checkout -b refactor/plugin-first
git status
```

Expected: `On branch refactor/plugin-first`, working tree clean (or with same untracked items as before).

- [ ] **Step 3: Capture baseline tree and disk usage**

```bash
mkdir -p /tmp/marketing-os-baseline
tree -L 2 -a -I '.git|node_modules|.pytest_cache|__pycache__' . > /tmp/marketing-os-baseline/before-tree.txt
du -sh */ .[^.]*/ 2>/dev/null | sort -hr > /tmp/marketing-os-baseline/before-du.txt
git rev-parse HEAD > /tmp/marketing-os-baseline/baseline-sha.txt
echo "Baseline captured at $(date)"
cat /tmp/marketing-os-baseline/baseline-sha.txt
```

Expected: SHA visible, files populated.

- [ ] **Step 4: Stage existing untracked work that we will keep**

The currently-untracked `scripts/validate_agents.py` will be the foundation of Tier 1 tests. Add it now (and other untracked items that belong to the plugin) to baseline.

```bash
git add scripts/validate_agents.py
git status --short
```

- [ ] **Step 5: Initial commit on the refactor branch**

```bash
git commit -m "$(cat <<'EOF'
chore(refactor): initial baseline for plugin-first refactor

- Stage existing scripts/validate_agents.py (was untracked)
- Branch from main, ready for phased refactor per spec
  docs/superpowers/specs/2026-05-06-marketing-os-plugin-first-refactor-design.md
EOF
)"
```

---

### Task 0.2: Set up pytest test infrastructure

**Files:**
- Create: `scripts/tests/__init__.py`
- Create: `scripts/tests/conftest.py`
- Modify: `pytest.ini`

- [ ] **Step 1: Create `scripts/tests/__init__.py` (empty file)**

```bash
touch scripts/tests/__init__.py
```

- [ ] **Step 2: Create `scripts/tests/conftest.py`**

```python
"""Shared fixtures for Marketing OS tests."""
from __future__ import annotations

from pathlib import Path

import pytest


@pytest.fixture(scope="session")
def project_root() -> Path:
    """Absolute path to the project root."""
    return Path(__file__).resolve().parent.parent.parent


@pytest.fixture(scope="session")
def plugin_dirs(project_root: Path) -> dict[str, Path]:
    """Plugin-side directories that ship with the distributable plugin."""
    return {
        "skills": project_root / "skills",
        "subagents": project_root / "subagents",
        "commands": project_root / "commands",
        "workflows": project_root / "workflows",
        "assets": project_root / "assets",
        "references": project_root / "references",
        "scripts": project_root / "scripts",
        "docs": project_root / "docs",
        "claude_agents": project_root / ".claude" / "agents",
    }


@pytest.fixture(scope="session")
def workspace_root(project_root: Path) -> Path:
    """User-side workspace directory (gitignored)."""
    return project_root / "workspace"
```

- [ ] **Step 3: Update `pytest.ini` to register markers**

Read current `pytest.ini` first:

```bash
cat pytest.ini
```

Then update it (or create if minimal) to:

```ini
[pytest]
testpaths = scripts/tests
python_files = test_*.py
python_classes = Test*
python_functions = test_*
markers =
    aios_removed: tests that only pass after Phase 3 (AIOS deleted)
    workspace_extracted: tests that only pass after Phase 1 (workspace/ exists)
    consolidated: tests that only pass after Phase 2 (single marketing-os)
    smoke: Tier 2 smoke tests using claude -p (slower, requires Claude Code login)
```

- [ ] **Step 4: Verify pytest can discover the test directory**

```bash
pytest --collect-only scripts/tests/ 2>&1 | head -20
```

Expected: collects 0 tests (no tests yet) without errors.

- [ ] **Step 5: Commit**

```bash
git add scripts/tests/__init__.py scripts/tests/conftest.py pytest.ini
git commit -m "test: scaffold pytest infrastructure with shared fixtures"
```

---

### Task 0.3: Add Tier 1 test — plugin manifest

**Files:**
- Create: `scripts/tests/test_plugin_manifest.py`

- [ ] **Step 1: Write the failing test (file doesn't exist yet)**

```python
"""Validates plugin.json structure."""
from __future__ import annotations

import json
from pathlib import Path

import pytest


REQUIRED_FIELDS = {"name", "version", "description"}
EXPECTED_NAME = "marketing-os"


@pytest.fixture(scope="module")
def plugin_manifest(project_root: Path) -> dict:
    manifest_path = project_root / "plugin.json"
    assert manifest_path.exists(), f"plugin.json missing: {manifest_path}"
    return json.loads(manifest_path.read_text(encoding="utf-8"))


def test_plugin_manifest_is_valid_json(plugin_manifest: dict) -> None:
    assert isinstance(plugin_manifest, dict)


def test_plugin_manifest_has_required_fields(plugin_manifest: dict) -> None:
    missing = REQUIRED_FIELDS - set(plugin_manifest.keys())
    assert not missing, f"plugin.json missing required fields: {missing}"


def test_plugin_manifest_name(plugin_manifest: dict) -> None:
    assert plugin_manifest["name"] == EXPECTED_NAME


def test_plugin_manifest_version_is_semver(plugin_manifest: dict) -> None:
    version = plugin_manifest["version"]
    parts = version.split(".")
    assert len(parts) == 3, f"Version not semver: {version}"
    for part in parts:
        assert part.isdigit(), f"Non-numeric version part: {part}"


def test_plugin_manifest_skills_paths_exist(plugin_manifest: dict, project_root: Path) -> None:
    skills = plugin_manifest.get("skills", [])
    for skill_path in skills:
        full = project_root / skill_path
        assert full.exists(), f"plugin.json declares skill at {skill_path} but path does not exist"
```

Save to `scripts/tests/test_plugin_manifest.py`.

- [ ] **Step 2: Run the tests**

```bash
pytest scripts/tests/test_plugin_manifest.py -v
```

Expected: all tests pass on current state (plugin.json exists and is valid).

- [ ] **Step 3: Commit**

```bash
git add scripts/tests/test_plugin_manifest.py
git commit -m "test: add plugin manifest validation tests"
```

---

### Task 0.4: Add Tier 1 test — SKILL.md frontmatter

**Files:**
- Create: `scripts/tests/test_skill_md.py`

- [ ] **Step 1: Inspect current SKILL.md frontmatter**

```bash
head -30 skills/marketing-os/SKILL.md
```

Note the frontmatter fields (typically: name, description, allowed-tools, etc).

- [ ] **Step 2: Write the test**

```python
"""Validates skills/marketing-os/SKILL.md frontmatter."""
from __future__ import annotations

from pathlib import Path

import pytest


REQUIRED_SKILL_FIELDS = {"name", "description"}


def _parse_frontmatter(content: str) -> dict | None:
    """Minimal YAML frontmatter parser (flat keys only)."""
    if not content.startswith("---\n"):
        return None
    end = content.find("\n---", 4)
    if end == -1:
        return None
    fm = content[4:end]
    result: dict = {}
    for line in fm.splitlines():
        line = line.strip()
        if not line or line.startswith("#") or ":" not in line:
            continue
        key, _, value = line.partition(":")
        result[key.strip()] = value.strip().strip('"').strip("'")
    return result


@pytest.fixture(scope="module")
def skill_md(project_root: Path) -> tuple[dict, str]:
    skill_path = project_root / "skills" / "marketing-os" / "SKILL.md"
    assert skill_path.exists(), f"SKILL.md missing: {skill_path}"
    content = skill_path.read_text(encoding="utf-8")
    fm = _parse_frontmatter(content)
    assert fm is not None, "SKILL.md has no YAML frontmatter"
    return fm, content


def test_skill_md_has_required_fields(skill_md: tuple[dict, str]) -> None:
    fm, _ = skill_md
    missing = REQUIRED_SKILL_FIELDS - set(fm.keys())
    assert not missing, f"SKILL.md missing required frontmatter fields: {missing}"


def test_skill_md_name_matches_plugin(skill_md: tuple[dict, str], project_root: Path) -> None:
    import json
    fm, _ = skill_md
    plugin = json.loads((project_root / "plugin.json").read_text(encoding="utf-8"))
    assert fm["name"] == plugin["name"], (
        f"SKILL.md name='{fm['name']}' should match plugin.json name='{plugin['name']}'"
    )


def test_skill_md_body_not_empty(skill_md: tuple[dict, str]) -> None:
    _, content = skill_md
    body_after_fm = content.split("---", 2)[-1]
    assert len(body_after_fm.strip()) > 100, "SKILL.md body too short (<100 chars)"
```

- [ ] **Step 3: Run the tests**

```bash
pytest scripts/tests/test_skill_md.py -v
```

If a test fails, inspect the actual SKILL.md frontmatter and adjust the expected fields. The tests should pass against the current canonical SKILL.md.

- [ ] **Step 4: Commit**

```bash
git add scripts/tests/test_skill_md.py
git commit -m "test: add SKILL.md frontmatter validation"
```

---

### Task 0.5: Add Tier 1 test — subagents knowledge base

**Files:**
- Create: `scripts/tests/test_subagents.py`

- [ ] **Step 1: Write the test**

```python
"""Validates subagents/ knowledge base files (Tier-2 in Marketing OS layering)."""
from __future__ import annotations

from pathlib import Path

import pytest


def test_subagents_dir_exists(project_root: Path) -> None:
    assert (project_root / "subagents").is_dir()


def test_subagents_dir_has_files(project_root: Path) -> None:
    md_files = list((project_root / "subagents").rglob("*.md"))
    assert len(md_files) > 0, "No .md files found in subagents/"


@pytest.mark.parametrize("path", list((Path(__file__).parent.parent.parent / "subagents").rglob("*.md")), ids=lambda p: p.relative_to(Path(__file__).parent.parent.parent / "subagents").as_posix())
def test_subagent_file_readable_and_nonempty(path: Path) -> None:
    content = path.read_text(encoding="utf-8")
    assert len(content) > 50, f"Subagent file suspiciously short: {path.name}"


@pytest.mark.parametrize("path", list((Path(__file__).parent.parent.parent / "subagents").rglob("*.md")), ids=lambda p: p.relative_to(Path(__file__).parent.parent.parent / "subagents").as_posix())
def test_subagent_has_heading(path: Path) -> None:
    content = path.read_text(encoding="utf-8")
    assert "# " in content or "## " in content, f"No markdown headings in {path.name}"
```

- [ ] **Step 2: Run the test**

```bash
pytest scripts/tests/test_subagents.py -v
```

Expected: passes (current subagents/ has .md files with headings).

- [ ] **Step 3: Commit**

```bash
git add scripts/tests/test_subagents.py
git commit -m "test: add subagents knowledge base validation"
```

---

### Task 0.6: Add Tier 1 test — wrap validate_agents.py

**Files:**
- Create: `scripts/tests/test_native_agents.py`

- [ ] **Step 1: Write the test that wraps existing validate_agents.py**

```python
"""Wraps scripts/validate_agents.py in pytest. Validates .claude/agents/ native subagents."""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

import pytest


def test_validate_agents_script_exists(project_root: Path) -> None:
    script = project_root / "scripts" / "validate_agents.py"
    assert script.exists(), f"validate_agents.py missing: {script}"


def test_native_agents_dir_exists(project_root: Path) -> None:
    agents_dir = project_root / ".claude" / "agents"
    assert agents_dir.is_dir(), f".claude/agents/ missing"


def test_native_agents_validate_clean(project_root: Path) -> None:
    """Run validate_agents.py and ensure exit code 0 (no errors, warnings allowed)."""
    result = subprocess.run(
        [sys.executable, "scripts/validate_agents.py"],
        capture_output=True,
        text=True,
        cwd=str(project_root),
        timeout=60,
    )
    assert result.returncode == 0, (
        f"validate_agents.py failed (exit {result.returncode}):\n"
        f"STDOUT:\n{result.stdout}\nSTDERR:\n{result.stderr}"
    )
```

- [ ] **Step 2: Run the test**

```bash
pytest scripts/tests/test_native_agents.py -v
```

Expected: passes if validate_agents.py reports OK on the current state. If it fails, inspect the script's output to see which native agents have issues, and decide whether to fix them now or accept current warnings.

- [ ] **Step 3: Commit**

```bash
git add scripts/tests/test_native_agents.py
git commit -m "test: wrap validate_agents.py in pytest for CI integration"
```

---

### Task 0.7: Add Tier 1 test — dangling symlinks

**Files:**
- Create: `scripts/tests/test_no_dangling_symlinks.py`

- [ ] **Step 1: Write the test**

```python
"""Detects broken symlinks in the project tree."""
from __future__ import annotations

import subprocess
from pathlib import Path


EXCLUDE_DIRS = {".git", "node_modules", ".pytest_cache", "__pycache__"}


def test_no_dangling_symlinks(project_root: Path) -> None:
    result = subprocess.run(
        [
            "find", str(project_root),
            "-type", "l",
            "!", "-name", ".git",
        ],
        capture_output=True,
        text=True,
    )
    all_symlinks = [Path(line) for line in result.stdout.splitlines() if line.strip()]
    filtered = [
        s for s in all_symlinks
        if not any(part in EXCLUDE_DIRS for part in s.parts)
    ]
    dangling = [s for s in filtered if not s.resolve().exists()]
    assert not dangling, f"Dangling symlinks found:\n" + "\n".join(str(d) for d in dangling)
```

- [ ] **Step 2: Run the test on current state**

```bash
pytest scripts/tests/test_no_dangling_symlinks.py -v
```

If it fails (dangling symlinks already exist), document each in the test output. They will be cleaned up in Phase 2. For now, this is informational. If it passes, great.

- [ ] **Step 3: Commit (regardless of pass/fail status — failing test is expected to be fixed in Phase 2)**

```bash
git add scripts/tests/test_no_dangling_symlinks.py
git commit -m "test: detect dangling symlinks (will be enforced after Phase 2)"
```

---

### Task 0.8: Set up Tier 2 smoke test infrastructure and capture baseline

**Files:**
- Create: `scripts/tests/test_agents_smoke.py`
- Create: `tests/snapshots/baseline/.gitkeep`
- Create: `tests/snapshots/baseline/<agent>.txt` (for 5-6 agents)

- [ ] **Step 1: Verify `claude -p` works from this directory**

```bash
cd "/Users/rilner/Marketing OS"
claude -p "Diga 'OK' e nada mais." 2>&1 | tail -5
```

Expected: claude responds with "OK" or similar short answer. If it errors out (auth issue, etc), pause and resolve before continuing.

- [ ] **Step 2: List native agents available**

```bash
ls .claude/agents/ | sed 's/\.md$//'
```

Expected: list of agent names (mos-ab-testing, mos-ads, mos-ai-tools, etc).

- [ ] **Step 3: Write the smoke test file**

```python
"""Tier 2 smoke tests: invoke marketing-os agents via `claude -p` (uses subscription)."""
from __future__ import annotations

import os
import shutil
import subprocess
from pathlib import Path

import pytest

pytestmark = pytest.mark.smoke


CLAUDE_BIN = shutil.which("claude")
TIMEOUT_SECONDS = 180


REPRESENTATIVE_AGENTS = [
    ("mos-copy", "Use o agente mos-copy para escrever uma headline curta para um produto fictício de cursos online de marketing.", ["headline"]),
    ("mos-seo", "Use o agente mos-seo para sugerir 5 keywords e uma meta description para um artigo sobre 'funil de vendas para infoprodutos'.", ["keyword", "meta"]),
    ("mos-social", "Use o agente mos-social para escrever um post curto de Instagram (com hashtags) sobre o tema 'produtividade para criadores de conteúdo'.", ["#"]),
    ("mos-email", "Use o agente mos-email para escrever um email curto com subject, corpo e CTA sobre o lançamento de um workshop online.", ["subject", "cta"]),
    ("mos-ads", "Use o agente mos-ads para escrever copy de um anúncio do Facebook (headline + texto principal) para um curso de copywriting.", ["headline", "ad"]),
]


@pytest.fixture(scope="module")
def baseline_dir(project_root: Path) -> Path:
    d = project_root / "tests" / "snapshots" / "baseline"
    d.mkdir(parents=True, exist_ok=True)
    return d


@pytest.mark.skipif(CLAUDE_BIN is None, reason="claude CLI not in PATH")
@pytest.mark.parametrize("agent_name,prompt,expected_markers", REPRESENTATIVE_AGENTS, ids=[a[0] for a in REPRESENTATIVE_AGENTS])
def test_agent_responds_structurally(
    agent_name: str,
    prompt: str,
    expected_markers: list[str],
    project_root: Path,
    baseline_dir: Path,
) -> None:
    """Invokes agent via claude -p, validates response is non-empty and has expected markers."""
    result = subprocess.run(
        [CLAUDE_BIN, "-p", prompt],
        capture_output=True,
        text=True,
        cwd=str(project_root),
        timeout=TIMEOUT_SECONDS,
    )
    output = result.stdout.strip()
    assert result.returncode == 0, (
        f"{agent_name} invocation failed (exit {result.returncode}):\n"
        f"STDERR:\n{result.stderr[:500]}"
    )
    assert len(output) > 200, f"{agent_name} output too short ({len(output)} chars):\n{output[:500]}"
    output_lower = output.lower()
    missing = [m for m in expected_markers if m.lower() not in output_lower]
    assert not missing, f"{agent_name} output missing expected markers {missing}"

    # Save to baseline if env var set
    if os.environ.get("MARKETING_OS_SAVE_BASELINE") == "1":
        baseline_path = baseline_dir / f"{agent_name}.txt"
        baseline_path.write_text(output, encoding="utf-8")
```

Save as `scripts/tests/test_agents_smoke.py`.

- [ ] **Step 4: Capture baseline outputs**

```bash
mkdir -p tests/snapshots/baseline
touch tests/snapshots/baseline/.gitkeep
MARKETING_OS_SAVE_BASELINE=1 pytest scripts/tests/test_agents_smoke.py -v -m smoke
```

Expected: 5 tests run, each takes 30-90s. All should pass and save outputs to `tests/snapshots/baseline/<agent>.txt`. If 1-2 tests fail with "output missing expected markers", inspect the saved output and either:
- Adjust expected markers in the test (if marker too specific), OR
- Note that this agent's output structure differs (might be a real issue)

- [ ] **Step 5: Verify baseline files saved**

```bash
ls -la tests/snapshots/baseline/
```

Expected: 6 files (.gitkeep + 5 agent baseline .txt files).

- [ ] **Step 6: Commit**

```bash
git add scripts/tests/test_agents_smoke.py tests/snapshots/baseline/
git commit -m "test: add Tier 2 smoke tests via claude -p with baseline snapshots"
```

---

### Task 0.9: Phase 0 verification

**Files:** None (verification only)

- [ ] **Step 1: Run all Tier 1 tests**

```bash
pytest scripts/tests/ -v -m "not smoke" 2>&1 | tail -30
```

Expected: all non-smoke tests pass (or document any pre-existing failures).

- [ ] **Step 2: Verify branch state**

```bash
git log --oneline refactor/plugin-first ^main 2>&1 | head -10
git status --short
```

Expected: ~6-8 commits visible, clean working tree.

- [ ] **Step 3: Confirm baseline artifacts exist**

```bash
ls /tmp/marketing-os-baseline/
ls tests/snapshots/baseline/
```

Expected: baseline tree, du, sha files present; agent outputs saved.

**Phase 0 complete:** safety net + scaffolding in place. Ready to mutate the repo.

---

## Phase 1 — Extract Personal Workspace

### Task 1.1: Write workspace separation test (TDD: fails first)

**Files:**
- Create: `scripts/tests/test_workspace_separation.py`

- [ ] **Step 1: Write the failing test**

```python
"""Validates that plugin code does not reference workspace/ paths."""
from __future__ import annotations

from pathlib import Path

import pytest


# Paths that ship as part of the plugin (must NOT reference workspace/)
PLUGIN_DIRS = ["skills", "subagents", "commands", "workflows", "assets", "references", ".claude/agents"]

# Search patterns that would indicate a leak from plugin → workspace
LEAK_PATTERNS = ["workspace/", "../workspace", "/workspace/"]


def test_workspace_dir_exists_after_phase_1(project_root: Path) -> None:
    """workspace/ should exist after Phase 1 migration."""
    pytest.importorskip("pathlib")
    workspace = project_root / "workspace"
    assert workspace.is_dir(), (
        "workspace/ does not exist yet — expected to be created in Phase 1.\n"
        "If Phase 1 completed, this is a regression."
    )


def test_no_plugin_file_references_workspace(project_root: Path) -> None:
    """No file inside plugin dirs should mention workspace/ paths."""
    leaks: list[str] = []
    for plugin_dir in PLUGIN_DIRS:
        d = project_root / plugin_dir
        if not d.exists():
            continue
        for path in d.rglob("*"):
            if not path.is_file():
                continue
            if path.suffix not in {".md", ".yaml", ".yml", ".json", ".py"}:
                continue
            try:
                content = path.read_text(encoding="utf-8")
            except (UnicodeDecodeError, IsADirectoryError):
                continue
            for pattern in LEAK_PATTERNS:
                if pattern in content:
                    leaks.append(f"{path.relative_to(project_root)}: contains '{pattern}'")
    assert not leaks, "Plugin files reference workspace paths:\n" + "\n".join(leaks)
```

- [ ] **Step 2: Run the test (expect failure on first test, pass on second)**

```bash
pytest scripts/tests/test_workspace_separation.py -v
```

Expected: `test_workspace_dir_exists_after_phase_1` FAILS (workspace/ doesn't exist yet). `test_no_plugin_file_references_workspace` likely PASSES (no leaks before workspace exists).

- [ ] **Step 3: Commit (test in failing state is OK — Phase 1 will fix it)**

```bash
git add scripts/tests/test_workspace_separation.py
git commit -m "test: add workspace separation test (currently failing, fixed by Phase 1)"
```

---

### Task 1.2: Create workspace structure

**Files:**
- Create: `workspace/{,drafts/,brand/,outputs/,research/,landing-pages/,media/}/.gitkeep`

- [ ] **Step 1: Create directories with .gitkeep markers**

```bash
mkdir -p workspace/{drafts,brand,outputs,research,landing-pages,media}
touch workspace/.gitkeep
for d in drafts brand outputs research landing-pages media; do
    touch workspace/$d/.gitkeep
done
ls -la workspace/
```

Expected: 7 directories created (workspace + 6 subdirs), each with `.gitkeep`.

- [ ] **Step 2: Verify (workspace dir test now passes, but git not yet aware)**

```bash
pytest scripts/tests/test_workspace_separation.py::test_workspace_dir_exists_after_phase_1 -v
```

Expected: PASS.

- [ ] **Step 3: Stage but do not commit yet (wait until moves done)**

```bash
git add workspace/.gitkeep workspace/*/.gitkeep
```

---

### Task 1.3: Move personal artifacts into workspace

**Files:** Multiple `git mv` operations

- [ ] **Step 1: Identify files to move (verify with git status)**

```bash
git status --short
ls -la *.md *.svg *.png 2>/dev/null
ls -la outputs/ output/ research/ landing-pages/ media/ 2>/dev/null
```

Note: untracked files (carrossel-instagram-*.md, vertice-logo.svg, etc) need `mv`, not `git mv`. Tracked files (e.g., outputs/, research/) need `git mv`.

- [ ] **Step 2: Move drafts (root MDs)**

```bash
# Untracked — use plain mv
mv carrossel-instagram-5-verdades-escalar-negocio.md workspace/drafts/ 2>/dev/null || true
mv Roteiro_Reels_90s_Viral.md workspace/drafts/ 2>/dev/null || true
mv Roteiro_Video_Estilo_ALTERD.md workspace/drafts/ 2>/dev/null || true
ls workspace/drafts/
```

- [ ] **Step 3: Move brand assets**

```bash
mv vertice-logo.svg vertice-symbol.png workspace/brand/ 2>/dev/null || true
ls workspace/brand/
```

- [ ] **Step 4: Move outputs/ and output/ (singular if exists)**

```bash
if [ -d outputs ]; then
    git mv outputs/* workspace/outputs/ 2>/dev/null || mv outputs/* workspace/outputs/
    rmdir outputs
fi
if [ -d output ]; then
    git mv output/* workspace/outputs/ 2>/dev/null || mv output/* workspace/outputs/
    rmdir output
fi
ls workspace/outputs/ | head
```

- [ ] **Step 5: Move research/, landing-pages/, media/**

```bash
for d in research landing-pages media; do
    if [ -d "$d" ]; then
        # Use git mv if tracked, plain mv otherwise
        git mv "$d" "workspace/$d-temp" 2>/dev/null || mv "$d" "workspace/$d-temp"
        # Merge contents (we already created workspace/$d/.gitkeep)
        if [ -d "workspace/$d-temp" ]; then
            cp -r workspace/$d-temp/* workspace/$d/ 2>/dev/null
            rm -rf workspace/$d-temp
        fi
    fi
done
ls workspace/
```

- [ ] **Step 6: Verify root is clean of personal artifacts**

```bash
ls -la *.md *.svg *.png 2>/dev/null
ls -d outputs output research landing-pages media 2>/dev/null
```

Expected: only generic root MDs (README, CHANGELOG, CONTRIBUTING, GUIA-DE-USO, INSTALACAO-SKILL, AGENTS) remain. No svg/png. No outputs/research/landing-pages/media at root.

---

### Task 1.4: Update .gitignore for workspace

**Files:**
- Modify: `.gitignore`

- [ ] **Step 1: Read current .gitignore**

```bash
cat .gitignore
```

- [ ] **Step 2: Update .gitignore**

Use the Edit tool to update `.gitignore` to include:

```gitignore
# Workspace pessoal (não distribuído)
workspace/*
!workspace/.gitkeep
!workspace/*/
!workspace/*/.gitkeep

# Secrets
.env
.env.backup.*
.env.local

# Caches
.playwright-mcp/
.pytest_cache/
node_modules/
__pycache__/
*.pyc
.DS_Store

# Backups de migração
*.pre-migration.backup
*.bak
```

The `!workspace/.gitkeep` and `!workspace/*/.gitkeep` exceptions ensure the empty workspace structure is preserved in git, while content inside is ignored.

- [ ] **Step 3: Verify .gitignore behavior**

```bash
echo "test content" > workspace/drafts/test-ignore-me.md
git status workspace/
rm workspace/drafts/test-ignore-me.md
```

Expected: `git status` does NOT show `workspace/drafts/test-ignore-me.md` (it's ignored). `.gitkeep` files are tracked.

- [ ] **Step 4: Run workspace separation test**

```bash
pytest scripts/tests/test_workspace_separation.py -v
```

Expected: both tests PASS now.

- [ ] **Step 5: Run all Tier 1 tests**

```bash
pytest scripts/tests/ -v -m "not smoke"
```

Expected: all non-smoke tests pass.

- [ ] **Step 6: Commit Phase 1**

```bash
git add -A
git status --short
git commit -m "$(cat <<'EOF'
refactor(phase-1): extract personal content to workspace/

- Create workspace/{drafts,brand,outputs,research,landing-pages,media}/
- Move root drafts (carrossel-*, Roteiro_*) to workspace/drafts/
- Move vertice-logo.svg, vertice-symbol.png to workspace/brand/
- Move outputs/, output/, research/, landing-pages/, media/ to workspace/
- Update .gitignore to ignore workspace/ contents (keep .gitkeep)
- workspace_separation tests now pass
EOF
)"
```

---

## Phase 2 — Consolidate marketing-os

### Task 2.1: Verify Claude Code plugin layout convention

**Files:** None (research only)

- [ ] **Step 1: Quick check on official Claude Code plugins for symlink convention**

```bash
# Check if any installed plugins use symlinks
ls -la ~/.claude/plugins/cache/*/skills/*/  2>/dev/null | head -20
```

Examine output for any `->` (symlink indicator).

- [ ] **Step 2: Decision recorded**

Based on what you find, decide:
- **If most plugins use symlinks like the current Marketing OS** → keep symlinks; only resolve broken ones
- **If most plugins have content directly in `skills/<name>/`** → move root dirs INTO `skills/marketing-os/` (different from current spec — would require updating Section 1 of design)
- **If unclear** → keep symlinks (default per spec)

Record decision inline in commit message of next task.

---

### Task 2.2: Diff and merge SKILL.md files

**Files:**
- Modify: `skills/marketing-os/SKILL.md`
- Delete (later): `skill-package/marketing-os/SKILL.md`

- [ ] **Step 1: Diff both SKILL.md files**

```bash
diff -u skills/marketing-os/SKILL.md skill-package/marketing-os/SKILL.md > /tmp/skill-md-diff.txt
wc -l /tmp/skill-md-diff.txt
head -50 /tmp/skill-md-diff.txt
```

Expected: see the divergences. Lines added in skill-package (`+`) might be content to merge into the canonical.

- [ ] **Step 2: Read both files in full**

```bash
cat skills/marketing-os/SKILL.md
echo "==========SEPARATOR=========="
cat skill-package/marketing-os/SKILL.md
```

- [ ] **Step 3: Decide merge strategy**

Based on the diff: are there sections in skill-package that are valuable and missing in canonical? If yes, edit canonical to include them. If no (skill-package is just stale), proceed to deletion in next task.

Use the Edit tool to update `skills/marketing-os/SKILL.md` if merging is needed.

- [ ] **Step 4: Re-run SKILL.md tests**

```bash
pytest scripts/tests/test_skill_md.py -v
```

Expected: all pass.

- [ ] **Step 5: Stage but don't commit yet (Task 2.3 will batch-commit Phase 2)**

```bash
git add skills/marketing-os/SKILL.md
```

---

### Task 2.3: Delete duplicate marketing-os/, skill-package/, backups

**Files:**
- Delete: `marketing-os/` (root)
- Delete: `skill-package/`
- Delete: `skills/marketing-os/SKILL.md.pre-migration.backup`
- Delete: any `*.pre-migration.backup`

- [ ] **Step 1: Verify these are safe to delete**

```bash
# What's in marketing-os/ (root)?
ls -la marketing-os/
# Confirm symlinks resolve to root dirs we have
ls -la marketing-os/{assets,references,scripts,subagents,workflows} 2>/dev/null

# What's in skill-package/?
ls -la skill-package/marketing-os/
```

- [ ] **Step 2: Find any other backups**

```bash
find . -name "*.pre-migration.backup" -not -path "./.git/*"
find . -name "*.bak" -not -path "./.git/*"
```

- [ ] **Step 3: Delete with git rm where tracked, plain rm where not**

```bash
# Untracked dirs — plain rm
rm -rf marketing-os/
rm -rf skill-package/

# Tracked file — git rm
git rm skills/marketing-os/SKILL.md.pre-migration.backup 2>/dev/null || rm -f skills/marketing-os/SKILL.md.pre-migration.backup

# Any other backups
find . -name "*.pre-migration.backup" -not -path "./.git/*" -delete
```

- [ ] **Step 4: Verify dangling symlinks are gone**

```bash
find . -xtype l 2>&1 | grep -v "^find:" | head
```

Expected: empty (no broken symlinks). If any remain, inspect — they probably pointed to deleted dirs and should be removed:

```bash
find . -xtype l -not -path "./.git/*" -delete
```

- [ ] **Step 5: Run all tests including symlink check**

```bash
pytest scripts/tests/ -v -m "not smoke"
```

Expected: all pass, including `test_no_dangling_symlinks`.

- [ ] **Step 6: Run Tier 2 smoke tests and compare to baseline**

```bash
pytest scripts/tests/test_agents_smoke.py -v -m smoke
```

Expected: all 5 smoke tests pass with structurally similar output to baseline. If any agent fails:
1. Read the diff between baseline and current output
2. Determine if structure changed (could indicate broken plugin loading) or content just naturally varied
3. If structural break: investigate before committing

- [ ] **Step 7: Commit Phase 2**

```bash
git add -A
git status --short
git commit -m "$(cat <<'EOF'
refactor(phase-2): consolidate marketing-os into single canonical location

- Merge unique content from skill-package/marketing-os/SKILL.md into
  skills/marketing-os/SKILL.md (canonical, referenced in plugin.json)
- Delete marketing-os/ (root, symlinked redundant copy)
- Delete skill-package/ (frozen export, stale jan/fev)
- Delete skills/marketing-os/SKILL.md.pre-migration.backup
- Single source of truth: root for shared resources, skills/marketing-os/
  with symlinks for plugin path resolution
- All Tier 1 tests pass
- Tier 2 smoke tests pass (5/5 agents respond structurally consistent
  with baseline)
EOF
)"
```

---

## Phase 3 — Decapitate AIOS

### Task 3.1: Write AIOS-residue test (TDD: fails first)

**Files:**
- Create: `scripts/tests/test_no_aios_residue.py`

- [ ] **Step 1: Write the test**

```python
"""Detects residual references to the AIOS framework after Phase 3."""
from __future__ import annotations

from pathlib import Path

import pytest


# Strings that indicate AIOS residue
AIOS_PATTERNS = [
    "@aios-master",
    "@aios",
    ".aios-core",
    "Synkra AIOS",
    "AIOS-MANAGED",
    "story-driven development",
    "IDS gate",
    "@po ",
    "@sm ",
    "@architect",
    "@devops",
    "QA Loop",
]

# Files/dirs to check (excluding CHANGELOG which legitimately mentions removal)
SEARCH_ROOTS = ["skills", "subagents", "commands", "workflows", "assets", "references", "scripts", "docs", ".claude"]
EXCLUDE_FILES = {
    # Historical/contextual mentions are legitimate
    "CHANGELOG.md",
    "2026-05-06-marketing-os-plugin-first-refactor-design.md",
    "2026-05-06-marketing-os-plugin-first-refactor.md",
    # User-facing docs rewritten in Phase 4 (deleted or fully replaced there)
    "README.md",
    "GUIA-DE-USO.md",
    "INSTALACAO-SKILL.md",
}
EXCLUDE_DIRS = {"snapshots"}  # baseline outputs may legitimately mention agents in their domain


@pytest.mark.aios_removed
def test_no_aios_strings_in_content(project_root: Path) -> None:
    """Fail if AIOS-related strings appear in plugin content (after Phase 3)."""
    leaks: list[str] = []
    for root in SEARCH_ROOTS:
        d = project_root / root
        if not d.exists():
            continue
        for path in d.rglob("*"):
            if not path.is_file():
                continue
            if path.name in EXCLUDE_FILES:
                continue
            if any(part in EXCLUDE_DIRS for part in path.parts):
                continue
            if path.suffix not in {".md", ".yaml", ".yml", ".json", ".py", ".txt"}:
                continue
            try:
                content = path.read_text(encoding="utf-8")
            except UnicodeDecodeError:
                continue
            for pattern in AIOS_PATTERNS:
                if pattern in content:
                    leaks.append(f"{path.relative_to(project_root)}: contains '{pattern}'")
                    break
    assert not leaks, "AIOS residue found:\n" + "\n".join(sorted(set(leaks))[:30])


@pytest.mark.aios_removed
def test_no_aios_dirs_remain(project_root: Path) -> None:
    aios_paths = [
        ".aios", ".aios-core", ".antigravity", ".codex", "squads",
        ".aios-installation-config.yaml", ".aios-pm-config.yaml",
    ]
    for p in aios_paths:
        assert not (project_root / p).exists(), f"AIOS path still exists: {p}"
```

- [ ] **Step 2: Run the test (expect failures since AIOS still present)**

```bash
pytest scripts/tests/test_no_aios_residue.py -v -m aios_removed
```

Expected: tests FAIL (AIOS exists). This is correct — the test is designed to pass after Phase 3.

- [ ] **Step 3: Commit failing test**

```bash
git add scripts/tests/test_no_aios_residue.py
git commit -m "test: add AIOS residue detection (fails until Phase 3 completes)"
```

---

### Task 3.2: Delete AIOS directories and config files

**Files:**
- Delete: `.aios/`, `.aios-core/`, `.aios-installation-config.yaml`, `.aios-pm-config.yaml`
- Delete: `.antigravity/`, `.codex/`
- Delete: `squads/`
- Delete: `AGENTS.md` (root)

- [ ] **Step 1: List what's about to be deleted (sanity check)**

```bash
ls -la .aios .aios-core .aios-installation-config.yaml .aios-pm-config.yaml .antigravity .codex squads AGENTS.md 2>&1 | head
du -sh .aios .aios-core .antigravity .codex squads 2>/dev/null
```

- [ ] **Step 2: Delete (use git rm for tracked, rm -rf for untracked)**

```bash
git rm -rf .aios 2>/dev/null || rm -rf .aios
git rm -rf .aios-core 2>/dev/null || rm -rf .aios-core
git rm .aios-installation-config.yaml 2>/dev/null || rm -f .aios-installation-config.yaml
git rm .aios-pm-config.yaml 2>/dev/null || rm -f .aios-pm-config.yaml
git rm -rf .antigravity 2>/dev/null || rm -rf .antigravity
git rm -rf .codex 2>/dev/null || rm -rf .codex
git rm -rf squads 2>/dev/null || rm -rf squads
git rm AGENTS.md 2>/dev/null || rm -f AGENTS.md
```

- [ ] **Step 3: Verify deletion**

```bash
ls .aios .aios-core .antigravity .codex squads AGENTS.md 2>&1 | head
```

Expected: all "No such file or directory" errors.

- [ ] **Step 4: Stage deletions (don't commit yet — more cleanup in 3.3)**

```bash
git status --short | head -20
```

---

### Task 3.3: Delete AIOS rules from .claude/rules/

**Files:**
- Delete: `.claude/rules/{workflow-execution,story-lifecycle,ids-principles,agent-authority,coderabbit-integration}.md`
- Evaluate: `.claude/rules/mcp-usage.md` (salvage useful bits)

- [ ] **Step 1: List rules**

```bash
ls .claude/rules/
```

- [ ] **Step 2: Read mcp-usage.md to identify salvageable content**

```bash
cat .claude/rules/mcp-usage.md
```

Identify generic-useful bits (e.g., "use Read for files, not docker-gateway"). These will be folded into the new CLAUDE.md.

- [ ] **Step 3: Delete AIOS-specific rules**

```bash
git rm .claude/rules/workflow-execution.md
git rm .claude/rules/story-lifecycle.md
git rm .claude/rules/ids-principles.md
git rm .claude/rules/agent-authority.md
git rm .claude/rules/coderabbit-integration.md
```

- [ ] **Step 4: Decide on mcp-usage.md**

Two options:
1. **Delete entirely** if its rules are too AIOS-specific or obvious
2. **Rename and trim** to `.claude/rules/mcp-conventions.md` keeping only generic, non-AIOS guidance

For option 2:
```bash
git mv .claude/rules/mcp-usage.md .claude/rules/mcp-conventions.md
```

Then use Edit tool to remove AIOS framing (mentions of @devops, @architect, AIOS workflows).

For option 1:
```bash
git rm .claude/rules/mcp-usage.md
```

Pick one and execute. Default: option 1 (delete) — content goes into CLAUDE.md instead.

- [ ] **Step 5: Verify .claude/rules/ is empty or has only mcp-conventions.md**

```bash
ls .claude/rules/
```

---

### Task 3.4: Rewrite .claude/CLAUDE.md (slim)

**Files:**
- Modify: `.claude/CLAUDE.md` (full rewrite)

- [ ] **Step 1: Use Write tool to replace `.claude/CLAUDE.md` with new content**

```markdown
# Marketing OS — Project Conventions

This file orients Claude Code when working inside this repo.

## What this is

Marketing OS is a Claude Code **plugin** (`marketing-os` v5.1.0) providing 18 specialized marketing subagents (Copy, SEO, Social, Video, Audio, Design, AI Tools, Analytics, Email, Ads, Research, Brand, Storytelling, Funnel, Growth, Launch, Infoproduct Builder, AB Testing).

The plugin is loaded by Claude Code via `plugin.json`. The skill entrypoint is `skills/marketing-os/SKILL.md`. Native subagents live in `.claude/agents/` (`mos-*.md`) and reference knowledge bases in `subagents/` (Tier 1 → Tier 2 layering).

## Layout

| Path | Purpose |
|---|---|
| `.claude/agents/` | Native Claude Code subagents (Tier 1 entrypoints) |
| `subagents/` | Knowledge base for agents (Tier 2 deep refs) |
| `commands/` | Slash commands |
| `workflows/` | Multi-step content workflows |
| `assets/` | Frameworks, personas, prompts, swipe files, templates |
| `references/` | Topic reference guides (ads, blog, email, social, etc) |
| `scripts/` | Tooling (validation, tests) |
| `docs/` | Plugin documentation |
| `workspace/` | **Personal/local content (gitignored). Never reference from plugin code.** |

## Working in this repo

- Plugin code is in versioned dirs above. **Never** reference `workspace/` from plugin files.
- For test runs: `pytest scripts/tests/ -v -m "not smoke"` (Tier 1, fast, free).
- For smoke tests: `pytest scripts/tests/ -v -m smoke` (Tier 2, ~60s, uses Claude Code subscription).
- For native agents validation: `python scripts/validate_agents.py`.

## Conventions

- Português é a língua padrão de descrições e prompts dos agentes.
- Frontmatter de native agents (`.claude/agents/*.md`) deve ter `name`, `description`, `tools`, `model`. Nome do arquivo = `name`.
- Subagents knowledge base (`subagents/*.md`) é referenciado por native agents via crase: `` `subagents/X.md` ``.
- Não fazer `git push`, `gh pr create`, ou ações que afetem repositório remoto sem confirmação explícita do autor.
- Não commitar `.env` ou conteúdo de `workspace/`.

## Tooling guidelines

- Use `Read`, `Edit`, `Write` para arquivos; `Bash` só pra operações shell.
- Use `Grep`/`Glob` para busca; evite `grep`/`find` no Bash quando ferramentas nativas servem.
- MCP `playwright` apenas para automação real de browser; nunca para ler/escrever arquivos locais.
```

Save as `.claude/CLAUDE.md`.

- [ ] **Step 2: Verify file**

```bash
wc -l .claude/CLAUDE.md
head -20 .claude/CLAUDE.md
```

Expected: ~40-60 lines.

- [ ] **Step 3: Stage**

```bash
git add .claude/CLAUDE.md
```

---

### Task 3.5: Run all tests including AIOS-residue

**Files:** None

- [ ] **Step 1: Run all Tier 1 tests including aios_removed marker**

```bash
pytest scripts/tests/ -v -m "not smoke"
```

Expected: all tests pass, including previously-failing `test_no_aios_residue.py`.

If `test_no_aios_strings_in_content` fails on files NOT in `EXCLUDE_FILES`: read the leaks list, identify the file(s), remove the AIOS strings via Edit tool, re-run.

Note: `README.md`, `GUIA-DE-USO.md`, `INSTALACAO-SKILL.md` are excluded by design — they get rewritten/deleted in Phase 4. The test correctly skips them here and Phase 4 cleanup ensures the final state has zero residue.

- [ ] **Step 2: Run smoke tests**

```bash
pytest scripts/tests/test_agents_smoke.py -v -m smoke
```

Expected: all 5 pass with structure consistent to baseline. If they fail with "agent not found" or "skill failed to load", the AIOS removal broke the plugin somehow — investigate immediately.

- [ ] **Step 3: Commit Phase 3**

```bash
git add -A
git status --short
git commit -m "$(cat <<'EOF'
refactor(phase-3): remove dormant Synkra AIOS framework

Deleted:
- .aios/, .aios-core/ (framework runtime + meta-config)
- .aios-installation-config.yaml, .aios-pm-config.yaml
- .antigravity/, .codex/ (unused IDE/CLI configs)
- squads/ (AIOS squad concept, redundant)
- AGENTS.md (AIOS-framed instructions for Codex CLI)
- .claude/rules/{workflow-execution,story-lifecycle,ids-principles,
  agent-authority,coderabbit-integration,mcp-usage}.md

Replaced:
- .claude/CLAUDE.md → slim ~50-line version focused on marketing-os
  plugin (no AIOS, no story-driven dev, no agent authority matrix)

All Tier 1 tests pass (test_no_aios_residue now green).
Tier 2 smoke tests still pass (plugin functional after AIOS removal).
EOF
)"
```

---

## Phase 4 — Polish

### Task 4.1: Decide package.json/node_modules fate

**Files:**
- Modify or delete: `package.json`, `node_modules/`

- [ ] **Step 1: Check if `ajv` (the only Node dep) is actually used**

```bash
grep -r "ajv\|json-schema" scripts/ subagents/ workflows/ commands/ --include="*.py" --include="*.js" --include="*.ts" --include="*.json" 2>/dev/null | grep -v "node_modules"
```

- [ ] **Step 2: Decision**

- **If ajv is used:** sync versions and keep
  ```bash
  # Update package.json version 5.0.0 → 5.1.0
  ```
  Use Edit tool to change `"version": "5.0.0"` to `"version": "5.1.0"` in `package.json`.

- **If ajv is NOT used:** delete Node toolchain
  ```bash
  git rm package.json
  rm -rf node_modules/ package-lock.json
  ```

- [ ] **Step 3: Stage changes**

```bash
git add -A
git status --short | head
```

---

### Task 4.2: Decide GUIA-DE-USO.md and INSTALACAO-SKILL.md fate

**Files:**
- Delete or move: `GUIA-DE-USO.md`, `INSTALACAO-SKILL.md`

- [ ] **Step 1: Read both files, compare with what new README.md will cover**

```bash
wc -l GUIA-DE-USO.md INSTALACAO-SKILL.md
head -30 GUIA-DE-USO.md
head -30 INSTALACAO-SKILL.md
```

- [ ] **Step 2: Decision**

If their content will be fully captured in the new README.md (next task):
```bash
git rm GUIA-DE-USO.md INSTALACAO-SKILL.md
```

If they have unique content worth preserving:
```bash
mkdir -p docs/guides
git mv GUIA-DE-USO.md docs/guides/uso.md
git mv INSTALACAO-SKILL.md docs/guides/instalacao.md
```

(Inside, also remove any AIOS references using Edit tool.)

- [ ] **Step 3: Stage**

```bash
git status --short | head
```

---

### Task 4.3: Rewrite README.md

**Files:**
- Modify: `README.md` (full rewrite)

- [ ] **Step 1: Use Write tool to replace README.md with focused content**

```markdown
# Marketing OS

> Plugin Claude Code com **18 subagentes especializados** em marketing digital.

[![Version](https://img.shields.io/badge/version-5.1.0-blue.svg)](./CHANGELOG.md)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](./LICENSE)

## O que é

Marketing OS é um plugin para o [Claude Code](https://www.anthropic.com/claude-code) que habilita 18 subagentes nativos especializados em domínios distintos do marketing digital — copy, SEO, social, vídeo, áudio, design, ads, analytics, email, brand, storytelling, funnel, growth, launch, AI tools, infoproduct builder, AB testing e research.

Cada agente tem acesso a uma knowledge base própria (`subagents/*.md`), uma biblioteca de assets (frameworks, personas, prompts, swipe files, templates) e referências técnicas curadas (`references/`).

## Instalação

### Como plugin do Claude Code

```bash
# Clone o repositório
git clone https://github.com/rilnermucio/Agents.git "Marketing OS"
cd "Marketing OS"

# Instale as deps Python (apenas pra rodar testes/validações)
pip install -r requirements.txt

# Configure o plugin no Claude Code (via plugin.json deste repo)
# Detalhes: https://docs.anthropic.com/claude-code/plugins
```

### Workspace pessoal

Crie sua área pessoal de conteúdo (gitignored, não distribuída):

```bash
mkdir -p workspace/{drafts,outputs,brand,research,landing-pages,media}
```

## Os 18 agentes

Invoque qualquer um via `@<agente>` no Claude Code:

| Agente | Domínio |
|---|---|
| `@mos-copy` | Copywriting persuasivo (headlines, body copy, CTAs) |
| `@mos-seo` | Otimização de busca (keywords, meta, on-page, conteúdo) |
| `@mos-social` | Conteúdo para redes sociais (posts, reels, threads) |
| `@mos-video` | Roteiros e produção audiovisual (YouTube, Reels, TikTok) |
| `@mos-audio` | Podcasts, audiobooks, sound design |
| `@mos-design` | Direção visual, mockups, design specs |
| `@mos-ai-tools` | Avaliação e uso de ferramentas de IA generativa |
| `@mos-analytics` | Métricas, dashboards, KPIs, atribuição |
| `@mos-email` | Email marketing (welcome series, broadcasts, automação) |
| `@mos-ads` | Anúncios pagos (Meta, Google, LinkedIn, TikTok) |
| `@mos-research` | Pesquisa de mercado, audiência, concorrência |
| `@mos-brand` | Identidade de marca, posicionamento, voz |
| `@mos-storytelling` | Narrativa, hero's journey, frameworks de história |
| `@mos-funnel` | Funis de conversão, jornada do cliente |
| `@mos-growth` | Growth hacking, experimentação, retention |
| `@mos-launch` | Lançamentos (PLF, escassez, urgência) |
| `@mos-infoproduct-builder` | Estrutura e curadoria de infoprodutos |
| `@mos-ab-testing` | A/B testing, multivariate, análise estatística |

## Estrutura

```
Marketing OS/
├── plugin.json              # Manifesto do plugin
├── .claude-plugin/          # Config Claude Code
├── skills/marketing-os/     # Skill entrypoint (SKILL.md)
├── .claude/agents/          # Native subagents (mos-*.md, Tier 1)
├── subagents/               # Knowledge base (Tier 2)
├── commands/                # Slash commands
├── workflows/               # Workflows multi-step
├── assets/                  # Frameworks, personas, prompts, etc
├── references/              # Guias técnicos por domínio
├── scripts/                 # Validation, tests
├── docs/                    # Documentação
├── .claude/                 # CLAUDE.md, regras opcionais
└── workspace/               # Conteúdo pessoal (gitignored)
```

## Desenvolvimento

```bash
# Validar native agents
python scripts/validate_agents.py

# Tier 1 (estático, rápido)
pytest scripts/tests/ -v -m "not smoke"

# Tier 2 (smoke via claude -p, requer Claude Code logado)
pytest scripts/tests/ -v -m smoke
```

## Licença

MIT — ver [LICENSE](./LICENSE).
```

- [ ] **Step 2: Verify size and content**

```bash
wc -l README.md
head -30 README.md
```

Expected: ~100-150 lines, focused on plugin.

- [ ] **Step 3: Stage**

```bash
git add README.md
```

---

### Task 4.4: Clean orphan files

**Files:**
- Delete: `.DS_Store` (all), `.env.backup.*`, any other orphans

- [ ] **Step 1: Find orphans**

```bash
find . -name ".DS_Store" -not -path "./.git/*"
ls .env.backup.* 2>/dev/null
```

- [ ] **Step 2: Delete**

```bash
find . -name ".DS_Store" -not -path "./.git/*" -delete
rm -f .env.backup.*
```

- [ ] **Step 3: Stage**

```bash
git status --short | head
```

---

### Task 4.5: Update CHANGELOG.md and finalize

**Files:**
- Modify: `CHANGELOG.md`

- [ ] **Step 1: Read current CHANGELOG**

```bash
cat CHANGELOG.md | head -30
```

- [ ] **Step 2: Add v6.0.0 entry**

Use Edit tool to prepend a new entry at the top of CHANGELOG.md:

```markdown
## [6.0.0] — 2026-05-06

### Breaking changes — Plugin-first refactor

- **Removed Synkra AIOS framework** (`.aios/`, `.aios-core/`, AIOS rules in `.claude/rules/`, AGENTS.md, squads/, .codex/, .antigravity/). The framework was dormant; marketing-os agents are the canonical workflow.
- **Consolidated marketing-os duplication**: removed `marketing-os/` (root, symlinked) and `skill-package/` (frozen export). Single canonical location: `skills/marketing-os/` with symlinks to root resources.
- **Extracted personal workspace** to `workspace/` (gitignored). Root-level drafts (`carrossel-*`, `Roteiro_*`), brand assets (`vertice-*`), research, landing-pages, and media moved into workspace/.
- **Rewrote `.claude/CLAUDE.md`** (~50 lines, focused on marketing-os).
- **Rewrote `README.md`** (~100 lines, focused on plugin usage).

### Added

- pytest test suite in `scripts/tests/`:
  - Tier 1 (static, fast): plugin manifest, SKILL.md, subagents, native agents (wraps validate_agents.py), workspace separation, dangling refs, dangling symlinks, AIOS residue.
  - Tier 2 (smoke via `claude -p`): structural validation of 5 representative agents.
- Baseline snapshots in `tests/snapshots/baseline/`.
- `.claude/rules/mcp-conventions.md` (or merged into CLAUDE.md): salvaged tool-usage guidance from former AIOS rules.

### Migration notes

If you maintained personal forks: your content in `outputs/`, `research/`, `landing-pages/`, `media/`, and root-level drafts now lives in `workspace/<dir>/`. The plugin code does not reference workspace paths.

```

- [ ] **Step 3: Stage**

```bash
git add CHANGELOG.md
```

---

### Task 4.6: Verify size reduction and commit Phase 4

**Files:** None (verification + commit)

- [ ] **Step 1: Capture post-refactor metrics**

```bash
tree -L 1 -a -I '.git|node_modules|.pytest_cache|__pycache__' . > /tmp/marketing-os-baseline/after-tree.txt
du -sh */ .[^.]*/ 2>/dev/null | sort -hr > /tmp/marketing-os-baseline/after-du.txt
diff /tmp/marketing-os-baseline/before-du.txt /tmp/marketing-os-baseline/after-du.txt | head -40
```

- [ ] **Step 2: Confirm criteria from spec**

```bash
# tree -L 1 fits in ~20 lines?
wc -l /tmp/marketing-os-baseline/after-tree.txt
cat /tmp/marketing-os-baseline/after-tree.txt

# Size reduction at least 30%?
echo "Before:" && du -sh . 2>/dev/null
echo "After:" && du -sh . 2>/dev/null
# Compute manually: (before - after) / before >= 0.3
```

- [ ] **Step 3: Run all Tier 1 tests**

```bash
pytest scripts/tests/ -v -m "not smoke"
```

Expected: all pass.

- [ ] **Step 4: Commit Phase 4**

```bash
git add -A
git status --short
git commit -m "$(cat <<'EOF'
refactor(phase-4): polish plugin metadata, docs, and workspace cleanup

- Decide package.json/node_modules fate (keep w/ version sync OR delete)
- Decide GUIA-DE-USO.md / INSTALACAO-SKILL.md (delete OR move to docs/)
- Rewrite README.md (~100 lines, plugin-focused)
- Clean orphans (.DS_Store, .env.backup.*)
- Update CHANGELOG.md with v6.0.0 entry documenting refactor

All Tier 1 tests pass.
EOF
)"
```

---

## Phase 5 — Final Verification

### Task 5.1: Run full Tier 1 + Tier 2 suite

**Files:** None

- [ ] **Step 1: Run all Tier 1**

```bash
pytest scripts/tests/ -v -m "not smoke"
```

Expected: 100% pass.

- [ ] **Step 2: Run all Tier 2 smoke and compare to baseline**

```bash
pytest scripts/tests/test_agents_smoke.py -v -m smoke
```

Expected: 5/5 agents respond with structurally similar output to baseline.

- [ ] **Step 3: Run validate_agents.py independently as final sanity check**

```bash
python scripts/validate_agents.py
```

Expected: exit code 0, no errors.

- [ ] **Step 4: Verify no AIOS residue**

```bash
grep -rli "aios" --include="*.md" . 2>/dev/null | grep -v CHANGELOG.md | grep -v "docs/superpowers" | grep -v ".git"
```

Expected: empty output (CHANGELOG and the spec/plan in `docs/superpowers/` legitimately mention AIOS in historical/contextual context).

---

### Task 5.2: Manual functional verification in Claude Code

**Files:** None (manual)

- [ ] **Step 1: Reload the plugin in Claude Code**

In a NEW Claude Code session at this project directory, the plugin should auto-load (per `plugin.json`).

- [ ] **Step 2: Manually invoke 2-3 agents with different domains**

Try in interactive Claude Code session:
- `@mos-copy escreva uma headline para um curso de Python`
- `@mos-seo sugira keywords para o nicho de "marketing para psicólogos"`
- `@mos-social escreva 3 posts curtos para LinkedIn sobre produtividade`

Expected: each responds with relevant, structured output.

- [ ] **Step 3: Document any anomalies**

If an agent fails or behaves oddly, note it in CHANGELOG.md as a known issue. Do NOT block the merge for minor regressions — the structural refactor goal is met.

---

### Task 5.3: Final commit and merge decision

**Files:** Optional `CHANGELOG.md` update

- [ ] **Step 1: Update CHANGELOG.md if any anomalies found**

Use Edit tool to add a "Known issues" section under v6.0.0 if needed.

- [ ] **Step 2: Squash or rebase decision**

```bash
git log --oneline refactor/plugin-first ^main
```

Decide:
- **Keep individual commits** (preserves phase boundaries) — leave as is
- **Squash to single commit** — `git rebase -i main` then squash all into one
- **Rebase clean** — `git rebase main` (linear history)

Default: keep individual commits (preserves traceability).

- [ ] **Step 3: Merge into main**

```bash
git checkout main
git merge --no-ff refactor/plugin-first -m "Merge plugin-first refactor (v6.0.0)"
git log --oneline | head -10
```

- [ ] **Step 4: Update version in `plugin.json`**

Use Edit tool to update `plugin.json` version `"5.1.0"` → `"6.0.0"`.

```bash
git add plugin.json
git commit -m "chore: bump version to 6.0.0"
```

- [ ] **Step 5: Final verification on main**

```bash
pytest scripts/tests/ -v -m "not smoke"
git log --oneline | head -10
git status
```

Expected: all green, clean tree, history clear.

**Refactor complete.**

---

## Self-Review Checklist (run before handoff)

After writing the plan, verify:

- [ ] Spec coverage: every spec section maps to at least one task — ✅ (Section 1 → architecture targets in tasks; Section 2 → Phases 0-5; Section 3 → Tasks 1.1-1.4; Section 4 → Tasks 3.2-3.3, 4.1-4.4; Section 5 → tasks throughout + 5.1)
- [ ] Placeholder scan: no "TBD/TODO/implement later" remaining
- [ ] Type/path consistency: file paths match across tasks
- [ ] Test names match across creation and execution

If you find issues, fix inline.

---

## Risks and mitigations recap

| Risk | Mitigation in plan |
|---|---|
| `claude -p` doesn't trigger agent properly | Phase 0 Task 0.8 Step 1 verifies `claude -p` works before depending on it; baseline saved before any mutation |
| Symlinks convention unclear | Phase 2 Task 2.1 verifies before deletion |
| AIOS removal breaks plugin | Phase 3 ends with Tier 2 smoke test against baseline |
| `package.json` deps actually used | Phase 4 Task 4.1 greps before deciding |
| Test markers inconsistent across files | Phase 0 Task 0.2 registers all markers in pytest.ini upfront |

---

## Execution choice

After this plan is reviewed:

1. **Subagent-Driven (recommended)** — dispatch fresh subagent per task, review between tasks, fast iteration
2. **Inline Execution** — execute tasks in this session using superpowers:executing-plans, batch execution with checkpoints
