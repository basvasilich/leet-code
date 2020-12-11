# https://leetcode.com/problems/palindrome-linked-list/
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head:
            return True

        if not head.next:
            return True

        values = []

        while head:
            values.append(head.val)
            head = head.next

        pointer_s = 0

        pointer_e = len(values) - 1

        while pointer_s <= pointer_e:
            if values[pointer_s] != values[pointer_e]:
                return False
            pointer_s += 1
            pointer_e -= 1

        return True
