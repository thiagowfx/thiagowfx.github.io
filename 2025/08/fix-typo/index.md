---
title: "\"Fix typo\""
url: https://perrotta.dev/2025/08/fix-typo/
last_updated: 2026-01-03
---


You, too, can make the ~~word~~ world a better place,
[one](https://github.com/codespell-project/codespell/pull/3758)
[typo](https://github.com/codespell-project/codespell/pull/3759) at a time.

The [codespell](https://github.com/codespell-project/codespell/) project can be
trivially adopted in a git repository via a [pre-commit
hook](https://pre-commit.com/):

```
repos:
  - repo: https://github.com/codespell-project/codespell
    rev: 63c8f8312b7559622c0d82815639671ae42132ac # frozen: v2.4.1
    hooks:
      - id: codespell
```

