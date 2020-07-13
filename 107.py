# https://leetcode.com/problems/binary-tree-level-order-traversal-ii/

# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        result = []

        def dfs(root, result, h):
            if not root:
                return []

            if len(result) <= h:
                result.append([])

            if root.left:
                result = dfs(root.left, result, h + 1)
            if root.right:
                result = dfs(root.right, result, h + 1)

            result[h].append(root.val)

            return result

        result = dfs(root, [], 0)
        result.reverse()
        return result
