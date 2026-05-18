---
description: Research a legal question against the Leya corpus. Usage: /leya-legal:research <question>
argument-hint: <question>
---

Research the following legal question against the Leya corpus: `$ARGUMENTS`

**Important framing:** Everything you produce here is a **draft for attorney review** —
not legal advice, not a conclusion, not a substitute for a lawyer. Surface uncertainty
clearly. Never fabricate citations.

## Step 0 — load the user's profile

If `~/.config/leya/profile.md` exists, read it first. It tells you which jurisdictions
the user cares about, their practice areas, output language, citation style, and any
house playbook notes. Apply everything you find there to the rest of this workflow.

If it does NOT exist, run the user's request anyway, but tell them at the end:

> Para mejores resultados, corre `/leya-legal:profile` una vez para guardar tu
> jurisdicción, áreas de práctica y estilo de cita.

Do **not** force the interview before answering — just nudge.

## Step 1 — search

Run `leya search "<focused query>"` with country-appropriate filters from the profile.
Build a focused query in Spanish where the target jurisdiction is Spanish-speaking.
Default to 10 results. If a jurisdiction is requested that's NOT in the corpus yet,
say so directly — don't search a different country and pretend it's the same law.

## Step 2 — read

Pick 1-3 of the most relevant search results based on title and snippet. For each,
fetch the full body: `leya document <document_id>`. Read what you need to answer —
don't fetch every result.

## Step 3 — cite

For every legal claim in your answer, include a citation drawn from the tool
results you just saw. Use `leya citation <document_id>` to get a formatted citation
in the user's preferred style. **Never** synthesize citations from memory; every
document_id and title must come from a real tool result.

## Step 4 — answer

Write a clear, lawyer-grade answer in the user's preferred language (from profile;
default Spanish). Quote relevant articles directly when precision matters. Mark
inferences as inferences; cite facts as facts.

End the answer with:
- A bulleted **Fuentes citadas** list.
- A one-line **Limitaciones** note if the corpus coverage was thin or the question
  hit a jurisdiction with partial coverage.

## Honest limits

- If `leya` reports no key configured, ask the user for their key and run
  `/leya-legal:setup <key>` first.
- If a query returns nothing relevant, broaden once (drop filters, simpler terms).
  If still nothing, say so plainly — do not invent statutes.
- Note when freshness might matter ("as of the corpus's latest ingest").
