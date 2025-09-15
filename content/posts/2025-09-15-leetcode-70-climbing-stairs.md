---
title: "LeetCode #70: Climbing Stairs"
date: 2025-09-15T22:35:21+02:00
tags:
  - coding
---

[LeetCode #70: Climbing Stairs](https://leetcode.com/problems/climbing-stairs/):

```python
from functools import cache

class Solution:
    def climbStairs(self, n: int) -> int:

        @cache
        def cs(n):
            """How many possibilities for n steps?"""
            assert n >= 0

            if n in [0, 1, 2]:
                return n

            return cs(n-1) + cs(n-2)

        return cs(n)
```

Previously:

```python
from functools import cache

class Solution:
    def climbStairs(self, n: int) -> int:

        @cache
        def solve(n):
            if n == 1:
                return 1

            if n == 2:
                return 2

            return solve(n - 1) + solve(n - 2)

        return solve(n)
```
