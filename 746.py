# https://leetcode.com/problems/min-cost-climbing-stairs/

from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        d = [float("inf")] * (len(cost) + 2)
        d[0] = 0
        d[1] = 0

        for i in range(len(cost)):
            d[i + 1] = min(d[i + 1], d[i] + cost[i])
            d[i + 2] = min(d[i + 2], d[i] + cost[i])

        return int(min(d[len(cost)], d[len(cost) + 1]))
