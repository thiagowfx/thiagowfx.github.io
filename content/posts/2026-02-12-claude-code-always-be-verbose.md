---
title: "Claude Code: always be 'verbose'"
date: 2026-02-12T13:37:25+01:00
tags:
  - ai
  - dev
---

**Problem statement**: Claude Code responses have been getting shorter lately.

There's been [discussion on HN](https://news.ycombinator.com/item?id=46978710)
and a [blog
post](https://symmetrybreak.ing/blog/claude-code-is-being-dumbed-down/) about
Claude Code being "dumbed down" with increasingly terse outputs.

Before:
![Claude Code verbose output](https://symmetrybreak.ing/images/dont-worry-about-claude/before.png)

After:
![Claude Code terse output](https://symmetrybreak.ing/images/dont-worry-about-claude/after.png)

Simply add `"outputStyle": "verbose"` to your `.claude/settings.json` to restore
the original behavior:

```diff
diff --git claude/.claude/settings.json claude/.claude/settings.json
index 13a58d2..7f59e73 100644
--- claude/.claude/settings.json
+++ claude/.claude/settings.json
@@ -95,5 +95,6 @@
     "lua-lsp@claude-plugins-official": true,
     "gopls-lsp@claude-plugins-official": true
   },
-  "alwaysThinkingEnabled": true
+  "alwaysThinkingEnabled": true,
+  "outputStyle": "verbose"
 }
```

"Verbose" is misleading in this context.

It sounds like `-vvv` and a firehose of logs and agent thinking traces filling
your terminal screen, but it is not.

As per Boris from the Claude Code team, in the aforementioned HN thread:

> To be clear: we re-purposed verbose mode to do exactly what you are asking
> for. We kept the name "verbose mode", but the behavior is what you want,
> without the other verbose output.

This is a comment for this reply:

> I don't want verbose mode. I want Claude to tell me what it's reading in the
> first 3 seconds, so I can switch gears without fear it's going to the wrong
> part of the codebase. By saying that my use case requires verbose mode, you're
> saying that I need to see massive levels of babysitting-level output (even if
> less massive than before) to be able to do this.

I find it a collective humanity waste of time that a thread like this gathers
600+ comments.

But it's just another day of a poor UX decision for power users.
You address it with a workaround, and then life moves on.
