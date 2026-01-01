
[LeetCode #977: Squares of a Sorted Array](https://leetcode.com/problems/leetcode-#977:-squares-of-a-sorted-array):

```python
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        return list(sorted(num ** 2 for num in nums))
```

