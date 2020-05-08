# https://leetcode.com/problems/ugly-number-ii/

from heapq import heappop, heappush


class Solution:
    def nthUglyNumber(self, n: int) -> int:
        h = []
        d = set()

        heappush(h, 1)
        count = 0
        next_num = 1
        while count < n:
            next_num = heappop(h)
            heappush(h, next_num * 2)
            heappush(h, next_num * 3)
            heappush(h, next_num * 5)
            d.add(next_num)
            while h[0] in d and len(h) > 0:
                heappop(h)
            count += 1

        return next_num
