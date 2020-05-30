# https://leetcode.com/problems/longest-palindrome

class Solution:
    def longestPalindrome(self, s: str) -> int:
        h = set()

        for char in s:
            if char in h:
                h.remove(char)
            else:
                h.add(char)

        if len(h) < 2:
            return len(s)
        else:
            return len(s) - len(h) + 1
