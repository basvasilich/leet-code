# https://leetcode.com/problems/add-binary/

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result = ""
        prev_one = False
        for i in range(max(len(a), len(b))):
            if i >= len(a):
                a_c = '0'
                b_c = b[-1 - i]
            elif i >= len(b):
                a_c = a[-1 - i]
                b_c = '0'
            else:
                b_c = b[-1 - i]
                a_c = a[-1 - i]

            if prev_one and ((a_c == '1' and b_c == '0') or (a_c == '0' and b_c == '1')):
                result = '0' + result
                prev_one = True
            elif prev_one and (a_c == '0' and b_c == '0'):
                result = '1' + result
                prev_one = False
            elif prev_one and (a_c == '1' and b_c == '1'):
                result = '1' + result
                prev_one = True
            elif (a_c == '1' and b_c == '0') or (a_c == '0' and b_c == '1'):
                result = '1' + result
                prev_one = False
            elif a_c == '0' and b_c == '0':
                result = '0' + result
                prev_one = False
            elif a_c == '1' and b_c == '1':
                result = '0' + result
                prev_one = True

        if prev_one:
            result = '1' + result

        return result
