
**Problem statement**: `watch -- git diff` / `watch -- git status` should emit
colors. Yet it doesn't.

[watch(1)](https://man.archlinux.org/man/watch.1):

```
NAME

watch - execute a program periodically, showing output fullscreen

SYNOPSIS

watch [option ...] command

DESCRIPTION

watch runs command repeatedly, displaying its output and errors (the first screenful). This allows you to watch the program output change over time. By default, command is run every 2 seconds and watch will run until interrupted. A header informs of the start and running time of command as well as its exit code.
```

You typically address this with `watch -c`:

```
-c, --color
  Interpret ANSI color and style sequences.
```

And yet, `watch -c -- git status` still won't emit colors. This is because `git`
"knows" the output is going through a TTY (`watch`), and thus defensively
disables colors. Some programs control this behavior with a `--color=always`
switch (the default is typically `auto`).

Without diving deep into what's happening underneath (terminal ANSI escape
colors, TTY output detection), the magical solution is to use
[`unbuffer(1)`](https://man.archlinux.org/man/unbuffer.1), which was
[previously]({{< ref "2024-12-23-unbuffer" >}}) covered. `unbuffer` is
agnostic of the underlying program; it doesn't matter whether it uses `--color`,
or `CLICOLOR`, or another mechanism.

Thus we achieve this form:

```shell
% watch -c -- unbuffer git status
```

But it's super tedious to remember and to type out the `-c -- unbuffer` bits.

To resolve this, I created a wrapper:
[`uwatch(1)`](https://github.com/thiagowfx/pancake/tree/master/uwatch). The `u`
alludes to "unbuffer":

```
Run a command repeatedly using watch, preserving colored output.

Uses unbuffer to maintain color codes through watch's output. Useful for monitoring git status, test output, or any command with color formatting.
```

Usage:

```shell
uwatch [--] git status
```

The `--` separator is optional.

