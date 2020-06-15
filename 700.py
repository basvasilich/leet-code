# https://leetcode.com/problems/search-in-a-binary-search-tree/


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        def helper(root: TreeNode, val: int) -> TreeNode:
            if not root or root.val == val:
                return root
            elif root.val > val:
                return helper(root.left, val)
            else:
                return helper(root.right, val)
        return helper(root, val)