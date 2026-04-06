---
title: "Delete newlines in a pipe"
url: https://perrotta.dev/2025/04/delete-newlines-in-a-pipe/
last_updated: 2025-06-15
---


**Problem statement**: Given `{cmd}` that emits lots of blank lines, delete all
blank lines in a pipe.

The following is a very elegant (and easy to remember!) way to do so:

```shell
{cmd} | awk 'NF'
```

From the LLM:

> When you use awk 'NF', it evaluates to true for lines where NF is greater than
> zero—that is, lines that are not empty or do not consist solely of whitespace.
> This makes it a concise way to filter out blank lines.

Other ways with classic tools and regular expressions:

```shell
{cmd} | grep -v '^[[:space:]]*$'
{cmd} | sed -e '/^[[:space:]]*$/d'
```

They are just a bit harder to remember.

