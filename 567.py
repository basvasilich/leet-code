# https://leetcode.com/problems/permutation-in-string/

import string


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2) or len(s1) == 0 or len(s2) == 0:
            return False

        char_h = {}

        for i, c in enumerate(string.ascii_lowercase):
            char_h[c] = (i + 1) ** 5

        p_h = sum([char_h[c] for c in s1])

        last_h = sum([char_h[c] for c in s2[:len(s1)]])

        if last_h == p_h:
            return True

        for i in range(1, len(s2) - len(s1) + 1):
            h = last_h + char_h[s2[i + len(s1) - 1]] - char_h[s2[i - 1]]
            if h == p_h:
                return True
            last_h = h

        return False