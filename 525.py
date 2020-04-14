# https://leetcode.com/problems/contiguous-array/
from typing import List


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:

        h = {0: -1}
        m_l = 0
        count = 0
        for index, num in enumerate(nums):
            if num == 1:
                count += 1
            else:
                count -= 1
            if count in h.keys():
                m_l = max(m_l, index - h[count])
            else:
                h[count] = index

        return m_l
