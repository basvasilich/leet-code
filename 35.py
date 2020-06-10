# https://leetcode.com/problems/search-insert-position/


from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            if target > nums[0]:
                return 1
            else:
                return 0

        def helper(l, r, t):
            if l > r:
                return -1
            elif l == r and ((nums[l] == t) or (l == 0 and nums[l] > t)):
                return l
            elif (l == len(nums) - 1 and nums[l] < t) or (l < len(nums) - 1 and nums[l] < t and nums[l + 1] > t):
                return l + 1
            elif l < r:
                mid = l + (r - l) // 2
                r_r = helper(mid + 1, r, target)
                r_l = helper(l, mid, target)

                if r_r > -1:
                    return r_r
                if r_l > -1:
                    return r_l
                return -1
            else:
                return -1

        return helper(0, len(nums) - 1, target)
