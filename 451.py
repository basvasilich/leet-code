#  https://leetcode.com/problems/sort-characters-by-frequency/

class Solution:
    def frequencySort(self, s: str) -> str:
        if len(s) < 2: return s

        h = {}
        result = ""
        for char in s:
            if char in h.keys():
                h[char] = (h[char][0] + 1, char)
            else:
                h[char] = (1, char)

        values_sorted = sorted(h.values(), key=lambda item: item[0], reverse=True)

        for value in values_sorted:
            char, num = value
            result += char * num

        return result
