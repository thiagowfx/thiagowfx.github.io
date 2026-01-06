---
title: "LeetCode #209: Minimum Size Subarray Sum"
date: 2026-01-06T16:00:13-03:00
tags:
  - dev
  - leetcode
categories:
  - coding
---

[LeetCode #209: Minimum Size Subarray Sum](https://leetcode.com/problems/minimum-size-subarray-sum):

Sliding window:

```python
from itertools import accumulate

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        right = 0
        n = len(nums)

        ans = float('inf')

        acc = list(accumulate(nums))
        def mysum(a, b, nums):
            return acc[b] - (acc[a - 1] if a > 0 else 0)

        # 2 3 1 2 4 3

        while right < n:
            assert left <= right
            s = mysum(left, right, nums)

            if s > target:
                ans = min(ans, right - left + 1)
                left += 1
                if left > right:
                    right = left
            elif s < target:
                right += 1
            else: ## s == target:
                ans = min(ans, right - left + 1)
                right += 1

        return ans if ans != float('inf') else 0
```
