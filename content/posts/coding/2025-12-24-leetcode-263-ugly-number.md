---
title: "LeetCode #263: Ugly Number"
date: 2025-12-24T17:19:27-03:00
rss: false
categories:
  - coding
---

[LeetCode #263: Ugly Number](https://leetcode.com/problems/ugly-number):

```python
class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False

        for factor in [2, 3, 5]:
            while n % factor == 0:
                n //= factor

        return n == 1
```
