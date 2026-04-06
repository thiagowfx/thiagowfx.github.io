---
title: "LeetCode #193: Valid Phone Numbers"
url: https://perrotta.dev/2025/12/leetcode-%23193-valid-phone-numbers/
last_updated: 2026-01-03
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

