from typing import Optional

from utils.list_node import ListNode


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:  # noqa
        bdummy = adummy = ListNode()
        if not head:
            return None
        if not head.next:
            return head
        while head and head.next:
            count = 0
            temp = head.next
            head.next = head.next.next
            temp.next = head
            head = temp
            head = head.next.next
            while adummy:
                if count == 2 or not adummy.next:
                    adummy.next = temp
                    break
                adummy = adummy.next
                count += 1
        return bdummy.next

    # better approach from leetcode
    def swapPairs2(self, head: Optional[ListNode]) -> Optional[ListNode]:  # noqa
        left = dummy = ListNode(0, head)

        while left.next and left.next.next:
            second = left.next
            third = second.next

            second.next = third.next
            third.next = second

            left.next = third
            left = second

        return dummy.next


if __name__ == '__main__':
    pass
