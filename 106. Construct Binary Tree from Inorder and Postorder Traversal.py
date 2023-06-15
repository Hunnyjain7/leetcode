from typing import List, Optional

from utils.tree_node import TreeNode


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:  # noqa
        if not inorder or not postorder:
            return None

        i = len(inorder) - 1
        p = len(postorder) - 1

        stack = []
        prev = None
        root = TreeNode(postorder[p])
        stack.append(root)
        p -= 1

        while p >= 0:
            while stack and stack[-1].val == inorder[i]:
                prev = stack.pop()
                i -= 1

            node = TreeNode(postorder[p])

            if prev:
                prev.left = node
            elif stack:
                curr = stack[-1]
                curr.right = node

            stack.append(node)
            prev = None
            p -= 1

        return root


if __name__ == '__main__':
    print(Solution().buildTree([9, 3, 15, 20, 7], [9, 15, 7, 20, 3]))
