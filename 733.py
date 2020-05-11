# https://leetcode.com/problems/flood-fill/

from typing import List


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:

        def paintAround(sr, sc, newColor):
            oldColor = image[sr][sc]
            image[sr][sc] = newColor

            if sr > 0 and image[sr - 1][sc] == oldColor and image[sr - 1][sc] != newColor:
                paintAround(sr - 1, sc, newColor)
            if sc > 0 and image[sr][sc - 1] == oldColor and image[sr][sc - 1] != newColor:
                paintAround(sr, sc - 1, newColor)
            if sr < len(image) - 1 and image[sr + 1][sc] == oldColor and image[sr + 1][sc] != newColor:
                paintAround(sr + 1, sc, newColor)
            if sc < len(image[0]) - 1 and image[sr][sc + 1] == oldColor and image[sr][sc + 1] != newColor:
                paintAround(sr, sc + 1, newColor)

        paintAround(sr, sc, newColor)

        return image