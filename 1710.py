# https://leetcode.com/problems/maximum-units-on-a-truck/
from typing import List


class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        sortedBoxTypes = sorted(boxTypes, key=lambda boxType: boxType[1], reverse=True)

        pointer = 0
        totalUnits = 0

        while truckSize > 0 and pointer < len(sortedBoxTypes):
            quantity, units = sortedBoxTypes[pointer]

            if quantity <= truckSize:
                totalUnits += quantity * units
                truckSize -= quantity
                pointer += 1
            else:
                totalUnits += truckSize * units
                truckSize = 0

        return totalUnits
