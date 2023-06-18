from typing import List, Optional

from utils.tree_node import TreeNode


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:  # noqa
        if not nums:
            return
        mid = len(nums) // 2
        return TreeNode(nums[mid], self.sortedArrayToBST(nums[:mid]), self.sortedArrayToBST(nums[mid + 1:]))


if __name__ == '__main__':
    print(Solution().sortedArrayToBST([-10, -3, 0, 5]))
