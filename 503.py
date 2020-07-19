# https://leetcode.com/problems/next-greater-element-ii/

from typing import List

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = []
        result = [-1] * len(nums)
        nums_s = nums + nums
        for index, val in enumerate(nums_s):
            if len(stack) == 0 or stack[-1][0] >= val:
                stack.append((val, index))
            else:
                while len(stack) > 0 and stack[-1][0] < val:
                    last_val, last_index = stack.pop()
                    result[last_index % len(nums)] = val
                stack.append((val, index))

        return result
