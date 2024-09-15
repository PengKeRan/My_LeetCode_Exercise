"""
72. 编辑距离
给你两个单词 word1和word2， 请返回将word1转换成word2 所使用的最少操作数。
你可以对一个单词进行如下三种操作：
插入一个字符
删除一个字符
替换一个字符
"""


class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        dp = [[9999 for _ in range(len(word2) + 1)] for _ in range(len(word1) + 1)]
        for i in range(len(word1) + 1):
            dp[i][0] = i
        for j in range(len(word2) + 1):
            dp[0][j] = j
        for i in range(1, len(word1) + 1):
            for j in range(1, len(word2) + 1):
                change = 1
                if word1[i-1] == word2[j-1]:
                    change = 0
                dp[i][j] = min(dp[i - 1][j] + 1, dp[i][j - 1] + 1, dp[i - 1][j - 1] + change)
        return dp[len(word1)][len(word2)]


word11 = "a"
word12 = "a"
word21 = "intention"
word22 = "execution"
sol = Solution()
print(sol.minDistance(word11, word12))
print(sol.minDistance(word21, word22))
