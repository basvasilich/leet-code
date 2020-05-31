# https://leetcode.com/problems/student-attendance-record-i/


class Solution:
    def checkRecord(self, s: str) -> bool:
        a_count = 0
        l_count = 0

        for char in s:
            if char == "A":
                a_count += 1
                if a_count >= 2:
                    return False
                l_count = 0
            elif char == "L":
                l_count += 1
                if l_count >= 3:
                    return False
            else:
                l_count = 0

        return True
