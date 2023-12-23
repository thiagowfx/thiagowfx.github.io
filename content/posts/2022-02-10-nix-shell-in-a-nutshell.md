---
title: "nix-shell in a nutshell"
date: 2022-02-10T20:48:02-05:00
tags:
  - dev
  - linux
  - macos
---

As soon as we finish installing [`Nix`](https://nixos.org/download.html) on
Darwin, we're greeted with a call to action:

```
Alright! We're done!
Try it! Open a new terminal, and type:

  $ nix-shell -p nix-info --run "nix-info -m"

Thank you for using this installer. If you have any feedback or need
help, don't hesitate:

You can open an issue at https://github.com/nixos/nix/issues
```

<!--more-->

## Hello world (bloated)

All right then, let's do it!

```shell
$ nix-shell -p nix-info --run "nix-info -m"
 - system: `"aarch64-darwin"`
 - host os: `Darwin 21.3.0, macOS 12.2`
 - multi-user?: `yes`
 - sandbox: `no`
 - version: `nix-env (Nix) 2.6.0`
 - channels(root): `"nixpkgs"`
 - nixpkgs: `/nix/var/nix/profiles/per-user/root/channels/nixpkgs`
```

Cool, it works. Let's break it down a bit.

## Hello world (classic)

Nix shell creates an ephemeral shell environment with the customizations you
want. The most basic customization is to make a given set of packages
available. There's a `hello` package:

```shell
$ nix-shell -p hello
$ hello
Hello, world!
```

In case you're curious, this is a GNU binary:

```shell
$ hello --version
hello (GNU Hello) 2.10

Copyright (C) 2014 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.
```

I have no idea why they are in version 2.10 and what their changelog is. It's
such a simple binary...

If you exit the shell, `hello` seemingly vanishes:

```
$ exit
exit
$ hello
zsh: command not found: hello
```

An easy way to think of `nix-shell` is like an ephemeral sandbox where all your
desired packages are made available when you enter it. It's possible to provide
more than one package, naturally. It's also possible to provide a `shell.nix`
file with the package declarations, so that when you can `nix-shell` without
any arguments.

```
$ cat shell.nix
{ pkgs ? import <nixpkgs> {} }:
  pkgs.mkShell {
    # nativeBuildInputs is usually what you want -- tools you need to run
    nativeBuildInputs = [ pkgs.buildPackages.hello ];
}
$ nix-shell
$ hello
Hello, world!
```

## Hello world (oneshot)

```shell
$ nix-shell -p hello --run hello
Hello, world!
```

This oneshot style doesn't enter the shell, it just runs the given `--run`
command and then exits.

This post just scratched the surface of what `nix-shell` can do. See the
references below for more in-depth guides about it.

## References

- [Tools You Should Know About: nix-shell](https://cuddly-octo-palm-tree.com/posts/2021-12-19-tyska-nix-shell/)
- [An introduction to nix-shell](https://ghedam.at/15978/an-introduction-to-nix-shell)
- [NixOS manual: `nix-shell`](https://nixos.org/manual/nix/stable/command-ref/nix-shell.html)
