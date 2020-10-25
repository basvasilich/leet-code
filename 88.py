# https://leetcode.com/problems/merge-sorted-array/

from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        if n == 0:
            return

        pointer_1 = m - 1
        pointer_2 = n - 1
        pointer = len(nums1) - 1

        while pointer >= 0:
            if pointer_2 < 0:
                nums1[pointer] = nums1[pointer_1]
                pointer_1 -= 1
            elif pointer_1 < 0:
                nums1[pointer] = nums2[pointer_2]
                pointer_2 -= 1
            else:
                num_1 = nums1[pointer_1]
                num_2 = nums2[pointer_2]

                if num_1 >= num_2:
                    nums1[pointer] = num_1
                    pointer_1 -= 1
                else:
                    nums1[pointer] = num_2
                    pointer_2 -= 1
            pointer -= 1

        return
