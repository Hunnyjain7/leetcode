from collections import deque
from typing import Optional

from utils.list_node import ListNode


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:  # noqa
        dummy = ListNode()

        queue = deque()
        count = 1
        while head:
            print(count)
            if count == k:
                count = 1
                # dummy.next = head
                print(queue)
                curr = temp = queue.popleft()
                i = 1
                while temp:
                    if i == k:
                        temp.next = None
                        print("curr", curr)
                        prev = None
                        while curr:
                            next = curr.next
                            curr.next = prev
                            prev = curr
                            curr = next
                        while dummy:
                            if not dummy.next:
                                dummy.next = prev
                                break

                        # dummy.next = prev
                        print("reversed prev", prev)
                        # break
                    i += 1
                    temp = temp.next
                # break
                queue = deque()
            else:
                queue.append(head)
                count += 1
            head = head.next
        return dummy.next


if __name__ == '__main__':
    pass
