# https://leetcode.com/problems/implement-strstr/


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        if len(needle) == 0: return 0
        if len(haystack) == 0 or len(needle) > len(haystack): return -1

        pointer_1 = 0
        pointer_2 = 0
        tmp = -1
        while pointer_1 < len(haystack):
            if haystack[pointer_1] == needle[pointer_2]:
                if tmp == -1: tmp = pointer_1
                pointer_2 += 1
                if pointer_2 == len(needle):
                    return tmp
            elif tmp != -1:
                pointer_1 = tmp
                pointer_2 = 0
                tmp = -1

            pointer_1 += 1

            if len(haystack) - pointer_1 < len(needle) - pointer_2: return -1

        return tmp
