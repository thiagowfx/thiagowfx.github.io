---
title: "LeetCode #1790: Check if One String Swap Can Make Strings Equal"
date: 2026-01-06T13:55:09-03:00
tags:
  - dev
  - leetcode
categories:
  - coding
---

[LeetCode #1790: Check if One String Swap Can Make Strings Equal](https://leetcode.com/problems/check-if-one-string-swap-can-make-strings-equal):

```python
class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if len(s1) != len(s2):
            return False

        diff = []

        for (c1, c2) in zip(s1, s2):
            if c1 != c2:
                diff.append((c1, c2))
                if len(diff) > 2:
                    return False

        ## [(b, k), (k, b)]
        return set(c1 for (c1, _) in diff) ==  set(c2 for (_, c2) in diff)
```
