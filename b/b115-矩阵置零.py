# 73. 矩阵置零
# 给定一个 m x n 的矩阵，如果一个元素为 0 ，则将其所在行和列的所有元素都设为 0 。请使用 原地 算法。


class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        row = len(matrix)
        col = len(matrix[0])
        mark_row = [0 for _ in range(row)]
        mark_col = [0 for _ in range(col)]
        for i in range(row):
            for j in range(col):
                if matrix[i][j] == 0:
                    mark_row[i] = 1
                    mark_col[j] = 1
        for i in range(row):
            for j in range(col):
                if mark_row[i] or mark_col[j]:
                    matrix[i][j] = 0


matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
sol = Solution()
print(sol.setZeroes(matrix))
