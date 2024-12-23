# 289. 生命游戏


class Solution(object):
    def liveOrDie(self, board, i, j):
        row = len(board)
        col = len(board[0])
        cnt = 0
        sourround = [
            [i - 1, j - 1],
            [i - 1, j],
            [i - 1, j + 1],
            [i, j - 1],
            [i, j + 1],
            [i + 1, j - 1],
            [i + 1, j],
            [i + 1, j + 1],
        ]
        for [m, n] in sourround:
            if m < 0 or m >= row or n < 0 or n >= col:
                continue
            if board[m][n] == 1:
                cnt += 1
            if board[i][j] == 1 and cnt > 3:
                return 0
        if board[i][j] == 0 and cnt == 3:
            return 1
        if board[i][j] == 1 and (cnt < 2 or cnt > 3):
            return 0
        return board[i][j]

    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        row = len(board)
        col = len(board[0])
        temp = [[-1 for _ in range(col)] for _ in range(2)]
        for i in range(row):
            for j in range(col):
                if i == 0:
                    temp[0][j] = self.liveOrDie(board, i, j)
                else:
                    temp[1][j] = self.liveOrDie(board, i, j)
            if i >= 1:
                for k in range(col):
                    board[i - 1][k] = temp[0][k]
                    temp[0][k] = temp[1][k]
        if row <= 2:
            for i in range(row):
                for j in range(col):
                    board[i][j] = temp[i][j]
        else:
            for k in range(col):
                board[row - 1][k] = temp[1][k]


board = [[0, 1, 0]]
sol = Solution()
print(sol.gameOfLife(board))
print(board)
