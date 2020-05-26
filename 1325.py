# https://leetcode.com/problems/delete-leaves-with-a-given-value/

# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def removeLeafNodes(self, root: TreeNode, target: int) -> TreeNode:

        def helper(root, target):
            left = None
            right = None

            if root and root.left:
                left = helper(root.left, target)

            if root and root.right:
                right = helper(root.right, target)

            if root and root.val != target:
                return TreeNode(root.val, left=left, right=right)

            if root and root.val == target and (left or right):
                return TreeNode(root.val, left=left, right=right)

            return None

        return helper(root, target)
