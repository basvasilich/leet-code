# https://leetcode.com/problems/daily-temperatures/
from typing import List


class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        stack = [T[0]]
        h = {T[0]: [0]}
        result = [0] * len(T)

        for index in range(1, len(T)):
            t = T[index]

            if t > stack[-1] and len(stack) != 0:
                while len(stack) != 0 and t > stack[-1]:
                    index_prev_t = h[stack.pop()].pop()
                    result[index_prev_t] = index - index_prev_t
            stack.append(t)
            if t in h.keys():
                h[t].append(index)
            else:
                h[t] = [index]

        return result
