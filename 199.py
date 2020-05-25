# https://leetcode.com/problems/binary-tree-right-side-view/


# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        h_list = []
        h_val = 0

        def helper(root, h_val):
            if root:
                if len(h_list) <= h_val:
                    h_list.append(-1)

                h_list[h_val] = root.val

                if root.left:
                    helper(root.left, h_val + 1)

                if root.right:
                    helper(root.right, h_val + 1)

        helper(root, h_val)

        return h_list
