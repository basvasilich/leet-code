# https://leetcode.com/problems/maximum-depth-of-n-ary-tree/

class Solution:
    def maxDepth(self, root: 'Node') -> int:

        if not root:
            return 0

        def dfs(node, h):
            if node.children:
                return max([dfs(node, h + 1) for node in node.children])

            return h

        return dfs(root, 1)
