from typing import Optional, List

from utils.tree_node import TreeNode


class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:  # noqa
        memo = {}

        def generate_trees(start, end):
            if start > end:
                return [None]

            if (start, end) in memo:
                return memo[(start, end)]

            results = []
            for i in range(start, end + 1):
                left_subtrees = generate_trees(start, i - 1)
                right_subtrees = generate_trees(i + 1, end)
                for left in left_subtrees:
                    for right in right_subtrees:
                        root = TreeNode(i)
                        root.left = left
                        root.right = right
                        results.append(root)
            memo[(start, end)] = results
            return results

        return generate_trees(1, n)
