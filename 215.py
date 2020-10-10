# https://leetcode.com/problems/kth-largest-element-in-an-array/

from heapq import heappop, heappush
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        h = []
        result = 0

        for num in nums:
            heappush(h, -1 * num)

        while k > 0:
            result = heappop(h)
            k -= 1

        return -1 * result
