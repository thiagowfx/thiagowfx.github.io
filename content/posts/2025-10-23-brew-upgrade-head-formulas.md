---
title: "brew: upgrade HEAD formulas"
date: 2025-10-23T12:53:11+02:00
tags:
  - dev
  - selfhosted
---

[Previously]({{< ref "2025-10-17-distributing-my-own-scripts-via-homebrew" >}}).

When a package is installed with `--HEAD`:

```shell
% brew install --HEAD pancake
```

...`brew upgrade` won't automatically fetch its latest version.

In order to do so, run:

```shell
% brew upgrade --fetch-HEAD [package...]
```

[Source](https://apple.stackexchange.com/questions/439595/brew-head-update-behaviour)[^1].

[^1]: I answered it there, does that count as linking to the source?
