# https://leetcode.com/problems/top-k-frequent-elements/

from collections import Counter
from heapq import heappush, heappop
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        h = []
        result = []

        for key in c.keys():
            heappush(h, (-1 * c[key], key))

        while k > 0 and len(h) > 0:
            value, key = heappop(h)
            result.append(key)
            k -= 1

        return result
