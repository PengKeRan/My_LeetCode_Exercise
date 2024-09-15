# 79. 单词搜索
# 给定一个 m x n 二维字符网格 board 和一个字符串单词 word 。如果 word 存在于网格中，返回 true ；否则，返回 false 。
#
# 单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。

class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        n = len(word)
        row = len(board)
        col = len(board[0])
        walked = [[False for _ in range(col)] for _ in range(row)]
        directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]

        def check(r, c, k):
            if board[r][c] != word[k]:
                return False
            if k == n - 1:
                return True
            walked[r][c] = True
            for direction in directions:
                next_row = r + direction[0]
                next_col = c + direction[1]
                if next_row >= row or next_row < 0 or next_col >= col or next_col < 0:
                    continue
                if not walked[next_row][next_col]:
                    if check(next_row, next_col, k + 1):
                        return True
            walked[r][c] = False
            return False

        for i in range(row):
            for j in range(col):
                if check(i, j, 0):
                    return True

        return False


sol = Solution()
board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
word = "ABCCED"
print(sol.exist(board, word))
