from typing import Optional, List

from utils.tree_node import TreeNode


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:  # noqa
        def dfs(root_node, curr, res):
            if not root_node:
                return res
            if not root_node.left and not root_node.right:
                curr.append(root_node.val)
                if sum(curr) == targetSum:
                    res.append(curr.copy())
                curr.pop()
                return res

            curr.append(root_node.val)
            res = dfs(root_node.left, curr, res)
            res = dfs(root_node.right, curr, res)
            curr.pop()
            return res

        return dfs(root, [], [])
