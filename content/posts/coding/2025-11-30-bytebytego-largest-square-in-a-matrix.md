---
title: "ByteByteGo: Largest Square in a Matrix"
date: 2025-11-30T23:18:37-03:00
tags:
  - bytebytego
  - dev

categories:
  - coding
---

[ByteByteGo: Largest Square in a Matrix](https://bytebytego.com/exercises/coding-patterns/dynamic-programming/largest-square-in-a-matrix):

```python
from typing import List
from functools import lru_cache

def largest_square_in_a_matrix(matrix: List[List[int]]) -> int:
    @lru_cache(maxsize=None)
    def solve(x: int, y: int) -> int:
        if x < 0 or y < 0:
            return 0
        if matrix[x][y] == 0 or x == 0 or y == 0:
            return matrix[x][y]
        return 1 + min(
            solve(x - 1, y),
            solve(x, y - 1),
            solve(x - 1, y - 1),
        )

    # stores the maximum side length
    ans = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            ans = max(ans, solve(i, j))

    # Return the area (side length squared)
    return ans * ans
```
