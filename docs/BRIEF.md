# Challenge brief — Regulatory Radar

> A ProoV **Deep Project**. The interactive briefing on projectstudy.in is ungraded; your
> **grade comes only from the artifact you submit here** — this repo plus a short Findings &
> Decisions brief. This document is the full version of the challenge.

## The setup

A portfolio of **22 electronics SMEs** (53 products — *synthetic and illustrative*) sells
into the EU market. EU product regulations change constantly — new restricted substances,
new labelling and passport rules, tightening deadlines — and a missed one means a fine, a
blocked shipment, or a product delisted and pulled from shelves. Keeping a portfolio like
this compliant is still, in most companies, a **manual loop**: someone reads the
legislation portals, maps each new rule to the affected products by hand, and emails the
owners one by one.

You are the **compliance-automation engineer**. You automate that loop.

## The deliverable — a repo AND a brief

Your graded deliverable has two parts.

### 1. The agent repo (public GitHub)

A working **Regulatory Radar** agent that runs the real-world loop end to end:

```
  FIND ─────────▶ UNDERSTAND ─────▶ ASSESS ────────▶ ALERT
  pull current    LLM extracts      reason over the   one prioritized,
  rules from a    the structured    22-SME portfolio  sourced, actionable
  real source     requirement       for real gaps     notice per gap
```

- **FIND** — pull **current** EU product requirements from **at least one real official
  source** (EUR-Lex, ECHA, EPREL, or EU Safety Gate — see [`data/SOURCES.md`](../data/SOURCES.md)).
  Real ingestion code, committed cached responses, and a recorded access date — **not** just
  a re-read of the bundled example `regulatory_updates.json`.
- **UNDERSTAND** — for each rule, extract its **structured** scope (which product categories
  / substances / markets it covers), its **deadline**, its conditions, and whether it's the
  current in-force version. This is where you direct your AI agent (IBM Bob / Claude Code /
  Cursor / Copilot) to read and extract.
- **ASSESS** — for each SME and product in [`data/partners.json`](../data/partners.json),
  reason from the product's **attributes** (category, substances, battery type, radio,
  markets, intended use…) whether a current requirement **applies**, and whether there's a
  **gap** (an applicable obligation that isn't satisfied). This is the core of the challenge.
- **ALERT** — emit one prioritized, actionable finding per gap in the
  [`sample_expected_output.json`](../data/sample_expected_output.json) shape. A real
  notification channel (email / webhook / console) is a **plus, never required** — contacts
  are synthetic `@example.com`, and you never contact a real person; use your own test
  number or email if you demo a live send.

A runnable **README** ties it together: setup steps, **data attribution** to the real
sources you used, the **not-affiliated / synthetic-portfolio disclaimer**, and an honest
**limitations** section.

### 2. The Findings & Decisions brief (deck or doc → PDF)

A short written brief, exported to **PDF** and uploaded at submit, that explains *your* work:

- Which **sources** you chose and why.
- **2–3 real gaps** you found — each with the reasoning and the **source URL**.
- At least one **look-alike you rejected** — a product that looked in-scope but wasn't — and why.
- Your key **architecture decisions**.
- Honest **limitations**.
- One concrete thing your **AI agent got wrong**, or a decision you overrode (the ownership beat).

The brief must be **consistent with the repo**: a brief describing work the repo doesn't
contain, or a repo whose behaviour the brief can't explain, is a strong negative signal.

## The look-alike trap (read this twice)

The single hardest part of ASSESS is **not over-flagging**. An obligation applies only when
the product's profile actually lands in the rule's scope:

1. **Market** — the company sells where the rule applies (`EU` = all 27 states; some rules
   are one country only).
2. **Category** — the rule covers the product's category (or all electronics).
3. **Substance** — if a rule names a substance, the product actually **contains** it.
4. **Attributes** — battery type/capacity, has-radio, connector, intended use, packaging.
5. **Exclusions** — general consumer-safety rules don't cover medical- or industrial-only
   equipment.

A **look-alike** is a product that matches on one axis but is knocked out on another: the
right category but the **wrong market**; a rule that names a substance the product **doesn't
contain**; a battery-passport rule that hits **LMT/industrial** batteries but **not
portable** ones. Category-only matching flags these as gaps — and is wrong. Reason on
attributes, not category labels.

A few companies carry an explicit **`compliance_status`** block (`certs_held` +
`known_gaps`). Treat those as **ground truth**: your assessment should agree with them. Most
companies have no such block — working out their gaps from the current requirements is the
challenge.

## Milestones

This is a solo, always-on Deep Project on a rolling three-week window. The milestones are
your own check-in cadence (no team, no invite window). Dates are computed per enrollment
from your start date — these are the **checkpoints**, not calendar dates:

1. **Sources chosen + repo scaffolded** — Repo set up from the template; 1–2 official
   sources chosen (EUR-Lex / ECHA / EPREL / Safety Gate); you can fetch and cache one real
   requirement. Report what you set up, what's blocking you, and a commit link.
2. **Extraction + gap assessment on a slice** — Your agent extracts a structured
   requirement from a real source and flags at least one real gap against a portfolio
   company, source cited. Report what works, and a tricky look-alike you handled.
3. **Repo + brief ready for review** — Findings emit in the expected shape with prioritized
   alerts; your brief documents sources, real gaps, look-alikes rejected, architecture,
   honest limits, and one thing your agent got wrong. Link the drafts.

## Data & sources

**The portfolio (`data/partners.json`)** is **synthetic and illustrative** — 22 fictional
electronics SMEs, 53 products, every contact an `@example.com` placeholder. Each product
carries the attributes you reason about: `category`, `substances`, `has_battery` +
`battery_type` + `battery_capacity_wh`, `has_radio`, `connector`, `packaging`,
`intended_use`, `markets`, and `compliance_streams`. See `data/taxonomy.json` for the
controlled vocabulary and `data/SOURCES.md` for the full data dictionary and the
regulation-family reference. This data is generated by a maintainer script and is
intentionally fictional; it must not be treated as a record of any real company.

**The regulations** you assess against are **real and public**. Pull current requirements
from the official sources listed in [`data/SOURCES.md`](../data/SOURCES.md) — EUR-Lex, ECHA,
EPREL, national EPR registers, EU Safety Gate — under **nominative fair use**, and **cite
the URL** for every gap. Respect `robots.txt` and rate limits, cache what you pull, and
record the access date.

## Fair use & integrity

This is an independent, ProoV-owned educational case study. It is **not affiliated with,
endorsed by, or sponsored by** any regulator, agency, or company; the SME portfolio is
fictional. **IBM Bob** is a recommended AI coding tool, mentioned nominatively; this project
is not affiliated with IBM. Your certificate claims only what your **repo and brief**
demonstrate.
