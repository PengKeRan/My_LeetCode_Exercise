# 54. 螺旋矩阵
# 提示
# 给你一个 m 行 n 列的矩阵 matrix ，请按照 顺时针螺旋顺序 ，返回矩阵中的所有元素。


class Solution(object):
    def valid(self, pos, matrix):
        if pos[0] < 0 or pos[0] >= len(matrix):
            return False
        if pos[1] < 0 or pos[1] >= len(matrix[0]):
            return False
        if matrix[pos[0]][pos[1]] == 101:
            return False
        return True

    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        res = []
        pos = [0, 0]
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        d = 0
        while True:
            if not self.valid(
                [
                    pos[0] + directions[d][0],
                    pos[1] + directions[d][1],
                ],
                matrix,
            ):
                d = (d + 1) % 4

                if not self.valid(
                    [
                        pos[0] + directions[d][0],
                        pos[1] + directions[d][1],
                    ],
                    matrix,
                ):
                    res.append(matrix[pos[0]][pos[1]])
                    return res

            res.append(matrix[pos[0]][pos[1]])
            matrix[pos[0]][pos[1]] = 101
            pos = [pos[0] + directions[d][0], pos[1] + directions[d][1]]


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
sol = Solution()
print(sol.spiralOrder(matrix))
