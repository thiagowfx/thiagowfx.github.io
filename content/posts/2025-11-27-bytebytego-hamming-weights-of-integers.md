---
title: "ByteByteGo: Hamming Weights of Integers"
date: 2025-11-27T03:09:16-03:00
tags:
  - coding
rss: false
---

[ByteByteGo: Hamming Weights of Integers](https://bytebytego.com/exercises/coding-patterns/bytebytego:-hamming-weights-of-integers):

Did someone say something about variable scoping? Poor `n` is overworked.

```python
from typing import List

def hamming_weights_of_integers(n: int) -> List[int]:
    def hammer(n):
        ans = 0
        while n > 0:
            ans += n & 1
            n >>= 1
        return ans

    return [hammer(n) for n in range(n + 1)]
```

With top-down dynamic programming, linear:

```python
from typing import List

def hamming_weights_of_integers(n: int) -> List[int]:
    from functools import lru_cache

    @lru_cache(maxsize=None)
    def hammer(n):
        if n in [0, 1]:
            return n

        return hammer(n >> 1) + (n & 1)

    return [hammer(n) for n in range(n + 1)]
```

With bottom-up dynamic programming, linear:

```python
from typing import List

def hamming_weights_of_integers(n: int) -> List[int]:
    from functools import lru_cache

    if n == 0:
        return [0]

    hammer = [0] * (n + 1)
    hammer[0] = 0
    hammer[1] = 1

    for x in range(2, n + 1):
        hammer[x] = hammer[x >> 1] + (x & 1)

    return hammer
```
