---
title: "new script: copy"
date: 2025-11-04T14:05:47+01:00
tags:
  - dev
  - macos
---

[Previously]({{< ref "2025-10-30-new-script-ssh-mux-restart" >}}).

I decided to add a new `copy` script to
[`pancake`](https://github.com/thiagowfx/pancake) to standardize copying command
output and files to the system clipboard in both macOS and Linux.

The idea was originally inspired by [Evan
Hahn](https://evanhahn.com/scripts-i-wrote-that-i-use-all-the-time/):

> `copy` and `pasta` are simple wrappers around system clipboard managers, like
> `pbcopy` on macOS and `xclip` on Linux. I use these all the time.

[Evan's version](https://codeberg.org/EvanHahn/dotfiles/src/commit/843b9ee13d949d346a4a73ccee2a99351aed285b/home/bin/bin/copy) is concise and elegant.

[My version](https://github.com/thiagowfx/pancake/blob/457441b3bc790068ff2618125da08de0effab016/copy/copy.sh) is more verbose, for the sake of consistency with the rest of my scripts in pancake.

## Usage

```bash
# Copy from stdin
echo "BANANA42SPLIT88SUNDAE99CHERRY" | copy

# Copy a file
copy notes.txt

# Copy multiple files
copy *.md
```

## Platform Support

- **macOS**: Uses `pbcopy` (built-in)
- **Linux**: Auto-detects first available tool:
  — `wl-copy` (Wayland) — prioritized for modern desktops
  — `xclip` (X11)
  — `xsel` (X11)

## Features

- Silent on success (Unix philosophy)
- Supports stdin input
- Supports single or multiple files
- Multiple files are concatenated with newline separators
- Clear error messages for missing files or dependencies
