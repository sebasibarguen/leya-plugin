---
description: Show which countries and datasets are currently available in the Leya corpus. Usage: /leya-legal:sources
---

Show the user which countries and legal sources are live in the Leya corpus right now, with current document counts.

## Step 1 — fetch live status

Run:

```bash
leya status
```

This calls the public status endpoint (no API key required) and returns per-source data including `total_indexed`, `last_run_status`, and `last_run_at`.

If `leya status` fails (network error), fall back to:

```bash
leya sources
```

which returns source metadata without document counts.

## Step 2 — format the output

Present the results grouped by country as a markdown table:

```
## Cobertura del corpus Leya

| País | Fuente | Documentos | Estado |
|------|--------|-----------|--------|
| 🇩🇴 DO | Tribunal Constitucional | 6,314 | Al día |
| 🇩🇴 DO | Suprema Corte de Justicia | 10 | Al día |
| ...  | ...    | ...       | ...    |
```

Status badge mapping:
- `no_new` or `success` with 0 new → "Al día ✓"
- `success` with docs_added > 0 → "Actualizado (+N docs)"
- `error` → "⚠ Error"
- `null` (no cron run yet) → "–"

After the table, add:

> **Cómo usar:** `/leya-legal:research <pregunta>` para investigar en cualquiera de estas fuentes.
> Para ver el detalle completo del corpus: https://leya.lawyer/status

## Coverage honesty

If the user asked about a country that doesn't appear in the table, say so clearly:

> El corpus de Leya aún no cubre [país]. Las jurisdicciones disponibles hoy son las de la tabla arriba.
> Puedes solicitar cobertura de nuevos países en hello@leya.lawyer.
