---
title: "Sourcegraph"
date: 2024-12-31T22:45:20-03:00
tags:
  - dev
---

[Sourcegraph](https://sourcegraph.com/) is a global search engine.
Think code.google.com back in the days, but more developer-friendly.
In fact, it's quite comparable to [Google Code Search](https://cs.chromium.org/).

I like to assign it as a search engine in Chrome:

- Navigate to [chrome://settings/search](chrome://settings/search)
- Click 'Manage search engines and site search'
- In the 'Site search' section, click 'Add'
- Populate it:

```
Name: Sourcegraph
Shortcut: ss
URL: https://sourcegraph.com/search?q=context:global+%s
```

Once it is saved, you can type in `ss {query}` in the URL bar to search using
Sourcegraph.

For example: `ss f:.pre-commit.config\.yaml$ "language: golang"`.
