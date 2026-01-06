---
title: "LeetCode #67: Add Binary"
date: 2026-01-06T14:33:59-03:00
tags:
  - dev
  - leetcode
categories:
  - coding
---

[LeetCode #67: Add Binary](https://leetcode.com/problems/add-binary):

```python
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        n = max(len(a), len(b))

        a = a.rjust(n, '0')
        b = b.rjust(n, '0')

        c = [0] * n

        inc = 0
        for (i, (d1, d2)) in list(enumerate(zip(a, b)))[::-1]:
            c[i] = int(d1) + int(d2) + inc

            if c[i] > 1:
                c[i] %= 2
                inc = 1
            else:
                inc = 0

        if inc == 1:
            c = [1] + c

        return ''.join([str(q) for q in c])


```

Native base 2 conversion:

```python
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return bin(int(a, 2) + int(b, 2))[2:]
```
