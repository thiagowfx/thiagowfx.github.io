---
title: "dual-review: address review findings automatically"
url: https://perrotta.dev/2026/08/dual-review-address-review-findings-automatically/
last_updated: 2026-08-16
---


[Previously]({{< ref "2026-06-25-claude-code-ship-your-skills-as-a-plugin-marketplace" >}}).

My
[`dual-review`](https://github.com/thiagowfx/skills/blob/master/plugins/thiagowfx/skills/dual-review/SKILL.md)
skill runs two independent LLM reviewers over a commit / diff / PR, validates
every finding against the code, and hands back one action plan — Blockers,
Important, Suggestions.

Recently I added a flag argument that closes the loop:

```diff
 argument-hint: "[branch|staged|all] [--pr NUMBER] [--post]"
+argument-hint: "[branch|staged|all] [--pr NUMBER] [--post] [--address]"
```

```diff
 - `--post`: post final action plan to target pull request after showing it; never post otherwise
+- `--address`: after showing (and, if requested, posting) the action plan, fix Blockers and Important findings directly in the reviewed tree; never fix Suggestions without explicit confirmation
```

```diff
+## 7. Address Findings (only with `--address`)
+
+Skip this section entirely unless `--address` was requested.
+
+1. Work in the same tree that was reviewed (existing worktree or user's checkout for `staged`/`all`); never create a second copy of the changes.
+2. Address every Blocker and every Important finding. For Suggestions, ask the user which (if any) to apply; default to none.
+3. For each finding: re-read the exact `file:line` locations, apply the `Fix:` recommendation, and fix every sibling location listed under that finding, not just the first instance.
+4. If a finding is ambiguous, requires a design decision, or the recommended fix turns out to be wrong once you're in the code, stop and ask the user instead of guessing.
+5. After edits, rerun any locally available checks that cover the change (tests, linters, type-checks) before treating a finding as resolved.
+6. Stage only the files touched while addressing findings. Commit with a message describing which findings were fixed (e.g. `address dual-review findings`), listing them briefly in the body.
+7. If scope was `branch`/`--pr`, push to the branch. If the action plan was posted (`--post`), leave a short follow-up comment noting the findings were addressed and pushed; do not repost the full plan.
+8. Report: which findings were fixed, which were skipped and why, and which need user input.
```

The important line is the second one: Suggestions never get auto-applied,
only Blockers and Important.

`/dual-review --post --address` now reviews, posts the plan, fixes
what's fixable, and pushes.

Why two review(er)s instead of one? Because LLMs are non-deterministic.

Why not more than two review(er)s then? Tokens ($$$) and time. It's a balance.

- - -

🤖 *Drafted with [`/bloggify`](https://github.com/thiagowfx/skills/blob/master/plugins/thiagowfx/skills/bloggify/SKILL.md).*

