# https://leetcode.com/problems/check-if-it-is-a-straight-line/
from typing import List


class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        x0, y0 = coordinates[0]
        x1, y1 = coordinates[1]
        a = x1 - x0
        b = y1 - y0

        def checkFn(x, y):
            return a * (y - y0) - b * (x - x0) == 0

        for i in range(2, len(coordinates)):
            if not checkFn(*coordinates[i]):
                return False

        return True