---
title: "LeetCode #229: Majority Element II"
date: 2025-12-31T01:51:18-03:00
tags:
  - coding
rss: false
---

[LeetCode #229: Majority Element II](https://leetcode.com/problems/majority-element-ii):

```python
from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        return [el for (el, count) in Counter(nums).most_common() if count > (len(nums) // 3)]
```
