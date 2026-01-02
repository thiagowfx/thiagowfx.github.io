
[LeetCode #102: Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal):

```python
from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        ans = []

        queue = deque([root])
        while queue:
            level = []

            for _ in range(len(queue)):
                node = queue.popleft()

                level.append(node.val)

                for child in [node.left, node.right]:
                    if child:
                        queue.append(child)

            ans.append(level)

        return ans
```

