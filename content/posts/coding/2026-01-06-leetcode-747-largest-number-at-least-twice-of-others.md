---
title: "LeetCode #747: Largest Number At Least Twice of Others"
date: 2026-01-06T04:24:42-03:00
tags:
  - dev
  - leetcode
categories:
  - coding
---

[LeetCode #747: Largest Number At Least Twice of Others](https://leetcode.com/problems/largest-number-at-least-twice-of-others):

```python
class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        g = max(nums)

        for num in nums:
            if num != g and g < 2 * num:
                return -1

        return nums.index(g)
```

One fewer loop:

```python
class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        ig = None
        g = float('-inf')

        for i, num in enumerate(nums):
            if num > g:
                g = num
                ig = i

        for num in nums:
            if num != g and g < 2 * num:
                return -1

        return ig
```
