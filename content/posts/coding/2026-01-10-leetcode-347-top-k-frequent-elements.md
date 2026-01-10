---
title: "LeetCode #347: Top K Frequent Elements"
date: 2026-01-10T02:09:59-03:00
tags:
  - dev
  - leetcode
categories:
  - coding
---

[LeetCode #347: Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements):

```python
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return [k for (k, v) in Counter(nums).most_common()[:k]]
```
