---
title: "claude code: ship your skills as a plugin marketplace"
date: 2026-06-25T20:40:02+02:00
tags:
  - ai
  - bestof
  - coding
  - dev
---

**Problem statement**: my Claude Code
[skills](https://code.claude.com/docs/en/skills) lived in my
[.dotfiles](https://github.com/thiagowfx/.dotfiles), usable only on the machine
that cloned them. I wanted them to be installable anywhere with one command, so
that (for example) my teammates could easily adopt them.

Claude Code reads skills from a marketplace, which is essentially a git repo
with a manifest. So I turned `github.com/thiagowfx/skills` into one. The layout:

```
.claude-plugin/marketplace.json    # marketplace manifest
plugins/skills/                    # one plugin
  .claude-plugin/plugin.json       # plugin manifest
  skills/<name>/SKILL.md           # one dir per skill (auto-discovered)
```

The marketplace lists plugins; a plugin bundles skills. I have one plugin
holding all nine. I do not find it necessary to have multiple plug-ins at this
point. `marketplace.json` points at it with a relative `source`:

```json
{
  "name": "thiagowfx",
  "owner": { "name": "Thiago Perrotta", "url": "https://github.com/thiagowfx" },
  "plugins": [
    {
      "name": "skills",
      "source": "./plugins/skills",
      "description": "Thiago's personal Gen-AI / Claude Code skills."
    }
  ]
}
```

The plugin manifest is just metadata — there's no need to enumerate skills.
Anything under `skills/<name>/SKILL.md` is discovered automatically:

```json
{
  "name": "skills",
  "version": "0.1.0",
  "license": "MIT"
}
```

The docs are explicit about why I keep that `version`:

> Setting `version` means users only receive updates when you change this field, so
> bump it on every release. If you omit `version` and host this marketplace in git,
> every commit automatically counts as a new version.

I'll go with version pinning for now.

Install from any machine:

```shell
/plugin marketplace add thiagowfx/skills
/plugin install skills@thiagowfx
```

`/plugin marketplace update thiagowfx` pulls future changes.

The whole thing — manifests, nine seeded skills, README, license — was
scaffolded by Claude Code itself, which felt appropriately recursive: one of the
skills I was packaging interviews me about a plan before any code gets written,
so it [grilled
me](https://github.com/thiagowfx/skills/blob/71467dbc4f9d2cfae273a52eeab71f2cdc37f3bc/plugins/skills/skills/grill-me/SKILL.md)
about how to package the skills. Quite meta, eh?

**Next up**: point the dotfiles at the repo so there's a single source of truth.

- - -

🤖 *Drafted with `/bloggify`.*
