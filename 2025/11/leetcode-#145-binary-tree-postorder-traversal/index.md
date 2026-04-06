---
title: "LeetCode #145: Binary Tree Postorder Traversal"
url: https://perrotta.dev/2025/11/leetcode-%23145-binary-tree-postorder-traversal/
last_updated: 2026-01-03
---


[LeetCode #145: Binary Tree Postorder
Traversal](https://leetcode.com/problems/binary-tree-postorder-traversal):

Sequence:

- left
- right
- current node

## Recursive

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []

        return self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val]
```

Alternative:

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []

        def postorder(node):
            if node:
                postorder(node.left)
                postorder(node.right)
                ans.append(node.val)

        postorder(root)

        return ans
```

