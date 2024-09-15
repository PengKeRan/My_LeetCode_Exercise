"""
48.旋转图像
给定一个 n×n 的二维矩阵matrix 表示一个图像。请你将图像顺时针旋转 90 度。
你必须在 原地 旋转图像，这意味着你需要直接修改输入的二维矩阵。请不要 使用另一个矩阵来旋转图像。
"""


class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        length = len(matrix)
        mid = (float(length) / 2) - 1 + 0.5
        for i in range(int(mid + 0.5)):
            for j in range(int(mid + 1)):
                x = mid - i
                y = mid - j
                temp = matrix[int(mid - x)][int(mid - y)]
                matrix[int(mid - x)][int(mid - y)] = matrix[int(mid + y)][int(mid - x)]
                matrix[int(mid + y)][int(mid - x)] = matrix[int(mid + x)][int(mid + y)]
                matrix[int(mid + x)][int(mid + y)] = matrix[int(mid - y)][int(mid + x)]
                matrix[int(mid - y)][int(mid + x)] = temp
                # matrix[int(mid - x)][int(mid - y)]
                # matrix[int(mid - y)][int(mid + x)]
                # matrix[int(mid + x)][int(mid + y)]
                # matrix[int(mid + y)][int(mid - x)]


sol = Solution()
matrix1 = [[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9]]
matrix2 = [[5, 1, 9, 11],
           [2, 4, 8, 10],
           [13, 3, 6, 7],
           [15, 14, 12, 16]]
sol.rotate(matrix1)
sol.rotate(matrix2)
print(matrix1)
# print(matrix2)
