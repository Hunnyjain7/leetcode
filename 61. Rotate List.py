from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:  # noqa
        cur = curr = head
        new = ListNode()
        if not head or not head.next or k == 0:
            return head

        # recursive
        def length(node: ListNode):
            return 0 if not node else 1 + length(node.next)

        lll = length(cur)
        print(lll)
        k = k % lll
        if not head or not head.next or k == 0:
            return head

        print(k)
        gotcha = False
        while k >= 0 and head.next:
            temp = head
            head = head.next
            temp.next = None
            while new.next:
                new = new.next
            new.next = temp
            k -= 1
            if not head.next and k == 0:
                print("in")
                gotcha = True
            print(head)
            print("temp", temp)
            print("curr", curr)
            print("new", new)
            print("====================")

        clone = head
        while head.next:
            head = head.next
        print("clone", clone)
        print("head", head)
        head.next = curr
        print("clone", clone)
        print("head", head)

        def rearrange(hea):
            # proceed only when the list is valid
            if hea is None or hea.next is None:
                return hea

            ptr = hea

            # move to the second last node
            while ptr.next.next:
                ptr = ptr.next

            # transform the list into a circular list
            ptr.next.next = hea

            hea = ptr.next  # Fix head
            ptr.next = None  # break the chain
            return hea

        if gotcha:
            return rearrange(clone)

        print("ENDED")
        return clone
