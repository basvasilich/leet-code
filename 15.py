# https://leetcode.com/problems/3sum/

from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result_h = set()

        if len(nums) < 3:
            return []

        nums.sort()

        def two_sum(i):
            pointer_lo = i + 1
            pointer_hi = len(nums) - 1

            num_1 = nums[i]

            if num_1 > 0:
                return

            while pointer_lo < pointer_hi:
                num_2 = nums[pointer_lo]
                num_3 = nums[pointer_hi]
                s = num_1 + num_2 + num_3
                if num_1 + num_2 + num_3 == 0:
                    result_h.add((num_1, num_2, num_3))
                    pointer_lo += 1
                    pointer_hi -= 1
                elif s > 0 or (pointer_hi < len(nums) - 1 and num_3 == nums[pointer_hi + 1]):
                    pointer_hi -= 1
                elif s < 0 or (pointer_lo > i + 1 and num_2 == nums[pointer_lo - 1]):
                    pointer_lo += 1

        pointer_1 = 0
        while pointer_1 < len(nums) - 1:
            if pointer_1 == 0 or nums[pointer_1 - 1] != nums[pointer_1]:
                two_sum(pointer_1)

            pointer_1 += 1

        return [list(i) for i in result_h]
