# https://leetcode.com/problems/course-schedule/

from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        if len(prerequisites) == 0 or numCourses == 1:
            return True

        pre = {}
        remaining_courses = set(range(numCourses))

        for course in range(numCourses):
            pre[course] = set()

        done_courses = set()

        for pair in prerequisites:
            course, prereq = pair
            pre[course].add(prereq)

        while len(done_courses) < numCourses:
            tmp_done_courses = set()
            for course in pre.keys():
                pre[course] = pre[course].intersection(remaining_courses)

                if len(pre[course]) == 0:
                    remaining_courses.remove(course)
                    tmp_done_courses.add(course)
                    done_courses.add(course)

            if len(tmp_done_courses) == 0:
                break
            else:
                for course in tmp_done_courses:
                    pre.pop(course, None)

        return len(done_courses) == numCourses
