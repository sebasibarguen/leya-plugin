---
description: Build a dated chronology of events for a matter from corpus documents. Usage: /leya-legal:chronology <matter description>
argument-hint: <matter description>
---

Build a dated chronology for the matter described in `$ARGUMENTS`. The output is a
**draft for attorney review** — order, dates, and characterizations are starting points
the lawyer must verify.

## Step 0 — load profile

Read `~/.config/leya/profile.md` if it exists. Apply jurisdiction, language, and
citation style.

## Step 1 — gather relevant documents

The matter description usually names parties, an event window, statutes, or a
docket / iniciativa number. For each named hook, run a search:

```bash
leya search "<hook>" --country <JURISDICTION> --limit 10
```

When the user names a specific document_id, statute number, or iniciativa number,
go straight to `leya document <id>`.

## Step 2 — extract dated events

For each document you fetch, extract every event with a real date attached:
- Statute promulgation / publication / entry into force
- Court filings, hearings, rulings, appeals
- Contract signings, amendments, terminations, notices
- Administrative resolutions, regulator letters

Discard:
- Events without a date.
- Events from documents not in this matter.

Each event row is `(YYYY-MM-DD, actor, action, source_document_id)`.

## Step 3 — render the chronology

Output a clean markdown table sorted ascending by date:

```markdown
# Cronología — <matter title>

> Construida a partir de <N> documentos del corpus. Borrador para revisión.

| Fecha | Actor | Acción | Fuente |
|---|---|---|---|
| YYYY-MM-DD | <actor> | <acción en una línea> | <título corto> ([<doc_id>](<url>)) |
| ... | ... | ... | ... |

---

## Lagunas / verificar
- <Anything where the doc was ambiguous about the date>
- <Any gap between two events that suggests a missing filing>

*Las fechas y caracterizaciones provienen de los documentos citados; el abogado
responsable debe verificar contra el expediente físico antes de usar esto en
audiencia o en una opinión.*
```

## Honesty rules

- Never invent a date. If the document says "en el mes de marzo" without a day,
  log it as `YYYY-03-??` and flag it in the gaps section.
- Never invent an actor. Pull names verbatim from the document.
- If two events from different sources conflict, list both rows and flag the
  conflict in the gaps section. Don't pick a winner.
