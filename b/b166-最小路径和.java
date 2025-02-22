class MinPathSum {
    int[][] memo;

    public int minPathSum(int[][] grid) {
        // int m = grid.length;
        // int n = grid[0].length;
        // memo = new int[m][n];
        // for (int i = 0; i < m; i++) {
        // for (int j = 0; j < n; j++) {
        // memo[i][j] = -1;
        // }
        // }
        // memo[0][0] = grid[0][0];
        // return dp(m - 1, n - 1, grid);

        int m = grid.length;
        int n = grid[0].length;
        int[] dp = new int[n];

        dp[0] = grid[0][0];
        for (int i = 1; i < n; i++) {
            dp[i] = dp[i - 1] + grid[0][i];
        }
        for (int i = 1; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (j == 0) {
                    dp[j] = dp[j] + grid[i][j];
                } else {
                    dp[j] = Math.min(dp[j - 1], dp[j]) + grid[i][j];
                }
            }
        }
        return dp[n - 1];
    }

    // private int dp(int i, int j, int[][] grid) {
    // if (memo[i][j] != -1) {
    // return memo[i][j];
    // }
    // if (i == 0 || j == 0) {
    // memo[i][j] = i == 0 ? dp(i, j - 1, grid) + grid[i][j] : dp(i - 1, j, grid) +
    // grid[i][j];
    // return memo[i][j];
    // }
    // return grid[i][j] + Math.min(dp(i - 1, j, grid), dp(i, j - 1, grid));
    // }
}