---
title: "Create a git commit with multiple contributors"
date: 2025-03-03T14:55:23+01:00
tags:
  - dev
  - git
---

- **Step 1**: Create a commit / pull request as usual.
- **Step 2**: Collaborate 🪄. Different people push to the same remote branch.
- **Step 3**: Once it's done, add as many git footer elements as needed, like in
  the following commit message example:

```
feat: adopt time machine API

Address one of our main feature requests.

Allow users to go back in time by integrating with gravitational://infty.improbability/

Co-authored-by: Marvin <marv_is_happy@in.space>
Co-authored-by: Zaphod Beeblebrox <zaph@in.space>
```

Ideally, sort the `Co-authored-by` field alphabetically.

Sources:

- https://docs.github.com/en/pull-requests/committing-changes-to-your-project/creating-and-editing-commits/creating-a-commit-with-multiple-authors
- https://stackoverflow.com/questions/7442112/how-to-attribute-a-single-commit-to-multiple-developers
