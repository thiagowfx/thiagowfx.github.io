---
title: "ByteByteGo: Matrix Pathways"
date: 2025-11-26T21:01:40-03:00
tags:
  - coding
rss: false
---

[ByteByteGo: Matrix Pathways](https://bytebytego.com/exercises/coding-patterns/dynamic-programming/matrix-pathways):

```python
def matrix_pathways(m: int, n: int) -> int:
    from functools import lru_cache

    @lru_cache(maxsize=None)
    def solve(m, n):
        # from 1 to m, from 1 to n
        assert (m, n) >= (0, 0)

        if m == 0 or n == 0:
            return 0

        if m == 1 and n == 1:
            return 1

        return solve(m - 1, n) + solve(m, n - 1)

    return solve(m, n)
```
