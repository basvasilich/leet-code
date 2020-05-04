# https://leetcode.com/problems/complement-of-base-10-integer/

class Solution:
    def bitwiseComplement(self, N: int) -> int:
        binary_str = "{0:b}".format(N)
        reversed_str = ""

        for char in binary_str:
            reversed_str += ("0" if char == "1" else "1")

        return int(reversed_str, 2)
