# https://leetcode.com/problems/find-duplicate-subtrees/

from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:

        if root is None: return [root]
        h = set()
        result_h = set()
        result = []

        def hash_tree(root):
            key = ''
            if root.val is not None:
                key += 'v' + str(root.val) + 'v'
            if root.left is not None:
                key += 'l' + hash_tree(root.left) + 'l'
            if root.right is not None:
                key += 'r' + hash_tree(root.right) + 'r'

            if key in h and key not in result_h:
                result.append(root)
                result_h.add(key)
            else:
                h.add(key)
            return key

        hash_tree(root)

        return result
