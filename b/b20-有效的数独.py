"""
36. 有效的数独
请你判断一个9 x 9 的数独是否有效。只需要 根据以下规则 ，验证已经填入的数字是否有效即可。
数字1-9在每一行只能出现一次。
数字1-9在每一列只能出现一次。
数字1-9在每一个以粗实线分隔的3x3宫内只能出现一次。（请参考示例图）
"""


class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        # 9行+9列+9块,用27个数组表示
        analyse = [[0 for i in range(9)] for _ in range(27)]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == '.':
                    continue
                num = int(board[i][j])
                if analyse[i][num - 1] == 1 or analyse[9 + j][num - 1] == 1 or \
                        analyse[18 + (i // 3) * 3 + (j // 3)][num - 1] == 1:
                    return False
                analyse[i][num - 1] += 1
                analyse[9 + j][num - 1] += 1
                analyse[18 + (i // 3) * 3 + (j // 3)][num - 1] += 1
        return True


board1 = [["5", "3", ".", ".", "7", ".", ".", ".", "."],
          ["6", ".", ".", "1", "9", "5", ".", ".", "."],
          [".", "9", "8", ".", ".", ".", ".", "6", "."],
          ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
          ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
          ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
          [".", "6", ".", ".", ".", ".", "2", "8", "."],
          [".", ".", ".", "4", "1", "9", ".", ".", "5"],
          [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
board2 = [["8", "3", ".", ".", "7", ".", ".", ".", "."],
          ["6", ".", ".", "1", "9", "5", ".", ".", "."],
          [".", "9", "8", ".", ".", ".", ".", "6", "."],
          ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
          ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
          ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
          [".", "6", ".", ".", ".", ".", "2", "8", "."],
          [".", ".", ".", "4", "1", "9", ".", ".", "5"],
          [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
board3 = [[".", ".", ".", ".", "5", ".", ".", "1", "."],
          [".", "4", ".", "3", ".", ".", ".", ".", "."],
          [".", ".", ".", ".", ".", "3", ".", ".", "1"],
          ["8", ".", ".", ".", ".", ".", ".", "2", "."],
          [".", ".", "2", ".", "7", ".", ".", ".", "."],
          [".", "1", "5", ".", ".", ".", ".", ".", "."],
          [".", ".", ".", ".", ".", "2", ".", ".", "."],
          [".", "2", ".", "9", ".", ".", ".", ".", "."],
          [".", ".", "4", ".", ".", ".", ".", ".", "."]]
sol = Solution()
# print(sol.isValidSudoku(board1))  # T
# print(sol.isValidSudoku(board2))  # F
print(sol.isValidSudoku(board3))  # F
