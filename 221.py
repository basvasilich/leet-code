# https://leetcode.com/problems/maximal-square/
from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        d = [[0] * len(matrix[0]) for _ in range(len(matrix))]
        max_s = 0

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == "1":
                    if i > 0 and j > 0:
                        d[i][j] = min(d[i - 1][j], d[i][j - 1], d[i - 1][j - 1]) + 1

                    else:
                        d[i][j] = 1

                    if d[i][j] > max_s:
                        max_s = d[i][j]
                else:
                    d[i][j] = 0

        return max_s * max_s
