# https://leetcode.com/problems/remove-element/

from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if len(nums) == 0:
            return 0

        slow_pointer = 0

        for num in nums:
            if num != val:
                nums[slow_pointer] = num
                slow_pointer += 1
        return slow_pointer
