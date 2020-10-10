# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        head_pointer = head
        if not head:
            return head_pointer
        if not head.next:
            return head_pointer

        cur_pointer = head
        while cur_pointer and cur_pointer.next:
            while cur_pointer and cur_pointer.next and cur_pointer.val == cur_pointer.next.val:
                cur_pointer.next = cur_pointer.next.next

            cur_pointer = cur_pointer.next
        return head_pointer