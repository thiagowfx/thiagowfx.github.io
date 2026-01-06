
[LeetCode #3667: Sort Array By Absolute Value](https://leetcode.com/problems/sort-array-by-absolute-value):

```python
class Solution:
    def sortByAbsoluteValue(self, nums: List[int]) -> List[int]:
        return list(sorted(nums, key=lambda x: abs(x)))
```

