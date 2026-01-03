---
title: "LeetCode #474: Ones and Zeroes"
date: 2025-12-28T05:24:05-03:00
tags:
  - dev

categories:
  - coding
---

[LeetCode #474: Ones and Zeroes](https://leetcode.com/problems/ones-and-zeroes):

```python
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        from functools import cache

        @cache
        def solve(i, m, n):
            if i < 0:
                return 0

            # take
            a = None
            new_m = m - strs[i].count('0')
            new_n = n - strs[i].count('1')

            if new_m >= 0 and new_n >= 0:
                a = 1 + solve(i - 1, new_m, new_n)

            # do not take
            b = 0 + solve(i - 1, m, n)

            return max(el for el in (a, b, 0) if el is not None)

        return solve(len(strs) - 1, m, n)
```

Lazy, risky:

```python
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        from functools import cache

        @cache
        def solve(i, m, n):
            if m < 0 or n < 0:
                return -1

            if i < 0:
                return 0

            # take
            a = 1 + solve(i - 1, m - strs[i].count('0'), n - strs[i].count('1'))

            # do not take
            b = 0 + solve(i - 1, m, n)

            return max(a, b)

        return solve(len(strs) - 1, m, n)
```
