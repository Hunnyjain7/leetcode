"""You are given the root of a binary tree.

A ZigZag path for a binary tree is defined as follow:

Choose any node in the binary tree and a direction (right or left).
If the current direction is right, move to the right child of the current node; otherwise, move to the left child.
Change the direction from right to left or from left to right.
Repeat the second and third steps until you can't move in the tree.
Zigzag length is defined as the number of nodes visited - 1. (A single node has a length of 0).

Return the longest ZigZag path contained in that tree.

Example 1:

Input: root = [1,null,1,1,1,null,null,1,1,null,1,null,null,null,1]
Output: 3
Explanation: Longest ZigZag path in blue nodes (right -> left -> right).

Example 2:

Input: root = [1,1,1,null,1,null,null,1,1,null,1]
Output: 4
Explanation: Longest ZigZag path in blue nodes (left -> right -> left -> right).

Example 3:

Input: root = [1]
Output: 0

Constraints:

The number of nodes in the tree is in the range [1, 5 * 104].
1 <= Node.val <= 100"""
from typing import Optional

from utils.tree_node import TreeNode


class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.res = 0  # noqa

        def dfs(root_node, count, prev):
            self.res = max(self.res, count)

            if root_node.left:
                dfs(root_node.left, count + 1, "left") if prev != "left" else dfs(root_node.left, 1, "left")
            if root_node.right:
                dfs(root_node.right, count + 1, "right") if prev != "right" else dfs(root_node.right, 1, "right")

        dfs(root, 0, "")
        return self.res
