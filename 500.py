# https://leetcode.com/problems/keyboard-row

from typing import List


class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        h = {}

        for char in 'QWERTYUIOPqwertyuiop':
            h[char] = 1
        for char in 'ASDFGHJKLasdfghjkl':
            h[char] = 2
        for char in 'ZXCVBNMzxcvbnm':
            h[char] = 3

        result = []

        for word in words:
            row = -1
            flag = True
            for index, char in enumerate(word):
                if index == 0:
                    row = h[char]
                elif h[char] != row:
                    flag = False
                    break

            if flag:
                result.append(word)

        return result
