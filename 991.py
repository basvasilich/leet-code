# https://leetcode.com/problems/broken-calculator/


class Solution(object):
    def brokenCalc(self, x, y):
        counter = 0
        while y > x:
            counter += 1

            if y % 2 == 1:
                y += 1
            else:
                y = int(y / 2)

        return counter + x - y
