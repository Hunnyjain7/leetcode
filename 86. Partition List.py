from typing import Optional

from utils.list_node import ListNode


class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:  # noqa
        temp = head
        while head and head.next:
            if head.next.val == x:
                print("in")
                curr = head.next
                last_temp = last = ListNode()
                while curr:
                    if curr.val < x:
                        head.next = curr
                        head = head.next
                        # break
                        print("IN IF")
                        print("curr", curr)
                        print("head", head)
                        print("temp", temp)
                    else:
                        while last.next is not None:
                            last = last.next
                        last.next = ListNode(curr.val)
                        print("IN ELSE")
                        print("last", last)
                        print("last_temp", last_temp)
                        print("curr", curr)
                        print("head", head)
                        print("temp", temp)
                    curr = curr.next
                head.next = last_temp.next
            head = head.next

        return temp
