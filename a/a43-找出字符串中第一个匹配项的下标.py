# 28. 找出字符串中第一个匹配项的下标
# 给你两个字符串 haystack 和 needle ，请你在 haystack 字符串中找出 needle 字符串的第一个匹配项的下标（下标从 0 开始）。如果 needle 不是 haystack 的一部分，则返回  -1 。


class Solution(object):

    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        # KMP
        n = len(needle)
        next_arr = [0] * n
        j = 0  # j表示最长前缀后缀的长度
        for i in range(1, n):
            while j > 0 and needle[i] != needle[j]:
                j = next_arr[j - 1]  # 如果字符不匹配，就回溯到前一个最长前后缀的索引
            if needle[i] == needle[j]:
                j += 1
            next_arr[i] = j

        j = 0
        for i in range(len(haystack)):
            while j > 0 and haystack[i] != needle[j]:
                j = next_arr[j - 1]
            if haystack[i] == needle[j]:
                j += 1
            if j == n:
                return i - n + 1

        return -1

        # 动态规划
        # n = len(haystack)
        # m = len(needle)
        # dp = [[0] * (m + 1) for _ in range(n + 1)]
        # for i in range(1, n + 1):
        #     for j in range(1, m + 1):
        #         if haystack[i - 1] == needle[j - 1]:
        #             dp[i][j] = dp[i - 1][j - 1] + 1
        #         else:
        #             dp[i][j] = 0
        #         if dp[i][j] == m:
        #             return i - m
        # return -1


sol = Solution()
haystack = "sadbutsad"
needle = "sad"
print(sol.strStr(haystack, needle))
