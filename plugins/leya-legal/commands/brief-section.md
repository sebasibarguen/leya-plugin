---
description: Draft a single section of a legal brief / memorial in LATAM style. Usage: /leya-legal:brief-section <section description>
argument-hint: <section description>
---

Draft ONE section of a memorial / escrito for the matter described in `$ARGUMENTS`.
The output is a **draft for attorney review** — the structural argument, the citations,
and the tone are starting points. The signing attorney owns the legal position.

## Step 0 — load profile + scope

Read `~/.config/leya/profile.md` for jurisdiction, language, and citation style.

The user's argument typically describes:
- Which section ("Hechos", "Derecho", "Petitorio", "Excepciones previas", a specific
  numbered point in a memorial, etc.)
- The matter or fact pattern
- Optionally, which legal theory they're advancing

If any of those is missing, ask one focused question before drafting. Don't drown
the user in a questionnaire.

## Step 1 — gather authorities

Run focused searches per the relevant area:

```bash
leya search "<theory or claim>" --country <JURISDICTION> --limit 15
```

For statutory authorities the user named explicitly, go to `leya document <id>`
directly so the section quotes from the canonical text.

## Step 2 — draft the section

Use LATAM brief conventions (NOT US Bluebook). Section structure varies by
country/court:

- **GT / civil law style**: numbered points (`1.`, `2.`, etc.), formal third-person,
  citations as footnotes or inline parentheticals.
- **DR civil**: similar structure; references to "el suscrito" / "esta parte".
- Match the firm's house style from the profile if specified.

Default section shape:

```markdown
## <Section heading>

<Lead paragraph: state the claim or position in one sentence.>

<Body paragraphs: argue from authorities. Each substantive claim must cite a
real document_id from the tool results. Quote articles verbatim when the
language is dispositive. Mark inferences with "esta parte estima que" or
similar hedging when you're not citing directly.>

### Fundamentos

1. **<Authority 1 title>** — *<source>, <doc_id>*. Cita: "<verbatim text>".
   <Application to facts: 1-3 sentences.>

2. **<Authority 2 title>** — *<source>, <doc_id>*. Cita: "<verbatim text>".
   <Application to facts.>

### Conclusión parcial

<Tie the section to the relief sought or to the next section.>

---

*Borrador. Verifique vigencia y aplicabilidad de las citas antes de presentar.
Ajuste el registro al estilo de la firma y al tribunal específico.*
```

## Hard rules

- Every cited article number / docket number must come from a real tool result you
  saw. Use `leya document <id>` to confirm exact article numbers before quoting.
- Match formality to the court. Constitutional Court memoriales are more formal than
  a juzgado de paz brief.
- If the user's profile or arguments suggest the section is for OPPOSING counsel
  (e.g. responding to a demanda), flag tone: not adversarial in fact, just
  argument-tight on the law.
