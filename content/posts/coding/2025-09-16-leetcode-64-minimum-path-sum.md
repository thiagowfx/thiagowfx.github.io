---
title: "LeetCode #64: Minimum Path Sum"
date: 2025-09-16T01:41:29+02:00
tags:
  - dev

categories:
  - coding
---

[LeetCode #64: Minimum Path Sum](https://leetcode.com/problems/minimum-path-sum/):

```python
from functools import cache

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        @cache
        def solve(row, col):
            assert row >= 0, col >= 0

            if row >= rows or col >= cols:
                return None

            if row == (rows - 1) and col == (cols - 1):
                return grid[row][col]

            def valid(x, default=float('inf')):
                return x if x is not None else default

            return grid[row][col] + min(
                valid(solve(row + 1, col)),
                valid(solve(row, col + 1)),
            )

        return solve(0, 0)
```

If you do not like `valid()`, the classic option is to cache each branch in a
local variable:

```python
from functools import cache

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        @cache
        def solve(row, col):
            assert row >= 0, col >= 0

            if row >= rows or col >= cols:
                return None

            if row == (rows - 1) and col == (cols - 1):
                return grid[row][col]

            ans1 = solve(row + 1, col)
            ans2 = solve(row, col + 1)
            ans = 0

            if ans1 is None:
                ans = ans2
            elif ans2 is None:
                ans = ans1
            else:
                ans = min(ans1, ans2)

            return grid[row][col] + ans
```

Previously:

```python
from functools import cache

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        @cache
        def solve(x, y):
            ans1 = grid[x][y]

            down = None
            if x + 1 < rows:
                down = solve(x + 1, y)

            right = None
            if y + 1 < cols:
                right = solve(x, y + 1)

            if down is None and right is None:
                return ans1
            elif down is None:
                return ans1 + right
            elif right is None:
                return ans1 + down
            else:
                return ans1 + min(down, right)

        return solve(0, 0)
```

Modern:

```python
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        from functools import cache

        @cache
        def solve(m, n):
            if m < 0 or n < 0:
                return float('inf')

            if m == 0 and n == 0:
                return grid[m][n]

            return grid[m][n] + min(
                solve(m - 1, n),
                solve(m, n - 1),
            )

        return solve(m - 1, n - 1)
```
