[![ProoV](https://img.shields.io/badge/ProoV-Project-0D9488)](https://goproov.com)

# Regulatory Radar — Build the Compliance Agent That Never Sleeps

This repository is the starting point for a **ProoV Deep Project**. You are the
compliance-automation engineer for a portfolio of electronics SMEs. EU product rules
change constantly, and a missed one means a fine or a blocked shipment. Your job is to
build **Regulatory Radar**: an AI agent that pulls the current requirements from official
sources, works out which products are non-compliant today, and raises a prioritized,
sourced alert for each gap.

## About this ProoV project

This is a real, company-grade challenge from ProoV — an independent virtual
work-experience platform. Read the full brief on
[goproov.com](https://goproov.com/explore/experience-regulatory-radar), and the
detailed version in [`docs/BRIEF.md`](docs/BRIEF.md).

> **Not affiliated / illustrative.** This is an independent, ProoV-owned educational case
> study. It uses **public official sources** (EUR-Lex, ECHA, EPREL, EU Safety Gate) under
> nominative fair use, and it is **not affiliated with, endorsed by, or sponsored by** any
> regulator, agency, or company. The SME portfolio in `data/partners.json` is **synthetic
> and illustrative** — every company is fictional and every contact is an `@example.com`
> placeholder, so a test alert never reaches a real person. **IBM Bob** is a recommended AI
> coding tool; this project is not affiliated with IBM.

## What a strong submission looks like

A strong submission actually pulls **current** EU requirements from at least one **real
official source** — with ingestion code that targets a real endpoint or page, committed
cached responses, and a recorded access date — not just a re-read of the bundled example
`regulatory_updates.json`. It **extracts each rule as structured data** (which product
categories, substances and markets it covers; its deadline; whether it's the in-force
version), then **reasons from product attributes** to decide, for every company and
product, whether the rule *applies* and whether there's a *gap*.

The hard part is the judgment. A strong submission **rejects look-alikes** — the right
category but the wrong market or a substance that isn't actually present is **not** a gap —
and it **agrees with the ground-truth companies** that carry an explicit `compliance_status`
in the data. Every reported gap **cites a real, resolvable source URL**. Findings come out
in the [`sample_expected_output.json`](data/sample_expected_output.json) shape (company ·
product · regulation · source_url · gap · deadline · severity · recommended_action ·
alert), prioritized by deadline and severity, and each alert reads like a notice a
compliance officer could act on.

The repository itself is honest: a clean module structure, a runnable README with **data
attribution** and the **not-affiliated disclaimer**, some tests, and an honest
**limitations** section (what's live vs. cached, how much of the portfolio and how many
regulations you actually covered). Alongside it you write a short **Findings & Decisions
brief** (exported to PDF) that explains *your* choices, the real gaps you found, at least
one look-alike you rejected and why, and one concrete thing your AI agent got wrong that
you had to override.

A hollow submission does the opposite: it only reads the bundled example JSON, matches on
category alone (so it flags look-alikes), skips citations, ships thin or no tests, and
over-claims in the README.

## Your build log

This is a **solo** Deep Project — a project of one. Use this table as a personal build log
so your commit history and your brief tell the same story. Fill it in as you go; it's the
README-side mirror of the contribution statement ProoV collects when you submit.

| Date | What I built | Evidence (commit / file) |
|---|---|---|
| _e.g. 2026-07-06_ | _Repo scaffolded from template; chose EUR-Lex + ECHA as sources_ | _`abc1234`_ |
| | | |
| | | |

## Getting started

This is a Python project. From the repo root:

```bash
# 1. Create and activate a virtual environment
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the (stubbed) pipeline end to end
python -m src.ingest             # FIND  — pull current rules from a real source
python -m src.extract            # UNDERSTAND — LLM-extract structured requirements
python -m src.assess             # ASSESS — find gaps against data/partners.json
python -m src.alert              # ALERT — emit prioritized findings + messages
```

The four `src/` modules ship as **stubs with docstrings and `TODO`s** — the build is
yours. Point your AI coding agent at them and work module by module.

### Where your starting data lives

Everything you need to start is in [`data/`](data/):

| File | What it is |
|---|---|
| `data/partners.json` | The **synthetic** SME portfolio — 22 companies, 53 products. This is your fixed input; you assess it. A few companies carry a `compliance_status` block (ground truth). |
| `data/taxonomy.json` | Controlled vocabulary — product categories, substances, regulation families. |
| `data/SOURCES.md` | The curated list of **real official sources** to pull current rules from. **Start here for the FIND step.** |
| `data/sample_expected_output.json` | The exact shape of one finding your agent should emit. |

Findings your agent produces go in [`findings/`](findings/) (git-tracked, so your emitted
output is part of the submission). Your written brief lives in [`docs/`](docs/) — see
[`docs/BRIEF.md`](docs/BRIEF.md).

### Pointing your AI coding agent at it

You direct an AI coding agent — **IBM Bob** (30-day student access:
`https://ibm.biz/student-bobathon`), **Claude Code**, **Cursor**, or **Copilot** — to build
the pipeline *with* you. A good first move is to open the repo in your agent and ask it to
read `README.md`, `docs/BRIEF.md`, and `data/SOURCES.md`, then help you design the FIND →
UNDERSTAND → ASSESS → ALERT loop. You stay the engineer: you decide the sources, you check
the gap logic, and you own the result. See [`CONTRIBUTING.md`](CONTRIBUTING.md) for the
one habit that keeps your submission honest.

---

*Built as a ProoV Deep Project · case study on EU electronics-product compliance · public
official sources under nominative fair use · synthetic portfolio, not affiliated with any
regulator or company.*
