
Assume you use `TODO` and `DOING` for workflow tracking in
[Logseq](https://logseq.com/).

Assume you use an `#instrospect` tag.

**Problem statement**: how to define a single page / live query that aggregates
all of the above?

```markdown
{{query (OR (task TODO DOING) [[introspect]])}}
```

Unraveling:

- `[[introspect]]` refers to the `#introspect` tag
- A live query can be added with `/query`, which is represented as `{{query }}`
  under the hood.

More information: check out the [logseq
hub](https://hub.logseq.com/features/av5LyiLi5xS7EFQXy4h4K8/getting-started-with-advanced-queries/8xwSRJNVKFJhGSvJUxs5B2).

