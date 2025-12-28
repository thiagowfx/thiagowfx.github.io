---
title: "LeetCode #518: Coin Change II"
date: 2025-12-28T07:51:45-03:00
tags:
  - coding
rss: false
---

[LeetCode #518: Coin Change II](https://leetcode.com/problems/coin-change-ii):

```python
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        from functools import cache

        @cache
        def solve(amount, i):
            if amount < 0:
                return 0

            if amount == 0:
                return 1

            if i < 0:
                return 0

            return sum((
                solve(amount - coins[i], i),
                solve(amount, i - 1),
            ))

        return solve(amount, len(coins) - 1
```
