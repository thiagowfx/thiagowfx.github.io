---
title: "LeetCode #120: Triangle"
url: https://perrotta.dev/2025/09/leetcode-%23120-triangle/
last_updated: 2026-01-03
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

