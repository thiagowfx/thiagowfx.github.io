---
title: "LeetCode #694: Number of Distinct Islands"
date: 2026-01-10T01:50:25-03:00
tags:
  - dev
  - leetcode
categories:
  - coding
---

[LeetCode #694: Number of Distinct Islands](https://leetcode.com/problems/number-of-distinct-islands):

**Wrong answer**: 696 / 760 testcases passed. Directions do not uniquely
identify shapes. Counterexample:

```
1 1   1 1
1 0   0 1
```

These produce the same directions.

```python
from collections import deque

class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        ans: set[str] = set()

        def within_bounds(a, b):
            return 0 <= a < m and 0 <= b < n

        def bfs(x, y):
            queue = deque([(x, y)])
            h = [str((0, 0))] # hash

            while queue:
                (x, y) = queue.popleft()

                # if not within_bounds(x, y):
                #     continue

                ## if grid[x][y] == -1:
                ##    continue

                grid[x][y] = -1

                for dir in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                    neighbor = (
                        x + dir[0],
                        y + dir[1],
                    )

                    if within_bounds(neighbor[0], neighbor[1]) and grid[neighbor[0]][neighbor[1]] == 1:
                        queue.append((neighbor[0], neighbor[1]))
                        h.append(str(dir))

            ans.add(''.join(h))


        for x, row in enumerate(grid):
            for y, cell in enumerate(row):
                if cell == 1:
                    bfs(x, y)

        return len(ans)
```

Instead, store relative positions. Memory limit exceeded: 714 / 760 testcases
passed.

```python
from collections import deque

class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        ans: set[str] = set()

        def within_bounds(a, b):
            return 0 <= a < m and 0 <= b < n

        def bfs(initial_x, initial_y):
            queue = deque([(initial_x, initial_y)])
            h = [str((0, 0))] # hash

            while queue:
                (x, y) = queue.popleft()

                # if not within_bounds(x, y):
                #     continue

                ## if grid[x][y] == -1:
                ##    continue

                grid[x][y] = -1

                for dir in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                    neighbor = (
                        x + dir[0],
                        y + dir[1],
                    )

                    if within_bounds(neighbor[0], neighbor[1]) and grid[neighbor[0]][neighbor[1]] == 1:
                        queue.append((neighbor[0], neighbor[1]))
                        h.append(str((neighbor[0] - initial_x, neighbor[1] - initial_y)))

            ans.add(''.join(h))


        for x, row in enumerate(grid):
            for y, cell in enumerate(row):
                if cell == 1:
                    bfs(x, y)

        return len(ans)
```

We need to mark cells as visited right away, before queueing them:

```python
from collections import deque

class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        ans: set[str] = set()

        def within_bounds(a, b):
            return 0 <= a < m and 0 <= b < n

        def bfs(initial_x, initial_y):
            queue = deque([(initial_x, initial_y)])
            h = [(0, 0)] # hash
            grid[initial_x][initial_y] = -1

            while queue:
                (x, y) = queue.popleft()

                # if not within_bounds(x, y):
                #     continue

                ## if grid[x][y] == -1:
                ##    continue

                ## grid[x][y] = -1

                for dir in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                    neighbor = (
                        x + dir[0],
                        y + dir[1],
                    )

                    if within_bounds(neighbor[0], neighbor[1]) and grid[neighbor[0]][neighbor[1]] == 1:
                        queue.append((neighbor[0], neighbor[1]))
                        grid[neighbor[0]][neighbor[1]] = -1
                        h.append((neighbor[0] - initial_x, neighbor[1] - initial_y))

            ## ans.add(frozenset(h))
            ans.add(tuple(sorted(h))) # supposedly faster


        for x, row in enumerate(grid):
            for y, cell in enumerate(row):
                if cell == 1:
                    bfs(x, y)

        return len(ans)
```
