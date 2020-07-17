# https://leetcode.com/problems/same-tree/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        def dfsPreOrder(root, result):
            if root:
                result.append(root.val)
            else:
                result.append(None)
                return result

            if root.left:
                dfsPreOrder(root.left, result)
            else:
                result.append(None)

            if root.right:
                dfsPreOrder(root.right, result)
            else:
                result.append(None)

            return result

        return dfsPreOrder(p, []) == dfsPreOrder(q, [])
