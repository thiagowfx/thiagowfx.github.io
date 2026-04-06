---
title: "LeetCode #746: Min Cost Climbing Stairs"
url: https://perrotta.dev/2025/12/leetcode-%23746-min-cost-climbing-stairs/
last_updated: 2026-01-03
---


[LeetCode #746: Min Cost Climbing Stairs](https://leetcode.com/problems/min-cost-climbing-stairs):

```python
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        from functools import cache

        n = len(cost)

        @cache
        def solve(i):
            assert i >= 0

            if i >= n:
                return 0

            return min(
                cost[i] + solve(i + 1),
                cost[i] + solve(i + 2),
            )

        return min(solve(0), solve(1))
```

Or the other way around:

```python
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        from functools import cache

        @cache
        def solve(n):
            if n <= 1:
                return 0

            return min(
                cost[n - 1] + solve(n - 1),
                cost[n - 2] + solve(n - 2),
            )


        return solve(len(cost))
```

