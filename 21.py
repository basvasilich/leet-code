# https://leetcode.com/problems/merge-two-sorted-lists/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        result = None
        cur_node = None
        while l1 is not None or l2 is not None:
            val = 0
            if l1 is None:
                val = l2.val
                l2 = l2.next
            elif l2 is None:
                val = l1.val
                l1 = l1.next
            elif l1.val > l2.val:
                val = l2.val
                l2 = l2.next
            else:
                val = l1.val
                l1 = l1.next

            if result is None:
                cur_node = ListNode(val)
                result = cur_node
            else:
                cur_node.next = ListNode(val)
                cur_node = cur_node.next

        return result