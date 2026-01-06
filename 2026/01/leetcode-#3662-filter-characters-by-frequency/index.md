
[LeetCode #3662: Filter Characters by Frequency](https://leetcode.com/problems/filter-characters-by-frequency):

```python
from collections import Counter

class Solution:
    def filterCharacters(self, s: str, k: int) -> str:
        ans = []

        counter = Counter(s)

        for c in s:
            if counter[c] < k:
                ans.append(c)

        return ''.join(ans)
```

