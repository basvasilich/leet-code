# https://leetcode.com/problems/group-anagrams/
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        h = {}
        result = []

        def make_key(s):
            return ''.join(sorted(s))

        for item in strs:
            key = make_key(item)
            if make_key(item) in h.keys():
                h[make_key(item)].append(item)
            else:
                h[make_key(item)] = [item]

        for key in h:
            result.append(h[key])

        return result
