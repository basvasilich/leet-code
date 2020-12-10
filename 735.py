# https://leetcode.com/problems/asteroid-collision/

from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        asteroids_pointer = 0

        def put_on_stack(item, stack):
            if len(stack) == 0 or stack[-1] < 0:
                stack.append(item)
                return stack
            elif stack[-1] > 0 > item and stack[-1] == -1 * item:
                return stack[:-1]
            elif stack[-1] > 0 > item:
                stack_item = stack.pop()
                return put_on_stack(item if -1 * item > stack_item else stack_item, stack)
            else:
                stack.append(item)
                return stack

        while asteroids_pointer < len(asteroids):
            stack = put_on_stack(asteroids[asteroids_pointer], stack)
            asteroids_pointer += 1

        return stack