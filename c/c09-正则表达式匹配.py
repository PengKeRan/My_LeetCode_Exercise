# 10. 正则表达式匹配
# 给你一个字符串 s 和一个字符规律 p，请你来实现一个支持 '.' 和 '*' 的正则表达式匹配。
# '.' 匹配任意单个字符
# '*' 匹配零个或多个前面的那一个元素
# 所谓匹配，是要涵盖 整个 字符串 s的，而不是部分字符串。


class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        # memo = dict()
        # def match(s, p):
        #     print(f"match:{s}--{p}")
        #     if s + "-" + p in memo.keys():
        #         return memo[s + "-" + p]
        #     if not s and not p:
        #         return True
        #     if s and not p:
        #         return False
        #     if not s and p:
        #         if len(p) == 1:
        #             return False
        #         if p[1] == "*":
        #             memo[s + "-" + p] = match(s, p[2:])
        #             return memo[s + "-" + p]
        #         return False

        #     if len(p) == 1:
        #         if s[0] != p[0] and p[0] != ".":
        #             memo[s + "-" + p] = False
        #             return memo[s + "-" + p]
        #         memo[s + "-" + p] = match(s[1:], p[1:])
        #         return memo[s + "-" + p]
            
        #     if p[1] == "*":
        #         if s[0] != p[0] and p[0] != ".":
        #             memo[s + "-" + p] = match(s,p[2:])
        #             return memo[s + "-" + p]
                
        #         ch_len = 1
        #         if p[0] != ".":
        #             for k in range(1, len(s)):
        #                 if s[k] == s[k-1]:
        #                     ch_len += 1
        #                 else:
        #                     break
        #         else:
        #             ch_len = len(s)
        #         for m in range(ch_len):
        #             if match(s[m:], p[2:]):
        #                 memo[s + "-" + p] = True
        #                 return memo[s + "-" + p]
        #         memo[s + "-" + p] = match(s[ch_len:], p)
        #         return memo[s + "-" + p]
            
        #     if s[0] == p[0] or p[0] == ".":
        #         memo[s + "-" + p] = match(s[1:], p[1:])
        #         return memo[s + "-" + p]
        #     memo[s + "-" + p] = False
        #     return memo[s + "-" + p]


        # return match(s, p)

        # 动态规划
        def match(i, j):
            if i == 0 :
                return False
            if p[j-1] == ".":
                return True
            return s[i-1] == p[j-1]

        m = len(s)
        n = len(p)
        dp = [[False for _ in range(n+1)] for _ in range(m+1)]
        dp[0][0] = True

        for i in range(0, m+1):
            for j in range(1, n+1):
                if p[j-1] == "*":
                    dp[i][j] = dp[i][j-2] or (match(i,j-1) and dp[i-1][j])
                else:
                    dp[i][j] = match(i,j) and dp[i-1][j-1]

        return dp[m][n]

sol = Solution()
# s = "aa"
# p = "a"
# s = "aa"
# p = "a*"
# s = "ab"
# p = ".*"
s = "aab"
p = "a*b"
# s = "ab"
# p = ".*c"
print(sol.isMatch(s, p))
