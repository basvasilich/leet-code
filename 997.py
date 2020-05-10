# https://leetcode.com/problems/find-the-town-judge/

from typing import List


class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        trust_no_one = set(range(1, N + 1))
        trust_adj = {}
        all_sum = N * (N + 1) / 2

        if len(trust) == 0 and N == 1: return 1

        for t_from, t_to in trust:
            if t_from in trust_no_one:
                trust_no_one.remove(t_from)

            if t_to in trust_adj.keys():
                trust_adj[t_to] += t_from
            else:
                trust_adj[t_to] = t_from

        for i in trust_no_one:
            if i in trust_adj.keys() and trust_adj[i] == all_sum - i:
                return i

        return -1
