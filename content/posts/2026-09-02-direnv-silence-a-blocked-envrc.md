---
title: "direnv: silence a blocked .envrc"
date: 2026-09-02T16:22:01+02:00
tags:
  - dev
---

Sometimes we simply do not want to activate [`direnv`](https://direnv.net/) in a
given project.

Deny it for the current directory:

```shell
% direnv deny .
```

To enable it later:

```shell
% direnv allow .
```

This is necessary to make it stop nagging you each time you `cd` into a project
(directory) with `.envrc`:

```shell
% cdtmp
/var/folders/yr/6sw3yylx6gjcy5jr38d6j6000000gn/T/thiago.perrotta-2026-09-02-k5lfb0

thiago.perrotta /var/folders/yr/6sw3yylx6gjcy5jr38d6j6000000gn/T/thiago.perrotta-2026-09-02-k5lfb0
% touch .envrc
direnv: error /private/var/folders/yr/6sw3yylx6gjcy5jr38d6j6000000gn/T/thiago.perrotta-2026-09-02-k5lfb0/.envrc is blocked. Run `direnv allow` to approve its content
```
