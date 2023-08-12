"""Given the root of a binary tree, the level of its root is 1, the level of its children is 2, and so on.

Return the smallest level x such that the sum of all the values of nodes at level x is maximal.

Example 1:

Input: root = [1,7,0,7,-8,null,null]
Output: 2
Explanation:
Level 1 sum = 1.
Level 2 sum = 7 + 0 = 7.
Level 3 sum = 7 + -8 = -1.
So we return the level with the maximum sum which is level 2.

Example 2:

Input: root = [989,null,10250,98693,-89388,null,null,null,-32127]
Output: 2

Constraints:

The number of nodes in the tree is in the range [1, 104].
-105 <= Node.val <= 105"""
from typing import Optional

from utils.tree_node import TreeNode


class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:  # noqa
        queue, res = [], float("-inf")
        if root:
            queue.append(root)
        s_level, level = 0, 0
        while queue:
            curr, nex = [], []
            for node in queue:
                if node.left:
                    nex.append(node.left)
                if node.right:
                    nex.append(node.right)
                curr.append(node.val)
            queue = nex
            level += 1
            if curr:
                curr_sum = sum(curr)
                if curr_sum > res:
                    s_level = level
                    res = curr_sum
        return s_level
