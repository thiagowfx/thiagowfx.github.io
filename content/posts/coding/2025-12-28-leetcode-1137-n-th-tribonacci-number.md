---
title: "LeetCode #1137: N-th Tribonacci Number"
date: 2025-12-28T06:48:41-03:00
rss: false
categories:
  - coding
---

[LeetCode #1137: N-th Tribonacci Number](https://leetcode.com/problems/n-th-tribonacci-number):

```python
class Solution:
    def tribonacci(self, n: int) -> int:
        from functools import cache

        @cache
        def tribo(n):
            if n == 0:
                return 0

            if n in (1, 2):
                return 1

            return tribo(n - 1) + tribo(n - 2) + tribo(n - 3)

        return tribo(n)
```
