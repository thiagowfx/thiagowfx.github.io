
[LeetCode #2215: Find the Difference of Two Arrays](https://leetcode.com/problems/find-the-difference-of-two-arrays):

```python
class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        s1 = set(nums1)
        s2 = set(nums2)

        return [list(s1 - s2), list(s2 - s1)]
```

