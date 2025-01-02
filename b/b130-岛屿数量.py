# 200. 岛屿数量
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    self.spread(grid, i, j)
                    res += 1
        return res

    def spread(self, grid, i, j):
        if not self.legit(grid, i, j) or grid[i][j] != "1":
            return
        grid[i][j] = "2"
        self.spread(grid, i - 1, j)
        self.spread(grid, i, j - 1)
        self.spread(grid, i + 1, j)
        self.spread(grid, i, j + 1)

    def legit(self, grid, i, j):
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]):
            return False
        return True


grid = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"],
]
print(Solution().numIslands(grid))
