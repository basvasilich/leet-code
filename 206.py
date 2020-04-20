# https://leetcode.com/problems/reverse-linked-list/


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        pointer_prev = None
        pointer_current = head

        while pointer_current is not None:
            next_tmp = pointer_current.next
            pointer_current.next = pointer_prev
            pointer_prev = pointer_current
            pointer_current = next_tmp

        return pointer_prev
