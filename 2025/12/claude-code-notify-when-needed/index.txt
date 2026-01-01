
This is one little productivity boost to make you a 10x Engineer! None of the
popular AI blogs talk about this!!1!

**Problem statement**: Make Claude Code emit a chime whenever it needs
attention.

```diff
commit e668b387b6b34943143b046ad915effbd3945601
Author: Thiago Perrotta <{redacted}>
Date:   Thu Dec 4 02:33:11 2025 -0300

    add a notification hook

diff --git claude/.claude/settings.json claude/.claude/settings.json
index 1979baf..1ac35da 100644
--- claude/.claude/settings.json
+++ claude/.claude/settings.json
@@ -1,7 +1,20 @@
 {
   "env": {
     "CLAUDE_CODE_ENABLE_TELEMETRY": "0"
   },
+  "hooks": {
+    "Notification": [
+      {
+        "hooks": [
+          {
+            "command": "afplay /System/Library/Sounds/Glass.aiff &",
+            "type": "command"
+          }
+        ]
+      }
+    ]
+  },
```

This is the JSON snippet for ease of copy and paste, you'll add it to your
`~/.claude/settings.json`:

```
"hooks": {
  "Notification": [
    {
      "hooks": [
        {
          "command": "afplay /System/Library/Sounds/Glass.aiff &",
          "type": "command"
        }
      ]
    }
  ]
}
```

This command is for macOS only, but it could be easily adapted to Linux (use
`aplay` instead).

[Claude Code Hooks docs](https://code.claude.com/docs/en/hooks#notification):

> Runs when Claude Code sends notifications. Supports matchers to filter by
> notification type.

macOS ships with various system sounds in `/System/Library/Sounds`.

This inspiration came from [Amp Code](https://ampcode.com/). Amp plays the
`Submarine.aiff` sound by default.

