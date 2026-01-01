---
title: "LeetCode #265: Paint House II"
date: 2025-12-29T13:51:31-03:00
rss: false
categories:
  - coding
---

[Previously]({{< ref "2025-12-29-leetcode-256-paint-house" >}}). Just replace
`3` with `k`.

[LeetCode #265: Paint House II](https://leetcode.com/problems/paint-house-ii):

```python
class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        from functools import cache

        # the number of houses
        n = len(costs)
        k = len(costs[0])

        @cache
        def solve(i, prev_color = -1) -> int:
            assert i < n

            if i < 0:
                return 0

            if i == 0:
                return min(costs[i][j] for j in range(k) if j != prev_color)

            return min(costs[i][j] + solve(i - 1, j) for j in range(k) if j != prev_color)

        return solve(n - 1)
```
