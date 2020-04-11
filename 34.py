# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        result = [None, None]

        if len(nums) == 0: return [-1, -1]
        if len(nums) == 1 and nums[0] == target: return [0, 0]
        if len(nums) == 1 and nums[0] != target: return [-1, -1]
        if target not in nums:
            return [-1, -1]

        def helper(i, j):
            if i == j and nums[i] == target:
                if result[0] is None or i < result[0]:
                    result[0] = i
                if result[1] is None or i > result[1]:
                    result[1] = i
            elif i > j:
                pass
            elif i < j:
                mid = i + ((j - i) // 2)
                helper(i, mid)
                helper(mid + 1, j)

        helper(0, len(nums) - 1)

        if result == [None, None]:
            return [-1, -1]

        return result

