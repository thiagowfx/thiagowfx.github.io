---
title: "LeetCode #104: Maximum Depth of Binary Tree"
url: https://perrotta.dev/2026/01/leetcode-%23104-maximum-depth-of-binary-tree/
last_updated: 2026-01-05
---


[LeetCode #104: Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree):

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
```

