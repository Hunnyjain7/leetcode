from typing import Optional

from utils.list_node import ListNode


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:  # noqa
        dummy = ListNode(head.val, head)
        first = dummy
        second = head

        while n > 0 and second:
            second = second.next
            n -= 1

        while second:
            first = first.next
            second = second.next
        first.next = first.next.next
        return dummy.next
