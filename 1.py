# https://leetcode.com/problems/two-sum
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        targets = {}
        for i, num in enumerate(nums):
            if target - num not in targets.keys():
                targets[num] = i
            else:
                return [targets[target - num], i]