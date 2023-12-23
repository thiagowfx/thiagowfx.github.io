---
title: "Transfer bash history to zsh"
date: 2022-02-04T21:58:50-05:00
tags:
  - dev
  - linux
---

After years of using `bash` as my default interactive shell at $DAYJOB,
I decided to switch to `zsh`. I didn't want to start from scratch and lose all
my history though:

```shell
$ wc -l ~/.bash_history | cut -f1 -d' '
64002
```

Thus my goal was to first migrate all my history from `bash` to `zsh`.

<!--more-->

The `bash-to-zsh-hist.py` python script in this
[gist](https://gist.github.com/muendelezaji/c14722ab66b505a49861b8a74e52b274)
did most of the job:

```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# This is how I used it:
# $ cat ~/.bash_history | python bash-to-zsh-hist.py >> ~/.zsh_history

import sys
import time

def main():
    timestamp = None
    for line in sys.stdin.readlines():
        line = line.rstrip('\n')
        if line.startswith('#') and timestamp is None:
            t = line[1:]
            if t.isdigit():
                timestamp = t
                continue
        else:
            sys.stdout.write(': %s:0;%s\n' % (timestamp or time.time(), line))
            timestamp = None

if __name__ == '__main__':
    main()
```

To use it:

```shell
$ wget https://gist.githubusercontent.com/muendelezaji/c14722ab66b505a49861b8a74e52b274/raw/49f0fb7f661bdf794742257f58950d209dd6cb62/bash-to-zsh-hist.py
$ chmod +x ./bash-to-zsh-hist.py
$ cat .bash_history | ./bash-to-zsh-hist.py >> ~/.zsh_history
```

However, that didn't fully work. Upon running `zsh`, there was an error:

```shell
$ zsh
zsh: corrupt history file /usr/local/google/home/tperrotta/.zsh_history
```

A quick google search led me to [a blog post](https://shapeshed.com/zsh-corrupt-history-file/). I adapted the command suggest therein[^1]:

```shell
$ strings -eS .zsh_history | sponge .zsh_history
```

And that fixed the issue!

[^1]: `sponge` comes from the [moreutils](https://joeyh.name/code/moreutils/) package.
