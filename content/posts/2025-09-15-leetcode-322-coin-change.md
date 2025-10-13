---
title: "LeetCode #322: Coin Change"
date: 2025-09-15T23:25:06+02:00
tags:
  - coding
rss: false
---

[LeetCode #322: Coin Change](https://leetcode.com/problems/coin-change/):

```python
from functools import cache

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        @cache
        def solve(i, amount):
            """
            Number of coins needed to complete amount for 0..i.
            """
            if amount < 0:
                return -1 # TODO: Beware

            if amount == 0:
                return 0

            if i < 0:
                return -1

            # use current coin
            # need to add 1 to the return of solve
            ans1 = solve(i, amount - coins[i])

            # do not use current coin
            ans2 = solve(i - 1, amount)

            if ans1 == -1:
                return ans2
            if ans2 == -1:
                return ans1 + 1
            return min(ans1 + 1, ans2)

        return solve(len(coins) - 1, amount)
```

Previously:

```python
from functools import cache

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
       coins.sort(key=lambda x: -x)

       @cache
       def solve(index, amount):
           if index >= len(coins):
               return -1

           if amount == 0:
               return 0

           if amount < 0:
               return -1

           s1 = solve(index, amount - coins[index])
           s2 = solve(index + 1, amount)

           if s1 == -1 and s2 == -1:
               return -1
           elif s1 == -1:
               return s2
           elif s2 == -1:
               return s1 + 1
           else:
               return min(s1 + 1, s2)

       return solve(0, amount)
```

Sorting the `coins` list provides no apparent benefit.
