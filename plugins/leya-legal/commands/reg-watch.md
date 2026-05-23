---
description: Surface new legal developments in the corpus since a date, filtered by topic + materiality. Usage: /leya-legal:reg-watch [--since YYYY-MM-DD] [--topic "<topic>"]
argument-hint: [--since YYYY-MM-DD] [--topic "<topic>"]
---

Run a regulatory / legislative watch over the Leya corpus and produce a digest of what's
new since the user last checked. This is the on-demand equivalent of a scheduled job.

**Draft framing:** Outputs are a triage for the user's review — not a legal opinion on
what each new instrument means.

## Step 0 — load profile

Read `~/.config/leya/profile.md` if it exists. Apply the user's jurisdictions, practice
areas, and language preference. If absent, use the arguments verbatim and nudge the
user toward `/leya-legal:profile` at the end.

## Step 1 — parse arguments

`$ARGUMENTS` may contain `--since YYYY-MM-DD` and/or `--topic "<topic>"`. Defaults:
- `--since`: 7 days ago.
- `--topic`: derive from the profile's practice areas. If neither profile nor topic,
  ask the user once: "What topic should I watch?"

## Step 2 — search per jurisdiction × topic

For each (jurisdiction, topic) pair from the profile, run a focused search:

```bash
leya search "<topic>" --country <JURISDICTION_ISO> --limit 20
```

Filter results to those with `effective_from >= <since>` (or `publication_date >=
<since>` if `effective_from` is null). Discard anything older than `--since`.

## Step 3 — classify by materiality

Group results into three buckets the user will recognize:

- **🔴 ALTA** — new statute, decreto-ley, constitutional ruling that directly touches the
  user's practice area. Surface in full.
- **🟡 MEDIA** — amendment, reglamento, important precedent. Surface with a one-line
  summary and link.
- **⚪ BAJA** — administrative resolution, minor adjustment, mention-only. List as
  one-line bullet.

If a result clearly doesn't fit the user's profile (wrong area / wrong jurisdiction),
drop it silently. Don't pad the digest.

## Step 4 — write the digest

Format:

```markdown
# Resumen regulatorio · <jurisdicción(es)> · <fecha hoy>

> Nuevos desarrollos desde <since>. Filtrado por <topic(s)>.

## 🔴 Alta materialidad
- **<título>** (<source>, <fecha>) — <2-3 líneas: qué cambia, a quién aplica>.
  [fuente](<url>)

## 🟡 Media materialidad
- <título> (<source>, <fecha>): <una línea>. [fuente](<url>)

## ⚪ Baja materialidad
- <título> (<source>, <fecha>). [fuente](<url>)

---

*Borrador para revisión profesional. Verificar la vigencia y aplicabilidad de cada
fuente antes de actuar.*
```

If a bucket is empty, omit the section entirely (don't write "ninguno").

## Coverage honesty

Before running searches, check which jurisdictions are live by running `leya status`.
If the user's profile mentions a jurisdiction not in that list, say so at the top:

> **Cobertura limitada:** Solicitaste seguimiento de [país], pero el corpus de Leya
> aún no lo cubre. Corre `/leya-legal:sources` para ver los países disponibles hoy.

## Tying into recurring jobs (optional)

If the user says "do this every Monday" or similar, point them at the web UI:

> Para correr esto automáticamente todas las semanas, crea una tarea recurrente en
> https://leya.lawyer/jobs/new con el mismo prompt.
