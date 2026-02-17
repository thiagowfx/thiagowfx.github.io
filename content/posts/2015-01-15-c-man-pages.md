---
title: "C++ man pages"
date: 2015-01-15T13:00:00-03:00
tags:
  - dev
  - legacy
---

Today I stumbled upon across a project called `cppman`[^1], which I believe has
a very suggestive name indeed. Manual pages for the C programming language are
almost always available on Unix systems. Don't you remember the signature of the
`qsort` function? No problem, a `man 3 qsort` will refresh your memory. What
about `printf`? What about `stdlib.h`? **Man** won't disappoint you. However,
what about C++ man pages? I first discovered that they weren't available by
default about three years ago. Okay, so what do I do? A simple google search
will probably lead you to Stack Overflow[^2]. At the aforementioned time, there
weren't really useful answers in there. Okay, some of them pointed out to
`libstd++` docs, but using them wasn't much convenient. The best documentation
sources you could find were cplusplus.com and cppreference wiki[^3]. You can
live with these on-line references, but you will quickly get bored with them.
Now, back to `cppman`, the boredom killer and time saver.

## cppman — quick reference

### Installing it

* If you're an user of Arch Linux, it is available in the AUR at the time I'm
  writing this post.
* Otherwise, you can install it using python's `pip` – ya know, `pip install
  cppman`.

It doesn't really matter the method you choose, just make sure to add it to your
`PATH`.

### Using it

```shell
cppman sort
cppman map
```

Don't cry, it is real. You can optionally cache all of its man pages, but I
don't find this strictly necessary for me. The default option (no cache)
downloads manual pages on-demand. Oh, it uses `vim` as its default pager, so you
can search for keywords with `/`. Also, hyperlinks are everywhere, so you can
use `K` or `C-]` to follow them. To go back, use `C-t`. By the way, it is
compatible with `man`, so if you decide to cache its man pages, you can view
them later with `man` (instead of `cppman`). Happy ~~hacking~~ reading![^4]

## Footnotes

[^1]: cppman — you don't need to read the whole article; if you're in a hurry,
    just open the project page and forget me!

[^2]: As always, huh? Stack Overflow thread.

[^3]: The last one is **by far** much better maintained.

[^4]: Wait, since when reading manual pages is a source of happiness?
