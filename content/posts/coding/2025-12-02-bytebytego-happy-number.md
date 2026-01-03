---
title: "ByteByteGo: Happy Number"
date: 2025-12-02T16:32:31-03:00
tags:
  - dev

categories:
  - coding
---

[ByteByteGo: Happy Number](https://bytebytego.com/exercises/coding-patterns/fast-and-slow-pointers/happy-number):

```python
def happy_number(n: int) -> bool:
    seen = (set([n]))

    def apply(n):
        ans = 0

        while n > 0:
            ans += (n % 10) ** 2
            n //= 10

        return ans

    assert apply(23) == 13

    while n != 1:
        n = apply(n)

        if n in seen:
            return False
        else:
            seen.add(n)

    return True
```
