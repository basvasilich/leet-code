# https://leetcode.com/problems/pascals-triangle/

from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = []
        for r in range(numRows):
            result.append([1] * (r + 1))
            for i in range(r + 1):
                if 1 < r != i and i != 0:
                    result[r][i] = result[r - 1][i] + result[r - 1][i - 1]
        return result
