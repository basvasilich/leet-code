# https://leetcode.com/problems/isomorphic-strings/

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if s == t: return True

        def makeH(s):
            h = {}
            for index, char in enumerate(s):
                if char in h.keys():
                    h[char].append(index)
                else:
                    h[char] = [index]
            return sorted(h.values())

        i = makeH(s)
        j = makeH(t)
        return i == j
