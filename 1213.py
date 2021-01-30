# https://leetcode.com/problems/intersection-of-three-sorted-arrays/
from typing import List


class Solution:
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        pointer_1 = 0
        pointer_2 = 0
        pointer_3 = 0

        if arr1[-1] < arr2[0] or arr2[-1] < arr3[0] or arr1[-1] < arr3[0] or arr3[-1] < arr2[0] or arr3[-1] < arr1[0]:
            return []
        result = []

        while pointer_1 < len(arr1) and pointer_2 < len(arr2) and pointer_3 < len(arr3):
            if arr1[pointer_1] == arr2[pointer_2] == arr3[pointer_3]:
                result.append(arr1[pointer_1])
                pointer_1 += 1
                pointer_2 += 1
                pointer_3 += 1
            else:
                if arr1[pointer_1] < arr2[pointer_2] or arr1[pointer_1] < arr3[pointer_3]:
                    pointer_1 += 1
                elif arr2[pointer_2] < arr3[pointer_3] or arr2[pointer_2] < arr1[pointer_1]:
                    pointer_2 += 1
                elif arr3[pointer_3] < arr2[pointer_2] or arr3[pointer_3] < arr1[pointer_1]:
                    pointer_3 += 1

        return result
