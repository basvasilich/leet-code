# https://leetcode.com/problems/find-all-duplicates-in-an-array/
from typing import List


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        if len(nums) == 1:
            return []

        result = []
        for index in range(0, len(nums)):
            val = 0
            item = nums[index]

            if item < 0:
                val = abs(item)
            else:
                val = item

            if nums[val - 1] < 0:
                result.append(val)
            else:
                nums[val - 1] = -1 * nums[val - 1]

        return result
