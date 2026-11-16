"""FIND — pull CURRENT EU product requirements from a real official source.

This is stage 1 of the Regulatory Radar loop. Your job here is to fetch current
regulatory requirements from at least one REAL official source (EUR-Lex, ECHA, EPREL, or
EU Safety Gate — see data/SOURCES.md) and cache the raw response so the rest of the
pipeline (and the grader) has evidence of a real fetch.

IMPORTANT — what "live" means for grading:
  The grader reads a SNAPSHOT of this repo; it does not run your code live. So "fetches
  live" is proven by EVIDENCE committed to the repo, not by a call at grade time:
    - ingestion code that targets a real source endpoint / page (not the bundled example),
    - the cached raw responses you pulled (commit them under data/cache/),
    - a recorded access date for each fetch,
    - a real, resolvable source_url that flows through to every finding.

  Reading only the bundled data/… example JSON, or hard-coding rules, scores LOW on
  "Live source ingestion & citation". Do a real fetch and cache it.

TODO:
  1. Pick 1-2 sources from data/SOURCES.md. Prefer official APIs / RSS / downloadable
     lists over scraping rendered HTML (more stable, more polite).
  2. Fetch the current requirement(s). Respect robots.txt and rate limits.
  3. Cache each raw response to data/cache/ with the source URL and an access timestamp
     (e.g. a small JSON envelope: {source_url, fetched_at, raw}). Commit the cache.
  4. Return the raw documents for the extract stage to parse.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path

CACHE_DIR = Path(__file__).resolve().parent.parent / "data" / "cache"


@dataclass
class RawRegulation:
    """One fetched, un-parsed regulatory document."""

    source_url: str
    fetched_at: str  # ISO-8601 UTC timestamp — record when you pulled it
    raw_text: str = ""
    metadata: dict = field(default_factory=dict)


def fetch_current_rules(sources: list[str] | None = None) -> list[RawRegulation]:
    """Fetch current EU requirements from a real official source and cache them.

    Args:
        sources: URLs / API entry points to pull from. Default to your chosen source(s).

    Returns:
        A list of RawRegulation documents (also written to data/cache/).

    TODO: implement the real fetch + cache. Do NOT just read the bundled example JSON.
    """
    raise NotImplementedError(
        "Implement fetch_current_rules(): pull from a real source in data/SOURCES.md, "
        "cache the raw response to data/cache/ with a source_url and access date."
    )


def _access_date() -> str:
    """UTC access timestamp to stamp on every cached fetch."""
    return datetime.now(timezone.utc).isoformat()


if __name__ == "__main__":
    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    rules = fetch_current_rules()
    print(f"Fetched and cached {len(rules)} current requirement(s).")
