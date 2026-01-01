
[LeetCode #300: Longest Increasing Subsequence](https://leetcode.com/problems/longest-increasing-subsequence/):

```python
from functools import cache
from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        @cache
        def solve(n: int, last: float) -> int:
            """
            Length of LIS for 0..n-1, with elements < last allowed.
            """
            assert n < len(nums)

            if n < 0:
                return 0

            # do not take current element
            ans1 = solve(n - 1, last)

            # take current element, if valid
            ans2 = 0
            if last is None or nums[n] < nums[last]:
                ans2 = 1 + solve(n - 1, n)

            return max(ans1, ans2)

        return solve(len(nums) - 1, None)
```

Initially I used `last` to represent the highest value, but it's better to
represent the index of the highest value, so to reduce the problem memory space.

The runtime complexity of this solution is O(n^2). The worst case input:
`[-1, -2, ..., -2500]`.

TODO: Iterative DP.

TODO: Patience sorting.

