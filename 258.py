# https://leetcode.com/problems/add-digits/

class Solution:
    def addDigits(self, num: int) -> int:
        step = sum([int(x) for x in str(num)])
        if step < 10:
            return step
        else:
            return self.addDigits(step)
