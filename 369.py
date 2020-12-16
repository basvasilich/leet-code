# https://leetcode.com/problems/plus-one-linked-list/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def plusOne(self, head: ListNode) -> ListNode:

        if not head:
            pass

        if head and head.val == 0 and not head.next:
            head.val += 1
            return head

        def reverce_list(head):
            pointer_prev = None
            pointer_cur = head

            while pointer_cur:
                tmp_pointer = pointer_cur.next
                pointer_cur.next = pointer_prev
                pointer_prev = pointer_cur
                pointer_cur = tmp_pointer

            return pointer_prev

        reversed_list_cur = reverce_list(head)

        if reversed_list_cur.val < 9:
            reversed_list_cur.val += 1
            return reverce_list(reversed_list_cur)
        else:
            tmp_pointer = reversed_list_cur
            while reversed_list_cur.next and reversed_list_cur.val == 9:
                reversed_list_cur.val = 0
                reversed_list_cur = reversed_list_cur.next

            if reversed_list_cur.next:
                reversed_list_cur.val += 1
            elif reversed_list_cur.val < 9:
                reversed_list_cur.val += 1
            else:
                reversed_list_cur.val = 0
                reversed_list_cur.next = ListNode(val=1)

            return reverce_list(tmp_pointer)

