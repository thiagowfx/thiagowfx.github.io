---
title: "sort deterministically"
date: 2024-11-12T11:25:12+01:00
tags:
  - dev
---

We had the following code in a CI pipeline:

```shell
find apps/base/ -type d -exec basename {} \; | sort | sed -e 's/^/- /
```

It lists all directories in `apps/base`.
We add `sort` to make the output canonical.
The `sed` part is just to make an unordered list out of it.

There was an issue though.

In my machine, and in CI (GitHub Actions), the following output was produced:

```
garden-info-export
gardenia
```

I use macOS + `sort` from GNU `coreutils` via homebrew:

```shell
% which sort
/opt/homebrew/opt/coreutils/libexec/gnubin/sort
% sort --version
sort (GNU coreutils) 9.5
Copyright (C) 2024 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <https://gnu.org/licenses/gpl.html>.
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.

Written by Mike Haertel and Paul Eggert.
```

In a coworker's machine (Ubuntu Linux), it produced the following instead:

```shell
gardenia
garden-info-export
```

We had the same `locale` (`en_US.UTF-8`), and the coworker was also using `sort` from GNU `coreutils`. Puzzling.

In order to force a deterministic output, I proposed to use `-d`. From `sort(1)`:

```shell
-d, --dictionary-order
	Consider only blank spaces and alphanumeric characters in comparisons.
```

And therein reproducibility was achieved[^1].

I do not really know why the outputs were different even with the same `locale` (`LANG`, `LC_COLLATE`, `LC_ALL`, etc). For future reference, my current locale:

```shell
% locale
LANG="en_US.UTF-8"
LC_COLLATE="en_US.UTF-8"
LC_CTYPE="en_US.UTF-8"
LC_MESSAGES="en_US.UTF-8"
LC_MONETARY="en_US.UTF-8"
LC_NUMERIC="en_US.UTF-8"
LC_TIME="en_US.UTF-8"
LC_ALL=
```

And my coworker's:

```shell
$ locale
LANG=en_US.UTF-8
LANGUAGE=en_US
LC_CTYPE="en_US.UTF-8"
LC_NUMERIC=en_US.UTF-8
LC_TIME=en_US.UTF-8
LC_COLLATE="en_US.UTF-8"
LC_MONETARY=en_US.UTF-8
LC_MESSAGES="en_US.UTF-8"
LC_PAPER=en_US.UTF-8
LC_NAME=en_US.UTF-8
LC_ADDRESS=en_US.UTF-8
LC_TELEPHONE=en_US.UTF-8
LC_MEASUREMENT=en_US.UTF-8
LC_IDENTIFICATION=en_US.UTF-8
LC_ALL=
```

[^1]: In this case, the coworker's version became the canonical one.
