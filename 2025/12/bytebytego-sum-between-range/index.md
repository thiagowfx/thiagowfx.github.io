---
title: "ByteByteGo: Sum Between Range"
url: https://perrotta.dev/2025/12/bytebytego-sum-between-range/
last_updated: 2026-01-03
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

