# https://leetcode.com/problems/find-pivot-index/

from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        if len(nums) == 0: return -1
        sums = [[None, None] for _ in range(len(nums))]
        sums[0] = [nums[0], None]
        sums[-1] = [None, nums[-1]]
        reverse_index = None
        index = None
        for i in range(1, len(nums)):
            sums[i][0] = sums[i - 1][0] + nums[i]
            sums[len(nums) - 1 - i][1] = sums[len(nums) - i][1] + nums[len(nums) - 1 - i]

            if sums[i][0] == sums[i][1] and index == None:
                index = i

            if sums[len(nums) - 1 - i][0] == sums[len(nums) - 1 - i][1]:
                reverse_index = len(nums) - 1 - i

        if reverse_index != None and index != None:
            return min(reverse_index, index)
        elif index != None:
            return index
        elif reverse_index != None:
            return reverse_index
        else:
            return -1
