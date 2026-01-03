---
title: "LeetCode #62: Unique Paths"
date: 2025-12-28T21:50:55-03:00
tags:
  - dev

categories:
  - coding
---

[LeetCode #62: Unique Paths](https://leetcode.com/problems/unique-paths):

```python
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        from functools import cache

        @cache
        def solve(m, n):
            if m == 0 and n == 0:
                return 1

            if m < 0 or n < 0:
                return 0

            return solve(m - 1, n) + solve(m, n - 1)

        return solve(m - 1, n - 1)
```
