---
title: "LeetCode #498: Diagonal Traverse"
date: 2026-01-06T03:01:27-03:00
tags:
  - dev
  - leetcode
categories:
  - coding
---

[LeetCode #498: Diagonal Traverse](https://leetcode.com/problems/diagonal-traverse):

Headshot!

```python
class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        pos = [0, 0]

        dirs = [(-1, 1), (1, -1)]
        idir = 0

        def is_within_bounds(x, y, mat):
            return 0 <= x < len(mat) and 0 <= y < len(mat[0])

        m = len(mat)
        n = len(mat[0])
        total = m * n

        ans = []

        while len(ans) < total:
            ans.append(mat[pos[0]][pos[1]])

            new_pos = [0, 0]

            new_pos[0] = pos[0] + dirs[idir][0]
            new_pos[1] = pos[1] + dirs[idir][1]

            if not is_within_bounds(new_pos[0], new_pos[1], mat):
                tries = []
                if idir == 0:
                    tries = [(0, 1), (1, 0)]
                else:
                    tries = [(1, 0), (0, 1)]

                for tri in tries:
                    new_pos[0] = pos[0] + tri[0]
                    new_pos[1] = pos[1] + tri[1]

                    if is_within_bounds(new_pos[0], new_pos[1], mat):
                        break

                idir = (idir + 1) % 2

            pos[0] = new_pos[0]
            pos[1] = new_pos[1]

        return ans
```
