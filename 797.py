# https://leetcode.com/problems/all-paths-from-source-to-target/

from typing import List


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        result = []

        def dfs(index, path):
            if index == len(graph) - 1:
                result.append([int(x) for x in path.split(' ')])
            else:
                for node in graph[index]:
                    dfs(node, path + ' ' + str(node))

        dfs(0, '0')
        return result
