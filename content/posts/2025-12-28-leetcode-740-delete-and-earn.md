---
title: "LeetCode #740: Delete and Earn"
date: 2025-12-28T06:04:14-03:00
tags:
  - coding
rss: false
---

[LeetCode #740: Delete and Earn](https://leetcode.com/problems/delete-and-earn):

```python
from collections import defaultdict

class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        h = defaultdict(int)
        max_number = 0

        for num in nums:
            h[num] += num
            max_number = max(max_number, num)

        from functools import cache

        @cache
        def solve(n):
            if n <= 0:
                return 0

            if n == 1:
                return h[1]

            return max(
                # do not take
                solve(n - 1),

                # take
                solve(n - 2) + h[n],
            )

        return solve(max_number)
```
