# https://leetcode.com/problems/search-in-rotated-sorted-array/
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:

        if len(nums) == 1:
            if nums[0] == target:
                return 0
            else:
                return -1

        def find_shift():
            for i in range(len(nums) - 1):
                if nums[i] > nums[i + 1]:
                    return i
            return i + 1

        def bs(start, end, target):
            if start > end or start < 0 or end >= len(nums):
                return -1
            elif start == end and nums[start] == target:
                return start
            elif start == end:
                return -1
            else:
                mid = start + (end - start) // 2

                if nums[mid] == target:
                    return mid
                elif nums[mid] >= target:
                    return bs(start, mid, target)
                else:
                    return bs(mid + 1, end, target)

        shift = find_shift()

        if target < nums[0]:
            return bs(shift + 1, len(nums) - 1, target)
        else:
            return bs(0, shift, target)


