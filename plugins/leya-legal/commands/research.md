---
description: Research a Guatemalan legal question using the Leya corpus. Usage: /leya-legal:research <question>
argument-hint: <question>
---

Research the following Guatemalan legal question using the Leya corpus: `$ARGUMENTS`

Follow this workflow:

1. **Search.** Run `leya search "<focused query>"` to find candidate documents. Build a focused query in Spanish where possible. Default to 10 results — don't ask for more unless the topic is broad.

2. **Read.** Pick the 1-3 most relevant results based on title and snippet. For each, fetch the full body: `leya document <document_id>`. Do not fetch every result — read only what's needed to answer.

3. **Cite.** For every legal claim in your answer, fetch the formatted citation: `leya citation <document_id>` and include it. Never paraphrase Guatemalan law without a citation to the source document.

4. **Answer.** Write a clear, lawyer-grade answer in Spanish (or the user's language if different). Quote relevant articles directly when precision matters. End with a short list of the documents you cited.

Honest limits:
- If the search returns nothing relevant, broaden the query (drop filters, simpler terms). If still nothing, say so plainly — do not invent statutes.
- If `leya` reports no key configured, ask the user for their key and run `/leya-legal:setup <key>` first.
- Note when freshness might matter ("as of the corpus's latest ingest").
