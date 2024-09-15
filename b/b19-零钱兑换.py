"""
322.零钱兑换
给你一个整数数组 coins ，表示不同面额的硬币；以及一个整数 amount ，表示总金额。
计算并返回可以凑成总金额所需的 最少的硬币个数 。如果没有任何一种硬币组合能组成总金额，返回-1 。
你可以认为每种硬币的数量是无限的。
"""


class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        df = [99999999] * (amount+1)
        df[0]=0
        for coin in coins:
            for i in range(coin,amount+1):
                df[i] = min(df[i-coin]+1,df[i])
        return df[amount] if df[amount] != 99999999 else -1


        # def dfs(coins, amount):
        #     arr = []
        #     count = 999
        #     flag = False
        #     if amount == 0:
        #         return 0
        #     if amount < coins[0]:
        #         return -1
        #     if amount in coins:
        #         return 1
        #     if path[amount] != -1:
        #         return path[amount]
        #     for i in range(len(coins)):
        #         res = self.coinChange(coins, amount - coins[i])
        #         if res == -1:
        #             continue
        #         arr.append(self.coinChange(coins, amount - coins[i]) + 1)
        #     for i in range(len(arr)):
        #         if arr[i] > 0 and arr[i] < count:
        #             count = arr[i]
        #     path[amount] = -1 if count == 999 else count
        #     print(amount)
        #     return path[amount]
        #
        # if (amount < 1):
        #     return 0
        # path = [-1] * (amount + 1)
        # return dfs(coins, amount)


coins1 = [1]
amount1 = 10000
coins2 = [2]
amount2 = 3
coins3 = [1, 2147483647]

amount3 = 2
sol = Solution()
print(sol.coinChange(coins1, amount1))  # 3
# print(sol.coinChange(coins2, amount2))  # -1
# print(sol.coinChange(coins3, amount3))  # 0
