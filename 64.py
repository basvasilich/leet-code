# https://leetcode.com/problems/minimum-path-sum/
from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        d = [[0] * len(grid[0]) for _ in range(len(grid))]

        d[0][0] = grid[0][0]

        for row in range(len(grid)):
            for col in range(len(grid[0])):

                if col == 0 and row == 0:
                    pass
                elif row > 0 and col > 0:
                    d[row][col] = min(d[row - 1][col] + grid[row][col], d[row][col - 1] + grid[row][col])
                elif col == 0:
                    d[row][col] = d[row - 1][col] + grid[row][col]
                elif row == 0:
                    d[row][col] = d[row][col - 1] + grid[row][col]

        return d[-1][-1]
