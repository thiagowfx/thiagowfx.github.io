---
title: "Google Gemini: read CLAUDE.md or AGENTS.md"
date: 2025-11-17T12:36:41-03:00
tags:
  - dev
---

**Problem statement**: Make Google's [Gemini](https://gemini.google.com/) read
[`CLAUDE.md`](https://www.anthropic.com/engineering/claude-code-best-practices)
and/or [`AGENTS.md`](https://agents.md). By default, it reads only
[`GEMINI.md`](https://geminicli.com/docs/cli/gemini-md/).

Update `~/.gemini/settings.json` to either:

```json
{
  "contextFileName": "AGENTS.md"
}
```

or

```json
{
  "contextFileName": "CLAUDE.md"
}
```

[My config](https://github.com/thiagowfx/.dotfiles/commit/c57b414d3daa1f8b931b3213f0d6c7904a31d93f):

```json
{
  "contextFileName": "CLAUDE.md",
  "security": {
    "auth": {
      "selectedType": "gemini-api-key"
    }
  },
  "ui": {
    "theme": "Default"
  }
}
```

Why not use `GEMINI.md`? Claude Code provides, by far, a superior experience[^1].
Either way, [`AGENTS.md`](https://agents.md) is the closest to becoming a
standard.

It is unfortunate[^2] that `Claude Code` does [not
yet](https://github.com/anthropics/claude-code/issues/6235) support `AGENTS.md`.
[One file](https://xkcd.com/927/) to rule them all would have been the best.

Alternatively, we could symlink `GEMINI.md` to one of the aforementioned files:

```shell
ln -s AGENTS.md GEMINI.md
```

or

```shell
ln -s CLAUDE.md GEMINI.md
```

...but that needs to be repeated in each repository, whereas the `settings.json`
change is global.

**Update(2025-11-17)**: Even better, as per
[docs](https://geminicli.com/docs/cli/configuration/#available-settings-in-settingsjson):

```json
{
  "contextFileName": [
      "AGENTS.md",
      "CLAUDE.md",
      "GEMINI.md"
  ]
}
```

> contextFileName (string or array of strings):

**Corollary**: It still pays to [RTFM](https://en.wikipedia.org/wiki/RTFM)
directly, even in the LLM era.

Once you launch `gemini` with this config, it gets automatically updated to:

```json
{
  "context": {
    "fileName": [
      "AGENTS.md",
      "CLAUDE.md",
      "GEMINI.md"
    ]
  },
}
```

...which suggests it to be the canonical form[^3].

We know it works because, upon launching `gemini` within a repository that
contains `CLAUDE.md`, it displays `Using: 1 context file`.

[^1]: Citation needed? This statement comes from experience. Or _personal
    vibes_, if you will.
[^2]: And likely intentional, as it would be trivial to support it.
[^3]: They aren't great at updating [their own
    docs](https://geminicli.com/docs/cli/configuration/#available-settings-in-settingsjson),
    eh? This is not yet documented there.
