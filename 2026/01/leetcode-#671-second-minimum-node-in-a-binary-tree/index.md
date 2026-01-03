
[LeetCode #671: Second Minimum Node In a Binary Tree](https://leetcode.com/problems/second-minimum-node-in-a-binary-tree):

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        two_min = set()

        def update(n):
            two_min.add(n)

            if len(two_min) > 2:
                two_min.remove(max(two_min))

        def dfs(node):
            if node:
                update(node.val)
                dfs(node.left)
                dfs(node.right)

        dfs(root)

        return max(two_min) if len(two_min) == 2 else -1
```

