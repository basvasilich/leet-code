# https://leetcode.com/problems/island-perimeter/


from typing import List


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        result = 0

        def dfs(i, j, result):
            if grid[i][j] == 1:
                grid[i][j] = 2

                if i == 0:
                    result += 1
                if i == len(grid) - 1:
                    result += 1
                if j == 0:
                    result += 1
                if j == len(grid[0]) - 1:
                    result += 1

                if i > 0:
                    if grid[i - 1][j] == 0:
                        result += 1
                    else:
                        result = dfs(i - 1, j, result)

                if j < len(grid[0]) - 1:
                    if grid[i][j + 1] == 0:
                        result += 1
                    else:
                        result = dfs(i, j + 1, result)

                if j > 0:
                    if grid[i][j - 1] == 0:
                        result += 1
                    else:
                        result = dfs(i, j - 1, result)

                if i < len(grid) - 1:
                    if grid[i + 1][j] == 0:
                        result += 1
                    else:
                        result = dfs(i + 1, j, result)

            return result

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    result = dfs(i, j, 0)
                    break;
        return result
