---
title: "LeetCode #326: Power of Three"
url: https://perrotta.dev/2025/12/leetcode-%23326-power-of-three/
last_updated: 2026-01-03
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

