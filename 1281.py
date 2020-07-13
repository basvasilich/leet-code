# https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/


class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        n_str = str(n)
        product = 1
        s = 0
        for char in n_str:
            num = int(char)
            product *= num
            s += num

        return product - s
