# https://leetcode.com/problems/jewels-and-stones/

class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        stash = {}
        result = 0

        for s in S:
            if s in stash.keys():
                stash[s] += 1
            else:
                stash[s] = 1

        for j in J:
            if j in stash.keys():
                result += stash[j]

        return result
