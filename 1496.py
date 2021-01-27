# https://leetcode.com/problems/path-crossing/

class Solution:
    def isPathCrossing(self, path: str) -> bool:
        x = 0
        y = 0
        points = set()
        points.add((0, 0))
        for delta in path:
            if delta == 'N':
                y += 1
            elif delta == 'S':
                y -= 1
            elif delta == 'E':
                x += 1
            elif delta == 'W':
                x -= 1

            if (x, y) in points:
                return True

            points.add((x, y))

        return False
