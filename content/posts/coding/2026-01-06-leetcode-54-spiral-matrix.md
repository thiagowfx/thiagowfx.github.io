---
title: "LeetCode #54: Spiral Matrix"
date: 2026-01-06T14:07:11-03:00
tags:
  - dev
  - leetcode
categories:
  - coding
---

[LeetCode #54: Spiral Matrix](https://leetcode.com/problems/spiral-matrix):

Modify input (easier):

```python
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []

        dirs = [
            (0, 1),
            (1, 0),
            (0, -1),
            (-1, 0)
        ]
        idir = 0

        m = len(matrix)
        n = len(matrix[0])

        def within_bounds(x, y, m, n):
            return 0 <= x < m and 0 <= y < n

        ans = []
        pos = [0, 0]
        new_pos = [None, None]

        ## while True
        while len(ans) < m * n:
            ans.append(matrix[pos[0]][pos[1]])
            matrix[pos[0]][pos[1]] = None

            new_pos[0] = pos[0] + dirs[idir][0]
            new_pos[1] = pos[1] + dirs[idir][1]

            if within_bounds(new_pos[0], new_pos[1], m, n) and matrix[new_pos[0]][new_pos[1]] is not None:
                pos[0] = new_pos[0]
                pos[1] = new_pos[1]
            else:
                idir = (idir + 1) % len(dirs)

                new_pos[0] = pos[0] + dirs[idir][0]
                new_pos[1] = pos[1] + dirs[idir][1]

                if within_bounds(new_pos[0], new_pos[1], m, n) and matrix[new_pos[0]][new_pos[1]] is not None:
                    pos[0] = new_pos[0]
                    pos[1] = new_pos[1]
                else:
                    return ans

        return ans
```

Classic:

```
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans = []

        start = (0, 0)
        end = (len(matrix) - 1, len(matrix[0]) - 1)

        def debian_once(start, end):
            (x1, y1) = start
            (x2, y2) = end

            # -> right
            for y in range(y1, y2 + 1):
                ans.append(matrix[x1][y])

            # \/ down
            for x in range(x1 + 1, x2):
                ans.append(matrix[x][y2])

            # <- left
            if x2 > x1:
                for y in range(y2, y1 - 1, -1):
                    ans.append(matrix[x2][y])

            # /\ up
            if y2 > y1:
                for x in range(x2 - 1, x1, -1):
                    ans.append(matrix[x][y1])

        while all(x <= y for (x, y) in zip(start, end)):
            debian_once(start, end)
            start = tuple(el + 1 for el in start)
            end = tuple(el - 1 for el in end)

        return ans
```
