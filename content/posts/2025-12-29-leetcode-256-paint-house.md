---
title: "LeetCode #256: Paint House"
date: 2025-12-29T13:48:38-03:00
tags:
  - coding
rss: false
---

[LeetCode #256: Paint House](https://leetcode.com/problems/paint-house):

```python
class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        from functools import cache

        # the number of houses
        n = len(costs)
        if n > 0:
            assert len(costs[0]) == 3  # 3 colors per house, sanity-check the first one

        @cache
        def solve(i, prev_color = -1) -> int:
            assert i < n

            if i < 0:
                return 0

            if i == 0:
                return min(costs[i][j] for j in range(3) if j != prev_color)

            cost = float('inf')
            for j in range(3):
                if j != prev_color:
                    cost = min(cost, costs[i][j] + solve(i - 1, j))

            return cost

        return solve(n - 1)
```
