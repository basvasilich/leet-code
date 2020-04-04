# https://leetcode.com/problems/intersection-of-two-arrays-ii/
from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:

        if nums1 == nums2:
            return nums1

        if len(nums1) == 0 or len(nums2) == 0:
            return []

        h1 = {}
        h2 = {}
        result = []

        for num in nums1:
            if num in h1.keys():
                h1[num] += 1
            else:
                h1[num] = 1

        for num in nums2:
            if num not in h1.keys():
                h1.pop(num, None)
            elif num in h2.keys():
                h2[num] += 1
            else:
                h2[num] = 1

        for num in h1:
            if num in h1.keys() and num in h2.keys():
                count = min(h1[num], h2[num])
                while count > 0:
                    result.append(num)
                    count -= 1
        return result
