"""Tests for audit_detector.py (input type detection)."""
from __future__ import annotations

import json
import os
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pytest

from audit_detector import detect


class TestLandingDetection:
    def test_https_url(self):
        result = detect("https://stripe.com")
        assert result["type"] == "landing"
        assert result["normalized"] == "https://stripe.com"
        assert result["slug"] == "stripe"

    def test_http_url(self):
        result = detect("http://example.com")
        assert result["type"] == "landing"
        assert result["normalized"] == "http://example.com"

    def test_url_with_path(self):
        result = detect("https://example.com/landing")
        assert result["type"] == "landing"
        assert result["slug"] == "example"

    def test_url_with_trailing_slash(self):
        result = detect("https://stripe.com/")
        assert result["normalized"] == "https://stripe.com"

    def test_url_with_subdomain(self):
        result = detect("https://blog.stripe.com")
        assert result["slug"] == "stripe"

    def test_url_with_query_preserves_query(self):
        result = detect("https://stripe.com/?ref=1")
        assert result["normalized"] == "https://stripe.com/?ref=1"
        assert result["slug"] == "stripe"


class TestInstagramDetection:
    def test_at_prefix(self):
        result = detect("@ericorocha")
        assert result["type"] == "instagram"
        assert result["normalized"] == "ericorocha"
        assert result["slug"] == "ericorocha"

    def test_no_prefix_letters_only(self):
        result = detect("ericorocha")
        assert result["type"] == "instagram"
        assert result["normalized"] == "ericorocha"

    def test_with_dot(self):
        result = detect("@joao.silva")
        assert result["type"] == "instagram"
        assert result["normalized"] == "joao.silva"

    def test_with_underscore(self):
        result = detect("@user_name_123")
        assert result["type"] == "instagram"
        assert result["normalized"] == "user_name_123"

    def test_uppercase_lowercased(self):
        result = detect("@EricoRocha")
        assert result["normalized"] == "ericorocha"
        assert result["slug"] == "ericorocha"
