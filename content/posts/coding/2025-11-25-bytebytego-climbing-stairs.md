---
title: "ByteByteGo: Climbing Stairs"
date: 2025-11-25T00:27:38-03:00
rss: false
categories:
  - coding
---

[ByteByteGo: Climbing Stairs](https://bytebytego.com/exercises/coding-patterns/dynamic-programming/climbing-stairs):

Top-down DP:

```python
def climbing_stairs(n: int) -> int:
    from functools import lru_cache

    @lru_cache(maxsize=None)
    def cs(n):
        """How many possibilities for n steps?"""
        assert n >= 0

        if n in [0, 1, 2]:
            return n

        return cs(n-1) + cs(n-2)

    return cs(n)
```

Their Python environment is quite old (3.8). Goodness.

We can only do `from functools import cache` [from Python
3.9+](https://stackoverflow.com/questions/66846743/importerror-cannot-import-name-cache-from-functools).

Bottom-up DP:

```python
def climbing_stairs(n: int) -> int:
    dp = [None] * n

    dp[0] = 1
    dp[1] = 2

    for i in range(2, n):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n - 1]
```
