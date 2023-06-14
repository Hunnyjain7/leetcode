from typing import Optional, List

from utils.tree_node import TreeNode


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:  # noqa
        in_index_map = dict(map(reversed, enumerate(inorder)))  # noqa
        root_idx = 0

        def build_tree(left, right):
            nonlocal root_idx
            if left > right:
                return None

            value = preorder[root_idx]
            root = TreeNode(value)
            root_idx += 1

            root.left = build_tree(left, in_index_map[value] - 1)
            root.right = build_tree(in_index_map[value] + 1, right)
            return root

        return build_tree(0, len(inorder) - 1)


if __name__ == '__main__':
    print(Solution().buildTree([3, 9, 20, 15, 7], [9, 3, 15, 20, 7]))
