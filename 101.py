# https://leetcode.com/problems/symmetric-tree/
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def dfs(root: TreeNode, result: list, invert: bool):

            if not root:
                result.append(None)
                return result
            else:
                if invert:
                    result = dfs(root.right, result, invert)
                    result.append(root.val)
                    result = dfs(root.left, result, invert)
                    result.append('|')
                else:
                    result = dfs(root.left, result, invert)
                    result.append(root.val)
                    result = dfs(root.right, result, invert)
                    result.append('|')

                return result

        if not root:
            return True
        elif root and not root.left and not root.right:
            return True
        elif root.left and root.right:
            result_l = dfs(root.left, [], False)
            result_r = dfs(root.right, [], True)

            if len(result_l) != len(result_r):
                return False
            else:
                for index in range(len(result_l)):
                    if result_l[index] != result_r[index]:
                        return False
                return True
        else:
            return False
