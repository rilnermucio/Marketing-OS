"""Testes para hook_generator.py — geração de hooks virais."""

import pytest
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from hook_generator import (
    generate_hooks,
    HOOK_TEMPLATES,
    EMOJIS,
    PLATFORM_SPECS,
)


class TestGenerateHooks:
    """Testes para geração de hooks."""

    def test_basic_generation(self):
        result = generate_hooks("marketing digital")
        assert result["tema"] == "marketing digital"
        assert result["plataforma"] == "reels"
        assert len(result["hooks"]) == 10

    def test_custom_quantity(self):
        result = generate_hooks("IA", "tiktok", 5)
        assert len(result["hooks"]) == 5

    def test_custom_platform(self):
        result = generate_hooks("produtividade", "linkedin")
        assert result["plataforma"] == "linkedin"

    def test_hooks_contain_tema(self):
        result = generate_hooks("finanças pessoais", "reels", 5)
        for hook_data in result["hooks"]:
            assert "finanças pessoais" in hook_data["hook"].lower() or "finanças pessoais" in hook_data["hook"]

    def test_hooks_have_required_fields(self):
        result = generate_hooks("tema teste", "reels", 3)
        for hook_data in result["hooks"]:
            assert "hook" in hook_data
            assert "categoria" in hook_data
            assert "emoji" in hook_data
            assert "chars" in hook_data
            assert isinstance(hook_data["chars"], int)

    def test_result_structure(self):
        result = generate_hooks("teste")
        assert "tema" in result
        assert "plataforma" in result
        assert "specs" in result
        assert "hooks" in result
        assert "categorias_usadas" in result
        assert "total_gerado" in result

    def test_categorias_usadas_not_empty(self):
        result = generate_hooks("tema", "reels", 10)
        assert len(result["categorias_usadas"]) > 0

    def test_zero_quantity(self):
        result = generate_hooks("tema", "reels", 0)
        assert len(result["hooks"]) == 0

    def test_large_quantity(self):
        result = generate_hooks("tema", "reels", 50)
        assert len(result["hooks"]) == 50

    def test_unknown_platform_fallback(self):
        result = generate_hooks("tema", "plataforma_inexistente")
        # Deve usar specs de "reels" como fallback
        assert result["specs"] == PLATFORM_SPECS["reels"]

    def test_emoji_placement_reels(self):
        """Reels deve ter emoji no início."""
        result = generate_hooks("tema", "reels", 5)
        for hook_data in result["hooks"]:
            # O hook deve começar com emoji (caractere não-ASCII)
            first_char = hook_data["hook"][0]
            assert not first_char.isalpha() or not first_char.isascii()


class TestHookTemplates:
    """Testes para templates de hooks."""

    def test_all_categories_have_templates(self):
        expected = ["curiosidade", "controversia", "numero", "historia", "urgencia", "identificacao", "promessa", "prova_social"]
        for cat in expected:
            assert cat in HOOK_TEMPLATES, f"Categoria '{cat}' não encontrada"
            assert len(HOOK_TEMPLATES[cat]) > 0

    def test_templates_have_tema_placeholder(self):
        for cat, templates in HOOK_TEMPLATES.items():
            for template in templates:
                assert "{tema}" in template, f"Template sem {{tema}} em {cat}: {template}"

    def test_templates_are_strings(self):
        for cat, templates in HOOK_TEMPLATES.items():
            for template in templates:
                assert isinstance(template, str)


class TestEmojis:
    """Testes para emojis por categoria."""

    def test_all_categories_have_emojis(self):
        for cat in HOOK_TEMPLATES:
            assert cat in EMOJIS, f"Categoria '{cat}' sem emojis"
            assert len(EMOJIS[cat]) > 0

    def test_emojis_are_strings(self):
        for cat, emoji_list in EMOJIS.items():
            for emoji in emoji_list:
                assert isinstance(emoji, str)
                assert len(emoji) > 0


class TestPlatformSpecs:
    """Testes para especificações de plataforma."""

    def test_all_platforms_exist(self):
        expected = ["reels", "tiktok", "youtube", "shorts", "linkedin", "twitter"]
        for platform in expected:
            assert platform in PLATFORM_SPECS

    def test_specs_structure(self):
        for platform, specs in PLATFORM_SPECS.items():
            assert "max_chars" in specs
            assert "style" in specs
            assert "emoji_position" in specs
            assert "tip" in specs
            assert isinstance(specs["max_chars"], int)
            assert specs["max_chars"] > 0
