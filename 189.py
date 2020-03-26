# https://leetcode.com/problems/rotate-array

from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        if k == 0 or len(nums) == 0 or len(nums) == 1:
            pass

        if k > len(nums):
            k = k % len(nums)

        def reverse_part(i, j):
            for m in range((j - i) // 2 + 1):
                nums[i + m], nums[j - m] = nums[j - m], nums[i + m]

        reverse_part(0, len(nums) - 1)
        reverse_part(0, k - 1)
        reverse_part(k, len(nums) - 1)
