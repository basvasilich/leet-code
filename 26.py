# https://leetcode.com/problems/remove-duplicates-from-sorted-array/
from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) < 2: return len(nums)
        read_pointer = 0
        write_pointer = 1

        while read_pointer < len(nums):
            if nums[read_pointer] != nums[write_pointer - 1]:
                nums[write_pointer] = nums[read_pointer]
                write_pointer += 1

            read_pointer += 1
        return write_pointer
