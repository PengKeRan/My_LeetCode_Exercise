# 309. 买卖股票的最佳时机含冷冻期
# 给定一个整数数组prices，其中第  prices[i] 表示第 i 天的股票价格 。​
#
# 设计一个算法计算出最大利润。在满足以下约束条件下，你可以尽可能地完成更多的交易（多次买卖一支股票）:
#
# 卖出股票后，你无法在第二天买入股票 (即冷冻期为 1 天)。
# 注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # 我们目前持有一支股票，对应的「累计最大收益」记为profit[i][0]；
        # 我们目前不持有任何股票，并且处于冷冻期中，对应的「累计最大收益」记为profit[i][1]；
        # 我们目前不持有任何股票，并且不处于冷冻期中，对应的「累计最大收益」记为profit[i][2]。
        profit = [[0 for _ in range(3)] for _ in range(len(prices))]
        profit[0][0] = -prices[0]
        for i in range(1, len(prices)):
            profit[i][0] = max(profit[i-1][0], profit[i-1][2] - prices[i])
            profit[i][1] = profit[i-1][0] + prices[i]
            profit[i][2] = max(profit[i-1][1], profit[i-1][2])
        return max(profit[len(prices)-1])

sol = Solution()
prices1 = [1, 2, 3, 0, 2]
print(sol.maxProfit(prices1))
