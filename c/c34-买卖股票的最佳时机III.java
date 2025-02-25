class MaxProfit {
    public int maxProfit(int[] prices) {
        int n = prices.length;
        int buy1, buy2, sell1 = 0, sell2 = 0;
        buy1 = -prices[0];
        buy2 = -prices[0];
        for (int i = 1; i < n; i++) {
            buy1 = Math.max(buy1, -prices[i]);
            sell1 = Math.max(sell1, prices[i] - buy1);
            buy2 = Math.max(buy2, sell1 - prices[i]);
            sell2 = Math.max(sell2, prices[i] + buy2);
        }

        return Math.max(sell1, sell2);
    }
}
