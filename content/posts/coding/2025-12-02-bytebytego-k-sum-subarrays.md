---
title: "ByteByteGo: K-Sum Subarrays"
date: 2025-12-02T22:56:27-03:00
rss: false
categories:
  - coding
---

[ByteByteGo: K-Sum Subarrays](https://bytebytego.com/exercises/coding-patterns/prefix-sums/k-sum-subarrays):

```python
from typing import List
import itertools

def k_sum_subarrays(nums: List[int], k: int) -> int:
    acc = list(itertools.accumulate(nums))

    ans = 0

    for i in range(len(nums)):
        for j in range(i, len(nums)):
            mysum = acc[j] - (acc[i - 1] if i != 0 else 0)
            if mysum == k:
                ans += 1

    return ans
```
