---
title: "LeetCode #112: Path Sum"
date: 2025-12-24T04:22:53-03:00
tags:
  - dev
  - leetcode

categories:
  - coding
---

[LeetCode #112: Path Sum](https://leetcode.com/problems/path-sum):

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        if root.val == targetSum and not root.left and not root.right:
            return True

        return any([
            self.hasPathSum(root.left, targetSum - root.val),
            self.hasPathSum(root.right, targetSum - root.val),
        ])
```

Note:

```python
if root.val == targetSum and not root.left and not root.right:
    return True
```

If we **DO NOT** check for the absence of `root.left` and `root.right` (i.e.
leaf node), then we fail on input `2 <- 1` with `targetSum = 1`.
