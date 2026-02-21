---
title: "neovim: inline git hunk control"
date: 2026-01-03T15:41:21-03:00
tags:
  - bestof
  - dev
  - git
  - vim
---

What is a
[hunk](https://stackoverflow.com/questions/37620729/in-the-context-of-git-and-diff-what-is-a-hunk)?

> When comparing two files, diff finds sequences of lines common to both files,
> interspersed with groups of differing lines called hunks[^2].

There are various ways to treat git hunks as first-class citizens, manipulating
them one at a time – staging, unstaging, or reverting them.

The classic one is [`git add [-p |
--patch]`](https://millerb.co.uk/2021/11/16/git-add-patch.html). Hit yes or no
for each hunk, one by one:

```shell
% git add -p
diff --git a/Justfile b/Justfile
index bbb3779a9..70840a008 100755
--- a/Justfile
+++ b/Justfile
@@ -175,3 +175,6 @@ update-pre-commit:
 # Update JSON schemas
 update-json-schemas:
     pre-commit run -a update-json-schemas --hook-stage manual
+
+hello:
+    echo world
(1/1) Stage this hunk [y,n,q,a,d,e,p,P,?]?
```

There's also [`git add [-i |
--interactive]`](https://nuclearsquid.com/writings/git-add/):

```shell
% git add -i

*** Commands ***
  1: status       2: update       3: revert       4: add untracked
  5: patch        6: diff         7: quit         8: help
What now>
```

It's also possible to manage hunks via git TUIs (=from the terminal) such as:

- **[gitui](https://github.com/gitui-org/gitui)**
- [tig](https://github.com/jonas/tig)
- [lazygit](https://github.com/jesseduffield/lazygit)

...or graphically with IDEs with as VSCode.

An honorable mention also goes to
[`git-crecord`](https://github.com/andrewshadura/git-crecord), which I
originally discovered by looking for an open source alternative to Google's
Fig[^1] interactive commit and split commands.

Now that you see how my mind is overloaded with many possibilities to manipulate
git hunks, the natural follow-up question is: how to do so right from within our
favorite text editor (`vim`)?

With classic `vim`, Tim Pope's
[`vim-fugitive`](https://github.com/tpope/vim-fugitive) is often touted as
best-in-class (paired with
[`vim-gitgutter`](https://github.com/airblade/vim-gitgutter)). I use it
occasionally. The workflow is as follows:

- From an open file with modifications, run `:GDiff` (`:GDiffsplit`).
- Proceed as you normally would in `vimdiff`. Use `:diffget` (`do`) and
  `:diffput` (`dp`) for each hunk. Use `[c` and `]c` to navigate to the previous
  / next hunk.

Finally, we get to the meat of the post. Is there any workflow
improvement in `neovim`, which I have recently [switched to]({{< ref
"2025-12-23-vim-nvim" >}})?

First of all, the familiar vim-fugitive workflow still works there.

Its evolution is [gitsigns.nvim](https://github.com/lewis6991/gitsigns.nvim):

> Git integration for buffers

Given the config below, the following becomes possible:

```lua
-- Git integration
{
'lewis6991/gitsigns.nvim',
config = function()
  require('gitsigns').setup({
    on_attach = function(bufnr)
      local gs = require('gitsigns')
      -- ]c / [c: next/prev hunk (falls back to default in diff mode)
      -- like git-gutter in vim
      vim.keymap.set('n', ']c', function()
        if vim.wo.diff then return ']c' end
        vim.schedule(function() gs.nav_hunk('next') end)
        return '<Ignore>'
      end, { expr = true, buffer = bufnr, desc = 'Next hunk' })
      vim.keymap.set('n', '[c', function()
        if vim.wo.diff then return '[c' end
        vim.schedule(function() gs.nav_hunk('prev') end)
        return '<Ignore>'
      end, { expr = true, buffer = bufnr, desc = 'Prev hunk' })
      vim.keymap.set('n', '<leader>s', gs.stage_hunk, { buffer = bufnr, desc = 'Stage hunk' })
      vim.keymap.set('n', '<leader>u', gs.reset_hunk, { buffer = bufnr, desc = 'Reset hunk' })
    end,
  })
end,
},
'tpope/vim-fugitive',
```

- Use `]c` and `[c` to navigate hunks (compatible with vim-gitgutter)
- Use `<leader>s` (comma + s in my setup) to toggle staging/unstaging hunks.
- Use `<leader>u` to do the equivalent of `git checkout -- file` for a single
  hunk.

The last two shortcuts are wherein the magic lives.

It is VERY convenient to choose what to stage/unstage/revert right from the
`nvim` buffer I am currently editing. For fine-grained control, I can always use
`:Gdiff` to perform hunk microsurgery.

[^1]: Internal mercurial VCS porcelain on top of Piper / google3.
[^2]: Not to confound with _hook_.
