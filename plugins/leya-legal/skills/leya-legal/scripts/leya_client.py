# ABOUTME: Thin CLI wrapper around the Leya v1 API for use from inside the Claude plugin.
# ABOUTME: Resolves the API key from ${CLAUDE_PLUGIN_DATA}/leya.json first, then LEYA_API_KEY env.

from __future__ import annotations

import argparse
import json
import os
import sys
from pathlib import Path
from urllib.parse import urlencode
from urllib.request import Request, urlopen
from urllib.error import HTTPError

DEFAULT_BASE = "https://leya-api-production.up.railway.app"


def _resolve_api_key() -> str | None:
    """Plugin data dir first, then env var.

    The plugin data dir is persistent per-user. /leya:setup writes a leya.json
    file there containing {"api_key": "leya_live_..."}. Env var is the
    fallback for power users running the script outside Claude.
    """
    data_dir = os.environ.get("CLAUDE_PLUGIN_DATA")
    if data_dir:
        config_path = Path(data_dir) / "leya.json"
        if config_path.is_file():
            try:
                blob = json.loads(config_path.read_text())
                key = blob.get("api_key")
                if key:
                    return key
            except (json.JSONDecodeError, OSError):
                pass
    return os.environ.get("LEYA_API_KEY")


def _request(path: str, params: dict[str, str] | None = None) -> dict:
    base = os.environ.get("LEYA_API_BASE", DEFAULT_BASE).rstrip("/")
    key = _resolve_api_key()
    if not key:
        print(
            "error: no Leya API key configured. "
            "Ask the user for their key and run /leya:setup <key> to save it.",
            file=sys.stderr,
        )
        sys.exit(2)

    url = f"{base}{path}"
    if params:
        url += "?" + urlencode({k: v for k, v in params.items() if v is not None})

    req = Request(url, headers={"Authorization": f"Bearer {key}"})
    try:
        with urlopen(req, timeout=30) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except HTTPError as e:
        body = e.read().decode("utf-8", errors="replace")
        print(f"error: HTTP {e.code} — {body}", file=sys.stderr)
        sys.exit(1)


def cmd_sources(args: argparse.Namespace) -> int:
    print(json.dumps(_request("/v1/sources"), indent=2, ensure_ascii=False))
    return 0


def cmd_search(args: argparse.Namespace) -> int:
    params = {
        "q": args.query,
        "country": args.country,
        "source_id": args.source_id,
        "document_type": args.document_type,
        "as_of": args.as_of,
        "legal_area": args.legal_area,
        "limit": str(args.limit) if args.limit else None,
    }
    print(json.dumps(_request("/v1/search", params), indent=2, ensure_ascii=False))
    return 0


def cmd_document(args: argparse.Namespace) -> int:
    print(
        json.dumps(
            _request(f"/v1/documents/{args.document_id}"),
            indent=2,
            ensure_ascii=False,
        )
    )
    return 0


def cmd_citation(args: argparse.Namespace) -> int:
    print(
        json.dumps(
            _request(f"/v1/documents/{args.document_id}/citation"),
            indent=2,
            ensure_ascii=False,
        )
    )
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description="Leya v1 API client (Skill helper).")
    sub = p.add_subparsers(dest="cmd", required=True)

    s_sources = sub.add_parser("sources", help="List registered legal sources.")
    s_sources.set_defaults(func=cmd_sources)

    s_search = sub.add_parser("search", help="Search the legal corpus.")
    s_search.add_argument("query")
    s_search.add_argument("--country", default="GT")
    s_search.add_argument("--source-id", dest="source_id")
    s_search.add_argument("--document-type", dest="document_type")
    s_search.add_argument("--as-of", dest="as_of")
    s_search.add_argument("--legal-area", dest="legal_area")
    s_search.add_argument("--limit", type=int, default=10)
    s_search.set_defaults(func=cmd_search)

    s_doc = sub.add_parser("document", help="Fetch a document by id (full markdown body).")
    s_doc.add_argument("document_id")
    s_doc.set_defaults(func=cmd_document)

    s_cite = sub.add_parser("citation", help="Get a formatted citation for a document.")
    s_cite.add_argument("document_id")
    s_cite.set_defaults(func=cmd_citation)

    return p


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
