
[LeetCode #198: House Robber](https://leetcode.com/problems/house-robber/):

```python
from functools import cache

class Solution:
    def rob(self, nums: List[int]) -> int:

        n = len(nums)

        @cache
        def profit(i):
            """
            Max profit accounting for nums[0]..nums[i-1]
            """
            assert i < n

            if i < 0:
                return 0

            if i == 0:
                return nums[0]

            if i == 1:
                return max(nums[0], nums[1])

            return max(
                nums[i] + profit(i - 2),
                nums[i - 1] + profit(i - 1 - 2),
            )

        return profit(n - 1)
```

In this memoization one index is enough to express a list interval.

One of the interval ends is fixed: either the beginning or the end.
In this solution I chose to fix the beginning, so that the base case is `profit(0)`.

Previously I did it the other way around:

```python
from functools import cache

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        @cache
        def solve(i):
            """
            Max profit accounting for nums[i]..nums[n - 1]
            """
            if i >= n:
                return 0

            return max(
                nums[i] + solve(i + 2),
                solve(i + 1),  # 0 +
            )

        return solve(0)
```

Which made me realize we can improve the first solution slightly:

```python
from functools import cache

class Solution:
    def rob(self, nums: List[int]) -> int:

        n = len(nums)

        @cache
        def profit(i):
            assert i < n

            if i < 0:
                return 0

            if i == 0:
                return nums[0]

            return max(
                nums[i] + profit(i - 2),
                profit(i - 1), # + 0
            )

        return profit(n - 1)
```

