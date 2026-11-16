"""UNDERSTAND — turn a raw regulatory document into a structured requirement.

Stage 2 of the loop. Direct your AI coding agent (IBM Bob / Claude Code / Cursor / Copilot)
to READ each fetched rule and EXTRACT the facts the assess stage needs. Do not hand-wave
this into free text — the assessment reasons over structured fields.

For each requirement, capture at minimum:
    - regulation      : the family + reference (e.g. "EU Battery Regulation (EU) 2023/1542")
    - requirement     : the plain-English obligation
    - scope.categories: which product categories it covers (or "all")
    - scope.substances: which substances it names (empty if none)
    - scope.markets   : which markets it applies to ("EU" = all 27 states)
    - scope.conditions: attribute conditions (battery type/capacity, has_radio, use, …)
    - deadline        : the compliance deadline (ISO date), if any
    - is_current      : whether this is the in-force version (not superseded/corrected)
    - source_url      : carried through from ingest — every requirement keeps its source

Watch the noise: real feeds mix in unrelated-domain entries and correction/duplicate
entries. Extraction should keep only current, in-scope requirements.

TODO:
  1. For each RawRegulation, prompt your agent (or parse) to produce a StructuredRequirement.
  2. Validate the structured output — reject a rule with no scope or a mangled deadline.
  3. Keep source_url attached; the assessment cites it on every gap.
"""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class Scope:
    categories: list[str] = field(default_factory=list)  # [] or ["all"]
    substances: list[str] = field(default_factory=list)
    markets: list[str] = field(default_factory=list)
    conditions: str = ""


@dataclass
class StructuredRequirement:
    regulation: str
    requirement: str
    scope: Scope
    deadline: str | None = None  # ISO-8601 date
    is_current: bool = True
    source_url: str = ""


def extract_requirement(raw) -> StructuredRequirement:
    """Extract one StructuredRequirement from a RawRegulation.

    TODO: implement extraction (LLM-directed or parsed). Keep source_url; validate scope.
    """
    raise NotImplementedError(
        "Implement extract_requirement(): produce structured scope + deadline + is_current, "
        "carrying source_url through. Reject entries with no scope or a bad deadline."
    )


def extract_all(raws: list) -> list[StructuredRequirement]:
    """Extract every raw doc, dropping non-current / out-of-scope / noise entries."""
    requirements: list[StructuredRequirement] = []
    for raw in raws:
        req = extract_requirement(raw)
        if req.is_current:
            requirements.append(req)
    return requirements
