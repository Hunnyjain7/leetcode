from typing import Optional

from utils.list_node import ListNode


class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:  # noqa
        if left == right:
            return head

        temp = head
        temp_node = None
        previous = None
        while head:
            if head.val == left:
                while head.val != right:
                    prev = ListNode(head.val, temp_node)
                    temp_node = prev
                    head = head.next
                    if head.val == right:
                        prev = ListNode(head.val, temp_node)
                        temp_node = prev
                        break
            if head.val == right:
                break
            previous = head.val
            head = head.next

        new_node = temp_node
        while temp_node.next:
            temp_node = temp_node.next
        temp_node.next = head.next

        while temp.val != previous:
            temp = temp.next
        temp.next = new_node
        return temp
