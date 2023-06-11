from collections import deque
from typing import Optional

from utils.tree_node import TreeNode


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:  # noqa
        queue = deque()
        if root:
            queue.append(root)

        level = 0
        while queue:
            for i in range(len(queue)):
                curr = queue.popleft()
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            level += 1
        return level
