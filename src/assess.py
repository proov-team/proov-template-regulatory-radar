"""ASSESS — reason over the portfolio to find real gaps (the core of the challenge).

Stage 3, and the heaviest-weighted part of the grade. For every company and product in
data/partners.json, decide two things against each current requirement:

    1. Does the obligation APPLY to this product?
    2. If it applies, is there a GAP (the obligation is not satisfied)?

Reason from the product's ATTRIBUTES, not its category label alone. An obligation applies
only when ALL of these line up:

    - market     : the company sells where the rule applies ("EU" = all 27 states)
    - category   : the rule covers the product's category (or "all" electronics)
    - substance  : if the rule names a substance, the product actually CONTAINS it
    - attributes : battery_type / battery_capacity_wh / has_radio / connector /
                   intended_use / packaging put it in scope
    - exclusions : general consumer-safety rules don't cover medical/industrial-only kit

The LOOK-ALIKE trap — the reason category-only matching fails:
    - right category, WRONG market                → NOT a gap
    - a rule naming a substance the product        → NOT a gap
      does NOT contain
    - a battery-passport rule that hits LMT /       → NOT a gap for a PORTABLE battery
      industrial batteries

Ground truth: a few companies carry an explicit `compliance_status` block
(certs_held + known_gaps). Your assessment should AGREE with those. Most companies have no
such block — inferring their gaps from the current requirements is the challenge.

Every gap you report must CITE the source_url of the requirement that raised it.

TODO:
  1. Load data/partners.json (and data/taxonomy.json for the vocabulary).
  2. For each product x requirement, run applies() then has_gap().
  3. Reject look-alikes (attribute mismatch is NOT a gap).
  4. Cross-check against compliance_status where present.
  5. Return a list of Gap records for the alert stage.
"""

from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parent.parent / "data"


@dataclass
class Gap:
    partner_id: str
    company: str
    product_id: str
    product: str
    regulation: str
    requirement: str
    source_url: str
    gap: str
    deadline: str | None
    severity: str  # "low" | "medium" | "high"
    recommended_action: str


def load_portfolio() -> list[dict]:
    """Load the synthetic SME portfolio from data/partners.json."""
    with open(DATA_DIR / "partners.json", encoding="utf-8") as fh:
        return json.load(fh)["partners"]


def applies(product: dict, requirement) -> bool:
    """Does `requirement` apply to `product`? Reason on market/category/substance/attributes.

    TODO: implement the scope check. This is where look-alikes are rejected — an attribute
    or market mismatch means the rule does NOT apply, even if the category matches.
    """
    raise NotImplementedError(
        "Implement applies(): a requirement applies only when market + category + "
        "substance + attributes all land in scope. Reject look-alikes here."
    )


def has_gap(product: dict, requirement) -> bool:
    """Given the requirement applies, is it unsatisfied for this product?

    TODO: infer from the product's compliance_streams / attributes, and cross-check
    compliance_status.known_gaps where the company provides it (ground truth).
    """
    raise NotImplementedError(
        "Implement has_gap(): an applicable obligation that is not satisfied is a gap. "
        "Agree with compliance_status ground truth where present."
    )


def assess_portfolio(requirements: list) -> list[Gap]:
    """Assess every product against every current requirement; return the real gaps."""
    portfolio = load_portfolio()
    gaps: list[Gap] = []
    for partner in portfolio:
        for product in partner["products"]:
            for req in requirements:
                if applies(product, req) and has_gap(product, req):
                    # TODO: build a Gap record here, citing req.source_url.
                    pass
    return gaps
