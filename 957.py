# https://leetcode.com/problems/prison-cells-after-n-days/

from typing import List, Tuple


class Solution:
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        if N == 0:
            return cells

        h = {}
        day = 1

        def get_next_state(state: List[int]) -> Tuple[Tuple[int, ...], List[int]]:
            next_state = [0]
            for i in range(0, len(cells) - 2):
                if (state[i] == 1 and state[i + 2] == 1) or (state[i] == 0 and state[i + 2] == 0):
                    next_state.append(1)
                else:
                    next_state.append(0)

            next_state.append(0)

            return tuple(next_state), next_state

        key, result = get_next_state(cells)
        h[key] = result
        flag = False
        N -= 1
        while N > 0:
            key, next_result = get_next_state(result)
            if key in h and not flag:
                N = N % day
                if N == 0:
                    return result
                flag = True
            else:
                h[key] = next_result
            result = next_result
            N -= 1
            day += 1

        return result