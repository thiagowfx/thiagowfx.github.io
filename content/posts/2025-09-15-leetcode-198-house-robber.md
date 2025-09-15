---
title: "LeetCode #198: House Robber"
date: 2025-09-15T22:47:23+02:00
tags:
  - coding
---

[LeetCode #198: House Robber](https://leetcode.com/problems/house-robber/):

```python
from functools import cache

class Solution:
    def rob(self, nums: List[int]) -> int:

        n = len(nums)

        @cache
        def profit(i):
            """
            Max profit accounting for nums[0]..nums[i-1]
            """
            assert i < n

            if i < 0:
                return 0

            if i == 0:
                return nums[0]

            if i == 1:
                return max(nums[0], nums[1])

            return max(
                nums[i] + profit(i - 2),
                nums[i - 1] + profit(i - 1 - 2),
            )

        return profit(n - 1)
```

In this memoization one index is enough to express a list interval.

One of the interval ends is fixed: either the beginning or the end.
In this solution I chose to fix the beginning, so that the base case is `profit(0)`.
