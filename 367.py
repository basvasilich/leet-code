# https://leetcode.com/problems/valid-perfect-square/

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        x = num

        while x ** 2 > num:
            x = x // 3

        while x ** 2 < num:
            x += 1

        return (x ** 2) == num
