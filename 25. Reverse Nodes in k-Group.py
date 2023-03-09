from collections import deque
from typing import Optional

from utils.list_node import ListNode


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:  # noqa
        temp = head
        adummy = dummy = ListNode()
        count = 1
        initial = None
        last = None
        while temp:
            if not last:
                last = temp
            if count == k:
                if temp.next:
                    nex = temp.next
                else:
                    nex = None

                temp.next = None

                prev = None
                curr = initial
                while curr:
                    next = curr.next
                    curr.next = prev
                    prev = curr
                    curr = next

                while dummy:
                    if not dummy.next:
                        dummy.next = prev or temp
                        break
                    dummy = dummy.next
                temp = nex
                last = None
                count = 1
                initial = None
            else:
                count += 1
                if not initial:
                    initial = temp
                temp = temp.next
        if last:
            while dummy:
                if not dummy.next:
                    dummy.next = last
                    break
                dummy = dummy.next
        elif temp:
            while dummy:
                if not dummy.next:
                    dummy.next = temp
                    break
                dummy = dummy.next
        return adummy.next


if __name__ == '__main__':
    pass
