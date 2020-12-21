# https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/
from typing import List


class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:

        if len(weights) == 1:
            return weights[0]

        if D == 1:
            return sum(weights)

        max_capacity = max(weights)

        def check_if_possible(w: List[int], D: int, C: int) -> bool:
            pointer = len(w) - 1
            while D > 0 and pointer >= 0:
                capacity = C
                while capacity > 0 and pointer >= 0:
                    item = w[pointer]
                    if capacity - item >= 0:
                        pointer -= 1
                        capacity -= item
                    else:
                        break;
                D -= 1

            if pointer >= 0:
                return False
            else:
                return True

        def helper(s, e):
            if s == e:
                return s
            else:
                mid = s + (e - s) // 2

                if check_if_possible(weights, D, mid):
                    return helper(s, mid)
                else:
                    return helper(mid + 1, e)

        return helper(max_capacity, max_capacity * 100)
