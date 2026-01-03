---
title: "ByteByteGo: Dutch National Flag"
date: 2025-11-26T14:03:26-03:00
tags:
  - bytebytego
  - dev

categories:
  - coding
---

[ByteByteGo: Dutch National Flag](https://bytebytego.com/exercises/coding-patterns/sort-and-search/dutch-national-flag):

Cheat, O(n log n) time:

```python
from typing import List
from collections import defaultdict

def dutch_national_flag(nums: List[int]) -> None:
    nums.sort()
```

O(n) time, O(1) storage:

```python
from typing import List
from collections import defaultdict

def dutch_national_flag(nums: List[int]) -> None:
    c = defaultdict(int)

    for num in nums:
        c[num] += 1

    order = sorted(c.keys())

    for i in range(len(nums)):
        for ins in order:
            if c[ins] > 0:
                nums[i] = ins
                c[ins] -= 1
                break
```

Clean:

```python
from typing import List

def dutch_national_flag(nums: List[int]) -> None:
    """
    In-place sort of array containing only 0,1,2 using the three-pointer method.
    Time: O(n), Space: O(1)
    """
    left = 0
    mid = 0
    right = len(nums) - 1

    while mid <= right:
        if nums[mid] == 0:
            nums[left], nums[mid] = nums[mid], nums[left]
            left += 1
            mid += 1
        elif nums[mid] == 1:
            mid += 1
        else:  # nums[mid] == 2
            nums[mid], nums[right] = nums[right], nums[mid]
            right -= 1
```
