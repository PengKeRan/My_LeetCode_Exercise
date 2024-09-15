"""
剑指 Offer 14- I. 剪绳子
给你一根长度为 n 的绳子，请把绳子剪成整数长度的 m 段（m、n都是整数，n>1并且m>1），每段绳子的长度记为 k[0],k[1]...k[m-1] 。
请问 k[0]*k[1]*...*k[m-1] 可能的最大乘积是多少？
例如，当绳子的长度是8时，我们把它剪成长度分别为2、3、3的三段，此时得到的最大乘积是18。

343. 整数拆分
给定一个正整数 n ，将其拆分为 k 个 正整数 的和（ k >= 2 ），并使这些整数的乘积最大化。
返回 你可以获得的最大乘积 。

2 <= n <= 58
"""


class Solution(object):
    def cuttingRope(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 2:
            return 1
        if n == 3:
            return 2
        num3 = n // 3
        num2 = 0
        rest = n % 3
        result = 1
        if rest == 1:
            num3 -= 1
            num2 = 2
        if rest == 2:
            num2 = 1

        for i in range(0, num3):
            result *= 3

        for i in range(0, num2):
            result *= 2

        return result

sol = Solution()
print(sol.cuttingRope(2))
print(sol.cuttingRope(10))
