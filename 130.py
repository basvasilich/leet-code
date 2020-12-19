# https://leetcode.com/problems/surrounded-regions/

from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        l_r = len(board)
        if l_r == 0:
            return

        l_c = len(board[0])

        if l_c == 0:
            return

        def helper(row, col):

            if row < 0 or col < 0 or row >= l_r or col >= l_c:
                return

            value = board[row][col]

            if board[row][col] != 'O':
                return
            else:
                board[row][col] = "1"
                helper(row - 1, col)
                helper(row + 1, col)
                helper(row, col - 1)
                helper(row, col + 1)

        for col in range(l_c):
            helper(0, col)
            helper(l_r - 1, col)

        for row in range(l_r):
            helper(row, 0)
            helper(row, l_c - 1)

        for row in range(l_r):
            for col in range(l_c):
                value = board[row][col]
                if value == "O":
                    board[row][col] = "X"
                elif value == "1":
                    board[row][col] = "O"
