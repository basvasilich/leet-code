# https://leetcode.com/problems/koko-eating-bananas/

from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        def check_k(k, H):
            for pile in piles:
                if pile <= k:
                    H -= 1
                else:
                    H -= (pile // k) + 1

                if H < 0:
                    return False

            return True

        lo, hi = 1, max(piles)
        while lo < hi:
            mid = (lo + hi) // 2
            if check_k(mid, H):
                hi = mid
            else:
                lo = mid + 1

        return lo
