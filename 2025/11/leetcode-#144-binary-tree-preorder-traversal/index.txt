
[LeetCode #144: Binary Tree Preorder Traversal](https://leetcode.com/problems/binary-tree-preorder-traversal):

Sequence:

- current node
- left
- right

## Recursive

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []

        return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)
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
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []

        def preorder(node):
            if not node:
                return

            ans.append(node.val)
            preorder(node.left)
            preorder(node.right)

        preorder(root)

        return ans
```

