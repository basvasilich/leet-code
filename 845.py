# https://leetcode.com/problems/longest-mountain-in-array/
from typing import List


class Solution:
    def longestMountain(self, A: List[int]) -> int:
        result = 0
        if len(A) < 3:
            return 0

        for i in range(1, len(A) - 1):
            num = A[i]
            prev_num = A[i - 1]
            next_num = A[i + 1]

            if prev_num < num > next_num:
                next_result = 1
                top_l = i - 1
                top_r = i + 1

                while top_l >= 0 and A[top_l] < A[top_l + 1]:
                    next_result += 1
                    top_l -= 1

                while top_r < len(A) and A[top_r] < A[top_r - 1]:
                    next_result += 1
                    top_r += 1

                result = max(result, next_result)
        return result

