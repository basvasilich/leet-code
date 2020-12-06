# https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/

# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        def step(root: 'Node', prev_root: 'Node', is_left: bool):

            if not root:
                pass
            elif prev_root is None:
                root.next = None
            else:
                print(root.val, prev_root.val)
                if is_left and prev_root.right:
                    root.next = prev_root.right
                elif prev_root.next:
                    check_root = prev_root.next
                    while check_root.next and not check_root.left and not check_root.right:
                        check_root = check_root.next
                    if check_root.left:
                        root.next = check_root.left
                    elif check_root.right:
                        root.next = check_root.right
                    else:
                        root.next = None
                else:
                    root.next = None

            if root and root.right:
                step(root.right, root, False)
            if root and root.left:
                step(root.left, root, True)

        step(root, None, True)

        return root
