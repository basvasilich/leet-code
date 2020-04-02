# https://leetcode.com/problems/happy-number/


class Solution:
    def isHappy(self, n: int) -> bool:
        if -1 < n < 2: return True

        h = set()

        def squareByInt(num):
            result = 0
            arr = [int(d) for d in str(num)]

            for val in arr:
                result += val ** 2

            if result in h:
                return False
            elif result == 1:
                return True
            else:
                h.add(result)
                return squareByInt(result)

        return squareByInt(n)
