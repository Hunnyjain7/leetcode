from typing import Optional

from utils.tree_node import TreeNode


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:  # noqa
        def inorder(node, mini, maxi):
            if node is None:
                return True
            if node.val <= mini or node.val >= maxi:
                return False
            return inorder(node.left, mini, node.val) and inorder(node.right, node.val, maxi)

        return inorder(root, float('-inf'), float('inf'))
