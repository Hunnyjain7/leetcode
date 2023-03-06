# Definition for singly-linked list.
from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def mergeTwoList(left, right):
            dummy = mergelist = ListNode()
            while left and right:
                if left.val < right.val:
                    mergelist.next = left
                    mergelist = mergelist.next
                    left = left.next
                else:
                    mergelist.next = right
                    mergelist = mergelist.next
                    right = right.next
            if left or right:
                mergelist.next = left if left else right
            return dummy.next

        lists_len = len(lists)
        if lists_len == 0:
            return None
        if lists_len == 1:
            return lists[0]

        new_head = mergeTwoList(lists[0], lists[1])

        count = 2
        while count < lists_len:
            new_head = mergeTwoList(lists[count], new_head)
            count += 1
        return new_head


if __name__ == '__main__':
    pass
    # print(Solution().mergeKLists())
