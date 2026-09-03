---
title: "pi: prompt before dangerous commands"
date: 2026-08-16T13:28:44+02:00
tags:
  - ai
  - bloggify
  - coding
  - dev
  - pi
  - security
---

[Previously]({{< ref "2026-07-28-pi-block-dangerous-commands-syntax-aware" >}}).

**Problem statement**: my Pi extension blocked dangerous shell commands outright,
even when I had already preserved the state they could destroy.

The guard parses every `bash` tool call with tree-sitter, catching commands such
as `rm -rf`, `terraform destroy`, and destructive Git operations. Today it did
exactly what I had asked:

```shell
% git -C "$(brew --repo thiagowfx/pancake)" reset --hard origin/master
git reset --hard is blocked - discards changes irreversibly
```

Blocking remains the right default, but an interactive session can ask me. Pi
extensions can intercept the
[`tool_call` event](https://github.com/earendil-works/pi-mono/blob/main/packages/coding-agent/docs/extensions.md#tool_call)
and open a confirmation dialog through `ctx.ui`.

The change in
[`dangerous-command-guard/guard.ts`](https://github.com/thiagowfx/.dotfiles/commit/b5cb42f8deafae176ecddc12fccbd7c04ca264dd):

```diff
-  pi.on("tool_call", async (event) => {
+  pi.on("tool_call", async (event, ctx) => {
     if (event.toolName !== "bash") return;

     const command = event.input.command;
     if (typeof command !== "string") return;

     const blocked = await findBlockedCommand(command);
-    if (blocked) return { block: true, reason: blocked.reason };
+    if (!blocked) return;
+    if (!ctx.hasUI) return { block: true, reason: blocked.reason };
+
+    const allowed = await ctx.ui.confirm(
+      "Allow dangerous command?",
+      `${blocked.command}\n\n${blocked.reason}`,
+    );
+    if (!allowed) return { block: true, reason: "Blocked by user" };
   });
```

Interactive Pi now pauses for approval. Print and JSON modes have no UI, so they
still fail closed. Safe commands never prompt.

The tests exercise all three decisions:

```text
✔ extension prompts before dangerous bash tool calls (0.66225ms)
ℹ tests 48
ℹ pass 48
ℹ fail 0
```

Same guardrails, with an escape hatch operated by a human rather than a model.
