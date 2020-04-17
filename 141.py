# https://leetcode.com/problems/linked-list-cycle/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        pointer_fast = head
        pointer_slow = head
        count = 0

        if head is None or head.next is None:
            return False

        while pointer_fast is not None:

            if count == 2:
                count = 0
                pointer_slow = pointer_slow.next

            pointer_fast = pointer_fast.next

            if pointer_fast == pointer_slow:
                return True

            count += 1

        return False
