# https://leetcode.com/problems/minimum-index-sum-of-two-lists/

from typing import List


class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:

        h1 = {}
        flag = False
        min_index = len(list1) + len(list2)
        min_key = []
        for index, item1 in enumerate(list1):
            if item1 not in h1.keys():
                h1[item1] = index

        for index, item2 in enumerate(list2):
            if item2 in h1.keys():
                if index + h1[item2] == min_index:
                    min_index = index + h1[item2]
                    min_key.append(item2)
                elif index + h1[item2] < min_index:
                    min_index = index + h1[item2]
                    min_key = [item2]
        return min_key
