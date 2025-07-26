---
title: "vim: add word to spellchecker"
date: 2025-07-26T12:13:42+02:00
tags:
  - dev
  - serenity
---

When you have the spellchecker from `vim` turned on (`:set spell`), it
highlights words that are not in the dictionary.

False positives will occasionally be flagged.

To
[add](https://superuser.com/questions/133208/how-to-make-vim-spellcheck-remember-a-new-word)
the current word under the cursor to the dictionary, hit `zg`. From the `vim`
manual:

> To add words to your own word list:
>
> zg       Add word under the cursor as a good word to the first
>          name in 'spellfile'.  A count may precede the command
>          to indicate the entry in 'spellfile' to be used.  A
>          count of two uses the second entry.

Once you do so, you'll see feedback text in the status bar:

```
Word 'hacky' added to ~/.vim/spell/en.utf-8.add
```

This file can be easily tracked in your dotfiles.

```
Word 'dotfiles' added to ~/.vim/spell/en.utf-8.add
```
