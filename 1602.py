from queue import SimpleQueue


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findNearestRightNode(self, root: TreeNode, u: TreeNode) -> TreeNode:
        def bfs(root, u):
            q = SimpleQueue()
            q.put((root, 0))
            while not q.empty():
                item, l = q.get()
                if not item:
                    return None
                elif item.val == u.val and q.empty():
                    return None
                elif item.val == u.val:
                    next_item, next_l = q.get()
                    return next_item if next_l == l else None

                if item.left:
                    q.put((item.left, l + 1))

                if item.right:
                    q.put((item.right, l + 1))

            return None

        return bfs(root, u)
