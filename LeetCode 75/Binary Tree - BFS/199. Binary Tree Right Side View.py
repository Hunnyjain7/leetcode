"""Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes
you can see ordered from top to bottom.

Example 1:

Input: root = [1,2,3,null,5,null,4]
Output: [1,3,4]

Example 2:

Input: root = [1,null,3]
Output: [1,3]

Example 3:

Input: root = []
Output: []

Constraints:

The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100"""
from typing import Optional, List

from utils.tree_node import TreeNode


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:  # noqa
        queue, rights = [], []
        if root:
            queue.append(root)

        while queue:
            curr, nex = [], []
            for node in queue:
                if node.left:
                    nex.append(node.left)
                if node.right:
                    nex.append(node.right)
                curr.append(node.val)
            if curr:
                rights.append(curr[-1])
            queue = nex
        return rights
