from typing import Optional

from utils.tree_node import TreeNode


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:  # noqa
        def dfs(root_node):
            if not root_node:
                return 0
            left, right = dfs(root_node.left), dfs(root_node.right)
            if left < 0 or right < 0 or abs(left - right) > 1:
                return -1
            return max(left, right) + 1

        return dfs(root) >= 0

    def isBalanced2(self, root: Optional[TreeNode]) -> bool:  # noqa
        def dfs(root_node):
            if not root_node:
                return [True, 0]

            left, right = dfs(root_node.left), dfs(root_node.right)
            balanced = left[0] and right[0] and abs(left[1] - right[1])
            return [balanced, max(left[1], right[1]) + 1]

        return dfs(root)[0]
