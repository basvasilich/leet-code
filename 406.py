# https://leetcode.com/problems/queue-reconstruction-by-height/

from typing import List


class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        result = []
        sorted_people = sorted(people, key=lambda x: (-x[0], x[1]))

        for item in sorted_people:
            result.insert(item[1], item)

        return result
