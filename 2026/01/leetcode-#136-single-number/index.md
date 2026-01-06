
[LeetCode #136: Single Number](https://leetcode.com/problems/single-number):

XOR everything:

```python
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0
        for num in nums:
            ans ^= num
        return ans
```

Or with `reduce`:

```python
from functools import reduce

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return reduce(lambda a, b: a ^ b, nums)
```

