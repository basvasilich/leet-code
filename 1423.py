# https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/
from typing import List


class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        sum_of_array = sum(cardPoints)

        if k == 1 and len(cardPoints) > 1:
            return max(cardPoints[0], cardPoints[-1])

        if k == 1:
            return cardPoints[0]

        if k >= len(cardPoints):
            return sum_of_array

        len_window = len(cardPoints) - k
        sum_of_window = sum(cardPoints[:len_window])
        result = sum_of_window

        for i in range(0, k):
            sum_of_window = sum_of_window - cardPoints[i] + cardPoints[len_window + i]
            result = min(sum_of_window, result)

        return sum_of_array - result
