---
title: "LeetCode #263: Ugly Number"
url: https://perrotta.dev/2025/12/leetcode-%23263-ugly-number/
last_updated: 2026-01-03
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

