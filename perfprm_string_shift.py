from typing import List


class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        if len(s) == 1: return s

        count = 0
        for sh in shift:
            d, val = sh
            if d == 1:
                count += val
            else:
                count -= val

        if abs(count) > len(s):
            if count > 0:
                count = abs(count) % len(s)
            else:
                count = -1 * (abs(count) % len(s))
        if count == 0:
            return s

        print(count)

        if count > 0:
            return s[-count:] + s[:len(s) - count]
        else:
            return s[-1 * count:] + s[:-1 * count]
