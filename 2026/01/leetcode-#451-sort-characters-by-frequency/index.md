
[LeetCode #451: Sort Characters By Frequency](https://leetcode.com/problems/sort-characters-by-frequency):

```python
class Solution:
    def frequencySort(self, s: str) -> str:
        return ''.join([c * v for (c, v) in Counter(s).most_common()])
```

