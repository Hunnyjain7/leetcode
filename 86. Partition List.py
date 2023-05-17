from typing import Optional

from utils.list_node import ListNode


class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:  # noqa
        less_head = less_tail = ListNode()
        greater_head = greater_tail = ListNode()

        while head:
            if head.val < x:
                less_tail.next = head
                less_tail = less_tail.next
            else:
                greater_tail.next = head
                greater_tail = greater_tail.next
            head = head.next
        greater_tail.next = None
        less_tail.next = greater_head.next
        return less_head.next
