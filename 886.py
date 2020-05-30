# https://leetcode.com/problems/possible-bipartition/
from typing import List


class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        if N == 1:
            return True

        if N > 1 and len(dislikes) == 0:
            return True

        colors = {}
        adj = [[] for _ in range(N + 1)]

        for dislike_from, dislike_to in dislikes:
            adj[dislike_from].append(dislike_to)
            adj[dislike_to].append(dislike_from)

        def helper(root, color='r'):
            if root in colors:
                return colors[root] == color

            colors[root] = color

            return all(helper(node, 'b' if color == 'r' else 'r') for node in adj[root])

        return all(helper(node) for node in range(1, N + 1) if node not in colors)
