# https://leetcode.com/problems/arranging-coins/


class Solution:
    def arrangeCoins(self, n: int) -> int:

        if n < 2:
            return n

        def get_sum(n):
            return (n * (n + 1)) / 2

        m = n // 2

        if m > 1:
            while get_sum(m) > n:
                m = m // 2

        if get_sum(m) == n:
            return m

        while get_sum(m) < n:
            m += 1

        if get_sum(m) == n:
            return m

        return m - 1
