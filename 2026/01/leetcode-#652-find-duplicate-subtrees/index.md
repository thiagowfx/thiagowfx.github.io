
[LeetCode #652: Find Duplicate Subtrees](https://leetcode.com/problems/find-duplicate-subtrees):

Original, 119 / 175 testcases passed:

```python
from collections import defaultdict

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        mappings = defaultdict(list)

        def dfs(node):
            if not node:
                return

            mappings[node.val].append(node)

            dfs(node.left)
            dfs(node.right)

        dfs(root)

        ans = set()

        def duplicate_subtree(node1, node2):
            if not node1 and not node2:
                return True

            if not node1 and node2:
                return False

            if node1 and not node2:
                return False

            return node1.val == node2.val and duplicate_subtree(node1.left, node2.left) and duplicate_subtree(node1.right, node2.right)

        for nodes in mappings.values():
            for i, node1 in enumerate(nodes[:-1]):
                for node2 in nodes[i + 1:]:
                    if duplicate_subtree(node1, node2):
                        ans.add(node1)

        return list(ans)
```

With proper serialization:

```shell
from collections import Counter

class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        # serial -> count
        seen = Counter()

        # serial -> node
        node_from_serial = {}

        def dfs(node) -> str:
            """Return the serialized representation of the node."""
            if not node:
                return "null"

            s = f"{node.val},{dfs(node.left)},{dfs(node.right)}"

            node_from_serial[s] = node

            seen[s] += 1

            return s

        dfs(root)

        ans = []

        for (serial, count) in seen.items():
            if count >= 2:
                ans.append(node_from_serial[serial])

        return ans
```

Optimized:

```python
from collections import Counter

class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        # serial -> count
        seen = Counter()

        ans = []

        def dfs(node) -> str:
            """Return the serialized representation of the node."""
            if not node:
                return "null"

            s = f"{node.val},{dfs(node.left)},{dfs(node.right)}"

            seen[s] += 1

            if seen[s] == 2:
                ans.append(node)

            return s

        dfs(root)

        return ans
```

