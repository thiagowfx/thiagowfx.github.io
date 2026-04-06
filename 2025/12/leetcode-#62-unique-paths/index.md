---
title: "LeetCode #62: Unique Paths"
url: https://perrotta.dev/2025/12/leetcode-%2362-unique-paths/
last_updated: 2026-01-03
---


[LeetCode #62: Unique Paths](https://leetcode.com/problems/unique-paths):

```python
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        from functools import cache

        @cache
        def solve(m, n):
            if m == 0 and n == 0:
                return 1

            if m < 0 or n < 0:
                return 0

            return solve(m - 1, n) + solve(m, n - 1)

        return solve(m - 1, n - 1)
```

