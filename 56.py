# https://leetcode.com/problems/merge-intervals/
from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        if len(intervals) < 2: return intervals

        points = []
        for interval in intervals:
            start, end = interval
            points.append((start, 's'))
            points.append((end, 'e'))

        points.sort(key=lambda item: item[0])

        result = []
        first_s_point = points[0][0]
        counter_s = 1
        counter_e = 0
        for i in range(1, len(points)):
            value, point_type = points[i]

            if point_type == 'e':
                counter_e += 1
                last_e_point = value

                if (i == len(points) - 1) or (counter_e == counter_s and points[i + 1][0] != value):
                    result.append([first_s_point, last_e_point])
                    counter_e = 0
                    counter_s = 0
                    first_s_point = -1

            elif first_s_point == -1:
                first_s_point = value
                counter_s += 1
            else:
                counter_s += 1

        return result