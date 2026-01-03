---
title: "LeetCode #190: Reverse Bits"
date: 2025-12-24T04:47:07-03:00
tags:
  - dev

categories:
  - coding
---

[LeetCode #190: Reverse Bits](https://leetcode.com/problems/reverse-bits):

```python
class Solution:
    def reverseBits(self, n: int) -> int:
        ans = 0

        for i in range(32):
            b = n & 1
            n >>= 1

            ans = (ans << 1) + b

        return ans
```

Note:

```python
for i in range(32):
```

...is needed to process all 32 bits of `n`.

Initially I tried it like this:

```python
class Solution:
    def reverseBits(self, n: int) -> int:
        ans = 0

        while n:
            b = n & 1
            n >>= 1

            ans = (ans << 1) + b

        return ans
```

...but it stops at the most significant bit of `n`.
