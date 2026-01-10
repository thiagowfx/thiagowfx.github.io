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

With `Counter`:

```python
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return [k for (k, v) in Counter(nums).most_common()[:k]]
```

With `defaultdict(int)`:

```python
from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = defaultdict(int)
        for num in nums:
            c[num] += 1

        return [k for (k, v) in (sorted(c.items(), key=lambda item: item[1], reverse=True))[:k]]
```
