from typing import Optional

from utils.tree_node import TreeNode


class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:  # noqa
        """
        Do not return anything, modify root in-place instead.
        """
        prev = None
        first = None
        second = None

        def in_order(root_node):
            if not root_node:
                return
            in_order(root_node.left)
            nonlocal prev
            if prev and prev.val >= root_node.val:  # noqa
                nonlocal first, second
                if not first:
                    first = prev
                second = root_node
            prev = root_node
            in_order(root_node.right)

        in_order(root)
        if first and second:
            first.val, second.val = second.val, first.val  # noqa
