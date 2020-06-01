# https://leetcode.com/problems/invert-binary-tree/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        def helper(node):
            left = None
            right = None
            if not node:
                return node

            if node.left:
                right = helper(node.left)
            if node.right:
                left = helper(node.right)

            node.left = left
            node.right = right

            return node

        return helper(root)
