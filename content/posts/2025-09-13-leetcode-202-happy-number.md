---
title: "LeetCode #202: Happy Number"
date: 2025-09-13T00:47:22+02:00
tags:
  - coding
rss: false
---

[LeetCode #202: Happy Number](https://leetcode.com/problems/happy-number/):

```python
class Solution:
    def isHappy(self, n: int) -> bool:
        assert n > 0

        def happyIter(n):
            # 19 -> '19' -> (1^2, 9^2) -> 1^2 + 9^2
            return sum(int(d)**2 for d in str(n))

        seen = {n}
        while n != 1:
            n = happyIter(n)
            if n in seen:
                return False
            seen.add(n)

        return True
```

Previously:

```python
class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        while n != 1 and n not in seen:
            seen.add(n)
            digits = [int(c) for c in str(n)]   # ['1', '9'] -> [1, 9]
            n = sum([digit ** 2 for digit in digits])

        return n == 1
```
