
[LeetCode #983: Minimum Cost For Tickets](https://leetcode.com/problems/minimum-cost-for-tickets):

```python
class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        pass1 = costs[0]
        pass7 = costs[1]
        pass30 = costs[2]

        # This is already the case
        # days.sort()

        n = len(days)
        assert len(costs) == 3

        from functools import cache

        @cache
        def solve(i):
            ## 0..n-1

            ## [1,4,6,7,8,20]

            if i >= n:
                return 0

            ans = float('inf')

            # 1-day
            ans = min(ans, pass1 + solve(i + 1))

            # 7-day
            next_i = i + 1
            while next_i < n and days[i] <= days[next_i] <= (days[i] + 6):
                next_i += 1
            ans = min(ans, pass7 + solve(next_i))

            # 30-day
            next_i = i + 1
            while next_i < n and days[i] <= days[next_i] <= (days[i] + 29):
                next_i += 1
            ans = min(ans, pass30 + solve(next_i))

            return ans


        return solve(0)
```

With binary search:

```python
import bisect

class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        pass1 = costs[0]
        pass7 = costs[1]
        pass30 = costs[2]

        # This is already the case
        # days.sort()

        n = len(days)
        assert len(costs) == 3

        from functools import cache

        @cache
        def solve(i):
            ## 0..n-1

            ## [1,4,6,7,8,20]

            if i >= n:
                return 0

            ans = float('inf')

            # 1-day
            ans = min(ans, pass1 + solve(i + 1))

            # 7-day
            ans = min(ans, pass7 + solve(bisect.bisect_right(days, days[i] + 6, i)))

            # 30-day
            ans = min(ans, pass30 + solve(bisect.bisect_right(days, days[i] + 29, i)))

            return ans

        return solve(0)
```

