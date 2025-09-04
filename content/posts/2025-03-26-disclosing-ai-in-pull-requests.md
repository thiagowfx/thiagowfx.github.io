---
title: "Disclosing AI in pull requests"
date: 2025-03-26T13:07:52+01:00
tags:
  - dev
---

As we start to draft more PRs with the help of AI, I am thinking to adopt a
subtle approach to signal that all (or most) of a given PR was created with the
help of AI.

Perhaps by adding a `:robot:` 🤖 emoji in the commit message.

[GitHub Markdown](https://api.github.com/emojis) will happily render `:robot:`.

I could also add an [attribution footer]({{< ref "2025-03-03-create-a-git-commit-with-multiple-contributors" >}}):

```
"Co-authored-by: Claude <noreply@anthropic.com>"
```

It's just a bit more verbose.

Have you thought about this?
