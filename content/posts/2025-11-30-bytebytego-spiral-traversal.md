---
title: "ByteByteGo: Spiral Traversal"
date: 2025-11-30T16:49:27-03:00
tags:
  - coding
rss: false
---

[ByteByteGo: Spiral Traversal](https://bytebytego.com/exercises/coding-patterns/math-and-geometry/spiral-traversal):

```python
from typing import List

def spiral_matrix(matrix: List[List[int]]) -> List[int]:
    ans = []

    start = (0, 0)
    end = (len(matrix), len(matrix[0]))

    def debian_once(matrix, start, end):
        # if (start[0], start[1]) == (end[0] - 1, end[1] - 1):
        #     ans.append(matrix[start[0]][start[1]])
        #     return

        for j in range(start[1], end[1]):
            ans.append(matrix[start[0]][j])

        for i in range(start[0] + 1, end[0] - 1):
            ans.append(matrix[i][end[1] - 1])

        if end[0] - 1 > start[0]:
            for j in range(end[1] - 1, start[1] - 1, -1):
                ans.append(matrix[end[0] - 1][j])

        if start[1] < end[1] - 1:
            for i in range(end[0] - 1 - 1, start[1], -1):
                ans.append(matrix[i][start[1]])

    #  while start[0] < end[0] and start[1] < end[1]:
    # while all(start[i] < end[i] for i in range(len(start))):
    while all(x < y for (x, y) in zip(start, end)):
        debian_once(matrix, start, end)
        start = tuple(el + 1 for el in start)
        end = tuple(el - 1 for el in end)

    return ans
```

Beware of not doing `<-` (leftwards) and `^` (upwards) whenever there's a single
column or a single row!
