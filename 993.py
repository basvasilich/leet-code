# https://leetcode.com/problems/cousins-in-binary-tree/


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        d = {}

        def helper(root: TreeNode, x: int, y: int, h: int):

            def check(root, x, y, h):
                if root.val == x:
                    d[x] = (root.val, h + 1)

                if root.val == y:
                    d[y] = (root.val, h + 1)

                helper(root, x, y, h + 1)

            if root.left:
                check(root.left, x, y, h)

            if root.right:
                check(root.right, x, y, h)

        helper(root, x, y, 0)

        if x not in d.keys() or y not in d.keys():
            return False

        return d[x][0] != d[y][0] and d[x][1] == d[y][1]
