from typing import Optional

from utils.list_node import ListNode
from utils.tree_node import TreeNode


class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if not head:
            return
        if not head.next:
            return TreeNode(head.val)
        slow, fast = head, head.next.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        val, right, slow.next = slow.next.val, slow.next.next, None
        return TreeNode(val, self.sortedListToBST(head), self.sortedListToBST(right))
