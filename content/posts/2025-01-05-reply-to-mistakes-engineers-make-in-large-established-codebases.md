---
title: "Reply to: Mistakes engineers make in large established codebases"
date: 2025-01-05T03:15:47-03:00
tags:
  - dev
---

[Sean Goedecke](https://www.seangoedecke.com/large-established-codebases/):

> The cardinal mistake is inconsistency
>
> There's one mistake I see more often than anything else, and it's absolutely
> deadly: ignoring the rest of the codebase and just implementing your feature
> in the most sensible way. In other words, limiting your touch points with the
> existing codebase in order to keep your nice clean code uncontaminated by
> legacy junk. For engineers that have mainly worked on small codebases, this is
> very hard to resist. But you must resist it! In fact, you must sink as deeply
> into the legacy codebase as possible, in order to maintain consistency.
>
> Why is consistency so important in large codebases? Because it protects you
> from nasty surprises, it slows down the codebase's progression into a mess,
> and it allows you to take advantage of future improvements.
>
> [...]
>
> Consistency is the most important thing. Let me quickly run through some other
> concerns as well, though:

**Consistency, consistency, consistency**. Hell yeah!

Consistency isn't only about [style
guides](https://google.github.io/styleguide/). There's no point in adopting
style guides if they aren't
[enforced](https://abseil.io/resources/swe-book/html/ch03.html).

Consistency is about uniformity. Enforcing invariants. Keeping the codebase tidy
and organized. Whenever done right, even if only in disjoint subsets of the
codebase, it's elegant. It's beautiful. All hail to consistent codebases.

But hey, no one said there's only one way to achieve consistency...

{{< figure align="center" src="https://imgs.xkcd.com/comics/standards.png" link="https://xkcd.com/927/" alt="Fortunately, the charging one has been solved now that we've all standardized on mini-USB. Or is it micro-USB? Shit." attr="XKCD Courtesy of Randall Munroe" >}}
