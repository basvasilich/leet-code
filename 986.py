# https://leetcode.com/problems/interval-list-intersections/

from typing import List


class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        points = []

        if len(A) == 0 or len(B) == 0: return []

        for a in A:
            s, e = a
            points.append((s, 's', 'a'))
            points.append((e, 'e', 'a'))
        for b in B:
            s, e = b
            points.append((s, 's', 'b'))
            points.append((e, 'e', 'b'))

        points.sort(key=lambda x: x[0])

        result = []
        last_s = -1
        open_a = False
        open_b = False
        for index, point in enumerate(points):
            val, t, a = point

            if t == 's':
                last_s = val
                if a == 'a':
                    open_a = True
                else:
                    open_b = True
            elif t == 'e' and open_a and open_b and last_s != -1:
                result.append([last_s, val])
                last_s = -1
                if a == 'a':
                    open_a = False
                else:
                    open_b = False
            elif t == 'e' and index + 1 < len(points) and points[index + 1][1] == 's' and points[index + 1][0] == val:
                result.append([val, val])
                last_s = -1
                if a == 'a':
                    open_a = False
                else:
                    open_b = False
            elif t == 'e':
                if a == 'a':
                    open_a = False
                else:
                    open_b = False

        return result
