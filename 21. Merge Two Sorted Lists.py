from typing import Optional

from utils.list_node import ListNode


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:  # noqa
        dummy = mergelist = ListNode()
        while list1 and list2:
            if list1.val < list2.val:
                mergelist.next = list1
                list1, mergelist = list1.next, mergelist.next
            else:
                mergelist.next = list2
                list2, mergelist = list2.next, mergelist.next

        if list1 or list2:
            mergelist.next = list1 if list1 else list2

        return dummy.next


if __name__ == '__main__':
    l1 = ListNode(1)
    a = l1.next = ListNode(2)
    a.next = ListNode(3)
    print(Solution().mergeTwoLists(l1, l1))
