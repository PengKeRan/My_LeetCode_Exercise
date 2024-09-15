"""
96. 不同的二叉搜索树
给你一个整数 n ，求恰由 n 个节点组成且节点值从 1 到 n 互不相同的 二叉搜索树 有多少种？返回满足题意的二叉搜索树的种数。
"""


class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return n
        dp = [0 for _ in range(n + 1)]
        dp[0] = 1
        dp[1] = 1
        dp[2] = 2
        for i in range(3, len(dp)):
            for num in range(1, i + 1):
                dp[i] += dp[num - 1] * dp[i - num]
        return dp[-1]


n1 = 3  # 5
n2 = 4  # 14
sol = Solution()
print(sol.numTrees(n1))
print(sol.numTrees(n2))
