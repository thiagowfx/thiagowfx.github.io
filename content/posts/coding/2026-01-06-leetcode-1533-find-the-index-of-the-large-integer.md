---
title: "LeetCode #1533: Find the Index of the Large Integer"
date: 2026-01-06T04:07:41-03:00
tags:
  - dev
  - leetcode
categories:
  - coding
---

[LeetCode #1533: Find the Index of the Large Integer](https://leetcode.com/problems/find-the-index-of-the-large-integer):

```python
# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
#class ArrayReader(object):
#	 # Compares the sum of arr[l..r] with the sum of arr[x..y]
#	 # return 1 if sum(arr[l..r]) > sum(arr[x..y])
#	 # return 0 if sum(arr[l..r]) == sum(arr[x..y])
#	 # return -1 if sum(arr[l..r]) < sum(arr[x..y])
#    def compareSub(self, l: int, r: int, x: int, y: int) -> int:
#
#	 # Returns the length of the array
#    def length(self) -> int:
#


class Solution:
    def getIndex(self, reader: 'ArrayReader') -> int:
        n = reader.length()

        l = 0
        r = n - 1

        while l < r and (r - l) > 1:
            print(l, r)
            mid = (l + r) // 2

            even = ((r - l) % 2) == 0

            # [l, mid - 1]
            # [mid + 1, r]
            if even:
                q = reader.compareSub(l, mid - 1, mid + 1, r)
                if q == 0:
                    return mid
                # left half is bigger
                elif q == 1:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                q = reader.compareSub(l, mid, mid + 1, r)
                if q == 0:
                    assert False
                # left half is bigger
                elif q == 1:
                    r = mid
                else:
                    l = mid

        if l == r:
            return l

        q = reader.compareSub(l, l, l + 1, l + 1)
        return l if q > 0 else (l + 1)

        # [0, 0, 1, 0, 0]
        #  l     m     r

        # [0, 0, 1, 0]
        #  l  m     r

        # [0, 0, 1]
        #  l  m  r

        # [ 0,  1]
        #  lm   r
```
