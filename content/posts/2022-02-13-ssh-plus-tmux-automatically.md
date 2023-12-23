---
title: "★ SSH plus tmux automatically"
date: 2022-02-13T20:20:27-05:00
tags:
  - dev
  - linux
  - star
---

One of the most classic sysadmin/DevOps tasks is to use secure shell to connect to remote machines.

To persist those connections, a terminal multiplexer is often used, `tmux` and `screen` being the two most popular ones.

In this post I will cover a few different client-side and server-side ways to have `ssh` automatically spawn `tmux` upon connection.

<!--more-->

## Option #1: Use command-line ssh flags (client-side, recommended)

Start `tmux`, forcing unicode, attaching to and/or creating a session named _main_:

```shell
$ ssh user@host -t -- tmux -u new -A -s main
```

`-u` is not strictly necessary, however I experienced occasional weirdness when connecting to some machines and omitting it. Some unicode characters wouldn't be properly rendered, like the horizontal and vertical lines used to render tmux pane splits. Even though most machines should work just fine these days by supporting UTF-8 out-of-the-box, it's safer to always include `-u` just in case.

Tip: If it's annoying to remember to type the full command above, consider adding an `alias` in your shell config. Alternatively, use a ssh client that remembers your flags preferences such as the [chrome secure shell](https://chrome.google.com/webstore/detail/secure-shell/iodihamcpbpeioajjeobimgagajmlibd?hl=en) extension.

## Option #2: Use `~/.ssh/config` (client-side)

This option is very similar to the previous one, but the flags live in the ssh config rather then being specified at the command line:

```shell
$ cat ~/.ssh/config
Host *
  RequestTTY yes
  RemoteCommand tmux -u new -A -s main
```

You don't need to match all hosts (`Host *`), if you'd rather match one or more specific hosts, refer to the ssh config syntax `ssh_config(5)` to add them. A simple example would be `Host mymachine.example.org`.

**Caveat**: I've found this method interferes with `git` + `ssh` authentication. More specifically:

```shell
$ git remote -v
origin	git@github.com:thiagowfx/.dotfiles.git (fetch)
origin	git@github.com:thiagowfx/.dotfiles.git (push)
$ git push
Cannot execute command-line and remote command.
fatal: Could not read from remote repository.

Please make sure you have the correct access rights
and the repository exists.
```

Therefore I discourage it, unless you only use it with specific hosts i.e. don't use it with `Host *`.

## Option #3: Use `~/.bash_profile` or similar (server-side, recommended)

This method leverages your login shell startup config file (`~/.bash_profile`, `~/.zprofile`, etc) to automatically spawn `tmux`.

```shell
# This file is invoked as part of my ~/.bash_profile.
$ cat ~/.profile.d/tmux_auto_ssh.sh.
# Automatically spawn tmux within ssh sessions for interactive terminals.
# https://stackoverflow.com/a/43819740/1745064
#
# The session is called `main`.
# Create a session with PREFIX :new, rename with PREFIX $, toggle with PREFIX s.
#
# Escape hatch:
#   ssh <host> -t -- NOTMUX=1 <shell>
if [ -z "$NOTMUX" ] && [ -z "$TMUX" ] && [ -n "$SSH_TTY" ] && [[ $- =~ i ]]; then
  tmux -u new -A -s main
  exit
fi
```

The `if` basically checks:

- whether we're not already inside a tmux session (we shouldn't be), so that we don't nest `tmux`
- whether we're accessing the shell via `ssh` (we should be)
- whether we're accessing an interactive shell (we should be), so that it doesn't interefere with oneshot `ssh` commands

There's also a escape hatch. If you want to get an interactive shell but bypass `tmux` for some reason[^1], just set `NOTMUX=1`:

```shell
$ ssh user@host -t -- NOTMUX=1 bash
```

## Final remarks

My favorite methods are #1 and #3, and whether I use one or the other depends whether I want to unconditionally spawn `tmux` server-side, or selectively spawn `tmux` client-side.

When using chrome secure shell (hterm) I find #1 convenient because hterm remembers your `ssh` host settings. That said, in scenarios where I fully control a host and it's not solely used for production, #3 is my favorite as it works unconditionally regardless of the client terminal emulator I am using.


[^1]: For example, maybe if `tmux` broke due to a recent upgrade, or if the `~/.tmux.conf` is invalid.
