# https://leetcode.com/problems/short-encoding-of-words/

from typing import List


class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        if len(words) == 1:
            return len(words[0]) + 1

        words_sorted = sorted(set(words), key=len, reverse=True)
        result = len(words_sorted[0]) + 1
        result_str = words_sorted[0] + '#'
        indies = {0}

        for i in range(1, len(words_sorted)):
            word = words_sorted[i]
            index = result_str.find(word)

            if index == -1 or index in indies:
                result += len(word) + 1
                indies.add(len(result_str))
                result_str += word + '#'
            elif index not in indies:
                indies.add(index)
        return result
