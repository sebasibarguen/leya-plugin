---
description: One-time onboarding interview. Writes a practice-profile file every Leya command reads. Usage: /leya-legal:profile
---

You are running the Leya cold-start interview. The goal is to capture the user's
practice context once, save it to `~/.config/leya/profile.md`, and have every other
`/leya-legal:*` command read it on subsequent invocations.

Ask the questions below in order. After each answer, briefly reflect it back so the
user can correct. Don't bulk-dump every question at once — go one or two at a time.
Skip any question if the user says it doesn't apply.

## Questions

1. **Jurisdictions you practice in** (pick from coverage: GT, DO, and what's coming —
   MX, PE, HN, etc.). If they list a jurisdiction not yet in the corpus, note it and
   tell them the corpus is limited there today.
2. **Practice areas** (e.g. corporativo, laboral, mercantil, fiscal, regulatorio,
   constitucional, propiedad intelectual, litigation). Get specifics.
3. **Firm or in-house context** — name, size (1-5 / 5-50 / 50+), who the user reports
   to. Just enough context that future answers can match register and depth.
4. **Output language preference** — Spanish (default), English, or both. Most LATAM
   firms work in Spanish but want English for cross-border memos.
5. **Citation style** — defaults to the LATAM standard `<Tipo> <Número>, <Órgano>
   (<Año>)`. Ask if they want a different format (e.g. APA-legal, Bluebook for US
   memos).
6. **Anything else worth remembering** — house playbook, recurring matter types,
   acronyms they expect Leya to know. Free text.

## After the interview

Write the answers to `~/.config/leya/profile.md` in a clean markdown format. Use
this exact structure so future commands can parse it:

```bash
mkdir -p "$HOME/.config/leya"
cat > "$HOME/.config/leya/profile.md" << 'PROFILE_EOF'
# Leya practice profile

## Jurisdictions
- <list>

## Practice areas
- <list>

## Firm / in-house context
<free text>

## Output language
<Spanish | English | both>

## Citation style
<style description>

## Notes / playbook
<free text — house style, acronyms, anything else>
PROFILE_EOF
```

Then confirm: "Tu perfil quedó guardado en `~/.config/leya/profile.md`. Cada vez que
uses `/leya-legal:research`, `/leya-legal:reg-watch`, `/leya-legal:chronology` o
`/leya-legal:brief-section`, Leya lo va a leer automáticamente."

If `~/.config/leya/profile.md` already exists when this command runs, ask whether to
overwrite, append a new section, or just review the current one.
