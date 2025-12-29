---
title: "LeetCode #718: Maximum Length of Repeated Subarray"
date: 2025-12-29T15:38:48-03:00
tags:
  - coding
rss: false
---

[LeetCode #718: Maximum Length of Repeated Subarray](https://leetcode.com/problems/maximum-length-of-repeated-subarray):

Top-down DP, Memory Limit Exceeded:

```python
class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        from functools import cache

        @cache
        def solve(p1, p2, taken = False):
            if p1 < 0 or p2 < 0:
                return 0

            # if p1 == 0 and p2 == 0:
            #     return int(nums1[p1] == nums2[p2])

            if taken:
                return 1 + solve(p1 - 1, p2 - 1, True) if nums1[p1] == nums2[p2] else 0

            return max(
                solve(p1 - 1, p2),
                solve(p1, p2 - 1),
                1 + solve(p1 - 1, p2 - 1, True) if nums1[p1] == nums2[p2] else 0
            )

        return solve(len(nums1) - 1, len(nums2) - 1)
```
