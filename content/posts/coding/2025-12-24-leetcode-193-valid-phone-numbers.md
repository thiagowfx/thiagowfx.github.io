---
title: "LeetCode #193: Valid Phone Numbers"
date: 2025-12-24T16:47:49-03:00
rss: false
categories:
  - coding
---

[LeetCode #193: Valid Phone Numbers](https://leetcode.com/problems/valid-phone-numbers):

```shell
# Read from the file file.txt and output all valid phone numbers to stdout.
grep -E '^\([0-9]{3}\) [0-9]{3}-[0-9]{4}$|^[0-9]{3}-[0-9]{3}-[0-9]{4}$' file.txt
```

`egrep` is the easiest way to go. It is a bit hard to remember its syntax.

A bit more optimized, grouping alternations at the beginning:

```shell
# Read from the file file.txt and output all valid phone numbers to stdout.
grep -E '^(\([0-9]{3}\) [0-9]{3}|[0-9]{3}-[0-9]{3})-[0-9]{4}$' file.txt
```
