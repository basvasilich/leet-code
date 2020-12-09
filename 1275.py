# https://leetcode.com/problems/find-winner-on-a-tic-tac-toe-game/

from typing import List


class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        board = [[None, None, None] for _ in range(3)]

        def check_board(board):
            if board[0][0] and board[0][0] == board[1][1] == board[2][2]:
                return board[0][0]

            if board[0][0] and board[0][0] == board[0][1] == board[0][2]:
                return board[0][0]

            if board[1][0] and board[1][0] == board[1][1] == board[1][2]:
                return board[1][0]

            if board[2][0] and board[2][0] == board[2][1] == board[2][2]:
                return board[2][0]

            if board[0][0] and board[0][0] == board[1][0] == board[2][0]:
                return board[0][0]

            if board[1][1] and board[0][1] == board[1][1] == board[2][1]:
                return board[1][1]

            if board[0][2] and board[0][2] == board[1][2] == board[2][2]:
                return board[0][2]

            if board[2][0] and board[2][0] == board[1][1] == board[0][2]:
                return board[2][0]

            return "P/D"

        for index in range(len(moves)):
            [row, col] = moves[index]

            board[row][col] = "A" if index % 2 == 0 else "B"

        result = check_board(board)

        if len(result) == 1:
            return result
        elif len(moves) == 9:
            return "Draw"
        else:
            return "Pending"
