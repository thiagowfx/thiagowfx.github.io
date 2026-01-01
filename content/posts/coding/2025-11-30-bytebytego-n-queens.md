---
title: "ByteByteGo: N Queens"
date: 2025-11-30T21:14:24-03:00
categories:
  - coding
---

[ByteByteGo: N Queens](https://bytebytego.com/exercises/coding-patterns/backtracking/n-queens):

```python
def n_queens(n: int) -> int:
    ans = 0

    def backtrack(r, vset: set, d1set: set, d2set: set):
        nonlocal ans

        # r, c: row, col

        # d1 set: r + c
        # d2 set: r - c (or c - r, just be consistent)

        if r == n:
            ans += 1
            return

        for c in range(n):
            # place a queen in (r, c) position if possible
            if c not in vset and c + r not in d1set and c - r not in d2set:
                vset.add(c)
                d1set.add(c + r)
                d2set.add(c - r)

                backtrack(r + 1, vset, d1set, d2set)

                vset.remove(c)
                d1set.remove(c + r)
                d2set.remove(c - r)


    backtrack(0, set(), set(), set())

    return ans
```
