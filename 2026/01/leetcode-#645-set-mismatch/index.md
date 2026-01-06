
[LeetCode #645: Set Mismatch](https://leetcode.com/problems/set-mismatch):

```python
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)

        s = set(nums)
        t = set(range(1, n + 1))

        missing = (t - s).pop()
        duplicate = Counter(nums).most_common(1)[0][0]

        return [duplicate, missing]
```

