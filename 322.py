# https://leetcode.com/problems/coin-change/

from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0: return 0

        h = [amount + 1] * (amount + 1)
        h[0] = 0

        for i in range(1, amount + 1):
            for coin in coins:
                if i - coin >= 0:
                    h[i] = min(h[i - coin] + 1, h[i])

        return h[amount] if 0 < h[amount] < amount + 1 else -1
