# 14. 最长公共前缀
# 编写一个函数来查找字符串数组中的最长公共前缀。
# 如果不存在公共前缀，返回空字符串 ""。


class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        ans = strs[0]
        for s in strs:
            temp = self.prefix(ans, s)
            if len(temp) < len(ans):
                ans = temp
            if len(ans) == 0:
                return ""
        return ans

    def prefix(self, s1, s2):
        cnt = 0
        for i in range(min(len(s1), len(s2))):
            if s1[i] == s2[i]:
                cnt += 1
            else:
                return s1[0:cnt]
        return s1 if len(s1) < len(s2) else s2


print(Solution().longestCommonPrefix(["flower", "flow", "flight"]))
