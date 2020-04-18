# https://leetcode.com/problems/intersection-of-two-linked-lists/


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        pointer_a = headA
        pointer_b = headB
        swith_a = False
        swith_b = False

        if pointer_a == pointer_b:
            return pointer_a

        if pointer_a is None or pointer_b is None:
            return None

        while pointer_a != pointer_b:

            if pointer_a.next is None:
                if swith_a:
                    return None
                pointer_a = headB
                swith_a = True
            else:
                pointer_a = pointer_a.next

            if pointer_b.next is None:
                pointer_b = headA
                if swith_b:
                    return None
                swith_b = True
            else:
                pointer_b = pointer_b.next

        return pointer_a


