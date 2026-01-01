
[LeetCode #922: Sort Array By Parity II](https://leetcode.com/problems/leetcode-#922:-sort-array-by-parity-ii):

New list:

```python
class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        def interleave(a, b):
            assert len(a) == len(b)
            ans = []
            for (x, y) in zip(a, b):
                ans += [x, y]
            return ans

        return interleave(
            [num for num in nums if num % 2 == 0],
            [num for num in nums if num % 2 == 1],
        )
```

In-place:

```python
class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        j = 1
        for i in range(0, len(nums), 2):
            if nums[i] % 2 == 1:
                while nums[j] % 2 == 1:
                    j += 2
                nums[i], nums[j] = nums[j], nums[i]
        return nums
```

