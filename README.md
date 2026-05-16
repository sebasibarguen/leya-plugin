# Leya — Guatemalan legal research, as a Claude plugin

Search, read, and cite Guatemalan laws, decrees, and congressional initiatives directly from the [Leya](https://leya.gt) corpus, without leaving Claude.

This repository is the public marketplace for the **`leya-legal`** plugin. It works in [Claude Code](https://code.claude.com) and [Cowork](https://claude.com/cowork).

## Install

From inside Claude Code or Cowork:

```
/plugin marketplace add sebasibarguen/leya-plugin
/plugin install leya-legal@leya
```

After installing, run `/reload-plugins` to activate it in the current session.

## First-time setup

You need a Leya API key (looks like `leya_live_…`). Once you have one, configure the plugin:

```
/leya:setup leya_live_your_actual_key_here
```

The key is stored locally in the plugin's data directory with `600` permissions. It is never sent anywhere except the Leya API.

Don't have a key yet? Email **sebas@vana.gt** to request one while we're in private beta.

## What it ships

- **Skill `leya-legal`** — kicks in automatically when you ask Claude about Guatemalan law.
- **`/leya:research <question>`** — one-shot search → read → cite workflow.
- **`/leya:setup <key>`** — save your API key.

All calls go to the public [Leya v1 API](https://leya.gt) over HTTPS with a bearer token.

## License

MIT. See `LICENSE`.
