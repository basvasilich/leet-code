# https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l1_curr = l1
        l2_curr = l2
        cur_node = None
        result = None
        need_add_1 = False
        while l1_curr is not None or l2_curr is not None:
            if l1_curr is None:
                sum = l2_curr.val
            elif l2_curr is None:
                sum = l1_curr.val
            else:
                sum = l1_curr.val + l2_curr.val

            if need_add_1:
                sum += 1
                need_add_1 = False

            if sum > 9:
                need_add_1 = True
                sum = sum % 10

            if cur_node is not None:
                cur_node.next = ListNode(sum)
                cur_node = cur_node.next
            else:
                cur_node = ListNode(sum)
                result = cur_node

            if l1_curr is not None: l1_curr = l1_curr.next
            if l2_curr is not None: l2_curr = l2_curr.next

        if need_add_1: cur_node.next = ListNode(1)
        return result