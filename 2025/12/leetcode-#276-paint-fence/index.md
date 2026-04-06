---
title: "LeetCode #276: Paint Fence"
url: https://perrotta.dev/2025/12/leetcode-%23276-paint-fence/
last_updated: 2026-01-03
---


[LeetCode #276: Paint Fence](https://leetcode.com/problems/paint-fence):

```python
class Solution:
    def numWays(self, n: int, k: int) -> int:
        from functools import cache

        @cache
        def solve(n):
            if n <= 0:
                return 0

            if n == 1:
                return k

            if n == 2:
                return k ** 2

            return (k - 1) *  (solve(n - 1) + solve(n - 2))

        return solve(n)
```

