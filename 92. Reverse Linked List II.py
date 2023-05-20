from typing import Optional

from utils.list_node import ListNode


class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:  # noqa
        if left == right:
            return head

        temp = head
        temp_node = None
        count = 1
        while head:
            if count == left:
                while count != right:
                    prev = ListNode(head.val, temp_node)
                    temp_node = prev
                    head = head.next
                    count += 1
                    if count == right:
                        prev = ListNode(head.val, temp_node)
                        temp_node = prev
                        break
            if count == right:
                break
            head = head.next
            count += 1

        new_node = temp_node
        while temp_node.next:
            temp_node = temp_node.next
        temp_node.next = head.next

        temp_new_node = temp
        if left != 1:
            count = 1
            while temp.next and count != left - 1:
                temp = temp.next
                count += 1
            temp.next = new_node
        return temp_new_node if left != 1 else new_node
