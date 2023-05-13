from typing import Optional

from utils.list_node import ListNode


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:  # noqa
        temp = head
        while head:
            while head and head.next and head.val == head.next.val:
                head.next = head.next.next
            head = head.next
        return temp
