# https://leetcode.com/problems/counting-bits/

from typing import List


class Solution:
    def countBits(self, num: int) -> List[int]:

        if num == 0:
            return [0]

        d = []
        d.append(0)
        d.append(1)

        while len(d) <= num:
            left_d = num - len(d)
            if left_d >= len(d):
                d = d + [x + 1 for x in d]
            else:
                d = d + [x + 1 for x in d[:left_d + 1]]

        return d
