---
title: "LeetCode #195: Tenth line"
date: 2025-12-06T04:05:42-03:00
categories:
  - coding
---

[LeetCode #195: Tenth line](https://leetcode.com/problems/tenth-line):

```shell
sed -n '10p' file.txt
```

`-n` is necessary to suppress other output.

If we do not know `sed`, then `head` + `tail` is a decent combination.

```shell
head -n 10 file.txt | tail -1
```

The above fails the edge case of <10 lines. The fix is straightforward:

```shell
if [[ $(head -n 10 file.txt | wc -l) -ge 10 ]]; then
    head -n 10 file.txt | tail -1
fi
```
