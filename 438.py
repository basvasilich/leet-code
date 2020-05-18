# https://leetcode.com/problems/find-all-anagrams-in-a-string/

import string
from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s) or len(p) == 0 or len(s) == 0:
            return []

        result = []
        char_h = {}

        for i, c in enumerate(string.ascii_lowercase):
            char_h[c] = (i + 1) ** 3

        p_h = sum([char_h[c] for c in p])

        last_h = sum([char_h[c] for c in s[:len(p)]])

        if last_h == p_h:
            result.append(0)

        for i in range(1, len(s) - len(p) + 1):
            h = last_h + char_h[s[i + len(p) - 1]] - char_h[s[i - 1]]
            if h == p_h:
                result.append(i)
            last_h = h

        return result
