# https://leetcode.com/problems/minimum-area-rectangle/

from typing import List


class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        result = float("Inf")
        h_2 = {}

        def make_pairs(_arr):
            arr = sorted(_arr)
            result = []
            for i in range(len(arr)):
                for j in range(i + 1, len(arr)):
                    result.append((arr[i], arr[j]))
            return result

        h_1 = {}

        for x, y in points:
            if x in h_1.keys():
                h_1[x].append(y)
            else:
                h_1[x] = [y]

        for x in sorted(h_1.keys()):
            pairs = make_pairs(h_1[x])
            for pair in pairs:

                if pair[1] > pair[0]:
                    if pair in h_2.keys() and x != h_2[pair]:
                        result = min(result, abs(pair[1] - pair[0]) * abs(h_2[pair] - x))
                        h_2[pair] = x
                    else:
                        h_2[pair] = x

        return result if result != float("Inf") else 0
