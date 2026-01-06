
[LeetCode #2154: Keep Multiplying Found Values by Two](https://leetcode.com/problems/keep-multiplying-found-values-by-two):

```python
class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        s = set(nums)

        while True:
            if original in s:
                original <<= 1
            else:
                break

        return original
```

