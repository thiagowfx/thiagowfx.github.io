---
title: "vim: reflow current paragraph"
date: 2025-10-08T18:03:57+02:00
tags:
  - dev
  - vim
---

**Problem statement**: Given a paragraph (`lorem_ipsum.txt`):

```
"Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
```

Reflow it in such a way each line does not exceed a certain number of
characters, say, in the 72-80 range. The number is not important, so
long as it is applied consistently and uniformly within a single file.

In the terminal we can achieve that with [`fmt(1)`](https://man.archlinux.org/man/fmt.1):

```shell
% cat lorem_ipsum.txt
"Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
thiago@thiagoperrotta-MacBook-Pro /tmp/thiago.perrotta-2025-10-08-eOaLRg
% fmt lorem_ipsum.txt
"Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod
tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim
veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea
commodo consequat. Duis aute irure dolor in reprehenderit in voluptate
velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat
cupidatat non proident, sunt in culpa qui officia deserunt mollit anim
id est laborum."
```

We can also do it in-place ([sponge(1)](https://man.archlinux.org/man/sponge.1) from [moreutils]({{< ref "2022-05-01-tools-you-should-know-about-moreutils" >}})):

```shell
% fmt lorem_ipsum.txt | sponge lorem_ipsum.txt
% cat lorem_ipsum.txt
"Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod
tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim
veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea
commodo consequat. Duis aute irure dolor in reprehenderit in voluptate
velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat
cupidatat non proident, sunt in culpa qui officia deserunt mollit anim
id est laborum."
```

Can we do it within `vim`? Yes, with the following mapping:

```vim
nnoremap <silent> W <Esc>!ipfmt<Enter>
```

Translation:

- `<silent>`: does not echo the mapping in the vim command line
- `<Esc>`: switch to normal mode
- `!`: `!{motion}{filter} Filter {motion} text lines through the external program {filter}.` (via `:h !`).
  — Not to confound this with `:!`: `:!{cmd} Execute {cmd} with the shell. See also the 'shell' and 'shelltype' option.  For the filter command, see |:range!|.` (via `:h :!`)
- `ip`: "inner paragraph" motion
- `fmt`: the filter command
- `<Enter>`: execute the command

Alternatively:

```vim
nnoremap <silent> Q gwip
```

Wherein `:h gw`:

```
gw{motion}	Format the lines that {motion} moves over.  Similar to
			|gq| but puts the cursor back at the same position in
			the text.  However, 'formatprg' and 'formatexpr' are
			not used.
```

One difference is that `gw` accounts for comment characters, whereas `fmt` does
not. Example, given a `.py` (python) file:

```
# "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
```

`gw` does:

```
# "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod
# tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,
# quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo
# consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse
# cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non
# proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
```

Whereas `fmt` does:

```
# "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad
minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip
ex ea commodo consequat. Duis aute irure dolor in reprehenderit in
voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur
sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt
mollit anim id est laborum."
```
