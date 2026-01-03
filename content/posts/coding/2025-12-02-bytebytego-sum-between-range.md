---
title: "ByteByteGo: Sum Between Range"
date: 2025-12-02T22:50:57-03:00
tags:
  - dev

categories:
  - coding
---

[ByteByteGo: Sum Between Range](https://bytebytego.com/exercises/coding-patterns/prefix-sums/sum-between-range):

```python
from typing import List

import itertools

class SumBetweenRange:
    def __init__(self, nums: List[int]):
        self.acc = list(itertools.accumulate(nums))

    def sum_range(self, i: int, j: int):
        return self.acc[j] - (self.acc[i - 1] if i != 0 else 0)
```
