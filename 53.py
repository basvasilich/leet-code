# https://leetcode.com/problems/maximum-subarray/
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        result = nums[0]
        prev = nums[0]

        for i in range(1, len(nums)):
            prev = max(prev + nums[i], nums[i])
            result = max(result, prev)

        return result
