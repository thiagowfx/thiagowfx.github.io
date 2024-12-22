---
title: "Alpine Linux: apk logs with etckeeper"
date: 2022-01-10T23:14:43-05:00
tags:
  - linux
---

`apk(8)` is the Alpine Linux package manager. Surprisingly, it lacks native
logs. In this post we will learn how to work around this limitation.


In a distribution like Arch Linux that uses `pacman(8)`, one would typically
find logs in `/var/log/pacman.log`. You would expect Alpine Linux to follow
suit and provide some `/var/log/apk.log` or similar, however that's not the
case.

Logs are nowhere to be found, even in the `apk-*` man pages. I double-checked
by asking on the `#alpine-linux` IRC and someone confirmed this is indeed the
case, and there's an (unconfirmed) possibility the next generation of apk may
add logging support.

Meanwhile, we will use `etckeeper(8)` to overcome this limitation.

## etckeeper: set-up

[`etckeeper`][etckeeper] is

> a collection of tools to let `/etc` be stored in a git, mercurial, bazaar or
> darcs repository. This lets you use git to review or revert changes that were
> made to /etc. Or even push the repository elsewhere for backups or
> cherry-picking configuration changes.

by [Joey Hess][hess].

It is available in the Alpine Linux [repositories][repo], just install it:

```
% apk add etckeeper
```

No configuration is needed, it works out-of-the-box, thanks to a [post-install
hook][hook] to initialize the git repository, and an [apk commit
hook][commit-hook] to update it upon `apk` package operations.

## etckeeper: viewing logs

Just run `git log` as root. Root privilege is necessary because the git
repository is initialized under `/etc/etckeeper`. Pick your poison:

```shell
$ GIT_DIR=/etc/etckeeper doas git log
```

```shell
$ doas git -C /etc/etckeeper log
```

```shell
$ (cd /etc/etckeeper && doas git log)
```

Here's what a typical log looks like, courtesy of `apk-autoupdate(1)`[^1]:

```
commit f06255c4be4657481082406b2050ecd88e3da768
Author: root <root@localhost.localdomain>
Date:   Tue Jan 11 00:00:24 2022 -0500

    committing changes in /etc after apk run

    Package changes:
    -libeconf-0.4.2-r0
    -libeconf-doc-0.4.2-r0
    +libeconf-0.4.4-r0
    +libeconf-doc-0.4.4-r0
    -mtools-4.0.36-r0
    -mtools-doc-4.0.36-r0
    +mtools-4.0.37-r0
    +mtools-doc-4.0.37-r0
    -perl-io-socket-ssl-2.073-r0
    -perl-io-socket-ssl-doc-2.073-r0
    +perl-io-socket-ssl-2.074-r0
    +perl-io-socket-ssl-doc-2.074-r0
    -py3-idna-3.3-r1
    +py3-idna-3.3-r2
    -py3-jinja2-3.0.1-r1
    -py3-jinja2-doc-3.0.1-r1
    +py3-jinja2-3.0.3-r0
    +py3-jinja2-doc-3.0.3-r0
```


[etckeeper]: https://etckeeper.branchable.com/
[repo]: https://pkgs.alpinelinux.org/packages?name=etckeeper
[hook]: https://git.alpinelinux.org/aports/tree/main/etckeeper/etckeeper.post-install
[commit-hook]: https://git.alpinelinux.org/aports/tree/main/etckeeper/apk-commit_hook
[hess]: https://joeyh.name/

[^1]: Which merely does `apk upgrade`, automatically. More details [here](https://github.com/jirutka/apk-autoupdate).
