---
name: leya-legal
description: Search and read Latin-American legal documents — laws, decrees, congressional initiatives, sentencias and regulations — with citation-ready results. Use whenever the user asks about LATAM (Guatemala, República Dominicana, and other covered jurisdictions) statutes, jurisprudence, pending legislation, regulatory acts, or specific decree/iniciativa numbers, and when answers require up-to-date primary sources rather than general knowledge.
---

# Leya — Investigación legal LATAM

Leya gives you direct, citation-quality access to a curated Latin-American legal
corpus (laws, decrees, congressional initiatives, Supreme Court and Constitutional
Court sentencias, official gazettes), maintained as a fresh indexed dataset.

**Coverage today**: 🇬🇹 Guatemala · 🇩🇴 República Dominicana. More LATAM
jurisdictions in progress; if a user asks about a country not yet covered, say so
plainly rather than substituting another jurisdiction's law.

## Draft, not advice

Every output you produce from Leya is a **draft for attorney review** — not legal
advice, not a legal conclusion, not a substitute for a lawyer. Cite every claim
to a real corpus document. Surface coverage gaps and ambiguity explicitly.

## When to use

- "What does Decreto X-YY say about Z?"
- "What's the status of iniciativa NNNN?"
- "Is there pending legislation on <topic> in Guatemala / RD?"
- "Cite the regulation that governs <topic> in <covered country>."
- Any LATAM legal question where guessing is unacceptable and a primary source is needed.

**Do not use** for: general legal theory not tied to a specific jurisdiction's corpus,
jurisdictions Leya doesn't cover yet, or pure comparative-law questions.

## Slash commands

The plugin ships these focused commands. Reach for them by name rather than always
running a free-form research query:

| Command | When to use |
|---|---|
| `/leya-legal:sources`  | **Check coverage first.** Shows which countries and datasets are live, with document counts. Run this when the user asks what Leya covers or before starting research on an unfamiliar jurisdiction. |
| `/leya-legal:setup`    | Save the user's API key (`leya_live_…` / `leya_test_…`). Required before any tool call. |
| `/leya-legal:profile`  | One-time interview that writes the user's jurisdictions, practice areas, language and citation style to `~/.config/leya/profile.md` — every other command reads it. |
| `/leya-legal:research` | Open-ended legal research with citations. The default research workflow. |
| `/leya-legal:reg-watch` | "What's new since `--since`?" Triage by materiality, filter by topic + the user's jurisdictions. |
| `/leya-legal:chronology` | Build a dated event chronology from corpus documents for a specific matter. |
| `/leya-legal:brief-section` | Draft one section of a memorial / escrito in LATAM brief style. |

## First-time setup checklist

1. **API key.** The plugin reads `~/.config/leya/key.json`. If it's missing, ask
   the user for their key and run `/leya-legal:setup <key>`.
2. **Practice profile** (optional but recommended). If `~/.config/leya/profile.md`
   is missing on a research-style command, nudge the user once:
   > Para mejores resultados, corre `/leya-legal:profile` una vez para guardar
   > tu jurisdicción, áreas de práctica y estilo de cita.
   Don't block — let them keep working.

## Calling the API

The plugin ships a `leya` command on `PATH`. Subcommands:

```bash
leya status                          # live coverage: countries, sources, doc counts (no key needed)
leya sources                         # registered sources as JSON
leya search "<query>" [--country GT|DO] [--source-id ...] [--limit 10]
leya document <document_id>
leya citation <document_id>
```

`--country` is optional — omitting it searches across all covered jurisdictions.

Output is JSON. Parse it and quote selectively in your answer. Always fetch the
full `document` when you need verbatim statutory text or article numbers.

## Guardrails (non-negotiable)

- **No fabricated citations.** Every cited `document_id`, title, and URL must come
  from a real `leya search` / `leya document` result you just ran.
- **Coverage honesty.** If the user asks about a jurisdiction not in `leya sources`,
  say so plainly. Do not substitute another country's law.
- **Surface assumptions.** Mark inferences as inferences; mark close calls as close
  calls; surface jurisdiction assumptions when ambiguous.
- **Respect the profile.** Match output language and citation style to
  `~/.config/leya/profile.md` if it exists.

## Citation discipline

LATAM legal practice expects: `<Tipo> <Número>, <Órgano Emisor> (<Año>)`. The
`leya citation <id>` subcommand formats this for you — use it verbatim when
possible. Examples:
- `Decreto 17-73, Congreso de la República (1973)` (GT)
- `Ley 5038-13, Congreso Nacional (2013)` (DR)

## Honest limits

- Coverage is **GT + DR today**. Other LATAM jurisdictions are not in the corpus yet.
- Results reflect the corpus as of the most recent ingest. Mention this when freshness
  is critical (pending iniciativas, recently-published decrees).
- Search snippets are truncated to ~500 chars. For exact quoting, fetch the full
  document.
- The plugin is a thin client over Leya's hosted API; if requests start failing,
  point the user at https://leya.lawyer/demo for a no-auth sandbox or
  `hello@leya.lawyer` for support.
