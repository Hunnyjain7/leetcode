from collections import deque
from typing import Optional, List

from utils.tree_node import TreeNode


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:  # noqa
        queue = deque()
        res = []
        if root:
            res.append([root.val])
            queue.append(root)
            right = True
            while queue:
                curr = []
                nex = deque()
                while queue:
                    hp = queue.popleft()
                    if hp.left:
                        nex.append(hp.left)
                        curr.append(hp.left.val)
                    if hp.right:
                        nex.append(hp.right)
                        curr.append(hp.right.val)
                if curr:
                    if right:
                        curr = curr[::-1]
                        right = False
                    else:
                        right = True
                    res.append(curr)
                queue = nex
        return res
