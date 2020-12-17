# https://leetcode.com/problems/decode-string/
import string


class Solution:
    def decodeString(self, s: str) -> str:
        def helper(s: str) -> str:
            stack = []
            result = ""
            open_count = 0
            close_count = 0
            first_open_index = 0
            for index, char in enumerate(s):
                if char in string.ascii_lowercase and len(stack) == 0:
                    result += char
                elif char == "[":
                    if open_count == 0:
                        first_open_index = index
                    open_count += 1
                    stack.append(char)
                elif char == "]" and open_count - close_count == 1:
                    close_count += 1
                    start_m_index = first_open_index - 1

                    while s[start_m_index].isdigit() and start_m_index > 0:
                        start_m_index -= 1

                    if s[start_m_index].isdigit():
                        mult = int(s[:first_open_index])
                    else:
                        mult = int(s[start_m_index + 1:first_open_index])

                    result += helper(s[first_open_index + 1:index]) * mult
                    open_count = 0
                    close_count = 0
                    stack = []
                elif char == "]":
                    close_count += 1
                    stack.append(char)
                else:
                    stack.append(char)

            return result

        return helper(s)
