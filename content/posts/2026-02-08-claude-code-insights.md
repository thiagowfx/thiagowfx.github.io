---
title: "Claude Code: /insights"
date: 2026-02-08T15:33:50+01:00
tags:
  - ai
  - bestof
  - dev
---

[TIL](https://aiengineerguide.com/blog/claude-code-insights-command/) via Ashik
Nesin:

> Claude Code now has support for /insights commands.
>
> [...]
>
> When you run it, Claude Code will read your message history from the past
> month. It'll summarize your projects, how you use Claude Code, and give
> suggestions on how to improve your workflow.

Let's try it:

```
 ▐▛███▜▌   Claude Code v2.1.37
▝▜█████▛▘  Opus 4.6 · Claude Team
  ▘▘ ▝▝    ~/Workspace/perrotta.dev

❯ /usage
  ⎿  Status dialog dismissed

❯ /insights

⏺ Your shareable insights report is ready:
  file:///Users/thiago.perrotta/.claude/usage-data/report.html

  Want to dig into any section or try one of the suggestions?
```

The generated report is a single self-contained HTML file.

The report is more useful than I anticipated! It's definitely better than
`/stats`: it contains actionable and concrete tips and suggestions to improve
your workflow.

I'll share a snippet of it:

> How You Use Claude Code You are a prolific, infrastructure-focused power user
> who drives Claude Code hard across a wide surface area — 325 sessions, 809
> hours, and 456 commits over roughly 7 weeks. Your workflow centers on
> Terraform infrastructure management, Hugo blog optimization, and DevOps
> tooling (ArgoCD, pre-commit hooks, CI pipelines). You lean heavily on Bash
> (6,780 invocations) as your primary tool, reflecting a hands-on operator style
> where you want Claude executing real commands and seeing real output rather
> than just generating files. Your use of TodoWrite (411 calls) and Task (124
> calls) suggests you frequently tackle complex, multi-step projects — like
> importing existing AWS infrastructure into Terraform or implementing 8+
> performance improvements for your Hugo blog — where structured planning is
> essential. You consistently push for clean git hygiene: granular commits, PRs,
> and proper branch workflows.

> Your interaction style is best described as iterative refinement with active
> course correction. You don't write exhaustive specs upfront; instead, you give
> Claude a clear goal and then steer as it executes. This shows up repeatedly:
> you interrupted Claude when it assumed a full 1Password migration ("only where
> applicable"), caught it when it reverted a change you only asked about
> ("revert. I just asked why"), pushed back on CSS inlining that would lose
> fingerprinting benefits, and redirected heading placement from shortcode
> templates to markdown files. Your friction data tells a consistent story — 24
> instances of wrong approach and 24 of buggy code — but these rarely derail you
> because you catch problems quickly and redirect. You're comfortable letting
> Claude run on multi-file changes (18 successful multi-file operations) but you
> interrupt decisively when the approach is wrong, such as stopping a file write
> to ask about pre-commit integration instead, or killing a premature commit
> attempt.

> What's striking is your high tolerance for iteration paired with low tolerance
> for sloppiness. Terraform import sessions required multiple rounds of fixing
> IDs, resource addresses, and provider syntax — and you stuck with it. But you
> also demanded succinct responses, rejected a poor-quality fullscreen feature
> outright, and expected Claude to understand nuances like provider read-only
> attributes before making sweeping changes. Your 94% achievement rate (32 fully + 15 mostly out of 50) despite working on genuinely hard infrastructure
> problems shows that this iterative, correction-heavy style works well for you.
> You treat Claude as a capable but supervision-required junior engineer — you
> trust it to do the legwork but always review the output critically before
> committing.

> Key pattern: You operate as an active supervisor who assigns complex
> infrastructure tasks, lets Claude execute broadly, but intervenes decisively
> and frequently to correct approach, scope, and quality — treating the tool as
> a capable junior engineer that needs real-time steering.

> Across 325 sessions and 809 hours, you've built a highly productive Claude
> Code workflow centered on infrastructure-as-code, Hugo blog optimization, and
> developer tooling — with a 94% goal achievement rate.

> You've developed a sophisticated pattern for standing up new Terraform
> projects by importing existing AWS and MongoDB Atlas infrastructure, working
> through complex import ID formats and provider quirks across multiple garden
> environments. Your approach of creating files, running plans, and iteratively
> fixing mismatches shows deep Terraform expertise, and you consistently push
> through to clean PRs even when provider limitations surface. The breadth of
> this work — EKS clusters, security groups, MongoDB Atlas modules, Azure OIDC —
> demonstrates you're using Claude as a true infrastructure engineering partner.

> You systematically drove your Hugo blog toward Lighthouse 100 scores through a
> multi-session campaign covering CSS inlining, critical request chain
> elimination, SRI hashes, code block enhancements, and RSS feed fixes. You
> maintained high standards by pushing back when Claude's suggestions sacrificed
> cache fingerprinting or batched too aggressively, ensuring each optimization
> was production-sound. The fact that you also created ADRs documenting your
> architectural decisions around search and caching shows you treat your
> personal blog with the same rigor as production infrastructure.

> You've built a remarkably robust developer experience layer using pre-commit
> hooks, Claude Code settings files, and automation scripts — from custom
> code-block linting parsers to Justfile safety guards that prevent direct
> module applies. You research hooks from other major projects like Airflow to
> cherry-pick the best ones, and you iterate on implementations until they're
> correct (like replacing a regex-based checker with a proper line-by-line
> parser after false positives). Your Claude Code settings PR for your Terraform
> repo, with carefully curated allow/deny/ask permission lists, shows you're
> intentionally shaping how AI tools interact with your codebase.

There's much more to it. I am not sharing actionable suggestions at this time.

There's also negative feedback! And suggestions to improve / augment
`CLAUDE.md`! "New Ways to Use Claude Code"!

I love it. And I definitely need to switch my workflow to writing specs upfront,
though I can't resist an iterative and incremental work style to achieve desired
outcomes 🤔.
