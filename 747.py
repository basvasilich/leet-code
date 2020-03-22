# https://leetcode.com/problems/largest-number-at-least-twice-of-others/

from typing import List


class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        if len(nums) == 1: return 0

        max_1 = (-1, -1)
        max_2 = (-1, -1)
        for i, num in enumerate(nums):
            if num > max_1[0]:
                max_2 = max_1
                max_1 = (num, i)
            elif num > max_2[0]:
                max_2 = (num, i)

        return max_1[1] if max_1[0] // 2 >= max_2[0] else -1
