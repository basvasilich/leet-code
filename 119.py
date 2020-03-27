# https://leetcode.com/problems/pascals-triangle-ii/

from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0: return [1]
        if rowIndex == 1: return [1, 1]
        result = [1, 1]
        for i in range(2, rowIndex + 1):
            result.append(1)
            for j in range(i, 0, -1):
                if j != 0 and j != i:
                    result[j] = result[j - 1] + result[j]
        return result
