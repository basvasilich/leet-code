# https://leetcode.com/problems/linked-list-cycle-ii/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        cur = head
        pointer_1 = None
        pointer_2 = None
        counter = 0
        need_pointer_2 = True

        while cur is not None and cur != pointer_1:

            if cur == pointer_2:
                need_pointer_2 = False
                pointer_1 = pointer_1.next

            if counter == 4 and need_pointer_2:
                counter = 0
                pointer_2 = pointer_2.next

            if pointer_1 is None:
                pointer_1 = head
            if pointer_2 is None:
                pointer_2 = head

            counter += 1
            cur = cur.next

        if cur is None:
            return cur

        return pointer_1
