from collections import Counter


class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        row = [[0] * 10] * 9
        col = [[0] * 10] * 9
        box = [[0] * 10] * 9
        for i in range(9):
            for j in range(9):
                ch = board[i][j]
                if ch == ".":
                    continue
                cur_num = ord(ch) - ord("0")
                if (
                    row[i][cur_num]
                    or col[j][cur_num]
                    or box[(i // 3) * 3 + j // 3][cur_num]
                ):
                    return False

                row[i][cur_num] = 1
                col[j][cur_num] = 1
                box[(i // 3) * 3 + j // 3][cur_num] = 1
        return True

    #     for i in range(9):
    #         if not self.check9(board[i]) or not self.check9([row[i] for row in board]):
    #             return False

    #     for i in [0, 3, 6]:
    #         for j in [0, 3, 6]:
    #             if not self.check9(
    #                 [board[x][y] for x in range(i, i + 3) for y in range(j, j + 3)]
    #             ):
    #                 return False

    #     return True

    # def check9(self, arr):
    #     tar = Counter(["1", "2", "3", "4", "5", "6", "7", "8", "9"])
    #     for num in arr:
    #         if num == ".":
    #             continue
    #         if tar[num] == 0:
    #             return False
    #         tar[num] -= 1
    #     return True


board = [
    ["8", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"],
]
sol = Solution()
print(sol.isValidSudoku(board))
