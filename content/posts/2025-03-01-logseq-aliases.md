---
title: "Logseq: aliases"
date: 2025-03-01T15:55:20+01:00
tags:
  - pkm
---

In [Logseq](https://logseq.com/), I have an entry called "Trips".

In a topic in my daily note, I want to use the `#trip` tag to link to it.

However, `#trip` links to a distinct page, called "Trip".

**Problem statement**: How can we "merge" the two entries, effectively treating
them as one?

Use [aliases](https://unofficial-logseq-docs.gitbook.io/unofficial-logseq-docs/beginner-to-advance-features/aliases):

In "Trips", in the very first bullet point, type `::alias`. The
auto-completion pops up. Type in "trip".

That's all. Linking with `[[trip]]` or `#trip` now points out to "Trips".
