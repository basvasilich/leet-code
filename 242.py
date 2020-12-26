# https://leetcode.com/problems/valid-anagram/


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) == 0 or len(t) == 0:
            return True

        def make_table(s: str) -> dict:
            result = {}
            for char in s:
                if char in result.keys():
                    result[char] += 1
                else:
                    result[char] = 1

            return result

        table_s = make_table(s)
        table_t = make_table(t)

        if table_t.keys() != table_s.keys():
            return False

        for key in table_t.keys():
            if key not in table_s.keys() or table_t[key] != table_s[key]:
                return False

        return True
