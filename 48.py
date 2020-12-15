# https://leetcode.com/problems/rotate-image/

from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        level = 0

        def make_step(n, level):
            if level >= n - level - 1:
                return

            for _ in range(n - level * 2 - 1):
                col = level
                row = level
                tmp = matrix[row][col]
                while col < n - level - 1:
                    matrix[row][col + 1], tmp = tmp, matrix[row][col + 1]
                    col += 1
                while row < n - level - 1:
                    matrix[row + 1][col], tmp = tmp, matrix[row + 1][col]
                    row += 1
                while col > level:
                    matrix[row][col - 1], tmp = tmp, matrix[row][col - 1]
                    col -= 1
                while row > level:
                    matrix[row - 1][col], tmp = tmp, matrix[row - 1][col]
                    row -= 1

        while level < n - 1:
            make_step(n, level)
            level += 1
        print(matrix)
