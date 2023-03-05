# Definition for singly-linked list.
from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = list1 = ListNode()

        for lis in lists:
            if list1 and lis and lis.next:
                list1.next, list1 = lis, list1.next
        return dummy


if __name__ == '__main__':
    pass
    # print(Solution().mergeKLists())
