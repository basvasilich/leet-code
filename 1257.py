# https://leetcode.com/problems/smallest-common-region/

from typing import List


class Solution:
    def findSmallestRegion(self, regions: List[List[str]], region1: str, region2: str) -> str:
        h = {}
        path1 = set()
        path2 = set()

        for region in regions:
            parent = region[0]
            for children in region[1:]:
                h[children] = parent

        parent1 = h[region1]
        parent2 = h[region2]
        path1.add(region1)
        path1.add(parent1)
        path2.add(region2)
        path2.add(parent2)

        while parent1 in h.keys() or parent2 in h.keys():
            if parent1 in path2:
                return parent1
            elif parent2 in path1:
                return parent2
            elif parent1 == parent2:
                return parent1
            elif parent1 in h.keys():
                parent1 = h[parent1]
                path1.add(parent1)
            else:
                parent2 = h[parent2]
                path2.add(parent2)

        if parent1 == parent2:
            return parent1

        return parent1
