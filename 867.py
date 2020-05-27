# https://leetcode.com/problems/transpose-matrix/

from typing import List


class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        result = [[0] * len(A) for _ in range(len(A[0]))]
        for i in range(len(A)):
            for j in range(len(A[0])):
                if i == j:
                    result[i][j] = A[i][j]
                else:
                    result[j][i] = A[i][j]
        return result
