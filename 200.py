# https://leetcode.com/problems/number-of-islands/

from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count_island = 0

        if len(grid) == 0 or len(grid[0]) == 0:
            return count_island

        def paint_neighbor(i, j):
            grid[i][j] = 0
            if i + 1 < len(grid) and grid[i + 1][j] == "1":
                paint_neighbor(i + 1, j)

            if j + 1 < len(grid[0]) and grid[i][j + 1] == "1":
                paint_neighbor(i, j + 1)

            if i - 1 >= 0 and grid[i - 1][j] == "1":
                paint_neighbor(i - 1, j)

            if j - 1 >= 0 and grid[i][j - 1] == "1":
                paint_neighbor(i, j - 1)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    count_island += 1
                    paint_neighbor(i, j)

        return count_island
