---
title: "ByteByteGo: Pair Sum - Unsorted"
date: 2025-11-22T19:28:06-03:00
tags:
  - coding
rss: false
---

[ByteByteGo: Pair Sum - Unsorted](https://bytebytego.com/exercises/coding-patterns/hash-maps-and-sets/pair-sum-unsorted):

```python
from typing import List

def pair_sum_unsorted(nums: List[int], target: int) -> List[int]:
    # Option 1: sort it and do two pointers.
    # Option 2: hash map.
    d = {}
    for i, num in enumerate(nums):
        d[num] = i

    for i, num in enumerate(nums):
        if (target - num) in d.keys():
            j = d[target - num]
            if i != j:
                return [i, j]

    return []
```

Be careful not to pick the same index twice.
