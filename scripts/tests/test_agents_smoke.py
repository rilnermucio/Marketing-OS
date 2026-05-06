"""Tier 2 smoke tests: invoke marketing-os agents via `claude -p`.

DEFERRED until plugin loading verified. See plan Phase 0.8.
"""
import pytest

pytestmark = pytest.mark.smoke


@pytest.mark.skip(reason="Tier 2 smoke tests deferred — needs plugin loading verification first")
def test_smoke_placeholder():
    pass
