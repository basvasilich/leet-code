# https://leetcode.com/problems/course-schedule-ii/

from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        if len(prerequisites) == 0:
            return list(range(numCourses))

        h = {}
        not_visited = set(range(numCourses))
        result = []

        for course in range(numCourses):
            h[course] = set()

        for pair in prerequisites:
            course, prereq = pair
            h[course].add(prereq)

        while len(h.keys()) > 0:
            visited = set()
            for course in h.keys():
                h[course] = h[course].intersection(not_visited)

                if len(h[course]) == 0:
                    not_visited.remove(course)
                    visited.add(course)
                    result.append(course)

            if len(visited) == 0:
                return []

            for course in visited:
                h.pop(course, None)

        return [] if len(not_visited) > 0 else result
