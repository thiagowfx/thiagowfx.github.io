
[LeetCode #274: H-Index](https://leetcode.com/problems/h-index):

```python
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)

        h = 0

        while h < len(citations):
            if h < citations[h]:
                h += 1
            else:
                break

        return h
```

