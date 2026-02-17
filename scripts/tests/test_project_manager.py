"""Testes para project_manager.py — gerenciamento de projetos."""

import pytest
import os
import sys
import json
import shutil
import tempfile
from unittest.mock import patch

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from project_manager import (
    slugify,
    create_project,
    list_projects,
    show_status,
    add_content,
    complete_project,
    add_note,
    load_project,
    save_project,
    ensure_projects_dir,
    get_project_path,
    PROJECT_TYPES,
    STATUSES,
    PROJECTS_DIR,
)


@pytest.fixture
def mock_projects_dir(tmp_dir):
    """Redireciona PROJECTS_DIR para diretório temporário."""
    with patch("project_manager.PROJECTS_DIR", tmp_dir):
        yield tmp_dir


@pytest.fixture
def create_test_project(mock_projects_dir):
    """Cria um projeto de teste e retorna o slug."""
    def _create(name="Projeto Teste", project_type="custom", description="Descrição teste"):
        with patch("project_manager.PROJECTS_DIR", mock_projects_dir):
            create_project(name, project_type, description)
            return slugify(name)
    return _create


class TestSlugify:
    """Testes para conversão de texto em slug."""

    def test_basic_slugify(self):
        assert slugify("Projeto Teste") == "projeto-teste"

    def test_accented_chars(self):
        assert slugify("Lançamento Curso IA") == "lancamento-curso-ia"

    def test_special_chars(self):
        assert slugify("Projeto @#$ Especial!") == "projeto-especial"

    def test_multiple_spaces(self):
        assert slugify("  Projeto   Teste  ") == "projeto-teste"

    def test_already_slug(self):
        assert slugify("projeto-teste") == "projeto-teste"

    def test_cedilla(self):
        assert slugify("Promoção") == "promocao"

    def test_all_accents(self):
        result = slugify("àáâãäèéêëìíîïòóôõöùúûüç")
        assert "a" * 5 in result or result.startswith("a")
        assert "c" in result

    def test_numbers_preserved(self):
        assert slugify("Projeto 2026") == "projeto-2026"

    def test_empty_string(self):
        assert slugify("") == ""


class TestProjectTypes:
    """Testes para tipos e status de projeto."""

    def test_all_types_have_descriptions(self):
        for ptype, desc in PROJECT_TYPES.items():
            assert len(desc) > 0
            assert isinstance(desc, str)

    def test_expected_types_exist(self):
        expected = ["launch", "funnel", "batch", "campaign", "editorial", "custom"]
        for t in expected:
            assert t in PROJECT_TYPES

    def test_statuses(self):
        assert "active" in STATUSES
        assert "completed" in STATUSES
        assert "paused" in STATUSES
        assert "archived" in STATUSES


class TestCreateProject:
    """Testes para criação de projetos."""

    def test_create_project_success(self, mock_projects_dir, capsys):
        with patch("project_manager.PROJECTS_DIR", mock_projects_dir):
            create_project("Meu Projeto", "launch", "Descrição do projeto")

        slug = "meu-projeto"
        project_path = os.path.join(mock_projects_dir, slug)
        assert os.path.exists(project_path)
        assert os.path.exists(os.path.join(project_path, "project.json"))
        assert os.path.exists(os.path.join(project_path, "brief.md"))
        assert os.path.isdir(os.path.join(project_path, "content"))
        assert os.path.isdir(os.path.join(project_path, "analytics"))

    def test_create_project_data(self, mock_projects_dir):
        with patch("project_manager.PROJECTS_DIR", mock_projects_dir):
            create_project("Teste Data", "campaign", "Campanha teste")

        slug = "teste-data"
        project_file = os.path.join(mock_projects_dir, slug, "project.json")
        with open(project_file, 'r') as f:
            data = json.load(f)

        assert data["name"] == "Teste Data"
        assert data["slug"] == slug
        assert data["type"] == "campaign"
        assert data["status"] == "active"
        assert "created_at" in data
        assert data["contents"] == []

    def test_create_duplicate_project_exits(self, mock_projects_dir):
        with patch("project_manager.PROJECTS_DIR", mock_projects_dir):
            create_project("Duplicado", "custom")
            with pytest.raises(SystemExit):
                create_project("Duplicado", "custom")

    def test_create_invalid_type_exits(self, mock_projects_dir):
        with patch("project_manager.PROJECTS_DIR", mock_projects_dir):
            with pytest.raises(SystemExit):
                create_project("Projeto", "tipo_invalido")

    def test_brief_contains_project_name(self, mock_projects_dir):
        with patch("project_manager.PROJECTS_DIR", mock_projects_dir):
            create_project("Brief Test", "editorial")

        brief_path = os.path.join(mock_projects_dir, "brief-test", "brief.md")
        with open(brief_path, 'r') as f:
            brief = f.read()

        assert "Brief Test" in brief
        assert "Calendário editorial" in brief


class TestLoadSaveProject:
    """Testes para load/save de projetos."""

    def test_load_nonexistent_project(self, mock_projects_dir):
        with patch("project_manager.PROJECTS_DIR", mock_projects_dir):
            result = load_project("nao-existe")
        assert result is None

    def test_save_and_load(self, mock_projects_dir):
        slug = "test-save"
        project_path = os.path.join(mock_projects_dir, slug)
        os.makedirs(project_path)

        data = {"name": "Test", "slug": slug, "status": "active"}
        with patch("project_manager.PROJECTS_DIR", mock_projects_dir):
            save_project(slug, data)
            loaded = load_project(slug)

        assert loaded["name"] == "Test"
        assert loaded["slug"] == slug
        assert "updated_at" in loaded


class TestListProjects:
    """Testes para listagem de projetos."""

    def test_list_empty(self, mock_projects_dir, capsys):
        with patch("project_manager.PROJECTS_DIR", mock_projects_dir):
            list_projects()

        captured = capsys.readouterr()
        assert "Nenhum projeto" in captured.out

    def test_list_with_projects(self, mock_projects_dir, capsys):
        with patch("project_manager.PROJECTS_DIR", mock_projects_dir):
            create_project("Projeto A", "launch")
            create_project("Projeto B", "campaign")
            list_projects()

        captured = capsys.readouterr()
        assert "Projeto A" in captured.out
        assert "Projeto B" in captured.out


class TestShowStatus:
    """Testes para status de projeto."""

    def test_status_existing_project(self, mock_projects_dir, capsys):
        with patch("project_manager.PROJECTS_DIR", mock_projects_dir):
            create_project("Status Test", "funnel", "Teste de status")
            show_status("status-test")

        captured = capsys.readouterr()
        assert "Status Test" in captured.out
        assert "Ativo" in captured.out

    def test_status_nonexistent(self, mock_projects_dir, capsys):
        with patch("project_manager.PROJECTS_DIR", mock_projects_dir):
            show_status("nao-existe")

        captured = capsys.readouterr()
        assert "não encontrado" in captured.out


class TestAddContent:
    """Testes para adição de conteúdo a projetos."""

    def test_add_content_success(self, mock_projects_dir, tmp_dir, capsys):
        # Criar arquivo de conteúdo temporário
        content_file = os.path.join(tmp_dir, "conteudo.md")
        with open(content_file, 'w') as f:
            f.write("# Conteúdo de teste\n\nTexto do conteúdo.")

        with patch("project_manager.PROJECTS_DIR", mock_projects_dir):
            create_project("Content Test", "batch")
            add_content("content-test", content_file, "post")

            data = load_project("content-test")

        assert len(data["contents"]) == 1
        assert data["contents"][0]["type"] == "post"
        assert data["contents"][0]["filename"] == "conteudo.md"

    def test_add_content_nonexistent_project(self, mock_projects_dir, capsys):
        with patch("project_manager.PROJECTS_DIR", mock_projects_dir):
            add_content("nao-existe", "arquivo.md")

        captured = capsys.readouterr()
        assert "não encontrado" in captured.out

    def test_add_content_nonexistent_file(self, mock_projects_dir, capsys):
        with patch("project_manager.PROJECTS_DIR", mock_projects_dir):
            create_project("File Test", "custom")
            add_content("file-test", "/caminho/inexistente.md")

        captured = capsys.readouterr()
        assert "não encontrado" in captured.out


class TestCompleteProject:
    """Testes para conclusão de projetos."""

    def test_complete_project(self, mock_projects_dir, capsys):
        with patch("project_manager.PROJECTS_DIR", mock_projects_dir):
            create_project("Complete Test", "launch")
            complete_project("complete-test")
            data = load_project("complete-test")

        assert data["status"] == "completed"
        assert "completed_at" in data

    def test_complete_nonexistent(self, mock_projects_dir, capsys):
        with patch("project_manager.PROJECTS_DIR", mock_projects_dir):
            complete_project("nao-existe")

        captured = capsys.readouterr()
        assert "não encontrado" in captured.out


class TestAddNote:
    """Testes para notas em projetos."""

    def test_add_note(self, mock_projects_dir, capsys):
        with patch("project_manager.PROJECTS_DIR", mock_projects_dir):
            create_project("Note Test", "custom")
            add_note("note-test", "Nota de teste importante")
            data = load_project("note-test")

        assert len(data["notes"]) == 1
        assert data["notes"][0]["text"] == "Nota de teste importante"
        assert "date" in data["notes"][0]

    def test_add_multiple_notes(self, mock_projects_dir):
        with patch("project_manager.PROJECTS_DIR", mock_projects_dir):
            create_project("Multi Notes", "custom")
            add_note("multi-notes", "Nota 1")
            add_note("multi-notes", "Nota 2")
            add_note("multi-notes", "Nota 3")
            data = load_project("multi-notes")

        assert len(data["notes"]) == 3
