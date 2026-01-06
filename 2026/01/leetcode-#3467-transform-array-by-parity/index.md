
[LeetCode #3467: Transform Array by Parity](https://leetcode.com/problems/transform-array-by-parity):

Manual:

```python
class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:
        for i, num in enumerate(nums):
            if num % 2 == 0:
                nums[i] = 0
            if num % 2 == 1:
                nums[i] = 1
        return list(sorted(nums))
```

List comprehension, less readable:

```python
class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:
        return list(sorted([(1 if num % 2 == 1 else num) for num in [(0 if num % 2 == 0 else num) for num in nums]]))
```

