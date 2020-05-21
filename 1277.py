# https://leetcode.com/problems/count-square-submatrices-with-all-ones/

from typing import List


class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])

        d = [[0] * n for _ in range(m)]

        count = 0

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 1:
                    if i == 0 or j == 0:
                        d[i][j] = 1
                    else:
                        d[i][j] = min(d[i - 1][j], d[i][j - 1], d[i - 1][j - 1]) + 1

                    count += d[i][j]

        return count

