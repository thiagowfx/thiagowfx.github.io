---
title: "LeetCode #97: Interleaving String"
date: 2025-12-30T04:56:17-03:00
tags:
  - dev

categories:
  - coding
---

[LeetCode #97: Interleaving String](https://leetcode.com/problems/leetcode-#97:-interleaving-string):

```python
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        from functools import cache

        n = len(s1)
        m = len(s2)

        @cache
        def solve(i, j):
            assert i >= 0
            assert j >= 0
            k = i + j

            if i >= n and j >= m:
                return i + j == len(s3)

            if i >= n:
                return solve(i, j + 1) if i + j < len(s3) and s2[j] == s3[i + j] else False

            if j >= m:
                return solve(i + 1, j) if i + j < len(s3) and s1[i] == s3[i + j] else False

            return any([
                solve(i + 1, j) if i + j < len(s3) and s1[i] == s3[i + j] else False,
                solve(i, j + 1) if i + j < len(s3) and s2[j] == s3[i + j] else False,
            ])

        return solve(0, 0)
```
