# https://leetcode.com/problems/max-area-of-island/

from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m = 0
        if len(grid) == 0 or len(grid[0]) == 0: return 0
        if len(grid) == len(grid[0]) == 1: return grid[0][0]

        def check_iland(i, j, a):
            grid[i][j] = 0

            if i > 0 and grid[i - 1][j] == 1:
                a = check_iland(i - 1, j, a + 1)
            if j > 0 and grid[i][j - 1] == 1:
                a = check_iland(i, j - 1, a + 1)
            if i < len(grid) - 1 and grid[i + 1][j] == 1:
                a = check_iland(i + 1, j, a + 1)
            if j < len(grid[0]) - 1 and grid[i][j + 1] == 1:
                a = check_iland(i, j + 1, a + 1)

            return a

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    m = max(m, check_iland(i, j, 1))

        return m
