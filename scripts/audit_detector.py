"""Detect input type for /auditoria command.

Input → {type: landing|instagram|meta_ads|youtube, normalized, slug}.
Raises ValueError on invalid input.

CLI: python audit_detector.py "<input>" → JSON to stdout.
"""
from __future__ import annotations

import json
import re
import sys
from urllib.parse import urlparse


_URL_RE = re.compile(r"^https?://", re.IGNORECASE)


def _slug_from_landing(url: str) -> str:
    parsed = urlparse(url)
    host = parsed.netloc.lower()
    if host.startswith("www."):
        host = host[4:]
    parts = host.split(".")
    if len(parts) >= 2:
        return parts[-2]
    return host


def _normalize_landing(url: str) -> str:
    parsed = urlparse(url)
    if parsed.path == "/" and not parsed.query and not parsed.fragment:
        return f"{parsed.scheme}://{parsed.netloc}"
    return url.rstrip("/") if not parsed.path or parsed.path == "/" else url


def detect(input_str: str) -> dict:
    """Return {type, normalized, slug} or raise ValueError."""
    if not input_str or not input_str.strip():
        raise ValueError(
            "Input vazio. Exemplos:\n"
            "  /auditoria https://stripe.com (landing)\n"
            "  /auditoria @ericorocha (instagram)\n"
            "  /auditoria https://www.facebook.com/ads/library/?... (meta ads)\n"
            "  /auditoria https://youtube.com/watch?v=... (youtube)"
        )

    s = input_str.strip()

    if _URL_RE.match(s):
        return {
            "type": "landing",
            "normalized": _normalize_landing(s),
            "slug": _slug_from_landing(s),
        }

    raise ValueError(f"Não consegui interpretar: {input_str!r}")
