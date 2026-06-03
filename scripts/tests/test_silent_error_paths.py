#!/usr/bin/env python3
"""Cobre os caminhos de erro que antes engoliam exceções em silêncio.

Garante que fetch/leitura com falha (a) retorna o sentinel esperado e
(b) emite o aviso no stderr (o fix de debuggability não regride).
"""
from __future__ import annotations

import os
import sys
from unittest.mock import patch

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

import competitor_analyzer
import content_audit
import trend_tracker


def test_competitor_fetch_failure_returns_none_and_warns(capsys):
    with patch("urllib.request.urlopen", side_effect=OSError("boom")):
        assert competitor_analyzer.fazer_requisicao("http://x.invalid") is None
    assert "competitor_analyzer" in capsys.readouterr().err


def test_trend_fetch_failure_returns_none_and_warns(capsys):
    with patch("urllib.request.urlopen", side_effect=OSError("boom")):
        assert trend_tracker.fazer_requisicao("http://x.invalid") is None
    assert "trend_tracker" in capsys.readouterr().err


def test_content_audit_read_error_returns_none_and_warns(tmp_path, capsys):
    # Passar um diretório dispara IsADirectoryError (não FileNotFoundError),
    # caindo no except amplo que agora avisa no stderr.
    result = content_audit.ler_arquivo(str(tmp_path))
    assert result == (None, None)
    assert "content_audit" in capsys.readouterr().err
