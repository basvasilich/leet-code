# https://leetcode.com/problems/robot-return-to-origin/

class Solution:
    def judgeCircle(self, moves: str) -> bool:
        h = 0
        v = 0

        for move in moves:
            if move == 'U':
                h += 1
            elif move == 'D':
                h -= 1
            elif move == 'L':
                v += 1
            else:
                v -= 1

        return h == 0 and v == 0
