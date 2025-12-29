---
title: "LeetCode #1220: Count Vowels Permutation"
date: 2025-12-29T14:39:50-03:00
tags:
  - coding
rss: false
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
