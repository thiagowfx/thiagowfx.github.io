---
title: "ByteByteGo: Find the Insertion Index"
date: 2025-11-26T13:48:52-03:00
tags:
  - bytebytego
  - dev

categories:
  - coding
---

[ByteByteGo: Find the Insertion Index](https://bytebytego.com/exercises/coding-patterns/binary-search/find-the-insertion-index):

```python
from typing import List

def find_the_insertion_index(nums: List[int], target: int) -> int:
    if len(nums) == 0:
        return 0

    left = 0
    right = len(nums) - 1
    assert right >= left

    while left < right:
        mid = left + ((right - left) // 2)

        if nums[mid] == target:
            return mid

        elif nums[mid] < target:
            left = mid + 1

        else:
            right = mid - 1

    if nums[left] < target:
        return left + 1
    else:
        return left

```

Elegant:

```python
import bisect
from typing import List

def find_the_insertion_index(nums: List[int], target: int) -> int:
    return bisect.bisect_left(nums, target)
```
