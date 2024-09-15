"""
221. 最大正方形
在一个由 '0' 和 '1' 组成的二维矩阵内，找到只包含 '1' 的最大正方形，并返回其面积。
"""


class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        square = [[0 for j in range(len(matrix[0]))] for i in range(len(matrix))]

        def near(i, j):
            if matrix[i][j] == '0':
                return 0
            if i == len(matrix) - 1 or j == len(matrix[0]) - 1:
                return 1
            return min(square[i][j + 1], square[i + 1][j], square[i + 1][j + 1]) + 1

        for i in range(len(matrix) - 1, -1, -1):
            for j in range(len(matrix[0]) - 1, -1, -1):
                square[i][j] = near(i, j)
        max_length = max(max(square[i]) for i in range(len(square)))
        return max_length ** 2

        # max_length = 0
        # valid = False
        # for i in range(len(matrix)):
        #     for j in range(len(matrix[0])):
        #         if matrix[i][j] == '0':
        #             continue
        #         max_length = max(max_length, 1)
        #         for k in range(1, len(matrix[0]) - j):
        #             if i < len(matrix) - k and j < len(matrix[0]) - k:
        #                 for m in range(0, k+1):
        #                     if matrix[i + k][j + m] == '0' or matrix[i + m][j + k] == '0':
        #                         valid = False
        #                         break
        #                     valid = True
        #                 if valid:
        #                     max_length = max(max_length, k + 1)
        #                 else:
        #                     break
        # return max_length ** 2


matrix1 = [["1", "0", "1", "0", "0"],
           ["1", "0", "1", "1", "1"],
           ["1", "1", "1", "1", "1"],
           ["1", "0", "0", "1", "0"]]
matrix2 = [["0", "1"], ["1", "0"]]
matrix3 = [["0", "1", "1", "0", "0", "1", "0", "1", "0", "1"],
           ["0", "0", "1", "0", "1", "0", "1", "0", "1", "0"],
           ["1", "0", "0", "0", "0", "1", "0", "1", "1", "0"],
           ["0", "1", "1", "1", "1", "1", "1", "0", "1", "0"],
           ["0", "0", "1", "1", "1", "1", "1", "1", "1", "0"],
           ["1", "1", "0", "1", "0", "1", "1", "1", "1", "0"],
           ["0", "0", "0", "1", "1", "0", "0", "0", "1", "0"],
           ["1", "1", "0", "1", "1", "0", "0", "1", "1", "1"],
           ["0", "1", "0", "1", "1", "0", "1", "0", "1", "1"]]

sol = Solution()
print(sol.maximalSquare(matrix1))
print(sol.maximalSquare(matrix2))
print(sol.maximalSquare(matrix3))
