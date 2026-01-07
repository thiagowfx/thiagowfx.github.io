---
title: "LeetCode #219: Contains Duplicate II"
date: 2026-01-06T21:10:50-03:00
tags:
  - dev
  - leetcode
categories:
  - coding
---

[LeetCode #219: Contains Duplicate II](https://leetcode.com/problems/contains-duplicate-ii):

```python
from collections import defaultdict

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        d = defaultdict(list)
        for i, num in enumerate(nums):
            d[num].append(i)

        for values in d.values():
            values.sort()
            # 1 3 4
            for a, b in zip(values[:-1], values[1:]):
                if abs(a - b) <= k:
                    return True

        return False
```
