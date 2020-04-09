# https://leetcode.com/problems/backspace-string-compare/
class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        if S == T: return True
        s_r = []
        t_r = []
        i = 0

        while i < len(S) or i < len(T):
            if i < len(S) and S[i] != '#':
                s_r.append(S[i])
            if i < len(T) and T[i] != '#':
                t_r.append(T[i])
            if i < len(S) and S[i] == '#' and len(s_r) > 0:
                s_r.pop()
            if i < len(T) and T[i] == '#' and len(t_r) > 0:
                t_r.pop()

            i += 1

        return s_r == t_r
