# https://leetcode.com/problems/binary-tree-preorder-traversal/
# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        def dfs(root: TreeNode, result: List[int]) -> List[int]:
            if not root:
                return result

            result.append(root.val)
            result = dfs(root.left, result)
            result = dfs(root.right, result)

            return result

        return dfs(root, [])