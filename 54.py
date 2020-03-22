# https://leetcode.com/problems/spiral-matrix/
from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if len(matrix) == 0: return []
        if len(matrix) == 1 and len(matrix[0]) == 1: return [matrix[0][0]]
        result = []

        def round(i_s, i_e, j_s, j_e):
            if i_s > i_e or j_s > j_e:
                return []
            elif i_s == i_e and j_s == j_e:
                return [matrix[i_s][j_s]]
            elif i_e - i_s == 1 and j_e - j_s == 1:
                return [matrix[i_s][j_s], matrix[i_s][j_e], matrix[i_e][j_e], matrix[i_e][j_s]]
            else:
                result = []
                for j in range(j_s, j_e + 1):
                    result.append(matrix[i_s][j])

                if i_s < i_e:
                    for i in range(i_s + 1, i_e + 1):
                        result.append(matrix[i][j_e])
                    for j in range(j_e - 1, j_s - 1, -1):
                        result.append(matrix[i_e][j])

                if j_s < j_e:
                    for i in range(i_e - 1, i_s, -1):
                        result.append(matrix[i][j_s])

                return result

        for d in range(max(len(matrix[0]) - 1, len(matrix) - 1)):
            result += round(d, len(matrix) - 1 - d, d, len(matrix[0]) - 1 - d)
        return result
