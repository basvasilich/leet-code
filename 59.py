# https://leetcode.com/problems/spiral-matrix-ii/

from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        # prepare result
        result = [[0 for _ in range(n)] for _ in range(n)]

        def recursive_helper(current_n: int, coord_offset: int, value_offset: int):
            if current_n == 0:
                pass
            elif current_n == 1:
                result[coord_offset][coord_offset] = value_offset + 1
            else:
                for col in range(current_n):
                    value_offset += 1
                    result[coord_offset][coord_offset + col] = value_offset

                for row in range(1, current_n):
                    value_offset += 1
                    result[coord_offset + row][n - coord_offset - 1] = value_offset

                for col in range(1, current_n):
                    value_offset += 1
                    result[n - coord_offset - 1][n - coord_offset - 1 - col] = value_offset

                for row in range(1, current_n - 1):
                    value_offset += 1
                    result[n - coord_offset - 1 - row][coord_offset] = value_offset

                recursive_helper(current_n - 2, coord_offset + 1, value_offset)

        recursive_helper(n, 0, 0)
        return result
