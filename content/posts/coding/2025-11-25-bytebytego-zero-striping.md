---
title: "ByteByteGo: Zero Striping"
date: 2025-11-25T00:13:43-03:00
categories:
  - coding
---

[ByteByteGo: Zero Striping](https://bytebytego.com/exercises/coding-patterns/hash-maps-and-sets/zero-striping):

```python
from typing import List

def zero_striping(matrix: List[List[int]]) -> None:
    row_set = set()
    col_set = set()

    for x in range(len(matrix)):
        for y in range(len(matrix[0])):
            c = matrix[x][y]

            if c == 0:
                row_set.add(x)
                col_set.add(y)

    for x in range(len(matrix)):
        for y in range(len(matrix[0])):
            if x in row_set or y in col_set:
                matrix[x][y] = 0
```
