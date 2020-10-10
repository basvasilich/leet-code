# https://leetcode.com/problems/binary-tree-postorder-traversal/
# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:

        if not root:
            return []

        def dfs(root: TreeNode, result):
            if root.left:
                result = dfs(root.left, result)
            if root.right:
                result = dfs(root.right, result)
            if root.val:
                result.append(root.val)

            return result

        return dfs(root, [])