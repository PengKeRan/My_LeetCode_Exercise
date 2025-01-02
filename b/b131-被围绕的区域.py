# 130. 被围绕的区域
class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        n = len(board)
        m = len(board[0])
        for i in range(n):
            for j in range(m):
                if i == 0 or j == 0 or i == n - 1 or j == m - 1:
                    if board[i][j] == "O":
                        self.spread(board, i, j)
        self.fresh(board)
        return board

    def fresh(self, board):
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "O":
                    board[i][j] = "X"
                if board[i][j] == "O2":
                    board[i][j] = "O"

    def spread(self, board, i, j):
        if not self.legit(board, i, j) or board[i][j] != "O":
            return
        if board[i][j] == "O":
            board[i][j] = "O2"
        self.spread(board, i - 1, j)
        self.spread(board, i, j - 1)
        self.spread(board, i + 1, j)
        self.spread(board, i, j + 1)
        return

    def legit(self, board, i, j):
        if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]):
            return False
        return True


board = [
    ["O", "O", "O", "O", "X", "X"],
    ["O", "O", "O", "O", "O", "O"],
    ["O", "X", "O", "X", "O", "O"],
    ["O", "X", "O", "O", "X", "O"],
    ["O", "X", "O", "X", "O", "O"],
    ["O", "X", "O", "O", "O", "O"],
]
print(Solution().solve(board))
