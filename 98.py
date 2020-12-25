# https://leetcode.com/problems/validate-binary-search-tree/
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        inorder = []

        def in_order(root, result):
            if not root:
                return result
            elif root.left and root.right:
                result = in_order(root.left, result)
                result.append(root.val)
                result = in_order(root.right, result)
                return result
            elif root.left:
                result = in_order(root.left, result)
                result.append(root.val)
                return result
            elif root.right:
                result.append(root.val)
                result = in_order(root.right, result)
                return result
            else:
                result.append(root.val)
                return result

        inorder = in_order(root, [])

        if len(inorder) == 1:
            return True

        prev = inorder[0]
        for index in range(1, len(inorder)):
            if inorder[index] <= prev:
                return False
            prev = inorder[index]

        return True

