"""Given the root of a binary tree and an integer targetSum, return the number of paths where the sum of the values
along the path equals targetSum.

The path does not need to start or end at the root or a leaf, but it must go downwards (i.e., traveling only from
parent nodes to child nodes).

Example 1:

Input: root = [10,5,-3,3,2,null,11,3,-2,null,1], targetSum = 8
Output: 3
Explanation: The paths that sum to 8 are shown.

Example 2:

Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
Output: 3

Constraints:

The number of nodes in the tree is in the range [0, 1000].
-109 <= Node.val <= 109
-1000 <= targetSum <= 1000"""
from typing import Optional

from utils.tree_node import TreeNode


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:  # noqa
        def dfs(node, prefix_sum, curr_sum, count):
            if not node:
                return count

            curr_sum += node.val
            count += prefix_sum.get(curr_sum - targetSum, 0)
            prefix_sum[curr_sum] = prefix_sum.get(curr_sum, 0) + 1

            count = dfs(node.left, prefix_sum, curr_sum, count)
            count = dfs(node.right, prefix_sum, curr_sum, count)

            prefix_sum[curr_sum] -= 1
            return count

        return dfs(root, {0: 1}, 0, 0)
