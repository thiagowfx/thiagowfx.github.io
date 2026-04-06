---
title: "LeetCode #349: Intersection of Two Arrays"
url: https://perrotta.dev/2025/12/leetcode-%23349-intersection-of-two-arrays/
last_updated: 2026-01-03
---


[LeetCode #349: Intersection of Two Arrays](https://leetcode.com/problems/intersection-of-two-arrays):

```python
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1) & set(nums2))
```

