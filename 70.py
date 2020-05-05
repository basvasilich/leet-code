# https://leetcode.com/problems/climbing-stairs/

class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 3:
            return n

        d = [0] * (n + 1)
        counter = 0
        while counter < n - 1:
            d[counter + 1] += d[counter] + 1
            d[counter + 2] += d[counter]
            counter += 1

        return d[n - 1] + 1
