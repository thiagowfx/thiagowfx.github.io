
**Problem statement**: I present this to you the same way I presented it to [Amp
Code](https://ampcode.com) in the context of my
[~/.dotfiles](https://github.com/thiagowfx/.dotfiles):

```
new shell alias: ee

quit all shells

example:

$ bash
$ bash
$ zsh

Now we're 3 levels deep.
"ee" should quit them all (effectively closing the underlying terminal emulator tab)
```

**Why do I even have this issue in the first place?** Utilities like
[wt](https://github.com/thiagowfx/pancake/tree/master/wt) (to manage git
worktrees) and [try](https://github.com/thiagowfx/pancake/tree/master/try) (to
manage scratch directories) need to change directories. Alas, it's not possible
to change the current working directly (`$PWD`) with a script. As such, my
workaround is to open a subshell in the desired directory. As a side effect, I
end up with nested subshells.

**Why `ee`?** I close my shell with `C-d` (Ctrl + D).
In this context I need to press it three times in a row.
`dd` would have been a natural alias but I'd rather avoid the name clash with
the [`dd`](https://wiki.archlinux.org/title/Dd) disk cloning util.
`ee` came next naturally.

This version works in `bash` but not in `zsh`:

```shell
% which ee
ee () {
        pid=$$
        pids=$pid
        while ppid=$(ps -o ppid= -p "$pid" | tr -d ' ')  && [ "$ppid" -gt 1 ] 2> /dev/null
        do
                case "$(ps -o comm= -p "$ppid" 2>/dev/null)" in
                        (*sh) pids="$pids $ppid"
                                pid=$ppid  ;;
                        (*) break ;;
                esac
        done
        kill -HUP $pids
}
```

> The issue is `zsh` doesn't word-split unquoted variables like `bash`/`sh` does.
> `$pids` is passed as a single string. Fix with `eval`:

The version below works in **both** `bash` and `zsh`:

```shell
ee () {
        pid=$$
        pids=$pid
        while ppid=$(ps -o ppid= -p "$pid" | tr -d ' ')  && [ "$ppid" -gt 1 ] 2> /dev/null
        do
                case "$(ps -o comm= -p "$ppid" 2>/dev/null)" in
                        (*sh) pids="$pids $ppid"
                                pid=$ppid  ;;
                        (*) break ;;
                esac
        done
        eval "kill -HUP $pids"
}
```

The only difference is the last line:

```diff
-       kill -HUP $pids
+       eval "kill -HUP $pids"
```

