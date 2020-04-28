# https://leetcode.com/problems/longest-palindromic-substring


class Solution:
    def longestPalindrome(self, s: str) -> str:
        result = ""
        if len(s) == 1: return s

        def check_pali(l, r):
            tmp = ""

            if l == r:
                tmp += s[l]
                l -= 1
                r += 1

            while l >= 0 and r < len(s) and s[l] == s[r]:
                tmp = s[l] + tmp + s[r]
                l -= 1
                r += 1

            return tmp

        for i in range(0, len(s) - 1):
            t1 = check_pali(i, i)
            t2 = check_pali(i, i + 1)

            if len(t1) > len(result):
                result = t1

            if len(t2) > len(result):
                result = t2

        return result
