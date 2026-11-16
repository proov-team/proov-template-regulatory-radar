# Contributing to this project

This is a **solo** ProoV Deep Project — a project of one. There's no team to coordinate,
but there is still one person the history has to be honest to: **you, later**, and the
reviewer reading your certificate. Two habits keep this repo trustworthy.

## 1. Commit as yourself, incrementally

Configure git with your real name and email so the history actually reflects who did the
work:

```bash
git config user.name  "Your Name"
git config user.email "you@example.com"
```

Then commit **as you go** — a string of small, dated commits across your three-week build
is a far more credible record of real work than one commit dumping the whole repo the night
before the deadline. Each commit should do one thing and say what it did
(`add ECHA SVHC fetch + cache`, not `stuff`). A single-commit dump, or a repo whose only
commit is the untouched template, reads from the outside like the work was never actually
done — and it will be graded that way.

This isn't bureaucracy. It's what lets your **Findings & Decisions brief** and your **commit
history** tell the same story. When your brief says "I chose EUR-Lex over scraping ECHA's
HTML because…", there should be a commit where that decision landed.

## 2. Write your Findings & Decisions brief — and own one mistake

Your graded deliverable is **the repo *and* a short brief** (a deck or doc exported to
PDF). The brief is where you take ownership. It must explain, in your own words:

- **Which sources you chose and why** (EUR-Lex? ECHA? EPREL? Safety Gate?).
- **2–3 real gaps you found**, each with the reasoning and the source URL.
- **At least one look-alike you rejected** — a product that looked in-scope but wasn't
  (wrong market, or a substance it doesn't actually contain) — and why you ruled it out.
- **Your key architecture decisions** and **honest limitations** (what's live vs. cached,
  how much of the portfolio you covered).
- **One concrete thing your AI agent got wrong**, or a decision you overrode. This is the
  most important beat. Directing an agent is the skill; catching where it was confidently
  wrong is how you prove you understood the problem, not just prompted it.

A brief that describes work the repo doesn't contain — or a repo whose behaviour the brief
can't explain — is a strong negative signal: it looks like the artifact was generated rather
than genuinely built and understood. Keep the two consistent, and the ownership beat
specific.
