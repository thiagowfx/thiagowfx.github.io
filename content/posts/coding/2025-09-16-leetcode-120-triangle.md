---
title: "LeetCode #120: Triangle"
date: 2025-09-16T01:20:40+02:00
categories:
  - coding
---

[LeetCode #120: Triangle](https://leetcode.com/problems/triangle/):

```python
from functools import cache

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        rows = len(triangle)

        @cache
        def solve(row, col):
            assert row >= 0, col >= 0

            if row >= rows:
                return 0

            return triangle[row][col] + min(
                solve(row + 1, col),
                solve(row + 1, col + 1)
            )

        return solve(0, 0)
```
