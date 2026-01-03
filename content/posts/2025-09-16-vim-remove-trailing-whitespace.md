---
title: "vim: remove trailing whitespace"
date: 2025-09-16T14:27:55+02:00
tags:
  - dev
  - vim
---

A simple addition to remove all trailing whitespace from the current buffer by
pressing `,t`[^1]
([via](https://vi.stackexchange.com/questions/454/whats-the-simplest-way-to-strip-trailing-whitespace-from-all-lines-in-a-file)):

```
% GIT_PAGER=cat git show
commit 1c22fcbc12ffd2cb3c40152d152d099c9a9b7f85 (HEAD -> master, origin/master, origin/HEAD)
Author: Thiago Perrotta <{redacted}>
Date:   Tue Sep 16 14:26:46 2025 +0200

    vim: remove trailing whitespace

diff --git vim/.vim/vimrc vim/.vim/vimrc
index 8cf33d8..004beda 100644
--- vim/.vim/vimrc
+++ vim/.vim/vimrc
@@ -60,6 +60,9 @@ nnoremap J gJ
 " Reflow current paragraph
 nnoremap <silent> Q gwip

+" Remove all trailing whitespace
+nnoremap <leader>t :let _s=@/<Bar>:%s/\s\+$//e<Bar>:let @/=_s<Bar><CR>
+
 " Always use vertical diff splits.
 set diffopt+=vertical
```

[^1]: My [leader](https://stackoverflow.com/questions/1764263/what-is-the-leader-in-a-vimrc-file) key is mapped to `,`.
