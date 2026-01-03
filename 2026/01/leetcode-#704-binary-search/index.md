
[LeetCode #704: Binary Search](https://leetcode.com/problems/binary-search):

From scratch, iteratively:

```python
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            ## mid = (left + right) // 2
            mid = left + (right - left) // 2
            assert 0 <= mid < len(nums)

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else: ## nums[mid] > target:
                right = mid - 1

        return left if (0 <= left < len(nums)) and nums[left] == target else -1
```

With `bisect`:

```shell
import bisect

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        index = bisect.bisect_left(nums, target)
        if index >= len(nums):
            return -1
        return index if nums[index] == target else -1
```

