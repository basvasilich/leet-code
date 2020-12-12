# https://leetcode.com/problems/string-compression/
from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        prev_char = chars[0]
        input_index = 0
        counter = 1
        result_str = ""

        if len(chars) <= 1:
            return len(chars)

        def add_record(prev_char, counter, input_index):
            chars[input_index] = prev_char
            input_index += 1
            if counter > 1:
                for digit in str(counter):
                    chars[input_index] = digit
                    input_index += 1
            return input_index

        for index in range(1, len(chars)):
            char = chars[index]
            if prev_char == char:
                counter += 1
            else:
                input_index = add_record(prev_char, counter, input_index)
                prev_char = char
                counter = 1

        input_index = add_record(prev_char, counter, input_index)

        return input_index
