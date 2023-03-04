# Definition for singly - linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, list1)
        a = list1
        while list1:
            temp = list2
            while temp:
                if temp.val <= list1.val:
                    dummy.next = ListNode(temp.val, list1)
                temp = temp.next
            list1 = list1.next
        return dummy.next


if __name__ == '__main__':
    l1 = ListNode(1)
    a = l1.next = ListNode(2)
    a.next = ListNode(3)
    print(Solution().mergeTwoLists(l1, l1))
