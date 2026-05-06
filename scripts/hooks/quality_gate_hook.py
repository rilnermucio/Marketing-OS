#!/usr/bin/env python3
"""
Marketing OS — PreToolUse Quality Gate Hook

Bloqueia escritas (Write/Edit/MultiEdit) que violem regras universais de qualidade.
Ativado via frontmatter `hooks:` em cada `.claude/agents/mos-*.md`.

Regras universais (aplicam a todo conteúdo de output):
- Em-dash `—` proibido (use `.` `,` `:` ou quebre a frase)
- Palavra "brutal" proibida (use: intenso, forte, pesado, impactante, poderoso)

Paths ignorados: arquivos de tooling, config, docs internas, knowledge bases didáticas.

Protocolo Claude Code hooks:
- Stdin: JSON com tool_name, tool_input
- Exit 0: permitir
- Exit 2: bloquear (com mensagem em stderr explicando ao agent como corrigir)
- Outros exits: tratados como erro mas não bloqueiam

Defensivo: qualquer exceção interna → exit 0 (não quebrar workflow do agent).
"""
import json
import re
import sys

SKIP_PATH_PATTERNS = [
    r'\.claude/',
    r'subagents/.*\.md$',
    r'scripts/',
    r'docs/',
    r'\.github/',
    r'CHANGELOG\.md$',
    r'README\.md$',
    r'CLAUDE\.md$',
    r'CONTRIBUTING\.md$',
    r'LICENSE$',
    r'\.json$',
    r'\.ya?ml$',
    r'\.py$',
    r'\.sh$',
    r'\.txt$',
    r'\.gitignore$',
    r'commands/.*\.md$',
    r'workflows/.*\.md$',
    r'references/.*\.md$',
    r'tests/',
]

PROHIBITED_PATTERNS = [
    (r'—', "Em-dash '—' proibido. Use '.', ',' ou ':' em vez disso, ou quebre a frase."),
    (r'(?<!\w)brutal(?!\w)', "Palavra 'brutal' proibida. Use: intenso, forte, pesado, impactante, poderoso."),
]


def should_skip(file_path: str) -> bool:
    if not file_path:
        return True
    for pat in SKIP_PATH_PATTERNS:
        if re.search(pat, file_path):
            return True
    return False


def extract_content(tool_name: str, tool_input: dict) -> str:
    if tool_name == 'Write':
        return tool_input.get('content', '') or ''
    if tool_name == 'Edit':
        return tool_input.get('new_string', '') or ''
    if tool_name == 'MultiEdit':
        edits = tool_input.get('edits') or []
        return ' '.join((e.get('new_string') or '') for e in edits)
    return ''


def find_violations(content: str) -> list[str]:
    violations = []
    for pat, msg in PROHIBITED_PATTERNS:
        if re.search(pat, content, flags=re.IGNORECASE if 'brutal' in pat else 0):
            violations.append(msg)
    return violations


def main() -> int:
    try:
        data = json.load(sys.stdin)
    except Exception:
        return 0

    tool_name = data.get('tool_name', '')
    tool_input = data.get('tool_input', {}) or {}
    file_path = tool_input.get('file_path', '') or ''

    if tool_name not in ('Write', 'Edit', 'MultiEdit'):
        return 0

    if should_skip(file_path):
        return 0

    content = extract_content(tool_name, tool_input)
    if not content:
        return 0

    violations = find_violations(content)
    if not violations:
        return 0

    print(f"Quality Gate (Marketing OS) bloqueou escrita em {file_path}:", file=sys.stderr)
    for v in violations:
        print(f"  - {v}", file=sys.stderr)
    print("Reescreva o conteudo eliminando as violacoes e tente novamente.", file=sys.stderr)
    return 2


if __name__ == '__main__':
    try:
        sys.exit(main())
    except Exception:
        sys.exit(0)
