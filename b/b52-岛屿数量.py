# 200. 岛屿数量
# 给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。
# 岛屿总是被水包围，并且每座岛屿只能由水平方向和/或竖直方向上相邻的陆地连接形成。
# 此外，你可以假设该网格的四条边均被水包围。

class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        def island_rm(i, j):
            grid[i][j] = "0"
            if i - 1 >= 0 and grid[i - 1][j] == "1":
                island_rm(i - 1, j)
            if i + 1 < len(grid) and grid[i + 1][j] == "1":
                island_rm(i + 1, j)
            if j - 1 >= 0 and grid[i][j - 1] == "1":
                island_rm(i, j - 1)
            if j + 1 < len(grid[0]) and grid[i][j + 1] == "1":
                island_rm(i, j + 1)
            return

        island = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    island += 1
                    island_rm(i, j)
        return island


sol = Solution()
grid = [
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"]
]
print(sol.numIslands(grid))
