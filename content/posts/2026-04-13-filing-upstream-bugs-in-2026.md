---
title: "Filing upstream bugs in 2026"
date: 2026-04-13T14:33:07+02:00
tags:
  - ai
  - bestof
  - dev
  - serenity
---

First of all, get familiar with some _decent guidelines_ that exist since
forever:

- [XYProblem]({{< ref "2024-06-23-xyproblem" >}})
- [How To Ask Questions The Smart Way](http://www.catb.org/~esr/faqs/smart-questions.html) by ESR (Eric Steven Raymond)
- [ArchWiki: Bug reporting guidelines](https://wiki.archlinux.org/title/Bug_reporting_guidelines)

What is different in 2026? Gen AI / LLMs / Coding agents, of course. Everything
else stays the same.

We don't have to complicate things, I'll start with an example, this is what a
typical decent bug report (or feature request) **should** look like, filed by
yours truly[^1]:

[nikvdp/cco](https://github.com/nikvdp/cco/issues/58) (Claude Code Condom):

> First of all, I [love](https://perrotta.dev/2026/02/cco-claude-condom-sandbox/) `cco`. Thanks for your effort and the good work on it!
>
> Now, to the point: Claude has recently introduced an auto mode: https://claude.com/blog/auto-mode:
>
> > Today, we're introducing auto mode, a new permissions mode in Claude Code where Claude makes permission decisions on your behalf, with safeguards monitoring actions before they run. It's available now as a research preview on the Team plan, and coming to the Enterprise plan and API users in the coming days.
>
> It's supposed to be slightly safer than the YOLO mode (`--dangerously-skip-permissions`).
>
> You can enable and set it with `claude --enable-auto-mode` (or via `settings.json`).
>
> **Feature request**: `cco` should support launching claude in auto mode. Currently it unconditionally launches claude with `--dangerously-skip-permissions`.
>
> Do you think this would be a reasonable addition? If so, I would be happy to give it a try to send a PR (realistically I would prompt Claude to do so).
>
> Side note: the comment above was fully written (manually) by me. Slop notes from Claude come below 🙃:
>
> ⏺ No upstream support exists yet. The repo is [nikvdp/cco](https://github.com/nikvdp/cco) and:
>
> - No issue or feature request for --auto mode support exists across all 25 issues and 33 PRs
> - No PR or commit adding it
> - The script hardcodes --dangerously-skip-permissions in 7 places (both native and Docker backends) with no configuration option
>
> This would be a good feature request to file. The implementation would be straightforward — make the permission mode configurable (e.g. via a --permission-mode flag or CCO_PERMISSION_MODE env var) instead of hardcoding --dangerously-skip-permissions.
>
> Worth noting: Claude Code's --auto mode (aka --permission-mode auto) requires an API-tier plan (Team/Enterprise/API, not Pro or Max) and uses a classifier model to review actions before execution — so it's a meaningful middle ground between full bypass and manual prompts.
>
> Want me to draft an issue for the nikvdp/cco repo?

In no particular order:

- Be [**kind**](https://en.wikipedia.org/wiki/Golden_Rule)[^2]. That cannot be
  understated. No one owes you anything. Leave (self-)entitlement at the door.
- Be **efficient**. Do not waste the maintainer's time. Information should be
  comprehensive/complete yet concise. Keep it simple and short
  ([KISS](https://en.wikipedia.org/wiki/KISS_principle)).
- Be **precise**, reduce room for _ambiguity_ as much as possible. Link to docs
  whenever it makes sense. When linking to docs, be respectful of your peer's
  time and ensure to extract and blockquote relevant snippets so that they don't
  need to dig for it themselves. Furthermore, the links are important for
  verification purposes ([_trust, but verify_](https://en.wikipedia.org/wiki/Trust,_but_verify)).
- Be **proactive**. Offer to help[^3] if you have the know-how and/or expertise
  to do so.
- **Move on**. If you get no reply from the maintainer, do not bug them about
  your bug/FR/PR. Find the next activity to work on. Fork it. Work around it.
  Just don't peg the maintainer to do it for you. This includes code review.

It is much easier if you remember that the maintainer is a person, just like you. Not
a machine. Sounds obvious to state this, but it seems to me many people forget
that, with so much context switching and social media these days...

If you're still reading until this point, chances are that you actually care.
Thank you! Keep it up.

[^1]: Practice what you preach...I am obviously biased though.
[^2]: Or nice. Or polite. Or _sympathisch_.
[^3]: Only if you actually have time to do so. No empty promises, please.
