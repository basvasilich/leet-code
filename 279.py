# https://leetcode.com/problems/perfect-squares/


class Solution:
    def numSquares(self, n: int) -> int:
        squares = []

        for i in range(1, int(n ** 0.5 + 1)):
            if i ** 2 <= n:
                squares.append(i ** 2)
            else:
                break

        d = [n + 1] * (n + 1)
        d[0] = 0

        for i in range(0, n + 1):
            for square in squares:
                if square > i:
                    break
                else:
                    d[i] = min(d[i - square] + 1, d[i])
        return d[n]
