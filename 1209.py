# https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/

class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []

        for char in s:
            if len(stack) == 0:
                stack.append((char, 1))
            else:
                last_char, last_count = stack[-1]

                if char == last_char:
                    last_count += 1

                    if last_count >= k:
                        stack.pop()
                    else:
                        stack[-1] = (last_char, last_count)
                else:
                    stack.append((char, 1))

        result = ""

        for char, l in stack:
            result += char * l

        return result
