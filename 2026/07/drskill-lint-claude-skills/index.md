---
title: "drskill: lint claude skills"
url: https://perrotta.dev/2026/07/drskill-lint-claude-skills/
last_updated: 2026-07-28
---


I found drskill through Drew Breunig's post about
[managing an agent's loadout](https://www.dbreunig.com/2026/07/24/manage-your-agent-s-loadout-with-dr-skill.html).

**Problem statement**: lint skills bundled in a Claude Code plugin with
[`drskill`](https://github.com/dbreunig/drskill).

Running it through `uvx` is easy enough:

```shell
% uvx drskill scan --detailed
drskill scan — 3 harnesses (10 more empty), 9 skills
...
0 errors, 5 warnings (5 new) · token counts are approximate
```

But none of this repository's 11 skills appeared. The
[known limitation](https://github.com/dbreunig/drskill#known-limitations) explains
why:

> Claude Code skills bundled inside plugins are not scanned yet.

I projected the plugin's skill directory into the plain `.claude/skills` layout
that drskill understands via `Justfile`:

```just
# Check skills with drskill
doctor:
    #!/usr/bin/env bash
    set -euo pipefail
    tmp=$(mktemp -d)
    trap 'trash "$tmp"' EXIT
    mkdir -p "$tmp/project/.claude/skills" "$tmp/home"
    for skill in "$PWD"/plugins/thiagowfx/skills/*; do
      ln -s "$skill" "$tmp/project/.claude/skills/$(basename "$skill")"
    done
    uv_cache=$(uv cache dir)
    cd "$tmp/project"
    HOME="$tmp/home" UV_CACHE_DIR="$uv_cache" uvx drskill scan --ci --harness claude-code
```

The temporary `HOME` excludes unrelated global skills. Reusing uv's cache avoids
redownloading drskill there. `--ci` makes warnings fail the recipe.

The first isolated scan found four warnings:

```text
drskill scan — 1 harness, 11 skills

WARNINGS
  [e91d] new frontmatter-angle-brackets: 'bloggify' ...
  [a551] new frontmatter-angle-brackets: 'gha' ...
  [6335] new frontmatter-angle-brackets: 'new-apkbuild' ...
  [206e] new missing-activation: 2 skills never say when to use them ...

0 errors, 4 warnings (4 new) · token counts are approximate
exit=2
```

The fixes were small: remove angle brackets from `argument-hint` values and add
explicit activation conditions to `catchup` and `handoff`:

```diff
-argument-hint: "<url>"
+argument-hint: "url"

-description: Create portable handoff document for another agent or harness to continue current work.
+description: Create a portable handoff document for another agent or harness to continue current work. Use when the user asks for a handoff, continuation brief, or context transfer.
```

Now the repository has its own linter:

```shell
% just doctor
drskill scan — 1 harness, 11 skills

No findings.
0 errors, 0 warnings · token counts are approximate
```

Restoring `<url>` temporarily made `just doctor` exit 2 again, so future warnings
will break the check. I should add it to CI at some point.

- - -

🤖 *Drafted with `/bloggify`.*

