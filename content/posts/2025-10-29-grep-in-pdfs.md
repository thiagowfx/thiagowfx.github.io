---
title: "Grep in PDFs"
date: 2025-10-29T01:59:08+01:00
tags:
  - dev
---

**Problem statement**: `grep`[^1] for a given string in a multitude of
multi-page PDF files:

```shell
% du -sh very_large_file.zip
513M    very_large_file.zip

% unzip very_large_file.zip
[...]

% ls -1 *.pdf | wc -l
6816
```

There's a tool called [`ripgrep-all`](https://github.com/phiresky/ripgrep-all)
(short: `rga`) that is perfect for that. And yes, it resembles our good ol'
`ripgrep` (short: `rg`).

It is [widely available](https://repology.org/project/ripgrep-all/versions) in
most package managers.

I install it with `homebrew`:

```shell
% brew install ripgrep-all  # or rga
```

Upon running it with:

```shell
% rga -i "perrotta"
```

...it did not initially work. `pdftotext` is a required dependency that was
missing.

[Where](https://superuser.com/questions/781693/how-to-determine-which-brew-package-provides-a-given-file) can we obtain `pdftotext`?

```shell
% brew which-formula pdftotext
pdf2image
poppler
poppler-qt5
xpdf
```

I installed `poppler`, as it is quite well-known in the Linux world.

The search works as expected afterwards:

```shell
% rga -i perrotta
my_cool_file_000.pdf
Page 12: HELLO PERROTTA GOODBYE

my_cool_file_001.pdf
Page 123: SERVUS PERROTTA CIAO
```

[^1]: grep foo, grep _in_ foo, or grep _for_ foo? Ah, English prepositions.
