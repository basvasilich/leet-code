# https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/

from collections import Counter
from typing import List


class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        result = 0
        chars_c = Counter(chars)

        for word in words:
            h = {}
            flag = True
            for char in word:
                if char not in chars_c.keys():
                    flag = False
                    break
                elif char in h.keys() and chars_c[char] < h[char] + 1:
                    flag = False
                    break
                elif char in h.keys():
                    h[char] += 1
                elif char not in h.keys():
                    h[char] = 1
            if flag:
                result += len(word)

        return result
