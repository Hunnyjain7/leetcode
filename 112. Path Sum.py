from typing import Optional

from utils.tree_node import TreeNode


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:  # noqa
        def dfs(root_node, has, curr):
            if has:
                return has
            if not root_node:
                return has
            if not root_node.left and not root_node.right:
                curr += root_node.val
                if curr == targetSum:
                    has = True
                curr -= root_node.val
                return has

            curr += root_node.val
            has = dfs(root_node.left, has, curr)
            has = dfs(root_node.right, has, curr)
            curr -= root_node.val
            return has

        return dfs(root, False, 0)
