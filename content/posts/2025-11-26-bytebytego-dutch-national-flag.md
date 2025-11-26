---
title: "ByteByteGo: Dutch National Flag"
date: 2025-11-26T14:03:26-03:00
tags:
  - coding
rss: false
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
