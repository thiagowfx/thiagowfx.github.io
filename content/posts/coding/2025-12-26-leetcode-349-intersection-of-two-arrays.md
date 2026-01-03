---
title: "LeetCode #349: Intersection of Two Arrays"
date: 2025-12-26T17:04:50-03:00
tags:
  - dev
  - leetcode

categories:
  - coding
---

[LeetCode #349: Intersection of Two Arrays](https://leetcode.com/problems/intersection-of-two-arrays):

```python
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1) & set(nums2))
```
