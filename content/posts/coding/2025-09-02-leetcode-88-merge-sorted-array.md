---
title: "LeetCode #88: Merge Sorted Array"
date: 2025-09-02T23:51:51+02:00
tags:
  - dev

categories:
  - coding
---

[LeetCode #88: Merge Sorted Array](https://leetcode.com/problems/merge-sorted-array/):

The original problem states:

> Do not return anything, modify `nums1` in-place instead.

Instead, I opted for allocating a new list.

## Naive and elegant

`O((m + n) * log (m + n))`. Total disregard for the fact the inputs are already
sorted[^3].

```python
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        return sorted(nums1 + nums2)
```

## Optimal

`O(m + n)`. We can achieve a linear solution by iterating only _once_ on each
element, keeping track of **two pointers**.

Storage: we can either start with an empty list and keep appending[^1] to it, or
preallocate `m + n` elements and simply populate them[^2].

```python
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        p1 = p2 = 0
        a = [None] * (m + n)
        # OR a = []

        while (p1 + p2) < (m + n):
          pa = p1 + p2

          if p2 >= n or (p1 < m and nums1[p1] < nums2[p2]):
            a[pa] = nums1[p1]
            # OR a.append(nums1[p1])
            p1 += 1
          else:
            a[pa] = nums2[p2]
            # OR a.append(nums2[p2])
            p2 += 1

        return a
```

## Original: Naive and elegant

The original problem modifies `num1` in-place.

```python
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        nums1[m:] = nums2
        nums1.sort()
```

## Original: Optimal

On top of the previous solution, just amend the end:

```python
for i, el in enumerate(a):
    nums1[i] = el
```

Or, use list slicing:

```python
nums1[:] = a
```

Note that a simple assignment (`nums1 = a` or `nums1 = a.copy()`) does not
entail in-place modification.

A solution from scratch, without allocating a separate list, could look like
this:

```python
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        p1 = p2 = 0

        while p1 < m:

            if p2 >= n or nums1[p1] < nums2[p2]:
                p1 += 1
            else:
                nums1[p1], nums2[p2] = nums2[p2], nums1[p1]
                p1 += 1

        def mysorted(v):
            for i in range(len(v) - 1):
                if v[i] > v[i+1]:
                    v[i], v[i+1] = v[i+1], v[i]

            return v

        nums1[m:] = mysorted(nums2.copy())
```

Except that it fails for the following input:

```
nums1: [4,5,6,0,0,0]
m = 3
nums2: [1,2,3]
n = 3

result: [1,4,5,2,3,6]
```

A revised solution † starts from the end, to account for the fact we need to
modify the list in-place:

```python
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        p1 = m - 1
        p2 = n - 1

        while p1 >= 0 and p2 >= 0:
            if nums1[p1] < nums2[p2]:
                nums1[p1 + p2 + 1] = nums2[p2]
                p2 -= 1
            else:
                nums1[p1 + p2 + 1] = nums1[p1]
                p1 -= 1

        # This is a no-op
        # while p1 >= 0:
        #     nums1[p1 + p2 + 1] = nums1[p1]
        #     p1 -= 1

        while p2 >= 0:
            nums1[p1 + p2 + 1] = nums2[p2]
            p2 -= 1

        # OR:
        # nums1[:p2 + 1] = nums2[:p2 + 1]
```

[^1]: Given `a = []`, do either `a.append(1)` or `a += [1]`.

[^2]: `a = nums1 + nums2` or `a = [None] * (m + n)`.

[^3]: `a = [3, 2, 1]; a.sort()` modifies `a` in-place, whereas `sorted(a)`
    creates a new list.
