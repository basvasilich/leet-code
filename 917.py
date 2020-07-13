# https://leetcode.com/problems/reverse-only-letters/

import re


class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        pointer_l = 0
        pointer_r = len(S) - 1
        result = ''

        while pointer_l <= len(S):
            l = S[pointer_l] if pointer_l < len(S) else ""
            r = S[pointer_r] if pointer_r >= 0 else ""

            if not re.match(r"[a-zA-Z]", l):
                result += l
                pointer_l += 1
            elif not re.match(r"[a-zA-Z]", r):
                pointer_r -= 1
            else:
                result += r
                pointer_r -= 1
                pointer_l += 1

        return result
