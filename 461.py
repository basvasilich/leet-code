# https://leetcode.com/problems/hamming-distance/

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        b_str1 = "{0:b}".format(x)[::-1]
        b_str2 = "{0:b}".format(y)[::-1]
        result = 0
        max_len = max(len(b_str1), len(b_str2))
        for i in range(max_len):
            if i >= len(b_str1):
                char_1 = '0'
                char_2 = b_str2[i]
            elif i >= len(b_str2):
                char_2 = '0'
                char_1 = b_str1[i]
            else:
                char_1 = b_str1[i]
                char_2 = b_str2[i]
            if char_1 != char_2:
                result += 1

        return result
