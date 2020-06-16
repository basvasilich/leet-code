# https://leetcode.com/problems/sort-colors/

from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        pointer_0 = 0
        pointer_2 = len(nums) - 1
        pointer_l = 0
        pointer_r = len(nums) - 1

        def swap(pointer_l, pointer_r):
            if nums[pointer_l] != nums[pointer_r]:
                nums[pointer_l], nums[pointer_r] = nums[pointer_r], nums[pointer_l]

        if len(nums) == 1:
            pass
        elif l == 2 and nums[0] < nums[1]:
            pass
        elif l == 2 and nums[0] > nums[1]:
            swap(0, 1)
        else:
            while pointer_l < pointer_r:
                if nums[pointer_0] == 0:
                    pointer_0 += 1
                    pointer_l = pointer_0
                elif nums[pointer_2] == 2:
                    pointer_2 -= 1
                    pointer_r = pointer_2
                elif nums[pointer_r] == 0:
                    swap(pointer_r, pointer_0)
                elif nums[pointer_r] == 2:
                    swap(pointer_r, pointer_2)
                elif nums[pointer_l] == 0:
                    swap(pointer_l, pointer_0)
                elif nums[pointer_l] == 2:
                    swap(pointer_l, pointer_2)
                elif nums[pointer_l] == 1:
                    pointer_l += 1
                elif nums[pointer_r] == 1:
                    pointer_r -= 1
