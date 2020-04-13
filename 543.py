# https://leetcode.com/problems/diameter-of-binary-tree/


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 0

        self.result = 0

        def helper(node):
            if node is None:
                return 0
            r = helper(node.left)
            l = helper(node.right)
            self.result = max(self.result, r + l + 1)
            return max(l, r) + 1

        helper(root)
        return self.result - 1
