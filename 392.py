# https://leetcode.com/problems/is-subsequence/


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True
        if len(t) == 0:
            return False
        h_s = set(s)
        h_t = {}

        for index, char in enumerate(t):
            if char in h_s:
                if char in h_t.keys():
                    h_t[char][1].append(index)
                else:
                    h_t[char] = (0, [index])

        cur_index = -1
        for index, char in enumerate(s):
            if char not in h_t.keys():
                return False
            else:
                char_pointer, char_positions = h_t[char]
                flag = True
                for i in range(char_pointer, len(char_positions)):
                    if char_positions[i] > cur_index:
                        cur_index = char_positions[i]
                        if i == len(char_positions) - 1:
                            h_t.pop(char, None)
                        else:
                            h_t[char] = (i, char_positions)
                        flag = False
                        break
                if flag:
                    return False

        return True
