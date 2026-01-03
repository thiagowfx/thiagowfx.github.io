---
title: "Pipe to Claude"
date: 2025-04-09T17:56:05+02:00
tags:
  - ai
  - dev
  - serenity
---

One of the most effective ways to resolve random software development problems
in 2025:

```shell
{command that emits warnings or errors} | claude
```

`claude` is Anthropic's [Claude
Code](https://docs.anthropic.com/en/docs/agents-and-tools/claude-code/overview)
CLI LLM agent tool:

> Learn about Claude Code, an agentic coding tool made by Anthropic. Currently
> in beta as a research preview.

There is a series of little / simple tasks I've been procrastinating (e.g.
linter issues) that can be quickly resolved with the assistance of a LLM tool.

There's no silver bullet here: all changes need to be properly reviewed and
tested. Nonetheless, even if the tool is wrong 50% of the time, it's still
faster for me to use the LLM tool as an initial suggestion than having to
do the research myself from scratch.
