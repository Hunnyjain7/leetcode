from typing import Optional, List

from utils.tree_node import TreeNode


class Solution:
    def __init__(self):
        self.res = []

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return  # noqa
        self.inorderTraversal(root.left)
        self.res.append(root.val)
        self.inorderTraversal(root.right)
        return self.res
