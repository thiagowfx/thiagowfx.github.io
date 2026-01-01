
[LeetCode #718: Maximum Length of Repeated Subarray](https://leetcode.com/problems/maximum-length-of-repeated-subarray):

Top-down DP, Memory Limit Exceeded:

```python
class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        from functools import cache

        @cache
        def solve(p1, p2, taken = False):
            if p1 < 0 or p2 < 0:
                return 0

            # if p1 == 0 and p2 == 0:
            #     return int(nums1[p1] == nums2[p2])

            if taken:
                return 1 + solve(p1 - 1, p2 - 1, True) if nums1[p1] == nums2[p2] else 0

            return max(
                solve(p1 - 1, p2),
                solve(p1, p2 - 1),
                1 + solve(p1 - 1, p2 - 1, True) if nums1[p1] == nums2[p2] else 0
            )

        return solve(len(nums1) - 1, len(nums2) - 1)
```

Bottom-up DP, originally wrong:

```python
class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        dp = [[[0] * 2 for _ in range(len(nums2))]  for _ in range(len(nums1))]
        assert len(dp) == len(nums1)
        assert len(dp[0]) == len(nums2)
        assert len(dp[0][0]) == 2

        # Base case
        # No-op: everything is zero
        #   dp[0][*][*] = 0
        #   dp[*][0][*] = 0

        for p1 in range(len(nums1)):
            for p2 in range(len(nums2)):
                # take
                dp[p1][p2][True] = max(
                    1 + dp[p1 - 1][p2 - 1][True] if nums1[p1] == nums2[p2] else 0,
                    1 + dp[p1 - 1][p2 - 1][False] if nums1[p1] == nums2[p2] else 0,
                )

                # do not take
                dp[p1][p2][False] = max(
                    dp[p1 - 1][p2][False],
                    dp[p1][p2 - 1][False],
                )

        # def solve(p1, p2, taken = False):
        #     if taken:
        #         return 1 + solve(p1 - 1, p2 - 1, True) if nums1[p1] == nums2[p2] else 0

        #     return max(
        #         solve(p1 - 1, p2),
        #         solve(p1, p2 - 1),
        #         1 + solve(p1 - 1, p2 - 1, True) if nums1[p1] == nums2[p2] else 0
        #     )

        # return max(
        #     dp[len(nums1) - 1][len(nums2) - 1][True],
        #     dp[len(nums1) - 1][len(nums2) - 1][False],
        # )

        return max(dp[len(nums1) - 1][len(nums2) - 1])
```

Bottom-up DP, fixed:

```python
class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        dp = [[[0] * 2 for _ in range(len(nums2))] for _ in range(len(nums1))]

        for p1 in range(len(nums1)):
            for p2 in range(len(nums2)):
                # take
                if nums1[p1] != nums2[p2]:
                    dp[p1][p2][True] = 0
                else:
                    dp[p1][p2][True] = max(
                        1 + dp[p1 - 1][p2 - 1][True] if (p1 > 0 and p2 > 0) else 0,
                        1,
                    )

                # do not take
                dp[p1][p2][False] = max(
                    dp[p1 - 1][p2][False] if p1 > 0 else 0,
                    dp[p1][p2 - 1][False] if p2 > 0 else 0,
                    dp[p1][p2][True],
                )

        return max(dp[len(nums1) - 1][len(nums2) - 1])
```

Simpler, without `taken`:

```python
class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        m, n = len(nums1), len(nums2)
        # dp[i][j] = length of longest common subarray ending at nums1[i-1] and nums2[j-1]
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        max_length = 0

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if nums1[i - 1] == nums2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                    max_length = max(max_length, dp[i][j])
                # else: dp[i][j] = 0 (already initialized)

        return max_length
```

