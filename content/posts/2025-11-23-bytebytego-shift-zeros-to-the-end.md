---
title: "ByteByteGo: Shift Zeros to the End"
date: 2025-11-23T18:16:40-03:00
tags:
  - coding
rss: false
---

[Same as LeetCode #283]({{< ref "2025-09-12-leetcode-283-move-zeroes" >}}).

[ByteByteGo: Shift Zeros to the End](https://bytebytego.com/exercises/coding-patterns/two-pointers/shift-zeros-to-the-end):

```python
from typing import List

def shift_zeros_to_the_end(nums: List[int]) -> None:
    j = None

    for i, num in enumerate(nums):
        if num != 0:
            if j is not None:
                assert j < i
                nums[i], nums[j] = nums[j], nums[i]
                j += 1
        else:
            if j is None:
                j = i

```

Simplified version:

```python
from typing import List

def shift_zeros_to_the_end(nums: List[int]) -> None:
    j = 0

    for i, num in enumerate(nums):
        if num != 0:
            nums[i], nums[j] = nums[j], nums[i]
            j += 1
```
