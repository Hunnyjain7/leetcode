"""You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807."""
from utils.list_node import ListNode


def lst2link(lst):
    cur = dummy = ListNode(0)
    for e in lst:
        cur.next = ListNode(e)
        cur = cur.next
    return dummy.next


class Solution(object):
    def nl_to_l(self, n):  # noqa
        l = []  # noqa
        while n is not None:
            l.append(n.val)
            n = n.next
        return l

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l1 = self.nl_to_l(l1)
        l2 = self.nl_to_l(l2)

        l1 = l1[::-1]
        l2 = l2[::-1]
        l1_str = ''
        l2_str = ''
        for i in l1:
            l1_str += str(i)
        for i in l2:
            l2_str += str(i)
        l1_l2 = [int(i) for i in str(int(l1_str) + int(l2_str))]
        return lst2link(l1_l2[::-1])


obj = Solution()
o = obj.addTwoNumbers(lst2link([2, 4, 3]), lst2link([5, 6, 4]))
print(o.val)
