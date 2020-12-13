# https://leetcode.com/problems/minimum-knight-moves/

from collections import deque
from math import copysign


class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        step_number = 0
        q = deque()
        visited = set()
        q.append((0, 0, 0))

        if abs(x) == 1 and abs(y) == 1:
            return 2

        while q:
            step, xf, yf = q.popleft()

            visited.add((xf, yf))

            if xf == x and yf == y:
                return step

            for dx, dy in [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]:
                if (xf + dx, yf + dy) not in visited and copysign(1, x) == copysign(1, xf + dx) and copysign(1,
                                                                                                             y) == copysign(
                    1, yf + dy):
                    q.append((step + 1, xf + dx, yf + dy))
                    visited.add((xf + dx, yf + dy))

        return step_number
