
[LeetCode #350: Intersection of Two Arrays II](https://leetcode.com/problems/intersection-of-two-arrays-ii):

```python
from collections import Counter

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        c1 = Counter(nums1)
        c2 = Counter(nums2)

        common = set(c1.keys()) & set(c2.keys())

        ans = []

        for n in common:
            ans.extend([n] * min(c1[n], c2[n]))

        return ans
```

