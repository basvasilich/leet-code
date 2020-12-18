# https://leetcode.com/problems/reverse-linked-list-ii/
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        start_pointer = head
        cur_pointer = head
        prev_pointer = None
        counter = 1

        def inver_list(head, n=1000) -> ListNode:
            prev_pointer = None
            cur_pointer = head
            counter = 0

            while cur_pointer and counter < n:
                tmp_pointer = cur_pointer.next
                cur_pointer.next = prev_pointer
                prev_pointer = cur_pointer
                cur_pointer = tmp_pointer
                counter += 1

            if cur_pointer:
                head.next = cur_pointer

            return prev_pointer

        while cur_pointer and counter < m:
            prev_pointer = cur_pointer
            cur_pointer = cur_pointer.next
            counter += 1

        if m == n:
            return head

        if m == 1:
            return inver_list(head, n)

        if cur_pointer and prev_pointer:
            prev_pointer.next = inver_list(cur_pointer, n - m + 1)

        return start_pointer
