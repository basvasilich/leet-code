# https://leetcode.com/problems/increasing-order-search-tree/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        def dsf_helper(root: TreeNode, tmp_arr):
            if not root.left and not root.right:
                tmp_arr.append(root)
                return tmp_arr

            if root.left:
                tmp_arr = dsf_helper(root.left, tmp_arr)

            tmp_arr.append(root)

            if root.right:
                tmp_arr = dsf_helper(root.right, tmp_arr)

            return tmp_arr

        tmp_arr = dsf_helper(root, [])
        for index in range(len(tmp_arr) - 1):
            node = tmp_arr[index]
            next_node = tmp_arr[index + 1]
            next_node.left = None
            node.left = None
            node.right = next_node

        return tmp_arr[0] if len(tmp_arr) else []
