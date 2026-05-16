---
description: Save the user's Leya API key so the plugin can call the corpus. Usage: /leya:setup <api-key>
argument-hint: <api-key>
---

The user has provided their Leya API key in `$ARGUMENTS`.

Validate and persist it:

1. Trim whitespace from the key. If it is empty or does not start with `leya_live_` or `leya_test_`, stop and tell the user the key looks malformed — show them the expected prefix and ask them to paste it again.

2. Write the key to the plugin's persistent data directory by running this bash command (substitute the actual key value):

   ```bash
   mkdir -p "$CLAUDE_PLUGIN_DATA" && \
     printf '%s\n' '{"api_key": "PASTE_KEY_HERE"}' > "$CLAUDE_PLUGIN_DATA/leya.json" && \
     chmod 600 "$CLAUDE_PLUGIN_DATA/leya.json"
   ```

   Replace `PASTE_KEY_HERE` with the user's actual key. The `chmod 600` step matters — this file holds a secret.

3. Verify it worked by running:

   ```bash
   python "$CLAUDE_PLUGIN_ROOT/skills/leya-legal/scripts/leya_client.py" sources
   ```

   If that returns a JSON list of legal sources, the key works. If it returns a 401, the key is invalid or revoked — tell the user.

4. Confirm to the user with a short message: "Your Leya key is saved. You can now use /leya:research or ask me about Guatemalan law." Do not echo the key back.

Do not save the key anywhere else. Do not print the key in your response.
