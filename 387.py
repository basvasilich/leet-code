# https://leetcode.com/problems/first-unique-character-in-a-string/

class Solution:
    def firstUniqChar(self, s: str) -> int:
        if len(s) == 0:
            return -1

        if len(s) == 1:
            return 0

        h = {}
        min_index: int = len(s)
        for index, char in enumerate(s):
            if char in h.keys():
                h[char] = (h[char][0], h[char][1] + 1)
            else:
                h[char] = (index, 1)

        for key in h:
            index, val = h[key]
            if val == 1 and index < min_index:
                min_index = index

        return -1 if min_index == len(s) else min_index
