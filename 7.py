# https://leetcode.com/problems/reverse-integer/


class Solution:
    def reverse(self, x: int) -> int:

        if x < 0:
            result_s = '-'
        else:
            result_s = ''

        s = str(x)

        for i in range(len(s) - 1, -1, -1):
            if s[i] != 0 and s[i] != '-':
                result_s += s[i]

        result = int(result_s)

        if result < -1 * (2 ** 31) or result > 2 ** 31 - 1:
            return 0

        return result

