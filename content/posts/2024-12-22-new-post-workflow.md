---
title: "New post workflow"
date: 2024-12-22T22:26:46-03:00
tags:
  - meta
---

```shell
% just new "post title"
% vim content/posts/
```

Hit 'G', open up the post, it looks like this:

```markdown
---
title: "New post workflow"
date: 2024-12-22T22:26:46-03:00
tags:
  - bestof
  - dev
  - linux
  - meta
  - portuguese
  - privacy
  - selfhosted
  - serenity
---
```

Delete tags that are not applicable from the exhaustive list above. Most of the
time I'll use `dev`.

Once it's done, save the file with `:Gwq` ([vim-fugitive](https://github.com/tpope/vim-fugitive)).

Commit and push. Profit[^1]. Committing usually has this form: `git commit -m
"new post: blablabla"`.

Sometimes, a pre-commit hook will rescue me, like with this post[^2]:

```
codespell................................................................iFailed
- hook id: codespell
- exit code: 65

content/posts/2024-12-22-new-post-workflow.md:37: Comitting ==> Committing
```

I do not use AI in any way, neither to draft the posts, nor to review them
afterwards. Especially, in particular, _not_ to modify my writing style.
Authenticity is important. This is not a professional publication, it's done
merely for fun, hence adding these extra steps would have been overkill.


[^1]: Still waiting for the profit ($$). Nah.
[^2]: Not on purpose, I swear.
