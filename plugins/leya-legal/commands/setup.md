---
description: Save the user's Leya API key so the plugin can call the corpus. Usage: /leya-legal:setup <api-key>
argument-hint: <api-key>
---

The user has provided their Leya API key in `$ARGUMENTS`.

Validate and persist it:

1. Trim whitespace from the key. If it is empty or does not start with `leya_live_` or `leya_test_`, stop and tell the user the key looks malformed — show them the expected prefix and ask them to paste it again.

2. Write the key to `~/.config/leya/key.json` by running this bash command (substitute the actual key value for `PASTE_KEY_HERE`):

   ```bash
   mkdir -p "$HOME/.config/leya" && \
     printf '%s\n' '{"api_key": "PASTE_KEY_HERE"}' > "$HOME/.config/leya/key.json" && \
     chmod 600 "$HOME/.config/leya/key.json"
   ```

   The `chmod 600` step matters — this file holds a secret.

3. Verify it worked by running:

   ```bash
   leya sources
   ```

   If that returns a JSON list of legal sources, the key works. If it returns a 401, the key is invalid or revoked — tell the user.

4. Confirm with a short message: "Your Leya key is saved. You can now use /leya-legal:research or just ask me about Guatemalan law." Do not echo the key back.

Do not save the key anywhere else. Do not print the key in your response.
