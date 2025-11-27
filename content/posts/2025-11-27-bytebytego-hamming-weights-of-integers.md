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
