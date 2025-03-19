class Solution {
    public int numIslands(char[][] grid) {
        int m = grid.length;
        int n = grid[0].length;
        int cnt = 0;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == '1') {
                    cnt += 1;
                    mark(grid, i, j);
                }
            }
        }
        return cnt;
    }

    private void mark(char[][] grid, int i, int j) {
        if (i < 0 || j < 0 || i >= grid.length || j >= grid[0].length || grid[i][j] != '1') {
            return;
        }
        grid[i][j] = '0';
        mark(grid, i - 1, j);
        mark(grid, i + 1, j);
        mark(grid, i, j - 1);
        mark(grid, i, j + 1);
    }
}