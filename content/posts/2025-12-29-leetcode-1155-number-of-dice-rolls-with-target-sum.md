---
title: "LeetCode #1155: Number of Dice Rolls With Target Sum"
date: 2025-12-29T19:02:58-03:00
tags:
  - coding
rss: false
---

[LeetCode #1155: Number of Dice Rolls With Target Sum](https://leetcode.com/problems/number-of-dice-rolls-with-target-sum):

```python
class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        mod = 10 ** 9 + 7

        from functools import cache

        @cache
        def solve(die_left, mysum = 0):
            # out of bounds
            if mysum > target:
                return 0

            if die_left == 0:
                return int(mysum == target)

            ans = 0
            for d in range(1, k + 1):
                ans += solve(die_left - 1, mysum + d)

            return ans

        return solve(n) % mod
```
