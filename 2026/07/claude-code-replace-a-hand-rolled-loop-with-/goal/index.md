---
title: "claude code: replace a hand-rolled loop with /goal"
url: https://perrotta.dev/2026/07/claude-code-replace-a-hand-rolled-loop-with-/goal/
last_updated: 2026-07-16
---


[Previously]({{< ref "2026-06-25-claude-code-ship-your-skills-as-a-plugin-marketplace" >}}).

**Problem statement**: one of my skills, `/pr-pass`, was a hand-rolled loop —
push, poll CI, fix a failure, re-push, repeat, bail after five iterations.

It works quite well, and it's one of my most used skills.

That said, recently Claude Code shipped
[`/goal`](https://code.claude.com/docs/en/goal) (in v2.1.139), which is exactly
that loop, packaging it as a primitive. So the skill was reimplementing something
the harness _now_ does natively.

In fact,
[most](https://newsletter.pragmaticengineer.com/p/what-is-loop-engineering)
harnesses ship `/goal` natively these days.

We shall refactor!

`/goal` sets a completion condition. After each turn a fast model checks whether
it holds; if not, Claude starts another turn on its own. It auto-clears once the
condition is met. From the docs:

> The `/goal` command sets a completion condition and Claude keeps working
> toward it without you prompting each step. After each turn, a small fast model
> checks whether the condition holds. If not, Claude starts another turn instead
> of returning control to you.

That deletes three things the old skill hand-built: the `Monitor` poll waiting
on CI state, the "go back to Step 1" loop, and the max-5-iterations guard. The
guard becomes a clause in the condition itself:

```text
/goal every check on this PR has passed (gh pr checks shows no FAILURE
and no PENDING), or stop after 5 turns
```

One catch worth knowing before reaching for `/goal`: the evaluator (tester?) is
a fresh model that **only reads the transcript**. It does not run `gh` or read
files.

> It does not call tools, so it can only judge what Claude has already surfaced
> in the conversation.

So the condition has to be something Claude's own output demonstrates. The skill
now says to paste the `gh pr checks` result into the reply every turn, so the
evaluator has a CI state to judge against. Otherwise the goal would have never
resolved thus it would have looped forever.

Another gotcha: `/goal` doesn't touch permissions. Each turn's `git push`
still prompts unless paired it with [auto
mode](https://code.claude.com/docs/en/auto-mode-config).

The lesson generalizes past this one skill: whenever the harness grows a
primitive, the custom code that predates it becomes technical debt. `/loop`,
Stop hooks, and `/goal` now cover most of the "keep going until X" constructs I
used previously.

- - -

🤖 *Drafted with `/bloggify`.*

