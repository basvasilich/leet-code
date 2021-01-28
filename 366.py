# https://leetcode.com/problems/find-leaves-of-binary-tree/
# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findLeaves(self, root: TreeNode) -> List[List[int]]:
        result_list = []

        def dps(root: TreeNode, main_root: TreeNode, result: List[int]) -> (TreeNode, List[int], bool):
            if not root:
                return main_root, result, True

            elif not root.right and not root.left:
                result.append(root.val)
                return main_root, result, True

            else:
                if root.left:
                    main_root, result, was_leaf = dps(root.left, main_root, result)
                    if was_leaf:
                        root.left = None
                        was_leaf = False

                if root.right:
                    main_root, result, was_leaf = dps(root.right, main_root, result)
                    if was_leaf:
                        root.right = None
                        was_leaf = False

                return main_root, result, False

        if not root:
            return []

        while root:
            root, result_one_dps, _ = dps(root, root, [])
            result_list.append(result_one_dps)
            if len(result_one_dps) == 1 and root.val == result_one_dps[0]:
                break

        return result_list
