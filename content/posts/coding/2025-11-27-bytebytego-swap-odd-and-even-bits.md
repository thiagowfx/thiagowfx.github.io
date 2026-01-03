---
title: "ByteByteGo: Swap Odd and Even Bits"
date: 2025-11-27T03:06:15-03:00
tags:
  - bytebytego
  - dev

categories:
  - coding
---

[ByteByteGo: Swap Odd and Even Bits](https://bytebytego.com/exercises/coding-patterns/bit-manipulation/swap-odd-and-even-bits):

```python
def swap_odd_and_even_bits(n: int) -> int:
    ans = 0
    shift = 0

    while n > 0:
        ans += ((n & 0b01) << 1) + ((n & 0b10) >> 1) << shift
        n >>= 2
        shift += 2

    return ans
```
