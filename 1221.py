# https://leetcode.com/problems/split-a-string-in-balanced-strings/

class Solution:
    def balancedStringSplit(self, s: str) -> int:
        index = 1
        result = 0
        stack = [s[0]]

        while index < len(s):
            if len(stack) > 0 and stack[len(stack) - 1] != s[index]:
                stack.pop()
                if len(stack) == 0:
                    result += 1
            else:
                stack.append(s[index])

            index += 1

        return result
