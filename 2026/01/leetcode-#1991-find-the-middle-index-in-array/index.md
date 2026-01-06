
[LeetCode #1991: Find the Middle Index in Array](https://leetcode.com/problems/find-the-middle-index-in-array):

```python
from itertools import accumulate

class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        acc = list(accumulate(nums))

        for i, num in enumerate(nums):
            if (acc[i - 1] if i > 0 else 0) == (acc[-1] - acc[i]):
                return i

        return -1
```

