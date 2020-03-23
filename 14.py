# https://leetcode.com/problems/longest-common-prefix/
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        if len(strs) == 1: return strs[0]
        if len(strs) == 0: return ""
        prefix = ""

        for str in strs:
            if len(str) == 0: return prefix

        for i in range(len(strs[0])):
            char = strs[0][i]
            flag = True
            for str in strs:
                if i >= len(str) or str[i] != char:
                    flag = False
                    break

            if flag:
                prefix += char

            else:
                return prefix

        return prefix
