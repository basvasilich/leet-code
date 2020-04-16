# https://leetcode.com/problems/rotting-oranges/

from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        h_1 = set()
        h_2 = {0: set()}
        minutes = 0

        def get_connections(item):
            i, j = item
            conn = []
            if i - 1 >= 0 and grid[i - 1][j] > 0:
                conn.append((i - 1, j))
            if j - 1 >= 0 and grid[i][j - 1] > 0:
                conn.append((i, j - 1))
            if i + 1 < len(grid) and grid[i + 1][j] > 0:
                conn.append((i + 1, j))
            if j + 1 < len(grid[0]) and grid[i][j + 1] > 0:
                conn.append((i, j + 1))
            return conn

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    h_1.add((i, j))
                    if len(get_connections((i, j))) == 0:
                        return -1
                elif grid[i][j] == 2:
                    h_2[0].add((i, j))

        if len(h_1) == 0:
            return minutes

        while True:
            if minutes not in h_2.keys() or len(h_2[minutes]) == 0:
                return -1
            for item in h_2[minutes]:
                item_conn = get_connections(item)
                for conn in item_conn:
                    i, j = conn
                    if (i, j) in h_1:
                        if minutes + 1 in h_2.keys():
                            h_2[minutes + 1].add((i, j))
                        else:
                            h_2[minutes + 1] = set()
                            h_2[minutes + 1].add((i, j))

                        if (i, j) in h_1:
                            h_1.remove((i, j))

            h_2.pop(minutes, None)

            if len(h_1) > 0:
                minutes += 1
            else:
                return minutes + 1
