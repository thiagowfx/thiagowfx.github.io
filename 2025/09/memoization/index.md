
How to bootstrap a **top-down** dynamic programming (DP) problem in Python:

```python
from functools import cache

class Solution:
    def doProblem(self, input: List[int]) -> int:
        @cache
        def solve():
            pass

        return solve(0)
```

[Previously]({{< ref "2024-01-12-python-all-hail-to-cache-memoization" >}}).

