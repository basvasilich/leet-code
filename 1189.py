# https://leetcode.com/problems/maximum-number-of-balloons/

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        if len(text) < 6:
            return 0

        h = {"b": 0, "a": 0, "l": 0, "o": 0, "n": 0}
        result = 0

        for char in text:
            if char in h.keys():
                h[char] += 1

        h["l"] = h["l"] // 2
        h["o"] = h["o"] // 2

        return min(h.values())

