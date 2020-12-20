# https://leetcode.com/problems/add-two-numbers-ii/
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        def helper(head):
            prev = None
            cur = head
            while cur:
                tmp = cur.next
                cur.next = prev
                prev = cur
                cur = tmp
            return prev

        def add_vals(val1, val2, plus_one, cur_result):
            val = val1 + val2 + (1 if plus_one else 0)
            if val >= 10:
                plus_one = True
                val = val % 10
            else:
                plus_one = False

            cur_result.next = ListNode(val)
            cur_result = cur_result.next
            return val, plus_one, cur_result

        l1_rev = helper(l1)
        l2_rev = helper(l2)
        cur_l1 = l1_rev
        cur_l2 = l2_rev
        val = cur_l1.val + cur_l2.val
        if val >= 10:
            prev_plus_one = True
            val = val % 10
        else:
            prev_plus_one = False
        cur_result = ListNode(val)
        result_head = cur_result

        cur_l1 = cur_l1.next
        cur_l2 = cur_l2.next
        while cur_l1 or cur_l2:
            if cur_l1 and cur_l2:
                val, prev_plus_one, cur_result = add_vals(cur_l1.val, cur_l2.val, prev_plus_one, cur_result)
                cur_l1 = cur_l1.next
                cur_l2 = cur_l2.next
            elif cur_l1:
                val, prev_plus_one, cur_result = add_vals(cur_l1.val, 0, prev_plus_one, cur_result)
                cur_l1 = cur_l1.next
            elif cur_l2:
                val, prev_plus_one, cur_result = add_vals(0, cur_l2.val, prev_plus_one, cur_result)
                cur_l2 = cur_l2.next
        if prev_plus_one:
            cur_result.next = ListNode(1)
            cur_result = cur_result.next
        return helper(result_head)
