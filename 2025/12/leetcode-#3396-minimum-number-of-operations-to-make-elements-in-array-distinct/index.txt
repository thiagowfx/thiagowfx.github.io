
[LeetCode 3396. Minimum Number of Operations to Make Elements in Array Distinct](https://leetcode.com/problems/minimum-number-of-operations-to-make-elements-in-array-distinct):

```python
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        c = Counter(nums)
        ans = 0
        i = 0

        while c.most_common()[0][1] > 1:
            ans += 1

            for _ in range(3):
                if i < len(nums):
                    c[nums[i]] -= 1
                    i += 1
                else:
                    break

        return ans
```

