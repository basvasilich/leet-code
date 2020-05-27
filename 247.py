# https://leetcode.com/problems/strobogrammatic-number-ii/

from typing import List


class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:

        ones = ["1", "8", "0"]
        twos = ["11", "69", "88", "96", "00"]
        result = set()

        if n == 1:
            return ones

        def helper(n):
            tmp = set()
            if n == 1:
                return ones
            if n == 2:
                return twos

            for num in helper(n - 2):
                for two in twos:
                    tmp.add(two[0] + num + two[1])

            return tmp

        for num in helper(n):
            if num[0] != "0":
                result.add(num)

        return result
