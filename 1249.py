# https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses


class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        for index, char in enumerate(list(s)):
            if char == '(':
                stack.append((char, index))
            elif char == ')' and len(stack) > 0 and stack[-1][0] == '(':
                stack.pop()
            elif char == ')':
                stack.append((char, index))

        if len(stack) > 0:
            result = ''
            to_remove = stack.pop()
            for index in range(len(s) - 1, -1, -1):
                if to_remove[1] != index:
                    result = s[index] + result
                elif len(stack) > 0:
                    to_remove = stack.pop()
                else:
                    result = s[0: index] + result
                    return result
            return result
        return s
