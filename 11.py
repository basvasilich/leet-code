# https://leetcode.com/problems/container-with-most-water/

class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_h = max(height)
        max_area = 0
        pointer_1 = 0
        pointer_2 = len(height) - 1
        flag = True

        def check_max_area(i, j, max_area):
            if i < 0 or j > len(height) - 1 or i > j:
                return max_area
            return max(max_area, (j - i) * min(height[j], height[i]))

        while max_h * (pointer_2 - pointer_1) > max_area and pointer_2 != pointer_1:
            max_area = check_max_area(pointer_1, pointer_2, max_area)
            if height[pointer_2] < height[pointer_1]:
                pointer_2 -= 1
            else:
                pointer_1 += 1

        return max_area

