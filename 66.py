# https://leetcode.com/problems/plus-one/
from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[0] == 0: return [1]
        num = 0
        for i in range(len(digits)):
            num += digits[i] * (10 ** (len(digits) - i - 1))
        num += 1
        return [int(d) for d in str(num)]
