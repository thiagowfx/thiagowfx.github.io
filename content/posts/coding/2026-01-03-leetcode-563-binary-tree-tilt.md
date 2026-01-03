---
title: "LeetCode #563: Binary Tree Tilt"
date: 2026-01-03T02:56:33-03:00
categories:
  - coding
---

[LeetCode #563: Binary Tree Tilt](https://leetcode.com/problems/binary-tree-tilt):

Works but it's slow, too many recomputations:

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        def mysum(node) -> int:
            if not node:
                return 0

            return node.val + mysum(node.left) + mysum(node.right)

        def tilt(node) -> int:
            if not node:
                return 0

            return abs(mysum(node.left) - mysum(node.right))

        def sum_tilt(node) -> int:
            if not node:
                return 0

            return tilt(node) + sum_tilt(node.left) + sum_tilt(node.right)

        return sum_tilt(root)
```

Better, with memoization:

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    from functools import cache

    def findTilt(self, root: Optional[TreeNode]) -> int:
        @cache
        def mysum(node) -> int:
            if not node:
                return 0

            return node.val + mysum(node.left) + mysum(node.right)

        def tilt(node) -> int:
            if not node:
                return 0

            return abs(mysum(node.left) - mysum(node.right))

        def sum_tilt(node) -> int:
            if not node:
                return 0

            return tilt(node) + sum_tilt(node.left) + sum_tilt(node.right)

        return sum_tilt(root)
```

Even better, with a single pass:

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        ans = 0

        # the sum
        def dfs(node):
            if not node:
                return 0

            left_sum = dfs(node.left)
            right_sum = dfs(node.right)

            tilt = abs(left_sum - right_sum)
            ans += tilt

            return left_sum + right_sum + node.val

        dfs(root)

        return ans
```

`dfs` tracks the total sum at the node.

Then, as we're already visiting each node and have its subtree sums, we
compute each node tilt right away, adding it to the final answer.
