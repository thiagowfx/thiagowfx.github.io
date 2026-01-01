---
title: "ByteByteGo: Pair Sum - Sorted"
date: 2025-11-22T15:08:14-03:00
rss: false
categories:
  - coding
---

[ByteByteGo: Pair Sum - Sorted](https://bytebytego.com/exercises/coding-patterns/two-pointers/pair-sum-sorted):

```python
from typing import List

def pair_sum_sorted(nums: List[int], target: int) -> List[int]:
    left = 0
    right = len(nums) - 1

    while left < right:
        if nums[left] + nums[right] == target:
            return [left, right]
        elif nums[left] + nums[right] < target:
            left += 1
        else:
            right -= 1

    return []
```

Classic Two Pointer problem, inward traversal.

In a single pass:

```python
from typing import List

def pair_sum_unsorted(nums: List[int], target: int) -> List[int]:
    d = {}
    for i, num in enumerate(nums):
        if (target - num) in d.keys():
            return [d[target-num], i]
        d[num] = i

    return []
```
