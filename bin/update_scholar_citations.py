#!/usr/bin/env python3
"""Update Google Scholar citation counts on _publications/*.md.

Queries the author's Scholar profile (site.author.googlescholar in _config.yml)
for the list of papers and their citedby counts, then fuzzy-matches each entry
against the frontmatter `title` of the local _publications files. When a match
is found, the file's frontmatter gets two updated fields:

  citations: <int>              # citedby count reported by Scholar
  citation_updated: <YYYY-MM-DD> # UTC date the value was refreshed

Files that already have a `citations` field but no longer match Scholar are
left untouched.

Run locally:
  pip install scholarly pyyaml
  python bin/update_scholar_citations.py
"""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from datetime import datetime, timezone
from difflib import SequenceMatcher
from pathlib import Path

import yaml
from scholarly import scholarly

REPO_ROOT = Path(__file__).resolve().parents[1]
PUBS_DIR = REPO_ROOT / "_publications"
CONFIG_PATH = REPO_ROOT / "_config.yml"

FRONT_MATTER_RE = re.compile(r"^---\n(.*?)\n---\n(.*)$", re.DOTALL)


@dataclass
class Publication:
    path: Path
    frontmatter: dict
    body: str


def load_publication(path: Path) -> Publication | None:
    text = path.read_text(encoding="utf-8")
    match = FRONT_MATTER_RE.match(text)
    if not match:
        return None
    fm = yaml.safe_load(match.group(1)) or {}
    return Publication(path=path, frontmatter=fm, body=match.group(2))


def dump_publication(pub: Publication) -> None:
    fm_text = yaml.safe_dump(
        pub.frontmatter, allow_unicode=True, sort_keys=False, default_flow_style=False
    ).strip()
    pub.path.write_text(f"---\n{fm_text}\n---\n{pub.body}", encoding="utf-8")


def scholar_user_id(config_path: Path) -> str:
    with config_path.open("r", encoding="utf-8") as fp:
        cfg = yaml.safe_load(fp)
    url = cfg.get("author", {}).get("googlescholar", "")
    match = re.search(r"user=([A-Za-z0-9_-]+)", url)
    if not match:
        raise SystemExit(f"Could not extract Scholar user id from {url!r}")
    return match.group(1)


def normalize(title: str) -> str:
    return re.sub(r"[^a-z0-9]", "", title.lower())


def best_match(target: str, candidates: list[dict]) -> tuple[dict | None, float]:
    target_norm = normalize(target)
    best, best_score = None, 0.0
    for pub in candidates:
        cand_title = pub.get("bib", {}).get("title", "")
        score = SequenceMatcher(None, target_norm, normalize(cand_title)).ratio()
        if score > best_score:
            best, best_score = pub, score
    return best, best_score


def fetch_scholar_pubs(user_id: str) -> list[dict]:
    author = scholarly.search_author_id(user_id)
    filled = scholarly.fill(author, sections=["publications"])
    return filled.get("publications", [])


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--min-score",
        type=float,
        default=0.75,
        help="Minimum fuzzy match score to accept a Scholar entry (0-1).",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print planned changes without writing files.",
    )
    args = parser.parse_args()

    user_id = scholar_user_id(CONFIG_PATH)
    print(f"Fetching Scholar profile for user {user_id}...", file=sys.stderr)
    scholar_pubs = fetch_scholar_pubs(user_id)
    print(f"  {len(scholar_pubs)} Scholar entries retrieved.", file=sys.stderr)

    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    updated = 0
    for path in sorted(PUBS_DIR.glob("*.md")):
        pub = load_publication(path)
        if pub is None or "title" not in pub.frontmatter:
            continue
        match, score = best_match(str(pub.frontmatter["title"]), scholar_pubs)
        if match is None or score < args.min_score:
            print(f"  skip {path.name} (best score {score:.2f})", file=sys.stderr)
            continue
        citations = int(match.get("num_citations", 0))
        prev = pub.frontmatter.get("citations")
        pub.frontmatter["citations"] = citations
        pub.frontmatter["citation_updated"] = today
        if prev == citations and pub.frontmatter.get("citation_updated") == today:
            continue
        if args.dry_run:
            print(f"  would update {path.name}: citations {prev} -> {citations}")
        else:
            dump_publication(pub)
            print(f"  updated {path.name}: citations {prev} -> {citations}")
        updated += 1

    print(f"{updated} files updated.", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
