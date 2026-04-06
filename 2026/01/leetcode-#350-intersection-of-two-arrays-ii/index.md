---
title: "LeetCode #350: Intersection of Two Arrays II"
url: https://perrotta.dev/2026/01/leetcode-%23350-intersection-of-two-arrays-ii/
last_updated: 2026-01-06
---


[LeetCode #350: Intersection of Two Arrays II](https://leetcode.com/problems/intersection-of-two-arrays-ii):

```python
from collections import Counter

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        c1 = Counter(nums1)
        c2 = Counter(nums2)

        common = set(c1.keys()) & set(c2.keys())

        ans = []

        for n in common:
            ans.extend([n] * min(c1[n], c2[n]))

        return ans
```

