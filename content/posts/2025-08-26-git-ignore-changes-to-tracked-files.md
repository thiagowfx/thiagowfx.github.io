---
title: "git: ignore changes to tracked files"
date: 2025-08-26T14:46:44+02:00
tags:
  - dev
---

[Previously]({{< ref "2025-08-26-midnight-commander-colorscheme" >}}).

Given this config file for [midnight
commander](https://midnight-commander.org/):

```shell
% head -n 2 ~/.dotfiles/mc/.config/mc/ini
[Midnight-Commander]
skin=modarin256
```

...properly installed via `stow`:

```shell
% (cd ~/.dotfiles && stow mc)
```

Upon opening `mc`, it writes a lot of configuration settings to that file:

```ini
[Midnight-Commander]
skin=modarin256
verbose=true
shell_patterns=true
auto_save_setup=true
preallocate_space=false
auto_menu=false
use_internal_view=true
use_internal_edit=true
clear_before_exec=true
[...]
```

I could check them into source control, but I do not want to. They are defaults.

So I tell `git` to leave these additions alone:

```shell
% git update-index --skip-worktree mc/.config/mc/ini
```

Now `git status` will not show the file.
