---
title: "LeetCode #63: Unique Paths II"
date: 2025-09-16T02:02:15+02:00
tags:
  - coding
---

[LeetCode #63: Unique Paths II](https://leetcode.com/problems/unique-paths-ii/):

```python
from functools import cache

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        grid = obstacleGrid
        rows = len(grid)
        cols = len(grid[0])

        @cache
        def solve(row, col):
            assert row >= 0, col >= 0

            if row >= rows or col >= cols:
                return 0

            if grid[row][col] == 1:
                return 0

            if row == (rows - 1) and col == (cols - 1):
                return 1

            return solve(row + 1, col) + solve(row, col + 1)

        return solve(0, 0)
```

Note that the rightmost bottommost square can have an obstacle.

As such, the check:

```python
if grid[row][col] == 1:
  return 0
```

...must come before:

```python
if row == (rows - 1) and col == (cols - 1):
    return 1
```
