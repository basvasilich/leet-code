# https://leetcode.com/problems/max-consecutive-ones/
from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:

        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]

        slow_pointer = 0
        max_count = 0

        for fast_pointer in range(len(nums)):
            if nums[fast_pointer] == 1:
                slow_pointer += 1
            else:
                max_count = max(slow_pointer, max_count)
                slow_pointer = 0

        return max(slow_pointer, max_count)
