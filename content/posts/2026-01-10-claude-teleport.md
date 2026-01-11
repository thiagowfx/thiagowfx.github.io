---
title: "claude --teleport"
date: 2026-01-10T22:26:21-03:00
tags:
  - ai
  - dev
---

After starting a coding start on the web with [Claude Code on
Web](https://code.claude.com/docs/en/claude-code-on-the-web)[^1], you can [resume it
in the
terminal](https://code.claude.com/docs/en/claude-code-on-the-web#from-web-to-terminal)
with the traditional Claude Code CLI app by running `claude --teleport`.

Without arguments, it prompts you to interactively choose an existing session to
resume.

With a provided session ID argument, the session is immediately resumed.

The docs mention the existence of the `/teleport` command within Claude Code but I
could not find it in my instance (version v2.1.4).

This [workflow](https://xcancel.com/bcherny/status/2007179832300581177) ("start
on your phone, resume later on your computer afterwards") is starting to become
popularized.

[^1]: https://claude.ai/code
