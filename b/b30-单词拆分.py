"""
139. 单词拆分
给你一个字符串 s 和一个字符串列表 wordDict 作为字典。请你判断是否可以利用字典中出现的单词拼接出 s 。
注意：不要求字典中出现的单词全部都使用，并且字典中的单词可以重复使用。
"""


class Solution(object):
    good = set()

    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        dp = [False for _ in range(len(s)+1)]
        for i in range(len(s)+1):
            for j in range(0, i):
                if s[0:i] in wordDict:
                    dp[i] = True
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
        return dp[-1]

        # if len(s) == s.count('*'):
        #     return True
        # flag = False
        # for i in range(len(wordDict)):
        #     if wordDict[i] in s or wordDict[i] in self.good:
        #         flag = True
        # if not flag:
        #     return False
        # flag = False
        # for i in range(len(wordDict)):
        #     if wordDict[i] in s:
        #         s1 = s.replace(wordDict[i], "*", 1)
        #         flag = flag or self.wordBreak(s1, wordDict)
        # if flag:
        #     self.good.add(s.replace('*'))
        # if len(self.good)!=0:
        #     print(self.good)
        # return flag


sol = Solution()
s1 = "leetcode"
wordDict1 = ["leet","code"]
print(sol.wordBreak(s1, wordDict1))
