# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        sums = {}
        for i, num in enumerate(numbers):
            j = len(numbers) - i - 1
            num_tail = numbers[j]
            if target - num not in sums.keys():
                sums[target - num] = i
            elif num in sums.keys() and sums[num] != i:
                return [min(sums[num] + 1, i + 1), max(sums[num] + 1, i + 1)]

            if target - num_tail not in sums.keys():
                sums[target - num_tail] = j
            elif numbers[j] in sums.keys() and sums[num_tail] != j:
                return [min(sums[num_tail] + 1, j + 1), max(sums[num_tail] + 1, j + 1)]

        return -1
