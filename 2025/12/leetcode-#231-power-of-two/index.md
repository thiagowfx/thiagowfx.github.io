
[LeetCode #231: Power of Two](https://leetcode.com/problems/power-of-two):

```python
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False

        while n & 1 == 0:
            n >>= 1  # n //= 2

        return n == 1
```

