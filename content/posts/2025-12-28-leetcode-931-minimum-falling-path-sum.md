---
title: "LeetCode #931: Minimum Falling Path Sum"
date: 2025-12-28T22:17:55-03:00
tags:
  - coding
rss: false
---

[LeetCode #931: Minimum Falling Path Sum](https://leetcode.com/problems/minimum-falling-path-sum):

```python
class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])

        from functools import cache

        @cache
        def solve(i, j):
            if i < 0 or j < 0 or i >= m or j >= n:
                return float('inf')

            if i == 0:
                return matrix[0][j]

            return matrix[i][j] + min(
                solve(i - 1, j - 1),
                solve(i - 1, j),
                solve(i - 1, j + 1),
            )

        return min(solve(m - 1, col) for col in range(n))
```
