# https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/

class Solution:
    def removeDuplicates(self, S: str) -> str:
        s = []
        for char in S:
            if len(s) and s[-1] == char:
                s.pop()
            else:
                s.append(char)

        return "".join(s)
