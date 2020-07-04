# https://leetcode.com/problems/leaf-similar-trees/
# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:

        def dfs(root, result: List[int]) -> List[int]:
            if not root.left and not root.right:
                result.append(root.val)
                return result
            if root.left:
                result = dfs(root.left, result)
            if root.right:
                result = dfs(root.right, result)

            return result

        return dfs(root1, []) == dfs(root2, [])