"""ALERT — emit one prioritized, actionable, sourced notice per gap.

Stage 4. Turn each Gap into a finding in the shape of data/sample_expected_output.json, and
a short alert message a compliance officer could act on.

Finding shape (one object per gap):
    company, partner_id, product_id, product, regulation, requirement, source_url,
    gap, deadline, severity, recommended_action,
    alert: { channel, to, message }

Rules:
    - Prioritize by deadline (soonest first) and severity (high first).
    - Every finding carries a real, resolvable source_url.
    - The message is concrete: "product Y must meet rule X by deadline Z — here's the fix."
    - A real notification (email / webhook / console) is a PLUS, never required. Contacts in
      the portfolio are synthetic @example.com — NEVER send to a real person. If you demo a
      live send, use your OWN test number / email.

    Write emitted findings to findings/ (git-tracked) so your output is part of the repo.

TODO:
  1. Sort gaps by (deadline, severity).
  2. Render each into the finding shape + an alert message.
  3. Write findings.json to findings/.
  4. (Optional) fire one real alert to your own test channel.
"""

from __future__ import annotations

import json
from pathlib import Path

OUTPUT_DIR = Path(__file__).resolve().parent.parent / "findings"


def to_finding(gap) -> dict:
    """Render a Gap into the sample_expected_output.json finding shape.

    TODO: build the dict + the alert sub-object. Keep source_url. Make the message specific.
    """
    raise NotImplementedError(
        "Implement to_finding(): match data/sample_expected_output.json, prioritized, sourced."
    )


def emit(gaps: list) -> Path:
    """Sort, render, and write all findings to findings/findings.json."""
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    findings = [to_finding(g) for g in gaps]  # TODO: sort by (deadline, severity) first
    out = OUTPUT_DIR / "findings.json"
    with open(out, "w", encoding="utf-8") as fh:
        json.dump(findings, fh, indent=2, ensure_ascii=False)
    return out


if __name__ == "__main__":
    print("Run the full pipeline: ingest -> extract -> assess -> alert.")
