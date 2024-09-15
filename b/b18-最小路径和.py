"""
64.最小路径和
给定一个包含非负整数的 m x n 网格 grid ，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。
说明：每次只能向下或者向右移动一步。
"""


class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        dis = [[4000000 for _ in range(len(grid[0]))] for _ in range(len(grid))]
        for i in range(len(grid) - 1, -1, -1):
            for j in range(len(grid[0]) - 1, -1, -1):
                if i == len(grid) - 1 and j == len(grid[0]) - 1:
                    dis[i][j] = grid[i][j]
                elif i == len(grid) - 1:
                    dis[i][j] = grid[i][j] + dis[i][j + 1]
                elif j == len(grid[0]) - 1:
                    dis[i][j] = grid[i][j] + dis[i + 1][j]
                else:
                    dis[i][j] = min((grid[i][j] + dis[i + 1][j]), (grid[i][j] + dis[i][j + 1]))
        return dis[0][0]


grid1 = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]  # 7
grid2 = [[1, 2, 3], [4, 5, 6]]  # 12
sol = Solution()
print(sol.minPathSum(grid1))
print(sol.minPathSum(grid2))
