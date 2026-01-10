---
title: "LeetCode #1254: Number of Closed Islands"
date: 2026-01-10T01:23:06-03:00
tags:
  - dev
  - leetcode
categories:
  - coding
---

[LeetCode #1254: Number of Closed Islands](https://leetcode.com/problems/number-of-closed-islands):

Recursive:

```python
class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        def within_bounds(a, b):
            return 0 <= a < m and 0 <= b < n

        def dfs(x, y, poisoned=False):
            if not within_bounds(x, y):
                return True

            if grid[x][y] in [-1, 1]:
                return False

            grid[x][y] = -1

            for dir in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                neighbor = (
                    x + dir[0],
                    y + dir[1],
                )
                if dfs(neighbor[0], neighbor[1]):
                    poisoned = True

            return poisoned

        ans = 0

        for x, row in enumerate(grid):
            for y, cell in enumerate(row):
                if grid[x][y] == 0:
                    if not dfs(x, y):
                        ans += 1

        return ans
```

Iterative:

```python
class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        def within_bounds(a, b):
            return 0 <= a < m and 0 <= b < n

        def dfs(x, y):
            valid = True

            stack = [(x, y)]

            while stack:
                (x, y) = stack.pop()

                if not within_bounds(x, y):
                    valid = False
                    continue

                if grid[x][y] in [-1, 1]:
                    continue

                ## assert grid[x][y] == 0
                grid[x][y] = -1

                for dir in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                    neighbor = (
                        x + dir[0],
                        y + dir[1],
                    )
                    ## if not within_bounds(neighbor[0], neighbor[1]):
                    ##     return False
                    stack.append((neighbor[0], neighbor[1]))

            return valid

        ans = 0

        for x, row in enumerate(grid):
            for y, cell in enumerate(row):
                if grid[x][y] == 0:
                    ans += dfs(x, y)

        return ans
```
