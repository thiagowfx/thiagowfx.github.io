---
title: "logseq: backlog"
date: 2024-11-26T18:53:22+01:00
tags:
  - dev
---

Assume you use `TODO` and `DOING` for workflow tracking in
[Logseq](https://logseq.com/).

Assume you use an `#instrospect` tag.

**Problem statement**: how to define a single page / live query that aggregates
all of the above?

```logseq
{{query (OR (task TODO DOING) [[introspect]])}}
```

Unraveling:

- `[[introspect]]` refers to the `#introspect` tag
- A live query can be added with `/query`, which is represented as `{{query }}`
  under the hood.

More information: check out the [logseq
hub](https://hub.logseq.com/features/av5LyiLi5xS7EFQXy4h4K8/getting-started-with-advanced-queries/8xwSRJNVKFJhGSvJUxs5B2).
