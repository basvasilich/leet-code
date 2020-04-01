# https://leetcode.com/problems/k-closest-points-to-origin/

from typing import List
from heapq import heappush, heappop


class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        if len(points) < 2: return points

        h = []
        result = []

        def dist(point):
            x, y = point
            return (x ** 2 + y ** 2) ** 0.5

        for point in points:
            heappush(h, (dist(point), point))

        for i in range(K):
            result.append(heappop(h)[1])

        return result