---
title: "LeetCode #790: Domino and Tromino Tiling"
date: 2025-12-29T19:31:05-03:00
tags:
  - dev
  - leetcode

categories:
  - coding
---

[LeetCode #790: Domino and Tromino Tiling](https://leetcode.com/problems/domino-and-tromino-tiling):

```python
class Solution:
    def numTilings(self, n: int) -> int:
        mod = 10**9 + 7

        from functools import cache

        @cache
        def solve(n):
            if n < 0:
                return 0

            if n == 0:
                return 1

            if n == 1:
                return 1 # 1 domino, vertical

            if n == 2:
                return 2 # 2 dominos: vertical, horizontal

            if n == 3:
                return 5

            # solve(n - 1),  # 1 domino, vertical
            # solve(n - 2),  # 2 dominos, horizontal
            ans = solve(n - 1) + solve(n - 2)

            for k in range(3, n + 1):
                ans += 2 * solve(n - k)

            # return sum((
            #     2 * solve(n - 3),  # 2 trominos, |^- or 2 tromino, |
            #     2 * solve(n - 4),  # 2 trominos + 1 domino, |^- ^-| or |_ _|: 0 dominos blocking
            #     2 * solve(n - 5),  # [...]
            #     [...],
            # ))

            return ans

        return solve(n) % mod
```

This also works:

```python
ans += 2 * sum(solve(i) for i in range(n - 2))
```

Bottom-up DP:

```python
class Solution:
    def numTilings(self, n: int) -> int:
        mod = 10**9 + 7

        if n == 0:
            return 0

        if n == 1:
            return 1

        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1
        dp[2] = 2

        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2] + 2 * sum(dp[i] for i in range(i - 2))

        return dp[n] % mod
```
