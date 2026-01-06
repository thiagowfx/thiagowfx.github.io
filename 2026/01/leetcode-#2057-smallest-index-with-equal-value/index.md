
[LeetCode #2057: Smallest Index With Equal Value](https://leetcode.com/problems/smallest-index-with-equal-value):

```python
class Solution:
    def smallestEqual(self, nums: List[int]) -> int:
        for i, num in enumerate(nums):
            if i % 10 == num:
                return i

        return -1
```

