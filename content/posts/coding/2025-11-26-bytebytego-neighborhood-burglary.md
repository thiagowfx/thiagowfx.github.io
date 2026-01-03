---
title: "ByteByteGo: Neighborhood Burglary"
date: 2025-11-26T21:17:39-03:00
tags:
  - dev

categories:
  - coding
---

[ByteByteGo: Neighborhood Burglary](https://bytebytego.com/exercises/coding-patterns/dynamic-programming/neighborhood-burglary):

```python
from typing import List

def neighborhood_burglary(houses: List[int]) -> int:
    from functools import lru_cache

    @lru_cache(maxsize=None)
    def solve(i):
        # 0 to n - 1
        assert i >= 0

        if i == 0:
            return houses[0]

        if i == 1:
            return max(houses[0], houses[1])

        return max(
            houses[i] + solve(i - 2),
            solve(i - 1),
        )

    return solve(len(houses) - 1)
```
