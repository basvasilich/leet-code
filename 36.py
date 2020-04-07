# https://leetcode.com/problems/valid-sudoku/

from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        h = {"r": [set() for _ in range(9)], "c": [set() for _ in range(9)], "q": [set() for _ in range(9)]}

        def get_q_key(i, j):
            if i < 3 and j < 3:
                return 0
            elif 2 < i < 6 and j < 3:
                return 3
            elif i > 5 and j < 3:
                return 6
            elif i < 3 and 2 < j < 6:
                return 1
            elif i < 3 and j > 5:
                return 2
            elif 2 < i < 6 and 2 < j < 6:
                return 4
            elif 2 < i < 6 and j > 5:
                return 5
            elif i > 5 and 2 < j < 6:
                return 7
            elif i > 5 and j > 5:
                return 8

        for i in range(9):
            for j in range(9):
                if board[i][j] != '.' and (
                        board[i][j] in h["r"][i] or board[i][j] in h["c"][j] or board[i][j] in h["q"][get_q_key(i, j)]):
                    return False
                elif board[i][j] != '.':
                    h["r"][i].add(board[i][j])
                    h["c"][j].add(board[i][j])
                    h["q"][get_q_key(i, j)].add(board[i][j])

        return True