---
title: "claude code: kitty keyboard protocol garbage"
date: 2026-03-25T14:15:27+01:00
tags:
  - ai
  - dev
---

Upon quitting [Claude Code](https://claude.ai/claude-code), pressing `C-c`
in the terminal produces garbage like this instead of the expected `^C`:

```
❯ 0;5u9;5u0;5uc9;5u9;5u9;5u9;5u9;5u
```

Something similar happens with `C-a`, `C-e`, `C-l`, etc. I am using `zsh`.

## What's happening

Claude Code enables the [kitty keyboard
protocol](https://sw.kovidgoyal.net/kitty/keyboard-protocol/) ("CSI u mode") for
enhanced key input handling. Whenever the program exits cleanly, it restores the
terminal to its original state. However, if the cleanup doesn't fully complete
(crash, `SIGKILL`, etc.), the terminal remains in `CSI u` mode.

In this mode, keypresses are sent as escape sequences rather than being
interpreted by the shell. For example, `Ctrl-C` sends `\e[99;5u` (keycode 99 =
`c`, modifier 5 = Ctrl) instead of being interpreted as `SIGINT`. Multiple rapid
keypresses concatenate into the garbled output above.

## Fix

Reset the terminal:

```sh
reset
```

Or, more targeted — disable `CSI u` mode explicitly:

```sh
printf '\e[<u'
```

...though no one can remember this. `reset` is standard and simple, though it
could be easily confused with `clear`.

## Prevention

Add a `precmd` hook to `~/.zshrc` so the protocol is disabled before every
prompt:

```zsh
precmd() { printf '\e[<u' 2>/dev/null }
```

For bash, use `PROMPT_COMMAND` instead:

```bash
PROMPT_COMMAND='printf "\e[<u" 2>/dev/null'
```

> This is a no-op when the terminal is already in normal mode, so there's no
downside to having it always run.

This is what Claude says, but I'd rather not clutter my `precmd` due to Claude.
For now, I am happy to run `reset` manually when needed.

I suspect this is well-known but they have [many open
bugs](https://github.com/anthropics/claude-code/issues?q=is%3Aissue%20state%3Aopen%20kitty)
in their GitHub issue tracker, I couldn't pinpoint it to a specific issue.

**Update**: well, someone reported it just [5 minutes
ago](https://github.com/anthropics/claude-code/issues/38761) at the time of this
post.
