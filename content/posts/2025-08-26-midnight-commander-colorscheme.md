---
title: "midnight commander: colorscheme"
date: 2025-08-26T14:09:58+02:00
tags:
  - dev
---

[Midnight commander](https://midnight-commander.org/):

> is a visual, dual-pane file manager. It is released under the GNU General
> Public License and therefore qualifies as Free Software.

> Midnight Commander is a feature-rich, full-screen, text-mode application that
> allows you to copy, move, and delete files and entire directory trees, search
> for files, and execute commands in the subshell. Internal viewer, editor and
> diff viewer are included.

![](https://midnight-commander.org/img/mc-screenshot-cropped.png)

It's available virtually [everywhere](https://repology.org/project/mc/versions).

I normally use [ranger](https://github.com/ranger/ranger), but I wanted to give
`mc` a try.

There has always been one problem: its default colorscheme is absolutely
terrible. Its lack of contrast is flabbergasting.

Well, I finally found a way to make it look better, without much fuss:

1. Open `mc`
2. Click "Options" in the top file menu
3. Click "Appearance"
4. Change the skin to `modarin256`

It's one of the fewest built-in colorscheme themes I could find that strikes a
good color contrast balance. Most other themes (including the default one) are
unreadable.

You can preview all themes [here](https://skins.midnight-commander.org/).

There are lots of jokes about how to quit `vim`, but do you know how to quit
`mc`? Press `F10` or type `exit<CR>`.
