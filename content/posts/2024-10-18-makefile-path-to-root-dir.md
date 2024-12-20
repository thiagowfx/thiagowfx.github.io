---
title: "Makefile: path to root dir"
date: 2024-10-18T14:52:44+02:00
tags:
  - dev
---

**Problem statement**: Given a `Makefile` within `~/git/scaffolding/Makefile`,
and a command that needs to run from the `scaffolding/` directory, create an
`all` target that works from any directory.

<!--more-->

**Solution**:

```make
# The directory wherein the Makefile resides.
ROOT_DIR := $(patsubst %/,%,$(dir $(realpath $(lastword $(MAKEFILE_LIST)))))

all:
    @echo $(ROOT_DIR)
	kickstart $(ROOT_DIR)/app

.PHONY: all
```

**Explanation**:

- The `echo` is used only for debugging, therefore it should be removed in prod.
- The `kickstart` command will properly run having `~/git/scaffolding` as `$PWD`
  whether you invoke it from `~/git/scaffolding` or from `~/git` (via `make
  -C`).
- `pathsubst` is needed to remove the trailing slash (`/`) from the directory,
  so that `$(ROOT_DIR)/` does not yield a double slash, which works but it is
  ugly.

**Source** (adapted): https://stackoverflow.com/questions/18136918/how-to-get-current-relative-directory-of-your-makefile
