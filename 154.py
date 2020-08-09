# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/

from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) < 5:
            return min(nums)

        def binary_search(l, r):
            if l > r:
                return None
            elif l == r and r < len(nums) - 1 and nums[r + 1] < nums[r]:
                return nums[r + 1]
            elif l == r:
                return None
            else:
                mid = l + (r - l) // 2
                r_l = binary_search(l, mid)

                if r_l is not None:
                    return r_l

                r_r = binary_search(mid + 1, r)
                if r_r is not None:
                    return r_r

                return None

        r = binary_search(0, len(nums) - 2)
        return r if r is not None else nums[0]
