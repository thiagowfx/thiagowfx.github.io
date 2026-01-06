
[LeetCode #724: Find Pivot Index](https://leetcode.com/problems/find-pivot-index):

Slow:

```python
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        for i, num in enumerate(nums):
            if sum(nums[:i]) == sum(nums[i + 1:]):
                return i

        return -1
```

Prefix sum:

```python
from itertools import accumulate

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        acc = list(accumulate(nums))

        for i, num in enumerate(nums):
            if (acc[i - 1] if i > 0 else 0) == (acc[-1] - acc[i]):
                return i

        return -1
```

