#!/usr/bin/env python3
"""
Apify Twitter/X Profile Scraper — opcional, requer APIFY_TOKEN.

Despacha o Actor apidojo/twitter-scraper-lite para extrair tweets recentes
de um perfil público no X (ex-Twitter). Usado pelo mos-research e
mos-social para análise de concorrente.

Uso:
    python apify_twitter.py --handle @elonmusk
    python apify_twitter.py --handle elonmusk --max-tweets 100
    python apify_twitter.py --handle https://x.com/elonmusk --dry-run
"""

import argparse
import json
import os
import re
import sys
from datetime import datetime, timezone
from typing import Any, Dict, List

from apify_client import (
    ENV_TOKEN,
    ApifyAPIError,
    ApifyAuthError,
    ApifyRateLimitError,
    ApifyTimeoutError,
    estimate_cost,
    run_actor_sync,
    save_result,
)


TWITTER_ACTOR_ID = "apidojo/twitter-scraper-lite"
DEFAULT_OUTPUT_DIR = "workspace/research/apify"
DEFAULT_MAX_TWEETS = 50
HARD_CAP_TWEETS = 200
DEFAULT_TIMEOUT = 120


def normalize_handle(raw: str) -> str:
    """
    Aceita @handle, handle, URL completa do X/Twitter. Retorna handle limpo.
    """
    if not raw:
        return ""
    s = raw.strip()
    m = re.match(
        r"https?://(www\.)?(x|twitter)\.com/([^/?#]+)",
        s,
        re.IGNORECASE,
    )
    if m:
        return m.group(3)
    if s.startswith("@"):
        return s[1:]
    return s


def build_input(handle: str, max_tweets: int = DEFAULT_MAX_TWEETS) -> Dict[str, Any]:
    """Constrói input do Actor apidojo/twitter-scraper-lite."""
    clean = normalize_handle(handle)
    capped = max(1, min(max_tweets, HARD_CAP_TWEETS))
    return {
        "twitterHandles": [clean],
        "maxItems": capped,
        "sort": "Latest",
    }


def parse_twitter_results(raw: List[Dict[str, Any]]) -> Dict[str, Any]:
    """Extrai tweets, perfil e métricas agregadas."""
    if not raw:
        return {
            "tweets": [],
            "profile": {},
            "metrics": {"total_tweets": 0, "avg_likes": 0, "avg_retweets": 0},
        }

    tweets = []
    profile_handle = ""
    profile_name = ""

    for item in raw:
        if not isinstance(item, dict):
            continue

        author = item.get("author") or {}
        tweet = {
            "id": str(item.get("id", "")),
            "text": item.get("text") or item.get("fullText") or "",
            "url": item.get("url", ""),
            "created_at": item.get("createdAt") or item.get("created_at") or "",
            "likes": int(item.get("likeCount") or item.get("favorite_count") or 0),
            "retweets": int(item.get("retweetCount") or item.get("retweet_count") or 0),
            "replies": int(item.get("replyCount") or item.get("reply_count") or 0),
            "views": int(item.get("viewCount") or 0),
        }
        tweets.append(tweet)

        if not profile_handle:
            profile_handle = author.get("userName") or author.get("screen_name") or ""
        if not profile_name:
            profile_name = author.get("name") or ""

    total = len(tweets)
    if total > 0:
        avg_likes = sum(t["likes"] for t in tweets) // total
        avg_retweets = sum(t["retweets"] for t in tweets) // total
    else:
        avg_likes = 0
        avg_retweets = 0

    return {
        "tweets": tweets,
        "profile": {
            "handle": profile_handle,
            "name": profile_name,
        },
        "metrics": {
            "total_tweets": total,
            "avg_likes": avg_likes,
            "avg_retweets": avg_retweets,
        },
    }


def format_summary_md(parsed: Dict[str, Any], handle: str) -> str:
    """Formata resultado em Markdown."""
    profile = parsed.get("profile", {})
    metrics = parsed.get("metrics", {})
    tweets = parsed.get("tweets", [])

    title_handle = profile.get("handle") or handle
    name = profile.get("name", "")

    lines = [f"## Twitter/X: @{title_handle}"]
    if name:
        lines.append(f"_{name}_")
    lines.append("")

    lines.append("### Métricas agregadas")
    lines.append(f"- Tweets analisados: **{metrics.get('total_tweets', 0)}**")
    lines.append(f"- Média de likes: **{metrics.get('avg_likes', 0):,}**")
    lines.append(f"- Média de retweets: **{metrics.get('avg_retweets', 0):,}**")
    lines.append("")

    if tweets:
        top = sorted(tweets, key=lambda t: t.get("likes", 0), reverse=True)[:5]
        lines.append("### Top 5 tweets por engajamento")
        for t in top:
            text = (t.get("text") or "").replace("\n", " ").strip()
            preview = text[:140] + ("..." if len(text) > 140 else "")
            lines.append(
                f"- {t['likes']:,} likes, {t['retweets']:,} retweets, "
                f"{t['replies']:,} replies"
            )
            if preview:
                lines.append(f"  > {preview}")
            if t.get("url"):
                lines.append(f"  {t['url']}")
        lines.append("")

    return "\n".join(lines).rstrip() + "\n"


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="apify_twitter.py",
        description="Twitter/X profile scraper via Apify (opcional, requer APIFY_TOKEN)",
    )
    parser.add_argument(
        "--handle",
        "-u",
        required=True,
        help="Handle do X/Twitter (@user, user, ou URL)",
    )
    parser.add_argument(
        "--max-tweets",
        "-n",
        type=int,
        default=DEFAULT_MAX_TWEETS,
        help=f"Máximo de tweets (default: {DEFAULT_MAX_TWEETS}, cap: {HARD_CAP_TWEETS})",
    )
    parser.add_argument(
        "--output-dir",
        "-o",
        default=DEFAULT_OUTPUT_DIR,
        help=f"Diretório de saída (default: {DEFAULT_OUTPUT_DIR})",
    )
    parser.add_argument(
        "--dry-run", action="store_true", help="Mostra estimativa de custo sem executar"
    )
    parser.add_argument(
        "--format",
        choices=["md", "json"],
        default="md",
        help="Formato do stdout (default: md)",
    )
    parser.add_argument(
        "--timeout",
        type=int,
        default=DEFAULT_TIMEOUT,
        help=f"Timeout em segundos (default: {DEFAULT_TIMEOUT})",
    )
    return parser


def main() -> int:
    parser = _build_parser()
    args = parser.parse_args()

    handle = normalize_handle(args.handle)
    if not handle:
        print("Handle inválido ou vazio.", file=sys.stderr)
        return 1

    actor_input = build_input(handle, args.max_tweets)
    cost = estimate_cost(TWITTER_ACTOR_ID, actor_input)

    if args.dry_run:
        print(f"Dry-run: Twitter/X scraping de @{handle}")
        print(f"  Actor: {TWITTER_ACTOR_ID}")
        print(f"  Max tweets: {actor_input['maxItems']}")
        print(f"  Custo estimado: ${cost:.4f} USD")
        return 0

    token = os.environ.get(ENV_TOKEN, "").strip()
    if not token:
        print(
            f"{ENV_TOKEN} não configurado. Pulando Twitter/X scraping. "
            f"Use mos-research com WebSearch como fallback.",
            file=sys.stderr,
        )
        return 0

    try:
        raw = run_actor_sync(
            TWITTER_ACTOR_ID, actor_input, token=token, timeout=args.timeout
        )
    except ApifyAuthError as e:
        print(f"Erro de autenticação Apify: {e}", file=sys.stderr)
        return 2
    except ApifyRateLimitError as e:
        print(f"Rate limit Apify: {e}", file=sys.stderr)
        return 2
    except ApifyTimeoutError as e:
        print(f"Timeout Apify: {e}", file=sys.stderr)
        return 2
    except ApifyAPIError as e:
        print(f"Erro Apify: {e}", file=sys.stderr)
        return 2

    # Detecção de "demo mode": Actor de Twitter exige rental/subscription
    # mensal explícita no Apify console. Sem isso, retorna lista de N items
    # idênticos no formato `{"demo": true}`. Detectamos pelo primeiro item.
    if (
        raw
        and isinstance(raw, list)
        and isinstance(raw[0], dict)
        and raw[0].get("demo") is True
    ):
        print(
            f"Actor {TWITTER_ACTOR_ID} retornou modo demo. "
            f"Twitter scrapers no Apify exigem rental mensal explícita "
            f"(não basta APIFY_TOKEN). Ative em "
            f"https://apify.com/{TWITTER_ACTOR_ID} "
            f"ou siga com WebSearch como fallback.",
            file=sys.stderr,
        )
        return 2

    parsed = parse_twitter_results(raw)
    summary_md = format_summary_md(parsed, handle)

    output = {
        "source": TWITTER_ACTOR_ID,
        "handle": handle,
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "cost_estimate_usd": cost,
        "results": parsed,
        "summary_md": summary_md,
    }

    saved_path = save_result(output, slug=handle, output_dir=args.output_dir)
    print(f"# Saved: {saved_path}", file=sys.stderr)

    if args.format == "json":
        print(json.dumps(output, indent=2, ensure_ascii=False))
    else:
        print(summary_md)

    return 0


if __name__ == "__main__":
    sys.exit(main())
