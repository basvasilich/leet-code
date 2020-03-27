# https://leetcode.com/problems/move-zeroes/

from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) < 2:
            pass

        read_pointer = 0
        write_pointer = 0

        while read_pointer < len(nums):
            if nums[read_pointer] != 0:
                nums[write_pointer] = nums[read_pointer]
                if write_pointer != read_pointer:
                    nums[read_pointer] = 0
                write_pointer += 1
            read_pointer += 1
