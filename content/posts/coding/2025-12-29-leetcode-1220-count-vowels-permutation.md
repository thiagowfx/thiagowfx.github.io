---
title: "LeetCode #1220: Count Vowels Permutation"
date: 2025-12-29T14:39:50-03:00
tags:
  - dev
  - leetcode

categories:
  - coding
---

[LeetCode #1220: Count Vowels Permutation](https://leetcode.com/problems/count-vowels-permutation):

Top-down DP. It is correct but we get Memory Limit Exceeded, as you would
expect.

```python
class Solution:
    def countVowelPermutation(self, n: int) -> int:
        assert n > 0

        mod = 10 ** 9 + 7

        from functools import cache

        @cache
        def solve(i, prev = ''):
            if i >= n:
                return 1

            if prev == 'a':
                return solve(i + 1, 'e')
            elif prev == 'e':
                return (solve(i + 1, 'a') + solve(i + 1, 'i'))
            elif prev == 'i':
                return (solve(i + 1, 'a') + solve(i + 1, 'e') + solve(i + 1, 'o') + solve(i + 1, 'u'))
            elif prev == 'o':
                return (solve(i + 1, 'i') + solve(i + 1, 'u'))
            elif prev == 'u':
                return solve(i + 1, 'a')
            else:
                return (solve(i + 1, 'a') + solve(i + 1, 'e') + solve(i + 1, 'i') + solve(i + 1, 'o') + solve(i + 1, 'u'))

        return solve(0) % mod
```

Bottom-up DP:

```python
class Solution:
    def countVowelPermutation(self, n: int) -> int:
        assert n > 0

        mod = 10 ** 9 + 7

        # dp = [[0, 0, 0, 0, 0], ...]: n times
        dp = [[0] * 5 for _ in range(n)]

        assert len(dp) == n
        assert len(dp[0]) == 5

        # Base case
        for j in range(5):
            dp[n - 1][j] = 1
        # dp[n][0] = dp[n][1] = dp[n][2] = dp[n][3] = dp[n][4] = 1

        for i in range(n)[::-1][1:]: # n = 4: 2, 1, 0
        # for i in range(n - 2, -1, -1):
            dp[i][0] = dp[i + 1][1]
            dp[i][1] = dp[i + 1][0] + dp[i + 1][2]
            dp[i][2] = dp[i + 1][0] + dp[i + 1][1] + dp[i + 1][3] + dp[i + 1][4]
            dp[i][3] = dp[i + 1][2] + dp[i + 1][4]
            dp[i][4] = dp[i + 1][0]

        return sum(dp[0]) % mod
```
