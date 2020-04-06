# https://leetcode.com/problems/group-shifted-strings/

from typing import List


class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:

        if len(strings) == 0: return strings

        if len(strings) == 1: return [strings]

        letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                   'u', 'v', 'w', 'x', 'y', 'z']
        h_letters = {}
        for index, char in enumerate(letters):
            h_letters[char] = index

        def h_fn(s):
            if len(s) == 1:
                return '-1'
            result = ''
            for i in range(len(s) - 1):
                char_l = s[i]
                char_r = s[i + 1]
                index_l = h_letters[char_l]
                index_r = h_letters[char_r]
                if index_r >= index_l:
                    result += str(index_r - index_l) + '|'
                else:
                    result += str(len(letters) - index_l + index_r) + '|'
            return result

        h_result = {}

        for s in strings:
            key = h_fn(s)
            if key in h_result.keys():
                h_result[key].append(s)
            else:
                h_result[key] = [s]

        return list(h_result.values())
