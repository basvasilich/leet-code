# https://leetcode.com/problems/can-place-flowers/
from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        pointer = 0

        if len(flowerbed) == 1 and n == 1:
            if flowerbed[0] == 0:
                return True
            else:
                return False

        while pointer < len(flowerbed) and n > 0:
            cur_position = flowerbed[pointer]

            if pointer >= len(flowerbed) - 1:
                next_position = 0
            else:
                next_position = flowerbed[pointer + 1]

            if pointer <= 0:
                last_position = 0
            else:
                last_position = flowerbed[pointer - 1]

            if last_position == next_position == cur_position == 0:
                flowerbed[pointer] = 1
                n -= 1
                pointer += 2
            else:
                pointer += 1

        return n <= 0
