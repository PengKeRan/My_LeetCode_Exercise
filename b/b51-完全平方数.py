# 279. 完全平方数
# 给你一个整数n ，返回和为n的完全平方数的最少数量 。
#
# 完全平方数
# 是一个整数，其值等于另一个整数的平方；换句话说，其值等于一个整数自乘的积。例如，1、4、9和16都是完全平方数，而3和11不是。
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        m = 1
        coins = []
        while True:
            if m * m > n:
                break
            coins.append(m*m)
            if m * m == n:
                break
            m += 1
        top_limit = [0 for i in range(len(coins))]
        for i in range(len(coins)):
            top_limit[i] = n // coins[i]

        min_coin = [n for _ in range(n+1)]
        min_coin[0] = 0
        for i in range(len(coins)):
            for j in range(coins[i], n+1):
                min_coin[j] = min(min_coin[j], min_coin[j-coins[i]]+1)
        return min_coin[n]

sol = Solution()
n = 13
print(sol.numSquares(n))
