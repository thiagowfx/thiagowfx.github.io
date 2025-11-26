---
title: "ByteByteGo: Reverse 32-Bit Integer"
date: 2025-11-26T15:06:17-03:00
tags:
  - coding
rss: false
---

[ByteByteGo: Reverse 32-Bit Integer](https://bytebytego.com/exercises/coding-patterns/bytebytego:-reverse-32-bit-integer):

With strings:

```python
def reverse_32_bit_integer(n: int) -> int:
    ans = ""

    s = str(n)[::-1]

    # 420
    # 024

    # -15
    # 51-

    is_negative = n < 0
    is_beginning = True

    for i, c in enumerate(s):
        if i == (len(s) - 1) and is_negative:
            continue

        if c == '0' and is_beginning:
            continue

        ans += c

        is_beginning = False

    ans = int(ans) * (-1 if is_negative else 1)

    return ans if (-1 * 2**31 <= ans <= 2**31 - 1) else 0
```
