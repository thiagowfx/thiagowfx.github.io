---
title: "Amp Code: queue/unqueue messages"
url: https://perrotta.dev/2026/01/amp-code-queue/unqueue-messages/
last_updated: 2026-02-22
---


When using [Amp Code](https://ampcode.com/) (a CLI coding agent), sending two
messages in a row results in the second message interrupting the first.

Most other agents (e.g. Claude Code, OpenAI Codex, Google Gemini) support
message queueing by default, wherein the second message "waits" until the first
prompt is complete.

To achieve the same behavior in `amp`, use `/queue`. There's also `/dequeue` to
undo it.

