---
title: "vim: spellchecker suggestions"
date: 2025-11-02T11:37:57+01:00
tags:
  - dev
  - vim
---

[Previously]({{< ref "2025-07-26-vim-add-word-to-spellchecker" >}}):

> When you have the spellchecker from `vim` turned on (`:set spell`), it
highlights words that are not in the dictionary.

It turns out `vim`[^1] can also suggest corrections to these words.

`:h z=`:

```
z=   For the word under/after the cursor suggest correctly
     spelled words.  This also works to find alternatives
     for a word that is not highlighted as a bad word,
     e.g., when the word after it is bad.
     In Visual mode the highlighted text is taken as the
     word to be replaced.
     The results are sorted on similarity to the word being
     replaced.
     This may take a long time.  Hit CTRL-C when you get
     bored.
```

For example: take the word `exampl`. When pressing `z=`:

```
Change "exampl" to:
 1 "example"
 2 "example" < "exampl."
 3 "exam pl"
 4 "exempt"
 5 "exam Pl"
 6 "exam"
 ```

Upon pressing `1<Enter>` it is automatically replaced.

Alternatively we can skip the suggestions and simply [pick the first
one](https://www.jakeworth.com/tils/select-first-spell-suggestion/) right away
with `1z=`.

[^1]: `vim` never ceases to amaze me.
