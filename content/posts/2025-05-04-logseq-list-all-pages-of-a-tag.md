---
title: "Logseq: list all pages of a tag"
date: 2025-05-04T13:24:52+02:00
tags:
  - selfhosted
---

**Problem statement**: Given a couple of pages in [Logseq](https://logseq.com/)
tagged with a given `content` tag:

```
tags:: content
```

...dynamically list all of them.

We can do so with the following logseq query[^1]:

```logseq
#+BEGIN_QUERY
{
  :title "Ideas 💡 (->)"
  :query (property :tags "idea")
}
#+END_QUERY
```

This is a static query, not meant to be changed.

Alternatively it's possible to create a live query, which allows one to tweak it
on-the-fly:

```logseq
{{query (property :tags "idea")}}
```


[^1]: The query syntax is somewhat a blend of [orgmode](https://orgmode.org) +
    emacs lisp from emacs.
