from typing import Optional

from utils.list_node import ListNode


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:  # noqa
        curr = head
        if not head or not head.next or k == 0:
            return head

        def length(head: ListNode):  # noqa
            return 0 if not head else 1 + length(head.next)

        node_length = length(curr)
        k = k % node_length
        if k == 0:
            return head
        new = ListNode()
        for k in range(node_length - k):
            temp = head
            head = head.next
            temp.next = None
            while new.next:
                new = new.next
            new.next = temp

        clone = head
        while head.next:
            head = head.next
        head.next = curr
        return clone


if __name__ == '__main__':
    node = ListNode(1)
    node.next = ListNode(2)
    node.next = ListNode(3)
    node.next = ListNode(4)
    node.next = ListNode(5)
    print(Solution().rotateRight(node, 2))
