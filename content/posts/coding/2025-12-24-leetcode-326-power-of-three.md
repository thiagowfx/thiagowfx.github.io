---
title: "LeetCode #326: Power of Three"
date: 2025-12-24T17:16:14-03:00
categories:
  - coding
---

[LeetCode #326: Power of Three](https://leetcode.com/problems/power-of-three):

```python
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False

        while n != 1:
            if n % 3 != 0:
                return False

            n //= 3

        return True
```
