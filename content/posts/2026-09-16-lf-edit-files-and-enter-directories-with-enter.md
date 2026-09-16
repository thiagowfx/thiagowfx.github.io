---
title: "lf: edit files and enter directories with enter"
date: 2026-09-16T16:41:39+02:00
tags:
  - bloggify
  - dev
  - linux
---

**Problem statement**: in [lf](https://github.com/gokcehan/lf), how can
`<Enter>` edit files without trying to edit directories?

`e` already opens the selected file in `$EDITOR`. My first keybinding mapping
attempt copied its default command:

```diff
 # Edit file: 'e' (mapped out-of-the-box)
+map <enter> $$EDITOR "$f"
```

This worked for files, but it also sent directories to the editor, which is
unwelcome.

Next up: lf's built-in `open` command already has the split behavior I wanted
for directories:

```text
% lf -doc | sed -n '533,540p'
Change the current working directory to the parent directory.

open (default l and <right>)

If the current file is a directory, then change the current directory to
it, otherwise, execute the open command. A default open command is
provided to call the default system opener asynchronously with the
current file as the argument. A custom open command can be defined to
```

So I kept the file branch in `$EDITOR` and sent the directory branch back to
lf's `open` command:

```text
cmd edit-or-open ${{
    if [ -d "$f" ]; then
        "$lf" -remote "send $id open"
    else
        $EDITOR "$f"
    fi
}}
map <enter> edit-or-open
```

This works exactly as intended!

The complete [lf
configuration](https://github.com/thiagowfx/.dotfiles/blob/3ded1cb73a5ef401aae7af0dd170a9e647c5f5ce/lf/.config/lf/lfrc#L14-L21)
lives in my dotfiles.
