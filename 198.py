# https://leetcode.com/problems/house-robber/

from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if 0 < len(nums) < 3:
            return max(nums)

        m = 0
        d = [0] * len(nums)
        for i in range(len(nums)):
            if i < 2:
                d[i] = nums[i]
            elif i == 2:
                d[i] = nums[i] + nums[0]
            else:
                d[i] = nums[i] + max(d[i - 2], d[i - 3])

            if d[i] > m:
                m = d[i]

        return m
