---
title: "bloggify"
url: https://perrotta.dev/2026/06/bloggify/
last_updated: 2026-06-22
---


I've been drawing a line for ages here. My [AI usage]({{< ref
"2024-12-29-ai-usage" >}}) policy, quoting Derek Sivers:

> I have never ever used AI to generate text in place of my "voice". [...]
> nothing claiming to be written by me is written by an AI.

Likewise, I said. Then in ["new blog post via Claude Code"]({{< ref
"2026-02-13-new-blog-post-via-claude-code" >}}) I held the line one more time:
the LLM orchestrates the publishing, but *"everything is still my own text, my
own words. The LLM is not writing the prose."*

The line moved. Slightly. I wrote a `/bloggify` skill whose entire job is to
draft a post in my own style / voice:

```markdown {filename="~/.claude/skills/bloggify/SKILL.md"}
---
name: bloggify
description: Draft a blog post for perrotta.dev in the existing house style.
argument-hint: "<topic or what you want to write about>"
---

Write a blog post about `$ARGUMENTS` for the perrotta.dev blog.
```

The trick is that the style is already written down. The repo has a
[`STYLE.md`](https://github.com/thiagowfx/thiagowfx.github.io/blob/master/STYLE.md)
— derived by reading my own old posts — and the skill just points at it:

> The repo owns the style. **Read `STYLE.md` and `CLAUDE.md` first** — they are
> the source of truth for voice, structure, frontmatter, and conventions.

It scaffolds with `just new`, follows the rules I'd already codified (minimal
frontmatter, bold problem statement, code carries the weight, no "In this post
I will…"), lints with `prek`, and hands back a draft. It does **not** commit.

So: is this still my own words?

Mostly. The skill forbids invented examples — it has to use real commands, real
output, the real artifact. The structure is mine, written down a year ago. The
voice is mine, learned from my old posts. The prose is the machine's impression
of me, and I edit it until it sounds like me again.

The line didn't disappear. It just got *blurrier*.

**I (still) commit to reading the entire post, paragraph by paragraph, and
making manual changes to it to better match my style**.

As of today, it's not clear to me whether this approach will stick.

- - -

🤖 *Drafted with `/bloggify`.*

