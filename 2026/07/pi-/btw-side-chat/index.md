---
title: "pi: /btw side-chat"
url: https://perrotta.dev/2026/07/pi-/btw-side-chat/
last_updated: 2026-07-22
---


[Previously]({{< ref "2026-07-22-pi-auto-retry-stalled-requests" >}}).

**Problem statement**: mid-task, I want to ask the LLM agent a quick tangential
question — "will this change cause downtime?" — without polluting the main
agent thread.

Claude Code has `/btw`[^1] for exactly this.
[pi](https://github.com/earendil-works/pi) doesn't, but
[patriceckhart/pi-btw](https://github.com/patriceckhart/pi-btw) does, as an
extension. It opens a side-chat overlay: the LLM gets to see the full main
thread context and answers, but nothing is written back to the conversation
history.

The upstream extension imports the pre-fork `@mariozechner/*` package names,
which are now deprecated. As such, I use
[earendil-works/pi](https://github.com/earendil-works/pi). Rather than trust a
diff I hadn't read, I reimplemented it against the current API, and
cross-checked against the bundled `examples/extensions/summarize.ts` (the
canonical example for calling the model from an extension):

```typescript
import { complete } from "@earendil-works/pi-ai/compat";
import type { ExtensionAPI, SessionEntry } from "@earendil-works/pi-coding-agent";
import { convertToLlm, getMarkdownTheme } from "@earendil-works/pi-coding-agent";

// ...inside the /btw command handler, once at entry:
const branch = ctx.sessionManager.getBranch();
const mainMessages = branch
  .filter((entry): entry is SessionEntry & { type: "message" } => entry.type === "message")
  .map((entry) => entry.message);
const mainLlmMessages = convertToLlm(mainMessages);   // frozen snapshot
const systemPrompt = ctx.getSystemPrompt();

// ...per question, the side-chat calls the model directly:
const response = await complete(
  ctx.model!,
  { systemPrompt, messages: [...mainLlmMessages, ...btwLlmMessages] },
  { apiKey: auth.apiKey, headers: auth.headers, env: auth.env, signal },
);
```

The key move is what's *missing*: the handler never calls `pi.sendMessage()`
or appends anything. It reads the branch once, talks to the model in an
[`ctx.ui.custom()`](https://github.com/earendil-works/pi/blob/main/packages/coding-agent/docs/extensions.md#custom-ui)
overlay, and returns. The main session is untouched, so the next real prompt
doesn't pay for any of it.

Added to [`~/.pi/agent/extensions/btw.ts`](https://github.com/thiagowfx/.dotfiles/blob/1f42eb6f6632f946c23d1278e7e3f18da78d5de8/pi/.pi/agent/extensions/btw.ts).

- - -

🤖 *Drafted with `/bloggify`.*

[^1]: I am no longer using [Arch](https://archlinux.org/), btw (sad!)

