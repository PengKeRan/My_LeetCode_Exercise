# 121. 买卖股票的最佳时机
# 给定一个数组 prices ，它的第 i 个元素 prices[i] 表示一支给定股票第 i 天的价格。
#
# 你只能选择 某一天 买入这只股票，并选择在 未来的某一个不同的日子 卖出该股票。设计一个算法来计算你所能获取的最大利润。
#
# 返回你可以从这笔交易中获取的最大利润。如果你不能获取任何利润，返回 0 。

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        res = 0
        small = prices[0]
        for i in range(1, len(prices)):
            if prices[i] < small:
                small = prices[i]
            if res < prices[i] - small:
                res = prices[i] - small
        return res


sol = Solution()
prices1 = [7, 1, 5, 3, 6, 4]
print(sol.maxProfit(prices1))
