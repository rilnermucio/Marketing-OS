"""Testes para mos.py — CLI unificado do Marketing OS."""

import pytest
import os
import sys
from unittest.mock import patch, MagicMock

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from mos import COMMAND_MAP, SPECIAL_ARGS, SCRIPTS_DIR


class TestCommandMap:
    """Testes para a estrutura do mapa de comandos."""

    def test_all_categories_exist(self):
        expected_categories = [
            "seo", "headlines", "hooks", "hashtags", "content",
            "reels", "carousel", "trends", "competitor",
            "readability", "ab", "captions", "quality", "project",
        ]
        for cat in expected_categories:
            assert cat in COMMAND_MAP, f"Categoria '{cat}' não encontrada no COMMAND_MAP"

    def test_all_commands_have_script_and_description(self):
        for category, commands in COMMAND_MAP.items():
            for cmd, (script, desc) in commands.items():
                assert script.endswith(".py"), f"{category}.{cmd}: script '{script}' não termina com .py"
                assert len(desc) > 0, f"{category}.{cmd}: descrição vazia"

    def test_all_scripts_exist(self):
        for category, commands in COMMAND_MAP.items():
            for cmd, (script, desc) in commands.items():
                script_path = os.path.join(SCRIPTS_DIR, script)
                assert os.path.exists(script_path), f"Script não existe: {script_path} (ref: {category}.{cmd})"

    def test_seo_commands(self):
        assert "analyze" in COMMAND_MAP["seo"]

    def test_headlines_commands(self):
        assert "score" in COMMAND_MAP["headlines"]
        assert "compare" in COMMAND_MAP["headlines"]

    def test_hooks_commands(self):
        assert "generate" in COMMAND_MAP["hooks"]
        assert "variants" in COMMAND_MAP["hooks"]

    def test_project_commands(self):
        expected = ["novo", "list", "status", "avancar", "aprovar", "rejeitar"]
        for cmd in expected:
            assert cmd in COMMAND_MAP["project"], f"Comando 'project.{cmd}' não encontrado"

    def test_quality_commands(self):
        assert "check" in COMMAND_MAP["quality"]


class TestSpecialArgs:
    """Testes para transformação de argumentos especiais."""

    def test_headlines_compare_transform(self):
        transform = SPECIAL_ARGS[("headlines", "compare")]
        result = transform(["Headline A", "Headline B"])
        assert result[0] == "--compare"
        assert "Headline A" in result
        assert "Headline B" in result

    def test_project_novo_transform(self):
        transform = SPECIAL_ARGS[("project", "novo")]
        result = transform(["Nome Projeto", "--tipo", "lancamento"])
        assert result[0] == "novo"
        assert "Nome Projeto" in result

    def test_project_list_transform(self):
        transform = SPECIAL_ARGS[("project", "list")]
        result = transform([])
        assert result[0] == "list"

    def test_project_status_transform(self):
        transform = SPECIAL_ARGS[("project", "status")]
        result = transform(["meu-projeto"])
        assert result[0] == "status"
        assert "meu-projeto" in result

    def test_all_project_commands_have_special_args(self):
        """Todos os comandos de project devem ter transformação de args."""
        for cmd in COMMAND_MAP["project"]:
            assert ("project", cmd) in SPECIAL_ARGS, f"SPECIAL_ARGS faltando para ('project', '{cmd}')"


class TestMainFunction:
    """Testes para a função main via sys.argv."""

    def test_help_flag(self, capsys):
        from mos import main
        with patch("sys.argv", ["mos.py", "--help"]):
            with pytest.raises(SystemExit) as exc:
                main()
            assert exc.value.code == 0

    def test_unknown_category(self, capsys):
        from mos import main
        with patch("sys.argv", ["mos.py", "desconhecido"]):
            with pytest.raises(SystemExit) as exc:
                main()
            assert exc.value.code == 1
        captured = capsys.readouterr()
        assert "desconhecida" in captured.out

    def test_category_without_command(self, capsys):
        from mos import main
        with patch("sys.argv", ["mos.py", "seo"]):
            with pytest.raises(SystemExit) as exc:
                main()
            assert exc.value.code == 1
        captured = capsys.readouterr()
        assert "Comandos disponíveis" in captured.out

    def test_unknown_command(self, capsys):
        from mos import main
        with patch("sys.argv", ["mos.py", "seo", "desconhecido"]):
            with pytest.raises(SystemExit) as exc:
                main()
            assert exc.value.code == 1
        captured = capsys.readouterr()
        assert "desconhecido" in captured.out


class TestRunScript:
    """Testes para execução de scripts."""

    def test_run_nonexistent_script(self, capsys):
        from mos import run_script
        with pytest.raises(SystemExit) as exc:
            run_script("script_que_nao_existe.py", [])
        assert exc.value.code == 1
        captured = capsys.readouterr()
        assert "não encontrado" in captured.out

    def test_run_script_calls_subprocess(self):
        from mos import run_script
        with patch("subprocess.run") as mock_run:
            mock_run.return_value = MagicMock(returncode=0)
            with pytest.raises(SystemExit) as exc:
                run_script("seo_analyzer.py", ["test.md"])
            assert exc.value.code == 0
            mock_run.assert_called_once()
            call_args = mock_run.call_args[0][0]
            assert "seo_analyzer.py" in call_args[-2] or call_args[1].endswith("seo_analyzer.py")


class TestScriptsDir:
    """Testes para o diretório de scripts."""

    def test_scripts_dir_exists(self):
        assert os.path.isdir(SCRIPTS_DIR)

    def test_scripts_dir_contains_mos(self):
        assert os.path.exists(os.path.join(SCRIPTS_DIR, "mos.py"))
