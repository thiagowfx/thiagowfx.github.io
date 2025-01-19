---
title: "Scan for markdown broken links in your blog"
date: 2025-01-01T16:35:00-03:00
tags:
  - bestof
  - dev
---

[Link rot](https://en.wikipedia.org/wiki/Link_rot) is a real problem in the web,
even though [Cool URIs don't (supposedly)
change](https://www.w3.org/Provider/Style/URI).

I figured I could try to mitigate it from my site from time to time with some CI
integration.

Then I found
[`markdown-link-check`](https://github.com/tcort/markdown-link-check).

The best way to illustrate its usage is with an example:

```shell
% pre-commit try-repo https://github.com/tcort/markdown-link-check --all-files
[...]
FILE: content/posts/2024-02-04-new-domain.md
  [✓] https://www.perrotta.dev/
  [✖] https://blog.perrotta.dev/
  [✓] https://perrotta.dev/
  [✓] https://thiagowfx.github.io/

  4 links checked.

  ERROR: 1 dead links found!
  [✖] https://blog.perrotta.dev/ → Status: 0

FILE: content/posts/2024-12-30-cookiecutter.md
  [✓] https://github.com/cookiecutter/cookiecutter
  [✖] https://crates.io/crates/kickstart
  [✓] https://github.com/Keats/kickstart?tab=readme-ov-file#050-2024-12-13

  3 links checked.

  ERROR: 1 dead links found!
  [✖] https://crates.io/crates/kickstart → Status: 404
[...]
```

It compiles an exhaustive list of all broken links in all markdown pages in my
git repository[^1].

[^1]: I ceased to use `blog.perrotta.dev` in favour of `perrotta.dev` in Q4
    2024.

It's not bullet-proof. For example, sites behind Cloudflare are reported as
broken, even though they may not be
([example](https://www.secretflying.com/posts/category/cities-countries/germany/)).
Sites that block bots / crawlers may also be flagged as false positives.

I added it to the list of pre-commit hooks for this site.
