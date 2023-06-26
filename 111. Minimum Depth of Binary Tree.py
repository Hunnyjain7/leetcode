from typing import Optional

from utils.tree_node import TreeNode


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:  # noqa
        min_depth = float('inf')

        def dfs(root_node, depth):
            nonlocal min_depth
            if not root_node:
                return min_depth
            if not root_node.left and not root_node.right:
                min_depth = min(min_depth, depth)
                return min_depth

            dfs(root_node.left, depth + 1)
            dfs(root_node.right, depth + 1)
            return min_depth

        return dfs(root, 1) if root else 0
