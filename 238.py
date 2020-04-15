# https://leetcode.com/problems/product-of-array-except-self/

from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1]

        product = 1

        for i in range(1, len(nums)):
            product *= nums[i - 1]
            result.append(product)
        product = 1

        for j in range(len(nums) - 2, -1, -1):
            product *= nums[j + 1]
            result[j] *= product

        return result
