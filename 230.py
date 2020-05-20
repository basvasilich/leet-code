# https://leetcode.com/problems/kth-smallest-element-in-a-bst/


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        def order_helper(root, result, count):
            if not root:
                return result, count

            if root.left and count < k:
                result, count = order_helper(root.left, result, count)

            if count < k:
                result = root.val
                count += 1

            if root.right and count < k:
                result, count = order_helper(root.right, result, count)

            return result, count

        return order_helper(root, None, 0)[0]
