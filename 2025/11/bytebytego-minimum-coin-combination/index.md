
[ByteByteGo: Minimum Coin Combination](https://bytebytego.com/exercises/coding-patterns/dynamic-programming/minimum-coin-combination):

The `-1` return requirement makes it a bit ugly.

```python
from typing import List
from functools import lru_cache

def min_coin_combination(coins: List[int], target: int) -> int:
    @lru_cache(maxsize=None)
    def solve(i, target):
        if i < 0 or target < 0:
            if target == 0:
                return 0
            else:
                return -1

        q1 = solve(i, target - coins[i])
        q2 = solve(i - 1, target)

        if q1 != -1 and q2 != -1:
            return min(
                q1 + 1,
                q2,
            )
        if q1 != -1:
            return q1 + 1
        if q2 != -1:
            return q2

        return -1

    return solve(len(coins) - 1, target)
```

