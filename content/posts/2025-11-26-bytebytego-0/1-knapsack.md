---
title: "ByteByteGo: 0/1 Knapsack"
date: 2025-11-26T22:06:31-03:00
tags:
  - coding
rss: false
---

[ByteByteGo: 0/1 Knapsack](https://bytebytego.com/exercises/coding-patterns/bytebytego:-0/1-knapsack):

```python
from typing import List

def knapsack(k: int, weights: List[int], values: List[int]) -> int:
    from functools import lru_cache

    assert len(weights) == len(values)

    @lru_cache(maxsize=None)
    def solve(i, k):
        assert i >= 0

        if i == 0:
            if weights[i] <= k:
                return values[i]
            else:
                return 0

        if k <= 0:
            return 0

        skip = solve(i - 1, k)

        take = 0
        if weights[i] <= k:
            take = values[i] + solve(i - 1, k - weights[i])

        return max(skip, take)

    return solve(len(weights) - 1, k)
```
