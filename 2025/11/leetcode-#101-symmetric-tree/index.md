
[LeetCode #101: Symmetric Tree](https://leetcode.com/problems/symmetric-tree):

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True

        def mirror(left, right):
            if left is None and left is None:
                return True

            if left is None or right is None:
                return False

            if left.val != right.val:
                return False

            return mirror(left.left, right.right) and mirror(left.right, right.left)

        return mirror(root.left, root.right)
```

