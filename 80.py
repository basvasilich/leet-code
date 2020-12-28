# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/

from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        if len(nums) < 3:
            return len(nums)

        prev_num = nums[0]
        num_counter = 1

        read_pointer = 1
        write_pointer = 1

        while read_pointer < len(nums):
            if nums[read_pointer] == prev_num:
                nums[write_pointer] = nums[read_pointer]
                num_counter += 1
            else:
                nums[write_pointer] = nums[read_pointer]
                prev_num = nums[read_pointer]
                num_counter = 1

            if num_counter >= 3:
                read_pointer += 1
            else:
                write_pointer += 1
                read_pointer += 1

        return write_pointer
