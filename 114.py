# https://leetcode.com/problems/flatten-binary-tree-to-linked-list/
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        def dfs(root: TreeNode):
            if not root or (not root.left and not root.right):
                return root, root

            if not root.left:
                right_pointer_s, right_pointer_e = dfs(root.right)
                root.right = right_pointer_s
                root.left = None
                return root, right_pointer_e
            elif not root.right:
                left_pointer_s, left_pointer_e = dfs(root.left)
                root.right = left_pointer_s
                root.left = None
                return root, left_pointer_e
            else:
                right_pointer_s, right_pointer_e = dfs(root.right)
                left_pointer_s, left_pointer_e = dfs(root.left)
                left_pointer_e.right = right_pointer_s
                root.right = left_pointer_s
                root.left = None
                return root, right_pointer_e

        dfs(root)
