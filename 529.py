from typing import List


class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        def getAdj(i, j):
            result_e = []
            result_m = []

            def getType(i, j):
                if board[i][j] == 'M':
                    result_m.append((i, j))
                elif board[i][j] == 'E':
                    result_e.append((i, j))

            if i > 0 and j > 0:
                getType(i - 1, j - 1)
            if i > 0:
                getType(i - 1, j)
            if j > 0:
                getType(i, j - 1)

            if i < len(board) - 1 and j < len(board[0]) - 1:
                getType(i + 1, j + 1)
            if i < len(board) - 1:
                getType(i + 1, j)
            if j < len(board[0]) - 1:
                getType(i, j + 1)

            if i < len(board) - 1 and j > 0:
                getType(i + 1, j - 1)
            if i > 0 and j < len(board[0]) - 1:
                getType(i - 1, j + 1)

            return result_e, result_m

        def getNum(i, j):

            if board[i][j] == 'M':
                return ('X', [])
            adj_e, adj_m = getAdj(i, j)
            return (str(len(adj_m)) if len(adj_m) > 0 else 'B', adj_e)

        def handleClick(i, j):
            click_result, adj_e = getNum(i, j)
            if click_result == 'X':
                board[i][j] = click_result
            elif click_result == 'B':
                board[i][j] = click_result
                for i_n, j_n in adj_e:
                    handleClick(i_n, j_n)
            else:
                board[i][j] = click_result

            return board

        i, j = click
        return handleClick(i, j)
