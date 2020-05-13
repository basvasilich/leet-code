# https://leetcode.com/problems/remove-k-digits/

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        s = []
        count = k

        if len(num) <= k: return "0"

        for index, n in enumerate(num):
            if len(s) > 0 and int(s[-1]) > int(n) and count > 0:
                while len(s) > 0 and int(s[-1]) > int(n) and count > 0:
                    s.pop()
                    count -= 1
                s.append(n)
            elif index == 0 or count == 0:
                s.append(n)
            elif index + count >= len(num):
                count -= 1
            elif int(s[-1]) <= int(n):
                s.append(n)

        return "".join(s).lstrip('0') or "0"
