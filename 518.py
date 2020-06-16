# https://leetcode.com/problems/coin-change-2/

from typing import List


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        d = [[0] * (amount + 1) for _ in range(len(coins) + 1)]

        d[0][0] = 1

        for i in range(1, len(coins) + 1):
            for j in range(amount + 1):
                if j == 0:
                    d[i][j] = 1
                else:
                    d[i][j] = d[i - 1][j] + ((d[i][j - coins[i - 1]]) if (j - coins[i - 1]) >= 0 else 0)

        return d[len(coins)][amount]