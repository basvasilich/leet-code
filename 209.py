# https://leetcode.com/problems/minimum-size-subarray-sum/
from typing import List


class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:

        if len(nums) == 0:
            return 0
        if len(nums) == 1 and nums[0] >= s:
            return 1

        slow_pointer = 0
        fast_pointer = 0
        cur_sum = 0
        is_sum_exists = False
        min_count = len(nums)

        while fast_pointer < len(nums) - 1 or slow_pointer < len(nums) - 1:
            if cur_sum < s and fast_pointer < len(nums):
                cur_sum += nums[fast_pointer]
                fast_pointer += 1
            else:
                if cur_sum >= s:
                    is_sum_exists = True
                    min_count = min(min_count, fast_pointer - slow_pointer)
                cur_sum -= nums[slow_pointer]
                slow_pointer += 1

        return min_count if is_sum_exists else 0
