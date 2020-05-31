# https://leetcode.com/problems/edit-distance/


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        d = [[0] * (len(word2) + 1) for _ in range(len(word1) + 1)]

        for j in range(len(word2) + 1):
            d[0][j] = j

        for i in range(len(word1) + 1):
            d[i][0] = i

        for j in range(1, len(word2) + 1):
            for i in range(1, len(word1) + 1):
                if i > 0 and j > 0:
                    insertion = d[i][j - 1] + 1
                    deletion = d[i - 1][j] + 1
                    mismatch = d[i - 1][j - 1] + 1
                    match = d[i - 1][j - 1]

                    if word1[i - 1] == word2[j - 1]:
                        d[i][j] = min(insertion, deletion, match)
                    else:
                        d[i][j] = min(insertion, deletion, mismatch)

        return d[len(word1)][len(word2)]
