class CoinChange {
    public int coinChange(int[] coins, int amount) {
        int n = coins.length;
        int[] res = new int[amount + 1];
        int i, j;
        for (i = 1; i < amount + 1; i++) {
            res[i] = amount + 1;
        }
        for (i = 1; i < amount + 1; i++) {
            for (j = 0; j < n; j++) {
                if (coins[j] > i) {
                    continue;
                }
                res[i] = Math.min(res[i], res[i - coins[j]] + 1);
            }
        }

        return res[amount] == amount + 1 ? -1 : res[amount];
    }
}