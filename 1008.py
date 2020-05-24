# https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/

# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        root = TreeNode(preorder[0])

        if len(preorder) < 2:
            return root

        def add_node(root, val):
            if val > root.val:
                if not root.right:
                    root.right = TreeNode(val)
                else:
                    add_node(root.right, val)
            else:
                if not root.left:
                    root.left = TreeNode(val)
                else:
                    add_node(root.left, val)

        for index in range(1, len(preorder)):
            add_node(root, preorder[index])

        return root
