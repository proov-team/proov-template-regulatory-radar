"""Starter tests for the ASSESS stage — the look-alike logic is what breaks first.

These are intentionally SKELETAL. Fill them in as you build src/assess.py. The repository
craft criterion rewards a real test suite, and the assess criterion specifically rewards
correctly REJECTING look-alikes — so test the negatives, not just the positives.

Run:  pytest
"""

import pytest

# from src.assess import applies, has_gap, load_portfolio


@pytest.mark.skip(reason="TODO: implement once src.assess.applies is built")
def test_wrong_market_is_not_a_gap():
    """A product sold outside a rule's market must NOT be flagged (look-alike)."""
    # TODO: build a product that matches on category but sells outside the rule's market,
    # assert applies(...) is False.
    ...


@pytest.mark.skip(reason="TODO: implement once src.assess.applies is built")
def test_substance_not_present_is_not_a_gap():
    """A substance-restriction rule must NOT flag a product that doesn't contain it."""
    # TODO: product in the right category but without the named substance -> not applicable.
    ...


@pytest.mark.skip(reason="TODO: implement once src.assess.has_gap is built")
def test_agrees_with_compliance_status_ground_truth():
    """For a company carrying compliance_status.known_gaps, the assessment must agree."""
    # TODO: load a compliance_status company from data/partners.json and assert the known
    # gap is detected.
    ...
