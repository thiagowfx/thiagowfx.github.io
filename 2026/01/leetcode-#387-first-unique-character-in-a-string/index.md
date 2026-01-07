
[LeetCode #387: First Unique Character in a String](https://leetcode.com/problems/first-unique-character-in-a-string):

```python
from collections import Counter

class Solution:
    def firstUniqChar(self, s: str) -> int:
        counter = Counter(s)
        for i, c in enumerate(s):
            if counter[c] == 1:
                return i

        return -1
```

