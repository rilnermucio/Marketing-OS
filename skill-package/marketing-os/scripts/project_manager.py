#!/usr/bin/env python3
"""
Project Manager - Gerencia projetos e campanhas de marketing

Uso:
    python project_manager.py create "Nome do Projeto" --type launch
    python project_manager.py list
    python project_manager.py status "nome-do-projeto"
    python project_manager.py add-content "nome-do-projeto" --file conteudo.md
    python project_manager.py complete "nome-do-projeto"
"""

import argparse
import os
import sys
import json
import re
from datetime import datetime
from typing import Dict, List, Optional

# Diretório base de projetos
PROJECTS_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "output", "projects")

# Tipos de projeto válidos
PROJECT_TYPES = {
    "launch": "Lançamento de produto ou campanha",
    "funnel": "Funil de vendas completo",
    "batch": "Produção de conteúdo em lote",
    "campaign": "Campanha de marketing",
    "editorial": "Calendário editorial",
    "sequence": "Sequência multi-canal",
    "infoproduct": "Criação de infoproduto",
    "custom": "Projeto personalizado"
}

# Status possíveis
STATUSES = ["active", "paused", "completed", "archived"]


def slugify(text: str) -> str:
    """Converte texto para slug (URL-safe)."""
    text = text.lower().strip()
    text = re.sub(r'[àáâãä]', 'a', text)
    text = re.sub(r'[èéêë]', 'e', text)
    text = re.sub(r'[ìíîï]', 'i', text)
    text = re.sub(r'[òóôõö]', 'o', text)
    text = re.sub(r'[ùúûü]', 'u', text)
    text = re.sub(r'[ç]', 'c', text)
    text = re.sub(r'[^a-z0-9]+', '-', text)
    text = text.strip('-')
    return text


def ensure_projects_dir():
    """Garante que o diretório de projetos existe."""
    os.makedirs(PROJECTS_DIR, exist_ok=True)


def get_project_path(slug: str) -> str:
    """Retorna o caminho do projeto."""
    return os.path.join(PROJECTS_DIR, slug)


def load_project(slug: str) -> Optional[Dict]:
    """Carrega dados do projeto."""
    project_file = os.path.join(get_project_path(slug), "project.json")
    if not os.path.exists(project_file):
        return None
    with open(project_file, 'r', encoding='utf-8') as f:
        return json.load(f)


def save_project(slug: str, data: Dict):
    """Salva dados do projeto."""
    project_file = os.path.join(get_project_path(slug), "project.json")
    data["updated_at"] = datetime.now().isoformat()
    with open(project_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def create_project(name: str, project_type: str = "custom", description: str = ""):
    """Cria um novo projeto."""
    ensure_projects_dir()

    slug = slugify(name)
    project_path = get_project_path(slug)

    if os.path.exists(project_path):
        print(f"\n❌ Projeto '{slug}' já existe.")
        print(f"   Use: python project_manager.py status \"{slug}\"")
        sys.exit(1)

    if project_type not in PROJECT_TYPES:
        print(f"\n❌ Tipo inválido: '{project_type}'")
        print(f"   Tipos válidos: {', '.join(PROJECT_TYPES.keys())}")
        sys.exit(1)

    # Criar estrutura de diretórios
    os.makedirs(project_path)
    os.makedirs(os.path.join(project_path, "content"))
    os.makedirs(os.path.join(project_path, "analytics"))

    # Criar project.json
    project_data = {
        "name": name,
        "slug": slug,
        "type": project_type,
        "type_description": PROJECT_TYPES[project_type],
        "description": description,
        "status": "active",
        "created_at": datetime.now().isoformat(),
        "updated_at": datetime.now().isoformat(),
        "contents": [],
        "metrics": {},
        "notes": []
    }
    save_project(slug, project_data)

    # Criar brief.md
    brief_content = f"""# {name}

## Tipo
{PROJECT_TYPES[project_type]}

## Descrição
{description if description else "[Adicionar descrição do projeto]"}

## Objetivos
- [ ] [Objetivo 1]
- [ ] [Objetivo 2]
- [ ] [Objetivo 3]

## Audiência-Alvo
[Descrever a audiência]

## Cronograma
- **Início:** {datetime.now().strftime('%Y-%m-%d')}
- **Deadline:** [Definir]

## Canais
- [ ] Instagram
- [ ] LinkedIn
- [ ] Email
- [ ] Blog/SEO
- [ ] Ads
- [ ] YouTube
- [ ] TikTok

## Notas
[Notas adicionais do projeto]
"""
    with open(os.path.join(project_path, "brief.md"), 'w', encoding='utf-8') as f:
        f.write(brief_content)

    print("\n" + "=" * 60)
    print("✅ PROJETO CRIADO COM SUCESSO")
    print("=" * 60)
    print(f"\n📁 Nome: {name}")
    print(f"🏷️  Slug: {slug}")
    print(f"📂 Tipo: {PROJECT_TYPES[project_type]}")
    print(f"📍 Local: {project_path}")
    print(f"\n📄 Arquivos criados:")
    print(f"   • project.json (metadados)")
    print(f"   • brief.md (briefing)")
    print(f"   • content/ (conteúdos gerados)")
    print(f"   • analytics/ (métricas)")
    print(f"\n💡 Próximos passos:")
    print(f"   1. Edite o brief.md com os detalhes do projeto")
    print(f"   2. Use os comandos do Marketing OS para gerar conteúdo")
    print(f"   3. Adicione conteúdo: python project_manager.py add-content \"{slug}\" --file conteudo.md")
    print("=" * 60)


def list_projects():
    """Lista todos os projetos."""
    ensure_projects_dir()

    projects = []
    if os.path.exists(PROJECTS_DIR):
        for item in sorted(os.listdir(PROJECTS_DIR)):
            project_path = os.path.join(PROJECTS_DIR, item)
            if os.path.isdir(project_path):
                data = load_project(item)
                if data:
                    projects.append(data)

    if not projects:
        print("\n📭 Nenhum projeto encontrado.")
        print("   Crie um: python project_manager.py create \"Nome do Projeto\" --type launch")
        return

    print("\n" + "=" * 60)
    print("📋 PROJETOS DO MARKETING OS")
    print("=" * 60)

    # Agrupar por status
    for status in STATUSES:
        status_projects = [p for p in projects if p.get("status") == status]
        if status_projects:
            status_icons = {
                "active": "🟢",
                "paused": "🟡",
                "completed": "✅",
                "archived": "📦"
            }
            print(f"\n{status_icons.get(status, '⬜')} {status.upper()} ({len(status_projects)})")
            print("-" * 40)

            for p in status_projects:
                content_count = len(p.get("contents", []))
                created = p.get("created_at", "")[:10]
                print(f"   📁 {p['name']}")
                print(f"      Slug: {p['slug']} | Tipo: {p['type']} | Conteúdos: {content_count} | Criado: {created}")

    print(f"\n📊 Total: {len(projects)} projeto(s)")
    print("=" * 60)


def show_status(slug: str):
    """Mostra status detalhado de um projeto."""
    data = load_project(slug)

    if not data:
        print(f"\n❌ Projeto '{slug}' não encontrado.")
        return

    status_icons = {
        "active": "🟢 Ativo",
        "paused": "🟡 Pausado",
        "completed": "✅ Concluído",
        "archived": "📦 Arquivado"
    }

    print("\n" + "=" * 60)
    print(f"📁 PROJETO: {data['name']}")
    print("=" * 60)
    print(f"\n🏷️  Slug: {data['slug']}")
    print(f"📂 Tipo: {data.get('type_description', data['type'])}")
    print(f"📊 Status: {status_icons.get(data['status'], data['status'])}")
    print(f"📅 Criado: {data['created_at'][:10]}")
    print(f"🔄 Atualizado: {data['updated_at'][:10]}")

    if data.get('description'):
        print(f"\n📝 Descrição: {data['description']}")

    contents = data.get('contents', [])
    if contents:
        print(f"\n📄 CONTEÚDOS ({len(contents)}):")
        for c in contents:
            print(f"   • {c.get('filename', 'sem nome')} — {c.get('type', 'desconhecido')} ({c.get('added_at', '')[:10]})")
    else:
        print("\n📄 Nenhum conteúdo adicionado ainda.")

    notes = data.get('notes', [])
    if notes:
        print(f"\n📌 NOTAS ({len(notes)}):")
        for n in notes[-5:]:  # Últimas 5
            print(f"   • [{n.get('date', '')[:10]}] {n.get('text', '')}")

    print("\n" + "=" * 60)


def add_content(slug: str, filepath: str, content_type: str = "general"):
    """Adiciona conteúdo ao projeto."""
    data = load_project(slug)
    if not data:
        print(f"\n❌ Projeto '{slug}' não encontrado.")
        return

    if not os.path.exists(filepath):
        print(f"\n❌ Arquivo '{filepath}' não encontrado.")
        return

    # Copiar arquivo para o diretório do projeto
    filename = os.path.basename(filepath)
    dest = os.path.join(get_project_path(slug), "content", filename)

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    with open(dest, 'w', encoding='utf-8') as f:
        f.write(content)

    # Atualizar metadados
    data.setdefault("contents", []).append({
        "filename": filename,
        "type": content_type,
        "source": filepath,
        "added_at": datetime.now().isoformat(),
        "lines": len(content.splitlines()),
        "words": len(content.split())
    })

    save_project(slug, data)

    print(f"\n✅ Conteúdo adicionado ao projeto '{data['name']}'")
    print(f"   📄 Arquivo: {filename}")
    print(f"   📏 {len(content.splitlines())} linhas, {len(content.split())} palavras")
    print(f"   📁 Salvo em: {dest}")


def complete_project(slug: str):
    """Marca projeto como concluído."""
    data = load_project(slug)
    if not data:
        print(f"\n❌ Projeto '{slug}' não encontrado.")
        return

    data["status"] = "completed"
    data["completed_at"] = datetime.now().isoformat()
    save_project(slug, data)

    contents = data.get("contents", [])
    print(f"\n✅ Projeto '{data['name']}' marcado como concluído!")
    print(f"   📄 Total de conteúdos: {len(contents)}")
    print(f"   📅 Concluído em: {datetime.now().strftime('%Y-%m-%d')}")


def add_note(slug: str, text: str):
    """Adiciona nota ao projeto."""
    data = load_project(slug)
    if not data:
        print(f"\n❌ Projeto '{slug}' não encontrado.")
        return

    data.setdefault("notes", []).append({
        "text": text,
        "date": datetime.now().isoformat()
    })
    save_project(slug, data)
    print(f"\n✅ Nota adicionada ao projeto '{data['name']}'")


def main():
    parser = argparse.ArgumentParser(
        description="Gerencia projetos e campanhas do Marketing OS",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Exemplos:
  python project_manager.py create "Lançamento Curso IA" --type launch
  python project_manager.py create "Conteúdo Fevereiro" --type editorial --desc "Calendário editorial de fevereiro 2026"
  python project_manager.py list
  python project_manager.py status "lancamento-curso-ia"
  python project_manager.py add-content "lancamento-curso-ia" --file output/post.md --content-type post
  python project_manager.py note "lancamento-curso-ia" "Ajustar tom para mais urgente"
  python project_manager.py complete "lancamento-curso-ia"
        """
    )

    subparsers = parser.add_subparsers(dest="command", help="Comando a executar")

    # create
    create_parser = subparsers.add_parser("create", help="Criar novo projeto")
    create_parser.add_argument("name", help="Nome do projeto")
    create_parser.add_argument("--type", "-t", default="custom", choices=PROJECT_TYPES.keys(), help="Tipo de projeto")
    create_parser.add_argument("--desc", "-d", default="", help="Descrição do projeto")

    # list
    subparsers.add_parser("list", help="Listar todos os projetos")

    # status
    status_parser = subparsers.add_parser("status", help="Ver status de um projeto")
    status_parser.add_argument("slug", help="Slug do projeto")

    # add-content
    add_parser = subparsers.add_parser("add-content", help="Adicionar conteúdo ao projeto")
    add_parser.add_argument("slug", help="Slug do projeto")
    add_parser.add_argument("--file", "-f", required=True, help="Arquivo de conteúdo")
    add_parser.add_argument("--content-type", "-ct", default="general", help="Tipo do conteúdo")

    # note
    note_parser = subparsers.add_parser("note", help="Adicionar nota ao projeto")
    note_parser.add_argument("slug", help="Slug do projeto")
    note_parser.add_argument("text", help="Texto da nota")

    # complete
    complete_parser = subparsers.add_parser("complete", help="Marcar projeto como concluído")
    complete_parser.add_argument("slug", help="Slug do projeto")

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        sys.exit(1)

    if args.command == "create":
        create_project(args.name, args.type, args.desc)
    elif args.command == "list":
        list_projects()
    elif args.command == "status":
        show_status(args.slug)
    elif args.command == "add-content":
        add_content(args.slug, args.file, args.content_type)
    elif args.command == "note":
        add_note(args.slug, args.text)
    elif args.command == "complete":
        complete_project(args.slug)


if __name__ == "__main__":
    main()
