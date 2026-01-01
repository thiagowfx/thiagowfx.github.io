
[broot](https://github.com/Canop/broot):

> A new way to see and navigate directory trees: https://dystroy.org/broot

It's a mixture of `ranger` / `mc` (terminal file manager), `fzf` (fuzzy file
finder), `tree` (list directory trees in the terminal), `ls`, `find` / `fd`,
`fpp`, `grep` / `ack` / `rg`, all-in-one. I'm starting to occasionally use it in
my daily workflow. Its [`Why?`](https://dystroy.org/broot/) page may convince
you to give it a try.

The upstream documentation is quite decent; as such, I do not intend to
replicate it here. That said, here are a couple of ad-hoc notes.

**Usage**: `broot {dir}` or simply `broot` to open it in the current directory,
as you would with `ranger`.

`-c` to `open_preview`. I do not know why this is not the default behavior. It
really should be! It displays the file contents of the currently focused file in
the right-side pane. We can make it the default:

```json
~/.config/broot/conf.hjson:

###############################################################
# Default flags
# You can set up flags you want broot to start with by
# default, for example `default_flags="-ihp"` if you usually want
# to see hidden and gitignored files and the permissions (then
# if you don't want the hidden files at a specific launch,
# you can launch broot with `br -H`).
# A popular flag is the `g` one which displays git related info.
#
# default_flags:
default_flags: "-c :open_preview"
```

Use the up and down arrows to navigate (or Tab / Shift + Tab). Vi-like
keybindings (`j` / `k`) do not work but that's for a good reason, by design:
there's a permanent command-line bar at the bottom (think of `mc`), used to
issue commands to `broot` and/or employ file/directory filtering; we need to be
able to type in characters there. This takes some getting used to if you're
coming from `ranger`.

`ENTER`, by default, opens the currently focused file in your visual editor
(e.g. VSCode, Zed). I am not a fan of this behavior, I'd rather it to use
`$EDITOR` (e.g. `vim`, `emacs`). It's possible to change this behavior, but I
haven't done so yet. There's a workaround: type in `<Space>e<Enter>` (or
`:e<Enter>` like in `vim`). This issues the `edit` command, which opens
`$EDITOR`. I wish `ENTER` would so do out-of-the-box!

The main reason to use `broot` is due to its excellent and versatile
[filtering](https://dystroy.org/broot/input/) capabilities, which allows
composite searches as well. Here's a practical example:

```
ep/pgbouncer\/values.yaml/&c/default
```

...it searches for all files named `pgbouncer/values.yaml` (within or nested in
PWD) whose file contents include the string `default`. Then it displays a
dynamic list of matches (including previews!) which you can manipulate
individually or in batches. For example, you could easily open each of them in
`$EDITOR`, or delete all of them, or run `sed -i` in all of them.

Explanation of the search modes (there are even more):

- `ep/`: exact string search on subpath (full path) – like `fd -p`
- `c/`: exact string search on file content – like `grep` or `ack` or `rg`

`:gs` opens an interactive tree with files in `git status` – comparable to `git
status | fpp -ko`.

We can run `sed -i` in all matches. First, define a verb (action) for it:

```json
~/.config/broot/verbs.hjson:

###############################################################
# This file contains the verb definitions for broot
#
# Some verbs here are examples and not enabled by default: you
#  need to uncomment them if you want to use them.
#
# Documentation at https://dystroy.org/broot/verbs/
###############################################################
verbs: [
    [...]
    {
        invocation: "sed {arg}"
        shortcut: sed
        apply_to: text_file
        execution: "gsed -i -e {arg} {file}"
        leave_broot: false
    }
    [...]
]
```

Then, after running a search, type in `<Space>sed<Space>'s/foo/bar/g'`.

Again, why is this not a built-in verb?

All things considered, I think `broot` needs some polishing in order to become
easy(ier) to use. It is a powerful tool, but its out-of-the-box devex experience
leaves a lot to be desired.

Another example: [#453](https://github.com/Canop/broot/issues/453): there's no
filter history.

