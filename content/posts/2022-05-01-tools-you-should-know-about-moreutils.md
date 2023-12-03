---
title: "★ Tools you should know about: moreutils"
date: 2022-05-01T13:02:51-04:00
tags:
  - linux
  - star
showtoc: true
---

[`moreutils`](https://joeyh.name/code/moreutils/) has previously been covered [elsewhere](https://news.ycombinator.com/item?id=31043655), multiple times. It's a collection of small unix tools that follow the [unix philosophy](https://en.wikipedia.org/wiki/Unix_philosophy)[^1] very strongly.

Here are some of my favorites with example usages. Obviously this post isn't a manual which would have been a disservice to the community; refer to the upstream man pages for detailed instructions.

<!--more-->

## sponge

> sponge(1) - soak up standard input and write to a file

Here's a typical workflow `sponge(1)` is great at:

```shell
# Given a file
$ cat myfile
a
b
c

# Imagine that for whatever reason we want to replace 'a' with 'b'
# Naively, we could try this:
$ cat myfile | tr 'a' 'b' > myfile
$ cat myfile

# However the file becomes empty!
# It got clobbered when we tried to simultenaously read from and write to it
# sponge comes to the rescue!

$ cat myfile | tr 'a' 'b' | sponge myfile
$ cat myfile
b
b
c
```

It is great to use `sponge` in lieu of `>` (shell output redirection) in shell pipelines when trying to both read from and write to the same file.

## vidir

> vidir(1) - edit directories and filenames

`vidir(1)` is great to bulk rename files/directories within a given directory, one level at a time. For example, if I open `vidir` at the top-level directory of this blog repository, it opens up `vim` (although it doesn't need to be `vim`, your `$EDITOR` is honoured) with the following content:

```
1	./.git
2	./.github
3	./.gitignore
4	./.gitmodules
5	./.hugo_build.lock
6	./LICENSE
7	./Makefile
8	./README.md
9	./archetypes
10	./config.yml
11	./content
12	./layouts
13	./public
14	./resources
15	./static
16	./themes
```

If I make, say, the following modifications (lines 7 and 8):

```
1	./.git
2	./.github
3	./.gitignore
4	./.gitmodules
5	./.hugo_build.lock
6	./LICENSE
7	./GNUMakefile
8	./README.rst
9	./archetypes
10	./config.yml
11	./content
12	./layouts
13	./public
14	./resources
15	./static
16	./themes
```

And then save and quit `vim` (`:wq`), then the effect would have been the same as:

```shell
$ mv Makefile GNUMakefile
$ mv README.md README.rst
```

If I changed my mind and decided not to save the modifications, I could just do `:cq`.

It's possible to leverage vim features such as `.` (repeat command) and `:%s/` (find and replace) to perform those mass file renames quickly and effectively. `vidir` is a breeze to use!

## ifne

> ifne(1) - Run command if the standard input is not empty

`ifne(1)` is effective when used with `find` or `fd` to keep shell pipes "happy". Here's one simple example:

```shell
$ find . -name '*.cpp' | xargs clang-format
```

This should work as expected, but it's cleaner to do:

```shell
$ find . -name '*.cpp' | ifne xargs clang-format
```

The added `ifne` ensures the `xargs` command is only executed if and only if `find` yields at least one result in its output.

This wasn't a very practical example though: a more realistic way to use `ifne` is with prototypical on-the-fly manipulation of shell pipes wherein initially you just do whatever, but then whenever you notice some command in the middle of the pipe has failed because its input was empty (=the previous pipe command output was empty) you just prepend `ifne` to it:

```
$ this | is | a | complicated | pipe
# assume "complicated" fails because it has no input
# so we iterate and do:
$ this | is | a | ifne complicated | pipe
```

## combine

> combine(1) - combine sets of lines from two files using boolean operations

`combine(1)` is pretty much `comm(1)`, but much more user-friendly. Given two files `file1` and `file2` it makes it easy to query which lines are {unique, common} to {each, both} files, using boolean operations (or, and, not, xor). Here's one example to find the _common lines_ in _both_ files, compare `combine` and `comm`:

```shell
$ combine file1 and file2
$ comm -12 file1 file2     # flags are harder to remember
```

[^1]: The Unix philosophy emphasizes building simple, short, clear, modular, and extensible code that can be easily maintained and repurposed by developers other than its creators. The Unix philosophy favors composability as opposed to monolithic design.
