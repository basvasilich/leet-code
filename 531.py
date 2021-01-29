# https://leetcode.com/problems/lonely-pixel-i/
from typing import List


class Solution:
    def findLonelyPixel(self, picture: List[List[str]]) -> int:
        def dfs(row, col, direction) -> bool:
            if row < 0 or col < 0 or row > len(picture) - 1 or col > len(picture[0]) - 1:
                return True
            elif picture[row][col] == 'D' or picture[row][col] == 'B':
                picture[row][col] = 'D'
                return False

            elif direction == 1:
                return dfs(row, col + 1, direction)
            elif direction == 2:
                return dfs(row, col - 1, direction)
            elif direction == 3:
                return dfs(row + 1, col, direction)
            elif direction == 4:
                return dfs(row - 1, col, direction)

            return True

        def check(row, col) -> bool:
            return dfs(row, col + 1, 1) and dfs(row + 1, col, 3) and dfs(row, col - 1, 2) and dfs(row - 1, col, 4)

        result = 0
        for row in range(len(picture)):
            for col in range(len(picture[0])):
                if picture[row][col] == 'B' and check(row, col):
                    result += 1

        return result
