# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prices_len = len(prices)
        if not prices_len: return 0

        results = [0] * prices_len
        min_p = prices[0]

        for i in range(1, prices_len):
            price = prices[i]

            if prices[i] < min_p: min_p = price

            results[i] = max(results[i - 1], price - min_p, 0)

        return results[-1]