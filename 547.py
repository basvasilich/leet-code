#https://leetcode.com/problems/friend-circles/

from typing import List


class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        N = len(M)
        friendship = [-1] * N
        result = set()

        def find_top_friend(i, j):
            if i == j and friendship[i] == -1:
                friendship[i] = j
                return

            if i > j:
                f = j
                t = i
            else:
                f = i
                t = j

            while friendship[f] != f:
                f = friendship[f]

            f_t = friendship[t]
            f_f = friendship[f]

            if f_t != -1 and f_f != -1 and f_f != f_t:
                if f_f > f_t:
                    top_parent = f_t
                    replace_child = f_f
                else:
                    top_parent = f_f
                    replace_child = f_t

                for i, x in enumerate(friendship):
                    if x == replace_child:
                        friendship[i] = top_parent
            elif friendship[t] == -1 or friendship[t] > f:
                friendship[t] = f

        for i in range(N):
            for j in range(i + 1):
                if M[i][j] == 1:
                    find_top_friend(i, j)

        for t in friendship:
            result.add(t)

        return len(result)