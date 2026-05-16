---
name: leya-legal
description: Search and read Guatemalan legal documents — laws, decrees, congressional initiatives (iniciativas), and regulations — with citation-ready results. Use whenever the user asks about Guatemalan (GT) statutes, jurisprudence, pending legislation, regulatory acts, or specific decree/iniciativa numbers, and when answers require up-to-date primary sources rather than general knowledge.
---

# Leya — Guatemalan Legal Research

Leya gives you direct, citation-quality access to the Guatemalan legal corpus
(congressional initiatives, laws, decrees, regulations) maintained as a fresh,
indexed dataset.

## When to use

- "What does Decreto X-YY say about Z?"
- "What's the status of iniciativa NNNN?"
- "Is there pending legislation on <topic> in Guatemala?"
- "Cite the GT regulation that governs <topic>."
- Any GT legal question where guessing is unacceptable and you need a primary source.

**Do not use** for: general legal theory, non-GT jurisdictions (not covered yet),
or questions that are clearly about international/comparative law.

## First-time setup

The plugin reads the user's Leya API key from `~/.config/leya/key.json`. If
you try to call the API and get an error about a missing key:

1. Ask the user for their Leya API key (it looks like `leya_live_...` or `leya_test_...`).
2. Run `/leya-legal:setup <their-key>` to save it.
3. Then retry their original request.

Never proceed without a key — fail loud, not silent.

## Calling the API

The plugin ships a `leya` command on `PATH`. Four subcommands map 1:1 to the v1 API:

```bash
leya sources
leya search "<query>" [--country GT] [--source-id ...] [--limit 10]
leya document <document_id>
leya citation <document_id>
```

Output is JSON. Parse it and quote selectively in your answer.

## Recommended workflow

1. **Search first** with a focused query (Spanish preferred). 5-10 results is plenty.
2. **Read 1-3 documents** in full with `leya document <id>` when you need actual statutory text.
3. **Cite** every legal claim with the `leya citation <id>` output. Never paraphrase GT law without a citation.
4. If a query returns nothing relevant, **broaden** before giving up. If still nothing, say so plainly — do not invent statutes.

## Citation discipline

GT legal practice expects citations to include document type, number, issuing body, and year. The `citation` subcommand formats this for you; use it verbatim when possible. Manual fallback:

`<Tipo> <Número>, <Órgano Emisor> (<Año>)`

Example: `Decreto 17-73, Congreso de la República (1973)`

## Honest limits

- Coverage is GT-first. Other jurisdictions are not in the corpus yet.
- Results reflect the corpus as of the most recent ingest. Mention this when freshness is critical.
- Search snippets are truncated. For exact quoting, fetch the full document.
