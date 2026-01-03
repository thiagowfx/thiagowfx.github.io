---
title: "ByteByteGo: First and Last Occurrences of a Number"
date: 2025-12-02T16:37:49-03:00
tags:
  - bytebytego
  - dev

categories:
  - coding
---

[ByteByteGo: First and Last Occurrences of a Number](https://bytebytego.com/exercises/coding-patterns/binary-search/first-and-last-occurrences-of-a-number):

```python
import bisect
from typing import List

def first_and_last_occurrences_of_a_number(nums: List[int], target: int) -> int:
    if not nums:
        return [-1, -1]

    left = bisect.bisect_left(nums, target)
    right = bisect.bisect_right(nums, target)

    if (left < len(nums) and nums[left] == target) and (right > 0 and nums[right - 1] == target):
        return [left, right - 1]

    return [-1, -1]
```
